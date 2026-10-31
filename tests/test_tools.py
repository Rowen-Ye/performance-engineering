import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / 'scripts'

class ToolsTests(unittest.TestCase):
    def run_tool(self, name, *args):
        return subprocess.run([sys.executable, str(TOOLS / name), *map(str,args)], capture_output=True, text=True)

    def data(self, samples, context=None):
        return {'context': context or {'workload':'demo','hardware':'simulation','version':'1'}, 'metrics': {'latency': {'unit':'ms','direction':'lower','samples':samples}}}

    def test_statistics_and_comparison(self):
        with tempfile.TemporaryDirectory() as d:
            a,b = Path(d)/'a.json',Path(d)/'b.json'
            a.write_text(json.dumps(self.data([10,20,30])))
            b.write_text(json.dumps(self.data([5,10,15])))
            result=self.run_tool('analyze-benchmark.py',a)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertEqual(json.loads(result.stdout)['metrics']['latency']['p95'],29)
            result=self.run_tool('compare-results.py',a,b)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertEqual(json.loads(result.stdout)['metrics']['latency']['improvement_pct'],50)
            result=self.run_tool('visualize-performance.py',a)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertIn('<svg',result.stdout)

    def test_invalid_document_has_readable_error(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'bad.json';p.write_text('[]')
            result=self.run_tool('analyze-benchmark.py',p)
            self.assertNotEqual(result.returncode,0)
            self.assertNotIn('Traceback',result.stderr)
            self.assertIn('错误',result.stderr)

    def test_invalid_samples(self):
        for samples in ([],[float('nan')],[-1],[True],['1']):
            with self.subTest(samples=samples), tempfile.TemporaryDirectory() as d:
                p=Path(d)/'bad.json'; p.write_text(json.dumps(self.data(samples)))
                self.assertNotEqual(self.run_tool('analyze-benchmark.py',p).returncode,0)

    def test_mismatch_and_zero(self):
        with tempfile.TemporaryDirectory() as d:
            a,b=Path(d)/'a.json',Path(d)/'b.json'
            a.write_text(json.dumps(self.data([0])))
            b.write_text(json.dumps(self.data([1])))
            r=self.run_tool('compare-results.py',a,b)
            self.assertEqual(r.returncode,0,r.stderr)
            self.assertIsNone(json.loads(r.stdout)['metrics']['latency']['improvement_pct'])
            b.write_text(json.dumps(self.data([1],{'workload':'different'})))
            self.assertNotEqual(self.run_tool('compare-results.py',a,b).returncode,0)

    def test_comparison_rejects_units_and_metric_changes(self):
        with tempfile.TemporaryDirectory() as d:
            a,b=Path(d)/'a.json',Path(d)/'b.json'
            a.write_text(json.dumps(self.data([1,2])))
            for field,value in [('unit','seconds'),('direction','higher')]:
                changed=self.data([1,2]); changed['metrics']['latency'][field]=value
                b.write_text(json.dumps(changed))
                self.assertNotEqual(self.run_tool('compare-results.py',a,b).returncode,0)
            changed=self.data([1]); changed['metrics']['extra']=changed['metrics']['latency']
            b.write_text(json.dumps(changed))
            self.assertNotEqual(self.run_tool('compare-results.py',a,b).returncode,0)

if __name__=='__main__': unittest.main()
