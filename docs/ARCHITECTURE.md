# Runova Mesh Architecture

## Design principle

Runova Mesh treats a set of machines as a managed compute fabric. It does **not** claim that arbitrary software can see several networked PCs as one physical GPU. Instead, it selects a distributed execution backend appropriate to the workload.

## Layers

1. **Inventory** - CPU, RAM, GPU, VRAM, OS, IP, and capabilities.
2. **Transport** - private LAN, with measured bandwidth and latency.
3. **Resource manager** - initially Ray for general distributed tasks.
4. **Execution backends** - PyTorch Distributed, DeepSpeed, vLLM, llama.cpp RPC.
5. **Scheduler** - future policy engine choosing local, data-parallel, tensor-parallel, pipeline-parallel, or task-parallel execution.
6. **Monitoring** - utilization, temperature, memory pressure, network throughput, failures.

## Scheduling strategy

The future scheduler should prefer the least communication-heavy method that satisfies the job:

- Independent work units: task/data parallelism.
- Synchronous training: DDP/FSDP.
- Very large model training: DeepSpeed/FSDP.
- Large-model inference: vLLM tensor/pipeline/data parallelism.
- GGUF remote-memory experiments: llama.cpp RPC.

Network bandwidth is part of scheduling. Cross-node tensor parallelism should only be selected when the measured fabric is fast enough to justify communication overhead.

## Node roles

The default three-node topology is:

- PC1: head + worker
- PC2: worker
- PC3: worker

The head is intentionally allowed to compute. Control-plane duties should not reserve an entire machine unless measurements prove that doing so improves throughput.

## Security boundary

Phase 0 assumes a trusted private LAN. Control ports must not be exposed directly to the Internet. Node-local secrets and addresses belong in ignored local configuration.
