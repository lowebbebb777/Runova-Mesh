from __future__ import annotations

import argparse

from .probe import probe_json


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="runova-mesh", description="Runova Mesh cluster CLI")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("probe", help="Print local CPU/GPU/RAM/network inventory as JSON")
    sub.add_parser("version", help="Print Runova Mesh version")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "probe":
        print(probe_json())
        return 0
    if args.command == "version":
        from . import __version__

        print(__version__)
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
