# 理论索引
优先按问题选择，发现不适用时停止套用。所有条目都需结合当前采集参数验证。

| 理论 | 公式与变量 | 条件及主要误用 | 原始或权威入口 |
|---|---|---|---|
| Roofline | P ≤ min(P_peak, B × I)，P 为运算/s，B 为字节/s，I 为运算/字节 | 数据量须对应同一存储层；只给上界，不解释所有调度/延迟损失 | https://www.osti.gov/biblio/950315 |
| Amdahl | S=1/((1-p)+p/s)，p 为基线可优化时间占比，s 为局部加速 | 固定工作量且其余路径不变；p 不是代码行占比 | https://doi.org/10.1145/1465482.1465560 |
| Little | L=λW，L 为平均在系统请求数，λ 为完成率，W 为平均停留时间 | 稳态、边界与统计窗口一致；不能用 P99 代 W | https://doi.org/10.1287/opre.9.3.383 |
| M/M/1 排队 | W=1/(μ-λ)，ρ=λ/μ<1 | 泊松到达、指数服务时间、单服务台；真实系统常不满足 | https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/ |
| Work-Span | T_p≥max(T_1/p,T_∞) | DAG 工作/关键路径模型，不含全部通信与调度成本 | https://supertech.csail.mit.edu/papers/steal.pdf |
| BDP | 在途字节=带宽(字节/s)×RTT(s) | 窗口、路径与吞吐边界一致；链路峰值不等于应用吞吐 | https://www.rfc-editor.org/rfc/rfc6349 |
| NUMA locality | T≈本地访问次数×本地成本+远端访问次数×远端成本 | 重叠/cache/争用会破坏简单相加，必须测放置与实际流量 | https://docs.kernel.org/admin-guide/mm/numa_memory_policy.html |
| CPU Top-down | slots 分类为 retiring、bad speculation、frontend/backend bound | 微架构/PMU 相关，计数器不可跨平台直接比较 | https://www.intel.com/content/www/us/en/docs/vtune-profiler/user-guide/2024-0/top-down-microarchitecture-analysis-method.html |
| USE | 每类资源检查 utilization、saturation、errors | 方法而非单一数学定律；高利用率不自动等于瓶颈 | https://www.brendangregg.com/usemethod.html |

引用需在任务中打开核实并记录版本与日期；索引链接本身不表示已经核实当前系统。
