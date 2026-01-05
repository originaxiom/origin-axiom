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
    ap.add_argument("--in_fig1", required=True)
    ap.add_argument("--in_fig2", required=True)
    ap.add_argument("--out_run_index", required=True)
    ap.add_argument("--out_manifest", required=True)
    args = ap.parse_args()

    in_summary = Path(args.in_summary)
    in_fig1 = Path(args.in_fig1)
    in_fig2 = Path(args.in_fig2)

    out_run_index = Path(args.out_run_index)
    out_manifest = Path(args.out_manifest)
    out_run_index.parent.mkdir(parents=True, exist_ok=True)
    out_manifest.parent.mkdir(parents=True, exist_ok=True)

    # Phase 3: run_id concept exists, but paper_bundle is reviewer-safe minimal store.
    # Here we treat the bundle itself as the canonical evidence store for Level A.
    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_index = {
        "generated_utc": now,
        "artifacts": {
            "theta_fit_summary.csv": str(in_summary),
            "fig1_theta_fit_diagnostics.pdf": str(in_fig1),
            "fig2_delta_rho_vac_vs_theta.pdf": str(in_fig2),
        },
        "notes": "Phase 3 bootstrap bundle (no heavy runs yet).",
    }

    manifest = {
        "generated_utc": now,
        "files": {
            str(in_summary): {"sha256": sha256_file(in_summary)},
            str(in_fig1): {"sha256": sha256_file(in_fig1)},
            str(in_fig2): {"sha256": sha256_file(in_fig2)},
        },
    }

    out_run_index.write_text(json.dumps(run_index, indent=2))
    out_manifest.write_text(json.dumps(manifest, indent=2))

if __name__ == "__main__":
    main()
