#!/usr/bin/env python3
"""W133, POST HOC, third pass: the number of distinct solutions, exactly. Nothing here was in the rule.

  E1  for each space, the multiplication matrix of a linear form on the quotient ring of W133's Groebner basis, over
      Q (python-flint); its characteristic polynomial (degree = solutions with multiplicity) and the degree of its
      squarefree part (the number of distinct values of the form on the solutions); two forms, so that a form that
      fails to separate points shows as a smaller count; the multiplicity structure from the squarefree
      factorisation, and which multiplicity each theta-power line carries (both added after this pass's first
      run, which gave the same counts)

    python3 -B the_zero_free_higgs_posthoc3.py      # writes the_zero_free_higgs_posthoc3.json beside itself
"""
import contextlib
import io
import json
import sys
from pathlib import Path

import flint
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_zero_free_higgs_posthoc as PH  # noqa: E402  (the first pass: standard monomials; W133's system)

W133 = PH.W133
OUT = HERE / "the_zero_free_higgs_posthoc3.json"
CASES = ((4, 0), (4, 1), (12, 1), (20, 1))
FORMS = ((3, -2, 5, 7), (11, 4, -9, 2))
THETA_POWERS = {(4, 0): (2,), (4, 1): (2, 26), (12, 1): (-6, 18), (20, 1): (10,)}      # found in the first pass


def mult_matrix(G, gens, form):
    B = PH.standard_monomials(G, gens)
    idx = {b: k for k, b in enumerate(B)}
    mono = lambda b: sp.prod([g ** e for g, e in zip(gens, b)])
    ell = sum(c * g for c, g in zip(form, gens))
    M = flint.fmpq_mat(len(B), len(B))
    for k, b in enumerate(B):
        _, rem = G.reduce(sp.expand(ell * mono(b)))
        for (cmon, cf) in sp.Poly(rem, *gens).terms():
            cf = sp.Rational(cf)
            M[idx[cmon], k] = flint.fmpq(int(cf.p), int(cf.q))
    return M


def main():
    out = {}
    for (r, n) in CASES:
        forms, a, eqs, _, _ = W133.cubic_system(r, n)
        G = sp.groebner(eqs, *a, order="grevlex", domain=sp.QQ)
        row = {}
        for form in FORMS:
            p = mult_matrix(G, a, form[:len(a)]).charpoly()
            g = p.gcd(p.derivative())
            _, facs = p.factor_squarefree()
            mult = {}
            for f, k in facs:
                mult[str(k)] = mult.get(str(k), 0) + f.degree()
            row[str(form[:len(a)])] = {"degree": p.degree(), "distinct values": p.degree() - g.degree(),
                                       "distinct values by multiplicity": mult}
        row["lines through the origin (distinct values / 3)"] = (p.degree() - g.degree()) // 3
        form = FORMS[0][:len(a)]
        p = mult_matrix(G, a, form).charpoly()
        _, facs = p.factor_squarefree()
        where = {}
        for aa in THETA_POWERS[(r, n)]:
            c = PH.coords(forms, PH.theta_power_lines(aa, r))
            lv = sum(sp.Rational(k) * x for k, x in zip(form, c))         # the form at the section, before scaling
            v = lv ** 3 / sp.Integer(2) ** (aa + 2)                        # its cube at the solutions t F_a
            cubic = flint.fmpq_poly([flint.fmpq(-int(v.p), int(v.q)), 0, 0, 1])
            where[str(aa)] = [k for f, k in facs if f.gcd(cubic).degree() == 3]
        row["the multiplicity of each theta-power line"] = where
        out[f"r={r} n={n}"] = row
    OUT.write_text(json.dumps({"arc": "W133", "status": "POST HOC, third pass", **out}, indent=1) + "\n",
                   encoding="utf-8")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
