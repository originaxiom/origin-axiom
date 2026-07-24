"""P2W5-ORGAN finalisation: merge the two robustness checks into results.json.

compute.py writes results.json (the sealed statistic and its verdict).
aux_convention.py and bc_check.py each answer a "declare every choice"
(WORKING_RULES #4) question about that verdict:
  - is the organ count NORMALISATION-robust?  (bbox diag / set diameter / raw)
  - is the organ count BOUNDARY-CONDITION-robust?  (periodic / open)
This script appends their computed answers under results.json["robustness"],
labelled with the script that produced each, and prints the final summary.
Re-runnable; it never edits a computed number, only attaches companions.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
res = json.load(open(os.path.join(HERE, "results.json")))
aux = json.load(open(os.path.join(HERE, "aux_convention.json")))
bc = json.load(open(os.path.join(HERE, "bc_check.json")))

res["robustness"] = {
    "normalisation": {
        "source": "aux_convention.py (depths 13,14; extended grid)",
        "conventions": ["e1/bbox_diagonal (sealed)", "e1/max_pairwise_diameter", "e1 raw"],
        "n_clusters_by_convention": aux["n_clusters_by_convention"],
        "identifiable_organs_bbox": aux["bbox"]["identifiable_organs"],
        "identifiable_organs_diam": aux["diam"]["identifiable_organs"],
        "identifiable_organs_raw": aux["raw"]["identifiable_organs"],
        "robust": aux["convention_robust"],
    },
    "boundary_condition": {
        "source": "bc_check.py (R3 grid at F=1597; extended grid at depths 13,14)",
        "word_identical_fib16_vs_metallic15": bc["word_identical"],
        "r3_banked_scan_reproduced_with_periodic_False": bc["r3_reproduced"],
        "r3_max_abs_diff": bc["r3_max_abs_diff"],
        "max_abs_periodic_minus_open_on_r3_grid": max(
            abs(a - b) for a, b in zip(bc["periodic_vals_r3grid"], bc["open_vals_r3grid"])),
        "open_bc_peaks": bc["open_bc_peaks"],
        "open_bc_identifiable_organs": bc["open_bc_organs"],
        "open_bc_n_clusters": bc["open_bc_n_clusters"],
        "periodic_bc_identifiable_organs": res["S1x_extended"]["identifiable_organs"],
        "periodic_bc_n_organs": len(res["S1x_extended"]["identifiable_organs"]),
        "robust": bc["bc_robust_two_organs"],
    },
}
res["verdict_qualifier"] = (
    "RESOLVED-A is the sealed cell criterion: a structurally discriminating "
    "statistic was designed, sealed, run and met its stated power (decision margin "
    f"{res['S1x_extended']['power_x_floor']:.2e} x the MEASURED floor; N3's box_dim "
    "floor was 1.7e8 x this statistic's floor; 0/27 depth-flapping pairs). The ORGAN "
    "COUNT it returns is conditional on the declared boundary condition: PERIODIC (the "
    "sealed convention) gives 2 identifiable organs (kappa 0.95, 1.60) and exactly 1 "
    "inside N3's plateau [0.80,1.55]; OPEN gives 1 identifiable organ (kappa 1.15). "
    "The count is normalisation-robust but NOT boundary-condition-robust. N3's own "
    "candidate peaks (1.10, 1.45) are peaks of NEITHER."
)
json.dump(res, open(os.path.join(HERE, "results.json"), "w"), separators=(",", ":"))

print("=" * 70)
print("P2W5-ORGAN FINAL")
print("=" * 70)
print(f"  CELL VERDICT     : {res['verdict']}  ({res['organ_call']})")
print(f"  sealed-window RAW: {res['S1_sealed_window']['raw_verdict']} "
      f"-> bound-hugging organ {res['S1_sealed_window']['bound_hugging']} dropped "
      f"-> {res['S1_sealed_window']['filtered_verdict']}")
print(f"  extended window  : organs {res['S1x_extended']['identifiable_organs']}")
print(f"  inside plateau   : {res['plateau_organs']}  ({len(res['plateau_organs'])} organ)")
print(f"  S3 clusters      : {res['S3']['clusters']}  ({res['S3']['n_clusters']})")
print(f"  S2 gap regime    : {res['S2']['verdict']} (l1 == 0.38197 = F(n-2)/F(n) everywhere)")
print(f"  power            : S1x {res['S1x_extended']['power_x_floor']:.2e} x floor, "
      f"S3 {res['S3']['power_x_floor']:.2e} x floor; floor {res['floor']['used']:.2e}")
print(f"  N3 floor ratio   : {res['floor']['n3_over_this']:.2e} "
      f"(N3's jitter floor / this statistic's floor)")
print(f"  normalisation-robust: {res['robustness']['normalisation']['robust']}")
print(f"  BC-robust           : {res['robustness']['boundary_condition']['robust']} "
      f"(open BC: {res['robustness']['boundary_condition']['open_bc_identifiable_organs']})")
print(f"  R3 banked scan reproduced with periodic=False, max|diff| = "
      f"{res['robustness']['boundary_condition']['r3_max_abs_diff']:.1e}")
print("\n" + res["verdict_qualifier"])
print("\nwritten: results.json (robustness block appended)")
