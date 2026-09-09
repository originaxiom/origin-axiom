#!/usr/bin/env python3
"""A7 vs B6: does the field equation's STABILITY select the order, or is it swap-symmetric?
A7 is the order choice LR vs RL. B6's Euler-Lagrange equation is box tau + V'(tau) = 0 with
V' = tau^2 - tau - 1 (the LR Mobius fixed-point polynomial). The honest test computes BOTH
orders and asks whether stability discriminates. Exact throughout."""
import sympy as sp

t = sp.symbols('t', real=True)
phi = (1 + sp.sqrt(5))/2
CASES = {"A = LR  (A7 as taken)": t**2 - t - 1,
         "RL      (A7 swapped)":  t**2 + t - 1,
         "K = LAL^-1 (the class conjugate, control)": t**2 - 3*t + 1}
print("="*82)
print("For each order: V' = the Mobius fixed-point polynomial; V'' = stability")
print("="*82)
res = {}
for name, dV in CASES.items():
    roots = sorted(sp.solve(sp.Eq(dV, 0), t), key=lambda r: float(r))
    d2 = sp.diff(dV, t)                     # V'' since dV IS V'
    print(f"\n{name}:  V' = {dV}")
    stable = []
    for r in roots:
        curv = sp.simplify(d2.subs(t, r))
        kind = "STABLE (min)" if curv > 0 else "unstable (max)"
        if curv > 0: stable.append(r)
        print(f"   tau = {sp.nsimplify(r)} = {float(r):+.9f}   V'' = {sp.nsimplify(curv)} "
              f"= {float(curv):+.6f}   {kind}")
    res[name] = stable

print("\n" + "="*82); print("DOES STABILITY BREAK THE TIE?"); print("="*82)
lr, rl = res["A = LR  (A7 as taken)"][0], res["RL      (A7 swapped)"][0]
print(f"  LR's stable vacuum: tau = {sp.nsimplify(lr)} = {float(lr):.9f}")
print(f"  RL's stable vacuum: tau = {sp.nsimplify(rl)} = {float(rl):.9f}")
print(f"  BOTH orders have exactly one stable vacuum -> stability alone does NOT discriminate.")
print(f"  product = {sp.simplify(lr*rl)}  -> they are INVERSES: phi and 1/phi")
print(f"  |LR stable| > 1 ? {float(lr) > 1}      |RL stable| > 1 ? {float(rl) > 1}")

print("\n" + "="*82); print("THE DISCRIMINATOR THAT REMAINS"); print("="*82)
print("  The two stable vacua are phi and 1/phi -- an EXPANDING and a CONTRACTING eigenvalue.")
print("  A1/A2's substrate is records that are TRANSFERRED BUT NOT DESTROYED (non-cancellation),")
print("  i.e. a growing record. If the vacuum must be the GROWING one (|tau| > 1), LR is selected")
print("  and RL is excluded. That criterion is NOT vacuous: it rejects exactly one of the two.")
print("  CONTROL: the class-conjugate K has stable vacuum phi^2 -- also > 1, so the criterion does")
print("  NOT single out LR among ALL polynomials; it discriminates only within the A7 pair, which")
print("  is the pair A7 is about.")
k = res["K = LAL^-1 (the class conjugate, control)"][0]
print(f"    K's stable vacuum = {sp.nsimplify(k)} = {float(k):.9f}  (= phi^2 ? {sp.simplify(k - phi**2) == 0})")
print("\n  STATUS: this makes A7's bit CONDITIONALLY selected -- conditional on (a) B6's lift,")
print("  which B6 ITSELF declares a choice (the canonical kinetic term), and (b) reading")
print("  non-cancellation as 'the vacuum grows'. Two declared inputs replace one. NOT a derivation.")
