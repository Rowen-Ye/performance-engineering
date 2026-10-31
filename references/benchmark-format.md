# 基准数据格式
Python 3.10+，无需第三方包。样本为同单位的有限非负数，不接受空列表、布尔值、NaN 或 Infinity。

```json
{"context":{"workload":"固定请求集与长度分布","hardware":"设备型号/数量","version":"基线代码和环境版本","protocol":"预热/测量时长/到达率/精度/并发"},"treatment":"本组唯一实验变更及提交","metrics":{"ttft":{"unit":"ms","direction":"lower","samples":[10,12,11]},"throughput":{"unit":"tokens/s","direction":"higher","samples":[100,101,99]}}}
```
context 应完整记录保持一致的条件，包括数据哈希和统计协议；treatment 记录变更，不放进 context。比较要求 context 完全一致，但这只是机械保护，不能代替人工检查实验可比性。

请求延迟样本可以计算分位数；每轮吞吐样本应为独立测量窗口。不要把 tokens/s 样本的 P99 解释成请求尾延迟。脚本保留名称与单位，不推断这些语义。

百分位按排序后 (n-1)q 线性插值；小样本尾部不可靠。标准差是样本标准差；单样本为 null。比较以均值计算变化率；lower 指标以下降为正向收益，higher 以上升为正向收益。基线为零则百分比 null。原始 JSON 必须保留，脚本不修改输入。

这些工具不计算显著性或置信区间，不自动移除异常值，也不自动证明因果。
