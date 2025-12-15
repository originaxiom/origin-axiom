#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Load the FRW-from-effective-vacuum data
data_path = Path("data/processed/frw_from_effective_vacuum.npz")
d = np.load(data_path)

print("Available arrays in frw_from_effective_vacuum.npz:", d.files)

# Use the actual keys from the file
t_m = d["t_matter_only"]
a_m = d["a_matter_only"]

t_eff = d["t_effective"]
a_eff = d["a_effective"]

# 2. Make the plot
plt.figure()
plt.plot(t_m, a_m, label="Matter-only FRW")
plt.plot(t_eff, a_eff, linestyle="--", label="Effective-vacuum FRW")

plt.xlabel("t (arb. units)")
plt.ylabel("a(t)")
plt.title("FRW toy: matter-only vs effective vacuum")
plt.legend()
plt.tight_layout()

# 3. Save to docs/paper/figures as PDF
fig_dir = Path("docs/paper/figures")
fig_dir.mkdir(parents=True, exist_ok=True)

out_path = fig_dir / "frw_from_effective_vacuum_a_of_t.pdf"
plt.savefig(out_path, bbox_inches="tight")
print("Saved:", out_path)