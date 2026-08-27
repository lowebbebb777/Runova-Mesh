from __future__ import annotations

import json
import platform
import shutil
import socket
import subprocess
from dataclasses import asdict, dataclass
from typing import Any

import psutil


@dataclass
class GpuInfo:
    index: int
    name: str
    memory_total_mib: int
    driver_version: str


def _local_ip() -> str:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(("8.8.8.8", 80))
        return sock.getsockname()[0]
    except OSError:
        return "unknown"
    finally:
        sock.close()


def _nvidia_gpus() -> list[GpuInfo]:
    if shutil.which("nvidia-smi") is None:
        return []

    cmd = [
        "nvidia-smi",
        "--query-gpu=index,name,memory.total,driver_version",
        "--format=csv,noheader,nounits",
    ]
    try:
        completed = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=10)
    except (subprocess.SubprocessError, OSError):
        return []

    gpus: list[GpuInfo] = []
    for raw in completed.stdout.splitlines():
        parts = [part.strip() for part in raw.split(",")]
        if len(parts) != 4:
            continue
        try:
            gpus.append(
                GpuInfo(
                    index=int(parts[0]),
                    name=parts[1],
                    memory_total_mib=int(float(parts[2])),
                    driver_version=parts[3],
                )
            )
        except ValueError:
            continue
    return gpus


def collect_probe() -> dict[str, Any]:
    virtual = psutil.virtual_memory()
    gpus = _nvidia_gpus()
    return {
        "hostname": socket.gethostname(),
        "ip": _local_ip(),
        "os": platform.platform(),
        "python": platform.python_version(),
        "cpu": {
            "processor": platform.processor() or "unknown",
            "physical_cores": psutil.cpu_count(logical=False),
            "logical_cores": psutil.cpu_count(logical=True),
        },
        "memory": {
            "total_gib": round(virtual.total / (1024**3), 2),
        },
        "gpu": [asdict(gpu) for gpu in gpus],
        "gpu_count": len(gpus),
        "vram_total_mib": sum(gpu.memory_total_mib for gpu in gpus),
    }


def probe_json(indent: int = 2) -> str:
    return json.dumps(collect_probe(), indent=indent, ensure_ascii=False)
