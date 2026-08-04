"""B902 (M5): the Knus-Paques difference data of the three cubics over Q(sqrt77).

Exact arithmetic in F = Q(sqrt77, sqrt-3) as 4-vectors over the basis
(1, s77, sm3, s231 = s77*sm3). Kummer elements alpha = (-27q + 3s*s231)/2
(depressed cubic y^3+py+q, disc = 77 s^2) -- these live in Q(sqrt-231).
Twist set: zeta6^a eps^b, a in {0,1,2} (mod cubes, since zeta6^3 = -1 ~ 1),
b in {-1,0,1}, eps = (9+s77)/2. Decision:
- non-cube: local witnesses at rational primes p == 1 mod 3, 77 and -3 QRs,
  p coprime to all denominators; a twist dies when some clean embedding has
  chi_3(value) != 1. Primes with any evaluation failure are skipped whole.
- cube: numeric cube-root reconstruction in F (4 coords from embeddings) +
  exact symbolic verification.
Control: delta(mu, generic) = 0 expected (same field, B888).
"""
import json, os
import sympy as sp
import mpmath as mp

mp.mp.dps = 50
HERE = os.path.dirname(os.path.abspath(__file__))
x, lam, b = sp.symbols("x lambda b")
S1 = json.load(open(os.path.join(HERE, "..", "B888_two_fields",
                                 "pencil_factors.json")))
FL = [sp.sympify(f["factor"].replace("lambda", "lam_"),
                 locals={"lam_": lam, "x": x})
      for f in S1["factor_structure"]]
F1 = [f for f, m in zip(FL, S1["factor_structure"]) if m["mult"] == 1][0]
F2 = [f for f, m in zip(FL, S1["factor_structure"]) if m["mult"] == 8][0]

def bcubic(F):
    Fp = sp.Poly(F, x, lam)
    B = sp.expand(sum(c * b ** m[0] for m, c in zip(Fp.monoms(), Fp.coeffs())
                      if m[0] + m[1] == 3))
    return sp.Poly(B, b)

rho = sp.Symbol("rho")
CUBICS = {
    "mu": sp.Poly(500716339200*rho**3 - 2075673600*rho**2 - 4769856*rho + 2197,
                  rho),
    "generic": bcubic(F2),
    "vacuum": bcubic(F1),
}

def depressed(P):
    P = P.monic()
    g = P.gens[0]
    a2 = P.all_coeffs()[1]
    Q = sp.Poly(P.as_expr().subs(g, g - a2/3), g)
    cs = Q.all_coeffs()
    assert cs[1] == 0
    return sp.Rational(cs[2]), sp.Rational(cs[3])

# ---- F as 4-vectors (1, s77, sm3, s231) over Q ----
def fmul(u, v):
    a1,b1,c1,d1 = u; a2,b2,c2,d2 = v
    return (a1*a2 + 77*b1*b2 - 3*c1*c2 - 231*d1*d2,
            a1*b2 + b1*a2 - 3*(c1*d2 + d1*c2),
            a1*c2 + c1*a2 + 77*(b1*d2 + d1*b2),
            a1*d2 + d1*a2 + b1*c2 + c1*b2)
def fconj77(u):  # s77 -> -s77
    a,b_,c,d = u; return (a, -b_, c, -d)
def fconj3(u):   # sm3 -> -sm3
    a,b_,c,d = u; return (a, b_, -c, -d)
def finv(u):
    n1 = fmul(u, fconj77(u))          # in Q(sm3): components (a,0,c,0)
    n2 = fmul(n1, fconj3(n1))         # rational: (r,0,0,0)
    r = n2[0]
    num = fmul(fconj77(u), fconj3(n1))
    return tuple(sp.Rational(t, 1)/r for t in num)
def fpow(u, k):
    if k < 0: return fpow(finv(u), -k)
    out = (sp.Integer(1), 0, 0, 0)
    for _ in range(k): out = fmul(out, u)
    return out

ALPHA = {}
for name, P in CUBICS.items():
    p_, q_ = depressed(P)
    D = -4*p_**3 - 27*q_**2
    s_ = sp.sqrt(sp.Rational(D, 77))
    assert s_.is_Rational, (name, "disc not 77*square")
    ALPHA[name] = (sp.Rational(-27*q_, 2), sp.Integer(0), sp.Integer(0),
                   sp.Rational(3*s_, 2))
    print(name, ": alpha =", ALPHA[name][0], "+", ALPHA[name][3], "* s231")

EPS = (sp.Rational(9,2), sp.Rational(1,2), sp.Integer(0), sp.Integer(0))
Z6  = (sp.Rational(1,2), sp.Integer(0), sp.Rational(1,2), sp.Integer(0))
TWISTS = {(a, bb): fmul(fpow(Z6, a), fpow(EPS, bb))
          for a in (0, 1, 2) for bb in (-1, 0, 1)}

def clean_primes(denoms, want=8):
    p = 7; out = []
    while len(out) < want:
        p = int(sp.nextprime(p))
        if p % 3 != 1: continue
        if sp.jacobi_symbol(77, p) != 1 or sp.jacobi_symbol(-3, p) != 1:
            continue
        if any(d % p == 0 for d in denoms): continue
        out.append(p)
    return out

def embed(u, p, r77, rm3):
    tot = 0
    for coef, base in zip(u, (1, r77, rm3, r77*rm3 % p)):
        c = sp.Rational(coef)
        if c.q % p == 0: raise ZeroDivisionError
        tot = (tot + (c.p % p)*pow(c.q % p, -1, p)*base) % p
    return tot

def local_scan(beta):
    denoms = set()
    for tw in TWISTS.values():
        for u in fmul(beta, tw):
            denoms.add(sp.Rational(u).q)
    primes = clean_primes(denoms)
    surviving = set(TWISTS)
    tested = 0
    for p in primes:
        r77 = int(sp.sqrt_mod(77, p)); rm3 = int(sp.sqrt_mod(-3, p))
        for sr in (r77, p - r77):
            for sm in (rm3, p - rm3):
                alive = set()
                skip = False
                vals = {}
                for key in surviving:
                    try:
                        vals[key] = embed(fmul(beta, TWISTS[key]), p, sr, sm)
                    except ZeroDivisionError:
                        skip = True; break
                if skip: continue
                tested += 1
                for key, v in vals.items():
                    if v == 0 or pow(v, (p-1)//3, p) == 1:
                        alive.add(key)
                surviving = surviving & alive
                if not surviving: return surviving, primes, tested
    return surviving, primes, tested

def cube_reconstruct(beta):
    """Try to prove beta = gamma^3 with gamma in F: numeric coords + exact cube.
    Scale beta by t^3 (t = lcm of coordinate denominators) so the target is
    near-integral; return gamma/t on success."""
    scl = sp.ilcm(*[int(sp.Rational(u).q) for u in beta])
    beta = tuple(sp.Rational(u) * scl**3 for u in beta)
    r77n = mp.sqrt(77); rm3n = mp.mpc(0, mp.sqrt(3))
    embeds = [(r77n, rm3n), (-r77n, rm3n)]
    vals = []
    for (e7, e3) in embeds:
        v = complex(beta[0]) + complex(beta[1])*complex(e7) \
            + complex(beta[2])*complex(e3) + complex(beta[3])*complex(e7*e3)
        vals.append(mp.cbrt(mp.mpc(v)))
    # solve gamma coords from the 2 complex embeddings (4 real equations)
    for k1 in range(3):
        for k2 in range(3):
            w1 = vals[0]*mp.exp(2j*mp.pi*k1/3)
            w2 = vals[1]*mp.exp(2j*mp.pi*k2/3)
            A = mp.matrix([[1, mp.sqrt(77), 0, 0],
                           [0, 0, mp.sqrt(3), mp.sqrt(77)*mp.sqrt(3)],
                           [1, -mp.sqrt(77), 0, 0],
                           [0, 0, mp.sqrt(3), -mp.sqrt(77)*mp.sqrt(3)]])
            rhs = mp.matrix([mp.re(w1), mp.im(w1), mp.re(w2), mp.im(w2)])
            try: sol = mp.lu_solve(A, rhs)
            except Exception: continue
            cand = []
            good = True
            for t in sol:
                fr = sp.nsimplify(float(t), rational=True, tolerance=1e-25)
                fr = sp.Rational(fr)
                if fr.q > 96: good = False; break
                cand.append(fr)
            if not good: continue
            g = tuple(cand)
            if fmul(fmul(g, g), g) == tuple(sp.Rational(u) for u in beta):
                return tuple(u / scl for u in g)
    return None

res = {"alphas": {k: [sp.sstr(t) for t in v] for k, v in ALPHA.items()}}
for a, bn in (("mu", "generic"), ("mu", "vacuum"), ("generic", "vacuum")):
    out = {}
    for conv, beta in (("ratio", fmul(ALPHA[a], finv(ALPHA[bn]))),
                       ("product", fmul(ALPHA[a], ALPHA[bn]))):
        surv, primes, tested = local_scan(beta)
        entry = {"surviving_twists": sorted(surv), "witness_primes": primes,
                 "clean_embedding_tests": tested}
        # exact cube proof for survivors
        proofs = {}
        for key in sorted(surv):
            g = cube_reconstruct(fmul(beta, TWISTS[key]))
            if g is not None:
                proofs[str(key)] = [sp.sstr(t) for t in g]
        entry["cube_proofs"] = proofs
        out[conv] = entry
        print(f"{a} vs {bn} [{conv}]: survivors {sorted(surv)} "
              f"({tested} clean tests), proven cubes: {list(proofs)}")
    res[f"{a}__{bn}"] = out
json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1,
          default=str)
print("saved")
