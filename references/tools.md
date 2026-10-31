# 采集工具与限制

| 场景 | 工具 | 使用前核实 |
|---|---|---|
| Linux CPU | perf、FlameGraph、VTune | PMU 支持、perf_event_paranoid、符号、采样开销 |
| 内存/NUMA | numastat、perf mem、Intel PCM | 处理器支持、进程放置、计数单位 |
| 内核/等待 | ftrace、trace-cmd、BPF | 内核配置、权限、采集容量 |
| NVIDIA | Nsight Systems/Compute | 驱动/CUDA/工具版本、同步与 replay 开销 |
| 昇腾 | CANN Profiler、msprof | CANN 与设备对应版本、指标语义 |
| 网络/RDMA | iperf3、ib_write_bw、ethtool | 对端授权、端口、业务干扰、链路配置 |
| I/O | fio、iostat、blktrace | 测试文件与空间，不能覆盖业务设备 |
| Go | pprof、runtime trace | 采集端点权限、运行时版本、采样时间 |

先查看工具帮助和对应版本官方文档，不假定所有指标可用。不具备权限时请求已有采集结果或提供命令方案。默认不执行重启、系统调参、全机长时间 tracing、压力或破坏性测试。

官方入口：
- https://www.kernel.org/doc/html/latest/trace/index.html
- https://docs.nvidia.com/nsight-systems/
- https://docs.nvidia.com/nsight-compute/
- https://www.hiascend.com/document
- https://fio.readthedocs.io/en/latest/fio_doc.html
- https://pkg.go.dev/net/http/pprof
