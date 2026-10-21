"""P-226 (exploratory, audit): the tricritical Ising model M(5,4) (c = 7/10) against Ising x Fibonacci: Verlinde fusion
from the minimal-model S-matrix, compared with the product of the two fusion rings under every bijection of labels."""
import itertools, numpy as np
p, q = 5, 4                                     # M(p, q), c = 1 - 6 (p - q)^2 / (p q) = 7/10
kac = [(r, s) for r in range(1, q) for s in range(1, p) if (r, s) <= (q - r, p - s)]
h = {(r, s): ((p * r - q * s) ** 2 - (p - q) ** 2) / (4 * p * q) for r, s in kac}
def S(a, b):
    (r, s), (rr, ss) = a, b
    return 2 * np.sqrt(2 / (p * q)) * (-1) ** (1 + s * rr + r * ss) * np.sin(np.pi * p * r * rr / q) * np.sin(np.pi * q * s * ss / p)
n = len(kac); Sm = np.array([[S(a, b) for b in kac] for a in kac])
assert np.allclose(Sm @ Sm.T, np.eye(n), atol=1e-12)
N = np.rint(np.einsum("ax,bx,cx,x->abc", Sm, Sm, Sm, 1 / Sm[0])).astype(int)   # Verlinde (S real symmetric, c-bar = c)
assert np.allclose(np.einsum("ax,bx,cx,x->abc", Sm, Sm, Sm, 1 / Sm[0]), N, atol=1e-9)
# Ising: 1, s, e (s s = 1 + e, s e = s, e e = 1); Fibonacci: 1, t (t t = 1 + t)
I = np.zeros((3, 3, 3), int)
for a in range(3): I[0, a, a] = I[a, 0, a] = 1
I[1, 1, 0] = I[1, 1, 2] = 1; I[1, 2, 1] = I[2, 1, 1] = 1; I[2, 2, 0] = 1
F = np.zeros((2, 2, 2), int); F[0, 0, 0] = F[0, 1, 1] = F[1, 0, 1] = F[1, 1, 0] = F[1, 1, 1] = 1
P = np.einsum("abc,xyz->axbycz", I, F).reshape(6, 6, 6)
match = [perm for perm in itertools.permutations(range(6)) if perm[0] == 0 and
         np.array_equal(N, P[np.ix_(perm, perm, perm)])]
print("TCI primaries (r,s): h =", {k: round(v, 4) for k, v in h.items()})
print("fusion ring of M(5,4) equals Ising x Fibonacci:", bool(match), "| bijections:", len(match))
if match:
    lab = [(i, f) for i in ("1", "s", "e") for f in ("1", "t")]
    for k, j in zip(kac, match[0]): print("  ", k, "h =", round(h[k], 4), "<->", lab[j])

# the twists: Ising^(nu) (h_s = nu/16, h_e = 1/2) times Fibonacci or its conjugate (h_t = 2/5 or 3/5), against the TCI's h
# mod 1 under the bijection found; and the central charges mod 8 (nu/2 and 14/5 or -14/5)
from fractions import Fraction as Fr
hT = {k: Fr(v).limit_denominator(1000) for k, v in h.items()}
found = []
for nu in range(1, 16, 2):
    for fib, hf, cf in (("Fib", Fr(2, 5), Fr(14, 5)), ("Fib-bar", Fr(3, 5), Fr(-14, 5))):
        hi = {"1": Fr(0), "s": Fr(nu, 16), "e": Fr(1, 2)}; hfib = {"1": Fr(0), "t": hf}
        lab = [(i, f) for i in ("1", "s", "e") for f in ("1", "t")]
        ok = all((hT[k] - hi[lab[j][0]] - hfib[lab[j][1]]) % 1 == 0 for k, j in zip(kac, match[0]))
        c = (Fr(nu, 2) + cf) % 8
        if ok: found.append({"ising_nu": nu, "fib": fib, "c_mod_8": str(c)})
print("twist-compatible products:", found, "| TCI c = 7/10")
import json, pathlib
json.dump({"kac": [list(k) for k in kac], "h": {str(k): str(v) for k, v in hT.items()}, "fusion_equal": bool(match),
           "bijections": len(match), "map": {str(k): "%s x %s" % (lab[j][0], lab[j][1]) for k, j in zip(kac, match[0])},
           "twist_products": found}, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
