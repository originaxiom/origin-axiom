"""R18 blind recomputation — F2 (A2's price).

Claim under test (banked): the sibling family = det=+1, |tr|<=2 monodromies of the
once-punctured torus has:
  - orders 3/4/6 at |tr|<=1 and tr=0 (finite), infinite order at non-central tr=+-2
  - max|eigenvalue| = 1 EXACTLY for the whole family
  - pseudo-Anosov count 0 for the ENTIRE family
  - hyperbolicity ruled out three ways (Thurston pA=0; 0/8 SnapPy twister sibling
    builds geometric; 2 positive controls ARE geometric)
  - lemma: periodic / rational-slope (reducible) classes force |tr| <= 2

Everything symbolic where possible (sympy); SnapPy only for the sealed-instrument
style geometrization checks + planted-positive controls.
"""
import json
import sympy as sp

out = {}

# ---------------------------------------------------------------- symbolic part
x = sp.symbols('x')

# Conjugacy-invariant data: A in SL(2,Z), char poly x^2 - t x + 1.
# Order via Cayley-Hamilton: powers of A reduce to c1*A + c0*I with integer c's.
def order_of_trace(t, max_n=24):
    """Order of any NON-CENTRAL A in SL(2,Z) with trace t, computed via
    Cayley-Hamilton reduction A^n = f_n(t) A + g_n(t) I. A^n = I for non-central A
    iff f_n = 0 and g_n = 1 (as integers, exactly). Central A (=+-I) handled apart."""
    f, g = sp.Integer(1), sp.Integer(0)   # A^1 = 1*A + 0*I
    for n in range(1, max_n + 1):
        if n > 1:
            f, g = sp.expand(t * f + g), sp.expand(-f)  # A^(n) = A*A^(n-1), A^2 = tA - I
        if f == 0 and g == 1:
            return n
    return None  # no finite order found up to max_n -> infinite (for |t|<=2 this is exact, see below)

orders = {}
for t in [-2, -1, 0, 1, 2]:
    orders[t] = order_of_trace(sp.Integer(t))
out['orders_noncentral_by_trace'] = {str(k): v for k, v in orders.items()}
# central elements: tr=2 -> I (order 1), tr=-2 -> -I (order 2)
out['central_orders'] = {'2': 1, '-2': 2}

# Infinite order at non-central tr=+-2 is exact: A = +-(unipotent), A^n = +-(I + nN),
# N nilpotent nonzero -> never I. Verify symbolically with a representative:
for t, rep in [(2, sp.Matrix([[1, 1], [0, 1]])), (-2, sp.Matrix([[-1, 1], [0, -1]]))]:
    P = rep**12
    assert P != sp.eye(2), "unexpected finite order at tr=%d" % t
    # closed form: (+-1)^n (I + n*N) has off-diagonal n -> nonzero for n>0. exact.
out['tr_pm2_noncentral_infinite_order'] = True

# Spectral radius: eigenvalues of x^2 - t x + 1 for t in {-2..2}, EXACT.
specrad = {}
for t in [-2, -1, 0, 1, 2]:
    roots = sp.roots(x**2 - t * x + 1, x)
    m = max(sp.Abs(r) for r in roots)
    specrad[t] = sp.simplify(m)
out['max_abs_eigenvalue_by_trace'] = {str(k): str(v) for k, v in specrad.items()}
out['max_abs_eigenvalue_all_one_exactly'] = all(sp.simplify(v - 1) == 0 for v in specrad.values())

# Also do it for t symbolic on the real interval [-2,2]: |lambda|^2 = 1 when disc<0,
# and lambda=+-1 at t=+-2 -> spectral radius identically 1 on the family.
tsym = sp.symbols('t', real=True)
lam = (tsym + sp.sqrt(tsym**2 - 4)) / 2
mod2 = sp.simplify(sp.expand(lam * sp.conjugate(lam)).rewrite(sp.Abs))
# For |t|<2 the sqrt is imaginary: |lam|^2 = (t^2 + (4-t^2))/4 = 1
mod2_interior = sp.simplify(((tsym / 2)**2 + (sp.sqrt(4 - tsym**2) / 2)**2))
out['symbolic_interior_modulus_sq'] = str(mod2_interior)  # should be 1

# pseudo-Anosov count: Thurston/Nielsen for the once-punctured torus:
# class of A is pA  iff  |tr A| > 2 (spectral radius > 1, irrational invariant foliations);
# |tr|<=2 -> periodic (|tr|<=1 or central) or reducible (non-central tr=+-2, rational
# eigen-slope). Our family has |tr|<=2 by definition -> pA count 0. We verify the
# spectral-radius criterion exactly (above) and count:
pA_count = sum(1 for t in [-2, -1, 0, 1, 2] if not sp.simplify(specrad[t] - 1) == 0)
out['pA_count_family'] = pA_count

# Lemma direction (completeness): periodic => eigenvalues roots of unity on unit
# circle => |tr| = |2 cos(theta)| <= 2; reducible (rational slope preserved) =>
# rational eigenvalue r with r*(1/r)=1, r in Z (algebraic integer & rational)
# => r=+-1 => tr=+-2. Verify the periodic branch exhaustively: integer traces with
# finite order are exactly {-2,-1,0,1,2}:
finite_order_traces = []
for t in range(-10, 11):
    o = order_of_trace(sp.Integer(t), max_n=60)
    if o is not None or abs(t) == 2:  # central at +-2
        finite_order_traces.append(t)
out['finite_order_traces_scan_-10..10'] = finite_order_traces

# Planted-positive on the symbolic route: a hyperbolic (Anosov/pA) input MUST fire.
ctrl = sp.Matrix([[2, 1], [1, 1]])   # tr=3, figure-eight monodromy
ev = max(sp.Abs(r) for r in sp.roots(ctrl.charpoly(x).as_expr(), x))
out['control_tr3_specrad'] = str(sp.simplify(ev))
out['control_tr3_specrad_gt1'] = bool(sp.simplify(ev - 1) > 0)
out['control_tr3_is_pA'] = bool(abs(ctrl.trace()) > 2)

# ---------------------------------------------------------------- SnapPy part
# Once-punctured torus S_1_1, Dehn twists a (about alpha), b (about beta):
# a -> [[1,1],[0,1]], b -> [[1,0],[-1,1]] (a choice of convention; inverses A,B).
import snappy
from snappy import twister

Ma = sp.Matrix([[1, 1], [0, 1]])
Mb = sp.Matrix([[1, 0], [-1, 1]])
gens = {'a': Ma, 'b': Mb, 'A': Ma.inv(), 'B': Mb.inv()}

def word_matrix(w):
    M = sp.eye(2)
    for ch in w:
        M = M * gens[ch]
    return M

# choose 8 sibling words with |tr|<=2 covering traces (a fresh choice, not copied):
sibling_words = ['ab', 'ba', 'abab', 'ababab', 'aabb', 'abababab', 'aB' if False else 'bbaa', 'abba']
# fix: ensure all have |tr|<=2; recompute and filter/extend from a small enumeration
import itertools
cands = []
for L in range(2, 6):
    for w in itertools.product('abAB', repeat=L):
        w = ''.join(w)
        M = word_matrix(w)
        if abs(M.trace()) <= 2 and M != sp.eye(2) and M != -sp.eye(2):
            cands.append((w, int(M.trace())))
# pick 8 spanning available traces
picked, seen_tr = [], {}
for w, t in cands:
    if seen_tr.get(t, 0) < 2 and len(picked) < 8:
        picked.append((w, t))
        seen_tr[t] = seen_tr.get(t, 0) + 1
out['sibling_words'] = picked

surf = twister.Surface('S_1_1')
def build(word):
    try:
        m = surf.bundle(word)
        m = snappy.Manifold(m) if not isinstance(m, snappy.Manifold) else m
        return str(m.solution_type())
    except Exception as e:
        return 'BUILD_FAIL: %s' % e

sib_results = {}
for w, t in picked:
    sib_results[w] = build(w)
out['sibling_solution_types'] = sib_results
out['sibling_geometric_count'] = sum(1 for v in sib_results.values()
                                     if 'positively oriented' in v)

# planted-positive controls: hyperbolic monodromies MUST return geometric
controls = {}
for w in ['aB', 'aBaB']:   # tr(aB)=3 -> Anosov; figure-8 and its double
    M = word_matrix(w)
    controls[w] = {'trace': int(M.trace()), 'solution': build(w)}
out['controls'] = controls
out['controls_geometric'] = all('positively oriented' in c['solution']
                                for c in controls.values())

print(json.dumps(out, indent=2, default=str))
