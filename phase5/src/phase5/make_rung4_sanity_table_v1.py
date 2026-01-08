#!/usr/bin/env python
import json
import csv
from pathlib import Path
from datetime import datetime

REPO_ROOT = Path(__file__).resolve().parents[3]
PHASE5_ROOT = REPO_ROOT / "phase5"

INTERFACE_SUMMARY = PHASE5_ROOT / "outputs" / "tables" / "phase5_interface_v1_summary.json"
FRW_EXT_DIAGNOSTICS = REPO_ROOT / "phase4" / "outputs" / "tables" / "phase4_F1_frw_external_diagnostics.json"
OUT_CSV = PHASE5_ROOT / "outputs" / "tables" / "phase5_rung4_sanity_table_v1.csv"


def load_json(path: Path):
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main():
    if not INTERFACE_SUMMARY.exists():
        raise SystemExit(f"Missing interface summary: {INTERFACE_SUMMARY}")

    summary = load_json(INTERFACE_SUMMARY)
    diagnostics = summary.get("diagnostics", {})

    rows = []

    # Phase 3 + Phase 4 + external from interface summary
    for section_name, section_dict in diagnostics.items():
        if not isinstance(section_dict, dict):
            continue
        for key, entry in section_dict.items():
            if not isinstance(entry, dict):
                continue

            relpath = entry.get("relpath")
            exists = entry.get("exists")
            size_bytes = entry.get("size_bytes")

            row = {
                "section": section_name,
                "key": key,
                "relpath": relpath,
                "exists": exists,
                "size_bytes": size_bytes,
                "ext_status": "",
                "ext_n_rows": "",
                "ext_extra": "",
            }

            rows.append(row)

    # Optionally enrich the external diagnostics row if the JSON is present
    frw_ext = load_json(FRW_EXT_DIAGNOSTICS)
    if frw_ext is not None:
        # We do NOT assume a particular schema; we just pick up a few likely scalar keys if present.
        status = frw_ext.get("status")
        n_rows = frw_ext.get("n_rows")
        # Collect a small human-readable dump of other simple scalar keys
        extra_items = []
        for k, v in frw_ext.items():
            if k in {"status", "n_rows"}:
                continue
            if isinstance(v, (int, float, str, bool)) or v is None:
                extra_items.append(f"{k}={v!r}")
        extra_str = "; ".join(extra_items)

        # Find the interface row corresponding to frw_external_diagnostics, if any
        for row in rows:
            if (
                row["section"] == "phase4"
                and row["key"].endswith("frw_external_diagnostics")
            ):
                if status is not None:
                    row["ext_status"] = status
                if n_rows is not None:
                    row["ext_n_rows"] = n_rows
                if extra_str:
                    row["ext_extra"] = extra_str
                break

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "section",
                "key",
                "relpath",
                "exists",
                "size_bytes",
                "ext_status",
                "ext_n_rows",
                "ext_extra",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    print(f"[phase5_rung4_sanity] Wrote {OUT_CSV} ({OUT_CSV.stat().st_size} bytes)")
    print(f"[phase5_rung4_sanity] Timestamp UTC: {datetime.utcnow().isoformat()}Z")


if __name__ == "__main__":
    main()
