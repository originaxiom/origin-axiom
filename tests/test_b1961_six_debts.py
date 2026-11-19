"""B1961 -- six verification debts recomputed on main: the fast scripts run live and equal their committed run files; the slow
ones (p156, p157) are read from their run files; every figure the page relies on is held here."""
import pathlib, subprocess, sys
V = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1961_six_verification_debts_recomputed_on_main" / "verification"
run = lambda n: (V / (n + "_run.txt")).read_text()


def test_fast_scripts_live():
    for n in ("w27", "w28", "w30", "w47", "p155"):
        out = subprocess.run([sys.executable, "-B", str(V / (n + ".py"))], capture_output=True, text=True, cwd=V).stdout + ""
        strip = lambda s: "\n".join(l for l in s.splitlines() if "0x" not in l)
        assert strip(out) == strip(run(n)), n


def test_the_figures():
    assert "three 27s: doublets 18 SU3^3 0 SU3^2Y 0 SU2^2Y 0 Y^3 0 grav 0" in run("w27")
    assert "dim{A in flavour algebra: A V ⊂ V}: V2 7 V4 7 (1 = scalars)" in run("w28")
    assert "|PSL(2,Z/4)| from L,R: 24" in run("w28") and "V2 char == tr g (spin 1/2) all 48: True" in run("w28")
    assert "order 72 mod scalars 24 commutant 2" in run("w30") and "order 648 mod scalars 216 commutant 1" in run("w30")
    assert "allowed j (Z-phase = j=0 phase): [0, 4, 8, 12, 16, 20] count 6" in run("w47") and "all exponents at allowed j odd multiples of 1/24: True" in run("w47")
    assert "4: np.float64(1.0)" in run("w47") and "20: np.float64(0.0)" in run("w47")
    assert "carry on some kernel 17 none 25" in run("p155") and "carry on EVERY kernel 12" in run("p155") and "carry on some not all (kernel-dependent): 5" in run("p155")
    assert "threads 42 carry on some reliable kernel 16" in run("p155")
    assert "order 192 commutant dim 1" in run("p156") and "(1, (6,), True, 1) 32" in run("p156")
    assert "TM2col" in run("p157") and "TM1col" in run("p157")
    f = (V.parent / "FINDINGS.md").read_text()
    assert "U(1) × U(2)" in f and "+1 at j = 4 only" in f and "32 of 64 sign choices" in f
