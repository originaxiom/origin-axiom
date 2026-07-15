"""B423 -- GATE B: the E6 adjoint Reidemeister torsion of the figure-eight.

CORRECTED 2026-07-15 (the 07-11 audit, item 5.2): the original producer's
product ran over k = 0..2m INCLUDING k = m, whose factor is 1 - phi^0 = 0,
so it returned zero identically while the committed artifact held nonzero
values (produced by an earlier version with a different schema). THE
DEFINITION, now stated: the REDUCED (adjusted) determinant with the
invariant eigenline omitted --

    tau_m := det'(I - Sym^{2m}(A)) = prod_{k != m} (1 - phi^{4(m-k)}),

the standard torsion convention when the twisted complex has the
one-dimensional invariant line (Sym^{2m} of the monodromy A = [[2,1],[1,1]]
has eigenvalues phi^{4(m-k)}, k = 0..2m; k = m is the eigenvalue 1). The
silver control uses the same reduced product with delta = 1 + sqrt(2)
(identified against the committed control value, exact match).
Regenerating with this definition REPRODUCES the committed artifact
exactly. The schema is versioned; the artifact is written next to the
script.
"""
import json
import os

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
phi = (1 + sp.sqrt(5)) / 2
delta = 1 + sp.sqrt(2)                  # the silver control
EXPS = [1, 4, 5, 7, 8, 11]              # E6 exponents


def tau_m(m, lam=phi):
    """the reduced determinant: the k = m (eigenvalue-1) factor omitted."""
    p = sp.Integer(1)
    for k in range(0, 2 * m + 1):
        if k == m:
            continue
        p *= (1 - lam ** (4 * (m - k)))
    return sp.expand(sp.simplify(p))


def prime_content(x):
    x = sp.Rational(sp.nsimplify(x))
    prs = set()
    for n in (abs(int(x.p)), int(x.q)):
        for pr in sp.factorint(n):
            prs.add(int(pr))
    return sorted(prs)


def compute():
    taus = {m: tau_m(m) for m in EXPS}
    tauE6 = sp.simplify(sp.prod([taus[m] for m in EXPS]))
    pc = prime_content(tauE6)
    ctrl = sp.simplify(sp.prod([tau_m(m, delta) for m in EXPS]))
    return dict(schema_version=2,
                taus={str(m): str(taus[m]) for m in EXPS},
                tauE6=str(tauE6),
                prime_content=pc,
                golden_only=bool(set(pc) <= {2, 5}),
                control_tauE6=str(ctrl),
                control_primes=prime_content(ctrl))


if __name__ == "__main__":
    res = compute()
    for m in EXPS:
        print(f"tau_{m} = {res['taus'][str(m)]}")
    print("tau_E6 =", res["tauE6"])
    print("prime content:", res["prime_content"],
          " golden_only:", res["golden_only"])
    out = os.path.join(HERE, "gateB.json")
    json.dump(res, open(out, "w"), indent=1)
    print("DONE ->", out)
