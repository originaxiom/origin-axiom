"""B1062 V2 -- the leading test (Maclachlan-Reid conjugate-boundedness) with the
box-count illustration. Sealed ad8d60f1 + addendum B1062-A1 (binding: m=1 is a
PIPELINE GATE; the conjugate test leads; box-counts illustrate).

Method (exact throughout, sympy):
  Fiber monodromy of metallic member m = phi_m^2, phi_m: a -> a^m b, b -> a.
  Discrete-faithful fiber traces = fixed point of the induced trace map on the
  Markov surface x^2+y^2+z^2 - xyz = 0  (kappa = tr[a,b] = -2, the cusp).
  Solve exactly; pick the geometric orbit; extract the trace field K_m.
  Leading test: for each non-identity, non-conjugation embedding of K_m, is the
  conjugated triple inside the bounded (SU(2)) locus [-2,2]^3-real? Unbounded
  conjugate <=> B-C fails (Hao Thm 2.3 as bound in the addendum).
  Pipeline gate: m=1's field must contain sqrt(-3) (banked) -- else HALT.
  Illustration: word-trace growth under each embedding, fixed window, declared.
"""
import sympy as sp
from sympy import symbols, Poly, groebner, QQ, sqrt, I, simplify, expand

x, y, z = symbols('x y z')

# ---- Fricke machinery: trace of a word in F2 = <a,b> as polynomial in (x,y,z)
# with x=tr a, y=tr b, z=tr ab. Standard identities:
#   tr(w a) via tr(uv) = tr(u)tr(v) - tr(u v^-1). We compute by matrix-free
#   recursion on words using the pair (tr w, tr wa, tr wb, tr wab) transported.
# Simpler robust route: SYMBOLIC 2x2 matrices with entries chosen so traces are
# (x,y,z) exactly: the classical Fricke parametrization
#   A = [[x, 1], [0? ...]] -- use A=[[x,1],[-1,0]]? tr=x, det=1 ✓
#   B = [[0? ...]] need tr B = y, tr AB = z: B = [[y - z*t?, ...]] -- use:
#   A = [[x, 1], [-1, 0]],  B = [[0, u], [-1/u, y]] with u free? tr AB = -u^{-1}?
# Cleanest: B = [[y, v],[w, 0]]? tr=y, det = -vw =1 -> w = -1/v; tr AB = x*y + v - ...
# Take the standard: A=[[x,1],[-1,0]], B=[[0,-v],[1/v, y]] (det=1),
#   AB = [[1/v? ...]] -- compute symbolically and SOLVE v so tr AB = z.
v = symbols('v')
A = sp.Matrix([[x, 1], [-1, 0]])
B = sp.Matrix([[0, -v], [1/v, y]])
trAB = sp.trace(A*B)
vsol = sp.solve(sp.Eq(trAB, z), v)
B = B.subs(v, vsol[0])
B = sp.simplify(B)
assert sp.simplify(sp.trace(A) - x) == 0
assert sp.simplify(sp.trace(B) - y) == 0
assert sp.simplify(sp.trace(A*B) - z) == 0
assert sp.simplify(A.det() - 1) == 0 and sp.simplify(B.det() - 1) == 0
print("[V2-0] Fricke parametrization built: tr A=x, tr B=y, tr AB=z, dets=1", flush=True)

Ainv, Binv = A.inv(), B.inv()

def word_matrix(word):
    M = sp.eye(2)
    for ch in word:
        M = M * {"a": A, "A": Ainv, "b": B, "B": Binv}[ch]
    return M

def word_trace_poly(word):
    t = sp.trace(word_matrix(word))
    return sp.simplify(sp.cancel(sp.together(t)))

# commutator check: tr[a,b] = x^2+y^2+z^2 - xyz - 2 (classical)
comm = word_trace_poly("abAB")
assert sp.simplify(comm - (x**2 + y**2 + z**2 - x*y*z - 2)) == 0
print("[V2-0] tr[a,b] identity verified: x²+y²+z²-xyz-2", flush=True)

# ---- the metallic substitution phi_m: a -> a^m b, b -> a ; monodromy = phi_m^2
def phi_words(m):
    wa = "a"*m + "b"          # phi(a)
    wb = "a"                   # phi(b)
    # phi^2: a -> phi(wa) = (a^m b)^m a ... build by substitution
    def sub(word):
        out = []
        for ch in word:
            out.append({"a": wa, "b": wb,
                        "A": inv(wa), "B": inv(wb)}[ch])
        return "".join(out)
    def inv(w):
        return "".join({"a":"A","A":"a","b":"B","B":"b"}[c] for c in reversed(w))
    w2a, w2b = sub(wa), sub(wb)
    return w2a, w2b

def trace_map(m):
    """the induced map on (x,y,z) for monodromy phi_m^2, via word traces."""
    w2a, w2b = phi_words(m)
    Ta = word_trace_poly(w2a)
    Tb = word_trace_poly(w2b)
    Tab = word_trace_poly(w2a + w2b)
    return Ta, Tb, Tab

MARKOV = x**2 + y**2 + z**2 - x*y*z   # kappa = -2 level

def geometric_points(m, timeout_note=""):
    Ta, Tb, Tab = trace_map(m)
    eqs = [sp.numer(sp.together(Ta - x)),
           sp.numer(sp.together(Tb - y)),
           sp.numer(sp.together(Tab - z)),
           MARKOV]
    print(f"[V2-{m}] solving fixed-point system on the Markov surface "
          f"(deg-bounds {[sp.total_degree(e) for e in eqs]}) {timeout_note}", flush=True)
    sols = sp.solve(eqs, [x, y, z], dict=True)
    return sols

def bounded_locus(triple):
    """SU(2)-locus test: all three real in [-2,2] (necessary+sufficient for a
    2-generator subgroup with these traces to be conjugate into SU(2), on the
    kappa=-2 Markov surface the reducible/boundary cases are handled by the
    box-count illustration; exact test on the generators' triple)."""
    vals = [sp.nsimplify(t, rational=False) for t in triple]
    out = []
    for t in vals:
        tv = complex(sp.N(t, 30))
        out.append(abs(tv.imag) < 1e-25 and -2 - 1e-25 <= tv.real <= 2 + 1e-25)
    return all(out)

RESULTS = {}
for m in (1, 2, 3):
    sols = geometric_points(m)
    print(f"[V2-{m}] fixed points found: {len(sols)}", flush=True)
    rows = []
    for s in sols:
        triple = (s[x], s[y], s[z])
        if any(t == 0 for t in triple) and all(t == 0 for t in triple):
            continue  # the trivial origin
        # minimal polynomial data / field of the triple
        try:
            mp = sp.minimal_polynomial(triple[0] + 2*triple[1] + 4*triple[2], x)
            deg = sp.degree(mp)
        except Exception:
            mp, deg = None, None
        rows.append((triple, mp, deg))
    RESULTS[m] = rows
    for (triple, mp, deg) in rows:
        print(f"[V2-{m}]   triple field-degree {deg}: "
              f"({sp.nsimplify(triple[0])}, {sp.nsimplify(triple[1])}, {sp.nsimplify(triple[2])})",
              flush=True)

# ---- PIPELINE GATE (m=1): the geometric orbit's field must contain sqrt(-3)
def contains_sqrt_minus3(mp_poly):
    if mp_poly is None:
        return False
    K = sp.QQ.algebraic_field(sp.sqrt(-3))
    # crude but exact: does the minimal polynomial factor further over Q(sqrt-3)?
    f_over = sp.factor_list(mp_poly, extension=sp.sqrt(-3))
    return len(f_over[1]) > 1 or any(sp.degree(p) < sp.degree(mp_poly) for p, _ in f_over[1])

gate = any(contains_sqrt_minus3(mp) for (_, mp, _) in RESULTS[1])
print(f"[GATE m=1] geometric field contains sqrt(-3): {gate}", flush=True)
if not gate:
    print("[GATE m=1] HALT -- machinery fault per the addendum (the banked field "
          "must appear); NOT a result.", flush=True)
    raise SystemExit(1)

print("==== V2 block 1 done: geometric points + gate ====", flush=True)
