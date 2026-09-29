from datetime import date, datetime, timezone
from contextlib import redirect_stdout
from io import StringIO
import copy
from pathlib import Path
import sys
import types
import unittest
from unittest.mock import patch

sys.modules.setdefault('yfinance', types.SimpleNamespace())
sys.path.insert(0, str(Path(__file__).resolve().parent))
import update_prices as p
import update_verdicts as v
import validate_prices as vp
import validate_verdicts as vv
from price_basis import split_adjusted_price


class SplitBasisTests(unittest.TestCase):
    def setUp(self):
        self.report = {'id':'kioxia-2026', 'priceSymbol':'285A.T', 'priceAsOf':'2026-07-31',
                       'chainLayer':'memory', 'stance':'cautious', 'conviction':'medium',
                       'stanceHistory':[{'date':'2026-07-31','price':46500,'stance':'cautious','conviction':'medium'}]}
        self.events = [{'date':'2026-09-29','ratio':3.0}]
        self.quotes = [p.PriceQuote(date(2026,7,31),15500),p.PriceQuote(date(2026,9,25),18593.333984375),
                       p.PriceQuote(date(2026,9,28),17780),p.PriceQuote(date(2026,9,29),17215)]
        self.observed = datetime(2026,9,29,1,35,tzinfo=timezone.utc)
        self.benchmarks = {'SMH':v.BenchmarkSeries('SMH',(p.PriceQuote(date(2026,7,31),100),p.PriceQuote(date(2026,9,28),111)))}

    def entry(self):
        with patch.object(p,'fetch_quotes',return_value=(self.quotes,'JPY',self.events)):
            entries, failed = p.build_price_entries([self.report],self.observed,{})
        self.assertEqual(failed,0)
        return entries[0]

    def test_intraday_split_changes_basis_without_including_intraday_price(self):
        entry=self.entry()
        self.assertEqual(entry['lastDate'],'2026-09-28')
        self.assertEqual(entry['lastClose'],17780)
        self.assertEqual(entry['basePrice'],15500)
        self.assertEqual(entry['changePct'],14.7)
        self.assertEqual(entry['splitEvents'],self.events)
        self.assertEqual(entry['priceBasisDate'],'2026-09-29')

    def test_verdict_and_validator_use_same_basis_preserving_recorded_stance(self):
        original=copy.deepcopy(self.report)
        price=self.entry()
        out=v.open_call_entry(self.report,price,self.benchmarks,'SMH',date(2026,9,29))
        self.assertEqual(out['priceAtStance'],15500)
        self.assertEqual(out['recordedPriceAtStance'],46500)
        self.assertEqual(out['changePct'],14.7)
        self.assertEqual(out['relativePct'],3.7)
        self.assertEqual(self.report,original)
        state=vv.OpenEntryValidationState({'kioxia-2026'},set(),{'kioxia-2026':price},{'default':'SMH','symbols':{'SMH':{}}},{'kioxia-2026':self.report})
        vv.validate_open_entry(out,0,state)
        out.update(priceAtStance=46500,changePct=-61.8,relativePct=-72.8,bookRelativePct=-72.8)
        state.seen.clear()
        with redirect_stdout(StringIO()),self.assertRaises(SystemExit):
            vv.validate_open_entry(out,0,state)

    def test_partially_adjusted_history_is_not_published_as_crash(self):
        bad=[p.PriceQuote(date(2026,7,31),46500),p.PriceQuote(date(2026,9,25),55780),p.PriceQuote(date(2026,9,28),17780)]
        with self.assertRaises(p.PriceDataUnavailable):
            p.build_ok_entry(self.report,bad,date(2026,9,28),'JPY')

    def test_split_metadata_detects_gradual_or_sparse_anchor_mismatch(self):
        bad=[p.PriceQuote(date(2026,7,31),46500),p.PriceQuote(date(2026,8,31),31000),p.PriceQuote(date(2026,9,28),17780)]
        with self.assertRaisesRegex(p.PriceDataUnavailable,'split basis'):
            p.build_ok_entry(self.report,bad,date(2026,9,29),'JPY',split_events=self.events)

    def test_validator_rejects_internally_consistent_wrong_anchor(self):
        entry=self.entry();entry.update(basePrice=46500,changePct=-61.8,status='carried-forward')
        with redirect_stdout(StringIO()),self.assertRaises(SystemExit):
            vp.validate_prices_data({'generatedAt':'2026-09-29','entries':[entry]},[self.report])

    def test_failure_preserves_whole_previous_basis(self):
        previous=self.entry()
        with patch.object(p,'fetch_quotes',side_effect=RuntimeError('offline')):
            entries,failed=p.build_price_entries([self.report],datetime(2026,9,30,1,tzinfo=timezone.utc),{'kioxia-2026':previous})
        self.assertEqual(failed,1)
        for key in ('splitEvents','priceBasisDate','basePrice','lastClose','changePct'):
            self.assertEqual(entries[0][key],previous[key])

    def test_no_raw_anchor_fallback_when_history_has_split(self):
        with patch.object(p,'fetch_quotes',return_value=(self.quotes[1:],'JPY',self.events)),patch.object(p,'fetch_nasdaq_anchor_quote') as fallback:
            entries,failed=p.build_price_entries([self.report],self.observed,{})
        self.assertEqual(failed,1);self.assertEqual(entries[0]['status'],'missing');fallback.assert_not_called()

    def test_split_after_window_cancels_in_closed_return(self):
        r=copy.deepcopy(self.report);r['stanceHistory'].append({'date':'2026-09-28','price':53340,'stance':'cautious','conviction':'medium'})
        before=v.closed_interval_entries(r,self.benchmarks,'SMH')[0]
        after=v.closed_interval_entries(r,self.benchmarks,'SMH',self.entry())[0]
        self.assertEqual(before['changePct'],after['changePct'])
        self.assertEqual(after['startPrice'],15500);self.assertEqual(after['endPrice'],17780)

    def test_reverse_multiple_splits_and_same_day_boundary(self):
        events=[{'date':'2026-08-01','ratio':3},{'date':'2026-09-01','ratio':0.5}]
        self.assertEqual(split_adjusted_price(150,'2026-07-31',events,'2026-09-29'),100)
        self.assertEqual(split_adjusted_price(150,'2026-08-01',events,'2026-09-29'),300)
        for invalid in ([{'date':'2026-10-01','ratio':3}],events+events,[{'date':'2026-08-01','ratio':True}]):
            with self.assertRaises(ValueError):split_adjusted_price(150,'2026-07-31',invalid,'2026-09-29')

    def test_missing_known_split_preserves_last_verified_snapshot(self):
        previous=self.entry()
        with patch.object(p,'fetch_quotes',return_value=(self.quotes,'JPY',[])):
            entries,failed=p.build_price_entries([self.report],self.observed,{'kioxia-2026':previous})
        self.assertEqual(failed,1)
        self.assertEqual(entries[0]['splitEvents'],self.events)

    def test_action_row_without_price_is_not_lost(self):
        class History:
            empty=False
            def iterrows(self):
                return iter([(datetime(2026,7,31),{'Close':15500,'Stock Splits':0}),
                             (datetime(2026,9,29),{'Close':float('nan'),'Stock Splits':3})])
        ticker=types.SimpleNamespace(history=lambda **kw:History(),fast_info={'currency':'JPY'})
        with patch.object(p.yf,'Ticker',return_value=ticker,create=True):
            quotes,currency,events=p.fetch_quotes('285A.T',date(2026,7,31),date(2026,9,29),include_splits=True)
        self.assertEqual(len(quotes),1)
        self.assertEqual(events,self.events)

    def test_preclose_snapshot_passes_date_status_validator(self):
        entry=self.entry()
        self.assertEqual(entry['status'],'carried-forward')
        vp.validate_prices_data({'generatedAt':'2026-09-29','entries':[entry]},[self.report])

if __name__=='__main__':unittest.main()

