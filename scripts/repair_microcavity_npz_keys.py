import numpy as np
from pathlib import Path

root = Path("data/processed")

targets = list(root.glob("microcavity_sweep_*.npz"))

print(f"Found {len(targets)} NPZ files.")

for npz_path in targets:
    print(f"\n--- Checking {npz_path.name} ---")
    arr = np.load(npz_path)

    keys = arr.files
    needs_write = False
    new_dict = {k: arr[k] for k in keys}

    # Ensure delta_E exists
    if "deltaE" in keys and "delta_E" not in keys:
        print("  Adding alias key: delta_E → deltaE")
        new_dict["delta_E"] = arr["deltaE"]
        needs_write = True

    # Ensure theta_grid exists (alias just in case)
    if "theta" in keys and "theta_grid" not in keys:
        print("  Adding alias key: theta_grid → theta")
        new_dict["theta_grid"] = arr["theta"]
        needs_write = True

    if needs_write:
        np.savez(npz_path, **new_dict)
        print("  ✔ Rewritten safely.")
    else:
        print("  No changes needed.")