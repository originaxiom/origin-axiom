#!/usr/bin/env python3

"""
Stage 2 — FRW empirical anchor mask (v1)

Reads Phase 4 FRW background outputs and applies a schematic
empirical anchor box defined in a JSON config.

This is a diagnostic-only, downstream analysis.
No claims are made or promoted at this rung.
"""

from pathlib import Path
import json
import pandas as pd

# Resolve repo root
REPO_ROOT = Path(__file__).resolve().parents[3]

# Paths
FRW_TABLE = REPO_ROOT / "phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv"
ANCHOR_CONFIG = REPO_ROOT / "stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json"
OUT_DIR = REPO_ROOT / "stage2/frw_data_probe_analysis/outputs/tables"
OUT_TABLE = OUT_DIR / "stage2_frw_empirical_anchor_mask_v1.csv"

# Load inputs
df = pd.read_csv(FRW_TABLE)
with open(ANCHOR_CONFIG, "r", encoding="utf-8") as f:
    anchor = json.load(f)

# Extract anchor parameters
omega_c = anchor["omega_lambda"]["center"]
omega_w = anchor["omega_lambda"]["half_width"]
age_c = anchor["age_Gyr"]["center"]
age_w = anchor["age_Gyr"]["half_width"]

# Required columns check
required_cols = ["theta", "omega_lambda", "age_Gyr"]
missing = [c for c in required_cols if c not in df.columns]
if missing:
    raise RuntimeError(f"Missing required columns in FRW table: {missing}")

# Compute anchor mask
df_out = df[required_cols].copy()
df_out["in_empirical_anchor_box"] = (
    (df_out["omega_lambda"] >= omega_c - omega_w) &
    (df_out["omega_lambda"] <= omega_c + omega_w) &
    (df_out["age_Gyr"] >= age_c - age_w) &
    (df_out["age_Gyr"] <= age_c + age_w)
)

# Write output
OUT_DIR.mkdir(parents=True, exist_ok=True)
df_out.to_csv(OUT_TABLE, index=False)

print("[stage2_empirical_anchor_rung3]")
print(f"  Input FRW table: {FRW_TABLE}")
print(f"  Anchor config:   {ANCHOR_CONFIG}")
print(f"  Output written:  {OUT_TABLE}")
print(f"  Rows: {len(df_out)}, in_anchor: {df_out['in_empirical_anchor_box'].sum()}")
