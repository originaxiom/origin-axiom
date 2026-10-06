#!/usr/bin/env python3
"""B1483, POST-SEAL (written after the sealed cells returned; labelled so; it changes no sealed result).
Why exactly two of the 34 amphichiral - word states have real end curves (R2's exceptions, the golden and silver words).

LEMMA.  On a - state the mirror is rhombic at the cusp with fixed class L and every spin structure has sigma(L) = -1; the
two classes of spin structures are the two characters sigma_+, sigma_- of the cusp lattice Lambda (mod 2) that are -1 on
L, and the mirror exchanges them.  So the end data (E, sigma_+) and (E, sigma_-), E = C / Lambda, are complex conjugate.
They are ISOMORPHIC iff Lambda has an automorphism of order > 2, i.e. iff E is the hexagonal curve (j = 0) or the square
one (j = 1728).   Proof: an isomorphism is a rotation u of Lambda carrying sigma_+ to sigma_-; +-1 act trivially on
Hom(Lambda, Z/2), so u has order 3, 4 or 6.  Conversely the rotation of order 3 of the hexagonal lattice permutes the
three non-zero characters cyclically, and on the square lattice Z[i], whose rhombic mirror fixes the class of 1 + i,
multiplication by i exchanges the two characters that are -1 on 1 + i.

CHECK (this script): j of the cusp lattice on the 68 amphichiral word states, from the shapes stored in end_curve.json;
the states with j = 0 or 1728; the - states whose end curves have real j.  The lemma predicts the first set, restricted to
the - states, equals the second if no further coincidence occurs; the census says it does."""
import json, pathlib
import mpmath as mp
mp.mp.dps = 30
HERE = pathlib.Path(__file__).resolve().parent


def reduce(t):
    t = mp.mpc(t)
    for _ in range(5000):
        t = t - mp.nint(t.real)
        if abs(t) < 1 - mp.mpf(10) ** -25: t = -1 / t
        else: break
    return t


def j(t):
    t = reduce(t); q = mp.e ** (2j * mp.pi * t)
    E4 = 1 + 240 * mp.nsum(lambda n: n ** 3 * q ** n / (1 - q ** n), [1, mp.inf])
    E6 = 1 - 504 * mp.nsum(lambda n: n ** 5 * q ** n / (1 - q ** n), [1, mp.inf])
    return 1728 * E4 ** 3 / (E4 ** 3 - E6 ** 2)


if __name__ == "__main__":
    assert abs(j(1j) - 1728) < 1e-15 and abs(j(mp.e ** (2j * mp.pi / 3))) < 1e-10 and abs(j(mp.sqrt(3) * 1j) - 54000) < 1e-10   # controls
    st = json.load(open(HERE / "end_curve.json"))["states"]; rows = {}
    for k, v in st.items():
        jE = j(mp.mpc(v["shape"][0], abs(v["shape"][1]))); sign = "-" if k.startswith("b+-") else "+"
        special = "hexagonal" if abs(jE) < 1e-6 else ("square" if abs(jE - 1728) < 1e-6 else None)
        rows[k] = dict(sign=sign, j_cusp=[float(jE.real), float(jE.imag)], cusp_real=bool(abs(jE.imag) < 1e-9 * max(1, abs(jE))),
                       lattice=special, end_curves_real=all(r["j_real"] for r in v["rows"]))
    minus = {k: r for k, r in rows.items() if r["sign"] == "-"}; plus = {k: r for k, r in rows.items() if r["sign"] == "+"}
    summary = dict(states=len(rows), minus=len(minus), plus=len(plus),
                   cusp_lattice_hexagonal_or_square={k: r["lattice"] for k, r in rows.items() if r["lattice"]},
                   minus_states_with_real_end_curves=sorted(k for k, r in minus.items() if r["end_curves_real"]),
                   plus_states_with_real_end_curves=sum(r["end_curves_real"] for r in plus.values()),
                   every_cusp_modulus_real=all(r["cusp_real"] for r in rows.values()))
    summary["the_two_sets_agree"] = sorted(k for k, r in minus.items() if r["lattice"]) == summary["minus_states_with_real_end_curves"]
    json.dump(dict(summary=summary, rows=rows), open(HERE / "exceptions_explained.json", "w"), indent=1)
    print(json.dumps(summary, indent=1))
