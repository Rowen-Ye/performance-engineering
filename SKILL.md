---
name: performance-engineering
description: 分析系统性能瓶颈、发现适用理论与业界方案、设计可复现实验并验证优化收益。适用于延迟、吞吐、资源效率和扩展性问题，以及 CPU、GPU/NPU、LLM 推理、内存、网络、存储和虚拟化性能攻关。
---
# 性能工程

从工作负载、性能目标和证据开始。不要以调参或修改代码替代理解问题。

## 路由与执行深度
- 先阅读 [问题定义](workflows/problem-definition.md)。缺失信息优先从获准访问的代码、日志、配置和已有数据获取，再询问影响判断的未知项。
- 单一指标解释或数据比较：按需加载相关理论与脚本，给出紧凑结论，不强制生成八份报告。
- 瓶颈定位：问题定义 → [系统画像](workflows/system-profiling.md) → 理论与业界研究 → 建模 → 可证伪实验。
- 完整优化：继续 [优化验证](workflows/optimization-validation.md) 和 [知识沉淀](workflows/knowledge-accumulation.md)。复杂攻关不得跳过理论、业界调研与实验验证；缺工具或数据时明确阻塞项，不伪造完成。
- [理论发现](workflows/theory-discovery.md) 与 [业界调研](workflows/industry-research.md) 是相互反馈的两条研究线，同轮推进，不等单条完全结束再开展另一条；有授权与适用工具时可并行。
- 使用 [性能建模](workflows/performance-modeling.md)、[实验设计](workflows/experiment-design.md) 建立当前系统的可计算模型和实验计划。

## 不可省略的判断
证据标注为：实测事实、理论估算、官方宣称、工程经验、待验证假设、未知。理论上界和预测单独注明，记录来源、版本、时间和适用条件。
不强套理论，不把利用率异常直接当瓶颈；不把论文收益当本系统收益。研究优先原始论文、官方文档及版本固定源码，机制不明则明确未知。
优化须验证正确性、稳定性、资源成本和可维护性。保留基线，控制主要变量，重复测量，记录回滚。系统配置、生产环境、服务重启或破坏性操作须有对应授权；自主研究不等于获准执行这些操作。
无联网能力时列出待核验来源；无硬件或执行权限时交付可执行方案，不能声称已测量或优化成功。

## 按需资料
- 领域选择：[领域分析路径](references/domains.md)，覆盖 CPU、GPU/NPU、LLM、内存/NUMA、虚拟化/容器、网络/RDMA、分布式、存储/I/O。
- 理论：[理论索引](references/theories/index.md)。读候选条目，再针对任务检索原始资料；索引不是知识边界。
- 工具：[采集工具与限制](references/tools.md)。不自动安装或运行高开销采集。
- 方案：[业界研究入口](references/industry-solutions.md)。入口不是已经验证的方案结论。
- 交付：[报告模板](templates/report.md)、[实验记录](templates/experiment.md)、[数据格式](references/benchmark-format.md)。
- 示例：[LLM 推理完整演示](examples/llm-inference/README.md)。数据为人工构造，不能引用为真实收益。

## 数据工具
脚本仅依赖 Python 3.10+ 标准库，执行路径相对于本 skill 目录：
```sh
python3 scripts/analyze-benchmark.py <原始数据.json>
python3 scripts/compare-results.py <优化前.json> <优化后.json>
python3 scripts/visualize-performance.py <原始数据.json> > performance.svg
```
比较拒绝 context、单位、方向或指标集合不一致的数据。输出为描述统计，不自动断言显著性、因果或瓶颈。

## 交付与知识位置
输出写入使用者指定的工作目录；未指定时使用当前项目的 performance-analysis/。不得写入安装目录或自动上传内部数据。
复杂任务用报告模板记录八阶段，阶段产物可以合并；每个实验保留独立目录及原始记录。最终说明证据、置信边界、收益与代价、失败假设、未解决事项和下一步。
