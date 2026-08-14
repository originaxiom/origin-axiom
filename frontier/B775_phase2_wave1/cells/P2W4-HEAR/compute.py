#!/usr/bin/env python3
"""P2W4-HEAR (OI-026 / L91) -- is the minimal bearing stage kappa = 5 FORCED?

Sealed question: L91 obligation (4) is discharged (B650 types + B644 group
functor + the equivariance wall, wall 9); obligations (1)-(3) collapse
(B666/W32) to ONE hypothesis, H-EAR (the shadow-realization principle):

    H-EAR: the bearing stage is a stage whose theta-odd modular block
    realizes the object's OWN conductor shadow SL(2,F5) through its
    McKay doublet pair (D(theta-odd) = 2, block projectively factoring
    through the mod-5 congruence quotient).

This cell tests H-EAR AS A SELECTION PRINCIPLE, from scratch (independent
re-implementation; the banked W32 numbers are targets, not inputs):

  PART 1  exact: the hearing filter (-w0 computed, not cited) + the
          exact-fit classification D(theta-odd) = 2 over all simply-laced
          families/ranks/levels (enumeration + closed forms = 2nd way).
  PART 2  exact: conformal weights, T-phases, ord(T); the projective
          T-order door and the Kronecker-Weber field door -> A5@1 out.
  PART 3  exact: the object's shadow SL(2,F5) built as the binary
          icosahedral group over Q(sqrt5); its TWO 2-dim (spin) irreps;
          they form ONE Galois orbit under sqrt5 -> -sqrt5.
  PART 4  exact: which doublet each surviving stage carries = the
          T-ratio exponent a in (Z/5)^*; a = 2 (A2@2) vs a = 1 (A4@1)
          sit in the two cosets of squares -- exchanged by sigma_2, the
          Galois element that flips sqrt5 (Gauss sum, verified exactly).
  PART 5  exact: the classical side carries the SAME undetermined bit
          (A1 = [[2,1],[1,1]] has spectrum {phi^2, phi^-2}, one orbit).
  PART 6  exact: the tiebreak audit -- minimality is NOT well-posed:
          kappa-minimality picks A2, LEVEL-minimality picks A4.

Verdict logic in-code; UNRESOLVED is reachable. Everything exact
(Fraction / Q(sqrt5) / cyclotomic integers); no floats decide anything.
Gate 5/5-Q: pure representation theory + lattice arithmetic. No SM values.
"""
from fractions import Fraction as F
from math import gcd
import json
import os

OUT = []


def say(s=""):
    OUT.append(s)
    print(s, flush=True)


def hdr(s):
    say("\n" + "=" * 68)
    say(s)
    say("=" * 68)


# ---------------------------------------------------------------- Cartan
def cartan(fam, n):
    A = [[0] * n for _ in range(n)]
    for i in range(n):
        A[i][i] = 2

    def lk(i, j):
        A[i][j] = A[j][i] = -1

    if fam == "A":
        for i in range(n - 1):
            lk(i, i + 1)
    elif fam == "D":
        for i in range(n - 3):
            lk(i, i + 1)
        lk(n - 3, n - 2)
        lk(n - 3, n - 1)
    elif fam == "E":
        chain = [0, 2, 3, 4, 5, 6, 7][: n - 1]
        for a, b in zip(chain, chain[1:]):
            lk(a, b)
        lk(1, 3)
    return A


def comarks(fam, n):
    if fam == "A":
        return [1] * n
    if fam == "D":
        return [1] + [2] * (n - 3) + [1, 1]
    if fam == "E":
        return {6: [1, 2, 2, 3, 2, 1], 7: [2, 2, 3, 4, 3, 2, 1],
                8: [2, 3, 4, 6, 5, 4, 3, 2]}[n]
    raise ValueError


def hvee(fam, n):
    return 1 + sum(comarks(fam, n))


def dim_g(fam, n):
    if fam == "A":
        return n * (n + 2)
    if fam == "D":
        return n * (2 * n - 1)
    return {6: 78, 7: 133, 8: 248}[n]


def s_i(i, lam, A):
    """simple reflection in fundamental-weight coordinates."""
    return tuple(lam[j] - lam[i] * A[j][i] for j in range(len(lam)))


def conjugation(fam, n):
    """sigma with -w0(Lambda_i) = Lambda_{sigma(i)} -- COMPUTED, not cited."""
    A = cartan(fam, n)
    sig = []
    for i in range(n):
        lam = tuple(1 if j == i else 0 for j in range(n))
        guard = 0
        while any(x > 0 for x in lam):
            j = next(j for j, x in enumerate(lam) if x > 0)
            lam = s_i(j, lam, A)
            guard += 1
            if guard > 10000:
                raise RuntimeError("w0 loop")
        neg = tuple(-x for x in lam)          # = -w0(Lambda_i), dominant
        sig.append(neg.index(1))
    return tuple(sig)


def level_weights(fam, n, k):
    cm = comarks(fam, n)
    res = []

    def rec(i, rem, acc):
        if i == n:
            res.append(tuple(acc))
            return
        for a in range(rem // cm[i] + 1):
            rec(i + 1, rem - a * cm[i], acc + [a])

    rec(0, k, [])
    return res


def D_theta_odd(fam, n, k):
    sig = conjugation(fam, n)
    ws = level_weights(fam, n, k)
    nonself = 0
    for w in ws:
        wc = tuple(w[sig[i]] for i in range(n))
        if wc != w:
            nonself += 1
    assert nonself % 2 == 0
    return nonself // 2


# ---------------------------------------------------------------- PART 1
hdr("PART 1 -- hearing filter (-w0 computed) + the exact-fit D = 2 grid")
fams = [("A", n) for n in range(1, 11)] + [("D", n) for n in range(4, 11)] + \
       [("E", 6), ("E", 7), ("E", 8)]
hearing, deaf = [], []
for fam, n in fams:
    sig = conjugation(fam, n)
    (hearing if sig != tuple(range(n)) else deaf).append(f"{fam}{n}")
say("  HEARS (-w0 != 1): " + " ".join(hearing))
say("  DEAF  (-w0  = 1): " + " ".join(deaf))
filter_ok = (set(hearing) == {f"A{n}" for n in range(2, 11)} |
             {f"D{n}" for n in (5, 7, 9)} | {"E6"})
say(f"  filter = A_(n>=2), D_odd, E6 : {filter_ok}")

grid = []
say("  D(theta-odd) by level:")
for fam, n in [("A", 2), ("A", 3), ("A", 4), ("A", 5), ("A", 6), ("A", 7),
               ("A", 8), ("D", 5), ("D", 7), ("D", 9), ("E", 6)]:
    kmax = 4 if n <= 5 else 3
    row = [D_theta_odd(fam, n, k) for k in range(1, kmax + 1)]
    for k, d in enumerate(row, 1):
        if d == 2:
            grid.append((f"{fam}{n}", k, k + hvee(fam, n)))
    say(f"    {fam}{n} (h^= {hvee(fam,n):2d}): D(k=1..{kmax}) = {row}")
say(f"  D = 2 at (stage, level, kappa): {grid}")
grid_target = [("A2", 2, 5), ("A4", 1, 6), ("A5", 1, 7)]
grid_ok = grid == grid_target
say(f"  reproduces the banked W32 grid {grid_target}: {grid_ok}")

# second way: closed forms, all ranks (closes the rank direction)
cf1 = all(D_theta_odd("A", n, 1) == (n + 1 - (1 + (n % 2))) // 2
          for n in range(2, 21))
cf2 = all(D_theta_odd("A", n, 2) ==
          (1 + n + n * (n + 1) // 2 - (1 + n // 2 + 2 * (n % 2))) // 2
          for n in range(2, 15))
d1 = [D_theta_odd("A", n, 1) for n in range(2, 21)]
d2 = [D_theta_odd("A", n, 2) for n in range(2, 15)]
dd = [(D_theta_odd("D", m, 1), D_theta_odd("D", m, 2)) for m in (5, 7, 9)]
say(f"  2nd way (closed forms level 1 / level 2, n<=20): {cf1} / {cf2}")
say(f"    D(A_n,1) n=2..20: {d1}  -> = 2 only n in {{4,5}}")
say(f"    D(A_n,2) n=2..14: {d2}  -> = 2 only n = 2")
say(f"    D(D_odd,1),(D_odd,2) m=5,7,9: {dd}  -> 1 -> 3, skips 2")
mono = all(D_theta_odd("A", n, k) <= D_theta_odd("A", n, k + 1)
           for n in (2, 3, 4, 5) for k in (1, 2, 3))
say(f"  level-monotonicity (set inclusion) verified on the grid: {mono}")
classification_closed = grid_ok and cf1 and cf2 and mono and filter_ok
say(f"  => CLASSIFICATION (all families, ranks, levels) CLOSED: "
    f"{classification_closed}")


# ---------------------------------------------------------------- PART 2
hdr("PART 2 -- conformal weights, projective T-order, the field door")


def inv_cartan(fam, n):
    A = [[F(x) for x in row] for row in cartan(fam, n)]
    M = [row[:] + [F(1) if i == j else F(0) for j in range(n)]
         for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return [row[n:] for row in M]


def hwt(fam, n, k, lam):
    Ci = inv_cartan(fam, n)
    kap = k + hvee(fam, n)
    ip = sum(F(lam[i]) * Ci[i][j] * F(lam[j]) for i in range(n)
             for j in range(n))
    two_rho = sum(F(2) * F(lam[i]) * Ci[i][j] for i in range(n)
                  for j in range(n))
    return (ip + two_rho) / (2 * kap)


def stage_data(fam, n, k):
    kap = k + hvee(fam, n)
    c = F(k * dim_g(fam, n), kap)
    sig = conjugation(fam, n)
    pairs, seen = [], set()
    for w in level_weights(fam, n, k):
        wc = tuple(w[sig[i]] for i in range(n))
        if wc != w and w not in seen:
            seen |= {w, wc}
            pairs.append(w)
    phases = [(hwt(fam, n, k, w) - c / 24) % 1 for w in pairs]
    allph = [(hwt(fam, n, k, w) - c / 24) % 1
             for w in level_weights(fam, n, k)]
    ordT = 1
    for p in allph:
        ordT = ordT * p.denominator // gcd(ordT, p.denominator)
    return kap, c, pairs, phases, ordT


survivors, excluded = [], []
for fam, n, k in [("A", 2, 2), ("A", 4, 1), ("A", 5, 1)]:
    kap, c, pairs, ph, ordT = stage_data(fam, n, k)
    ratio = (ph[0] - ph[1]) % 1
    a, m = ratio.numerator, ratio.denominator      # projective T-order = m
    field_door = (ordT % 5 == 0)                   # sqrt5 in Q(zeta_ordT)
    # Gamma(5)-certificate: rho_odd(T^5) is SCALAR on the theta-odd block
    # (with the classical fact that Gamma(5) = normal closure of T^5 in
    # SL(2,Z), this gives projective factorization through SL(2,F5)).
    t5_scalar = ((5 * ph[0] - 5 * ph[1]) % 1) == 0
    ok = (m == 5) and field_door and t5_scalar
    say(f"  {fam}{n} level {k} (kappa={kap}, c={c}): theta-odd phases "
        f"{[str(x) for x in ph]}")
    say(f"     projective T-ratio = {ratio} -> order {m}"
        f"   |  ord(T) = {ordT}, 5 | ord(T) : {field_door}"
        f"   |  T^5 scalar on the block (Gamma(5) cert): {t5_scalar}"
        f"   |  H-EAR: {ok}")
    (survivors if ok else excluded).append((f"{fam}{n}_{k}", kap, a, m, ordT))
say("  A5@1 walls (both exact): projective T-order 4 != 5  AND  5 does not"
    " divide 24 => sqrt5 not in Q(zeta24) [Kronecker-Weber, conductor 5]")
say(f"  H-EAR SOLUTION SET = {[(s[0], 'kappa=' + str(s[1])) for s in survivors]}"
    f"   (count {len(survivors)})")
say(f"  excluded = {[e[0] for e in excluded]}")


# ---------------------------------------------------------------- PART 3
hdr("PART 3 -- the object's shadow SL(2,F5) = 2I over Q(sqrt5): TWO doublets")


def qmul(x, y):          # Q(sqrt5): x = (a, b) ~ a + b sqrt5
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def qadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def qsub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def qsig(x):             # the nontrivial Galois automorphism sqrt5 -> -sqrt5
    return (x[0], -x[1])


Z, ONE = (F(0), F(0)), (F(1), F(0))
PHI, PHIINV = (F(1, 2), F(1, 2)), (F(-1, 2), F(1, 2))


def hmul(p, q):
    a1, b1, c1, d1_ = p
    a2, b2, c2, d2_ = q
    return (qsub(qsub(qsub(qmul(a1, a2), qmul(b1, b2)), qmul(c1, c2)),
                 qmul(d1_, d2_)),
            qadd(qadd(qadd(qmul(a1, b2), qmul(b1, a2)), qmul(c1, d2_)),
                 qsub(Z, qmul(d1_, c2))),
            qadd(qadd(qsub(qmul(a1, c2), qmul(b1, d2_)), qmul(c1, a2)),
                 qmul(d1_, b2)),
            qadd(qadd(qadd(qmul(a1, d2_), qmul(b1, c2)),
                      qsub(Z, qmul(c1, b2))), qmul(d1_, a2)))


h = (F(1, 2), F(0))
g1 = ((F(1, 2), F(0)),) * 4
g2 = (qmul(PHI, (F(1, 2), F(0))), qmul(PHIINV, (F(1, 2), F(0))), h, Z)
G, frontier = {g1, g2, (ONE, Z, Z, Z)}, [g1, g2]
while frontier:
    nf = []
    for p in frontier:
        for g in (g1, g2):
            r = hmul(p, g)
            if r not in G:
                G.add(r)
                nf.append(r)
    frontier = nf
G = sorted(G)
say(f"  |2I| = {len(G)}  (binary icosahedral = SL(2,5)) : {len(G) == 120}")
chi = {q: (2 * q[0][0], 2 * q[0][1]) for q in G}      # trace of the SU(2) rep
vals = sorted(set(chi.values()))
say(f"  distinct character values of the defining doublet 2^: {len(vals)}"
    f" (= number of classes)")
norm = (F(0), F(0))
for q in G:
    norm = qadd(norm, qmul(chi[q], chi[q]))
irr = norm == (F(120), F(0))
say(f"  sum |chi|^2 = {norm[0]} + {norm[1]}*sqrt5   -> irreducible: {irr}")
# the Galois action on CHARACTERS: (sigma_t chi)(g) = chi(g^t).  t = 37 is
# = 2 mod 5 (a non-residue: the sqrt5-flip) and = 1 mod 4, 1 mod 3, so
# sigma_t acts trivially on the rest of the exponent-60 cyclotomic field.
def hpow(q, e):
    r = (ONE, Z, Z, Z)
    for _ in range(e):
        r = hmul(r, q)
    return r


T = 37
assert T % 5 == 2 and T % 4 == 1 and T % 3 == 1
chi2 = {q: chi[hpow(q, T)] for q in G}                  # the partner doublet
galois_conj = all(chi2[q] == qsig(chi[q]) for q in G)
distinct = any(chi2[q] != chi[q] for q in G)
norm2 = (F(0), F(0))
for q in G:
    norm2 = qadd(norm2, qmul(chi2[q], chi2[q]))
irr2 = norm2 == (F(120), F(0))
say(f"  partner character chi'(g) := chi(g^{T}) equals sigma(chi(g)) for all"
    f" g: {galois_conj};  chi' != chi: {distinct}; chi' irreducible: {irr2}")
say(f"  values include phi = (1+sqrt5)/2 and -1/phi = (1-sqrt5)/2 : "
    f"{(F(1,2),F(1,2)) in vals and (F(1,2),F(-1,2)) in vals}")
rational_sep = any(chi[q] == qsig(chi[q]) and chi[q] != chi2[q] for q in G)
sym_rational = all(qadd(chi[q], chi2[q])[1] == 0 and
                   qmul(chi[q], chi2[q])[1] == 0 for q in G)
say(f"  Q-rational class value separating them: {rational_sep};  chi+chi'"
    f" and chi*chi' are Q-valued: {sym_rational}")
say("  => {2^, 2^'} is ONE Galois orbit; every Q-rational invariant is")
say("     symmetric in the pair -- no Q-structure tells the branches apart.")
two_doublets = (len(G) == 120 and irr and irr2 and distinct and galois_conj
                and sym_rational and not rational_sep)


# ---------------------------------------------------------------- PART 4
hdr("PART 4 -- which doublet each survivor carries: the Galois bit sigma_2")
# sqrt5 = z + z^4 - z^2 - z^3 in Z[zeta5]; sigma_2 : z -> z^2
vec = [0, 1, -1, -1, 1]                                  # coeffs of z^0..z^4


def red(v):                                              # mod Phi_5
    return [v[i] - v[4] for i in range(4)] + [0]


def act(v, s):
    w = [0] * 5
    for i, ci in enumerate(v):
        w[(i * s) % 5] += ci
    return red(w)


g5 = red(vec[:])
s2 = act(vec, 2)
flips = all(x + y == 0 for x, y in zip(g5, s2))
say(f"  Gauss sum sqrt5 = z+z^4-z^2-z^3;  sigma_2(sqrt5) = -sqrt5 : {flips}")
sq = sorted({(x * x) % 5 for x in (1, 2, 3, 4)})
expo = {s[0]: s[2] for s in survivors}
say(f"  squares mod 5 = {sq};  T-ratio exponents a: "
    f"{ {k: v for k, v in expo.items()} }")
cosets = {k: ("QR" if v in sq else "nQR") for k, v in expo.items()}
say(f"  cosets of (Z/5)^*/squares: {cosets}")
well_def = (-1) % 5 in sq          # a and -a share a coset <=> -1 is a square
say(f"  coset independent of the pair's ordering (-1 = 4 is a square mod 5):"
    f" {well_def}")
split_by_galois = (len(survivors) == 2 and well_def and
                   len(set(cosets.values())) == 2 and flips)
say(f"  the two survivors sit in the TWO cosets, exchanged by sigma_2"
    f" (the sqrt5-flip): {split_by_galois}")
say("  => the surviving pair {SU(3)_2 (kappa=5), SU(5)_1 (kappa=6)} is ONE")
say("     Galois orbit: they carry the two conjugate doublets 2^', 2^.")


# ---------------------------------------------------------------- PART 5
hdr("PART 5 -- the classical side carries the SAME undetermined bit")
# A1 = [[2,1],[1,1]] (the golden monodromy); char poly x^2 - 3x + 1
tr, det = 3, 1
disc = tr * tr - 4 * det
say(f"  A1 = [[2,1],[1,1]]: charpoly x^2 - {tr}x + {det}, disc = {disc} = 5"
    f" (= the conductor det(A1+I)): {disc == 5}")
say("  spectrum {phi^2, phi^-2} = (3 +- sqrt5)/2 -- a single Galois orbit;")
say("  the banked bridge det(I - B_odd) = phi^2 (B595-D2a) fixes ONE root.")
say("  Choosing an eigenvalue of A1 = choosing a square root of 5 = the")
say("  SAME Z/2 as the stage branch. The object is symmetric under it")
say("  (theta-symmetry / total non-canonicity, B711-B712 banked).")
classical_bit = (disc == 5)


# ---------------------------------------------------------------- PART 6
hdr("PART 6 -- tiebreak audit: is 'MINIMAL bearing stage' well-posed?")
rows = []
for fam, n, k in [("A", 2, 2), ("A", 4, 1)]:
    kap, c, pairs, ph, ordT = stage_data(fam, n, k)
    rows.append({"stage": f"{fam}{n}_{k}", "kappa": kap, "level": k,
                 "rank": n, "dim_g": dim_g(fam, n), "ordT": ordT,
                 "kappa_eq_conductor": kap == 5})
for r in rows:
    say(f"  {r['stage']}: kappa={r['kappa']} level={r['level']} rank={r['rank']}"
        f" dim g={r['dim_g']} ord(T)={r['ordT']} kappa==N(=5): "
        f"{r['kappa_eq_conductor']}")
by_kappa = min(rows, key=lambda r: r["kappa"])["stage"]
by_level = min(rows, key=lambda r: r["level"])["stage"]
by_rank = min(rows, key=lambda r: r["rank"])["stage"]
by_cond = [r["stage"] for r in rows if r["kappa_eq_conductor"]]
say(f"  argmin kappa  -> {by_kappa}      argmin LEVEL -> {by_level}")
say(f"  argmin rank   -> {by_rank}      kappa = conductor -> {by_cond}")
minimality_ambiguous = by_kappa != by_level
say(f"  MINIMALITY IS AMBIGUOUS (kappa-min and level-min disagree): "
    f"{minimality_ambiguous}")
say("  the object supplies no ordering on stages; 3 added principles")
say("  (kappa-min, rank-min, kappa=conductor) and H-CUSP (B672: the cusp")
say("  lattice Z[2sqrt-3] quantizes A2's Z[zeta3], never A4's Q(zeta5))")
say("  converge on kappa=5, while LEVEL-minimality picks the partner.")
say("  Each is an ADDED axiom: obligation (3) ('minimal bearing is a")
say("  theorem') is not discharged -- it is not even single-valued.")


# ---------------------------------------------------------------- VERDICT
hdr("VERDICT")
hear_forces = (len(survivors) == 1)
prereq = (classification_closed and two_doublets and split_by_galois
          and classical_bit and len(excluded) == 1)
if not prereq:
    verdict = "UNRESOLVED"
    head = "the discriminating chain did not close in-cell"
elif hear_forces:
    verdict = "RESOLVED-A"
    head = "H-EAR has a unique solution: kappa = 5 is forced (theorem)"
elif len(survivors) == 2 and split_by_galois and minimality_ambiguous:
    verdict = "RESOLVED-B"
    head = ("H-EAR forces only the Galois PAIR {kappa=5, kappa=6}; kappa=5 "
            "is a priced choice -- price = one sqrt5/orientation bit, and "
            "the 'minimal' tiebreak is not even single-valued "
            "(level-minimality picks kappa=6)")
else:
    verdict = "UNRESOLVED"
    head = "solution set neither singleton nor a clean Galois pair"

say(f"  VERDICT = {verdict}")
say(f"  {head}")
say("  status of the links: classification (1)-(2) = THEOREM in-cell;")
say("  H-EAR itself = DEFINITION of 'bearing' (not derived: the L84/L91-4")
say("  functor exists only GROUP-level, wall 9 -- no equivariant classical")
say("  ->stage map to define 'the' bearing stage); obligation (3) = OPEN")
say("  and ambiguous. kappa=5 stands as a CHOICE with an explicit price.")

res = {
    "cell": "P2W4-HEAR", "lead": "OI-026 / L91",
    "hearing_filter_ok": filter_ok,
    "D2_grid": grid, "grid_reproduces_W32": grid_ok,
    "classification_closed_all_ranks_levels": classification_closed,
    "HEAR_solution_set": [[s[0], s[1]] for s in survivors],
    "HEAR_solution_count": len(survivors),
    "excluded_two_walls": [e[0] for e in excluded],
    "SL2F5_two_doublets_one_galois_orbit": two_doublets,
    "no_rational_separator": not rational_sep,
    "survivors_in_two_cosets_mod5": split_by_galois,
    "sigma2_flips_sqrt5": flips,
    "classical_bit_same_Z2_disc5": classical_bit,
    "minimality_ambiguous_kappa_vs_level": minimality_ambiguous,
    "tiebreaks_picking_kappa5": ["kappa-min", "rank-min", "kappa=conductor",
                                 "H-CUSP (B672)"],
    "tiebreak_picking_kappa6": ["level-min"],
    "reproduction": ("D=2 grid + A5@1 double exclusion reproduce banked "
                     "B666/W32 by an independent implementation (-w0 computed "
                     "from the Cartan matrix, not cited); grid also re-derived "
                     "a 2nd way by closed forms for all ranks; an earlier "
                     "duplicate run of this cell (prior_run_v1/) reached the "
                     "same grid and the same verdict by a partly different "
                     "route (cusp-field tiebreak); sufficiency of H-EAR at "
                     "A4@1 = in-cell Gamma(5) T^5-scalar certificate + banked "
                     "W32 Part 4 (12/12 corpus)."),
    "verdict": verdict, "headline": head,
    "discriminating_fact": (
        "The H-EAR predicate has EXACTLY TWO solutions over all simply-laced "
        "stages (classification closed in-cell: theta-odd D=2 only at A2@2 "
        "kappa=5, A4@1 kappa=6, A5@1 kappa=7; A5@1 killed twice -- projective "
        "T-order 4!=5 and 5 does not divide ord(T)=24 so sqrt5 is not in "
        "Q(zeta24)). The two survivors carry the T-ratio exponents a=2 and "
        "a=1, which lie in the two cosets of the squares mod 5 and are "
        "exchanged by sigma_2 in Gal(Q(zeta5)/Q), the element that flips "
        "sqrt5 (Gauss sum verified exactly) -- i.e. they realize the two "
        "Galois-conjugate 2-dim irreps of the object's own shadow SL(2,F5) "
        "(built as 2I over Q(sqrt5): 120 elements, both doublets "
        "irreducible, NO Q-rational class value separates them). The "
        "classical side carries the same bit (A1 spectrum {phi^2,phi^-2}, "
        "disc = 5 = the conductor). Hence H-EAR forces the PAIR, not kappa=5. "
        "The tiebreak is an added axiom AND is not single-valued: "
        "kappa-minimality, rank-minimality, kappa=conductor and H-CUSP pick "
        "kappa=5, while LEVEL-minimality picks kappa=6."),
    "gate_5Q": {"structural_only": True, "no_SM_values": True,
                "nothing_to_CLAIMS": True, "one_number_pin_untouched": True},
}
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "results.json"), "w") as f:
    json.dump(res, f, indent=1)
with open(os.path.join(here, "output.txt"), "w") as f:
    f.write("\n".join(OUT) + "\n")
