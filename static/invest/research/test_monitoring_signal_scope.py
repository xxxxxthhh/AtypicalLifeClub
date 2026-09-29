import copy
import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO
import validate_coverage_map as v

class MonitoringSignalScopeTests(unittest.TestCase):
    def setUp(self):
        self.reports=[{'id':'example','monitoring':[{'id':'returns'}]}]
        self.signal={'id':'event','date':'2026-09-29','title':{'zh':'回购','en':'Buyback'},'detail':{'zh':'已执行','en':'Executed'},'scope':'report-monitoring','crossChecks':[],'reportIds':['example'],'monitoringRefs':['example:returns']}
    def validate(self, signal):
        with patch.object(v,'load_json',return_value=[signal]):v.validate_signals({'existing-rule'},self.reports)
    def test_report_only_event_does_not_invent_cross_company_rule(self):
        self.validate(self.signal)
    def test_orphan_unscoped_and_unknown_links_fail_closed(self):
        variants=[dict(scope=None),dict(reportIds=[]),dict(monitoringRefs=[]),dict(monitoringRefs=['example:missing']),dict(reportIds=['unknown'])]
        for change in variants:
            with self.subTest(change=change),redirect_stdout(StringIO()),self.assertRaises(SystemExit):self.validate(dict(self.signal,**change))
    def test_normal_cross_company_event_still_requires_known_rule(self):
        x=copy.deepcopy(self.signal);x.pop('scope');x['crossChecks']=['existing-rule'];self.validate(x)
        x['crossChecks']=['invented-rule']
        with redirect_stdout(StringIO()),self.assertRaises(SystemExit):self.validate(x)
