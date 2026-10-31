# LLM 推理性能分析：完整演示
**所有 JSON 数值为人工构造，未运行模型、Profiler 或硬件实验；20%/25% 仅用于验证脚本。**

## 1 问题定义
演示问题：固定长度 Prefill 的 TTFT 高于目标。真实任务需先补齐模型版本、输入/输出长度分布、请求到达率、并发、精度、TP/EP 与缓存状态。区分排队、Prefill 和 Decode，TTFT 不能直接等同于纯 Prefill 时间。
## 2 系统画像
无实测设备。待采集：设备拓扑、HBM/互联、框架/驱动版本、算子时间线、主机等待和通信。不能从示例 JSON 推断硬件瓶颈。
## 3 理论发现
候选 Roofline 与关键路径。假设有效计算量 10^12 FLOP、对应 HBM 搬运 10^11 byte，则 I=10 FLOP/byte；假设可持续带宽 10^12 byte/s、峰值 10^14 FLOP/s，Roofline 上界为 10^13 FLOP/s。全部是假定参数，需要真实计数器验证。
## 4 业界研究
FlashAttention 原论文 https://arxiv.org/abs/2205.14135v2 提出 I/O 感知的分块注意力，利用片上存储减少 HBM 读写；选择它是因数据搬运假设，不代表当前系统尚未使用它。该机制已于 2026-10-31 对照原论文摘要核验；正式分析要核实框架实现、设备/精度支持与数值正确性。备选为调度/批处理优化：可能提高吞吐但增加等待和内存，不能直接与内核收益混比。
## 5 性能建模
上述假定下，计算时间下界至少 max(10^12/10^14,10^11/10^12)=0.1s，不含排队、通信、主机开销。若实测远慢于下界，不能据此确定 HBM 饱和，需要时间线与实际带宽。
## 6 假设与实验
H1：关键注意力算子 HBM 搬运造成瓶颈。预期优化减少对应层级字节量并缩短关键路径。证伪：计数显示搬运未减少，或端到端时间被排队/通信主导。固定模型、精度、请求集与并发，分离冷暖状态，交错 A/B、重复独立运行，记录正确性、错误率、内存和温度。未授权前不压测生产环境。
## 7 优化与验证
当前未实施真实优化。两个 JSON 仅演示均值 TTFT 100→80ms，描述性下降20%；吞吐1000→1250 tokens/s，上升25%。5个构造样本不能证明真实收益、显著性、稳定性或因果。真实任务还需验证输出容差、超时、长稳和资源代价。
## 8 知识沉淀
结论：分析路径与工具输出可以重现；瓶颈假设仍未验证。记录失败假设、条件变化和新证据后更新，不将本例写为优化成功案例。

从仓库根目录重现：
```sh
python3 scripts/analyze-benchmark.py examples/llm-inference/benchmark-before.json
python3 scripts/compare-results.py examples/llm-inference/benchmark-before.json examples/llm-inference/benchmark-after.json
python3 scripts/visualize-performance.py examples/llm-inference/benchmark-before.json > performance.svg
```
