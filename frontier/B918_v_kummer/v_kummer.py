"""B918 (register item V-L3): the hierarchy element V into the Kummer machinery.

Stage 0  the numeric anchors: the three v_g^2 values at 95 digits, regenerated
         on THIS bench by a dps-100 rerun of the relay pipeline (the solo
         seat's norms.py atom construction + the belt100 coupling loop, with
         the section-LXIV dps throttle removed at exec time; belt driver and
         outputs in the session scratchpad per relay discipline; residuals
         953*lambda-2304 = 2.8e-85, 953*CCC-13824 = 3.5e-85).  From them the
         symmetric functions e1, e2, e3 are pinned by 953^4-rounding
         (proximity < 1e-70 asserted) and anchored on the EXACT banked P9 law
         e3 = 27*lambda^4 = 2^32 3^11 / 953^4 (pure integers).
Stage 1  the hierarchy cubic pinned EXACTLY:
         HIER = 953^4 x^3 - 2^8 3^9 13*421493 x^2 + 2^21 3^8 17*1129 x
                - 2^32 3^11,
         certified: primitive, irreducible over Q, disc kernel {7,11} (the
         sqrt77 family), [1,2] split over K = Q[rho]/mu with the EXACT root
         V(rho) (polynomial-remainder certificate), roots = the anchors to
         ~88 digits, the branch identity rho_g -> v_g^2 (identity map), and
         the solo seat's numeric K-linear certificate (HG2) EXACTIFIED:
         V*(19474 - 1154453 rho - 18197524 rho^2) + (-152295 - 15081984 rho
         - 50844672 rho^2) == 0 mod mu.
Stage 2  the B910 Lagrange-resolvent Kummer element alpha_V in
         F = Q(sqrt77, sqrt-3); local scans (8 clean primes, all four
         embeddings, twist set zeta6^a eps77^b) for DISCOVERY on alpha_V vs
         each banked alpha; EXACT symbolic cube certificates for every
         survivor, chi_3 witnesses for every negative; the FIVE-element
         multiplication table in F*/(F*)^3, asserted consistent with every
         scan and with B910's banked four-element table.
Stage 3  the place structure at the value primes p in {953, 1129, 421493}
         (each [1,2] in K, p coprime to disc of the monic model): the
         degree-one place exhibited (residue of rho), Hensel-lifted
         valuations of V at BOTH places, f-weighted norm consistency,
         residues and the unit-corrected trace/e2 congruences; the
         integrality lemma (from e_i's exact 953^4-only denominators, via
         the characteristic polynomial) pinning V's denominator support;
         the H-B917-SPLIT two-outcome verdict.

House rules: exact arithmetic for every verdict; the numeric belt is an
anchor + reproduction check only; scans are discovery + exact negative
witnesses; every positive is proved by symbolic cubing.
"""
import json, os, time
import sympy as sp
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()
res = {}
x, lam, b, rho, y = sp.symbols("x lambda b rho y")

# ------------------------------------------------------------------ stage 0
print("== stage 0: numeric anchors -> exact symmetric functions ==", flush=True)
# The three v_g^2 at 95 digits, regenerated on this bench (dps-100 relay
# belt rerun, this session; see DRAFT_FINDINGS "The numeric anchor").
V2_STR = [
 "5.6949646542627022800114395018643909803511537241825032972661994700327374859995160260560968489452",
 "8.3270641823804018236805452226598240111759437156635398384260921794314458799945227033081544639939",
 "19.450873775663868128388849662750898517072742957098824776192855797291942760933196636972607646129",
]
mp.mp.dps = 110
v2 = [mp.mpf(s) for s in V2_STR]
D953 = 953**4
ee = {"e1": v2[0]+v2[1]+v2[2],
      "e2": v2[0]*v2[1]+v2[0]*v2[2]+v2[1]*v2[2],
      "e3": v2[0]*v2[1]*v2[2]}
NN = {}
for k, val in ee.items():
    t = val * D953
    n = int(mp.nint(t))
    dist = abs(t - n)
    assert dist < mp.mpf("1e-70"), (k, dist)
    NN[k] = n
    print(f"  {k}*953^4 = {n}  (distance to integer {mp.nstr(dist, 3)})",
          flush=True)
N1, N2, N3 = NN["e1"], NN["e2"], NN["e3"]
# the EXACT anchor: P9's product law (banked, pure integers)
assert N3 == 27 * 2304**4 == 2**32 * 3**11
assert sp.Rational(N3, D953) == 27 * sp.Rational(2304, 953)**4
# the section-LXVI numerator content
assert sp.factorint(N1) == {2: 8, 3: 9, 13: 1, 421493: 1}
assert sp.factorint(N2) == {2: 21, 3: 8, 17: 1, 1129: 1}
assert all(sp.isprime(p) for p in (953, 1129, 421493))
res["anchors"] = {"v_sq_95d": V2_STR,
                  "provenance": "dps-100 relay-belt rerun on this bench "
                                "(session scratchpad); residuals "
                                "953*lambda-2304 = 2.8e-85, "
                                "953*CCC-13824 = 3.5e-85",
                  "e_times_953^4": {k: int(v) for k, v in NN.items()},
                  "P9_exact": "e3 = 27*(2304/953)^4, pure integers"}
print(f"  P9 anchor exact; numerator content 13*421493 | 17*1129 OK "
      f"({time.time()-T0:.0f}s)", flush=True)

# ------------------------------------------------------------------ stage 1
print("== stage 1: the hierarchy cubic, pinned + certified ==", flush=True)
HIER = sp.Poly(D953*x**3 - N1*x**2 + N2*x - N3, x)
assert sp.igcd(*[int(c) for c in HIER.all_coeffs()]) == 1     # primitive
assert HIER.is_irreducible
Dh = sp.discriminant(HIER.as_expr(), x)
fd = sp.factorint(Dh)
kern = sorted(p for p, e in fd.items() if e % 2)
assert kern == [7, 11], kern                                   # sqrt77 family
assert fd == {2: 64, 3: 24, 5: 6, 7: 3, 11: 1, 73: 2, 214189: 2}
print(f"  HIER = {HIER.as_expr()}", flush=True)
print(f"  irreducible; disc = {fd}; kernel {{7,11}} OK", flush=True)

# roots reproduce the anchors
rts = sorted(mp.polyroots([int(c) for c in HIER.all_coeffs()],
                          maxsteps=200, extraprec=80))
root_err = max(abs(r - v) for r, v in zip(rts, v2))
assert root_err < mp.mpf("1e-85"), root_err   # the 95-digit anchor floor
print(f"  three real roots = the belt anchors, max err "
      f"{mp.nstr(root_err, 3)}", flush=True)

# [1,2] split over K = Q[rho]/mu + the exact root V(rho)
MU = sp.Poly(500716339200*rho**3 - 2075673600*rho**2 - 4769856*rho + 2197,
             rho)
assert MU.is_irreducible
th = sp.CRootOf(MU.as_expr(), 0)
fl_K = sp.factor_list(HIER.as_expr(), x, extension=th)
degs = sorted(sp.Poly(f, x).degree() for f, m in fl_K[1] for _ in range(m))
assert degs == [1, 2], degs
lin = [sp.Poly(f, x) for f, m in fl_K[1] if sp.Poly(f, x).degree() == 1][0]
r_expr = sp.simplify(-lin.all_coeffs()[1] / lin.all_coeffs()[0])
V_poly = sp.Poly(r_expr.subs(th, rho).rewrite(sp.Pow), rho)
rem = sp.rem(HIER.as_expr().subs(x, V_poly.as_expr()), MU.as_expr(), rho)
assert sp.expand(rem) == 0, "root certificate failed"
vc = [sp.Rational(c) for c in V_poly.all_coeffs()]   # [rho^2, rho, 1]
assert [sp.factorint(c.q) for c in vc] == \
    [{13: 4, 953: 4}, {13: 3, 953: 4}, {13: 2, 953: 4}]
print(f"  degrees over K: [1,2]; V(rho) = {V_poly.as_expr()}", flush=True)
print(f"  EXACT certificate: HIER(V(rho)) = 0 mod mu(rho)", flush=True)

# branch identity rho_g -> v_g^2 (identity map, ascending real roots)
mu_rts = sp.real_roots(MU)
branch_err = []
for i, mr in enumerate(mu_rts):
    rv = mp.mpf(str(sp.N(mr, 105)))
    Vv = (mp.mpf(vc[2].p)/vc[2].q + mp.mpf(vc[1].p)/vc[1].q*rv
          + mp.mpf(vc[0].p)/vc[0].q*rv*rv)
    branch_err.append(abs(Vv - v2[i]))
assert max(branch_err) < mp.mpf("1e-85"), branch_err
print(f"  branch identity V(rho_g) = v_g^2, identity map, max err "
      f"{mp.nstr(max(branch_err), 3)}", flush=True)

# the solo seat's K-linear certificate (HG2), EXACTIFIED
HG2_A = 19474 - 1154453*rho - 18197524*rho**2
HG2_B = -152295 - 15081984*rho - 50844672*rho**2
cert = sp.rem(sp.expand((V_poly.as_expr()*HG2_A + HG2_B) * vc[0].q),
              MU.as_expr(), rho)
assert sp.expand(cert) == 0
print(f"  HG2 exactified: V*(19474-1154453 rho-18197524 rho^2) "
      f"+ (-152295-15081984 rho-50844672 rho^2) == 0 mod mu "
      f"({time.time()-T0:.0f}s)", flush=True)
res["hier_cubic"] = {
    "coeffs": [int(c) for c in HIER.all_coeffs()],
    "coeff_factorizations": {"lead": "953^4", "x^2": "-2^8 3^9 13 421493",
                             "x^1": "2^21 3^8 17 1129",
                             "const": "-2^32 3^11 = -27*2304^4"},
    "irreducible": True,
    "disc_factorization": {str(p): int(e) for p, e in fd.items()},
    "disc_kernel": [7, 11],
    "split_over_K": [1, 2],
    "V_in_rho": sp.sstr(V_poly.as_expr()),
    "root_certificate": "rem(HIER(V(rho)), mu(rho)) == 0",
    "root_reproduction_err": mp.nstr(root_err, 3),
    "branch_identity": "V(rho_g) = v_g^2, identity map (ascending), max err "
                       + mp.nstr(max(branch_err), 3),
    "HG2_certificate_exactified": "V*A + B == 0 mod mu, A = 19474-1154453rho"
                                  "-18197524rho^2, B = -152295-15081984rho"
                                  "-50844672rho^2"}

# ------------------------------------------------------------------ stage 2
print("== stage 2: alpha_V and the five Kummer classes ==", flush=True)
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

B910 = json.load(open(os.path.join(HERE, "..", "B910_kappa_class",
                                   "results.json")))
KAPPA = sp.Poly([sp.Integer(c) for c in B910["kappa"]["coeffs"]], x)
CUBICS = {"mu": MU, "generic": bcubic(F2), "vacuum": bcubic(F1),
          "kappa": KAPPA, "V": HIER}

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
    Dd = -4*p_**3 - 27*q_**2
    s_ = sp.sqrt(sp.Rational(Dd, 77))
    assert s_.is_Rational, (name, "disc not 77*square")
    ALPHA[name] = (sp.Rational(-27*q_, 2), sp.Integer(0), sp.Integer(0),
                   sp.Rational(3*s_, 2))
# the four banked alphas regenerate B910 EXACTLY
for k in ("mu", "generic", "vacuum", "kappa"):
    banked = tuple(sp.sympify(t) for t in B910["alphas"][k])
    assert banked == ALPHA[k], k
print("  four banked alphas regenerated = B910 exactly", flush=True)
aV = ALPHA["V"]
print(f"  alpha_V = {aV[0]} + {aV[3]} * s231", flush=True)
assert sp.factorint(sp.Rational(aV[0]).q) == {953: 12}
assert sp.factorint(sp.Rational(aV[3]).q) == {953: 8}
res["alpha_V"] = {"vector": [sp.sstr(t) for t in aV],
                  "denominators": "953^12 (rational part), 953^8 (s231 part)",
                  "s231_numerator_content": str(sp.factorint(
                      sp.Rational(aV[3]).p))}

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
    """Discovery + exact non-cube witnesses (chi_3 at split primes:
    the embedding is a ring hom on p-integral elements; cubes land on
    cubes, so chi_3(embed) != 1 PROVES beta*twist is not a cube in F)."""
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

def cube_reconstruct(beta, qmax=10**14):
    """Prove beta = gamma^3: scale by t^3, 110-dps numeric cube roots at two
    embeddings, rational reconstruction, then EXACT symbolic cubing (the
    B910 recipe, denominator cap raised to 1e14 for the 953^4 content)."""
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
            gam = tuple(sp.Rational(sp.Float(t, 90)).limit_denominator(qmax)
                        for t in sol)
            if fcube(gam) == beta_s:
                return tuple(u / scl for u in gam)
    return None

print("  -- scans + certificates: V vs the four --", flush=True)
res["pairs"] = {}
CERT = {}
for other in ("mu", "generic", "vacuum", "kappa"):
    out = {}
    for conv, beta in (("ratio", fmul(aV, finv(ALPHA[other]))),
                       ("product", fmul(aV, ALPHA[other]))):
        surv, primes, tested, wit = local_scan(beta)
        entry = {"surviving_twists": sorted(surv),
                 "witness_primes": primes,
                 "clean_embedding_tests": tested,
                 "noncube_witnesses": {str(k): w for k, w in wit.items()}}
        proofs = {}
        for key in sorted(surv):
            gam = cube_reconstruct(fmul(beta, TWISTS[key]))
            assert gam is not None, ("survivor without certificate",
                                     other, conv, key)
            assert fcube(gam) == tuple(sp.Rational(u)
                                       for u in fmul(beta, TWISTS[key]))
            proofs[str(key)] = [sp.sstr(t) for t in gam]
            if key == (0, 0):
                CERT[("V", other, conv)] = gam
        # every dead twist must carry a witness; every survivor a proof
        for key in TWISTS:
            if key not in surv:
                assert str(key) in entry["noncube_witnesses"], (other, conv,
                                                                key)
        entry["cube_proofs"] = proofs
        out[conv] = entry
        print(f"  V vs {other} [{conv}]: survivors {sorted(surv)} "
              f"({tested} clean tests), proven cubes: {list(proofs)}",
              flush=True)
    res["pairs"][f"V__{other}"] = out

# singles: no alpha is trivial (all five, regenerating B910's four)
res["singles"] = {}
for name in ("mu", "generic", "vacuum", "kappa", "V"):
    surv, primes, tested, wit = local_scan(ALPHA[name])
    assert not surv, f"alpha_{name} unexpectedly trivial up to twist"
    res["singles"][name] = {
        "surviving_twists": [], "witness_primes": primes,
        "clean_embedding_tests": tested,
        "noncube_witnesses": {str(k): w for k, w in wit.items()}}
    print(f"  alpha_{name} itself: non-cube at all 9 twists "
          f"({tested} clean tests)", flush=True)

# the five-element table in F*/(F*)^3, C := [alpha_mu]
CLASS = {"mu": 1, "generic": 1, "kappa": 1, "V": 1, "vacuum": 2}
NAMES5 = ["mu", "generic", "vacuum", "kappa", "V"]
# consistency of the V-row with every scan verdict
for other in ("mu", "generic", "vacuum", "kappa"):
    e_rat = (CLASS["V"] - CLASS[other]) % 3
    e_prod = (CLASS["V"] + CLASS[other]) % 3
    for conv, e in (("ratio", e_rat), ("product", e_prod)):
        surv = res["pairs"][f"V__{other}"][conv]["surviving_twists"]
        if e == 0:
            assert [0, 0] in [list(t) for t in surv], (other, conv)
            assert "(0, 0)" in res["pairs"][f"V__{other}"][conv]["cube_proofs"]
        else:
            assert surv == [], (other, conv)
table = {}
for a in NAMES5:
    for bn in NAMES5:
        e = (CLASS[a] + CLASS[bn]) % 3
        table[f"{a}*{bn}"] = {0: "1", 1: "C", 2: "C^2"}[e]
# the four-element sub-table must equal B910's banked table
for k, v in B910["classes"]["multiplication_table"].items():
    assert table[k] == v, (k, table[k], v)
res["classes"] = {"generator": "C = [alpha_mu]",
                  "assignments": {k: {0: "1", 1: "C", 2: "C^2"}[v]
                                  for k, v in CLASS.items()},
                  "multiplication_table": table,
                  "consistency": "V-row consistent with all 8 scans + "
                                 "4 certificates; sub-table = B910 banked"}
print("  five-element table consistent with every scan + certificate; "
      "sub-table = B910", flush=True)
# structural note: gamma(V/mu), gamma(V/generic) lie in Q(sqrt-231)
# (untwisted); gamma(V/kappa), gamma(V*vacuum) are 2*zeta6*(Q(sqrt-231))
g = CERT[("V", "mu", "ratio")]
assert g[1] == 0 and g[2] == 0
g = CERT[("V", "generic", "ratio")]
assert g[1] == 0 and g[2] == 0
for key in (("V", "kappa", "ratio"), ("V", "vacuum", "product")):
    g = CERT[key]
    assert g[0] == g[2] and g[1] == -3*g[3]     # (1+sqrt-3)*(u + v*s231)
res["certificate_structure"] = {
    "V_mu_ratio": "untwisted, in Q(sqrt-231)",
    "V_generic_ratio": "untwisted, in Q(sqrt-231)",
    "V_kappa_ratio": "2*zeta6 * (element of Q(sqrt-231))",
    "V_vacuum_product": "2*zeta6 * (element of Q(sqrt-231))",
    "denominator_law": "every V-certificate carries 953^4 alongside the "
                       "partner prime (13^3 for mu, 19^3 for kappa, "
                       "13 for vacuum)"}
print(f"  certificate structure verified ({time.time()-T0:.0f}s)", flush=True)

# ------------------------------------------------------------------ stage 3
print("== stage 3: the place structure at the value primes ==", flush=True)
L, B2c, C1c, E0c = 500716339200, -2075673600, -4769856, 2197
assert [int(c) for c in MU.all_coeffs()] == [L, B2c, C1c, E0c]
# monic integral model y = L*rho: m(y) = y^3 + B2 y^2 + C1*L y + E0*L^2
m_poly = sp.Poly(y**3 + B2c*y**2 + C1c*L*y + E0c*L**2, y)
dm = int(sp.discriminant(m_poly.as_expr(), y))
assert sorted(sp.factorint(dm)) == [2, 3, 5, 7, 11, 13]   # no value primes
# V = P(y)/d, P in Z[y]
v2c, v1c, v0c = vc[0], vc[1], vc[2]
Vy = v0c + (v1c/L)*y + (v2c/sp.Integer(L)**2)*y**2
d_den = sp.ilcm(v0c.q, (v1c/L).q, (v2c/sp.Integer(L)**2).q)
Pint = sp.Poly(sp.expand(Vy*d_den), y)
Pc = [int(c) for c in Pint.all_coeffs()]
assert all(sp.Rational(c).q == 1 for c in Pint.all_coeffs())

# THE INTEGRALITY LEMMA (exact): e1, e2, e3 have lowest-terms denominator
# EXACTLY 953^4.  For any place w over a prime q != 953, all e_i are
# w-integral; if v_w(V) = -t < 0 then v_w(V^3) = -3t while
# v_w(e1 V^2 - e2 V + e3) >= -2t > -3t -- contradiction with
# V^3 = e1 V^2 - e2 V + e3.  So V is integral at EVERY place outside 953,
# and at 953 the same argument bounds v_w(V) >= -4.  V's denominator
# support is decided entirely over 953.
E1, E2, E3 = (sp.Rational(N1, D953), sp.Rational(N2, D953),
              sp.Rational(N3, D953))
for e in (E1, E2, E3):
    assert e.q == D953   # lowest terms: denominator exactly 953^4
res["integrality_lemma"] = {
    "statement": "den(e1)=den(e2)=den(e3)=953^4 exactly => V integral at "
                 "every place outside 953 (char-poly valuation argument), "
                 "and v_w(V) >= -4 over 953",
    "hypothesis_check": "e_i lowest-terms denominators = 953^4, asserted"}
print("  integrality lemma: V's denominator support lives over 953 only",
      flush=True)

def vp(n, p):
    assert n != 0
    v = 0
    while n % p == 0: n //= p; v += 1
    return v

def mval(t, mod): return (((t + B2c) % mod * t + C1c*L) % mod * t
                          + E0c*L**2) % mod
def mder(t, mod): return (3*t*t + 2*B2c*t + C1c*L) % mod
def Pval(t, mod): return ((Pc[0]*t + Pc[1]) % mod * t + Pc[2]) % mod

KLIFT = 40
res["places"] = {}
for p in (953, 1129, 421493):
    assert dm % p != 0 and L % p != 0     # clean model at p
    fl = sp.factor_list(MU.as_expr(), rho, modulus=p)
    fdegs = sorted(sp.Poly(f, rho).degree() for f, _ in fl[1])
    assert fdegs == [1, 2], (p, fdegs)
    fm = sp.factor_list(m_poly.as_expr(), y, modulus=p)
    lin_p = [f for f, mm in fm[1] if sp.Poly(f, y).degree() == 1][0]
    r0 = int((-sp.Poly(lin_p, y).all_coeffs()[1]) % p)
    r_rho = (r0 * pow(L, -1, p)) % p
    assert (L*r_rho**3 + B2c*r_rho**2 + C1c*r_rho + E0c) % p == 0
    # Newton/Hensel lift of the simple root to mod p^KLIFT
    mod = p**KLIFT
    r = r0; kcur = 1
    while kcur < KLIFT:
        kcur = min(2*kcur, KLIFT)
        m2 = p**kcur
        r = (r - mval(r, m2) * pow(mder(r, m2), -1, m2)) % m2
    assert mval(r, mod) == 0 or vp(mval(r, mod), p) >= KLIFT
    # degree-one place valuation
    num1 = Pval(r, mod)
    vnum1 = vp(num1, p) if num1 else KLIFT
    vd = vp(d_den, p) if int(d_den) % p == 0 else 0
    vw1 = vnum1 - vd
    # lifted cofactor quadratic: m = (y - r)(y^2 + b y + c) mod p^KLIFT
    b_ = (B2c + r) % mod
    c_ = (C1c*L + r*b_) % mod
    assert (-r*c_ - E0c*L**2) % mod == 0
    # reduce P mod the quadratic: A + B*y; unramified deg-2 place =>
    # v = min(v_p(A), v_p(B)) (the residue algebra F_p[y]/(quad) is the
    # FIELD F_p^2, so {1, y} is an integral basis of the completion)
    A_ = (Pc[2] - Pc[0]*c_) % mod
    B_ = (Pc[1] - Pc[0]*b_) % mod
    vA = vp(A_, p) if A_ else KLIFT
    vB = vp(B_, p) if B_ else KLIFT
    vw2 = min(vA, vB) - vd
    # f-weighted norm consistency (exact): v_p(N(V)) from e3
    vN = (vp(E3.p, p) if E3.p % p == 0 else 0) - \
         (vp(E3.q, p) if E3.q % p == 0 else 0)
    assert vw1 + 2*vw2 == vN, (p, vw1, vw2, vN)
    entry = {"mu_mod_p": sp.sstr(fl[1]),
             "rho_residue_deg1": int(r_rho),
             "v_deg1_place": int(vw1), "v_deg2_place": int(vw2),
             "norm_consistency": f"{vw1} + 2*{vw2} = v_p(N(V)) = {vN}"}
    # residues + unit-corrected symmetric congruences where V is a unit
    du = d_den // p**vd
    duinv = pow(int(du), -1, p)
    u953 = pow(953, 4, p) if p != 953 else None
    if vw1 == 0 and vw2 == 0:
        res1 = ((num1 // p**vd) * duinv) % p
        Ares = ((A_ // p**vd) * duinv) % p
        Bres = ((B_ // p**vd) * duinv) % p
        tr2 = (2*Ares - Bres*(b_ % p)) % p
        nr2 = (Ares*Ares - Ares*Bres*(b_ % p) + Bres*Bres*(c_ % p)) % p
        # e1 = res1 + tr2, e2 = nr2 + res1*tr2 (mod p, up to the 953^4 unit)
        assert (res1 + tr2) % p == (N1 % p) * pow(u953, -1, p) % p, p
        assert (nr2 + res1*tr2) % p == (N2 % p) * pow(u953, -1, p) % p, p
        entry["V_residue_deg1"] = int(res1)
        entry["V_residue_deg2"] = f"{Ares} + {Bres}*y in F_p2"
        entry["congruences"] = {
            "trace": f"res1 + Tr_deg2 = {(res1+tr2) % p} = e1*(unit) mod p",
            "e2": f"N_deg2 + res1*Tr_deg2 = {(nr2+res1*tr2) % p} "
                  f"= e2*(unit) mod p"}
        if N1 % p == 0:
            entry["localization"] = ("e1's numerator prime: the TRACE of "
                                     "the V-residues vanishes mod p")
            assert (res1 + tr2) % p == 0
        if N2 % p == 0:
            entry["localization"] = ("e2's numerator prime: the SECOND "
                                     "symmetric function of the V-residues "
                                     "vanishes mod p")
            assert (nr2 + res1*tr2) % p == 0
    res["places"][str(p)] = entry
    print(f"  p={p}: rho == {r_rho} at the deg-1 place; "
          f"v_deg1(V) = {vw1}, v_deg2(V) = {vw2}"
          + (f"; residues {entry.get('V_residue_deg1','-')} | "
             f"{entry.get('V_residue_deg2','-')}" if vw1 == 0 else ""),
          flush=True)

# the H-B917-SPLIT verdict
v953 = res["places"]["953"]
verdict_yes = (v953["v_deg1_place"] == -4 and v953["v_deg2_place"] == 0)
assert verdict_yes
res["H_B917_SPLIT"] = {
    "question": "do V's denominators select exactly the degree-one places?",
    "verdict": "YES (theorem-shape)",
    "content": "V's denominator ideal is w1(953)^4 EXACTLY: the integrality "
               "lemma confines denominators to places over 953; the Hensel "
               "computation gives v = -4 at the degree-one place, v = 0 at "
               "the degree-two place. At 1129 and 421493 V is a unit at "
               "both places; those primes enter through numerator "
               "congruences instead (421493: the trace of the residues "
               "vanishes; 1129: the second symmetric function vanishes)."}
print("  H-B917-SPLIT: YES -- denominator ideal = (deg-1 place over 953)^4 "
      f"exactly ({time.time()-T0:.0f}s)", flush=True)

json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1,
          default=str)
print(f"saved results.json ({time.time()-T0:.0f}s)", flush=True)
