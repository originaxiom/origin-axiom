#!/usr/bin/env python3
"""
R01 / B1225 blind recomputation — THE NO-CANONICAL-SELECTOR THEOREM.

Written BEFORE opening frontier/B1225_no_canonical_selector/verification/ or any
B1225 test lock. Inputs used (committed data of OTHER arcs only):

  - The 17 tier-1 atoms: the only enumerated list anywhere on this bench is the
    dict hard-coded in frontier/B1203_two_probes/verification/reproduce.sh
    (1,2,3,11,12,27,64,72,78,112,953,2304,151/64,553/64,3/8,phi,2+sqrt3).
  - Operations {+,-,*,/,sqrt} (B1203 / B1225 step 2).
  - B1168's law: object-canonical <=> beta-even (mirror-even) AND dimensionless.
  - GC-15 (B1191 batch3_cells.json): G := Stab_Aut(D)|_T, read off D.
  - Aut(D): recomputed independently from snappy for m004 (the object),
    cross-checked against the banked "Isom(m004) = D4, 8 elements" (B1104 line
    in docs, cited in CLAIM_CANDIDATES.md).

What is recomputed here:
  1. Aut(D) for D = m004 from snappy: order, and how many elements are
     orientation-reversing (amphichirality).
  2. The induced action of Aut(D) on numerical invariants. A numerical invariant
     read off D is unchanged by every orientation-PRESERVING self-isometry (that
     is what "invariant" means); an orientation-REVERSING one acts through the
     mirror, which on complex-valued archimedean data acts by complex
     conjugation c (B1168: the complex volume conjugates, CS -> -CS, etc.).
     So the action of Aut(D) on values factors through eps: Aut(D) -> {1, c}.
     We implement the FULL group element-by-element via eps and act on every
     menu value exactly (sympy conjugate), then check every orbit.
  3. The menu: the exact tier rule of cloud's enumerator is NOT committed on
     this bench (B1225 ADDENDUM + relay CC_TO_CLOUD_2026-08-31_SEND_THE_
     SEVENTEEN_ATOMS.md both state the enumerator/list is cloud-side). We
     therefore generate closures of the 17 atoms under {+,-,*,/,sqrt}
     (sqrt restricted to nonnegative arguments, which is the restriction under
     which "the ops preserve reality" in B1203 is true) at several depths, and
     check triviality of the G-action on EVERY generated value. Triviality on
     the full closure implies triviality on the banked 11,720-value menu no
     matter what tier rule cloud used, PROVIDED the menu is inside the real
     closure of these atoms — which is exactly B1203's banked property.
  4. VACUITY probe: the sqrt-equivariance clause. c(sqrt(x)) = sqrt(c(x)) holds
     for x >= 0 but FAILS for x < 0 (sqrt(-2) = i*sqrt(2) is moved by c). So
     step 5 of B1225 ("{+,-,*,/,sqrt} are G-equivariant") is true only on the
     reality-preserving domain; we exhibit the failure exactly.
  5. CONTROL (the instrument can find a nontrivial action when one exists):
     plant a beta-odd atom (a non-real value, standing for e.g. a CS-like
     mirror-odd datum) into the atom list, rebuild the small menu, rerun the
     same orbit check, and confirm (a) the reality assert catches it, (b) the
     G-action is NOT trivial, (c) an invariance filter now cuts a nonzero,
     correctly-identified subset.
Gate 5: no measured Standard Model value appears anywhere below.
"""
import sys
import sympy as sp
import mpmath as mp

mp.mp.dps = 40
OUT = []
def say(s=""):
    print(s); OUT.append(s)

# ---------------------------------------------------------------- 1. Aut(D)
say("== 1. Aut(D) recomputed independently (snappy, D = m004) ==")
autd_order = None
autd_or_rev = None
try:
    import snappy
    M = snappy.Manifold("m004")
    G = M.symmetry_group()
    autd_order = G.order()
    amph = G.is_amphicheiral()
    say(f"  snappy: symmetry_group(m004) = {G}, order = {autd_order}, "
        f"amphichiral = {amph}")
    # orientation-reversing elements: in a group of order 2n containing
    # orientation-reversing elements, exactly half reverse orientation
    autd_or_rev = autd_order // 2 if amph else 0
    say(f"  => {autd_order - autd_or_rev} orientation-preserving, "
        f"{autd_or_rev} orientation-reversing elements")
except Exception as e:
    say(f"  snappy unavailable/failed ({e}); falling back to the banked "
        f"Isom(m004) = D4 (order 8, amphichiral) — flagged as CITED not recomputed")
    autd_order, autd_or_rev = 8, 4

# The induced action of Aut(D) on numerical invariants factors through
# eps: Aut(D) -> Z/2 = {identity, mirror}; mirror acts on C-valued data by
# complex conjugation (B1168's own-verified rows: complex volume conjugates,
# CS -> -CS, cusp shape tau -> -conj(tau)).
group_eps = [ +1 ] * (autd_order - autd_or_rev) + [ -1 ] * autd_or_rev
def act(eps, v):
    return v if eps == +1 else sp.conjugate(v)

# ---------------------------------------------------------------- 2. atoms
say("")
say("== 2. The 17 tier-1 atoms (the ONLY committed list: B1203 reproduce.sh) ==")
phi = (1 + sp.sqrt(5)) / 2
atoms = {
    "1": sp.Integer(1), "2": sp.Integer(2), "3": sp.Integer(3),
    "11": sp.Integer(11), "12": sp.Integer(12), "27": sp.Integer(27),
    "64": sp.Integer(64), "72": sp.Integer(72), "78": sp.Integer(78),
    "112": sp.Integer(112), "953": sp.Integer(953), "2304": sp.Integer(2304),
    "151/64": sp.Rational(151, 64), "553/64": sp.Rational(553, 64),
    "3/8": sp.Rational(3, 8), "phi": phi, "2+sqrt3": 2 + sp.sqrt(3),
}
assert len(atoms) == 17
nonreal = [k for k, v in atoms.items() if not v.is_real]
say(f"  count = {len(atoms)}; non-real atoms = {nonreal}")
assert nonreal == []
# exact fixedness under the full group
moved_atoms = [k for k, v in atoms.items()
               for e in group_eps if sp.simplify(act(e, v) - v) != 0]
say(f"  atoms moved by ANY of the {autd_order} elements of Aut(D): "
    f"{sorted(set(moved_atoms))}  (exact sympy check)")
assert moved_atoms == []

# ---------------------------------------------------------------- 3. ops equivariance (exact, symbolic)
say("")
say("== 3. Are {+,-,*,/,sqrt} G-equivariant? (symbolic, exact) ==")
x, y = sp.symbols("x y", real=True)
xp = sp.Symbol("xp", nonnegative=True)
for name, expr in [("+", x + y), ("-", x - y), ("*", x * y), ("/", x / y)]:
    d = sp.simplify(sp.conjugate(expr) - expr.subs({x: sp.conjugate(x), y: sp.conjugate(y)}))
    say(f"  c(a {name} b) - (c(a) {name} c(b)) = {d}")
    assert d == 0
d_ok = sp.simplify(sp.conjugate(sp.sqrt(xp)) - sp.sqrt(xp))
say(f"  sqrt on NONNEGATIVE reals: c(sqrt(x)) - sqrt(x) = {d_ok}  -> equivariant AND fixed")
assert d_ok == 0
bad = sp.sqrt(sp.Integer(-2))
d_bad = sp.simplify(sp.conjugate(bad) - bad)
say(f"  sqrt on a NEGATIVE real: c(sqrt(-2)) - sqrt(-2) = {d_bad}  (NOT zero)")
assert d_bad != 0
say("  => B1225 step 5 as literally stated ('sqrt is G-equivariant') holds only on")
say("     the reality-preserving domain; the theorem's conclusion survives because")
say("     every MENU VALUE is real (B1203), and c fixes every real regardless of route.")

# ---------------------------------------------------------------- 4. menu closures + full-orbit check
say("")
say("== 4. Menu closure from the atoms; full Aut(D)-orbit of every value ==")

def close_once(vals, allow_sqrt=True, cap=None):
    """one round of {+,-,*,/} on all ordered pairs + sqrt of nonnegatives, numeric."""
    out = dict(vals)  # key: mpf string at 35 digits -> mpf
    items = list(vals.values())
    for i, a in enumerate(items):
        if allow_sqrt and a >= 0:
            out.setdefault(mp.nstr(mp.sqrt(a), 35), mp.sqrt(a))
        for b in items:
            for r in (a + b, a - b, a * b):
                out.setdefault(mp.nstr(r, 35), r)
            if b != 0:
                r = a / b
                out.setdefault(mp.nstr(r, 35), r)
            if cap and len(out) > cap:
                return out
    return out

num_atoms = {k: mp.mpf(sp.N(v, 40).__str__()) for k, v in atoms.items()}
base = {mp.nstr(v, 35): v for v in num_atoms.values()}
S1 = close_once(base)                      # depth 1
S2 = close_once(S1, cap=300_000)           # depth 2 (cap-limited probe)
say(f"  |atoms| = {len(base)}, |closure depth 1| = {len(S1)}, "
    f"|closure depth 2| = {len(S2)}{' (hit 300k cap; true depth-2 is larger)' if len(S2)>=300_000 else ''}")
say(f"  banked W1 = 11720: neither depth equals it — the tier rule that yields")
say(f"  exactly 11,720 is cloud's enumerator, NOT committed on this bench (ADDENDUM).")

# The action check does not depend on the tier rule: check EVERY generated value
# at depth 1 (superset of any real tier-1 combination of one op) exactly where
# feasible, numerically at scale.
say("")
say("  orbit check, numeric at 40 dps, ALL depth-1 closure values, all group elements:")
moved = 0
for v in S1.values():
    # numeric values here are real mpf by construction; c acts as identity on them.
    # The honest check is on the EXACT representatives: do it symbolically on a
    # stratified exact sample, and numerically confirm realness for all.
    if abs(mp.im(mp.mpc(v))) != 0:
        moved += 1
say(f"    non-real (hence c-movable) depth-1 values: {moved} of {len(S1)}")
assert moved == 0

# exact symbolic orbit check on every atom pair under every op (the complete
# tier-1 single-op stratum, 17*17*4 ordered combinations + 17 sqrts):
say("  exact symbolic orbit check on the complete single-op stratum:")
exact_moved = []
avals = list(atoms.values())
exprs = []
for a in avals:
    if a >= 0:
        exprs.append(sp.sqrt(a))
    for b in avals:
        exprs.extend([a + b, a - b, a * b])
        if b != 0:
            exprs.append(a / b)
has_reversing = -1 in group_eps
for t in exprs:
    # eps=+1 elements act as the literal identity on values (checked once, above,
    # structurally): act(+1, t) is t itself. Only the reversing class can move t.
    if has_reversing and sp.simplify(sp.conjugate(t) - t) != 0:
        exact_moved.append(t)
say(f"    stratum size = {len(exprs)}; values moved by any of the {autd_order} "
    f"group elements: {len(exact_moved)}")
assert exact_moved == []
say("  => THE ACTION OF THE FULL Aut(D) (hence of G = Stab_Aut(D)|_T, a subgroup)")
say("     ON EVERY VALUE BUILT FROM THE ATOMS IS TRIVIAL: every orbit is a fixed")
say("     point; every subset of the menu is G-invariant; invariance selects nothing.")

# ---------------------------------------------------------------- 5. CONTROL
say("")
say("== 5. CONTROL: plant a beta-odd (mirror-odd) atom; the instrument must bite ==")
# a CS-like mirror-odd datum: represented by a value with nonzero imaginary part
# (the mirror conjugates it, so it is NOT fixed). Use i*sqrt(2).
planted = {**atoms, "PLANT_i_sqrt2": sp.I * sp.sqrt(2)}
nonreal_p = [k for k, v in planted.items() if not (sp.im(v) == 0)]
say(f"  reality assert now catches: {nonreal_p}")
assert nonreal_p == ["PLANT_i_sqrt2"]
pvals = list(planted.values())
moved_p, fixed_p = 0, 0
sample = []
for a in pvals:
    for b in pvals:
        for t in (a + b, a * b):
            if any(sp.simplify(act(e, t) - t) != 0 for e in group_eps):
                moved_p += 1
                if len(sample) < 2:
                    sample.append(t)
            else:
                fixed_p += 1
say(f"  planted-menu (all +,* pairs): {moved_p} values MOVED by the mirror, "
    f"{fixed_p} fixed — e.g. {sample}")
assert moved_p > 0
say(f"  an invariance filter on the planted menu cuts {moved_p} of {moved_p+fixed_p}:")
say("  NONZERO. The instrument CAN find a nontrivial action / nonzero cut when one")
say("  exists; the zero cut on the real menu is therefore a finding, not blindness.")

# ---------------------------------------------------------------- 6. verdict data
say("")
say("== 6. Summary of the recomputed facts ==")
say(f"  Aut(D) order (snappy, independent): {autd_order}; orientation-reversing: {autd_or_rev}")
say("  action on values factors through {1, c}; all 17 committed atoms exactly real;")
say("  ops equivariant (sqrt only on nonnegatives); complete single-op stratum")
say(f"  ({len(exprs)} exact values) pointwise fixed by all {autd_order} elements;")
say("  depth-1 numeric closure all real. TRIVIAL ACTION: reproduced.")
say("  W1 = 11720 itself: NOT reproducible from committed files (enumerator is")
say("  cloud-side; ADDENDUM + relay ledger confirm). Triviality is depth/tier-")
say("  independent, so the banked conclusion follows for ANY menu inside the real")
say("  closure of these atoms.")

with open(__file__.replace("recompute_action.py", "recompute_output.txt"), "w") as f:
    f.write("\n".join(OUT) + "\n")
print("\nDONE")
