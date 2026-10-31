# 性能工程 · performance-engineering

一个面向 Codex 的性能工程 Skill：从工作负载和性能目标出发，结合理论建模、业界方案调研与可复现实验，定位瓶颈并验证优化收益。

适合需要回答以下问题的工程师：系统为什么慢、该测什么、哪些方案值得尝试，以及优化后是否真的有效。

## 能做什么

- **定位问题**：梳理系统环境与关键路径，用 Profiling 和指标检验瓶颈假设。
- **解释原因**：选择适用理论，将公式、参数和测量结果对应起来，说明模型的条件与局限。
- **研究方案**：查阅原始论文、官方文档与开源实现，比较优化机制、资源成本和迁移条件。
- **验证结果**：设计可证伪的对照实验，保留原始数据，检查性能、正确性、稳定性与回归。
- **积累经验**：记录成功与失败实验，让结论可以复查、复现和有条件地复用。

覆盖 CPU、GPU/NPU、LLM 推理、内存与 NUMA、虚拟化与容器、网络与 RDMA、分布式系统、存储与 I/O 的分析入口。首版提供 LLM 推理完整演示，尚未在所有领域和硬件上实测。

## 安装

本仓库只包含一个 skill，安装时无需下载其他 skill。

### 推荐：让 Codex 安装

在 Codex 中输入：

```text
$skill-installer 请从这个仓库安装 performance-engineering：
https://github.com/Rowen-Ye/performance-engineering
```

安装后在 skill 列表中确认 `performance-engineering` 已出现；未出现时重新打开会话或重启 Codex。安装方式和发现目录以所用版本为准，参见 [Codex 官方说明](https://developers.openai.com/codex/skills/)。

### 备选：手动安装

[下载源码 ZIP](https://github.com/Rowen-Ye/performance-engineering/archive/refs/heads/main.zip)，解压后将文件夹命名为 `performance-engineering`，放入 `~/.agents/skills/`。确认最终路径为：

```text
~/.agents/skills/performance-engineering/SKILL.md
```

也可以只给当前项目使用：放入项目的 `.agents/skills/performance-engineering/`。已有同名目录时先备份，不要直接覆盖。更新时下载新版本并替换已备份的旧目录；分析产物应存放在项目工作目录，避免更新时丢失。

阅读和使用 Skill 指令不需要 Python。运行附带的数据分析工具需要 Python 3.10+，无需安装第三方包。真实测量还需要匹配硬件、工具和权限；联网研究需要相应搜索能力。

## 开始使用

在需要分析的项目中调用：

```text
$performance-engineering 分析当前推理服务的 TTFT（首个 token 返回时间）问题。先检查工作负载、性能目标和现有证据，再研究适用理论与方案，设计可证伪实验。缺少数据时，列出待采集指标，不要把猜测当成瓶颈结论。
```

Skill 会按任务规模选择执行深度：简单问题给出紧凑分析；复杂攻关采用问题定义、系统画像、理论发现、业界调研、性能建模、实验设计、优化验证、知识沉淀八阶段流程。

产物默认写入当前项目的 `performance-analysis/`，也可指定其他目录。报告会区分实测、估算、官方宣称、经验、假设和未知项。生产变更及高风险操作需要对应授权。

## 示例、模板与工具

- [LLM 推理完整演示](examples/llm-inference/README.md)：展示分析路径和复现命令。
- [报告模板](templates/report.md)与[实验记录](templates/experiment.md)：用于组织分析和保留证据。
- [基准数据格式](references/benchmark-format.md)：说明输入要求、指标方向与统计限制。
- [Skill 入口](SKILL.md)：查看工作流路由及参考资料。

从本仓库根目录运行：

```sh
python3 scripts/analyze-benchmark.py examples/llm-inference/benchmark-before.json
python3 scripts/compare-results.py examples/llm-inference/benchmark-before.json examples/llm-inference/benchmark-after.json
python3 scripts/visualize-performance.py examples/llm-inference/benchmark-before.json > performance.svg
```

**示例数据均为人工构造，未代表真实硬件测量或优化收益。** 工具提供描述统计，不自动证明统计显著性、因果或瓶颈；在缺少设备或权限时，Skill 应交付实验方案与未验证项。

## 验证与贡献

```sh
python3 -m unittest discover -s tests -v
```

当前自动测试覆盖统计、异常输入和比较条件校验，不等于真实系统调优验证。欢迎提交脱敏案例、失败实验及可复现问题，参见[贡献指南](CONTRIBUTING.md)。项目采用 [MIT 许可证](LICENSE)。

其他技能见[工程技能导航](https://github.com/Rowen-Ye/engineering-skills)。
