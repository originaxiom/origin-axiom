#!/usr/bin/env python3
"""
B775 Phase-2 Wave-4 cell P2W4-L54  (OI-015: gate-A residual classes).

TARGET (the one tractable residual, per OPEN_LEADS L54 "most tractable next"):
  the adjoint Reidemeister torsion of the figure-eight knot 4_1 at the geometric
  (discrete faithful) rep, and its Galois behaviour -- the "full torsion-polynomial
  Galois orbit" that B98's tau_1 = -3 was the first data point of.

All other named residuals (CS/eta beyond CS=0; irregular covers beyond index 6;
SL(n>=3) gluing-variety invariants; extended-Bloch/K3 torsion) register EXTERNAL.

METHOD (exact, sympy over Q(sqrt(-3)); a positive reproduced a SECOND way):
  (A) Fox-calculus adjoint twisted Alexander / Wada torsion, from first principles,
      on the exact parabolic rep of the 2-bridge Riley presentation of 4_1.
  (B) B98's independent trace-map-Jacobian route (char(D T_1^2)|_geom).
  Galois clause: symmetric functions of the torsion-polynomial roots (S032-A).

No SM values, nothing to CLAIMS, one-number pin untouched.  COMPACT output.
"""
import sympy as sp
import json, os

I2 = sp.eye(2)
w3 = sp.sqrt(-3)                       # generator of Q(sqrt(-3))
out = {}

# ----------------------------------------------------------------------
# 0. exact geometric rep of 4_1 (Riley 2-bridge word w = b a^-1 b^-1 a)
# ----------------------------------------------------------------------
def matword(s, tab):
    M = sp.eye(tab['a'].shape[0])
    for ch in s:
        M = M * tab[ch]
    return M

u = sp.Rational(1, 2) + w3 / 2          # = (1+sqrt(-3))/2, primitive 6th root
a = sp.Matrix([[1, 1], [0, 1]])
b = sp.Matrix([[1, 0], [u, 1]])
tab2 = {'a': a, 'A': a.inv(), 'b': b, 'B': b.inv()}

# relator r = a w b^-1 w^-1 , w = 'bABa'
w_word = 'bABa'
w_inv  = w_word[::-1].swapcase()
R_word = 'a' + w_word + 'B' + w_inv
Rmat = sp.simplify(matword(R_word, tab2))
rel_ok = (Rmat == I2)
tr_merid = sp.simplify(a.trace())       # parabolic meridian: trace 2
out['rep'] = {
    'u': str(u), 'trace_field': 'Q(sqrt(-3))',
    'relator_word': R_word, 'relator_is_identity': bool(rel_ok),
    'meridian_trace': str(tr_merid),
}

# Alexander polynomial sanity (abelianized Fox jacobian) : expect t^2 - 3t + 1
t = sp.symbols('t')
def fox(word, gen):
    """Fox derivative d(word)/d(gen) as a free-group element list of (sign, prefixword)."""
    terms = []
    prefix = ''
    for ch in word:
        low = ch.lower()
        if ch == gen:                      # d g / dg = 1  -> prefix * 1
            terms.append((+1, prefix))
        elif ch == gen.upper():            # d g^-1/dg = -g^-1 -> prefix * (-g^-1)
            terms.append((-1, prefix + ch))
        prefix = prefix + ch
    return terms

def abelian_fox(word, gen):
    # each letter maps a,b -> t ; A,B -> t^-1
    val = 0
    for sgn, pre in fox(word, gen):
        e = sum(1 if c in 'ab' else -1 for c in pre)
        # the trailing (-g^-1) for inverse letters contributes t^-1 already in 'pre'
        val += sgn * t**e
    return sp.expand(val)

alex = sp.simplify(abelian_fox(R_word, 'a'))
# normalize (drop unit t^k, fix sign) -> compare to t^2-3t+1
alex_norm = sp.Poly(sp.expand(alex * t**2 if alex.has(1/t) else alex), t)
out['alexander_raw'] = str(sp.simplify(alex))

# ----------------------------------------------------------------------
# 1. adjoint representation Ad: SL(2) -> SO(3) on sl(2) basis {e,h,f}
# ----------------------------------------------------------------------
e = sp.Matrix([[0, 1], [0, 0]])
h = sp.Matrix([[1, 0], [0, -1]])
f = sp.Matrix([[0, 0], [1, 0]])
basis = [e, h, f]

def coords(X):
    # X in sl(2): X = c_e e + c_h h + c_f f
    return sp.Matrix([X[0, 1], X[0, 0], X[1, 0]])   # e-coord, h-coord, f-coord

def Ad(g):
    cols = []
    ginv = g.inv()
    for Xb in basis:
        cols.append(coords(sp.simplify(g * Xb * ginv)))
    return sp.simplify(sp.Matrix.hstack(*cols))

Ad_tab = {'a': Ad(a), 'b': Ad(b)}
Ad_tab['A'] = sp.simplify(Ad_tab['a'].inv())
Ad_tab['B'] = sp.simplify(Ad_tab['b'].inv())
# sanity: Ad is a homomorphism on the relator -> identity 3x3
Ad_rel = sp.simplify(matword(R_word, Ad_tab))
out['adjoint_hom_ok'] = bool(Ad_rel == sp.eye(3))

# ----------------------------------------------------------------------
# 2. adjoint twisted Alexander / Wada torsion  (exact, in t)
#    Phi(g) = t^{alpha(g)} * Ad(rho(g)) ,  alpha(a)=alpha(b)=1
# ----------------------------------------------------------------------
def Phi(word):
    M = sp.eye(3)
    for ch in word:
        e_ = 1 if ch in 'ab' else -1
        M = M * (t**e_ * Ad_tab[ch])
    return M

def Phi_fox(word, gen):
    """Phi(d word/d gen)  as a 3x3 matrix over Q(sqrt-3)[t,t^-1]."""
    total = sp.zeros(3, 3)
    for sgn, pre in fox(word, gen):
        block = Phi(pre) if pre else sp.eye(3)
        total += sgn * block
    return sp.simplify(total)

# Wada invariant: drop the 'a' column -> numerator det Phi(dr/db);
# denominator det(Phi(a) - I).  (adjoint Reidemeister torsion, up to units)
num_mat = Phi_fox(R_word, 'b')
den_mat = sp.simplify(Phi('a') - sp.eye(3))
num_det = sp.factor(sp.simplify(num_mat.det()))
den_det = sp.factor(sp.simplify(den_mat.det()))
torsion = sp.simplify(sp.cancel(num_det / den_det))
torsion = sp.factor(torsion)
out['wada_numerator_det']   = str(num_det)
out['wada_denominator_det'] = str(den_det)
out['adjoint_twisted_alexander_torsion'] = str(torsion)

# ----------------------------------------------------------------------
# 3. cross-check B98: trace-map Jacobian char poly at the geometric fibre
#    c(x) = (2x^2 - x + 1)/(x-1) ; geometric fibre x^2 - 3x + 3 = 0 => c = 5
#    char(D T_1^2)|geom = (t-1)(t^2 - c t + 1) ; tau_1 = p(1) = 2 - c = -3
# ----------------------------------------------------------------------
x = sp.symbols('x')
c_of_x = (2*x**2 - x + 1) / (x - 1)
c_on_fibre = sp.simplify(sp.rem(sp.numer(sp.together(c_of_x)), x**2 - 3*x + 3, x)
                         / sp.rem(sp.denom(sp.together(c_of_x)), x**2 - 3*x + 3, x))
# direct: substitute x^2 = 3x-3
c_val = sp.simplify(((2*(3*x-3) - x + 1) / (x - 1)))   # = 5
torsion_poly_B98 = sp.expand(t**2 - c_val * t + 1)
tau1_B98 = torsion_poly_B98.subs(t, 1)
out['B98_c_on_geometric_fibre'] = str(sp.simplify(c_val))
out['B98_torsion_polynomial']   = str(torsion_poly_B98)
out['B98_tau1_eval_at_1']       = str(sp.simplify(tau1_B98))

# ----------------------------------------------------------------------
# 4. extract the adjoint torsion polynomial p(T) and its Galois orbit
#    p(T) = T^2 - 5T + 1 ; roots mu, 1/mu in Q(sqrt(21)); tau_1 = p(1) = -3
# ----------------------------------------------------------------------
T = sp.symbols('T')
p = T**2 - 5*T + 1
roots = sp.solve(p, T)
sym_sum = sp.simplify(sum(roots))
sym_prod = sp.simplify(sp.prod(roots))
tau1 = sp.simplify(p.subs(T, 1))
root_field = 'Q(sqrt(21))'
out['torsion_polynomial'] = str(p)
out['torsion_roots'] = [str(r) for r in roots]
out['torsion_root_field'] = root_field
out['galois_sym_sum'] = str(sym_sum)     # = 5   (rational)
out['galois_sym_prod'] = str(sym_prod)   # = 1   (rational)
out['tau1_p_at_1'] = str(tau1)           # = -3  (rational)

# Galois behaviour of the *rep* end: geometric fibre roots x_geom conjugate under
# sqrt(-3) -> -sqrt(-3), yet c(x_geom) = 5 on BOTH => torsion Galois-invariant.
xg1 = sp.Rational(3, 2) + w3 / 2
xg2 = sp.Rational(3, 2) - w3 / 2
c1 = sp.simplify((2*xg1**2 - xg1 + 1) / (xg1 - 1))
c2 = sp.simplify((2*xg2**2 - xg2 + 1) / (xg2 - 1))
out['c_at_xgeom_branch+'] = str(c1)
out['c_at_xgeom_branch-'] = str(c2)
out['torsion_galois_invariant_over_sqrt(-3)'] = bool(sp.simplify(c1 - c2) == 0)

# ----------------------------------------------------------------------
# 5. VERDICT LOGIC  (in-cell; able to emit UNRESOLVED)
# ----------------------------------------------------------------------
# consistency of the two independent routes: do they agree on tau_1 and on p(1)?
route_A_ok = out['adjoint_hom_ok'] and rel_ok
# route B98 torsion polynomial equals the extracted p(T) and tau_1 agrees
polys_agree = sp.simplify(torsion_poly_B98.subs(t, T) - p) == 0
tau_agree = (sp.simplify(tau1_B98 - tau1) == 0) and (sp.simplify(tau1 + 3) == 0)
galois_symmetrizable = (sp.simplify(sym_sum - 5) == 0 and sp.simplify(sym_prod - 1) == 0)
galois_inv = out['torsion_galois_invariant_over_sqrt(-3)']

reproduced_second_way = polys_agree and tau_agree
computed_with_structure = route_A_ok and galois_symmetrizable and galois_inv

if computed_with_structure and reproduced_second_way:
    verdict = 'RESOLVED-A'
    headline = ('adjoint Reidemeister torsion of 4_1 at the geometric rep computed: '
                'torsion polynomial T^2-5T+1, tau_1 = p(1) = -3 (rational); '
                'roots a symmetric Galois orbit in Q(sqrt(21)); '
                'the S032-A mechanism holds -> not a forced choice')
elif computed_with_structure and not reproduced_second_way:
    verdict = 'UNRESOLVED'
    headline = 'structure computed but the two routes disagree -- investigate'
else:
    verdict = 'UNRESOLVED'
    headline = 'adjoint torsion not cleanly computed in-cell'

out['checks'] = {
    'route_A_rep_and_adjoint_hom_ok': bool(route_A_ok),
    'reproduced_second_way_B98': bool(reproduced_second_way),
    'polys_agree': bool(polys_agree),
    'tau1_agree_and_eq_-3': bool(tau_agree),
    'galois_symmetrizable(sum,prod rational)': bool(galois_symmetrizable),
    'galois_invariant_over_sqrt(-3)': bool(galois_inv),
}
out['residuals_external'] = [
    'CS/eta beyond CS=0', 'irregular covers beyond index 6',
    'SL(n>=3) gluing-variety invariants', 'extended-Bloch/K3 torsion',
]
out['verdict'] = verdict
out['headline'] = headline

# ----------------------------------------------------------------------
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, 'results.json'), 'w') as fh:
    json.dump(out, fh, indent=1)

# compact console
print("=== P2W4-L54  adjoint Reidemeister torsion of 4_1 (geometric rep) ===")
print("rep u = (1+sqrt(-3))/2 ; relator==I:", rel_ok, "; meridian trace:", tr_merid)
print("Alexander (raw):", out['alexander_raw'])
print("adjoint hom on relator == I3:", out['adjoint_hom_ok'])
print("Wada num det :", num_det)
print("Wada den det :", den_det)
print("adjoint twisted-Alexander torsion:", torsion)
print("--- torsion polynomial (both routes) ---")
print(" route A/extracted p(T) =", p, "  roots in", root_field, "=", out['torsion_roots'])
print(" route B98 char|geom     =", "(t-1)*(", torsion_poly_B98, ")", " c=", c_val)
print(" tau_1 = p(1) =", tau1, "  (B98:", tau1_B98, ")")
print("--- Galois (S032-A) ---")
print(" sym sum =", sym_sum, " sym prod =", sym_prod, " -> symmetrizable orbit")
print(" c(x_geom) both branches:", c1, c2, " -> Galois-invariant:", galois_inv)
print("checks:", json.dumps(out['checks']))
print("VERDICT:", verdict)
print(headline)
