"""B1297 -- THE SPECTRAL-COVER INDEX: the pre-registration is sealed, every step reproduces by RUNNING in a scratch cwd,
and the banked numbers are pinned (16 + 45 sectors all zero, the period-2 symmetry = -1 on the torsion, the E6 block cycle in W(E6))."""
import hashlib, json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1297_the_spectral_cover_index"
VER = ARC / "verification"


def _run(script, cwd, *args):
    r = subprocess.run([sys.executable, str(VER / script)] + [str(a) for a in args], capture_output=True, text=True, cwd=str(cwd))
    assert r.returncode == 0, r.stdout[-2500:] + r.stderr[-2500:]
    return r.stdout


def test_the_pre_registration_is_sealed_and_the_seal_reproduces():
    seals = (ARC / "PREREG.sha256").read_text(encoding="utf-8")
    for name in ("PREREG.md", "PREREG_C4.md"):
        h = hashlib.sha256((ARC / name).read_bytes()).hexdigest()
        assert f"{h}  {name}" in seals, (name, h)
    p = (ARC / "PREREG.md").read_text(encoding="utf-8")
    assert "I(M;V) := n(V) − n(V*)" in p and "Domain D" in p and "PASS (the descent carries the bit)" in p and "FAIL (the fail theorem" in p


def test_controls_census_and_the_C3_table_reproduce_by_RUNNING(tmp_path):
    out = _run("step3_controls.py", tmp_path)
    assert out.rstrip().endswith("CONTROLS: PASS"), out[-800:]
    assert "H1(C) invariants (SNF): [4, 4, 0]" in out and "[m_C] = (0, 0, 1)  [l_C] = (0, 0, 0)" in out
    for k, h1 in zip(range(7), (1, 0, 1, 0, 1, 0, 1)):                       # B1256/B1267's untwisted table on m004
        assert f"  k={k}: a=({0 if k else 1},{h1}," in out, k
    out = _run("step4_census.py", tmp_path)                                   # the census BEFORE the table
    assert "count: 24 = 12 orientation-preserving + 12 reversing" in out
    assert "elements acting as -1 on the torsion: [('A', 'aaab', 1, 1)]" in out
    assert "characters with J forced to 0: 16  possibly nonzero: []" in out
    out = _run("step4b_period2_check.py", tmp_path)                           # the second, RS-free route
    assert "VERDICT (independent of Reidemeister-Schreier): period-2 acts as -1 on Tors H1(C), +1 on the free part: True" in out
    out = _run("step5_table.py", tmp_path)
    assert out.rstrip().endswith("TABLE: nonzero = 0"), out[-800:]
    t = json.loads((tmp_path / "table.json").read_text(encoding="utf-8"))
    assert len(t["table"]) == 16 and t["nonzero"] == 0 and t["lift_independent"] is True
    assert all(r["a"] == [0, 1, 1] and r["t"] == [1, 2, 1] and r["r1"] == 1 and r["r1s"] == 1 and r["ids"] and r["float_ok"] for r in t["table"])
    assert "lift +B: set of (a, t, r1, I, ids) = [((0, 0, 0), (0, 0, 0), 0, 0, True)]" in out       # odd k: t0 = 0


def test_the_E6_block_cycle_is_a_Weyl_element_and_the_code_is_not_vacuous(tmp_path):
    out = _run("step6_e6_blocks.py", tmp_path)
    assert out.rstrip().endswith("E6 BLOCKS: PASS") and "number of roots: 72" in out and "det: 3" in out
    assert "sigma in W(E6): True  reduced word length (as product of simple reflections): 6  word: [1, 5, 3, 2, 4, 5]" in out
    assert "sigma on blocks: B1->B2 True  B2->B3 True  B3->B1 True" in out
    out = _run("step7_nonvacuity_random.py", tmp_path)
    assert "31 random trials: I != 0 in 26; at least one 3-manifold identity violated in 26" in out


def test_galois_the_4fold_cover_and_the_alexander_module_reproduce_by_RUNNING(tmp_path):
    _run("step3_controls.py", tmp_path)
    out = _run("step9_galois.py", tmp_path)
    assert "V^tau == Sym^2 rho (x) chi^-1 entrywise for all 16 chi: True" in out
    assert "H1(C_4) invariants: [3, 15, 0]" in out and "order-3 characters of H1(C_4): 8; trivial on the cusp: 8" in out
    out = _run("step10_c4.py", tmp_path)
    assert "isometries of C4 realised: 32 word pairs, 32 distinct actions on H1(C4)" in out
    assert "order  3:  8 characters, forced J = 0 by the signed symmetry group:  8, free: []" in out
    assert "NONZERO INDICES among the 45 sectors: 0   ;  order-3 (Galois-unprotected) sectors nonzero: 0" in out
    assert "all identities hold: True  exact == numeric on order-3: True" in out
    out = _run("step11_alexander_module.py", tmp_path)
    assert "=> P acts on H1(X~) = Z[t^+-] e_a / (Delta) as multiplication by -1" in out
    assert "n=3: |Tors H1(C_n)| = |Res(Delta, (t^n-1)/(t-1))| = 16" in out and "n=4: |Tors H1(C_n)| = |Res(Delta, (t^n-1)/(t-1))| = 45" in out


def test_the_live_scan_finds_no_nonzero_index_on_a_capped_census_slice(tmp_path):
    out = _run("step8_live_manifold_scan.py", tmp_path, 8)
    assert "NONZERO INDICES: 0" in out and "scanned 8 one-cusped census manifolds" in out
