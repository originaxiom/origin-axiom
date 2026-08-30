#!/usr/bin/env python3
"""SEAM-B (own code) — is the 2T-vs-A4 distinction the beat's bit, and where is it visible?

The center of 2T is -I = ker(2T ->> A4). Codex (memo/OA-C1056 sibling audit) argued "the
PRINCIPAL action on adjoint E6 factors through A4, so it cannot distinguish 2T from A4."
This bench asks the discriminating question on the OBJECT's stratum (the minimal A1 = the
fermion-capable holonomy stratum, B1112/B1145), not the principal:

  where does rho(-I) act nontrivially -- on the 27 (matter), on the 78 (adjoint), or both?

  rho(-I) = exp(i*pi*ad(h)) acts on a weight-w space as (-1)^w. So rho(-I) != I on a module
  iff that module has an ODD ad(h)-weight.

Reuses ONLY banked B1102 machinery (load_ccb + build_27). No golden_gate import.
"""
import os, importlib.util
from fractions import Fraction as F

_H=__import__("os").path.dirname(__import__("os").path.abspath(__file__))
_REPO=__import__("os").path.dirname(__import__("os").path.dirname(__import__("os").path.dirname(_H)))
BASE=__import__("os").path.join(_REPO,"frontier","B1102_exact_hypercharge_solve")
os.environ["B1102_CCB_PATH"] = os.path.join(BASE, "e6_bracket_vendored.py")
spec = importlib.util.spec_from_file_location("b1102_common", os.path.join(BASE, "b1102_common.py"))
c2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(c2)
ccb = c2.load_ccb()
weights, WIDX, rho27 = c2.build_27(ccb)
N, DIM, ROOTS, IDX = ccb.N, ccb.DIM, ccb.ROOTS, ccb.IDX
evec, br = ccb.evec, ccb.br
assert DIM == 78

def unit(i):
    v = [F(0)] * DIM; v[i] = F(1); return v

def adjoint_spectrum(h):
    """ad(h) eigenvalue multiset on e6 (78). Verifies ad(h) is diagonal in the basis."""
    spec = {}
    for i in range(DIM):
        img = br(h, unit(i))
        lam = img[i]
        # diagonal check
        for j in range(DIM):
            if j != i and img[j] != 0:
                raise RuntimeError(f"ad(h) not diagonal at ({i},{j})")
        assert lam.denominator == 1, ("non-integer adjoint weight", lam)
        spec[int(lam)] = spec.get(int(lam), 0) + 1
    return dict(sorted(spec.items()))

def parity_of(spec):
    """(#odd-weight dims, rho(-I) != I ?)"""
    odd = sum(v for k, v in spec.items() if k % 2 != 0)
    return odd, odd > 0

# ---------------- the object's stratum: minimal A1 (fermion-capable, B1112/B1145) ----------
r0 = ROOTS[0]; mr0 = tuple(-x for x in r0)
e = evec(r0)
h = [F(0)] * DIM
for k in range(N):
    h[k] = F(r0[k])
f = [-c for c in evec(mr0)]
assert all(a == b for a, b in zip(br(e, f), h)), "triple [e,f]=h failed"
assert all(a == 2 * b for a, b in zip(br(h, e), e)), "[h,e]=2e failed"

# adjoint spectrum
adj = adjoint_spectrum(h)
adj_odd, adj_minusI_nontrivial = parity_of(adj)

# 27 spectrum
H27 = rho27(h)
w27 = {}
for i in range(27):
    wi = int(H27[i][i]); w27[wi] = w27.get(wi, 0) + 1
w27 = dict(sorted(w27.items()))
m27_odd, m27_minusI_nontrivial = parity_of(w27)

# ---------------- the principal reference (codex's sl2): grading = 2*height ---------------
# principal h has <alpha_i, h> = 2 for every simple root, so ad(h)-eigenvalue on a root of
# height ht is 2*ht -- ALWAYS EVEN. (heights: ROOTS are in the simple-root basis.)
heights = [sum(a) for a in ROOTS]
principal_adj = {}
for ht in heights:
    principal_adj[2 * ht] = principal_adj.get(2 * ht, 0) + 1
for k in range(N):
    principal_adj[0] = principal_adj.get(0, 0) + 1  # Cartan
principal_adj = dict(sorted(principal_adj.items()))
princ_odd, princ_minusI_nontrivial = parity_of(principal_adj)

print("========= SEAM-B: where does rho(-I) live? =========")
print(f"OBJECT stratum = minimal A1 (fermion-capable, su(6) centralizer):")
print(f"  adjoint(78) ad(h) spectrum : {adj}")
print(f"    -> odd-weight dims: {adj_odd};  rho78(-I) != I : {adj_minusI_nontrivial}")
print(f"  matter(27) weight spectrum : {w27}")
print(f"    -> odd-weight dims: {m27_odd};  rho27(-I) != I : {m27_minusI_nontrivial}")
print()
print(f"PRINCIPAL sl2 (codex's reference): adjoint grading = 2*height, all even")
print(f"  adjoint(78) spectrum all even? {not princ_minusI_nontrivial}  (rho78(-I) != I : {princ_minusI_nontrivial})")
print()
print("VERDICT:")
if adj_minusI_nontrivial and m27_minusI_nontrivial and not princ_minusI_nontrivial:
    print("  On the OBJECT's minimal-A1 stratum, -I (the 2T center) acts NONTRIVIALLY on BOTH")
    print("  the 27 AND the 78 -- so the object's stratum DISTINGUISHES 2T from A4 on matter AND")
    print("  gauge. Codex's 'adjoint can't distinguish' is a PRINCIPAL-sl2 artifact (there the")
    print("  grading is 2*height, all even, -I trivial) and does NOT apply to the object's stratum.")
    print("  => codex's 2T-vs-A4 indistinguishability worry is DEFUSED: the object's own holonomy")
    print("     sl2 sees the center; the beat (B1141) is the spin-selection of that -I's lift.")
    print("  RESULT: SEAM-B resolves NUANCED-MATCH (the sealed clean-MATCH framing is corrected:")
    print("  the adjoint does NOT kill the object's -I; it is visible on BOTH modules).")
else:
    print("  unexpected parity pattern -- inspect the spectra above.")
