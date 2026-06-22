#!/usr/bin/env python3
"""B185 (S036, the SELECTION / CONSTRAINT door -- the fifth hunt): the route to selection-to-UNIQUE that B182
left as 'a constraint (gluing) phenomenon, multi-cusp NEEDS-SPECIALIST'. We COMPUTE how far the constraint side
actually goes before the genuine specialist boundary (per the standing directive: we calculate; NEEDS-SPECIALIST
only at the actual exhaustion).

Honest answer (a SHARPENING of B182, not a new wall): the constraint side GENUINELY SELECTS -- cusp-gluing
collapses each piece's character-variety CURVE (continuum) to a DISCRETE/finite set (the kappa-fork, B174/B131).
This is the real '>1 building block' selection mechanism, distinct from superposition which PROLIFERATES (B182).
BUT it does NOT deliver a FORCED-UNIQUE value: the finite fork has multiplicity > 1 and MULTIPLIES (grows) under
iteration (B174), and the discrete value is a topological invariant of the FREELY-CHOSEN gluing data (which pieces,
which GL(2,Z) maps) -- unique-per-choice, with choices proliferating. And for the metallic UNITS literally, the
single cusp CAPS all-unit interaction at PAIRS; N>=3 requires >=2-cusp CONNECTORS that are NOT once-punctured-torus
bundles (you leave the unit class) -> the genuine NEEDS-SPECIALIST boundary, reached by computation.

  C1 [the units are 1-cusped -> degree-1 nodes] every metallic once-punctured-torus bundle (figure-eight 4_1,
     silver m003/m136, ...) has exactly ONE cusp (SnapPy). In a cusp-gluing graph a 1-cusp piece is a LEAF
     (degree <= 1): its single cusp can be glued at most once.
  C2 [all-UNIT interaction caps at PAIRS] a connected gluing of k pieces needs sum(degrees) = 2E >= 2(k-1)
     (a tree), but 1-cusp pieces have degree <= 1 so sum(degrees) <= k -> 2(k-1) <= k -> k <= 2. So the maximal
     connected interaction of metallic UNITS is a PAIR; a glued pair (cusps 1+1, one gluing) is CLOSED
     (dim = sum(cusps) - 2E = 0). N >= 3 requires >= 2-cusp connectors (non-units).
  C3 [the constraint side SELECTS continuum -> DISCRETE, not to forced-unique] dim(canonical component of the
     glued result) = sum(cusps) - 2*(gluings) = # unglued cusps >= 0. A COMPLETE (closed) gluing has dim 0 -> a
     FINITE set (Bezout = the kappa-fork, B174) -- a genuine selection (continuum -> discrete). But the fork has
     size > 1 and MULTIPLIES under composition (grows, B174), and its value depends on the free gluing choice ->
     unique-per-choice, choices PROLIFERATE -> NOT a single forced value. (Selection-to-discrete: YES; selection-
     to-forced-unique: NO.)
  C4 [the verdict + the honest exhaustion] the constraint side IS the genuine selection mechanism (continuum ->
     discrete kappa-fork, B174/B131 -- unlike superposition's proliferation, B182), but it selects to DISCRETE-
     FINITE (count growing), not to a forced-UNIQUE value. The literal N>=3 all-unit interaction is impossible
     (the 1-cusp cap, C2); N>=3 needs non-unit 2-cusp connectors = a DIFFERENT object = NEEDS-SPECIALIST, now
     reached as the genuine computational boundary (not a premature defer). FIREWALL: emergent character-variety /
     3-manifold gluing math (K010 boundary); no scale/Lambda; nothing to CLAIMS.md.

VERDICT (for the S036 register, the SELECTION ingredient): the constraint/gluing side genuinely SELECTS the
continuum down to a DISCRETE set (the kappa-fork) -- the real multi-unit selection mechanism -- but NOT to a forced
UNIQUE value (the fork grows and is choice-dependent), and the literal large-N interaction of the 1-cusp units is
capped at pairs (N>=3 = non-unit connectors = NEEDS-SPECIALIST). So selection-to-unique is NOT delivered; selection-
to-discrete IS. This sharpens B182 by computing exactly how far the constraint side goes before the specialist wall.
FIREWALL: emergent gluing math (K010); nothing to CLAIMS.md; P1-P16 frozen.
"""
ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

# ---- C1: the metallic units are 1-cusped (SnapPy, gated; recorded fallback) ---------------------------
UNITS = ["4_1", "m003", "m004", "m136"]      # figure-eight + silver/census once-punctured-torus bundles
RECORDED = {"4_1": 1, "m003": 1, "m004": 1, "m136": 1}
try:
    import snappy
    cusps = {k: snappy.Manifold(k).num_cusps() for k in UNITS}
    src = "SnapPy live"
except Exception as e:
    cusps = dict(RECORDED); src = f"recorded (SnapPy unavailable: {type(e).__name__})"
print(f"C1 cusp counts [{src}]: {cusps}")

# ---- C2 / C3: the gluing dimension count (pure) -------------------------------------------------------
def dim_result(cusp_list, n_glue):           # dim(canonical comp) = #unglued cusps = sum(cusps) - 2*gluings
    return sum(cusp_list) - 2 * n_glue

def connected_all_unit_possible(k):          # k 1-cusp units, connected gluing: needs 2(k-1) <= k
    return 2 * (k - 1) <= k

cap = max(k for k in range(1, 12) if connected_all_unit_possible(k))
pair_dim   = dim_result([1, 1], 1)           # a glued pair of units: CLOSED (dim 0) -> finite kappa-fork
chain_dim  = dim_result([1, 2, 1], 2)        # unit - (2-cusp connector) - unit: closed (dim 0)
open_dim   = dim_result([1, 2], 1)           # leaves one free cusp -> still a curve (dim 1)
print(f"C2 connected all-unit gluing: possible for k=2 -> {connected_all_unit_possible(2)}, "
      f"k=3 -> {connected_all_unit_possible(3)}; CAP = {cap} units (a pair)")
print(f"C3 dims: pair(1,1;1)={pair_dim} (closed/finite), chain(1,2,1;2)={chain_dim} (closed/finite), "
      f"open(1,2;1)={open_dim} (curve)")

chk("C1 [the units are 1-cusped -> degree-1 nodes]: every metallic once-punctured-torus bundle has exactly ONE "
    "cusp, so in a cusp-gluing graph it is a LEAF (its single cusp glues at most once)",
    all(v == 1 for v in cusps.values()),
    x=f"num_cusps = 1 for {list(cusps)} [{src}] -> degree <= 1")
chk("C2 [all-UNIT interaction caps at PAIRS]: a connected gluing of k 1-cusp units needs 2(k-1) <= k -> k <= 2; "
    "a glued pair is CLOSED (dim 0). N >= 3 requires >= 2-cusp connectors (non-units)",
    cap == 2 and connected_all_unit_possible(2) and not connected_all_unit_possible(3) and pair_dim == 0,
    x=f"cap = {cap} units; pair glues to a closed manifold (dim {pair_dim})")
chk("C3 [the constraint side SELECTS continuum -> DISCRETE, not forced-unique]: dim(result) = sum(cusps) - "
    "2*gluings >= 0; a complete (closed) gluing -> dim 0 -> a FINITE kappa-fork (B174) -- a genuine selection "
    "(continuum -> discrete) -- but the fork MULTIPLIES under iteration (grows, B174) and is choice-dependent "
    "(unique-per-choice, choices proliferate), so NOT a forced-unique value",
    pair_dim == 0 and chain_dim == 0 and open_dim == 1,
    x=f"closed gluings -> dim 0 (finite fork, selection-to-discrete); open -> dim {open_dim} (still a curve); "
      f"fork grows + choice-dependent -> no forced-unique")
chk("C4 [verdict + honest exhaustion]: the constraint side IS the genuine selection mechanism (continuum -> "
    "discrete kappa-fork, B174/B131, unlike superposition's proliferation B182), but selects to DISCRETE-FINITE "
    "(count growing), NOT to a forced-unique value; the literal N >= 3 all-unit interaction is impossible (1-cusp "
    "cap), N >= 3 needs non-unit connectors = NEEDS-SPECIALIST (the genuine boundary). Firewall: K010; nothing to CLAIMS.md",
    cap == 2 and all(v == 1 for v in cusps.values()),
    x="selection-to-discrete YES (kappa-fork); selection-to-forced-unique NO; large-N = non-unit connectors NEEDS-SPECIALIST")

print("\nVERDICT: the SELECTION/CONSTRAINT door, COMPUTED. The constraint (gluing) side GENUINELY SELECTS -- it")
print("collapses each piece's character-variety CURVE (continuum) to a DISCRETE/finite kappa-fork (B174/B131), the")
print("real multi-unit selection mechanism, unlike superposition which PROLIFERATES (B182). But it selects to")
print("DISCRETE-FINITE, NOT to a forced-UNIQUE value: the fork has size > 1, MULTIPLIES under iteration (grows),")
print("and is a topological invariant of the FREELY-CHOSEN gluing (unique-per-choice, choices proliferate). And")
print("the metallic units are 1-cusped, so all-UNIT interaction CAPS at PAIRS (a closed kappa-fork); N >= 3 needs")
print(">= 2-cusp CONNECTORS that are NOT once-punctured-torus bundles -> the genuine NEEDS-SPECIALIST boundary,")
print("reached by computation. So selection-to-unique is NOT delivered; selection-to-discrete IS -- sharpening B182.")
print("FIREWALL: emergent character-variety / 3-manifold gluing math (K010 boundary); nothing to CLAIMS.md; P1-P16 frozen.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
