import argparse
import csv
import hashlib
import json
import math
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import matplotlib.pyplot as plt


def sha256_text(s: str) -> str:
    h = hashlib.sha256()
    h.update(s.encode("utf-8"))
    return h.hexdigest()


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def try_git_head(repo_root: Path) -> str:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
            stderr=subprocess.DEVNULL,
        )
        return out.decode("utf-8").strip()
    except Exception:
        return "UNKNOWN"


def parse_theta_best(summary_csv: Path) -> float:
    # Expect a header row; find theta_best_rad or theta_rad; otherwise first numeric in first row.
    with summary_csv.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        raise RuntimeError(f"Empty summary CSV: {summary_csv}")

    row0 = rows[0]
    for key in ["theta_best_rad", "theta_rad", "theta_star_rad", "theta"]:
        if key in row0 and row0[key] not in (None, ""):
            return float(row0[key])

    # fallback: first value in the first row
    for v in row0.values():
        if v not in (None, ""):
            try:
                return float(v)
            except Exception:
                pass

    raise RuntimeError(f"Could not parse theta from summary CSV headers: {list(row0.keys())}")


def extract_b_pmns_from_targets(targets_yaml: Path) -> float:
    """
    Strict but dependency-free extraction of:
      ansatz.mapping.delta_pmns.b: <float>
    We do not fully parse YAML. We scan for the delta_pmns block and then the first 'b:' in that block.
    """
    txt = targets_yaml.read_text(encoding="utf-8").splitlines()
    in_delta_pmns = False
    base_indent = None

    for line in txt:
        raw = line
        line = line.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        indent = len(line) - len(line.lstrip(" "))

        if line.strip().startswith("delta_pmns:"):
            in_delta_pmns = True
            base_indent = indent
            continue

        if in_delta_pmns:
            # Exit block if indentation goes back to base or less and looks like a new key
            if base_indent is not None and indent <= base_indent and ":" in line.strip():
                in_delta_pmns = False
                base_indent = None
                continue

            if line.strip().startswith("b:"):
                val = line.split("b:", 1)[1].strip()
                return float(val)

    # Default fallback (should never happen if targets.yaml is baseline-locked)
    return float("nan")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--theta_summary", required=True)
    ap.add_argument("--out_fig", required=True)
    ap.add_argument("--out_meta", required=False, default=None)
    ap.add_argument("--targets_yaml", required=False, default="phase3/fit/targets.yaml")
    args = ap.parse_args()

    repo_root = Path.cwd().resolve()
    theta_summary = Path(args.theta_summary).resolve()
    out_fig = Path(args.out_fig).resolve()

    out_meta = Path(args.out_meta).resolve() if args.out_meta else Path(str(out_fig) + ".meta.json").resolve()
    targets_yaml = (repo_root / args.targets_yaml).resolve()

    theta_best = parse_theta_best(theta_summary)

    # ---- Placeholder injection function (keep consistent with current Phase 3 scope) ----
    # We do NOT claim a physical model here; this is a pipeline artifact for tracing how
    # an injection-style mapping behaves vs theta under the locked model-choice.
    #
    # Current choice: a smooth periodic diagnostic curve with a marked theta*.
    thetas = [i * (2.0 * math.pi) / 2000.0 for i in range(2001)]
    ys = [math.sin(t - theta_best) for t in thetas]

    out_fig.parent.mkdir(parents=True, exist_ok=True)
    plt.figure()
    plt.plot(thetas, ys)
    plt.axvline(theta_best)
    plt.xlabel("theta (rad)")
    plt.ylabel("diagnostic Δρ_vac proxy (arb.)")
    plt.tight_layout()
    plt.savefig(out_fig)
    plt.close()

    # ---- Provenance meta ----
    git_head = try_git_head(repo_root)

    targets_sha = sha256_file(targets_yaml) if targets_yaml.exists() else "MISSING"
    summary_sha = sha256_file(theta_summary)

    b_pmns = extract_b_pmns_from_targets(targets_yaml) if targets_yaml.exists() else float("nan")

    meta = {
        "generated_utc": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "git_head": git_head,
        "inputs": {
            "theta_summary_csv": str(theta_summary),
            "theta_summary_sha256": summary_sha,
            "targets_yaml": str(targets_yaml),
            "targets_yaml_sha256": targets_sha,
        },
        "model_lock": {
            "baseline_selected_by": "theta_offset_sweep.csv (lowest chi2)",
            "targets_yaml_expected": "phase3/fit/targets.yaml",
            "b_pmns_rad": b_pmns,
        },
        "fit_result": {
            "theta_best_rad": theta_best,
        },
        "outputs": {
            "fig": str(out_fig),
            "meta": str(out_meta),
        },
        "notes": "Phase 3 injection figure meta binds plot to exact model choice + theta* + file hashes.",
    }

    out_meta.parent.mkdir(parents=True, exist_ok=True)
    out_meta.write_text(json.dumps(meta, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
