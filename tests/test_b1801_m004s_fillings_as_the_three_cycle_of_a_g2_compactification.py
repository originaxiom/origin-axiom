"""B1801 -- m004's fillings as the 3-cycle of a G2 compactification.  The committed run: the Fox-calculus Alexander polynomial
of the figure-eight; |Delta(omega)| = 4; the order-3 torsion 4/3 and L(Q) = 3|H1|/4 on every listed filling; the Wilson line's
holonomy table (leptons and the Higgs doublet untwisted, quarks, the colour triplet and the X,Y bosons twisted)."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1801_m004s_fillings_as_the_three_cycle_of_a_g2_compactification" / "verification"


def test_the_torsion():
    run = (V / "torsion_run.txt").read_text(encoding="utf-8")
    assert "(t**2 - 3*t + 1)/t" in run and "Fox value |d r/d b (omega)| = 4.0" in run
    rows = re.findall(r"H1 Z/(\d+)\s+vol [0-9.]+ \| \|tau\(Q, order-3 char\)\| = ([0-9.]+) \| L\(Q\) = \|H1\|/\|tau\| = ([0-9.]+)", run)
    assert len(rows) >= 10
    for h, tau, L in rows:
        assert abs(float(tau) - 4 / 3) < 1e-6 and abs(float(L) - 3 * int(h) / 4) < 1e-6


def test_the_wilson_line():
    run = (V / "torsion_run.txt").read_text(encoding="utf-8")
    for f in ("L ", "e^c", "H doublet"):
        assert re.search(re.escape(f) + r"\s+6Y = [+-]\d+: holonomy trivial", run)
    for f in ("Q ", "T triplet", "X,Y bosons"):
        assert re.search(re.escape(f) + r"\s+6Y = [+-]\d+: holonomy omega", run)
    assert "torsion exit 0" in run


def test_the_bench_checks():
    run = (V / "bench_checks_run.txt").read_text(encoding="utf-8")
    assert "(3.21) identity holds: True" in run and "det[16pi^2/g_a^2, k_a, b_a] = 0" in run
    assert "|tau|^2 = |H1(Qt)| / (3p) = 16/9 on every row: True" in run
    assert run.count("(H^1 = 0)") == 3 and "bench_checks exit 0" in run


def test_delta_at_omega_recomputed():
    import cmath, math
    w = cmath.exp(2j * math.pi / 3)
    assert abs(abs(w - 3 + 1 / w) - 4) < 1e-12 and abs(abs(w - 1) - math.sqrt(3)) < 1e-12
