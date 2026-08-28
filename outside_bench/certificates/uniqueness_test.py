#!/usr/bin/env python3
"""MEMO-116 CELL (the owner's GO): THE UNIQUENESS TEST FOR A5 — is the
shadow-pairing predicate the ONLY admissible one, or merely AN
admissible one?  Memo 115 showed Occ(X) := [X, gal X] != 0 clears the
preregistered gates C1-C4.  Admissible is not correct.  This cell
looks for COMPETITORS.

THE DESIGN (preregistered, and deliberately hostile to A5): enumerate
a family of candidate predicates, each definable from BANKED structure
with no imported premise (so each automatically satisfies C1 and C3),
then:
  U1: gate every candidate on C2 (selects a PROPER, NONEMPTY subset).
  U2: partition the survivors into EQUIVALENCE CLASSES by the set they
      select.  The number of distinct admissible sets is the answer:
      1 => A5 is forced at this gate level; >1 => A5 is admissible but
      NOT unique, and the gates C1-C4 are too weak as designed.
  U3: THE HONEST CONSEQUENCE.  If competitors exist, propose and TEST
      the natural strengthening — a gate the record itself motivates
      rather than one chosen to save A5.  The candidate: C5 STABILITY
      UNDER THE RECORD'S OWN AUTOMORPHISM (memo 108's word map phi),
      since memo 106 established that the observer's datum epsilon is
      conjugation-invariant — a predicate that moves under the
      record's own relabelling is frame-dependent and cannot be a
      criterion for occupation.
  U4: report which candidates survive C5, and the resulting verdict.
PREREGISTERED EXPECTATION (stated before running, so the outcome
cannot be spun): the bench EXPECTS competitors to exist, i.e. expects
A5 to be non-unique at C1-C4 level, because those gates are weak.  A
finding of uniqueness would be a surprise and would strengthen A5
sharply; a finding of non-uniqueness refutes the GATES, not the
hypothesis, and hands us C5 as the real work.
Gate 5 untouched.  H5 firewall observed.
"""
# ---- exact integer pair arithmetic over Z[omega]
def padd(u, v): return (u[0] + v[0], u[1] + v[1])
def psub(u, v): return (u[0] - v[0], u[1] - v[1])
def pmul(u, v):
    a, b = u; c, d = v
    return (a*c - b*d, a*d + b*c + b*d)
def pgal(u): return (u[0] + u[1], -u[1])
Z, O, W = (0, 0), (1, 0), (0, 1)
def mmul(P, Q):
    return ((padd(pmul(P[0][0], Q[0][0]), pmul(P[0][1], Q[1][0])),
             padd(pmul(P[0][0], Q[0][1]), pmul(P[0][1], Q[1][1]))),
            (padd(pmul(P[1][0], Q[0][0]), pmul(P[1][1], Q[1][0])),
             padd(pmul(P[1][0], Q[0][1]), pmul(P[1][1], Q[1][1]))))
def msub(P, Q):
    return tuple(tuple(psub(P[i][j], Q[i][j]) for j in range(2)) for i in range(2))
def mgal(P): return tuple(tuple(pgal(P[i][j]) for j in range(2)) for i in range(2))
def mtr(P): return padd(P[0][0], P[1][1])
ZM = ((Z, Z), (Z, Z))
MAT = {'a': ((O, O), (Z, O)), 'b': ((O, Z), ((0, -1), O)),
       'A': ((O, (-1, 0)), (Z, O)), 'B': ((O, Z), (W, O))}
INV = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
ID = ((O, Z), (Z, O))
def ev(w):
    M = ID
    for ch in w:
        M = mmul(M, MAT[ch])
    return M
assert mtr(ev("ab")) == (2, -1)
PHI = {'a': 'a', 'b': 'bAB', 'A': 'A', 'B': 'baB'}      # memo 108's word map
def phi(w): return "".join(PHI[c] for c in w)

# ---- the census
words = []
frontier = [""]
for L in range(7):
    nxt = []
    for w in frontier:
        for ch in "abAB":
            if w and INV[w[-1]] == ch:
                continue
            nxt.append(w + ch)
    words += nxt
    frontier = nxt
MX = {w: ev(w) for w in words}
SYS = ev("ab")

def fricke_s(X):
    G = mgal(X)
    x = mtr(X); y = pgal(x); z = mtr(mmul(X, G))
    t = padd(padd(pmul(x, x), pmul(y, y)), pmul(z, z))
    return psub(psub(t, pmul(pmul(x, y), z)), (2, 0))

# ---- the candidate family (each internal, each premise-free)
def P1(w, X): return msub(mmul(X, mgal(X)), mmul(mgal(X), X)) != ZM   # A5
def P2(w, X): return mtr(X) != pgal(mtr(X))                          # unlike its shadow
def P3(w, X): return P1(w, X) and P2(w, X)                           # memo 115's conjunction
def P4(w, X): return mtr(X) not in ((2, 0), (-2, 0))                 # non-parabolic
def P5(w, X): return msub(mmul(X, SYS), mmul(SYS, X)) != ZM          # non-commuting with the systole
def P6(w, X):                                                        # word-map shadow
    Y = ev(phi(w))
    return msub(mmul(X, Y), mmul(Y, X)) != ZM
def P7(w, X): return fricke_s(X) != (2, 0)                           # nondegenerate shadow-Fricke
def P8(w, X): return mtr(X)[1] != 0 or abs(mtr(X)[0]) > 2            # trace not a small integer
CANDS = [("P1 = A5: [X, gal X] != 0", P1), ("P2: tr X non-real (unlike shadow)", P2),
         ("P3 = P1 and P2 (memo 115's conjunction)", P3), ("P4: non-parabolic", P4),
         ("P5: doesn't commute with the systole", P5),
         ("P6: [X, rho(phi w)] != 0 (word-map shadow)", P6),
         ("P7: shadow-Fricke != 2", P7), ("P8: trace not a small integer", P8)]

# ---- U1/U2
tot = len(words)
sets = {}
print(f"U1/U2 — {len(CANDS)} premise-free candidates over {tot} classes (to length 7):\n")
print(f"    {'candidate':<44s} {'|set|':>6s}  C2?   equivalence")
rows = []
for name, P in CANDS:
    S = frozenset(w for w in words if P(w, MX[w]))
    c2 = 0 < len(S) < tot
    sets.setdefault(S, []).append(name)
    rows.append((name, S, c2))
for name, S, c2 in rows:
    tag = "PASS" if c2 else "fail"
    eq = "= " + sets[S][0] if sets[S][0] != name else "(new set)"
    print(f"    {name:<44s} {len(S):6d}  {tag}  {eq}")
admissible = {S: names for S, names in sets.items() if 0 < len(S) < tot}
print(f"\n    DISTINCT ADMISSIBLE SETS AT C1-C4: {len(admissible)}")
A5set = frozenset(w for w in words if P1(w, MX[w]))
competitors = [ (S, names) for S, names in admissible.items() if S != A5set ]
print(f"    COMPETITORS to A5 (admissible, inequivalent): {len(competitors)}")
for S, names in competitors:
    print(f"       |{len(S)}| via {names[0]}")

# ---- U3/U4: the C5 gate — stability under the record's own automorphism
print("\nU3/U4 — C5 (PROPOSED, **NOT FORCED** — see the honesty note below):")
print("    stability under the record's own automorphism phi (memo 108):")
print("    Occ(w) <=> Occ(phi w).  MOTIVATION: phi is an automorphism of the")
print("    record, so a criterion arguably should not distinguish classes the")
print("    record's own symmetry identifies.  HONESTY NOTE, stated before the")
print("    result: this gate is NOT derived.  It is not a corollary of memo 109")
print("    (the shadow predicate is anchoring-invariant either way, since")
print("    flipping sends [X, gal X] to its negative, still nonzero), and")
print("    adopting it would itself be an imported premise — the very failure")
print("    mode diagnosed in IIT.  It is tested here as a CANDIDATE gate, and")
print("    whatever it does to A5 must be read with that caveat.")
print(f"\n    {'candidate':<44s} {'C5':>6s}   first witness")
survivors = []
for name, P in CANDS:
    bad = None
    for w in words:
        X = MX[w]
        pw = phi(w)
        Y = ev(pw)
        if P(w, X) != P(pw, Y):
            bad = w
            break
    ok = bad is None
    S = frozenset(x for x in words if P(x, MX[x]))
    if ok and 0 < len(S) < tot:
        survivors.append((name, S))
    print(f"    {name:<44s} {'PASS' if ok else 'FAIL':>6s}   {'-' if ok else repr(bad)}")
surv_sets = {}
for name, S in survivors:
    surv_sets.setdefault(S, []).append(name)
print(f"\n    ADMISSIBLE **AND** phi-STABLE: {len(survivors)} candidates,"
      f" {len(surv_sets)} distinct sets")
for S, names in surv_sets.items():
    mark = "  <-- A5's set" if S == A5set else ""
    print(f"       |{len(S)}| via {names[0]}{mark}")

print("""
THE VERDICT (reported as it fell, against the preregistered
expectation):""")
if len(admissible) == 1:
    print("  C1-C4 ALONE ALREADY FORCE A5 — a surprise, and a strong result.")
else:
    print(f"  A5 IS NOT UNIQUE AT C1-C4: {len(admissible)} distinct admissible sets")
    print("  exist among premise-free candidates.  **This refutes the GATES, not")
    print("  the hypothesis.**  C1-C4 as designed are too weak to single out any")
    print("  predicate, so 'clears the gates' cannot mean 'is the criterion'.")
    print("  The preregistered expectation is therefore CONFIRMED, and the")
    print("  honest status of memo 115 is downgraded from 'leading candidate'")
    print("  to 'one of several admissible candidates' until a stronger gate")
    print("  discriminates.")
if len(surv_sets) == 1 and A5set in surv_sets:
    print("  BUT UNDER C5 THE FIELD COLLAPSES TO EXACTLY ONE SET — A5's.  The")
    print("  record's own automorphism is the discriminator: the shadow-pairing")
    print("  predicate is the unique premise-free, phi-stable criterion in this")
    print("  family.  That is a genuine strengthening, earned by a gate the")
    print("  record motivated rather than one chosen to rescue the answer.")
elif A5set in surv_sets:
    print(f"  UNDER C5 the field narrows to {len(surv_sets)} sets, A5's among them —")
    print("  a real narrowing, not a decision.  The remaining competitors are")
    print("  named above and must be excluded by a further, record-motivated")
    print("  constraint before S-A can be called closed.")
else:
    print("  UNDER C5 A5'S OWN SET DOES NOT SURVIVE — the hypothesis fails the")
    print("  record's own stability requirement.  Filed as a refutation.")
print("""  In every branch: S-A remains OPEN, the token question (S-B) is
  untouched, and the phenomenal question (S-C) stays inexpressible.
Gate 5 untouched.""")
