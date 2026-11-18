"""B1957: the physical lane's reconciliation of its files that are not notes (NON_MARKDOWN_COVERAGE.md at aa9facef6): the
counts and pointers main can check from the repository, with nothing of the lane's run or imported (data-free).
 V1  the number of paths that are not markdown, added or changed in its window 1aa76251..8d5c91032; its table's counts.
 V2  the twelve methods of its unrun mathematical checker, at the lines it names (the file is read as text).
 V3  the control it makes explicit: the fixed points of M^2 on the torus (det(M^2 - I)); the key in its result file.
 V4  the keys of its two result files that its tables name as check groups."""
import json, pathlib, re, subprocess
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent; ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True, cwd=ROOT).stdout
D = "reports/physical_bridge_2026_09_05/"; PIN = "8d5c91032"
names = [l for l in git("diff", "--name-only", "--diff-filter=AM", "1aa76251", PIN).split("\n") if l and not l.endswith(".md")]
table = {"provenance, specification and quotations": 67, "mathematical checker source": 3, "historical mathematical output": 2, "empty preserved streams": 4, "proposed checker repair": 1, "custody collector": 1, "execution infrastructure": 2, "engineering receipts and logs": 4}
print("V1: paths that are not markdown in the window: %d (the lane says 84); its table's eight counts sum to %d; by extension: %s" % (len(names), sum(table.values()), dict(sorted({e: sum(1 for x in names if x.endswith(e)) for e in {pathlib.Path(x).suffix for x in names}}.items()))))
src = git("show", "%s:%sregistered_domain_index_join_2026_11_16/verification/checks.py" % (PIN, D)).split("\n")
want = [("test_quaternion_relations_and_conjugation_generators", 64), ("test_coupling_span_full_and_traceless", 91), ("test_coupling_covariance_and_unsigned_counterexample", 103), ("test_inner_residual_and_vertical_spin_sheet", 128),
        ("test_full_and_slot_family_constant_stabilizers", 167), ("test_source_cubic_and_polarization", 219), ("test_root_vertex_and_physical_mass_derivative", 237), ("test_normalized_vertex_current_and_rescalings", 256),
        ("test_shape_inequality_exact_metric_controls", 289), ("test_slot_rank_and_illicit_form_entry", 305), ("test_full_complement_response_and_backreaction", 315), ("test_complex_bilinear_gram_and_current_transport", 359)]
found = [(n, ln) for n, ln in want if len(src) >= ln and ("def %s(" % n) in src[ln - 1]]; all_tests = [l for l in src if re.match(r"\s+def test_", l)]
print("V2: the lane's unrun checker, read as text at %s: %d of its 12 named methods are at the lines named; the file defines %d test methods in all" % (PIN, len(found), len(all_tests)))
M = sp.Matrix([[2, 1], [1, 1]]); K = M ** 2 - sp.eye(2)
fixed = sum(1 for a in range(45) for b in range(45) if all(x % 45 == 0 for x in (K * sp.Matrix([a, b]))))
res = json.loads(git("show", "%s:%sagy_exp_endgame_review_2026_11_15/run01/result.json" % (PIN, D)) or "{}")
def find(o, key):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == key: return v
            r = find(v, key)
            if r is not None: return r
    elif isinstance(o, list):
        for v in o:
            r = find(v, key)
            if r is not None: return r
print("V3: M^2 - I = %s, determinant %s; points of the denominator-45 grid fixed by M^2: %d; the lane's result file holds degree2_fixed_point_count = %s (a key main's first comparison did not include)" % (K.tolist(), K.det(), fixed, find(res, "degree2_fixed_point_count")))
res2 = json.loads(git("show", "%s:%srelative_register_boundary_law_2026_11_15/run01/result.json" % (PIN, D)) or "{}")
g1 = [k for k in ("exact_topology_and_orbits", "weil_order", "majorana_coefficient_freedom", "ordered_yukawa_products", "rank_one_two_loop_mixing", "gluing_area_and_collar") if find(res, k) is not None]
g2 = [k for k in ("finite_cell_response", "reference_and_sector_controls", "cut_and_source_controls", "smooth_radial_control") if find(res2, k) is not None]
print("V4: check groups named by the note and present as keys of the two result files: %d of 6 and %d of 4" % (len(g1), len(g2)))
