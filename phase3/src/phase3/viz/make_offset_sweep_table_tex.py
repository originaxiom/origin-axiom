import argparse
from pathlib import Path
import pandas as pd

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in_csv", required=True)
    ap.add_argument("--out_tex", required=True)
    args = ap.parse_args()

    df = pd.read_csv(args.in_csv)

    # Keep the key columns, rounded for paper readability
    cols = [
        "b_pmns_deg",
        "theta_best_deg",
        "chi2",
        "delta_chi2",
        "theta_68_lo_rad",
        "theta_68_hi_rad",
    ]
    df = df[cols].copy()

    df["b_pmns_deg"] = df["b_pmns_deg"].map(lambda x: f"{x:.0f}")
    df["theta_best_deg"] = df["theta_best_deg"].map(lambda x: f"{x:.3f}")
    df["chi2"] = df["chi2"].map(lambda x: f"{x:.6f}")
    df["delta_chi2"] = df["delta_chi2"].map(lambda x: f"{x:.6f}")
    df["theta_68_lo_rad"] = df["theta_68_lo_rad"].map(lambda x: f"{x:.6f}")
    df["theta_68_hi_rad"] = df["theta_68_hi_rad"].map(lambda x: f"{x:.6f}")

    out = Path(args.out_tex)
    out.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\caption{Discrete fixed-offset sweep for $b_{\mathrm{PMNS}}$ with a single fitted parameter $\theta$. Lower $\chi^2$ is better; $\Delta\chi^2$ is relative to the best row.}")
    lines.append(r"\label{tab:offset-sweep}")
    lines.append(r"\begin{tabular}{r r r r r r}")
    lines.append(r"\hline")
    lines.append(r"$b_{\mathrm{PMNS}}$ (deg) & $\theta^*$ (deg) & $\chi^2$ & $\Delta\chi^2$ & $\theta_{68\%}^{\mathrm{lo}}$ (rad) & $\theta_{68\%}^{\mathrm{hi}}$ (rad) \\")
    lines.append(r"\hline")
    for _, row in df.iterrows():
        lines.append(
            f"{row['b_pmns_deg']} & {row['theta_best_deg']} & {row['chi2']} & {row['delta_chi2']} & {row['theta_68_lo_rad']} & {row['theta_68_hi_rad']} \\\\"
        )
    lines.append(r"\hline")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
