import csv
from pathlib import Path

def read_csv_by_theta(path, float_cols=None, int_cols=None):
    float_cols = float_cols or []
    int_cols = int_cols or []
    data = {}
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                theta = float(row["theta"])
            except (KeyError, ValueError):
                raise RuntimeError(f"File {path} is missing a valid 'theta' column")
            cleaned = {}
            for k, v in row.items():
                if k == "theta":
                    continue
                if v is None or v == "":
                    cleaned[k] = None
                    continue
                if k in float_cols:
                    try:
                        cleaned[k] = float(v)
                    except ValueError:
                        cleaned[k] = None
                elif k in int_cols:
                    try:
                        cleaned[k] = int(v)
                    except ValueError:
                        cleaned[k] = None
                else:
                    cleaned[k] = v
            data[theta] = cleaned
    return data

def main():
    repo_root = Path(__file__).resolve().parents[3]
    phase4_tables = repo_root / "phase4" / "outputs" / "tables"
    out_dir = repo_root / "stage2" / "obstruction_tests" / "outputs" / "tables"
    out_dir.mkdir(parents=True, exist_ok=True)

    data_probe_path = phase4_tables / "phase4_F1_frw_data_probe_mask.csv"
    viability_path = phase4_tables / "phase4_F1_frw_viability_mask.csv"
    lcdm_path = phase4_tables / "phase4_F1_frw_lcdm_probe_mask.csv"
    shape_path = phase4_tables / "phase4_F1_frw_shape_probe_mask.csv"

    if not data_probe_path.exists():
        raise SystemExit(f"Missing input: {data_probe_path}")
    if not viability_path.exists():
        raise SystemExit(f"Missing input: {viability_path}")
    if not lcdm_path.exists():
        raise SystemExit(f"Missing input: {lcdm_path}")
    if not shape_path.exists():
        raise SystemExit(f"Missing input: {shape_path}")

    floats = ["E_vac", "omega_lambda", "age_Gyr", "chi2_data", "chi2_per_dof"]
    ints_data = ["has_matter_era", "has_late_accel", "smooth_H2", "frw_viable", "data_ok"]
    data_probe = read_csv_by_theta(data_probe_path, float_cols=floats, int_cols=ints_data)

    ints_viab = ["has_matter_era", "has_late_accel", "smooth_H2", "frw_viable"]
    viability = read_csv_by_theta(viability_path, float_cols=["E_vac", "omega_lambda", "age_Gyr"], int_cols=ints_viab)

    lcdm = read_csv_by_theta(lcdm_path, float_cols=["E_vac", "omega_lambda", "age_Gyr"], int_cols=["frw_viable", "lcdm_like"])

    shape = read_csv_by_theta(
        shape_path,
        float_cols=["E_vac", "omega_lambda", "age_Gyr"],
        int_cols=["in_toy_corridor", "frw_viable", "lcdm_like", "shape_and_viable", "shape_and_lcdm"],
    )

    all_thetas = sorted(set(data_probe.keys()) & set(viability.keys()) & set(lcdm.keys()) & set(shape.keys()))
    if not all_thetas:
        raise SystemExit("No overlapping theta values across FRW masks")

    out_path = out_dir / "stage2_obstruction_static_frw_kernel_v1.csv"
    fieldnames = [
        "theta",
        "E_vac",
        "omega_lambda",
        "age_Gyr",
        "has_matter_era",
        "has_late_accel",
        "smooth_H2",
        "frw_viable",
        "lcdm_like",
        "in_toy_corridor",
        "shape_and_viable",
        "shape_and_lcdm",
        "data_ok",
        "chi2_data",
        "chi2_per_dof",
        "in_pre_data_kernel",
    ]

    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        n_total = 0
        n_kernel = 0
        for theta in all_thetas:
            row_data = {}
            dp = data_probe[theta]
            vb = viability[theta]
            lc = lcdm[theta]
            sh = shape[theta]
            n_total += 1

            row_data["theta"] = theta
            row_data["E_vac"] = dp.get("E_vac")
            row_data["omega_lambda"] = dp.get("omega_lambda")
            row_data["age_Gyr"] = dp.get("age_Gyr")

            row_data["has_matter_era"] = dp.get("has_matter_era")
            row_data["has_late_accel"] = dp.get("has_late_accel")
            row_data["smooth_H2"] = dp.get("smooth_H2")
            frw_viable = dp.get("frw_viable")
            row_data["frw_viable"] = frw_viable

            row_data["lcdm_like"] = lc.get("lcdm_like")
            row_data["in_toy_corridor"] = sh.get("in_toy_corridor")
            row_data["shape_and_viable"] = sh.get("shape_and_viable")
            row_data["shape_and_lcdm"] = sh.get("shape_and_lcdm")

            row_data["data_ok"] = dp.get("data_ok")
            row_data["chi2_data"] = dp.get("chi2_data")
            row_data["chi2_per_dof"] = dp.get("chi2_per_dof")

            in_kernel = False
            if isinstance(frw_viable, int):
                in_kernel = frw_viable == 1
            elif isinstance(frw_viable, str):
                in_kernel = frw_viable.strip() == "1"
            row_data["in_pre_data_kernel"] = 1 if in_kernel else 0
            if in_kernel:
                n_kernel += 1

            writer.writerow(row_data)

    print(f"[stage2_obstruction_static_frw_kernel_v1] Repo root: {repo_root}")
    print(f"[stage2_obstruction_static_frw_kernel_v1] Input tables:")
    print(f"  - {data_probe_path}")
    print(f"  - {viability_path}")
    print(f"  - {lcdm_path}")
    print(f"  - {shape_path}")
    print(f"[stage2_obstruction_static_frw_kernel_v1] Output: {out_path}")
    print(f"[stage2_obstruction_static_frw_kernel_v1] Grid points: {n_total}, pre-data kernel size: {n_kernel}")
    print("[stage2_obstruction_static_frw_kernel_v1] Done.")

if __name__ == "__main__":
    main()
