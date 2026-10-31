# 业界研究入口
这些是检索入口，不是已验证的优化承诺。任务中固定版本/commit 后阅读源码与设计。

- LLM：vLLM https://github.com/vllm-project/vllm 、SGLang https://github.com/sgl-project/sglang 、TensorRT-LLM https://github.com/NVIDIA/TensorRT-LLM 。围绕 KV 管理、批处理、调度、并行通信查机制与代价。
- 注意力 I/O：FlashAttention https://arxiv.org/abs/2205.14135 。研究分块与片上存储如何减少 HBM 搬运；核验支持精度、形状和设备。
- 虚拟化：Firecracker https://github.com/firecracker-microvm/firecracker 、QEMU https://www.qemu.org/docs/master/ 。分辨启动路径、设备模型、隔离与内存成本。
- 内存：jemalloc https://github.com/jemalloc/jemalloc 、mimalloc https://github.com/microsoft/mimalloc 。研究分配、碎片、线程本地缓存与峰值内存代价。
- 网络/存储：DPDK https://www.dpdk.org/ 、SPDK https://spdk.io/ 。研究轮询、批处理、零拷贝及专用核心/设备约束。
- 分布式：从当前项目的调度、复制、分片与一致性协议官方设计入手，不把缓存/批处理收益跨语义迁移。

跨领域映射须列出共同机制、不同约束及可证伪迁移实验。每项最终记录：来源、日期、版本、代码符号、原问题、机制、公开实验条件、迁移条件、资源成本和未知项。
