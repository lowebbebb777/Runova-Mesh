from __future__ import annotations

import hashlib
import json
import os
import time


def main() -> None:
    blocks = 250_000
    payload = b"runova-mesh" * 128
    start = time.perf_counter()
    digest = b""
    for i in range(blocks):
        digest = hashlib.sha256(payload + i.to_bytes(8, "little")).digest()
    elapsed = time.perf_counter() - start
    result = {
        "pid": os.getpid(),
        "blocks": blocks,
        "elapsed_seconds": round(elapsed, 4),
        "blocks_per_second": round(blocks / elapsed, 2),
        "checksum": digest.hex(),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
