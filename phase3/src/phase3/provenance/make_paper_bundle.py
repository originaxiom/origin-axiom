import argparse
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in_summary", required=True)
    ap.add_argument("--in_summary_meta", required=True)
    ap.add_argument("--in_diag", required=True)
    ap.add_argument("--in_sweep_csv", required=True)
    ap.add_argument("--in_sweep_meta", required=True)
    ap.add_argument("--in_fig1", required=True)
    ap.add_argument("--in_fig2", required=True)
    ap.add_argument("--in_fig2_meta", required=True)
    ap.add_argument("--out_run_index", required=True)
    ap.add_argument("--out_manifest", required=True)
    args = ap.parse_args()

    files = [
        Path(args.in_summary),
        Path(args.in_summary_meta),
        Path(args.in_diag),
        Path(args.in_sweep_csv),
        Path(args.in_sweep_meta),
        Path(args.in_fig1),
        Path(args.in_fig2),
        Path(args.in_fig2_meta),
    ]

    out_run_index = Path(args.out_run_index)
    out_manifest = Path(args.out_manifest)
    out_run_index.parent.mkdir(parents=True, exist_ok=True)
    out_manifest.parent.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    run_index = {
        "generated_utc": now,
        "artifacts": {p.name: str(p) for p in files},
        "notes": "Phase 3 paper bundle (Level A evidence store).",
    }

    manifest = {
        "generated_utc": now,
        "files": {str(p): {"sha256": sha256_file(p)} for p in files},
    }

    out_run_index.write_text(json.dumps(run_index, indent=2), encoding="utf-8")
    out_manifest.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main()
