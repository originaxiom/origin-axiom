#!/usr/bin/env python3
"""B8076 item 1 (field half) -- the weight field IS the charge field K, proved exactly.

Appendix B block (b) carries "the 78 weights; seven hyperplanes; certified gap" -- a
FLOATING-POINT census.  This replaces the field half of it with exact arithmetic.

Every factor of ad(x) for all four charges is an irreducible cubic in u = L^2.  Each has
discriminant with squarefree part 77, matching disc K = 6237 = 3^4.7.11.  But sharing a
resolvent is weaker than being the same field, so the decisive test is run: does the
weight cubic acquire a ROOT in K?

CONTROL: disc K and disc W differ enormously (6237 vs 2^66.3^22.5^2.7^9.11) while the
field is the same -- exactly the trap main registered as E41, "model invariant read as
field invariant".  Discriminants are model-borne; the field is the invariant.

QUANTIFIER: the ALGEBRA layer -- the ad-spectrum of the charge algebra on e6.
"""
import sympy as sp

t, u = sp.symbols('t u')
K = t**3 - 12*t - 5
W = u**3 - 15095808*u**2 + 56970854793216*u - 23922095638236364800

FAILED = []


def gate(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}{('  ' + detail) if detail else ''}")
    if not ok:
        FAILED.append(label)


def sqfree(n):
    s = 1
    for p, e in sp.factorint(abs(n)).items():
        if e % 2:
            s *= p
    return s


print("=" * 74)
print("ITEM 1 (field half) -- is the weight field the charge field?")
print("=" * 74)
dK, dW = sp.discriminant(K, t), sp.discriminant(W, u)
gate("the paper's charge field has disc 6237 = 3^4.7.11", dK == 6237, f"got {dK}")
print(f"      disc(weight cubic) = {sp.factorint(dW)}   -- a different number entirely")
gate("both have squarefree discriminant part 77", sqfree(dK) == sqfree(dW) == 77)
gate("the weight cubic is irreducible over Q", len(sp.factor_list(W)[1]) == 1)

th = sp.rootof(K, 0)
lin = [f for f, _ in sp.factor_list(W, extension=[th])[1] if sp.Poly(f, u).degree() == 1]
gate("DECISIVE: the weight cubic acquires a root in K", len(lin) == 1,
     f"{len(lin)} linear factor(s) over K")
if lin:
    print(f"\n      the K-rational root: {sp.expand(lin[0])} = 0")
print()
print("READING")
print("  The eigenvalues of ad on the charge algebra are K-VALUED.  The charge field and")
print("  the spectral field are the SAME field -- not two fields sharing Q(sqrt(77)).")
print("  This replaces the field half of block (b)'s floating-point census with exact")
print("  arithmetic.  The 14-locus itself is NOT certified here: B892 shows a^2 < 0, so")
print("  it is real-inaccessible, and certifying it needs arithmetic IN K, not over Q.")
if FAILED:
    raise SystemExit(f"CONTROLS FAILED: {FAILED}")
print("\n  ALL CHECKS PASS")
