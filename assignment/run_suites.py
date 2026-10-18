"""Execute groups sequentially, optionally using parallel workers per group."""
import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parallel", action="store_true")
    parser.add_argument("--member", choices=["saim", "ahmed"])
    args = parser.parse_args()
    for group in ("length", "between", "mac"):
        selection = f"{group} and {args.member}" if args.member else group
        command = [sys.executable, "-m", "pytest", "-c", "pytest-assignment.ini",
                   "-m", selection, "-v"]
        if args.parallel:
            command += ["-n", "2"]
        print(f"\nRunning group: {selection}", flush=True)
        result = subprocess.run(command, cwd=ROOT)
        if result.returncode:
            return result.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
