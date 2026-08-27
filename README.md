# Runova Mesh

**Distributed Compute Fabric for pooling CPUs, GPUs, RAM, and networked machines into one controllable home compute cluster.**

Runova Mesh is the orchestration layer for a small heterogeneous cluster. The goal is not to pretend that several PCs are literally one physical CPU/GPU, but to make them behave like one managed compute resource whenever the workload supports distributed execution.

## Goals

- Discover CPU, RAM, NVIDIA GPU, VRAM, hostname, OS, and local IP information on every node.
- Keep every machine eligible for useful work; the head node can also be a worker.
- Provide one inventory and one CLI for the whole cluster.
- Use the best backend for each workload instead of forcing everything through one engine.
- Start with Windows 11 support and keep Linux/Ubuntu as the preferred path for high-performance multi-node GPU work.
- Make network performance a first-class resource when choosing a distribution strategy.

## Planned execution backends

| Workload | Preferred backend |
| --- | --- |
| General CPU/GPU tasks | Ray |
| Multi-node training | PyTorch Distributed / DDP / FSDP |
| Large-model training | DeepSpeed |
| Distributed LLM serving | vLLM + Ray |
| GGUF / remote device experiments | llama.cpp RPC |

## Phase 0

Phase 0 establishes the cluster control plane:

1. Local hardware probing.
2. Node inventory configuration.
3. Windows and Linux bootstrap scripts.
4. Ray head/worker launch scripts.
5. Baseline CPU/GPU/network benchmarking hooks.
6. Architecture and roadmap documentation.
7. CI checks for the Python control-plane package.

## Quick start

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
runova-mesh probe
```

Copy `config/nodes.example.yaml` to `config/nodes.local.yaml` and put machine-specific addresses and settings there. `nodes.local.yaml` is ignored by Git.

## Security

Runova Mesh is intended for a trusted private LAN. Do not commit API keys, VPN credentials, private keys, model weights, datasets, or private node configuration. Do not expose Ray, llama.cpp RPC, or control ports directly to the public Internet.

## Project status

**Phase 0 - bootstrap / inventory / baseline cluster control plane.**
