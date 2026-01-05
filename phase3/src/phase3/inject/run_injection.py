import argparse
import json
from pathlib import Path
from typing import Dict, Any

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def vacuum_residue_metric(theta: float) -> float:
    """
    Placeholder hook: inject theta into the Phase 2 vacuum mechanism.
    Phase 3 TODO:
      - import / wrap Phase 2 module entrypoint OR
      - re-expose a stable API from phase2 to compute residue metric
    """
    # Minimal illustrative curve; replace with real mechanism call.
    return 1.0 + 0.02 * np.cos(theta)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--theta_summary", required=True)
    ap.add_argument("--out_fig", required=True)
    args = ap.parse_args()

    theta_summary = Path(args.theta_summary)
    out_fig = Path(args.out_fig)
    out_fig.parent.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(theta_summary)
    theta_best = float(df.loc[0, "theta_best_rad"])

    thetas = np.linspace(0.0, 2.0*np.pi, 721)
    vals = np.array([vacuum_residue_metric(th) for th in thetas])

    plt.figure()
    plt.plot(thetas, vals)
    plt.axvline(theta_best, linestyle="--")
    plt.xlabel("theta [rad]")
    plt.ylabel("delta_rho_vac (normalized)")
    plt.tight_layout()
    plt.savefig(out_fig)
    plt.close()

    meta = {
        "theta_best_rad": theta_best,
        "metric_definition": "placeholder; replace with phase2 vacuum mechanism call",
    }
    meta_path = out_fig.with_suffix(".meta.json")
    meta_path.write_text(json.dumps(meta, indent=2))

if __name__ == "__main__":
    main()
