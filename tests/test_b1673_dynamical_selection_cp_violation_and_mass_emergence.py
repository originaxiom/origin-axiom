"""B1673 -- the dynamical-selection claims of 19 October, verified (NEGATIVE). Live: the received rotation and conjugation
of the 9-torsion points are wrong on the points as the received arc builds them (the coordinate error), and on the true
points the ground orbit is fixed by no reflection and closed under all six (nothing is broken); the torus-determinant
extremum at omega and the saddle at i. Stored: the averaged J set by the input matrix, the 12 disjoint from W59's lines,
the Selberg spectra near 1/2. The bite: the received reading's CP-even count is 4, the true one 0."""
import cmath, json, pathlib
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1673_dynamical_selection_cp_violation_and_mass_emergence"
OM = complex(-0.5, 3 ** 0.5 / 2)
UNITS = [cmath.exp(1j * cmath.pi * k / 3) for k in range(6)]


def pt(a, b): return (a * OM - b) / 9                                   # the received arc's points (its line 101)


def in_lattice(z):
    n = z.imag / OM.imag; m = z.real - n * OM.real
    return abs(n - round(n)) < 1e-9 and abs(m - round(m)) < 1e-9


def received_mul(x, y):                                                 # the received rotation, verbatim in substance
    a, b = x; c, d = y; return ((a * c - b * d) % 9, (a * d + b * c - b * d) % 9)


def received_conj(x):
    a, b = x; return ((a - b) % 9, (-b) % 9)


def ground():
    d = json.load(open(A / "verification" / "as_received" / "verify_dynamical_selection_cp_hierarchy.json"))
    return [tuple(p) for p in d["Theorem_2"]["ground_state_points"]]


def test_the_coordinate_error_and_the_true_cp_count():
    pts = [(a, b) for a in range(9) for b in range(9) if (a % 3 or b % 3)]
    assert sum(not in_lattice(OM * pt(a, b) - pt(*received_mul((0, 1), (a, b)))) for a, b in pts) == 72
    assert sum(not in_lattice(pt(a, b).conjugate() - pt(*received_conj((a, b)))) for a, b in pts) == 72
    g = ground(); assert len(g) == 12
    received_even = sum(any(received_mul(u, received_conj(p)) == p for u in [(1, 0), (0, 1), (8, 8), (8, 0), (0, 8), (1, 1)]) for p in g)
    true_even = sum(any(in_lattice(u * pt(*p).conjugate() - pt(*p)) for u in UNITS) for p in g)
    assert (received_even, true_even) == (4, 0)                          # the bite: 8:4 was the error, the truth is 12:0
    zs = [pt(*p) for p in g]
    assert all(any(in_lattice(u * z.conjugate() - w) for w in zs) for z in zs for u in UNITS)   # reflection-closed


def test_the_torus_determinant_extremum():
    def V(t):
        q = cmath.exp(2j * cmath.pi * t); eta = cmath.exp(2j * cmath.pi * t / 24) * np.prod([1 - q ** n for n in range(1, 200)])
        return -np.log(t.imag * abs(eta) ** 4)
    assert abs(V(OM) - 1.0335192760) < 1e-9 and abs(V(1j) - V(OM) - 0.0211690050) < 1e-9


def test_stored_negatives():
    mc = A / "verification" / "main_check"
    yuk = (mc / "yuk_run.txt").read_text(); sel = (mc / "sel_run.txt").read_text(); v = (mc / "v_run.txt").read_text()
    assert "S_arc(complex) GS-avg J= -0.0367" in yuk and "S real GS-avg J= 0.0325" in yuk
    assert "W59 18 in GS: []" in v and "min over ALL 80 incl 3-torsion -0.5493" in v
    assert "s=1.925 up 0.565 0.474" in sel
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "NEGATIVE"
