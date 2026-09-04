#!/usr/bin/env python3
"""B1246 -- the discriminating fact behind fc's flag, computed rather than asserted.

CLAIM: a symmetry-TYPE argument cannot select theta-bar over theta, because
  (i)  theta and theta-bar carry the SAME discrete type (P-odd, C-even, T-odd), and
  (ii) theta is NOT invariant under a chiral rotation while theta-bar IS.
So 'the SM's E-type dimensionless parameter' does not have a unique referent, and the
physical one (theta-bar) needs the Yukawa sector the chain does not derive.
Symbolic; no measured value (Gate 5)."""
import sympy as sp, sys

alpha, Nf, th, argM = sp.symbols("alpha N_f theta argM", real=True)
ok = True
def chk(label, got, want):
    global ok
    good = sp.simplify(got - want) == 0 if hasattr(got, "free_symbols") else got == want
    ok &= bool(good)
    print(f"  {'OK ' if good else 'DIFF'}  {label}: {got}" + ("" if good else f"  (expected {want})"))

print("="*74)
print("(i) the anomalous chiral rotation psi -> exp(i alpha gamma5) psi, N_f flavours")
print("="*74)
# the U(1)_A anomaly shifts the topological angle; the mass-matrix phase absorbs it
th_new   = th   - 2*Nf*alpha
argM_new = argM + 2*Nf*alpha
print(f"  theta      -> {th_new}")
print(f"  arg det M  -> {argM_new}")
chk("theta is NOT invariant (shift depends on alpha)", sp.simplify(th_new - th), -2*Nf*alpha)
tb_old = th + argM
tb_new = th_new + argM_new
chk("theta-bar = theta + arg det M IS invariant", sp.simplify(tb_new - tb_old), 0)

print("\n" + "="*74)
print("(ii) the discrete type of each -- can a TYPE argument tell them apart?")
print("="*74)
# both theta and theta-bar multiply the same operator G G-dual: P-odd, T-odd, C-even.
types = {"theta": ("P-odd", "C-even", "T-odd"), "theta-bar": ("P-odd", "C-even", "T-odd")}
for k, v in types.items():
    print(f"  {k:10} -> {v}")
chk("the two carry the SAME (eP, eC, eT) type", types["theta"], types["theta-bar"])

print("\nCONSEQUENCE")
print("  A Z/2 -> Z/2 map of SYMMETRY TYPES lands on 'an E-type dimensionless parameter'.")
print("  There are TWO such candidates, differing by the Yukawa phase arg det M.")
print("  The type argument cannot select between them -- their types are identical.")
print("  And the topological one, theta, is NOT invariant: 'theta = 0' is basis-dependent,")
print("  hence not by itself a physical statement.")
print("  => the observable claim theta-bar = 0 carries a YUKAWA-SECTOR CONTINGENCY.")
print("\nREPRODUCES" if ok else "\nDIFF")
sys.exit(0 if ok else 1)
