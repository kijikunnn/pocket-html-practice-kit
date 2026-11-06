#!/usr/bin/env python3
"""Compare ten local synthetic examples with the copied checker's actual CLI."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
SOURCE_SHA256 = "9927076590dcf237cca3d4c59f8a11d85c4a534d693868d53c253f4831818c67"


def main():
    checker = ROOT / "check-analytics-html.py"
    if checker.stat().st_size > 65536 or hashlib.sha256(checker.read_bytes()).hexdigest() != SOURCE_SHA256:
        print(json.dumps({"status": "source_hash_mismatch"}))
        return 1
    expected_path = ROOT / "expected-results.json"
    if expected_path.stat().st_size > 65536:
        raise ValueError("expected results too large")
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    if len(expected) != 10:
        raise ValueError("expected ten fixtures")
    for name, result in sorted(expected.items()):
        if Path(name).name != name or not name.endswith(".html"):
            raise ValueError("unexpected fixture name")
        fixture = ROOT / "fixtures" / name
        if fixture.stat().st_size > 8192:
            raise ValueError("fixture too large")
        checked = subprocess.run([sys.executable, "-I", "-B", str(checker), str(fixture)],
                                 capture_output=True, text=True, timeout=2, check=False)
        if checked.returncode != 0 or len(checked.stdout) > 8192 or json.loads(checked.stdout) != result:
            print(json.dumps({"status": "output_mismatch", "fixture": name}))
            return 1
    print(json.dumps({"status": "expected_outputs_match", "fixture_count": len(expected)}))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, subprocess.TimeoutExpired):
        print(json.dumps({"status": "verification_failed"}))
        sys.exit(1)
