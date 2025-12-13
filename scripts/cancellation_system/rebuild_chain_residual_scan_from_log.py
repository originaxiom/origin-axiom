#!/usr/bin/env python3
"""
Rebuild chain residual scan artifacts from a saved terminal log.

Outputs (repo-friendly):
- docs/results/cancellation_system/runs/<run_id>/chain_residual_scan.csv
- figures/cancellation_system/runs/<run_id>/theta_scan_N<maxN>.png
- figures/cancellation_system/runs/<run_id>/theta_scan_min_over_N.png
"""
from __future__ import annotations
import argparse, re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd

try:
    import matplotlib.pyplot as plt
    HAVE_MPL = True
except Exception:
    HAVE_MPL = False

THETA_RE = re.compile(r"^--- theta = ([0-9.]+) ---$")
N_RE = re.compile(
    r"^N=\s*(\d+):\s*mean\|S\|=([0-9.eE+-]+),\s*rms\|S\|=([0-9.eE+-]+),\s*mean\|S\|/sqrtN=([0-9.eE+-]+)"
)
HDR_RE = re.compile(r"^=== 1D cancellation chain residual scan ===$")

META_RX = {
    "Ns": re.compile(r"^Ns\s*:\s*(\[.*\])$"),
    "max_charge": re.compile(r"^max_q\s*:\s*(\d+)$"),
    "noise_sigma": re.compile(r"^noise\s*:\s*([0-9.eE+-]+)$"),
    "n_samples": re.compile(r"^n_samples per point:\s*(\d+)$"),
    "enforce_zero_sum": re.compile(r"^enforce_zero_sum\s*:\s*(True|False)$"),
}

def find_seed(lines: List[str], start_idx: int) -> Optional[int]:
    for j in range(start_idx, max(-1, start_idx - 80), -1):
        if "--seed" in lines[j]:
            m = re.search(r"--seed\s+(\d+)", lines[j])
            if m:
                return int(m.group(1))
    return None

@dataclass
class Segment:
    meta: Dict[str, object]
    rows: pd.DataFrame

def parse_segments(lines: List[str]) -> List[Segment]:
    hdr_idxs = [i for i, l in enumerate(lines) if HDR_RE.match(l.strip())]
    segs: List[Segment] = []
    for k, h in enumerate(hdr_idxs):
        end = hdr_idxs[k + 1] if k + 1 < len(hdr_idxs) else len(lines)

        meta: Dict[str, object] = {"seed": find_seed(lines, h)}
        for j in range(h + 1, min(end, h + 35)):
            s = lines[j].strip()
            if s.startswith("--- theta"):
                break
            for key, rx in META_RX.items():
                m = rx.match(s)
                if m:
                    if key == "Ns":
                        meta["Ns"] = m.group(1)  # keep as string
                    elif key == "enforce_zero_sum":
                        meta[key] = (m.group(1) == "True")
                    elif key in ("max_charge", "n_samples"):
                        meta[key] = int(m.group(1))
                    else:
                        meta[key] = float(m.group(1))

        recs = []
        cur_theta: Optional[float] = None
        for j in range(h, end):
            s = lines[j].strip()
            tm = THETA_RE.match(s)
            if tm:
                cur_theta = float(tm.group(1))
                continue
            nm = N_RE.match(s)
            if nm and cur_theta is not None:
                recs.append({
                    "theta": cur_theta,
                    "N": int(nm.group(1)),
                    "mean_abs_S": float(nm.group(2)),
                    "rms_abs_S": float(nm.group(3)),
                    "mean_abs_S_over_sqrtN": float(nm.group(4)),
                })
        segs.append(Segment(meta=meta, rows=pd.DataFrame(recs)))
    return segs

def write_run(run_id: str, seg: Segment, out_results: Path, out_figures: Path) -> None:
    if seg.rows.empty:
        print(f"[skip] {run_id}: no rows parsed")
        return

    rdir = out_results / run_id
    fdir = out_figures / run_id
    rdir.mkdir(parents=True, exist_ok=True)
    fdir.mkdir(parents=True, exist_ok=True)

    df = seg.rows.copy()
    df["run_id"] = run_id
    for k, v in seg.meta.items():
        df[k] = v
    df = df.sort_values(["theta", "N"])

    csv_path = rdir / "chain_residual_scan.csv"
    df.to_csv(csv_path, index=False)
    print(f"[ok] wrote {csv_path}")

    if not HAVE_MPL:
        print("[warn] matplotlib not available; skipping plots")
        return

    maxN = int(df["N"].max())
    dN = df[df["N"] == maxN].sort_values("theta")
    if dN.shape[0] >= 3:
        plt.figure()
        plt.plot(dN["theta"], dN["mean_abs_S_over_sqrtN"])
        plt.xlabel("theta")
        plt.ylabel(f"mean(|S|)/sqrt(N) at N={maxN}")
        plt.title(f"Chain residual theta scan (N={maxN})\n{run_id}")
        p1 = fdir / f"theta_scan_N{maxN}.png"
        plt.tight_layout(); plt.savefig(p1, dpi=180); plt.close()
        print(f"[ok] wrote {p1}")

    piv = df.pivot_table(index="theta", columns="N", values="mean_abs_S_over_sqrtN", aggfunc="first")
    dmin = piv.min(axis=1).reset_index()
    plt.figure()
    plt.plot(dmin["theta"], dmin[0])
    plt.xlabel("theta")
    plt.ylabel("min_N mean(|S|)/sqrt(N)")
    plt.title(f"Min over N of mean(|S|)/sqrt(N)\n{run_id}")
    p2 = fdir / "theta_scan_min_over_N.png"
    plt.tight_layout(); plt.savefig(p2, dpi=180); plt.close()
    print(f"[ok] wrote {p2}")

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", required=True)
    ap.add_argument("--run-prefix", default="20251212_chain_residual_scan")
    ap.add_argument("--out-results", default="docs/results/cancellation_system/runs")
    ap.add_argument("--out-figures", default="figures/cancellation_system/runs")
    args = ap.parse_args()

    lines = Path(args.log).read_text(errors="replace").splitlines()
    segs = parse_segments(lines)
    if not segs:
        raise SystemExit("No scan headers found in log.")

    for i, seg in enumerate(segs, start=1):
        ez = seg.meta.get("enforce_zero_sum", None)
        ez_tag = "zero_sum" if ez is True else ("no_zero_sum" if ez is False else "unknown")
        ns = seg.meta.get("n_samples", "na")
        seed = seg.meta.get("seed", "na")
        run_id = f"{args.run_prefix}__seg{i}__{ez_tag}__ns{ns}__seed{seed}"
        write_run(run_id, seg, Path(args.out_results), Path(args.out_figures))

if __name__ == "__main__":
    main()