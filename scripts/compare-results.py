import argparse
import json
import sys
from benchmark_lib import load, compare

p=argparse.ArgumentParser(description='在环境与负载一致时比较两组基准数据')
p.add_argument('before'); p.add_argument('after'); args=p.parse_args()
try:
    print(json.dumps(compare(load(args.before),load(args.after)),ensure_ascii=False,indent=2,allow_nan=False))
except (ValueError,OSError,TypeError,KeyError,OverflowError) as e:
    print(f'错误：{e}',file=sys.stderr); sys.exit(1)
