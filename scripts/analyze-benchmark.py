import argparse
import json
import sys
from benchmark_lib import load, summarize

p=argparse.ArgumentParser(description='汇总基准 JSON 描述统计')
p.add_argument('input'); args=p.parse_args()
try:
    print(json.dumps(summarize(load(args.input)),ensure_ascii=False,indent=2,allow_nan=False))
except (ValueError,OSError,TypeError,KeyError,OverflowError) as e:
    print(f'错误：{e}',file=sys.stderr); sys.exit(1)
