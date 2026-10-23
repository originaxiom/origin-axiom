"""B1737 -- the slope is a zeta value (P-311), PROVED.  Live: on +LR level 2, +LLR level 3 and -LLRLR level 1 every
character's exact slope equals the twisted Shintani value at s = 0 less (1/2)#(-I), and the trivial character's zeta(0)
is -Psi/12.  Stored: the full 601 characters at 16 levels."""
import importlib.util, json, pathlib, math, cmath
V = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1737_the_slope_is_a_zeta_value" / "verification"


def _m():
    spec = importlib.util.spec_from_file_location("b1737", V / "the_slope_is_a_zeta_value.py"); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_the_identity_live():
    m = _m(); SL = m._sl()
    for st, k in (("+LR", 2), ("+LLR", 3), ("-LLRLR", 1)):
        eps = 1 if st[0] == "+" else -1; N, F, S = SL.exact_slopes(eps, st[1:], k); M = m.abel_M(SL, eps, st[1:], k)
        zz = cmath.exp(2j * math.pi / N); nI = k if eps < 0 else 0
        for (i, j, _), s in S.items():
            if (i, j) == (0, 0): continue
            sv = sum(float(c) * zz ** e for e, c in enumerate(s.c))
            assert abs(sv - (m.Z0(M, i, j, N) - nI / 2)) < 1e-10
        assert abs(m.zeta0_trivial(M) - float(-m.rademacher_Psi([[int(x) for x in r] for r in M]) / 12)) < 1e-9


def test_the_stored_census():
    d = json.loads((V / "the_slope_is_a_zeta_value.json").read_text(encoding="utf-8"))
    assert d["characters"] == 601 and d["max |s - (Z - #(-I)/2)|"] < 1e-12 and d["max |Z(w) - Z(w')|"] < 1e-12
    assert d["max |zeta0 + Psi/12| (trivial)"] < 1e-9 and len(d["levels"]) == 16
