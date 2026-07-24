"""B771 Phase-1 Wave-5 cell W5-204 -- the being-hand 3-adic defect pattern d(n).

TARGET (B690 / S067, structural labels only; Gate 5-Q, no SM reading):
  The "being" object is GSWZ's symmetrised figure-eight Habiro series
  P(h) = Phi(h)Phi(-h), expanded in u = q-1.  Its coefficient denominators are
  PURE POWERS OF 3 (B685/B755, computed).  Write

        v3(n) = 3-adic valuation of the denominator of the u^n coefficient
        pred(n) = n + v3(n!)              (the being divided-power law)
        d(n) = v3(n) - pred(n)            (the being-hand DEFECT)

  B690 (intake, on ~10 published coefficients) reported
        n:      2   3   4   5   100
        v3:     3   3   5   5   146
        pred:   2   4   5   6   148
        d:     +1  -1   0  -1   -2      (|d|<=2, exact only at n=4)
  with the honest caveat: the EXACT pattern needs the FULL GSWZ tower
  (GSWZ's 600-term run used unpublished scripts).

WHAT THIS CELL DOES (compute-not-cite, house method):
  1. Independently EXTRACT the Phi(h) coefficients r_j (Ohtsuki/Kashaev
     asymptotics of 4_1) from an exact Kashaev ladder + Richardson fit,
     recognised as exact rationals (PSLQ), 2 seeds (full vs sub fit) with a
     conditioning gate (trusted-digit estimate), r_1=11/24 & r_2=697/1152
     hard-gated against GSWZ eq (1).  This is the discriminating datum IN-CELL.
  2. Form P(h)=Phi(h)Phi(-h) EXACTLY, substitute h=log(1+u), expand in u as
     far as the recognised r-tower's EVEN reach permits (u^n exact needs the
     even coefficient b_{2k} for 2k<=n, hence r_{2k}; largest even reach with
     r_1..r_M is 2*floor(M/2), giving n up to 2*floor(M/2)+1).
  3. Compute v3(n), pred(n), d(n) for every reachable n; verify pure-3 and,
     where GSWZ eq (2) is printed (n<=5), MATCH it.
  4. VERDICT block (emits UNRESOLVED-capable):
       - full pattern d(n) for ALL n (incl the n=100 tower point) => RESOLVED-A
       - partial d(n) to the extraction reach + EXTERNAL boundary named
         (the full 600-term GSWZ tower / n=100 valuation, unpublished scripts)
         => RESOLVED-B
  B772 parity note (in code): the target is a quantum TRACE (Kashaev = |.|^2
  sum); P(h) is the h-EVEN (theta-even) symmetrisation.  We record the odd/
  theta-odd analog explicitly -- the odd sector is where the non-3 primes of
  the r_j live and where the pure-3 cancellation could FAIL.
"""
import json, os
import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- extraction parameters (tuneable; more points+dps => deeper r-tower) -----
DPS = 1300
NPTS = 48
STEP = 900
mp.mp.dps = DPS

V = 2 * mp.im(mp.polylog(2, mp.expjpi(mp.mpf(1) / 3)))   # 2*Im Li2(e^{i pi/3})


def kashaev(N):
    """|4_1|_N Kashaev invariant = sum_{k=0}^{N-1} |(q;q)_k|^2, q=e^{2 pi i/N}."""
    q = mp.expjpi(mp.mpf(2) / N)
    qk = mp.mpc(1)
    prod = mp.mpc(1)
    tot = mp.mpf(1)                       # k=0 term
    for k in range(1, N):
        qk *= q
        prod *= (1 - qk)
        tot += abs(prod) ** 2
    return tot


def fit(points):
    """Exact Vandermonde solve t = sum_j c_j x^j, x = 1/N, through the points."""
    m = len(points)
    A = mp.matrix(m, m)
    b = mp.matrix(m, 1)
    for i, (N, t) in enumerate(points):
        x = mp.mpf(1) / N
        for j in range(m):
            A[i, j] = x ** j
        b[i] = t
    return mp.lu_solve(A, b)


LADDER = [STEP * j for j in range(1, NPTS + 1)]
print(f"[extract] ladder N={LADDER[0]}..{LADDER[-1]} ({NPTS} pts), dps={DPS}", flush=True)
tvals = []
for N in LADDER:
    K = kashaev(N)
    s = K / (mp.mpf(N) ** mp.mpf(1.5) * mp.e ** (N * V / (2 * mp.pi)))
    tvals.append(s * mp.mpf(3) ** mp.mpf(0.25))          # t(N) -> Phi asymptotics

full = fit(list(zip(LADDER, tvals)))
sub = fit(list(zip(LADDER[2:], tvals[2:])))              # 2nd seed: drop 2 smallest N
assert abs(full[0] - 1) < mp.mpf("1e-20"), "normalisation gate failed (c0 != 1)"

rs = []
extract_log = []
for j in range(1, NPTS - 2):
    cf, cs = full[j], sub[j]
    agree = -mp.log10(abs(cf - cs) / (abs(cf) + mp.mpf("1e-300")) + mp.mpf("1e-300"))
    rj = cf * mp.mpf(3) ** (mp.mpf(3 * j) / 2) / (2 * mp.pi) ** j
    tol = mp.mpf(10) ** (-(max(int(agree) - 14, 8)))     # PSLQ tol = agree-14, both dirs
    rel = mp.pslq([mp.mpf(1), rj], tol=tol, maxcoeff=10 ** 22, maxsteps=10 ** 7)
    if rel is None or rel[1] == 0:
        print(f"  r_{j}: trusted ~{int(agree)}d, NOT recognised -- extraction stops")
        break
    frac = sp.Rational(rel[0], -rel[1])
    resid = abs(rj - mp.mpf(frac.p) / frac.q)
    need = agree - mp.log10(abs(frac.q)) - 3             # E25 coefficient-aware accept
    ok = resid < mp.mpf(10) ** (-max(need, 12))
    print(f"  r_{j} = {frac}  (trusted ~{int(agree)}d, den~1e{len(str(frac.q))}, "
          f"resid {mp.nstr(resid,3)}, accept={ok})")
    if not ok:
        print(f"  r_{j}: recognised but failed acceptance -- extraction stops")
        break
    rs.append(frac)
    extract_log.append({"j": j, "r": f"{frac.p}/{frac.q}", "trusted_digits": int(agree)})

# ---- hard gates against GSWZ eq (1) (the two PUBLISHED coefficients) ----------
assert rs[0] == sp.Rational(11, 24), f"GATE r1: {rs[0]}"
assert rs[1] == sp.Rational(697, 1152), f"GATE r2: {rs[1]}"
M = len(rs)
print(f"[extract] {M} coefficients recognised; r1,r2 match GSWZ eq (1).", flush=True)

# ---- form P(h)=Phi(h)Phi(-h) EXACTLY, expand in u=q-1 ------------------------
# Phi(h) = 1 + sum_j r_j x^j h^j,  x = 1/(3 sqrt(-3)),  x^2 = -1/27.
h, u, x = sp.symbols("h u x")
even_reach = 2 * (M // 2)                 # largest even h coeff fully determined
order = even_reach + 1                    # u^n exact for n <= even_reach+1 (odd h=0)
Phi_p = 1 + sum(rs[j - 1] * x ** j * h ** j for j in range(1, M + 1))
Phi_m = 1 + sum(rs[j - 1] * x ** j * (-h) ** j for j in range(1, M + 1))
prod = sp.expand(Phi_p * Phi_m)
for _ in range(M + 2):                    # reduce x^2 -> -1/27 to exhaustion
    prod = sp.expand(prod.subs(x ** 2, sp.Rational(-1, 27)))
prod = sp.expand(prod + sp.O(h ** (order + 1))).removeO()
assert x not in prod.free_symbols, "odd x power survived -- product must be h-even"

# odd-h coefficients must vanish identically (P is h-even) -- CHECK, don't assume
odd_vanish = all(sp.simplify(prod.coeff(h, m)) == 0 for m in range(1, order + 1, 2))

hs = sp.series(sp.log(1 + u), u, 0, order + 1).removeO()
sym = sp.expand(sp.series(prod.subs(h, hs), u, 0, order + 1).removeO())

# ---- the DEFECT pattern d(n) -------------------------------------------------
def v3fact(n):
    s, m = 0, n
    while m:
        s += m % 3
        m //= 3
    return (n - s) // 2                    # v3(n!) = (n - s_3(n))/2 (Legendre)

PRINTED = {2: sp.Rational(-1, 27), 3: sp.Rational(1, 27),
           4: sp.Rational(-4, 243), 5: sp.Rational(-1, 243)}   # GSWZ eq (2)

rows = []
pure3 = True
eq2_ok = True
for n in range(2, order + 1):
    ck = sym.coeff(u, n)
    den = sp.fraction(sp.nsimplify(ck))[1]
    fac = sp.factorint(den)
    p3 = set(fac) <= {3}
    pure3 &= p3
    v3 = fac.get(3, 0) if p3 else None
    pred = n + v3fact(n)
    d = (v3 - pred) if v3 is not None else None
    printed_match = None
    if n in PRINTED:
        printed_match = (ck == PRINTED[n])
        eq2_ok &= printed_match
    rows.append({"n": n, "coeff": str(ck), "den": str(den),
                 "pure3": bool(p3), "v3": v3, "pred": pred, "defect": d,
                 "eq2_printed": (str(PRINTED[n]) if n in PRINTED else None),
                 "eq2_match": printed_match})
    tag = ""
    if n in PRINTED:
        tag = f"  [eq(2) {PRINTED[n]}: {'MATCH' if printed_match else 'MISMATCH'}]"
    print(f"  n={n}: coeff={ck}  v3={v3}  pred={pred}  d={d}{tag}")

# ---- the EXTERNAL boundary (the cited n=100 tower point) ----------------------
# GSWZ's full 600-term run (unpublished scripts) gives v3(100)=146 => d(100)=-2.
EXT = {"n": 100, "v3_cited": 146, "pred": 100 + v3fact(100),
       "defect_cited": 146 - (100 + v3fact(100)),
       "source": "GSWZ full 600-term tower (unpublished scripts); CITED, not in-cell"}

# ---- B772 parity / theta-odd note (computed, not asserted) -------------------
# The theta-ODD analog Q(h) = Phi(h)/Phi(-h) (odd under h->-h at leading order):
# its low coefficients carry the non-3 primes that P(h) cancels. Compute q-den
# primes for the first few orders to SHOW the even-symmetrisation hides them.
Phi_m_ser = 1 + sum(rs[j - 1] * x ** j * (-h) ** j for j in range(1, M + 1))
quo = sp.series(Phi_p / Phi_m_ser, h, 0, min(order, M) ).removeO()
for _ in range(M + 2):
    quo = sp.expand(quo.subs(x ** 2, sp.Rational(-1, 27)))
odd_primes = set()
for m in range(1, min(order, M)):
    cm = quo.coeff(h, m)
    if cm != 0 and x not in sp.sympify(cm).free_symbols:
        d_ = sp.fraction(sp.nsimplify(cm))[1]
        odd_primes |= set(sp.factorint(d_))
theta_odd_has_non3 = bool(odd_primes - {3})

# ---- VERDICT (in-code; UNRESOLVED-capable) -----------------------------------
defects = {r["n"]: r["defect"] for r in rows if r["defect"] is not None}
reached_all_n = False        # a full all-n closed form (incl n=100) is NOT in-cell
partial_ok = (M >= 2 and pure3 and eq2_ok and odd_vanish and len(defects) >= 4)
max_abs_defect = max(abs(d) for d in defects.values()) if defects else None
exact_ns = sorted(n for n, d in defects.items() if d == 0)

if reached_all_n:
    verdict = "RESOLVED-A"
    headline = "full being-hand defect pattern d(n) computed for all n"
elif partial_ok:
    verdict = "RESOLVED-B"
    headline = (f"partial d(n) computed n=2..{order} (|d|<={max_abs_defect}, exact at "
                f"n={exact_ns}); EXTERNAL boundary = full GSWZ 600-term tower (n=100 "
                f"v3=146 cited, unpublished scripts)")
else:
    verdict = "UNRESOLVED"
    headline = "extraction/consistency gates did not pass; no defect pattern banked"

result = {
    "cell": "W5-204",
    "target": "B690 being-hand 3-adic defect d(n) = v3(denom) - (n + v3(n!))",
    "extraction": {"dps": DPS, "n_points": NPTS, "coeffs_recognised": M,
                   "r_j": [f"{r.p}/{r.q}" for r in rs], "log": extract_log},
    "even_reach": even_reach, "u_order_exact": order,
    "checks": {"pure3": bool(pure3), "eq2_printed_match": bool(eq2_ok),
               "odd_h_vanishes": bool(odd_vanish)},
    "defect_rows": rows,
    "defect_pattern": {str(n): d for n, d in defects.items()},
    "max_abs_defect": max_abs_defect, "exact_ns": exact_ns,
    "external_boundary": EXT,
    "b772_parity_note": {"target_is_trace": True,
                         "P_is_theta_even_symmetrisation": True,
                         "theta_odd_denominator_primes": sorted(int(p) for p in odd_primes),
                         "theta_odd_carries_non3": theta_odd_has_non3,
                         "reading": ("the pure-3 being law is a property of the h-EVEN "
                                     "(theta-even) symmetrisation P=Phi(h)Phi(-h); the "
                                     "theta-odd analog Phi/Phi carries non-3 primes that "
                                     "the symmetrisation cancels -- the defect pattern is "
                                     "an even-sector statement, per the B772 lesson")},
    "verdict": verdict, "headline": headline,
    "gate_5Q": "structural labels being/hearing only; no SM reading; nothing to CLAIMS",
}
with open(os.path.join(HERE, "results.json"), "w") as f:
    json.dump(result, f, indent=2, default=str)

print()
print("=" * 72)
print(f"VERDICT: {verdict}")
print(headline)
print(f"defect pattern d(n) [in-cell, n=2..{order}]: "
      + ", ".join(f"d({n})={d:+d}" for n, d in sorted(defects.items())))
print(f"  |d|<= {max_abs_defect}; exact (d=0) only at n={exact_ns}")
print(f"EXTERNAL (cited, full tower): d(100) = {EXT['defect_cited']:+d} "
      f"(v3=146, pred={EXT['pred']})")
print(f"checks: pure3={pure3}  eq2_match={eq2_ok}  odd_h_vanishes={odd_vanish}")
print(f"B772 parity: theta-odd (Phi/Phi) denominator primes = "
      f"{sorted(int(p) for p in odd_primes)} (non-3 present: {theta_odd_has_non3})")
print("=" * 72)
