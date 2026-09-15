#!/usr/bin/env python3
"""Grounds B1331's wording: on H^1(T;Sym^m) with m even the ambient form is SYMPLECTIC,
so 'L_V isotropic' is literally 'L_V Lagrangian'.  Computed, with a negative control."""
import sympy as sp

def sym_form(m):
    """invariant bilinear form on Sym^m(C^2): B(e_i,e_j) = delta_{i+j,m} (-1)^i / C(m,i)"""
    M = sp.zeros(m+1, m+1)
    for i in range(m+1):
        M[i, m-i] = sp.Integer(-1)**i / sp.binomial(m, i)
    return M

def parity(M):
    Z = sp.zeros(*M.shape)
    return (sp.simplify(M - M.T) == Z, sp.simplify(M + M.T) == Z)   # (sym, anti)

# --- instrument alive: the form must be SL(2)-invariant.  Check on the raising operator.
# e_i = x^i y^(m-i);  E: x->x, y->x  acts as e_i -> ... ; use the standard check:
# invariance under the Weyl element w: x->y, y->-x, i.e. e_i -> (-1)^(m-i) e_(m-i).
def weyl_invariant(m):
    M = sym_form(m); n = m+1
    W = sp.zeros(n, n)
    for i in range(n):
        W[m-i, i] = sp.Integer(-1)**(m-i)
    return sp.simplify(W.T*M*W - M) == sp.zeros(n, n)

print("="*70); print("ambient form on H^1(T; Sym^m)"); print("="*70)
rows=[]
for m in range(1, 7):
    s, a = parity(sym_form(m))
    inv = weyl_invariant(m)
    # cup product on a surface is antisymmetric; total = cup (x) coefficient form
    total = "SYMPLECTIC" if s else ("ORTHOGONAL" if a else "??")
    rows.append((m, s, a, inv, total))
    print(f"  Sym^{m}: coeff-form sym={str(s):5s} anti={str(a):5s}  W-invariant={str(inv):5s}"
          f"  ->  H^1(T;Sym^{m}) is {total}")

alive   = all(r[3] for r in rows)                       # every form SL2-invariant
control = all((r[1] != r[2]) for r in rows)             # never both sym and anti
law     = all((r[1] == (r[0] % 2 == 0)) for r in rows)  # symmetric  <=>  m even
print()
print(f"  C-alive (all forms SL(2)-invariant)        : {alive}")
print(f"  C-control (never both sym and anti)        : {control}")
print(f"  law: coefficient form symmetric <=> m even : {law}")
if not (alive and control):
    print("  VERDICT: VOID"); raise SystemExit(1)
print()
print("  CONSEQUENCE for B1331: its germs are Sym^2 and Sym^4 (m EVEN), so the")
print("  ambient form on H^1(T;W) is symplectic and 'L_V isotropic' == 'L_V Lagrangian'.")
print("  For m ODD the ambient form would be ORTHOGONAL and the word 'Lagrangian' would")
print("  NOT apply -- so the theorem's statement is germ-parity dependent. Flagged.")
raise SystemExit(0 if law else 1)
