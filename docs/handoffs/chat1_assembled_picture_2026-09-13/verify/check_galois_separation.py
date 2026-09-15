#!/usr/bin/env python3
"""Is B1331 §3's elimination of Galois EXACT?  i.e. does ANY automorphism of the
computing field invert the order-3 character chi while FIXING the trace field Q(sqrt-3)?
Computed in Gal(Q(zeta_12)/Q), the field B1331 actually computes over."""
import sympy as sp

n = 12
z = sp.exp(2*sp.pi*sp.I/n)                       # zeta_12
units = [k for k in range(1, n) if sp.gcd(k, n) == 1]   # Gal(Q(z_n)/Q) = (Z/nZ)^*
zeta3 = sp.simplify(z**4)                        # zeta_3
sqrtm3 = sp.simplify(zeta3 - zeta3**2)           # sqrt(-3)
ii     = sp.simplify(z**3)                       # i

def act(k, expr_pow):
    """sigma_k : z -> z^k ; apply to z**e"""
    return sp.simplify(z**((expr_pow*k) % n))

print("="*76)
print("Gal(Q(zeta_12)/Q) = (Z/12)^* =", units)
print("="*76)
print(f"{'sigma_k':>8} | {'zeta_3 ->':>12} | {'inverts chi?':>13} | {'sqrt(-3) ->':>12} | {'fixes trace fld?':>16}")
rows = []
for k in units:
    z3k = act(k, 4)                                # image of zeta_3 = z^4
    inverts = sp.simplify(z3k - zeta3**2) == 0     # zeta_3 -> zeta_3^{-1}
    s3k = sp.simplify(act(k,4) - act(k,8))         # image of sqrt(-3) = z^4 - z^8
    fixes_tf = sp.simplify(s3k - sqrtm3) == 0
    ik = act(k, 3)
    rows.append((k, inverts, fixes_tf, sp.simplify(ik-ii)==0))
    lbl = "zeta_3^-1" if inverts else ("zeta_3" if sp.simplify(z3k-zeta3)==0 else "?")
    print(f"{'sigma_'+str(k):>8} | {lbl:>12} | {str(inverts):>13} | "
          f"{('sqrt(-3)' if fixes_tf else '-sqrt(-3)'):>12} | {str(fixes_tf):>16}")

both = [k for k,inv,fix,_ in rows if inv and fix]
print()
print("  automorphisms that INVERT chi AND FIX Q(sqrt-3):", both)

# --- controls ---
alive  = any(inv for _,inv,_,_ in rows)            # some element does invert chi
alive2 = any(fix for _,_,fix,_ in rows)            # some element does fix the trace field
# the reason, stated and checked:  Q(zeta_3) == Q(sqrt-3)
x = sp.Symbol('x')
mp_s3 = sp.minimal_polynomial(sp.nsimplify(sqrtm3, [sp.sqrt(3)]), x)
mp_z3 = sp.minimal_polynomial(sp.nsimplify(zeta3,  [sp.sqrt(3)]), x)
same_field = (sp.expand(mp_s3 - (x**2 + 3)) == 0) and (sp.expand(mp_z3 - (x**2 + x + 1)) == 0)
print(f"  min poly of sqrt(-3) = {mp_s3}   min poly of zeta_3 = {mp_z3}")
print(f"\n  C-alive  (some sigma inverts chi)        : {alive}")
print(f"  C-alive2 (some sigma fixes Q(sqrt-3))    : {alive2}")
print(f"  Q(zeta_3) = Q(sqrt-3)  (zeta_3=(-1+sqrt-3)/2, sqrt-3^2=-3) : {same_field}")
if not (alive and alive2):
    print("  VERDICT: VOID"); raise SystemExit(1)

print()
print("  LEMMA (computed): the set is EMPTY. Every automorphism that inverts the order-3")
print("  character also moves sqrt(-3), i.e. conjugates the geometric holonomy to the")
print("  MIRROR. The obstruction is field-theoretic and unavoidable:")
print("     the character field Q(zeta_3) and the trace field Q(sqrt-3) ARE THE SAME FIELD,")
print("  so no automorphism separates chi <-> chi^-1 from rho <-> rho^mirror.")
print("  => B1331 section 3's elimination of Galois is EXACT, not merely an observation")
print("     about one isomorphism. It cannot be repaired by enlarging the field: adjoining")
print("     i (as B1331 does) adds sigma_7, which fixes zeta_3 and so does not invert chi.")
raise SystemExit(0 if len(both) == 0 else 1)
