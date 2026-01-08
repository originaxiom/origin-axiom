#!/usr/bin/env python3
"""
Phase 5 helper: generate a human-readable dashboard for
`phase5_interface_v1_summary.json`.

Input:
  phase5/outputs/tables/phase5_interface_v1_summary.json

Output:
  phase5/outputs/tables/phase5_interface_dashboard_v1.md
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict


def _format_size(size_bytes: Any) -> str:
    if size_bytes is None:
        return "-"
    try:
        return str(int(size_bytes))
    except (TypeError, ValueError):
        return "-"


def _emit_section(title: str, assets: Dict[str, Dict[str, Any]]) -> str:
    lines = []
    lines.append(f"## {title}")
    lines.append("")
    if not assets:
        lines.append("_No entries in this section._")
        lines.append("")
        return "\n".join(lines)

    # Special-case: if some entries are non-path (e.g. notes)
    # we show them in a separate list after the table.
    path_rows = []
    non_path_rows = []

    for name, info in sorted(assets.items()):
        is_path = bool(info.get("is_path", False))
        exists = bool(info.get("exists", False))

        if is_path:
            relpath = info.get("relpath") or info.get("abspath") or "?"
            size = _format_size(info.get("size_bytes"))
            path_rows.append((name, relpath, exists, size))
        else:
            non_path_rows.append((name, info))

    if path_rows:
        lines.append("| key | relpath | exists | size_bytes |")
        lines.append("| --- | ------- | ------ | ---------- |")
        for name, relpath, exists, size in path_rows:
            exists_str = "yes" if exists else "no"
            lines.append(f"| `{name}` | `{relpath}` | {exists_str} | {size} |")
        lines.append("")

    if non_path_rows:
        lines.append("Non-path entries:")
        lines.append("")
        for name, info in non_path_rows:
            raw = info.get("raw_value", "")
            raw_clean = " ".join(str(raw).split())
            lines.append(f"- **{name}**: {raw_clean}")
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    summary_path = repo_root / "phase5/outputs/tables/phase5_interface_v1_summary.json"
    dashboard_path = repo_root / "phase5/outputs/tables/phase5_interface_dashboard_v1.md"

    if not summary_path.exists():
        raise SystemExit(
            f"[phase5_dashboard_v1] ERROR: summary JSON not found at {summary_path}"
        )

    data = json.loads(summary_path.read_text())

    diagnostics = data.get("diagnostics", {})
    phase3 = diagnostics.get("phase3", {})
    phase4 = diagnostics.get("phase4", {})
    external = diagnostics.get("external", {})

    interface_version = data.get("interface_version", "unknown")
    ts_json = data.get("timestamp_utc")
    ts_now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    lines = []
    lines.append("# Phase 5 Interface Dashboard (v1)")
    lines.append("")
    lines.append(f"- Interface version: `{interface_version}`")
    if ts_json:
        lines.append(f"- Summary timestamp (from JSON): `{ts_json}`")
    lines.append(f"- Dashboard generated at (UTC): `{ts_now}`")
    lines.append(
        "- Source summary: "
        "`phase5/outputs/tables/phase5_interface_v1_summary.json`"
    )
    lines.append("")
    lines.append(
        "This dashboard provides a human-readable view of the Phase 3 and "
        "Phase 4 assets consumed by Phase 5, plus any optional external "
        "datasets. It is derived from the JSON summary and should remain "
        "consistent with it."
    )
    lines.append("")

    lines.append(_emit_section("Phase 3 inputs", phase3))
    lines.append(_emit_section("Phase 4 inputs", phase4))
    lines.append(_emit_section("External inputs (optional)", external))

    dashboard_path.parent.mkdir(parents=True, exist_ok=True)
    dashboard_path.write_text("\n".join(lines))

    print(f"[phase5_dashboard_v1] Wrote dashboard to {dashboard_path}")


if __name__ == "__main__":
    main()
