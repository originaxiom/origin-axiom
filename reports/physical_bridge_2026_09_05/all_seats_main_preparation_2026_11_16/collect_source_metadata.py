"""Read Git blobs and record quoted locations, hashes and existing JSON flags.

This metadata utility imports or executes no scientific project code.
It never computes a model observable and never changes an upstream file.
"""

import hashlib
import json
from pathlib import Path
import subprocess


OUT = Path(__file__).resolve().parent
REFS = {
    "exp": "origin/agy/self-consistent-loop-2026-11-11",
    "endgame": "origin/agy-002/endgame",
    "agy": "origin/agy/audit-2026-11-02",
}
TARGETS = json.loads((OUT / "TARGET_HEADS.json").read_text())
HEADS = {name: TARGETS[ref] for name, ref in REFS.items()}
P4 = "relays/x_closure_4_verify/verify_x_closure_4.py"
P3 = "relays/x_closure_3_verify/verify_x_closure_3.py"
P2 = "relays/x_closure_2_verify/verify_x_closure_2.py"
P1 = "relays/x_closure_1_verify/verify_x_closure_1.py"
G1 = "relays/agy002_endgame_v2_g1_fixed/verify_endgame_v2_g1_fixed.py"
G2 = "relays/agy002_endgame_v2_g2/verify_endgame_v2_g2.py"
G2R = "relays/agy002_endgame_v2_g2_referee/referee_endgame_v2_g2.py"
G3 = "relays/agy002_endgame_v2_g3/verify_endgame_v2_g3.py"

# Every matching occurrence is recorded. Interpretations must cite the
# applicable exact line, rather than silently assuming a unique substring.
QUOTES = [
    ("F01", "exp", P4, '"statement": "Repaired BPV 2-loop mixed-Yukawa adjoint'),
    ("F01", "exp", P4, "def tropical_svd_exponents_exact"),
    ("F01", "exp", P4, "e5_s2 = tropical_svd_exponents_exact"),
    ("F02", "exp", P4, '"id": "T_IB_08_step_converged'),
    ("F02", "exp", P4, "g_uv_ref, g_uv_ref, g_uv_ref, lam_uv_ref, dln_cover, n_steps=600, repaired_mixed_order=True,"),
    ("F02", "exp", P4, "except Exception:"),
    ("F03", "endgame", "relays/AGY002_ENDGAME_V2_MASTER_SYNTHESIS.md", "chiral boundary conditions on"),
    ("F03", "endgame", G1, "Yu = Au @ Au.conj().T"),
    ("F03", "endgame", G1, "th_uv, j_uv, _ = extract_quark_cp_observables"),
    ("F04", "endgame", G2, "loop_pref = (4 * math.pi / 50)"),
    ("F04", "endgame", G2, "for af, bf in pts5:"),
    ("F04", "endgame", G2R, "kappa_loop = 1 / (4 * math.pi)"),
    ("F04", "endgame", G2R, "y_mat = cim_triple_closed_form(geodesic_tau(float(s_val)), 0, 0)"),
    ("F05", "exp", P4, '"statement": "Repaired 2^{-1} mod N'),
    ("F05", "exp", P1, "s_pref = inv_sqrt / gamma_n"),
    ("F06", "exp", P3, "pure_form_cubic_zero = True"),
    ("F06", "exp", P3, "odd_vs_aligned_diff = 0"),
    ("F06", "exp", P3, "form_count_twisted = 2"),
    ("F06", "exp", P2, "central_sheet_aligned = {"),
    ("F07", "exp", "relays/AGY_EXP_TO_PHYSICAL_AND_CC_2026-11-16_X_CLOSURE_1_RESULTS.md", "irrational distance"),
    ("F08", "agy", "relays/STATUS_AGY.md", "Six of the seven upstream stages"),
    ("F09", "endgame", G3, "d_S = 16"),
    ("F09", "endgame", G3, "delta_sm_mp = mp.mpf(28)"),
    ("F10", "endgame", "relays/agy002_endgame_v2_g0_fixed/verify_endgame_v2_g0_fixed_out.json", '"gate_0_passed": false'),
    ("F10", "endgame", "relays/agy002_endgame_v2_g2_referee/referee_endgame_v2_g2_out.json", '"gate_2_countercheck_passed": false'),
    ("F10", "endgame", "relays/agy002_endgame_v2_g3_referee/referee_endgame_v2_g3_out.json", '"gate_3_referee_passed": false'),
]


def dump(name, obj):
    (OUT / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


items = []
for finding, seat, path, needle in QUOTES:
    blob = subprocess.check_output(["git", "show", HEADS[seat] + ":" + path])
    hits = [(n, line) for n, line in enumerate(blob.decode().splitlines(), 1) if needle in line]
    if not hits:
        raise ValueError((finding, path, needle))
    for number, line in hits:
        items.append({
            "finding": finding, "commit": HEADS[seat], "path": path,
            "line": number, "quote": line,
            "sha256": hashlib.sha256(blob).hexdigest(),
        })
dump("QUOTED_SOURCE_EVIDENCE.json", {
    "method": "Git blob reads and exact substring/line matching. No scientific execution.",
    "items": items,
})

current = TARGETS
before = json.loads((OUT / "BASELINE_HEADS.json").read_text())
dump("FETCH_COMPARISON.json", {
    "date": "2026-11-16", "operation": "git fetch --prune origin", "exit_code": 0,
    "remote": "https://github.com/originaxiom/origin-axiom.git", "heads": current,
    "changed_external_heads": [
        {"ref": ref, "before": before.get(ref), "after": head}
        for ref, head in current.items()
        if before.get(ref) != head and ref != "origin/audit/physical-bridge-2026-09-05"
    ],
    "scientific_execution": "none",
    "inherited_staged_diff_sha256": hashlib.sha256(subprocess.check_output([
        "git", "diff", "--cached", "--binary",
    ])).hexdigest(),
})
inventory = json.loads((OUT / "SOURCE_INVENTORY.json").read_text())["files"]
for item in inventory:
    blob = subprocess.check_output(["git", "show", item["commit"] + ":" + item["path"]])
    if hashlib.sha256(blob).hexdigest() != item["sha256"]:
        raise ValueError(("source hash differs", item["path"]))
print(json.dumps({"quoted_locations": len(items), "checked_source_hashes": len(inventory)}))
