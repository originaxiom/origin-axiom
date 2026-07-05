"""B437 (C2) -- the child's abelian torsion book: the "golden return" [RETRACTED as inheritance,
#562: numerator-forced, trefoil control] + the Lucas-square law.

Child = 4_1(5,1) (H1 = Z/5, B435). Abelian Reidemeister torsions via the surgery formula:
tau_j = Delta(zeta5^j)/(zeta5^j - 1)^2, Delta = t^2-3t+1 = (t-phi^2)(t-phi^-2) (GOLDEN roots).

RESULTS (exact, sympy poly arithmetic mod Phi_p + numeric crosscheck):
1. THE "GOLDEN RETURN" [RETRACTED as inheritance, #562 -- trefoil(5,1) gives the SAME
   Q(sqrt5); the field is forced by the numerator 5, not the parent]: tau's trace to the
   real subfield = 3 + sqrt(5)/5 in Q(sqrt5) -- and
   Q(sqrt5) IS the real subfield of Q(zeta5): the parent's golden field is literally the
   child's abelian character field. Slope 5 -> Z/5 -> zeta5 -> sqrt5: the loop closes.
2. THE LUCAS-SQUARE LAW: total abelian torsion prod_j |Delta(zeta_p^j)| = |2 - L_{2p}| = L_p^2
   (classical L_{2n} = L_n^2 + 2 for odd n): child (p=5) -> L_5^2 = 121 = 11^2; sibling
   (p=7) -> L_7^2 = 841 = 29^2. Also = |H1| of the parent's p-fold cyclic branched cover.
3. CONTROL DICHOTOMY (the bar's leg iv, exact): the Lucas-square law is FAMILY-GENERIC
   (every child obeys it) but the GOLDEN FIELD RETURN is slope-5-SPECIFIC (sqrt5 in Q(zeta5);
   Q(zeta7)+ is cubic, disc 49 -- no sqrt5). The forced child speaks the parent's language;
   the unforced sibling does not.
4. The child's torsion prime 11 lies in the parent's Fibonacci apparition set (B423) -- noted.

Firewall: torsion/cyclotomic arithmetic -- mathematics. No physics claim.
"""
import os, json, cmath
import sympy as sp
t = sp.Symbol('t')
D = sp.Poly(t**2 - 3*t + 1, t)

def L(n):
    a, b = 2, 1
    for _ in range(n): a, b = b, a+b
    return a

def total_torsion(p):
    Phi = sp.Poly(sum(t**k for k in range(p)), t)
    return abs(int(sp.resultant(Phi.as_expr(), D.as_expr(), t)))

def golden_trace():
    """Tr_{Q(zeta5)/Q(sqrt5)} of tau = Delta/(t-1)^2 mod Phi5, exact."""
    Phi = sp.Poly(sum(t**k for k in range(5)), t)
    inv_den = sp.invert(sp.Poly((t-1)**2, t), Phi)
    tau = (D * inv_den) % Phi
    s4 = sp.Poly(tau.as_expr().subs(t, t**4), t) % Phi
    half = (tau + s4) % Phi
    h = half.all_coeffs()[::-1]; h += [sp.Integer(0)]*(4-len(h))
    w = (-1+sp.sqrt(5))/2                     # zeta+zeta^4
    # half = h0 + h1*z + h2*z^2 + h3*z^3 with h1 = 0, h2 = h3 (Galois-invariant):
    assert h[1] == 0 and h[2] == h[3]
    return sp.simplify(h[0] + h[2]*(-1 - w))

if __name__ == "__main__":
    gt = golden_trace()
    z = cmath.exp(2j*cmath.pi/5)
    num = sum((z**j**1)**0 for j in [])  # noop
    tau_n = lambda j: ((z**j)**2 - 3*z**j + 1)/(z**j-1)**2
    chk = tau_n(1) + tau_n(4)
    assert abs(float(gt) - chk.real) < 1e-12 and abs(chk.imag) < 1e-12
    t5, t7 = total_torsion(5), total_torsion(7)
    print("golden trace:", gt, " (numeric check passed)")
    print("totals: child", t5, "= L5^2 =", L(5)**2, " sibling", t7, "= L7^2 =", L(7)**2)
    assert t5 == L(5)**2 == 121 and t7 == L(7)**2 == 841
    json.dump(dict(golden_trace=str(gt), child_total=t5, sibling_total=t7,
                   lucas_law="|2-L_{2p}| = L_p^2 (odd p; L_{2n}=L_n^2+2)",
                   apparition_11=True),
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "abelian_book.json"), "w"),
              indent=1)
    print("[written] abelian_book.json")
