import argparse
import hashlib
import json
from pathlib import Path

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run_index", required=True)
    ap.add_argument("--manifest", required=True)
    args = ap.parse_args()

    run_index = json.loads(Path(args.run_index).read_text())
    manifest = json.loads(Path(args.manifest).read_text())

    for fpath, info in manifest["files"].items():
        p = Path(fpath)
        if not p.exists():
            raise SystemExit(f"[verify_bundle] missing: {fpath}")
        got = sha256_file(p)
        exp = info["sha256"]
        if got != exp:
            raise SystemExit(f"[verify_bundle] hash mismatch for {fpath}\nexp={exp}\ngot={got}")

    print("[verify_bundle] OK")

if __name__ == "__main__":
    main()
