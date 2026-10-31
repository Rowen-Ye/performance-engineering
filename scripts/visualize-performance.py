import argparse
import html
import sys
from benchmark_lib import load, summarize

p=argparse.ArgumentParser(description='输出独立 SVG，每项指标按自身最大值缩放，不跨指标比较')
p.add_argument('input'); args=p.parse_args()
try:
    data=summarize(load(args.input)); rows=list(data['metrics'].items())
    print(f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{100+len(rows)*80}" viewBox="0 0 960 {100+len(rows)*80}">')
    print('<rect width="100%" height="100%" fill="white"/><text x="20" y="30" font-size="18">描述统计：均值；每行独立归一化，不代表优化收益</text>')
    for i,(name,m) in enumerate(rows):
        y=80+i*80; width=400*m['mean']/m['max'] if m['max'] else 0
        label=html.escape(f"{name}: {m['mean']:.4g} {m['unit']} (n={m['n']})")
        print(f'<text x="20" y="{y}" font-size="15">{label}</text><rect x="450" y="{y-18}" width="{width}" height="24" fill="#3569b7"/>')
    print('</svg>')
except (ValueError,OSError,TypeError,KeyError,OverflowError) as e:
    print(f'错误：{e}',file=sys.stderr); sys.exit(1)
