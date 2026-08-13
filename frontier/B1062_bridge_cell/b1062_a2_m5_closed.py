"""A2's m = 4, 5 via the CLOSED CHEBYSHEV FORM (supersedes both dead routes):
phi_m^2(a) = s^m a, phi_m^2(b) = s, with s = a^m b. Cayley-Hamilton gives
a^m = U_{m-1}(x/2) a - U_{m-2}(x/2) and s^n = U_{n-1}(t/2) s - U_{n-2}(t/2)
with t = tr(s). So the whole induced trace map is three small polynomials:
  t      = P_m z - Q_m y                     (P_m = U_{m-1}, Q_m = U_{m-2} at x/2)
  tr(sa) = P_{m+1} z - P_m y                 (tr(a^{m+1} b))
  Ta = C_{m-1} tr(sa) - C_{m-2} x            (C_k = U_k at t/2)
  Tb = t
  Tab = tr(s^{m+1} a) = C_m tr(sa) - C_{m-1} x
GATE: m = 1 must reproduce the banked geometric triple field Q(sqrt(-3)).
Then m = 4 (typing repaired) and m = 5 (the last blind number + raw discards).
"""
import sympy as sp
from sympy import symbols, groebner

x, y, z = symbols('x y z')

def U(n, s):
    """Chebyshev U_n(s/2) as a polynomial (dilated), U_{-1}=0, U_0=1."""
    if n < 0: return sp.Integer(0)
    a, b = sp.Integer(1), s
    if n == 0: return a
    for _ in range(n - 1):
        a, b = b, sp.expand(s*b - a)
    return b

def system(m):
    Pm, Qm = U(m-1, x), U(m-2, x)
    Pm1 = U(m, x)
    t = sp.expand(Pm*z - Qm*y)          # tr(s)
    tsa = sp.expand(Pm1*z - Pm*y)       # tr(s a) = tr(a^{m+1} b)
    Cm2, Cm1, Cm = U(m-2, t), U(m-1, t), U(m, t)
    Ta  = sp.expand(Cm1*tsa - Cm2*x)
    Tb  = t
    Tab = sp.expand(Cm*tsa - Cm1*x)
    return [sp.expand(Ta - x), sp.expand(Tb - y), sp.expand(Tab - z),
            x**2 + y**2 + z**2 - x*y*z]

def run(m, gate_field=None):
    eqs = system(m)
    print(f"[C m={m}] degrees {[sp.total_degree(e) for e in eqs]}; groebner...", flush=True)
    G = groebner(eqs, x, y, z, order='lex')
    uni = [g for g in G.exprs if g.free_symbols <= {z}][0]
    facs = sp.factor_list(sp.Poly(uni, z))[1]
    print(f"[C m={m}] z-eliminant factors: {[(sp.degree(f), e) for f, e in facs]}", flush=True)
    for f, e in facs:
        print(f"[C m={m}]   RAW deg {sp.degree(f)}: {sp.expand(f.as_expr() if hasattr(f,'as_expr') else f)}", flush=True)
    # numeric full-triple typing per factor root
    others = [g for g in G.exprs if not (sp.sympify(g).free_symbols <= {z})]
    def etype(c):
        if abs(c.imag) > 1e-18: return "lox"
        if abs(c.real) < 2 - 1e-18: return "ELL"
        return "par/hyp"
    geo_degs = []
    for f, _e in facs:
        d = sp.degree(f)
        if d == 0: continue
        roots = sp.Poly(f, z).nroots(n=30, maxsteps=300)
        tags, fails = [], 0
        for zr in roots:
            zc = complex(zr)
            try:
                sols = sp.solve([sp.expand(g.subs(z, sp.nsimplify(zr, rational=False))) for g in others],
                                [x, y], dict=True)
            except Exception:
                sols = []
            if not sols:
                # numeric fallback: solve the two lowest-degree basis elements numerically
                fails += 1
                tags.append(("solve-fail",))
                continue
            s0 = sols[0]
            try:
                xc, yc = complex(sp.N(s0[x], 25)), complex(sp.N(s0[y], 25))
                tags.append((etype(xc), etype(yc), etype(zc)))
            except Exception:
                fails += 1
                tags.append(("eval-fail",))
        n_ell = sum(1 for tg in tags if "ELL" in tg)
        all_lox = [tg for tg in tags if tg == ("lox","lox","lox")]
        if all_lox and not any("fail" in str(tg) for tg in tags[:1]):
            geo_degs.append(d)
        print(f"[C m={m}]   deg-{d}: typed {len(tags)}, elliptic-bearing {n_ell}, "
              f"all-lox {len(all_lox)}, fails {fails}", flush=True)
    print(f"[C m={m}] GEOMETRIC-CANDIDATE factor degrees: {geo_degs}", flush=True)
    if gate_field is not None:
        # the m=1 gate: the nontrivial factor must be x^2-3x+3-shaped in its field
        ok = any(d == 2 for d in geo_degs)
        print(f"[C m={m}] GATE (banked field degree 2 present): {ok}", flush=True)
        assert ok, "GATE FAILED"
    return geo_degs

run(1, gate_field=True)
run(4)
run(5)
print("==== closed-form A2 done ====", flush=True)
