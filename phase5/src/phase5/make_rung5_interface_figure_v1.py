#!/usr/bin/env python3
"""
Phase 5 Rung 5: Minimal visual sanity panel for the interface contract.

- Consumes the Rung 4 CSV:
    phase5/outputs/tables/phase5_rung4_sanity_table_v1.csv

- Produces a simple PNG summarizing:
    * which files exist,
    * their sizes (KB),
    * and any external status flags.

- This is purely program-level: no physics, no FRW modeling,
  no likelihoods. It just makes the interface state visible.
"""
from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


def find_repo_root() -> Path:
    # __file__ = .../phase5/src/phase5/make_rung5_interface_figure_v1.py
    return Path(__file__).resolve().parents[3]


def load_sanity_csv(path: Path):
    if not path.is_file():
        raise FileNotFoundError(f"Rung 4 CSV not found: {path}")
    rows = []
    with path.open("r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    if not rows:
        raise RuntimeError(f"Rung 4 CSV is empty: {path}")
    return rows


def parse_bool(s: str) -> bool:
    if s is None:
        return False
    return s.strip().lower() in {"true", "1", "yes"}


def build_figure(rows, out_path: Path):
    labels = []
    sizes_kb = []
    exists_flags = []
    ext_statuses = []

    for r in rows:
        section = r.get("section", "").strip()
        key = r.get("key", "").strip()
        label = f"{section}:{key}" if section and key else (key or section or "?")

        size_str = r.get("size_bytes") or ""
        try:
            size_kb = int(size_str) / 1024.0 if size_str else 0.0
        except ValueError:
            size_kb = 0.0

        exists = parse_bool(r.get("exists", "false"))
        ext_status = (r.get("ext_status") or "").strip()

        labels.append(label)
        sizes_kb.append(size_kb)
        exists_flags.append(exists)
        ext_statuses.append(ext_status)

    n_total = len(rows)
    n_missing = sum(1 for e in exists_flags if not e)

    # Basic horizontal bar chart
    fig, ax = plt.subplots(figsize=(max(6.0, 0.4 * n_total + 3.0), 4.5))

    y_positions = range(len(labels))

    # Color files by existence
    colors = ["tab:green" if ex else "tab:red" for ex in exists_flags]

    ax.barh(list(y_positions), sizes_kb, color=colors)

    ax.set_yticks(list(y_positions))
    ax.set_yticklabels(labels, fontsize=7)
    ax.set_xlabel("File size [KB]")
    ax.set_title(
        f"Phase 5 interface sanity (Rung 4)\n"
        f"Files: {n_total}, missing: {n_missing}"
    )

    # Simple legend-like text
    ax.text(
        1.02,
        1.0,
        "green: exists\nred: missing",
        transform=ax.transAxes,
        va="top",
        ha="left",
        fontsize=7,
    )

    # Collect external-status info (if any)
    ext_notes = [s for s in ext_statuses if s]
    if ext_notes:
        unique_notes = sorted(set(ext_notes))
        ext_text = "External status:\n" + "\n".join(f"- {u}" for u in unique_notes)
        ax.text(
            1.02,
            0.0,
            ext_text,
            transform=ax.transAxes,
            va="bottom",
            ha="left",
            fontsize=7,
        )

    fig.tight_layout()

    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=200)
    plt.close(fig)


def main():
    repo_root = find_repo_root()
    print(f"[phase5_rung5_figure] Repo root: {repo_root}")

    in_csv = repo_root / "phase5" / "outputs" / "tables" / "phase5_rung4_sanity_table_v1.csv"
    out_png = repo_root / "phase5" / "outputs" / "figures" / "phase5_interface_sanity_v1.png"

    print(f"[phase5_rung5_figure] Input CSV: {in_csv}")
    print(f"[phase5_rung5_figure] Output PNG: {out_png}")

    rows = load_sanity_csv(in_csv)
    build_figure(rows, out_png)

    print(
        f"[phase5_rung5_figure] Wrote {out_png} "
        f"({out_png.stat().st_size} bytes)"
    )
    print(
        f"[phase5_rung5_figure] Timestamp UTC: "
        f"{datetime.utcnow().isoformat()}Z"
    )


if __name__ == "__main__":
    main()
