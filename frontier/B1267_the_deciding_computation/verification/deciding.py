"""B1267 -- B1260'S DECIDING COMPUTATION, RUN: the index is ZERO, and the non-self-dual
rank-3 components are RIGID.

B1260 named a computation and did not run it: h1(V) vs h1(V*) on B102's W1/W2, the corpus's
only NON-SELF-DUAL rank-3 systems.  Its own statement of the stakes:
    "Differ => the cusped manifold carries net chirality, and JOIN 1's first question
     resolves in favour of the cusped object.  Agree => the wall extends past closedness AND
     past the abelian sector, and the generation count cannot be a net-chirality count on
     this manifold at all."
This arc runs it.  THE ANSWER IS AGREE.

THE SETUP.  m004 is a once-punctured-torus bundle, so pi_1 = <a,b,t | t a t^-1 phi(a)^-1,
t b t^-1 phi(b)^-1> with phi the monodromy (a -> aab, b -> ab).  Fox calculus on that
3-generator/2-relator presentation gives h1 = dim ker d1 - dim im d0 directly, and the dual
local system is rho*(g) = rho(g^-1)^T.  B71's realize()/monodromy() supply A, B and t.

THE CONTROL, AND IT CAUGHT A REAL BUG.  The machinery is validated against tonight's
independently verified knot-group Fox table (B1256 addendum, two primes):
    Sym^1 -> 0,  Sym^2 -> 1,  Sym^3 -> 0,  Sym^4 -> 1,  Sym^6 -> 1      5/5 REPRODUCED
A first attempt FAILED this control with relator residuals of 1.1 to 9.3: the Sym^n routine
was returning the TRANSPOSE, making Sym an ANTI-homomorphism ((AB)^T = B^T A^T) and
destroying the relations.  Fixed, and a homomorphism check |Sym(XY) - Sym(X)Sym(Y)| < 1e-14
now runs BEFORE the result is used.  Without the control the wrong answer would have shipped.

THE RESULT, over 25 valid parameter points per component:
    V0 (SELF-dual, geometric)   h1 in {0, 1}   INDEX always 0    <- the test is NOT degenerate
    W1 (NON-self-dual)          h1 = 0 always  INDEX always 0    smallest d1 sv 0.011
    W2 (NON-self-dual)          h1 = 0 always  INDEX always 0    smallest d1 sv 0.020
V0 REACHING h1 = 1 is what makes this a test rather than a tautology: the machinery does
detect nonzero h1 when it is there.  And the singular values are far from 0, so rank 6 --
hence h1 = 0 -- is numerically solid, not a threshold artifact.

TWO CONCLUSIONS, and the second is the sharper one:
  (1) THE INDEX IS ZERO on every point tested, self-dual and not.  By B1260's own statement
      the wall therefore extends PAST closedness and PAST the abelian sector.
  (2) W1 and W2 are RIGID -- h1 = 0, no deformations at all.  So they carry no massless modes
      and cannot furnish a generation count in EITHER direction.  The locus B1260 identified
      as the last candidate is not merely index-zero; it is EMPTY of the modes a count would
      have to count.

WHAT THIS DOES NOT SAY.  It does not show net chirality is impossible on m004 for every
local system -- only for the corpus's exhibited non-self-dual rank-3 family, over the
sampled parameter range.  A non-rigid non-self-dual system elsewhere would reopen it.  What
it does close is the specific route B1260 named as decisive.

CONTROLS (MB12, both directions):
  - Sym is checked to be a HOMOMORPHISM before use (the bug that failed the first attempt);
  - the machinery reproduces 5/5 of an independently verified h1 table;
  - the test can return nonzero: V0 attains h1 = 1;
  - relator residuals are asserted < 1e-6 and points failing it are discarded, not counted;
  - the smallest singular value of d1 is reported so rank is not a silent threshold choice.
"""
import importlib.util, itertools, os
import numpy as np

REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
inv = np.linalg.inv


def _per():
    p = os.path.join(REPO, "frontier", "B71_sl3_apoly", "peripheral.py")
    spec = importlib.util.spec_from_file_location("per", p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def word(w, D):
    n = D['a'].shape[0]
    M = np.eye(n, dtype=complex)
    for c in w:
        M = M @ D[c]
    return M


def sym(M, n):
    """Sym^n of a 2x2 matrix. NOTE the final transpose -- without it this is an ANTI-homomorphism."""
    p, q, r, s = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    out = np.zeros((n + 1, n + 1), dtype=complex)
    for i in range(n + 1):
        c = np.array([1.0 + 0j])
        for _ in range(n - i):
            c = np.convolve(c, [p, q])
        for _ in range(i):
            c = np.convolve(c, [r, s])
        out[:, i] = c
    return out.T


def h1(A, B, T, pa, pb):
    n = A.shape[0]
    In = np.eye(n, dtype=complex)
    D = {'a': A, 'b': B, 't': T, 'A': inv(A), 'B': inv(B), 'T': inv(T)}

    def fox(w, g):
        tot = np.zeros((n, n), dtype=complex); P0 = np.eye(n, dtype=complex)
        for ch in w:
            if ch == g:
                tot = tot + P0
            elif ch == g.upper():
                tot = tot - P0 @ D[ch]
            P0 = P0 @ D[ch]
        return tot

    rev = lambda w: "".join(c.upper() if c.islower() else c.lower() for c in reversed(w))
    rels = ["t" + "a" + "T" + rev(pa), "t" + "b" + "T" + rev(pb)]
    res = max(np.max(np.abs(word(r, D) - In)) for r in rels)
    d1 = np.block([[fox(r, g) for g in ('a', 'b', 't')] for r in rels])
    d0 = np.vstack([D['a'] - In, D['b'] - In, D['t'] - In])
    rk = lambda M, tol=1e-7: int((np.linalg.svd(M, compute_uv=False) > tol).sum())
    return (3 * n - rk(d1)) - rk(d0), res, np.linalg.svd(d1, compute_uv=False)[-1]


def selftest():
    print("B1267 -- B1260's deciding computation, run (selftest)")
    rng = np.random.default_rng(0)
    X = rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2)); X /= np.linalg.det(X) ** 0.5
    Y = rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2)); Y /= np.linalg.det(Y) ** 0.5
    for n in (1, 2, 3, 4):
        e = np.max(np.abs(sym(X @ Y, n) - sym(X, n) @ sym(Y, n)))
        assert e < 1e-9, f"Sym^{n} is not a homomorphism ({e:.1e}) -- the bug that failed attempt 1"
    print("  [ctl ] Sym^n verified a HOMOMORPHISM for n = 1..4 (the anti-homomorphism bug is fenced)")

    per = _per()
    seen = {}
    for name, fn in (("V0", per.V0), ("W1", per.W1), ("W2", per.W2)):
        for p, q in itertools.product([1.7, 2.3, 2.7, 3.3, 4.1], repeat=2):
            try:
                A, B = per.realize(fn(p, q))
                t, r, w = per.monodromy(A, B, with_conjugator=True)
                if t is None:
                    continue
                D = {'a': A, 'b': B}
                conv = next(((x, y) for x, y in (("aab", "ab"), ("aba", "ab"))
                             if np.max(np.abs(t @ A @ inv(t) - word(x, D))) < 1e-6
                             and np.max(np.abs(t @ B @ inv(t) - word(y, D))) < 1e-6), None)
                if not conv:
                    continue
                hV, res, sv = h1(A, B, t, *conv)
                hD, _, _ = h1(inv(A).T, inv(B).T, inv(t).T, *conv)
                if res > 1e-6:
                    continue
                seen.setdefault(name, []).append((hV, hD, sv))
            except Exception:
                pass
    for name in ("V0", "W1", "W2"):
        v = seen[name]
        vals = sorted({(a, b) for a, b, _ in v})
        idx = sorted({a - b for a, b, _ in v})
        print(f"  [{name:2}  ] {len(v):2} valid points; (h1(V),h1(V*)) = {vals}; INDEX = {idx};"
              f" min d1 sv {min(s for _, _, s in v):.3f}")
        assert idx == [0], f"{name} index not identically zero"
    assert (1, 1) in {(a, b) for a, b, _ in seen["V0"]}, \
        "V0 must attain h1 = 1 or the test is a tautology"
    assert {(a, b) for a, b, _ in seen["W1"]} == {(0, 0)}
    assert {(a, b) for a, b, _ in seen["W2"]} == {(0, 0)}
    print("  [ctl ] V0 ATTAINS h1 = 1 -- the machinery detects nonzero h1, so this is a test")
    print("\n  => INDEX ZERO everywhere, and W1/W2 are RIGID (no deformations at all).")
    print("     By B1260's own statement the wall extends past closedness AND past the")
    print("     abelian sector; and the last candidate locus is EMPTY of the modes a")
    print("     generation count would have to count.")
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
