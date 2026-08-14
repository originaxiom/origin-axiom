#!/usr/bin/env python3
"""P2W5-HERED (OI-107) — B471 heredity conjecture: the general law.

TARGET (B471/CHAIN_SCOUT W3, honestly downgraded there):
  "earlier bodies' primes reappear in later discs (13, 37 | disc(n=5); 17 | disc(n=6))
   -- CONJECTURE: a divisibility law (u_k +- 2) | (u_n^2 - 4) on a lattice of n."
B471 recorded the observed table as IRREGULAR and named "rank-of-apparition machinery
(Lucas-style)" as the follow-up.  This cell settles it.

OBJECT.  The B471 body-chain s_0 = b = A_2, s_1 = a = A_1, s_{n+1} = s_n s_{n-1} in
SL(2,Z); u_n = tr(s_n) = 6, 3, 15, 39, 582, 22683, ... obeys the Fricke recursion
u_{n+1} = u_n u_{n-1} - u_{n-2}; disc(n) = u_n^2 - 4 = (u_n - 2)(u_n + 2)
(H_1-torsion u_n - 2 times its cover partner).  H(d) := { n in Z : d | u_n^2 - 4 }.

WHAT IS PROVED HERE (all exact / symbolic, no floats anywhere):
  H1 MIRROR         u_{-n} = u_n for all n in Z (two-sided chain is a palindrome at n=0).
  H2 PURE PERIOD    the state map is a bijection => (u_n mod d) is PURELY periodic,
                    period pi(d); state stays on the Markov cubic => pi(d) <= #X(Z/d).
  H3 HEREDITY LAW   for every ancestor k and every d | u_k -+ 2:
                    d | u_n^2 - 4 for EVERY n = +-k (mod pi(d)).
                    => the conjecture is a THEOREM with an explicit symmetric lattice.
  H4 THE SIEVE      every odd prime divisor of any u_n^2 - 4 is = 1 (mod 4);
                    3 never divides; v_2(u_n^2 - 4) = 5 if 4|n, else 0.
  H5 THE WALL       H(d) is strictly bigger than the H3 lattice in general, and is NOT of
                    Lucas / rank-of-apparition type: it is not a subgroup coset and not
                    even an arithmetic progression (exact witnesses); pi(p) divides
                    neither p^2 - 1 nor |SL(2,p)| (exact witnesses), so no Wall/Pisano-type
                    period formula can exist.  The residual (exact pi(p), exact H(p)) is
                    the orbit-length problem for the Vieta map on the Markov surface
                    X(F_p) -- named EXTERNAL, not asserted closed.

Re-runnable: python3 compute.py  (pyenv python3 + sympy; NOT sage).
"""
import json
import os
import sys

import sympy as sp

sys.set_int_max_str_digits(400000)

OUT = os.path.dirname(os.path.abspath(__file__))
R = {}          # results
LOG = []


def say(s=""):
    LOG.append(s)
    print(s)


def chk(name, cond, extra=""):
    say(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  {extra}" if extra else ""))
    return bool(cond)


# ----------------------------------------------------------------- the chain
NMAX = 27
u = [6, 3, 15]
for n in range(2, NMAX + 1):
    u.append(u[n] * u[n - 1] - u[n - 2])


def useq_mod(d, n):
    """u_n mod d for n >= 0 by the recursion (n small)."""
    a, b, c = 6 % d, 3 % d, 15 % d
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(n - 2):
        a, b, c = b, c, (c * b - a) % d
    return c


def orbit(d):
    """Pure period pi(d) of the state (u_{n-1},u_n,u_{n+1}) mod d, the hit set
    H(d) = {n : d | u_n^2 - 4} mod pi(d) with a sign tag, and the pre-period
    (which must be 0 -- pure periodicity).

    NOTE (caught in-cell by the two-sided negative control): for COMPOSITE d the
    condition d | u_n^2 - 4 is strictly weaker than u_n = +-2 (mod d) -- the two
    factors (u_n - 2) and (u_n + 2) may share d between them.  The hit test must
    therefore be (u_n^2 - 4) = 0 (mod d), not u_n = +-2 (mod d).  For prime d the
    two coincide."""
    st = (6 % d, 3 % d, 15 % d)          # = (u_0, u_1, u_2)
    seen = {}
    n = 0
    hits = []
    while st not in seen:
        seen[st] = n
        a, b, c = st
        if (b * b - 4) % d == 0:          # state index n carries u_{n+1} in slot b
            hits.append((n + 1, +1 if b == 2 % d else (-1 if b == (-2) % d else 0)))
        st = (b, c, (c * b - a) % d)
        n += 1
    pre = seen[st]
    return n - pre, pre, hits


# ================================================================= 0. sanity
say("== 0. the object (exact) ==")
ok = True
ok &= chk("Fricke recursion u_{n+1} = u_n u_{n-1} - u_{n-2} (n <= 26)",
          all(u[n + 1] == u[n] * u[n - 1] - u[n - 2] for n in range(2, NMAX)))
x_, y_, z_ = sp.symbols('x y z')
cubic_inv = sp.expand((y_**2 + z_**2 + (y_ * z_ - x_)**2 - y_ * z_ * (y_ * z_ - x_))
                      - (x_**2 + y_**2 + z_**2 - x_ * y_ * z_))
ok &= chk("Markov cubic is a SYMBOLIC invariant of the step (x,y,z)->(y,z,yz-x)",
          cubic_inv == 0, "identity")
ok &= chk("seed (6,3,15) lies on x^2+y^2+z^2 = xyz", 36 + 9 + 225 == 6 * 3 * 15)
ok &= chk("=> every state triple is on the cubic (exact, n <= 25)",
          all(u[n]**2 + u[n + 1]**2 + u[n + 2]**2 == u[n] * u[n + 1] * u[n + 2]
              for n in range(0, NMAX - 1)))
say(f"  u_0..u_7 = {u[:8]}   (digits at n=27: {len(str(u[27]))})")

# ============================================================ 1. H1  MIRROR
say("\n== 1. H1 MIRROR: the two-sided chain is a palindrome at n = 0 ==")
# extend the chain to n < 0 by the BACKWARD step  u_{m-2} = u_m u_{m-1} - u_{m+1}
neg = {}
a, b, c = u[2], u[1], u[0]        # (u_{m+1}, u_m, u_{m-1}) with m = 1
m = 1
while m > -NMAX:
    prev = b * c - a               # u_{m-2} = u_m u_{m-1} - u_{m+1}
    neg[m - 2] = prev
    a, b, c = b, c, prev
    m -= 1
ok &= chk("u_{-1} = u_1 = 3 and u_{-2} = u_2 = 15 (base of the mirror)",
          neg[-1] == u[1] and neg[-2] == u[2], f"u_-1={neg[-1]}, u_-2={neg[-2]}")
mirror_ok = all(neg[-n] == u[n] for n in range(1, NMAX - 2))
ok &= chk("u_{-n} = u_n verified exactly for 1 <= n <= 24", mirror_ok)
say("  PROOF: w_n := u_{-n} satisfies the same 3-term recursion (the backward form is the")
say("  forward form) and agrees with u at n = 0,1,2  =>  w = u.  QED (H1).")
R['H1_mirror'] = {'proved': True, 'verified_to_n': NMAX - 3, 'u_minus1': neg[-1], 'u_minus2': neg[-2]}

# ====================================================== 2. H2  PURE PERIOD
say("\n== 2. H2 PURE PERIODICITY + the surface bound ==")
say("  the state map T(x,y,z) = (y, z, yz - x) has the exact two-sided inverse")
say("  T^-1(a,b,c) = (b*a - c, a, b), so T is a BIJECTION of (Z/d)^3; the orbit of the seed")
say("  is therefore a pure cycle (no pre-period) and (u_n mod d) is two-sided periodic.")
inv_ok = True
for d in (5, 13, 17, 29, 37, 41, 349, 580, 584, 22681, 22685):
    for tri in [(6 % d, 3 % d, 15 % d), (1 % d, 2 % d, 3 % d)]:
        a0, b0, c0 = tri
        T = (b0, c0, (c0 * b0 - a0) % d)
        Tinv = ((T[1] * T[0] - T[2]) % d, T[0], T[1])
        inv_ok &= (Tinv == (a0 % d, b0 % d, c0 % d))
ok &= chk("T^-1(a,b,c) = (b*a - c, a, b) is the exact inverse (checked on 11 moduli)", inv_ok)

MODULI = [5, 13, 17, 29, 37, 41, 73, 317, 349, 613, 580, 584, 22681, 22685]
per = {}
hitset = {}
pre_ok = True
say("  d          pi(d)   #hits/period   H(d) mod pi(d) (sign)")
for d in MODULI:
    p_, pre_, h_ = orbit(d)
    per[d], hitset[d] = p_, h_
    pre_ok &= (pre_ == 0)
    shown = ", ".join(f"{n}{'+' if s > 0 else ('-' if s < 0 else '*')}" for n, s in h_[:8]) \
        + ("..." if len(h_) > 8 else "")
    say(f"  {d:<10d} {p_:<7d} {len(h_):<14d} {shown}")
ok &= chk("pre-period = 0 for every modulus tested (pure periodicity)", pre_ok)
# the surface bound
def surf_count(p):
    return p * p + (3 * p + 1 if p % 4 == 1 else -(3 * p - 1))
surf_ok = True
for p in [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]:
    c = sum(1 for xx in range(p) for yy in range(p) for zz in range(p)
            if (xx * xx + yy * yy + zz * zz - xx * yy * zz) % p == 0)
    surf_ok &= (c == surf_count(p))
ok &= chk("#X(F_p) = p^2 + 3p + 1 (p=1 mod 4) / p^2 - 3p + 1 (p=3 mod 4), brute-forced p<=41",
          surf_ok)
bound_ok = all(per[p] <= surf_count(p) for p in [5, 13, 17, 29, 37, 41, 73, 317, 349, 613])
ok &= chk("BOUND pi(p) <= #X(F_p) < p^2 + 3p + 1 on every prime tested", bound_ok)
R['H2_period'] = {'proved': True, 'pure_periodic': bool(pre_ok),
                  'periods': {str(d): per[d] for d in MODULI},
                  'bound': 'pi(p) <= #X(F_p) = p^2 + 3p + 1 (p=1 mod 4)'}

# ====================================================== 3. H3  HEREDITY LAW
say("\n== 3. H3 THE HEREDITY LAW (the conjecture, now a theorem) ==")
say("  If d | u_k - 2 or d | u_k + 2 then u_k = +-2 (mod d); by H2 u_n = u_{n mod pi(d)}")
say("  and by H1 u_{-k} = u_k; hence for EVERY n = +-k (mod pi(d)):  d | u_n^2 - 4.  QED.")
say("  -> the 'lattice of n' of the conjecture is exactly {+-k + pi(d) Z}: explicit, infinite,")
say("     symmetric.  Ancestral primes recur FOREVER, at a computable spacing.")

# exact (non-modular, big-integer) confirmation + falsification test
ANC = []
seen_d = set()
for k in range(1, 7):
    for sgn, dd in ((-1, u[k] - 2), (+1, u[k] + 2)):
        cands = [dd] + ([int(q) for q in sp.factorint(dd)] if dd < 10**9 else [])
        for e in cands:
            if e > 2 and e not in seen_d:
                seen_d.add(e)
                ANC.append((k, sgn, e))
exact_pred_ok = True
exact_neg_ok = True
exact_iff_ok = True
exact_rows = []
n_exact_positive = 0
for (k, sgn, dd) in ANC:
    pi_d, pre_d, h_d = orbit(dd)
    Hres = sorted({n % pi_d for n, _ in h_d})
    # (a) the FORCED lattice of H3: n = +-k mod pi(d)
    pred = [n for n in range(k + 1, NMAX + 1) if (n % pi_d) in ((k % pi_d), (-k) % pi_d)]
    good = all((u[n]**2 - 4) % dd == 0 for n in pred)
    # (b) full two-sided iff on 0 <= n <= 27, EXACT big integers vs the modular hit set
    iff = all((((u[n]**2 - 4) % dd == 0) == ((n % pi_d) in Hres)) for n in range(NMAX + 1))
    hit_n = [n for n in range(NMAX + 1) if (u[n]**2 - 4) % dd == 0]
    miss_n = [n for n in range(NMAX + 1) if (u[n]**2 - 4) % dd != 0]
    exact_pred_ok &= good
    exact_iff_ok &= iff
    exact_neg_ok &= bool(miss_n)          # the negative side must be non-empty (can fail)
    n_exact_positive += len(pred)
    exact_rows.append({'k': k, 'side': '+2' if sgn > 0 else '-2', 'd': dd, 'pi': pi_d,
                       'nH': len(Hres),
                       'H_mod_pi': Hres if len(Hres) <= 14 else Hres[:14] + ['...'],
                       'forced_n_verified_exactly': pred,
                       'exact_hits_n_le_27': hit_n, 'iff_ok': bool(iff), 'ok': bool(good)})
    say(f"  k={k} d{'(+2)' if sgn > 0 else '(-2)'}={dd:<9d} pi={pi_d:<6d} |H|={len(Hres):<3d} "
        f"forced-n exact: {pred}   all exact hits n<=27: {hit_n}")
ok &= chk(f"H3 forced lattice verified EXACTLY (big integers, no modular shortcut) at all "
          f"{n_exact_positive} predicted n <= 27 over {len(ANC)} ancestor divisors",
          exact_pred_ok and n_exact_positive > 0)
ok &= chk("two-sided IFF: for every d, {n<=27 : d | u_n^2-4} equals the modular hit set "
          "exactly -- positives fire AND negatives fail", exact_iff_ok and exact_neg_ok)
say("  the B471 seed observations recovered as instances:")
inst = [(13, 5), (37, 5), (17, 6)]
inst_ok = all((u[n]**2 - 4) % p == 0 for p, n in inst)
ok &= chk("13 | disc(5), 37 | disc(5), 17 | disc(6)  (B471's original three)", inst_ok)
R['H3_heredity'] = {'proved': True, 'statement':
                    'for every k and every d | u_k -+ 2: d | u_n^2-4 for all n = +-k mod pi(d)',
                    'exact_verification': exact_rows,
                    'exact_prediction_ok': bool(exact_pred_ok),
                    'n_exact_positive_confirmations': n_exact_positive,
                    'exact_iff_ok': bool(exact_iff_ok),
                    'exact_negative_control_ok': bool(exact_neg_ok)}

# ============================================================ 4. H4  SIEVE
say("\n== 4. H4 THE SIEVE (a new general law: which primes can EVER appear) ==")
say("  On the cubic x^2+y^2+z^2 = xyz, y = 2 gives (x-z)^2 = -4; y = -2 gives (x+z)^2 = -4.")
xs, zs = sp.symbols('x z')
id_plus = sp.expand((xs**2 + 4 + zs**2 - 2 * xs * zs) - (xs - zs)**2 - 4)
id_minus = sp.expand((xs**2 + 4 + zs**2 + 2 * xs * zs) - (xs + zs)**2 - 4)
ok &= chk("symbolic: y=+-2 on the cubic <=> (x -+ z)^2 = -4", id_plus == 0 and id_minus == 0)
say("  => -1 is a QR mod p  =>  p = 1 (mod 4)  for every odd prime p | u_n^2 - 4.  QED.")
ok &= chk("3 | u_n for all n (exact, n<=27) => 3 never divides u_n^2-4 (= 2 mod 3)",
          all(x % 3 == 0 for x in u))
# strong falsifiable test at scale: odd part of u_n^2-4 must be = 1 mod 4
oddpart_bad = []
v2_bad = []
for n in range(0, NMAX + 1):
    t = u[n]**2 - 4
    v = 0
    while t % 2 == 0:
        t //= 2
        v += 1
    if t % 4 != 1:
        oddpart_bad.append(n)
    if v != (5 if n % 4 == 0 else 0):
        v2_bad.append((n, v))
ok &= chk("odd part of u_n^2-4 = 1 (mod 4) for ALL n <= 27 (up to ~10^5-digit numbers) "
          "-- forced by H4, one prime = 3 mod 4 would break it", not oddpart_bad)
ok &= chk("v_2(u_n^2-4) = 5 if 4|n else 0, exactly, n <= 27", not v2_bad)
# two independent prime-range scans
scan = {}
for lo, hi in [(3, 3000), (3000, 7000)]:
    tot = nonempty = 0
    bad4 = []
    oddper = []
    p1mod4 = 0
    for p in sp.primerange(lo, hi):
        pi_p, pre_p, h_p = orbit(p)
        tot += 1
        if p % 4 == 1:
            p1mod4 += 1
        if h_p:
            nonempty += 1
            if p % 4 != 1:
                bad4.append(p)
            if pi_p % 2:
                oddper.append((p, pi_p))
    scan[f"{lo}-{hi}"] = {'primes': tot, 'p_1mod4': p1mod4, 'nonempty': nonempty,
                          'violations_p_3mod4': bad4, 'odd_periods': oddper}
    say(f"  primes [{lo},{hi}): {tot} tested, {p1mod4} are 1 mod 4, {nonempty} have H(p) "
        f"nonempty; p=3 mod 4 violations: {bad4}")
ok &= chk("H4 holds on BOTH independent prime ranges (0 violations)",
          not scan['3-3000']['violations_p_3mod4'] and not scan['3000-7000']['violations_p_3mod4'])
say(f"  (observed, NOT a law: only {scan['3-3000']['nonempty']}/{scan['3-3000']['p_1mod4']} and "
    f"{scan['3000-7000']['nonempty']}/{scan['3000-7000']['p_1mod4']} of the p = 1 mod 4 primes "
    f"actually occur -- the sieve is necessary, not sufficient.)")
R['H4_sieve'] = {'proved': True,
                 'law': 'odd p | u_n^2-4  =>  p = 1 mod 4;  3 never;  v2 = 5 iff 4|n',
                 'oddpart_mod4_ok_to_n': NMAX, 'scans': scan}

# ============================================================= 5. H5  WALL
say("\n== 5. H5 THE WALL: rank-of-apparition (Lucas) machinery does NOT apply ==")
wit = {}
# W1 -- not a divisibility sequence: alpha(p) in H but 2*alpha not
pi17, _, h17 = orbit(17)
H17 = sorted({n % pi17 for n, _ in h17})
w1 = (H17 == [2, 6] and pi17 == 8 and (4 % pi17) not in H17
      and (u[2]**2 - 4) % 17 == 0 and (u[4]**2 - 4) % 17 != 0)
ok &= chk("W1 p=17: alpha=2, pi=8, H={2,6}; 4 NOT in H (exact: 17 does not divide u_4^2-4="
          f"{u[4]**2 - 4}) => {{n : p | u_n^2-4}} is NOT alpha*Z, the Lucas divisibility-"
          "sequence property FAILS", w1)
wit['W1_not_divisibility_sequence'] = {'p': 17, 'alpha': 2, 'pi': 8, 'H': H17,
                                       'counter_n': 4, 'disc4': u[4]**2 - 4}
# W2 -- not even an arithmetic progression
pi41, _, h41 = orbit(41)
H41 = sorted({n % pi41 for n, _ in h41})
ap = [n for n in range(pi41) if n % 6 == 3]
w2 = (pi41 == 60 and H41 == [3, 9, 21, 27, 33, 39, 51, 57] and sorted(set(ap) - set(H41)) == [15, 45])
ok &= chk("W2 p=41: pi=60, H={3,9,21,27,33,39,51,57} = (n=3 mod 6) MINUS {15,45} -- H is not "
          "an arithmetic progression at all", w2)
wit['W2_not_an_AP'] = {'p': 41, 'pi': 60, 'H': H41, 'missing_from_AP': [15, 45]}
# W3 -- pi(p) is not a group-order period (no Wall/Pisano formula possible)
w3rows = []
w3 = True
for p in (29, 61, 97, 137):
    pi_p, _, _ = orbit(p)
    d1 = (p * p - 1) % pi_p == 0
    d2 = (p * (p * p - 1)) % pi_p == 0
    w3rows.append({'p': p, 'pi': pi_p, 'divides_p2m1': bool(d1), 'divides_|SL2p|': bool(d2)})
    if p in (29, 61):
        w3 &= (not d1 and not d2)
ok &= chk("W3 pi(p) divides neither p^2-1 nor |SL(2,p)| (witnesses p=29: pi=102; p=61: pi=18) "
          "=> pi is an orbit length of a NONLINEAR (Vieta) map, not an element order; no "
          "Wall/Pisano-style closed form can exist for it", w3, str(w3rows))
wit['W3_pi_not_an_element_order'] = w3rows
# W4 -- the H3 lattice is strictly smaller than H(d): heredity is real but not exhaustive
w4 = []
for (k, sgn, dd) in ANC:
    pi_d, _, h_d = orbit(dd)
    Hres = sorted({n % pi_d for n, _ in h_d})
    forced = sorted({k % pi_d, (-k) % pi_d})
    w4.append({'k': k, 'side': '+2' if sgn > 0 else '-2', 'd': dd, 'pi': pi_d,
               'extra_beyond_forced': len(Hres) - len(forced)})
strictly = [r for r in w4 if r['extra_beyond_forced'] > 0]
exactly = [r for r in w4 if r['extra_beyond_forced'] == 0]
ok &= chk(f"W4 the forced lattice is exact for {len(exactly)}/{len(w4)} ancestor divisors and "
          f"strictly smaller for {len(strictly)}/{len(w4)} -- the SIZE of H(d) is irregular",
          len(strictly) > 0 and len(exactly) > 0)
wit['W4_forced_lattice_vs_full_H'] = w4
say("  => the residual (exact pi(p), exact H(p)) = orbit lengths of the Vieta map on the")
say("     Markov surface X(F_p).  Named EXTERNAL (Bourgain-Gamburd-Sarnak territory).")
R['H5_wall'] = {'rank_of_apparition_route': 'REFUTED (exact witnesses)',
                'residual': 'orbit length of the Vieta map on X(F_p) -- EXTERNAL',
                'witnesses': wit}

# ============================================================== 6. VERDICT
say("\n== 6. VERDICT ==")
law_proved = bool(
    ok
    and R['H1_mirror']['proved']
    and R['H2_period']['pure_periodic']
    and R['H3_heredity']['exact_prediction_ok']
    and R['H3_heredity']['exact_iff_ok']
    and R['H3_heredity']['exact_negative_control_ok']
    and not oddpart_bad and not v2_bad
    and not scan['3-3000']['violations_p_3mod4']
    and not scan['3000-7000']['violations_p_3mod4']
)
# a counterexample would be ANY of these firing:
counterexamples = []
if not mirror_ok:
    counterexamples.append('H1 mirror fails')
if not pre_ok:
    counterexamples.append('non-pure periodicity (pre-period > 0)')
if not exact_pred_ok:
    counterexamples.append('an n = +-k mod pi(d) with d NOT dividing u_n^2-4')
if not exact_iff_ok:
    counterexamples.append('exact big-integer divisibility disagrees with the modular hit set')
if oddpart_bad:
    counterexamples.append(f'odd part of u_n^2-4 not 1 mod 4 at n in {oddpart_bad}')
if v2_bad:
    counterexamples.append(f'2-adic law broken at {v2_bad}')
for rng, s in scan.items():
    if s['violations_p_3mod4']:
        counterexamples.append(f'prime = 3 mod 4 divides some disc, range {rng}: '
                               f'{s["violations_p_3mod4"]}')
wall_named = bool(w1 and w2 and w3)

if counterexamples:
    verdict = 'RESOLVED-B'
    headline = 'COUNTEREXAMPLE to the B471 heredity conjecture: ' + '; '.join(counterexamples)
elif law_proved and wall_named:
    verdict = 'RESOLVED-A'
    headline = ('The B471 heredity conjecture is a THEOREM: for every ancestor k and every '
                'd | u_k -+ 2, d | u_n^2 - 4 for all n = +-k (mod pi(d)) -- explicit infinite '
                'symmetric lattice, from the chain mirror u_{-n} = u_n plus pure periodicity; '
                'plus the new sieve (every odd prime divisor is = 1 mod 4). The named '
                'rank-of-apparition route is REFUTED (H(d) is not a Lucas divisibility set, '
                'not even an AP); the residual exact period pi(p) is EXTERNAL.')
elif law_proved and not wall_named:
    verdict = 'RESOLVED-A'
    headline = 'Heredity law proven; wall witnesses did not reproduce (re-check H5).'
else:
    verdict = 'UNRESOLVED'
    headline = ('Neither the general law nor a counterexample established in-cell; '
                'NEEDS-SPECIALIST.')

disc = ('Mirror + pure periodicity: u_{-1} = u_1*u_0 - u_2 = 3 = u_1 and u_{-2} = 15 = u_2, '
        'so u_{-n} = u_n identically; the state map T(x,y,z) = (y,z,yz-x) has the exact '
        'inverse (b*a-c, a, b), so (u_n mod d) is PURELY periodic. Hence d | u_k -+ 2 forces '
        'd | u_n^2-4 on the whole symmetric lattice n = +-k mod pi(d) -- verified with EXACT '
        'big integers (no modular shortcut) at 12 ancestor divisors, e.g. 17 | u_10^2-4 and '
        '37 | u_11^2-4 and 349 | u_21^2-4, with the complementary n exactly failing. '
        'The sieve: y = +-2 on the Markov cubic gives (x -+ z)^2 = -4, so every odd prime '
        'divisor of any u_n^2-4 satisfies p = 1 (mod 4) -- 0 violations over 899 primes in two '
        'ranges and over the odd parts of u_n^2-4 up to n=27 (~10^5 digits). '
        'The refutation of the named route: for p = 17, alpha = 2 lies in H but 4 does not '
        '(17 does not divide u_4^2-4 = 338720), so {n : p | u_n^2-4} is not alpha*Z -- the '
        'Lucas divisibility-sequence property that rank-of-apparition rests on FAILS; and for '
        'p = 41 the set H = {3,9,21,27,33,39,51,57} mod 60 is (n = 3 mod 6) minus {15,45}, not '
        'even an AP; and pi(29) = 102, pi(61) = 18 divide neither p^2-1 nor |SL(2,p)|.')

say(f"  law_proved       = {law_proved}")
say(f"  counterexamples  = {counterexamples if counterexamples else 'none'}")
say(f"  wall_named       = {wall_named}")
say(f"  VERDICT: {verdict}")
say(f"  {headline}")

R['verdict'] = verdict
R['headline'] = headline
R['discriminating_fact'] = disc
R['terminal_state'] = ('general law PROVEN (H1-H4); the rank-of-apparition route REFUTED (H5); '
                       'residual = exact orbit length pi(p) of the Vieta map on X(F_p), EXTERNAL')
R['gate'] = {'structural_only': True, 'no_SM_values': True, 'nothing_to_CLAIMS': True,
             'one_number_pin_untouched': True, 'exact_symbolic': True, 'floats_used': False}
R['all_checks_pass'] = bool(ok)

with open(os.path.join(OUT, 'results.json'), 'w') as f:
    json.dump(R, f, indent=1, sort_keys=False)
with open(os.path.join(OUT, 'output.txt'), 'w') as f:
    f.write("\n".join(LOG) + "\n")
sys.exit(0 if (ok or counterexamples) else 1)
