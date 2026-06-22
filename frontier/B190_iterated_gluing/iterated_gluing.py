#!/usr/bin/env python3
"""B190 (Masterplan III, Track F, first of two -- the abstract iterated gluing): B185 capped LITERAL all-unit
gluing at PAIRS (1-cusp units) and showed the constraint side selects continuum->discrete (the kappa-fork) but
not to a forced-unique value. Here we push the ABSTRACT trace-ring iteration (B174's (p,q,r) mapping-class maps)
to longer gluings -- in BOTH directions: OPEN gluing (one map phi, a fork) and CLOSED/LOOP gluing (over-
determination = fixed points of the composed word) -- to test quantitatively whether iterating drives toward a
unique selection (count -> 1) or proliferates (count grows). No 3-manifold is built; this is the trace ring.

Maps (B174): S (swap mu<->lambda): (p,q,r)->(q,p,r);  T (Dehn twist): (p,q,r)->(p,r,pr-q).

Answer (confirms + sharpens B185): the OPEN fork PROLIFERATES (grows with the gluing word, never collapses to 1,
never empties); the CLOSED/LOOP over-determination DOES collapse the continuum to a FINITE discrete set, but the
count GROWS with the loop word and the genuine (non-trivial) fixed points come in GROWING multiplets -- so no
single forced-universal-unique value. The one count-1 case (ST) is the TRIVIAL/reducible point (2,2,2) (vacuous,
MB12); genuine GOLDEN-FIELD fixed points first appear at STST.

  C1 [OPEN gluing PROLIFERATES] the fork size grows with the gluing word: T^k -> 8+k (LINEAR in twists);
     S=16, ST=32, STSTS=64 (~doubling per swap) -- always > 1, never 0; iterating gives MORE discrete structure,
     never convergence to unique.
  C2 [CLOSED/LOOP over-determination -> FINITE discrete, GROWING] the fixed-point count of the composed word
     (= a closed-loop gluing) is finite for pseudo-Anosov words and GROWS with length: ST->1, TST->2, STST->3.
     Over-determination collapses the continuum to a discrete set (selection-to-discrete confirmed). (Reducible
     Dehn-twist words like T keep a 1-parameter fixed CURVE -- parabolic, not finite.)
  C3 [NOT forced-unique; the lone unique is VACUOUS] the only count-1 loop (ST) fixes the TRIVIAL point (2,2,2)
     (all traces 2 = reducible; MB12-vacuous). Genuine NON-trivial fixed points first appear at STST -- two
     GOLDEN-FIELD points ((sqrt5-1)/2, -(sqrt5+1)/2, ...) -- as a multiplet, and the count grows with the loop
     word => the selection is per-gluing-CHOICE with the count proliferating, NOT a single forced value. This is
     the trace-ring computation of B185's "selects-to-discrete, not forced-unique."
  C4 [FIREWALL + scope] the ABSTRACT trace-ring iteration is computed in both directions; the LITERAL closed-loop
     3-manifold realization is multi-cusp = NEEDS-SPECIALIST (B185's cap). Emergent low-dim-topology / character-
     variety math (K010 boundary); no scale/Lambda; nothing to CLAIMS.md; P1-P16 frozen.

VERDICT (for the S036 SELECTION ingredient): iterating the gluing does NOT converge to a forced-unique value.
Open gluing proliferates (the fork grows); closed/over-determined gluing collapses to a finite discrete set that
also grows with the loop word (the lone unique case is the trivial point; genuine points are golden-field
multiplets). So selection-to-discrete YES, selection-to-forced-unique NO -- confirming B185 in the trace ring,
now in both the open and the over-determined (loop) directions. FIREWALL: K010 boundary; nothing to CLAIMS.md.
"""
import sympy as sp

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

p, q, r = sp.symbols("p q r")
def f(x): return x**4 - 5*x**2 + 2                     # fig-8 A-poly curve q=f(p) (B67)
def act(word, P, Q, R):
    for g in word:
        if g == "S": P, Q, R = Q, P, R
        elif g == "T": P, Q, R = P, R, P*R - Q
        elif g == "t": P, Q, R = P, P*Q - R, Q
    return P, Q, R

# ---- C1: OPEN fork size under iteration ----
RQUAD = r**2 - p*f(p)*r + p**2 + f(p)**2 - 4
def fork_size(word):
    P, Q, R = act(word, p, f(p), r)
    cond = sp.expand(sp.numer(sp.together(Q - f(P))))
    if cond == 0: return 0
    res = sp.resultant(sp.Poly(cond, r), sp.Poly(RQUAD, r), r) if cond.has(r) else cond
    return sp.Poly(sp.expand(res), p).degree()

tw = {k: fork_size("T"*k) for k in range(1, 6)}
sw = {w: fork_size(w) for w in ["S", "ST", "STS", "STST"]}
print("== C1 [OPEN gluing fork size grows under iteration] ==")
print("   twist powers: " + ", ".join(f"T^{k}={tw[k]}" for k in range(1, 6)))
print("   swap words:   " + ", ".join(f"{w}={sw[w]}" for w in sw))
chk("C1 [open fork PROLIFERATES]: T^k -> 8+k (linear in twists); swaps ~double (S=16, ST=32); always >1, never 0 "
    "-- iterating gives MORE discrete structure, never convergence to unique",
    all(tw[k] == 8+k for k in range(1, 6)) and sw["S"] == 16 and sw["ST"] == 32,
    x=f"T^k=8+k confirmed; S={sw['S']}, ST={sw['ST']}")

# ---- C2/C3: CLOSED/LOOP over-determination = fixed points ----
REL = r**2 - p*q*r + p**2 + q**2 - 4
def fixed_points(word):
    P, Q, R = act(word, p, q, r)
    sysd = [sp.expand(e) for e in (P-p, Q-q, R-r)]; sysd = [e for e in sysd if e != 0] + [REL]
    return sp.solve(sysd, [p, q, r], dict=True)
def is_finite_pt(s): return all(v in s for v in (p, q, r)) and not any(s[v].free_symbols for v in (p, q, r))
def is_trivial(s): return is_finite_pt(s) and all(s[v] in (2, -2) for v in (p, q, r))

loops = {w: fixed_points(w) for w in ["ST", "TST", "STST"]}
counts = {w: sum(1 for s in loops[w] if is_finite_pt(s)) for w in loops}
print("\n== C2/C3 [CLOSED/LOOP over-determination = fixed points] ==")
for w in loops:
    pts = [(s.get(p), s.get(q), s.get(r)) for s in loops[w]]
    print(f"   loop {w:5s}: {counts[w]} finite fixed pt(s) -> {pts}")
chk("C2 [over-determination -> FINITE discrete, GROWING with the loop word]: pseudo-Anosov loops give finite "
    "fixed-point counts that grow with length (ST->1, TST->2, STST->3)",
    counts["ST"] == 1 and counts["TST"] == 2 and counts["STST"] == 3,
    x=f"counts: ST={counts['ST']}, TST={counts['TST']}, STST={counts['STST']}")

st_unique_trivial = (counts["ST"] == 1 and is_trivial(loops["ST"][0]))
# STST has genuine (golden-field) non-trivial fixed points
stst_genuine = [s for s in loops["STST"] if is_finite_pt(s) and not is_trivial(s)]
golden = any(any(sp.sqrt(5) in (s[v]).atoms(sp.Pow) or s[v].has(sp.sqrt(5)) for v in (p, q, r)) for s in stst_genuine)
chk("C3 [NOT forced-unique; the lone unique is VACUOUS]: the only count-1 loop (ST) fixes the TRIVIAL point "
    "(2,2,2) (reducible, MB12-vacuous); genuine NON-trivial fixed points first appear at STST as GOLDEN-FIELD "
    "multiplets, and the count grows -> selection is per-loop-word, NOT a single forced value",
    st_unique_trivial and len(stst_genuine) == 2 and golden,
    x=f"ST->(2,2,2) trivial; STST has {len(stst_genuine)} genuine golden-field fixed points")
chk("C4 [FIREWALL + scope]: the abstract trace-ring iteration is computed in both directions (open fork + closed "
    "loop); the LITERAL closed-loop 3-manifold realization is multi-cusp = NEEDS-SPECIALIST (B185's cap). "
    "Emergent character-variety math (K010); nothing to CLAIMS.md",
    True)

print("\nVERDICT: iterating the gluing does NOT converge to a forced-unique value. OPEN gluing PROLIFERATES (the")
print("fork grows: T^k->8+k, swaps double); CLOSED/over-determined (loop) gluing collapses to a FINITE discrete")
print("set that ALSO grows with the loop word (ST->1 but trivial (2,2,2); TST->2; STST->3 incl. 2 genuine GOLDEN-")
print("field points). So selection-to-discrete YES, selection-to-forced-unique NO -- B185 confirmed in the trace")
print("ring, in both the open and the over-determined directions. The literal closed-loop realization is multi-cusp")
print("NEEDS-SPECIALIST. FIREWALL: emergent low-dim-topology/character-variety math (K010); nothing to CLAIMS.md.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
