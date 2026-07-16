"""B645 locks — the unit cross-ratio law and the 13-dial (exact)."""
import os
import re

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
B637 = os.path.join(HERE, "..", "frontier", "B637_corrected_cell3")
r = sp.sqrt(-3)
VAL = re.compile(r"Y\[\((\d), (\d), (\d)\)\] = (.+)$")


def _parse_val(s):
    s = s.strip()
    if s == "0":
        return sp.Integer(0)
    m = re.match(r"\((-?\d+(?:/\d+)?)\+(-?\d+(?:/\d+)?)r\)", s)
    return sp.Rational(m.group(1)) + sp.Rational(m.group(2)) * r


def _tables():
    T = {}
    for path, headers in (
        (os.path.join(B637, "stage3_output.txt"),
         [("phi(a)=a:", "Dphi_a"), ("phi(a)=A:", "Dphi_Ainv"),
          ("phi(a)=b:", "Dphi_b"), ("phi(a)=B:", "Dphi_Binv"),
          ("unbent weld table", "weld_none")]),
        (os.path.join(B637, "part2b_stage2_fixed_output.txt"),
         [("D_bent(M; m=1):", "bent_m1"), ("D_bent(M; m=5):", "bent_m5"),
          ("D_bent(M; m=7):", "bent_m7"),
          ("D_bent(M; m=11):", "bent_m11")]),
    ):
        cur = None
        for ln in open(path).read().splitlines():
            for h, name in headers:
                if h in ln:
                    cur = name
                    T[cur] = {}
            m = VAL.search(ln)
            if m and cur is not None:
                T[cur][(int(m.group(1)), int(m.group(2)),
                        int(m.group(3)))] = _parse_val(m.group(4))
    return T


def test_core_law_all_nine():
    T = _tables()
    assert len(T) == 9
    z6 = (1 + r) / 2
    for k, tab in T.items():
        assert sp.simplify(tab[(0, 2, 3)] - 24 * z6 * tab[(1, 2, 3)]) == 0


def test_unit_cross_ratio_on_silent_six():
    T = _tables()
    silent = [k for k, tab in T.items() if tab[(0, 2, 4)] == 0]
    assert sorted(silent) == ["Dphi_Binv", "Dphi_b", "bent_m11",
                              "bent_m5", "bent_m7", "weld_none"]
    for k in silent:
        tab = T[k]
        cr = sp.simplify((tab[(0, 2, 3)] * tab[(1, 3, 4)])
                         / (tab[(0, 3, 4)] * tab[(1, 2, 3)]))
        assert cr == 1, (k, cr)


def test_thirteen_dial_on_lit_three():
    T = _tables()
    lit = [k for k, tab in T.items() if tab[(0, 2, 4)] != 0]
    assert sorted(lit) == ["Dphi_Ainv", "Dphi_a", "bent_m1"]
    for k in lit:
        tab = T[k]
        for num_slots, den_slots in (
            (((0, 2, 3), (1, 2, 4)), ((0, 2, 4), (1, 2, 3))),
            (((0, 2, 3), (1, 3, 4)), ((0, 3, 4), (1, 2, 3))),
        ):
            val = sp.simplify(
                tab[num_slots[0]] * tab[num_slots[1]]
                / (tab[den_slots[0]] * tab[den_slots[1]]))
            dev = sp.expand(sp.radsimp(val - 1))
            a, b = dev.as_real_imag()
            b = sp.simplify(b / sp.sqrt(3))
            assert dev != 0, (k, "deviation vanishes — not lit?")
            for comp in (a, b):
                if comp != 0:
                    num, den = sp.fraction(sp.Rational(comp))
                    assert num % 13 == 0, (k, comp)
                    assert den % 13 != 0, (k, comp)
