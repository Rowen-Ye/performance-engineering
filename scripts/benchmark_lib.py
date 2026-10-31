"""基准数据的显式格式与描述统计；不作统计显著性推断。"""
import json
import math
import statistics

def load(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError('JSON 根节点必须为对象')
    if not isinstance(data.get('context'), dict) or not data['context']:
        raise ValueError('context 必须为非空对象')
    metrics = data.get('metrics')
    if not isinstance(metrics, dict) or not metrics:
        raise ValueError('metrics 必须为非空对象')
    for name, metric in metrics.items():
        if not isinstance(metric, dict) or not isinstance(metric.get('unit'), str) or not metric['unit'] or metric.get('direction') not in ('lower','higher'):
            raise ValueError(f'{name}: 缺少 unit 或 direction')
        samples=metric.get('samples')
        if not isinstance(samples,list) or not samples:
            raise ValueError(f'{name}: samples 不能为空')
        if any(type(x) not in (int,float) or not math.isfinite(x) or x<0 for x in samples):
            raise ValueError(f'{name}: 样本必须为有限非负数')
    return data

def percentile(values, q):
    values=sorted(values); index=(len(values)-1)*q
    lo=math.floor(index); hi=math.ceil(index)
    return values[lo]+(values[hi]-values[lo])*(index-lo)

def summarize(data):
    out={}
    for name,m in data['metrics'].items():
        s=m['samples']
        out[name]={'unit':m['unit'],'direction':m['direction'],'n':len(s),'mean':statistics.mean(s),'min':min(s),'max':max(s),'p50':percentile(s,.5),'p95':percentile(s,.95),'p99':percentile(s,.99),'stdev':statistics.stdev(s) if len(s)>1 else None}
    return {'context':data['context'],'metrics':out,'note':'描述统计；百分位使用线性插值。小样本尾延迟不可靠；不代表显著性或因果。'}

def compare(before, after):
    if before['context'] != after['context']:
        raise ValueError('context 不一致，拒绝直接比较；变更内容请放在 treatment 字段')
    if before['metrics'].keys()!=after['metrics'].keys():
        raise ValueError('指标集合不一致')
    a,b=summarize(before),summarize(after); result={}
    for name,m in a['metrics'].items():
        n=b['metrics'][name]
        if (m['unit'],m['direction'])!=(n['unit'],n['direction']):
            raise ValueError(f'{name}: 单位或优化方向不一致')
        baseline=m['mean']; delta=n['mean']-baseline
        result[name]={'unit':m['unit'],'before_mean':baseline,'after_mean':n['mean'],'change_pct':delta/baseline*100 if baseline else None,'improvement_pct':delta/baseline*100*(1 if m['direction']=='higher' else -1) if baseline else None,'before':m,'after':n}
    return {'context':before['context'],'metrics':result,'note':'均值变化仅为描述性比较，不证明统计显著性或优化因果；零基线百分比为 null。'}
