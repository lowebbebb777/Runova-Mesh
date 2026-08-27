# Roadmap

## Phase 0 - Bootstrap and inventory

- [x] Repository structure
- [x] Cross-platform hardware probe
- [x] Three-node configuration example
- [x] Windows/Linux bootstrap scripts
- [x] Ray head/worker launchers for Windows
- [x] CPU baseline benchmark
- [ ] Real three-node inventory
- [ ] LAN throughput/latency benchmark
- [ ] GPU compute benchmark
- [ ] Cluster-wide status command

## Phase 1 - Ray compute pool

- Register all three nodes.
- Verify head node also participates as a worker.
- Add distributed CPU/GPU smoke tests.
- Add task placement and resource labels.
- Add health/status reporting.

## Phase 2 - AI training

- PyTorch torchrun multi-node examples.
- DDP benchmark.
- FSDP benchmark.
- DeepSpeed hostfile/config generation.
- Compare single-node vs multi-node efficiency.

## Phase 3 - LLM inference fabric

- vLLM + Ray multi-node deployment profile.
- Data, tensor, and pipeline parallel profiles.
- llama.cpp RPC experimental profile.
- Model placement calculator using VRAM and measured network capacity.

## Phase 4 - Smart scheduler

- Job manifest format.
- Automatic backend selection.
- Cost model for compute vs communication.
- Failover/retry policy.
- Per-node power/temperature constraints.

## Phase 5 - Runova integration

- Expose Runova Mesh as a compute backend.
- Cluster dashboard.
- Job history and benchmark database.
- One-command workload launch.
