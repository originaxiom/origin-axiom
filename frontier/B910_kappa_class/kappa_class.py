"""B910 (L3): the Kummer class of the compact-pencil cubic kappa.

Stage 0  rebuild kappa EXACTLY from B854's e6 machinery (the compact pair's
         pencil g14 + s*g22 on the 18-dim core/floor quotient; nu(s) = det,
         20-point exact interpolation; nu = c*kappa^6), and verify:
         constant term -19^3 = -6859, squarefree disc kernel {7,11}.
Stage 1  verify kappa splits [1,2] over K = Q[rho]/mu (mu = B866's charge
         cubic) with an EXACT root certificate kappa(r(rho)) = 0 mod mu.
Stage 2  the B902 Lagrange-resolvent Kummer elements alpha for all four
         cubics (mu, generic, vacuum, kappa) in F = Q(sqrt77, sqrt-3),
         4-vector arithmetic over the basis (1, s77, sm3, s231).
Stage 3  local scans (8 clean primes p == 1 mod 3, 77 and -3 QRs, p coprime
         to all denominators; all four embeddings) over the twist set
         zeta6^a eps77^b for DISCOVERY + exact non-cube witnesses.
Stage 4  EXACT cube certificates for every surviving twist (scaled numeric
         reconstruction at 80 dps -> symbolic cubing); composed-certificate
         fallback; every positive claim is verified by exact cubing.
Stage 5  the multiplication table of the four classes in F*/(F*)^3.

House rules: exact arithmetic for every verdict; scans are discovery +
exact negative witnesses; positives are proved by symbolic cubing.
"""
import io, contextlib, json, os, time
import sympy as sp
import mpmath as mp

mp.mp.dps = 80
HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()
res = {}

# ------------------------------------------------------------------ stage 0
print("== stage 0: rebuild kappa from the compact pencil ==", flush=True)
# exec in an ISOLATED namespace: B854's module-level names (res, s, x, HERE,
# its own json.dump target) must not leak into this script. Its __file__ is
# pointed into THIS arc dir, so its results.json dump lands here (and is
# overwritten by our final dump), never touching the banked B854 files.
_g854 = {"__name__": "b854", "__file__": os.path.abspath(__file__)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open(os.path.join(HERE, "..", "B854_centralizer_exact",
                                   "e6_centralizer.py")).read(),
                 "b854", "exec"), _g854)
ADS = _g854["ADS"]
print(f"  b854 exec done ({time.time()-T0:.0f}s)", flush=True)

s = sp.Symbol("s")
A14 = sp.Matrix(ADS[14]); A22 = sp.Matrix(ADS[22])
A8 = sp.Matrix(ADS[8]);  A16 = sp.Matrix(ADS[16])
K18 = sp.Matrix.vstack(A8, A16).nullspace()          # the 30-dim core
FL  = sp.Matrix.vstack(A8, A14, A16, A22).nullspace() # the 12-dim floor
assert len(K18) == 30 and len(FL) == 12, (len(K18), len(FL))
Bfull = sp.Matrix.hstack(*(FL + K18))
_, piv = Bfull.rref()
comp = [c - len(FL) for c in piv if c >= len(FL)]
Q = [K18[i] for i in comp]
assert len(Q) == 18, len(Q)
BB2 = sp.Matrix.hstack(*(FL + Q))
Pi = (BB2.T * BB2).inv() * BB2.T
def q18(Am):
    R = Pi * (Am * BB2); return R[len(FL):, len(FL):]
R14 = q18(A14); R22 = q18(A22)
pts = [(sv, (R14 + sv * R22).det()) for sv in range(20)]   # 20 > deg 18
NU = sp.Poly(sp.expand(sp.interpolate(pts, s)), s)
assert NU.degree() == 18, NU.degree()
den = sp.ilcm(*[sp.Rational(c).q for c in NU.all_coeffs()])
NUi = sp.Poly(sp.expand(NU.as_expr() * den), s)
g = sp.igcd(*[int(c) for c in NUi.all_coeffs()])
NUi = sp.Poly([sp.Integer(int(c) // g) for c in NUi.all_coeffs()], s)
cont, facs = sp.factor_list(NUi)
assert cont == 1 and len(facs) == 1 and facs[0][0].degree() == 3 \
    and facs[0][1] == 6, (cont, [(f.degree(), m) for f, m in facs])
KAPPA = sp.Poly(facs[0][0], s)
c_nu = sp.Rational(g, den)
assert sp.expand(NU.as_expr() - c_nu * KAPPA.as_expr()**6) == 0
kc = KAPPA.all_coeffs()
print(f"  nu = c * kappa^6 exact, c = {c_nu}", flush=True)
print(f"  kappa = {KAPPA.as_expr()}", flush=True)
assert kc[-1] == -6859 == -19**3, kc[-1]
Dk = sp.discriminant(KAPPA.as_expr(), s)
kern = sorted(p for p, e in sp.factorint(Dk).items() if e % 2)
assert kern == [7, 11], kern
assert KAPPA.is_irreducible
print(f"  constant = -19^3, disc = {sp.factorint(Dk)}, kernel {{7,11}} OK "
      f"({time.time()-T0:.0f}s)", flush=True)
res["kappa"] = {"coeffs": [int(c) for c in kc],
                "nu_scalar_c": str(c_nu),
                "disc_factorization": {str(p): int(e)
                                       for p, e in sp.factorint(Dk).items()},
                "disc_kernel": [7, 11], "irreducible": True}

# ------------------------------------------------------------------ stage 1
print("== stage 1: kappa splits [1,2] over K = Q[rho]/mu ==", flush=True)
rho = sp.Symbol("rho")
MU = sp.Poly(500716339200*rho**3 - 2075673600*rho**2 - 4769856*rho + 2197, rho)
assert MU.is_irreducible
th = sp.CRootOf(MU.as_expr(), 0)
fl_K = sp.factor_list(KAPPA.as_expr(), s, extension=th)
degs = sorted(sp.Poly(f, s).degree() for f, m in fl_K[1] for _ in range(m))
assert degs == [1, 2], degs
lin = [sp.Poly(f, s) for f, m in fl_K[1] if sp.Poly(f, s).degree() == 1][0]
r_expr = sp.simplify(-lin.all_coeffs()[1] / lin.all_coeffs()[0])
# rewrite the root as a polynomial in rho and verify by exact reduction
r_poly = sp.Poly(r_expr.subs(th, rho).rewrite(sp.Pow), rho)
rem = sp.rem(KAPPA.as_expr().subs(s, r_poly.as_expr()), MU.as_expr(), rho)
assert sp.expand(rem) == 0, "root certificate failed"
print(f"  factor degrees over K: [1, 2]; root s*(rho) = {r_poly.as_expr()}",
      flush=True)
print(f"  EXACT certificate: kappa(s*(rho)) = 0 mod mu(rho) "
      f"({time.time()-T0:.0f}s)", flush=True)
res["split_over_K"] = {"factor_degrees": [1, 2],
                       "root_in_rho": sp.sstr(r_poly.as_expr()),
                       "certificate": "rem(kappa(s*(rho)), mu(rho)) == 0"}

# ------------------------------------------------------------------ stage 2
print("== stage 2: the four Kummer elements ==", flush=True)
x, lam, b = sp.symbols("x lambda b")
S1 = json.load(open(os.path.join(HERE, "..", "B888_two_fields",
                                 "pencil_factors.json")))
FLp = [sp.sympify(f["factor"].replace("lambda", "lam_"),
                  locals={"lam_": lam, "x": x})
       for f in S1["factor_structure"]]
F1 = [f for f, m in zip(FLp, S1["factor_structure"]) if m["mult"] == 1][0]
F2 = [f for f, m in zip(FLp, S1["factor_structure"]) if m["mult"] == 8][0]

def bcubic(F):
    Fp = sp.Poly(F, x, lam)
    B = sp.expand(sum(c * b ** m[0] for m, c in zip(Fp.monoms(), Fp.coeffs())
                      if m[0] + m[1] == 3))
    return sp.Poly(B, b)

CUBICS = {"mu": MU, "generic": bcubic(F2), "vacuum": bcubic(F1),
          "kappa": KAPPA}

def depressed(P):
    P = P.monic()
    gv = P.gens[0]
    a2 = P.all_coeffs()[1]
    Qd = sp.Poly(P.as_expr().subs(gv, gv - a2/3), gv)
    cs = Qd.all_coeffs()
    assert cs[1] == 0
    return sp.Rational(cs[2]), sp.Rational(cs[3])

# ---- F = Q(sqrt77, sqrt-3) as 4-vectors over (1, s77, sm3, s231) ----
def fmul(u, v):
    a1,b1,c1,d1 = u; a2,b2,c2,d2 = v
    return (a1*a2 + 77*b1*b2 - 3*c1*c2 - 231*d1*d2,
            a1*b2 + b1*a2 - 3*(c1*d2 + d1*c2),
            a1*c2 + c1*a2 + 77*(b1*d2 + d1*b2),
            a1*d2 + d1*a2 + b1*c2 + c1*b2)
def fconj77(u):
    a,b_,c,d = u; return (a, -b_, c, -d)
def fconj3(u):
    a,b_,c,d = u; return (a, b_, -c, -d)
def finv(u):
    n1 = fmul(u, fconj77(u))
    n2 = fmul(n1, fconj3(n1))
    r = n2[0]
    num = fmul(fconj77(u), fconj3(n1))
    return tuple(sp.Rational(t, 1)/r for t in num)
def fpow(u, k):
    if k < 0: return fpow(finv(u), -k)
    out = (sp.Integer(1), 0, 0, 0)
    for _ in range(k): out = fmul(out, u)
    return out
def fcube(u):
    return fmul(fmul(u, u), u)

ALPHA = {}
for name, P in CUBICS.items():
    p_, q_ = depressed(P)
    D = -4*p_**3 - 27*q_**2
    s_ = sp.sqrt(sp.Rational(D, 77))
    assert s_.is_Rational, (name, "disc not 77*square")
    ALPHA[name] = (sp.Rational(-27*q_, 2), sp.Integer(0), sp.Integer(0),
                   sp.Rational(3*s_, 2))
    print(f"  alpha_{name} = {ALPHA[name][0]} + {ALPHA[name][3]} * s231",
          flush=True)
# the numerator law: alpha_mu carries 13^6, alpha_kappa carries 19^6
assert abs(sp.Rational(ALPHA["mu"][0]).p) == 13**6
assert abs(sp.Rational(ALPHA["kappa"][0]).p) == 19**6
assert abs(sp.Rational(ALPHA["kappa"][3]).p) == 19**6
res["alphas"] = {k: [sp.sstr(t) for t in v] for k, v in ALPHA.items()}

EPS = (sp.Rational(9,2), sp.Rational(1,2), sp.Integer(0), sp.Integer(0))
Z6  = (sp.Rational(1,2), sp.Integer(0), sp.Rational(1,2), sp.Integer(0))
TWISTS = {(a, bb): fmul(fpow(Z6, a), fpow(EPS, bb))
          for a in (0, 1, 2) for bb in (-1, 0, 1)}

# ------------------------------------------------------------------ stage 3
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
    """Discovery scan + exact non-cube witnesses.
    A witness (p, r77, rm3) with chi_3(embed) != 1 PROVES beta*twist is not
    a cube in F (the embedding is a ring hom on p-integral elements; cubes
    land on cubes)."""
    denoms = set()
    for tw in TWISTS.values():
        for u in fmul(beta, tw):
            denoms.add(sp.Rational(u).q)
    primes = clean_primes(denoms)
    surviving = set(TWISTS)
    tested = 0
    witness = {}
    for p in primes:
        r77 = int(sp.sqrt_mod(77, p)); rm3 = int(sp.sqrt_mod(-3, p))
        for sr in (r77, p - r77):
            for sm in (rm3, p - rm3):
                skip = False
                vals = {}
                for key in TWISTS:
                    try:
                        vals[key] = embed(fmul(beta, TWISTS[key]), p, sr, sm)
                    except ZeroDivisionError:
                        skip = True; break
                if skip: continue
                tested += 1
                alive = set()
                for key, v in vals.items():
                    if v == 0 or pow(v, (p-1)//3, p) == 1:
                        alive.add(key)
                    elif key not in witness:
                        witness[key] = {"p": p, "r77": sr, "rm3": sm,
                                        "val": int(v)}
                surviving = surviving & alive
    return surviving, primes, tested, witness

# ------------------------------------------------------------------ stage 4
def cube_reconstruct(beta, qmax=10**9):
    """Prove beta = gamma^3, gamma in F: scale by t^3 (t = lcm of coordinate
    denominators), 80-dps numeric cube roots at two embeddings, rational
    reconstruction via limit_denominator, then EXACT symbolic cubing.
    (B902's version rationalized through float64 and capped denominators at
    96 -- too coarse for the 13*19^3 denominators appearing here.)"""
    scl = sp.ilcm(*[int(sp.Rational(u).q) for u in beta])
    beta_s = tuple(sp.Rational(u) * scl**3 for u in beta)
    r77n = mp.sqrt(77); rm3n = mp.mpc(0, mp.sqrt(3))
    vals = []
    for (e7, e3) in ((r77n, rm3n), (-r77n, rm3n)):
        v = mp.mpc(0)
        for coef, base in zip(beta_s, (mp.mpf(1), e7, e3, e7*e3)):
            cr = sp.Rational(coef)
            v += mp.mpf(cr.p) / mp.mpf(cr.q) * base
        vals.append(mp.cbrt(v))
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
            gam = tuple(sp.Rational(sp.Float(t, 60)).limit_denominator(qmax)
                        for t in sol)
            if fcube(gam) == beta_s:
                return tuple(u / scl for u in gam)
    return None

print("== stages 3+4: scans + exact certificates ==", flush=True)
NAMES = ["mu", "generic", "vacuum", "kappa"]
res["pairs"] = {}
CERT = {}
for i in range(4):
    for j in range(i+1, 4):
        a, bn = NAMES[i], NAMES[j]
        out = {}
        for conv, beta in (("ratio", fmul(ALPHA[a], finv(ALPHA[bn]))),
                           ("product", fmul(ALPHA[a], ALPHA[bn]))):
            surv, primes, tested, wit = local_scan(beta)
            entry = {"surviving_twists": sorted(surv),
                     "witness_primes": primes,
                     "clean_embedding_tests": tested,
                     "noncube_witnesses": {str(k): w for k, w in wit.items()}}
            proofs = {}
            for key in sorted(surv):
                gam = cube_reconstruct(fmul(beta, TWISTS[key]))
                if gam is not None:
                    assert fcube(gam) == tuple(sp.Rational(u) for u in beta) \
                        if key == (0, 0) else True
                    proofs[str(key)] = [sp.sstr(t) for t in gam]
                    if key == (0, 0):
                        CERT[(a, bn, conv)] = gam
            entry["cube_proofs"] = proofs
            out[conv] = entry
            print(f"  {a} vs {bn} [{conv}]: survivors {sorted(surv)} "
                  f"({tested} clean tests), proven cubes: {list(proofs)}",
                  flush=True)
        res["pairs"][f"{a}__{bn}"] = out

# singles: is any alpha itself a cube (up to twist)?
res["singles"] = {}
for name in NAMES:
    surv, primes, tested, wit = local_scan(ALPHA[name])
    res["singles"][name] = {
        "surviving_twists": sorted(surv), "witness_primes": primes,
        "clean_embedding_tests": tested,
        "noncube_witnesses": {str(k): w for k, w in wit.items()}}
    print(f"  alpha_{name} itself: survivors {sorted(surv)} "
          f"({tested} clean tests)", flush=True)
    assert not surv, f"alpha_{name} unexpectedly trivial up to twist"

# composed-certificate fallback for any (0,0) survivor without a direct one
def need(a, bn, conv):
    return ([0, 0] in [list(t) for t in
            [tuple(x) for x in
             res["pairs"][f"{a}__{bn}"][conv]["surviving_twists"]]]) \
        and str((0, 0)) not in res["pairs"][f"{a}__{bn}"][conv]["cube_proofs"]

for (a, bn, conv) in [("mu", "generic", "ratio"), ("generic", "kappa", "ratio")]:
    if not need(a, bn, conv):
        continue
    # compose from certified neighbors: gamma_ab = product of known gammas
    if (a, bn, conv) == ("mu", "generic", "ratio"):
        g1 = CERT[("mu", "vacuum", "product")]
        g2 = CERT[("generic", "vacuum", "product")]
        gam = fmul(g1, finv(g2))
        beta = fmul(ALPHA["mu"], finv(ALPHA["generic"]))
    else:
        g2 = CERT[("generic", "vacuum", "product")]
        g4 = CERT[("vacuum", "kappa", "product")]
        gam = fmul(g2, finv(g4))          # (gen*vac)/(vac*kap) = gen/kap
        beta = fmul(ALPHA["generic"], finv(ALPHA["kappa"]))
    assert fcube(gam) == tuple(sp.Rational(u) for u in beta), (a, bn, conv)
    res["pairs"][f"{a}__{bn}"][conv]["cube_proofs"]["(0, 0)"] = \
        [sp.sstr(t) for t in gam]
    res["pairs"][f"{a}__{bn}"][conv]["cube_proofs_note"] = \
        "composed certificate, verified by exact symbolic cubing"
    CERT[(a, bn, conv)] = gam
    print(f"  composed certificate for {a}/{bn} [{conv}] verified exactly",
          flush=True)

# ------------------------------------------------------------------ stage 5
print("== stage 5: the class table in F*/(F*)^3 ==", flush=True)
# assignments relative to C := [alpha_mu]
# exact facts: alpha_mu/alpha_kappa cube, alpha_mu/alpha_generic cube,
#              alpha_mu*alpha_vac cube, each alpha non-cube (witnesses)
CLASS = {"mu": 1, "generic": 1, "kappa": 1, "vacuum": 2}   # exponent of C
assert ("mu", "kappa", "ratio") in CERT
assert ("mu", "vacuum", "product") in CERT
table = {}
for a in NAMES:
    for bn in NAMES:
        e = (CLASS[a] + CLASS[bn]) % 3
        table[f"{a}*{bn}"] = {0: "1", 1: "C", 2: "C^2"}[e]
res["classes"] = {"generator": "C = [alpha_mu]",
                  "assignments": {k: {0: "1", 1: "C", 2: "C^2"}[v]
                                  for k, v in CLASS.items()},
                  "multiplication_table": table,
                  "C_nontrivial": "each alpha killed at all 9 twists "
                                  "(exact local witnesses, res['singles'])"}
# consistency: every scan verdict must match the table
for i in range(4):
    for j in range(i+1, 4):
        a, bn = NAMES[i], NAMES[j]
        e_prod = (CLASS[a] + CLASS[bn]) % 3
        e_rat = (CLASS[a] - CLASS[bn]) % 3
        for conv, e in (("product", e_prod), ("ratio", e_rat)):
            surv = res["pairs"][f"{a}__{bn}"][conv]["surviving_twists"]
            if e == 0:
                assert [0, 0] in [list(t) for t in surv], (a, bn, conv)
                assert "(0, 0)" in \
                    res["pairs"][f"{a}__{bn}"][conv]["cube_proofs"], \
                    (a, bn, conv, "cube claimed but no exact certificate")
            else:
                assert surv == [], (a, bn, conv,
                                    "non-cube claimed but twist survived")
print("  table consistent with every scan + certificate", flush=True)
print(json.dumps(table, indent=1), flush=True)

json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1,
          default=str)
print(f"saved results.json ({time.time()-T0:.0f}s)", flush=True)
