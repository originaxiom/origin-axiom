import csv
from pathlib import Path

def load_kernel(path):
    rows = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            def as_int(name):
                v = row.get(name)
                if v is None or v == "":
                    return 0
                try:
                    return int(v)
                except ValueError:
                    return 0
            rows.append({
                "theta": float(row["theta"]),
                "in_pre_data_kernel": as_int("in_pre_data_kernel"),
                "lcdm_like": as_int("lcdm_like"),
                "in_toy_corridor": as_int("in_toy_corridor"),
                "shape_and_viable": as_int("shape_and_viable"),
                "shape_and_lcdm": as_int("shape_and_lcdm"),
            })
    return rows

def family_mask(rows, name):
    if name == "ALL_GRID":
        return [True] * len(rows)
    if name == "PRE_DATA_KERNEL":
        return [r["in_pre_data_kernel"] == 1 for r in rows]
    if name == "LCDM_LIKE":
        return [r["lcdm_like"] == 1 for r in rows]
    if name == "TOY_CORRIDOR":
        return [r["in_toy_corridor"] == 1 for r in rows]
    if name == "KERNEL_AND_LCDM":
        return [(r["in_pre_data_kernel"] == 1 and r["lcdm_like"] == 1) for r in rows]
    if name == "KERNEL_AND_TOY":
        return [(r["in_pre_data_kernel"] == 1 and r["in_toy_corridor"] == 1) for r in rows]
    if name == "LCDM_AND_TOY":
        return [(r["lcdm_like"] == 1 and r["in_toy_corridor"] == 1) for r in rows]
    if name == "KERNEL_AND_LCDM_AND_TOY":
        return [(r["in_pre_data_kernel"] == 1 and r["lcdm_like"] == 1 and r["in_toy_corridor"] == 1) for r in rows]
    if name == "SHAPE_AND_VIABLE":
        return [r["shape_and_viable"] == 1 for r in rows]
    if name == "SHAPE_AND_LCDM":
        return [r["shape_and_lcdm"] == 1 for r in rows]
    raise ValueError(f"Unknown family: {name}")

def main():
    repo_root = Path(__file__).resolve().parents[3]
    kernel_path = repo_root / "stage2" / "obstruction_tests" / "outputs" / "tables" / "stage2_obstruction_static_frw_kernel_v1.csv"
    if not kernel_path.exists():
        raise SystemExit(f"Missing kernel table: {kernel_path}")
    rows = load_kernel(kernel_path)
    n_grid = len(rows)
    n_kernel = sum(r["in_pre_data_kernel"] == 1 for r in rows)

    families = [
        "ALL_GRID",
        "PRE_DATA_KERNEL",
        "LCDM_LIKE",
        "TOY_CORRIDOR",
        "KERNEL_AND_LCDM",
        "KERNEL_AND_TOY",
        "LCDM_AND_TOY",
        "KERNEL_AND_LCDM_AND_TOY",
        "SHAPE_AND_VIABLE",
        "SHAPE_AND_LCDM",
    ]

    out_dir = repo_root / "stage2" / "obstruction_tests" / "outputs" / "tables"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "stage2_obstruction_static_frw_kernel_families_v1.csv"

    fieldnames = ["family_name", "n_points", "frac_of_grid", "frac_of_kernel", "note"]

    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for fam in families:
            mask = family_mask(rows, fam)
            n_points = sum(1 for m in mask if m)
            if n_grid > 0:
                frac_grid = n_points / n_grid
            else:
                frac_grid = 0.0
            if fam == "ALL_GRID":
                frac_kernel = ""
            else:
                if n_kernel > 0:
                    frac_kernel = n_points / n_kernel
                else:
                    frac_kernel = ""
            note = ""
            if fam == "PRE_DATA_KERNEL":
                note = "defined by frw_viable = 1 in current Phase 4 snapshot"
            if fam == "KERNEL_AND_LCDM_AND_TOY":
                note = "triple intersection: kernel ∩ lcdm_like ∩ toy corridor"
            writer.writerow({
                "family_name": fam,
                "n_points": n_points,
                "frac_of_grid": f"{frac_grid:.6f}",
                "frac_of_kernel": "" if frac_kernel == "" else f"{frac_kernel:.6f}",
                "note": note,
            })

    print(f"[stage2_obstruction_static_frw_kernel_families_v1] Repo root: {repo_root}")
    print(f"[stage2_obstruction_static_frw_kernel_families_v1] Input: {kernel_path}")
    print(f"[stage2_obstruction_static_frw_kernel_families_v1] Grid points: {n_grid}, pre-data kernel size: {n_kernel}")
    print(f"[stage2_obstruction_static_frw_kernel_families_v1] Output: {out_path}")
    print("[stage2_obstruction_static_frw_kernel_families_v1] Done.")

if __name__ == "__main__":
    main()
