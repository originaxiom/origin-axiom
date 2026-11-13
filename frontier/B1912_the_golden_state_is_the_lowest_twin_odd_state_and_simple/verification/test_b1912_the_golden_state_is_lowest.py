"""B1912's lock. It runs the method at the points that decide (the golden state at both heights in its class and not in the
others; the positive control at 2 R0; a single-height false minimum that the second height removes), plants a wrong
character that must lose the golden state, and holds the page to the kept scans. It writes nothing."""
import sys, json, math, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import hejhal_level5 as H
R0 = math.pi / (2 * math.log((1 + math.sqrt(5)) / 2))
A = dict(M=40, Y=0.10, Q=72); B = dict(M=34, Y=0.12, Q=60)
PAGE = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")

def test_the_golden_state_is_an_eigenvalue_at_both_heights_in_its_class_only():
    assert H.least_singular(R0, parity="sin", eps=-1, **A)[0] < 1e-9 and H.least_singular(R0, parity="sin", eps=-1, **B)[0] < 1e-9
    for par, ep in (("sin", 1), ("cos", -1), ("cos", 1)):
        assert H.least_singular(R0, parity=par, eps=ep, **B)[0] > 1e-2

def test_it_is_simple():
    assert H.least_singular(R0, parity="sin", eps=-1, k=2, **A)[1] > 1e-3

def test_the_positive_control_in_a_mirror_even_class():
    from scipy.optimize import minimize_scalar
    r = minimize_scalar(lambda R: H.least_singular(R, parity="cos", eps=1, **A)[0], bracket=(2 * R0 - 0.003, 2 * R0, 2 * R0 + 0.003), tol=1e-12)
    assert abs(r.x - 2 * R0) < 1e-6 and r.fun < 1e-8 and H.least_singular(r.x, parity="cos", eps=1, **B)[0] < 1e-6

def test_a_single_height_false_minimum_is_removed_by_the_other():
    import numpy as np
    assert abs(H.KiR(2.558385, np.array([2 * np.pi * 0.12]))[0]) < 1e-6           # K_iR(2 pi Y) vanishes there: the cause
    assert H.least_singular(2.558385, parity="cos", eps=-1, **B)[0] < 1e-6 and H.least_singular(2.558385, parity="cos", eps=-1, **A)[0] > 1e-2

def test_plant_a_wrong_character_loses_the_golden_state():
    real = H.legendre5
    try:
        H.legendre5 = lambda d: 1
        assert H.least_singular(R0, parity="sin", eps=-1, **B)[0] > 1e-4
    finally:
        H.legendre5 = real

def test_the_page_is_the_kept_scans():
    s2 = json.loads((HERE / "scan2.json").read_text(encoding="utf-8"))
    main = {k: v for k, v in s2.items() if "R in [0.25, 3.40]" in k}
    assert [len(v) for v in main.values()] == [1, 0, 0, 0] and abs(main["sin, Fricke -1, R in [0.25, 3.40]"][0]["R"] - R0) < 1e-8
    ctl = {k: v for k, v in s2.items() if k.startswith("control")}
    assert sum(len(v) for v in ctl.values()) == 1 and len(ctl["control near 2 R0 = %.6f: cos, Fricke +1" % (2 * R0)]) == 1
    s3 = json.loads((HERE / "scan3.json").read_text(encoding="utf-8"))
    assert min(v["least of max over both heights"] for v in s3.values()) > 0.5
    assert "the only eigenvalue is R₀, in the golden state's own class, and it" in PAGE
