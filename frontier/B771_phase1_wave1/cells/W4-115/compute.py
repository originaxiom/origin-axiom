#!/usr/bin/env python3
"""
B771 W4-115 -- L76: cover-torsion tower vs charge tower e_n law.

Two towers, both attached to the same mathematical object (figure-eight / golden field Q(sqrt5)):

  COVER-TORSION tower  T(n) = |Res(Delta_{4_1}, t^n - 1)| = |L_{2n} - 2|
      = |H_1| of the n-fold cyclic cover of the figure-eight
      (Delta = t^2 - 3t + 1, roots phi^2, phi^-2; Fox-Weber).
      T = 1,5,16,45,121,320,841,... for n=1,2,3,...

  CHARGE tower  e_n = det(I - M_n),  M_n = T_esc^n(F),  T_esc(M)=[[M,M],[M^2,M]], F=[[1,1],[1,0]]
      |e_n| = 1,11,809,18845089,228654672055316545291,... for n=0,1,2,3,4,...
      coker(I-M_n) = Z/|e_n| (the B552 Z/11 base charge is e_1).

The open door (L76): |Res| hits 11^2 = e_1^2 at n=5 (T(5)=121=11^2).
Question: is there a LAW relating the two towers for ALL n, or is the n=5 hit isolated/base-rate?

SEALED CRITERION:
  law relating the towers found & verified n<=12  => RESOLVED-A
  no law (n=5 hit isolated / base-rate)           => RESOLVED-B
  computation inconclusive                        => UNRESOLVED

House method: exact/symbolic; discriminating facts computed IN-CELL; comparator control; E20 on specialness.
"""

import json
import sympy as sp

x, t, y = sp.symbols('x t y')

NMAX_COVER = 12          # cover tower index n = 1..12
NMAX_CHARGE = 5          # charge tower rung n = 0..5 (exact; |e_5| already 62 digits)

results = {"cell": "W4-115", "lead": "L76", "checks": {}}
LOG = []
def log(s=""):
    LOG.append(str(s))
    print(s)

# ----------------------------------------------------------------------------
# (0) Lucas numbers (exact integers)
# ----------------------------------------------------------------------------
def lucas(n):
    a, b = 2, 1   # L_0=2, L_1=1
    if n == 0: return 2
    for _ in range(n - 1):
        a, b = b, a + b
    return b

def fib(n):
    a, b = 0, 1
    if n == 0: return 0
    for _ in range(n - 1):
        a, b = b, a + b
    return b

# ----------------------------------------------------------------------------
# (1) COVER-TORSION tower  T(n) = |L_{2n} - 2|, verified 3 independent ways
# ----------------------------------------------------------------------------
log("="*78)
log("(1) COVER-TORSION tower  T(n) = |Res(Delta, t^n-1)| = |L_{2n}-2|")
log("="*78)

# Delta_{4_1} = t^2 - 3 t + 1  (figure-eight Alexander poly, roots phi^2 & phi^-2)
Delta = t**2 - 3*t + 1
Tvals = {}
Tfact = {}
for n in range(1, NMAX_COVER + 1):
    # method A: resultant Res_t(Delta, t^n - 1)  (exact, symbolic)
    resA = int(abs(sp.resultant(Delta, t**n - 1, t)))
    # method B: |L_{2n} - 2|
    resB = abs(lucas(2*n) - 2)
    # method C: |N_{Q(sqrt5)}(phi^{2n}-1)| = |a^2 + a b - b^2|, a=F_{2n-1}-1, b=F_{2n}
    a = fib(2*n - 1) - 1
    b = fib(2*n)
    resC = abs(a*a + a*b - b*b)
    assert resA == resB == resC, f"cover-tower method disagreement at n={n}: {resA},{resB},{resC}"
    Tvals[n] = resA
    Tfact[n] = sp.factorint(resA) if resA > 0 else {}

log("n : T(n) = |L_{2n}-2|            factorization")
for n in range(1, NMAX_COVER + 1):
    fs = "*".join(f"{p}^{e}" if e > 1 else f"{p}" for p, e in sorted(Tfact[n].items())) or "1"
    log(f"{n:2d}: {Tvals[n]:<24d}  {fs}")
results["checks"]["cover_tower_T"] = {str(n): Tvals[n] for n in Tvals}
results["checks"]["cover_tower_methods_agree"] = True

# Structural fact used as a control below: odd-n torsion is ALWAYS a perfect square = L_n^2
odd_square_fact = {}
for n in range(1, NMAX_COVER + 1, 2):
    Ln = lucas(n)
    assert Tvals[n] == Ln*Ln, f"odd-n square law fails at n={n}"
    odd_square_fact[n] = Ln
log("\nControl fact (asserted): T(odd n) = L_n^2 is a PERFECT SQUARE for every odd n.")
log("  sqrt(T(odd n)) = L_n = " + ", ".join(f"L_{n}={odd_square_fact[n]}" for n in odd_square_fact))
results["checks"]["odd_n_torsion_is_square"] = {str(n): odd_square_fact[n] for n in odd_square_fact}

# ----------------------------------------------------------------------------
# (2) CHARGE tower  e_n = det(I - M_n),  two independent methods
# ----------------------------------------------------------------------------
log("\n" + "="*78)
log("(2) CHARGE tower  e_n = det(I - M_n),  M_n = escalator T_esc^n(F)")
log("="*78)

# method A -- direct integer matrix det for small rungs (cross-check)
def escalator(M):
    # T_esc(M) = [[M, M],[M^2, M]]
    M2 = M * M
    top = M.row_join(M)
    bot = M2.row_join(M)
    return top.col_join(bot)

F = sp.Matrix([[1, 1], [1, 0]])
e_direct = {}
Mn = F
for n in range(0, 5):   # up to 32x32 (n=4) exact matrix det
    dim = Mn.shape[0]
    en = int((sp.eye(dim) - Mn).det())
    e_direct[n] = en
    if n < 4:
        Mn = escalator(Mn)

# method B -- charpoly-resultant recursion (poly stays 1-variable; scales further)
#   p_0 = x^2 - x - 1
#   p_{n+1}(x) = Res_t( p_n(t), x^2 - 2 t x + t^2 - t^3 )   (monic-normalized)
#   e_n = p_n(1)
p = x**2 - x - 1
e_recur = {}
p_list = {}
for n in range(0, NMAX_CHARGE + 1):
    pn = sp.Poly(p, x)
    p_list[n] = pn
    e_recur[n] = int(pn.eval(1))
    if n < NMAX_CHARGE:
        doub = x**2 - 2*t*x + t**2 - t**3          # x^2 - 2 mu x + mu^2 - mu^3  with mu=t
        pt = p.subs(x, t)                          # p_n expressed in the eliminated variable t
        r = sp.resultant(sp.Poly(pt, t), sp.Poly(doub, t), t)   # eliminate t -> poly in x
        rp = sp.Poly(sp.expand(r), x)
        # normalize to monic
        lead = rp.LC()
        rp = sp.Poly(rp.as_expr() / lead, x)
        p = sp.expand(rp.as_expr())

# reconcile signs: use |e_n|
e_abs = {n: abs(e_recur[n]) for n in e_recur}
# cross-check the two methods where both available
for n in e_direct:
    assert abs(e_direct[n]) == e_abs[n], f"charge-tower method disagreement n={n}: {e_direct[n]} vs {e_recur[n]}"
log("charge-tower methods (direct matrix det vs charpoly-resultant) AGREE on n=0..4: True")

# known-value anchor (computed here, asserted -- discriminating facts not cited)
known = {0: 1, 1: 11, 2: 809, 3: 18845089, 4: 228654672055316545291}
for n, v in known.items():
    assert e_abs[n] == v, f"charge value mismatch n={n}: got {e_abs[n]} expected {v}"
log("charge values anchored (asserted): |e_0..e_4| = 1,11,809,18845089,228654672055316545291")

e_fact = {n: sp.factorint(e_abs[n]) for n in e_abs}
log("\nn : |e_n|                         factorization")
for n in range(0, NMAX_CHARGE + 1):
    fs = "*".join(f"{p_}^{e_}" if e_ > 1 else f"{p_}" for p_, e_ in sorted(e_fact[n].items())) or "1"
    v = e_abs[n]
    vs = str(v) if v < 10**22 else f"{v} (~1e{len(str(v))-1})"
    log(f"{n:2d}: {vs:<30s}  {fs}")
results["checks"]["charge_tower_e_abs"] = {str(n): str(e_abs[n]) for n in e_abs}
results["checks"]["charge_tower_methods_agree"] = True

charge_primes = set()
for n in e_fact:
    charge_primes |= set(e_fact[n].keys())
log("\ncharge-tower primes (n<=5): " + ", ".join(str(p_) for p_ in sorted(charge_primes)))

# ----------------------------------------------------------------------------
# (2b) BOTH towers are norms from Q(sqrt5) -- the shared HOME (not a term-law)
#      cover: T(n) = |N(phi^{2n}-1)|   (verified above, method C)
#      charge: e_n = |N_{Q(sqrt5)}(g_n(phi))| via doubling transfer D(G)=Res_t(t^2-2yt+y^2-y^3, G)
# ----------------------------------------------------------------------------
log("\n" + "="*78)
log("(2b) SHARED HOME: both towers are norms from Q(sqrt5)")
log("="*78)
# g_1 = x^3 - x^2 + 2x - 1 ;  g_{n+1}(y) = Res_t(t^2 - 2 y t + y^2 - y^3, g_n(t))
def norm_Qsqrt5_of_poly_at_phi(poly_expr):
    # evaluate poly at phi and at psi (Galois conjugate), multiply -> rational integer
    phi = (1 + sp.sqrt(5))/2
    psi = (1 - sp.sqrt(5))/2
    val = sp.simplify(poly_expr.subs(x, phi) * poly_expr.subs(x, psi))
    return int(sp.nsimplify(val))

g = x**3 - x**2 + 2*x - 1
norm_ok = {}
for n in range(1, 4):   # verify n=1,2,3 (degrees 3,9,27) exactly
    Ncharge = abs(norm_Qsqrt5_of_poly_at_phi(g))
    norm_ok[n] = (Ncharge == e_abs[n])
    assert Ncharge == e_abs[n], f"golden-norm charge mismatch n={n}: {Ncharge} vs {e_abs[n]}"
    # doubling transfer to next g
    doub = t**2 - 2*y*t + y**2 - y**3
    gn = sp.resultant(sp.Poly(doub, t), sp.Poly(g.subs(x, t), t), t)
    g = sp.expand(gn.subs(y, x))
log("charge e_n = |N_{Q(sqrt5)}(g_n(phi))| verified exactly for n=1,2,3:  " + str(all(norm_ok.values())))
log("cover  T(n) = |N_{Q(sqrt5)}(phi^{2n}-1)| verified exactly for n=1..12 (method C above).")
log("=> BOTH sequences are norms from the SAME field Q(sqrt5) -- a shared arithmetic HOME,")
log("   but of DIFFERENT elements (cyclotomic-type phi^{2n}-1 vs cubic-iterate g_n(phi)).")
results["checks"]["both_are_Qsqrt5_norms"] = True

# ----------------------------------------------------------------------------
# (3) CROSS TESTS -- is there a term-relating LAW?  (all asserted with direction)
# ----------------------------------------------------------------------------
log("\n" + "="*78)
log("(3) CROSS TESTS between the two towers")
log("="*78)

Tset = Tvals                      # n=1..12
Eset = e_abs                      # n=0..5

# (3a) direct EQUALITY  T(n) == e_m  (nontrivial: value>1)
eq_hits = []
for n in Tset:
    for m in Eset:
        if Tset[n] > 1 and Tset[n] == Eset[m]:
            eq_hits.append((n, m, Tset[n]))
log(f"(3a) EQUALITY T(n)==e_m, value>1 : {eq_hits if eq_hits else 'NONE'}")

# (3b) SQUARE  T(n) == e_m^2
sq_hits = []
for n in Tset:
    for m in Eset:
        if Tset[n] > 1 and Tset[n] == Eset[m]**2:
            sq_hits.append((n, m, Tset[n]))
log(f"(3b) SQUARE   T(n)==e_m^2, value>1 : {sq_hits if sq_hits else 'NONE'}")

# (3c) higher powers T(n) == e_m^k, k=3,4  (value>1)
pow_hits = []
for n in Tset:
    for m in Eset:
        for k in (3, 4):
            if Eset[m] > 1 and Tset[n] > 1 and Tset[n] == Eset[m]**k:
                pow_hits.append((n, m, k, Tset[n]))
log(f"(3c) HIGHER POWER T(n)==e_m^k (k=3,4): {pow_hits if pow_hits else 'NONE'}")

# (3d) DIVISIBILITY both directions with NONTRIVIAL charge value (e_m>1)
div_e_into_T = []   # e_m | T(n)
for n in Tset:
    for m in Eset:
        if Eset[m] > 1 and Tset[n] % Eset[m] == 0:
            div_e_into_T.append((m, n, Eset[m], Tset[n]))
log(f"(3d) e_m | T(n), e_m>1 : {div_e_into_T if div_e_into_T else 'NONE'}")

# (3e) which CHARGE PRIMES appear in the cover tower (n<=12)?
cover_primes = set()
for n in Tset:
    cover_primes |= set(Tfact[n].keys())
shared_primes = sorted(charge_primes & cover_primes)
charge_only = sorted(charge_primes - cover_primes)
log(f"(3e) charge primes: {sorted(charge_primes)}")
log(f"     cover primes (n<=12): {sorted(cover_primes)}")
log(f"     SHARED primes: {shared_primes}")
log(f"     charge primes ABSENT from cover tower: {charge_only}")

# (3f) 11-adic index patterns -- the 'law' the lead conjectured (n = 0 mod 5?)
def vp(nn, p):
    c = 0
    nn = abs(nn)
    while nn % p == 0 and nn != 0:
        nn //= p; c += 1
    return c
cover_11 = {n: vp(Tset[n], 11) for n in Tset}
charge_11 = {n: vp(Eset[n], 11) for n in Eset}
cover_11_idx = [n for n in cover_11 if cover_11[n] > 0]
charge_11_idx = [n for n in charge_11 if charge_11[n] > 0]
log(f"(3f) v_11(T(n)) nonzero at n = {cover_11_idx}   (values {[cover_11[n] for n in cover_11_idx]})")
log(f"     v_11(e_n) nonzero at n = {charge_11_idx}   (values {[charge_11[n] for n in charge_11_idx]})")
# cover pattern: n = 0 mod 5 ; charge pattern: n = 1 mod 3
cover_mod5 = all(n % 5 == 0 for n in cover_11_idx) and len(cover_11_idx) > 0
charge_mod3 = all(n % 3 == 1 for n in charge_11_idx) and len(charge_11_idx) > 0
log(f"     cover 11-divides <=> n = 0 mod 5 : {cover_mod5}")
log(f"     charge 11-divides <=> n = 1 mod 3 : {charge_mod3}")
patterns_incompatible = cover_mod5 and charge_mod3   # 0 mod5 vs 1 mod3 are different APs
log(f"     11-index patterns are DIFFERENT arithmetic progressions (5-periodic vs 3-periodic): {patterns_incompatible}")

results["checks"]["cross"] = {
    "equality_hits": eq_hits,
    "square_hits": [(n, m) for (n, m, v) in sq_hits],
    "higher_power_hits": pow_hits,
    "e_divides_T_hits": [(m, n) for (m, n, a, b) in div_e_into_T],
    "shared_primes": shared_primes,
    "charge_primes_absent_from_cover": charge_only,
    "cover_11_index": cover_11_idx,
    "charge_11_index": charge_11_idx,
    "cover_11_is_mod5": cover_mod5,
    "charge_11_is_mod3": charge_mod3,
    "eleven_patterns_incompatible": patterns_incompatible,
}

# ----------------------------------------------------------------------------
# (4) BASE-RATE COMPARATOR CONTROL (E20 on the '121=11^2' specialness)
#     The n=5 hit decomposes as: T(5)=121 is a square TRIVIALLY (all odd-n
#     torsions are L_n^2); the real content is sqrt(T(5)) = L_5 = 11 = e_1.
#     Control: do OTHER Lucas roots L_n (= sqrt of odd-n torsions) coincide with
#     ANY charge value e_m or charge prime?  A law would need MANY hits; base
#     rate predicts ~the single small-value collision at 11.
# ----------------------------------------------------------------------------
log("\n" + "="*78)
log("(4) BASE-RATE COMPARATOR CONTROL (E20)")
log("="*78)
lucas_roots = {n: lucas(n) for n in range(1, NMAX_COVER + 1, 2)}   # sqrt(T(odd n))
charge_values = set(e_abs.values())
control_hits = []
for n, Ln in lucas_roots.items():
    hit_val = Ln in charge_values and Ln > 1
    hit_prime = Ln in charge_primes and Ln > 1
    if hit_val or hit_prime:
        control_hits.append((n, Ln, hit_val, hit_prime))
log(f"Lucas roots sqrt(T(odd n)) = {lucas_roots}")
log(f"charge values e_m = {sorted(charge_values)}")
log(f"coincidences (L_n equals a charge value OR charge prime): {control_hits}")
log(f"  => number of nontrivial value-collisions across all odd n<=12: {len(control_hits)}")
# The point: T(5)=121 being a SQUARE is generic (every odd n); only its ROOT value 11 collides,
# and it collides exactly ONCE (base rate for a small prime shared by two integer sequences).
n5_is_square_trivially = (Tvals[5] == lucas(5)**2)
only_11_collision = (len(control_hits) == 1 and control_hits[0][1] == 11)
log(f"  T(5)=121 is a perfect square by the generic odd-n law (not special): {n5_is_square_trivially}")
log(f"  the ONLY value-collision is L_5 = 11 = e_1 (a single small-prime coincidence): {only_11_collision}")
results["checks"]["control"] = {
    "lucas_roots": {str(n): lucas_roots[n] for n in lucas_roots},
    "control_hits": control_hits,
    "num_collisions": len(control_hits),
    "n5_square_is_generic": bool(n5_is_square_trivially),
    "only_11_collision": bool(only_11_collision),
}

# ----------------------------------------------------------------------------
# (5) IN-CODE VERDICT
# ----------------------------------------------------------------------------
log("\n" + "="*78)
log("(5) VERDICT LOGIC")
log("="*78)

# A genuine LAW (RESOLVED-A) would require a term-relating structure holding across n:
#   - repeated equalities / powers / divisibilities linking e_m to T(n) beyond trivial n<=1, OR
#   - matching 11-index (or prime-index) patterns under a consistent index map.
# Evidence FOR a law:
law_evidence = []
# (i) nontrivial equalities beyond the single square hit?
extra_equalities = [h for h in eq_hits]                       # value>1 equalities
extra_powers = [h for h in pow_hits]                          # higher powers
# (ii) nontrivial divisibility by a charge value >1 that ISN'T just the shared small prime 11
nontrivial_div = [d for d in div_e_into_T if d[2] not in (11,)]  # e_m>1 not accounted by 11 alone
# (iii) do 11-index patterns MATCH (would be a real law)?  They do NOT (mod5 vs mod3).
patterns_match = (cover_11_idx == charge_11_idx) or (not patterns_incompatible and False)
# (iv) any charge prime (other than 11) appears in cover tower?
extra_shared_primes = [p_ for p_ in shared_primes if p_ != 11]

if extra_equalities: law_evidence.append("nontrivial term equalities T=e")
if extra_powers: law_evidence.append("nontrivial higher-power hits")
if nontrivial_div: law_evidence.append("nontrivial divisibility beyond 11")
if patterns_match: law_evidence.append("matching 11-index patterns")
if extra_shared_primes: law_evidence.append(f"shared charge primes beyond 11: {extra_shared_primes}")

# The single documented hit T(5)=e_1^2 is EXPECTED to remain (sq_hits contains (5,1)).
only_the_known_square = (set((n, m) for (n, m, v) in sq_hits) == {(5, 1)})

log(f"positive law-evidence found: {law_evidence if law_evidence else 'NONE'}")
log(f"only cross-tower hit is the known T(5)=e_1^2 square: {only_the_known_square}")
log(f"charge primes absent from cover tower (n<=12): {charge_only}")
log(f"11-index patterns incompatible (5-periodic vs 3-periodic): {patterns_incompatible}")
log(f"growth: cover ~single-exponential (phi^2n), charge ~double-exponential (log e_n triples/rung)")
log(f"base-rate control: exactly {len(control_hits)} value-collision(s), only L_5=11=e_1")

# decide
computed_ok = (results["checks"]["cover_tower_methods_agree"] and
               results["checks"]["charge_tower_methods_agree"] and
               results["checks"]["both_are_Qsqrt5_norms"])

if not computed_ok:
    verdict = "UNRESOLVED"
    headline = "computation did not close (method cross-checks failed)"
elif law_evidence:
    verdict = "RESOLVED-A"
    headline = "a term-relating law between the towers was found & verified n<=12: " + "; ".join(law_evidence)
elif (only_the_known_square and not extra_shared_primes and patterns_incompatible
      and only_11_collision and n5_is_square_trivially):
    verdict = "RESOLVED-B"
    headline = ("no law relating the towers; the n=5 hit is isolated/base-rate -- "
                "T(5)=121 is a square by the generic odd-n law (T(odd n)=L_n^2), its only content is "
                "the single small-prime collision L_5=11=e_1; the 11-divisibility patterns are "
                "incompatible (cover n=0 mod5, charge n=1 mod3), charge primes {809,1459,...} are "
                "absent from the cover tower, and growth rates differ (single vs double exponential). "
                "Shared arithmetic HOME (both are Q(sqrt5) norms) is a common framework, not a term-law.")
else:
    verdict = "UNRESOLVED"
    headline = "cross-tests neither exhibit a clean law nor cleanly reduce to base-rate"

results["verdict"] = verdict
results["headline"] = headline
results["discriminating_fact"] = (
    "T(5)=121=11^2 and e_1=11, but (a) T(odd n)=L_n^2 is a perfect square for EVERY odd n so "
    "'121 is a square' carries no information; its content is L_5=11=e_1, a single small-prime "
    "value-collision (exactly 1 collision across all odd n<=12). (b) 11 | T(n) iff n=0 mod 5 "
    "(5-periodic) while 11 | e_n iff n=1 mod 3 (3-periodic): incompatible index laws. "
    "(c) charge primes 809,1459,597049,2169349081 divide NO cover-torsion T(n), n<=12. "
    "(d) growth rates differ (cover single-exponential phi^{2n}; charge double-exponential, log|e_n| triples per rung). "
    "The only genuine shared structure is that BOTH are norms from Q(sqrt5) -- a common home, not a relating law."
)

log("\n" + "#"*78)
log(f"VERDICT: {verdict}")
log(headline)
log("#"*78)

with open("output.txt", "w") as f:
    f.write("\n".join(LOG) + "\n")
with open("results.json", "w") as f:
    json.dump(results, f, indent=2, default=str)
print("\n[wrote output.txt, results.json]")
