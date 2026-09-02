"""B1238 -- the seat harvest, third ring. Locks, in order of what they protect:

  1. THE IDENTITY: 4*Phi(x,z) = (2z - x^2 - 1)^2 - (x^2-1)(x^2-5) -- B211's character variety IS B509's
     square-time curve (recomputed by sympy here, not read from a file); the quotient map to 40a1 and the
     involution sigma (fixed-point-free on X^na) that realises it.
  2. THE LABEL: Jac(Phi) has minimal model [0,0,0,-2,1] = Cremona 40a3, torsion Z/4, j = 55296/5 (PARI);
     the a_p that B211 counted are the same across the isogeny class (why the old evidence could not tell).
  3. THE PROPAGATION (E53 #16-#18): the correction lives in B211's own verdict file, B362 is superseded by
     B367 in its own file, the four "degree 6" arcs carry the octic, and every addendum exists.
  4. THE REGISTER: I-12 is EARNED and the UNEARNED baseline is untouched (the ratchet's other direction).
  5. BRONZE: the octic is irreducible, has field discriminant 391728981, signature (0,4), and is its own
     polredabs (PARI); the two-route computation itself is the slow lane (reproduce.sh, OA_SLOW).
  6. R39: the Z1 rerun equals main's banked P2W4-Z1 ladder at every level it reached (nothing was lost).
"""
import json
import os
import pathlib
import subprocess
import sys

import pytest
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1238_seat_harvest_40a3_bronze_octic"
VER = ARC / "verification"
X, Z = sp.symbols("x z")
PHI = Z**2 - (X**2 + 1)*Z + (2*X**2 - 1)
OCTIC = "x^8 + 6*x^6 - x^5 + 12*x^4 - 3*x^3 + 8*x^2 - x + 2"


def _verdict(d):
    return json.loads((ROOT / "frontier" / d / "arc_verdict.json").read_text(encoding="utf-8"))


def _pari():
    pytest.importorskip("cypari")
    import cypari
    return cypari.pari


# 1. the identity ---------------------------------------------------------------------------------
def test_character_variety_is_the_square_time_curve():
    c, d = X, 2*Z - X**2 - 1
    assert sp.expand(d**2 - (c**2 - 1)*(c**2 - 5) - 4*PHI) == 0
    # B509's geometric point (c=2, d^2=-3) is Phi's complete-structure point x=2
    assert sp.expand(PHI.subs(X, 2) - (Z**2 - 5*Z + 7)) == 0
    assert sp.expand(d.subs(X, 2)**2 + 3 - 4*PHI.subs(X, 2)) == 0
    # rational points: (+-1, 1) lie on Phi
    assert PHI.subs({X: 1, Z: 1}) == 0 and PHI.subs({X: -1, Z: 1}) == 0


def test_40a1_is_the_sigma_quotient():
    Xq, Yq = X**2, X*(2*Z - X**2 - 1)
    q, r = sp.div(sp.expand(Yq**2 - Xq*(Xq - 1)*(Xq - 5)), PHI, Z)
    assert r == 0 and sp.expand(q - 4*X**2) == 0
    sig = PHI.subs({X: -X, Z: X**2 + 1 - Z}, simultaneous=True)
    assert sp.expand(sig - PHI) == 0
    # sigma's only affine fixed point (0, 1/2) is NOT on X^na: the involution is fixed-point-free there
    assert PHI.subs({X: 0, Z: sp.Rational(1, 2)}) == sp.Rational(-5, 4)


# 2. the label -------------------------------------------------------------------------------------
def test_jacobian_is_cremona_40a3_not_40a1():
    pari = _pari()
    J = "ellfromeqn(w^2 - (x^4 - 6*x^2 + 5))"
    assert list(pari(f"ellminimalmodel(ellinit({J}))")[0:5]) == [0, 0, 0, -2, 1]
    assert pari(f"ellglobalred(ellinit({J}))")[0] == 40
    assert pari(f"ellinit({J}).j") == pari("55296/5")
    assert pari(f"elltors(ellinit({J}))")[1] == pari("[4]")                    # Z/4, not Z/2 x Z/2
    E1 = "ellinit([0,-6,0,5,0])"                                                # y^2 = x(x-1)(x-5) = 40a1
    assert pari(f"{E1}.j") == pari("148176/25") and pari(f"elltors({E1})")[1] == pari("[2, 2]")
    for p in (3, 7, 11, 13, 17, 19):                                            # same a_p: isogeny-invariant
        assert pari(f"ellap(ellinit({J}), {p})") == pari(f"ellap({E1}, {p})")
    assert list(pari("ellrank(ellinit([0,0,0,-2,1]))")[0:2]) == [0, 0]         # B509's rank 0, for X^na itself


# 3. the propagation -------------------------------------------------------------------------------
def test_b211_carries_the_correction_in_its_own_file():
    d = _verdict("B211_metallic_arithmetic_geometric_faces")
    assert d["verdict"] == "PROVED"
    assert d["claim_one_line"].startswith("CORRECTED 2026-09-02 (B1238)") and "40a3" in d["claim_one_line"]
    assert "ORIGINAL CLAIM AS ASSERTED: " in d["claim_one_line"]
    assert "B1238" in d["note"] and "40a3" in d["note"]


def test_b362_is_superseded_by_b367_in_its_own_file():
    d = _verdict("B362_seam_law_confirmations")
    assert d["superseded_by"] == "B367"
    assert d["claim_one_line"].startswith("SUPERSEDED by B367")
    assert d["verdict"] == "PROVED"                                 # not RETRACTED (B818)


@pytest.mark.parametrize("arc", ["B125_snappy_arithmeticity", "B137_s031_sealing_m2", "B840_close_loose_ends"])
def test_degree_six_sites_carry_the_octic(arc):
    d = _verdict(arc)
    assert "degree 8" in d["note"] and "B1238" in d["note"]


@pytest.mark.parametrize("path,line_hint", [
    ("B125_snappy_arithmeticity/FINDINGS.md", "canonical 6) [B1238, 2026-09-02:"),
    ("B137_s031_sealing_m2/FINDINGS.md", "1.8e-142) [B1238, 2026-09-02:"),
    ("B578_debt_clearing/RESULTS.md", "[B1238, 2026-09-02:"),          # no verdict file: RESULTS is the record
    ("B840_close_loose_ends/FINDINGS.md", "**degree 6**. [B1238, 2026-09-02:"),
])
def test_degree_six_sites_are_bracketed_in_place(path, line_hint):
    s = (ROOT / "frontier" / path).read_text(encoding="utf-8")
    assert line_hint in s and "degree **8**" in s


@pytest.mark.parametrize("arc", ["B211_metallic_arithmetic_geometric_faces", "B213_higgs_side_periods",
                                 "B362_seam_law_confirmations", "B509_square_time_curve",
                                 "B510_convening_resolution", "B125_snappy_arithmeticity",
                                 "B137_s031_sealing_m2", "B578_debt_clearing", "B840_close_loose_ends",
                                 "B1062_bridge_cell", "B778_cleanup", "B1060_digest_ledger"])
def test_addendum_exists(arc):
    assert (ROOT / "frontier" / arc / "ADDENDUM_2026-09-02_B1238.md").is_file()


def test_b778_pending_block_points_to_its_own_completion():
    s = (ROOT / "frontier" / "B778_cleanup" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "## COMPLETION (2026-07-24)" in s
    assert "[B1238, 2026-09-02:" in s and s.index("[B1238, 2026-09-02:") < s.index("## COMPLETION (2026-07-24)")


# 4. the register ----------------------------------------------------------------------------------
def test_i12_is_earned_and_the_ratchet_baseline_is_untouched():
    led = (ROOT / "docs" / "IDENTIFICATION_LEDGER.md").read_text(encoding="utf-8")
    row = next(l for l in led.splitlines() if l.startswith("| I-12 |"))
    assert "**EARNED**" in row and "40a3" in row and "(c,d) = (x, 2z−x²−1)" in row
    base = json.loads((ROOT / "docs" / "IDENTIFICATION_BASELINE.json").read_text(encoding="utf-8"))
    assert base["unearned"] == 5 and base["total_rows"] == 12
    d = _verdict("B1238_seat_harvest_40a3_bronze_octic")
    assert [i["row"] for i in d["identifications"]] == ["I-12"]
    assert d["identifications"][0]["status"] == "EARNED"
    assert d["verdict"] == "PROVED" and d["creates_law"] is False
    assert (ARC / "FINDINGS.md").is_file() and (VER / "reproduce.sh").is_file()


# 5. bronze ----------------------------------------------------------------------------------------
def test_bronze_octic_is_the_committed_field():
    pari = _pari()
    assert pari(f"polisirreducible({OCTIC})") == 1 and pari(f"poldegree({OCTIC})") == 8
    assert pari(f"nfdisc({OCTIC})") == 391728981
    assert pari(f"polsturm({OCTIC})") == 0                                      # no real roots: signature (0,4)
    assert pari(f"polredabs({OCTIC})") == pari(OCTIC)
    out = (VER / "bronze_invariant_trace_field.txt").read_text(encoding="utf-8")
    assert "b++RRRLLL: invariant trace field degree 8" in out and OCTIC in out
    assert "routes agree (nfisisom): True" in out
    assert "b++RL: invariant trace field degree 2" in out and "b++RRLL: invariant trace field degree 2" in out
    # the field is not imaginary quadratic => bronze is NOT arithmetic; silver and golden are (E55 axis)
    assert "polredabs x^2 - x + 1" in out and "polredabs x^2 + 1" in out


# 5b. R40 (physics seat): among the metallic means, only golden's beta = x(1+sqrt x) is Pisot ------------
def test_pisot_quartics_golden_and_m5():
    s, x = sp.symbols("s x")
    def minpoly(m):
        xm = (m + sp.sqrt(m*m + 4))/2
        beta = xm*(1 + sp.sqrt(xm))
        P = sp.factor(sp.resultant(s**4 - m*s**2 - 1, x - s**2 - s**3, s))
        return next(f for f, _ in sp.factor_list(P)[1] if abs(sp.N(f.subs(x, beta), 60)) < 1e-40), beta
    F1, b1 = minpoly(1)
    assert sp.expand(F1 - (x**4 - 2*x**3 - 5*x**2 - 4*x - 1)) == 0
    others = [abs(r) for r in sp.Poly(F1, x).nroots(n=30) if abs(r - sp.N(b1, 30)) > 1e-10]
    assert len(others) == 3 and all(o < 1 for o in others)                     # golden: PISOT
    F5, b5 = minpoly(5)
    assert sp.expand(F5 - (x**4 - 10*x**3 - 117*x**2 - 44*x - 5)) == 0
    others = [abs(r) for r in sp.Poly(F5, x).nroots(n=30) if abs(r - sp.N(b5, 30)) > 1e-10]
    assert any(o > 1 for o in others)                                           # m = 5: not Pisot


# 6. R39 / Z1 ---------------------------------------------------------------------------------------
def test_z1_rerun_equals_main_and_nothing_was_lost():
    r = subprocess.run([sys.executable, str(VER / "z1_compare.py")], capture_output=True, text=True,
                       cwd=str(ROOT))
    assert r.returncode == 0, r.stdout + r.stderr
    assert "rerun == main banked at levels: 22 / 22  mismatches: []" in r.stdout
    assert "byte-identical): True" in r.stdout


# the slow lane: the whole cell ------------------------------------------------------------------------
@pytest.mark.skipif(not os.environ.get("OA_SLOW"), reason="OA_SLOW=1 re-runs reproduce.sh (bronze at 1000 bits)")
def test_reproduce_sh_reproduces():
    r = subprocess.run(["bash", str(VER / "reproduce.sh")], capture_output=True, text=True, cwd=str(ROOT))
    assert r.returncode == 0, r.stdout + r.stderr
    assert "REPRODUCES" in r.stdout and "DOES NOT" not in r.stdout


# --- E57: the lock-without-tool class, found at this cell's landing -------------------------------
def _gates_module():
    import importlib.util
    spec = importlib.util.spec_from_file_location("b1238_gates", ROOT / "scripts" / "gates" / "gates.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_e57_the_tool_b1237_forgot_is_tracked_and_its_selftest_passes():
    """B1237 pushed the lock; the tool it runs had never been `git add`ed. The fix is this commit."""
    r = subprocess.run(["git", "ls-files", "--error-unmatch", "scripts/checks/paper_ledger_counts.py"],
                       capture_output=True, text=True, cwd=str(ROOT))
    assert r.returncode == 0, "scripts/checks/paper_ledger_counts.py is not tracked (E57 regressed)"
    r2 = subprocess.run([sys.executable, str(ROOT / "scripts" / "checks" / "paper_ledger_counts.py"), "--selftest"],
                        capture_output=True, text=True, cwd=str(ROOT))
    assert r2.returncode == 0 and "CONTROLS PASS" in r2.stdout, r2.stdout + r2.stderr


def test_tracked_deps_gate_is_green_and_bites():
    """The gate is registered, green on the tree, and REDS when a tracked py file names an untracked
    on-disk path. The plant is a comment appended to a tracked file (restored in finally) plus an
    untracked file for it to point at -- the exact shape of the B1237 instance."""
    g = _gates_module()
    assert "tracked-deps" in g.GATES
    ok, detail = g.gate_tracked_deps()
    assert ok, detail
    host = ROOT / "scripts" / "checks" / "paper_ledger_counts.py"      # tracked (the instance's own tool)
    plant = ROOT / "scripts" / "checks" / "_e57_plant_untracked_tool.py"
    assert not plant.exists()
    orig = host.read_text(encoding="utf-8")
    try:
        plant.write_text("# E57 plant -- must never be tracked\n", encoding="utf-8")
        host.write_text(orig + "\n# plant: scripts/checks/_e57_plant_untracked_tool.py\n", encoding="utf-8")
        ok2, detail2 = g.gate_tracked_deps()
        assert not ok2, "the gate did NOT bite on an untracked-but-referenced path"
        assert "_e57_plant_untracked_tool.py" in str(detail2), detail2
    finally:
        host.write_text(orig, encoding="utf-8")
        if plant.exists():
            plant.unlink()
    ok3, detail3 = g.gate_tracked_deps()
    assert ok3, detail3
    assert host.read_text(encoding="utf-8") == orig
