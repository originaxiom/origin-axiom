"""B602 cell N1 (sealed order; runs after N0 banked #968): the X1 phase
cells, exact. J-norm cells: INVALID-DEGENERATE (g_4 = g_8 = 0, N0).

Live cells: W x identity-D and W x D. The W-norm classical cross-ratio is
r_cl = (N8/N4)(tau4/tau8) (1-w)/(1+w) with POSITIVE rational prefactor
(banked integers), so arg(r_cl) = arg((1-w)/(1+w)) exactly; the stage
ratio arg is arg(hbar3/h3) in both cells (D-norm divides by positive
reals phi, 1). Verdicts printed; the outcome statement waits for N2.
"""
import sympy as sp

w = sp.I * sp.sqrt(3)
phi = (1 + sp.sqrt(5)) / 2
h3 = 1 / (2 * phi) + sp.I * sp.sin(2 * sp.pi / 5) / sp.sqrt(5)

arg_cl = sp.arg((1 - w) / (1 + w))
arg_st = sp.arg(sp.conjugate(h3) / h3)
acl = sp.simplify(arg_cl)
ast_ = sp.nsimplify(sp.simplify(arg_st), [sp.pi])
print(f"classical W-norm phase: arg((1-w)/(1+w)) = {acl} (exact)")
print(f"stage phase (identity-D and D-norm alike): {ast_} (exact)")
diff = sp.simplify(acl - ast_)
print(f"residual: {diff} = {sp.nsimplify(diff, [sp.pi])} "
      f"(numeric {float(diff):+.9f})")
for cell, dnote in (("W x identity-D", "d = (1,1)"), ("W x D", "d = (phi,1)")):
    match = sp.simplify(acl - ast_) == 0
    print(f"X1 [{cell}] ({dnote}): phase match: {bool(match)}  "
          f"(|residual| = {abs(float(diff)):.6f} rad vs 1e-9)")
print("X1 [J x identity-D]: INVALID-DEGENERATE (g = 0, per the seal)")
print("X1 [J x D]:          INVALID-DEGENERATE (g = 0, per the seal)")
print("N1 DONE (banked blind before N2)")
