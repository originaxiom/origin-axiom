# B1476 — THE SPIN SWAP, PHASE 1c: AT CS = ¼ NO SPIN STRUCTURE SURVIVES THE MIRROR — thirteen of thirteen, certified without enumerating isometries — the fate of the geometric lift at CS = 0 is not decided by CS, the whole family's phase sits on the 1/24 lattice, the knot's spin bit is the parent's Pin type by a second route — and A5 selected a member, not the object

**Verdict: PROVED** (scope: the 13 amphichiral rank-one members of the 112-family for the classification and the ¼ law;
the 112 for the lattice; 15 cusped and 37 closed amphichiral census manifolds outside the family for the law's reach;
reach *class* for the family facts, *general* for the one-way law as far as tested, *conjectural* beyond). cc (main),
2026-10-04. Sealed at `88ed6981` (sha256 `aedf139f…`). L246 Phase 1c: **advanced and paid; the owner's rule frames
the A5 question.** **The prize first:** a derived, discrete, family-wide law — the mirror's action on the fermionic
bit is read off the Chern–Simons phase — found together with its scope by the computation that tried to break it.
No value, no count: **0 of 19.**

## 0. Seen first

As sealed: `topic_sweep.py "quarter class|1/4 class|CS = 1/4|cs ≡ ¼|Pin+|Pin-|Pin type|free deck|orientation double
cover|free orientation-reversing"` — VERDICT 38 of 1348 arcs (NEGATIVE 4, OPEN 3, PROVED 31); B1224, B1239, B1235/L194,
B279, sm:B1382/B1383, B1141/B1118, B1474, B1475, chat1's two handoffs of the day (L247, L248), codex's R89 read.
**Literature:** Pin structures on 3-manifolds and the pullback of a Pin structure on M/τ to a τ-invariant spin
structure (Kirby–Taylor, not re-read); Neumann's complex volume as a sum of Rogers dilogarithms (standard; the
tetrahedral census setting).

## 1. The sealed predictions, scored

| | prediction | prior | outcome |
|---|---|---|---|
| P1 | swap ⟺ CS ≡ ¼ (mod ½) on the thirteen | 70% | **HOLDS 13 of 13** — the seven swap members are exactly the seven at ¼, the six fix members exactly the six at 0 |
| P2 | classes all = 5, some = 1, none = 7 | 65% | **all = 4** (m004, m206, t12839, o10_150696), **some = 2** (s961 4 of 8, o10_150707 4 of 8), **none = 7** — off by one member |
| P3 | m003 is the orientation cover of no non-orientable census manifold; m004 is the Gieseking's | 90% | **HOLDS** (C3: m003 → none; m004 → m000) |
| P4 | on m004, C·C̄ gives one Pin type per lift, opposite | 85% | **HOLDS** (corrected cell, §3): C·C̄ = +ρ(w), w = ba / baBAb / aBAbaBA for three reversing isometries; the geometric lift Pin⁺, the other lift Pin⁻ |
| P5 | the referee's exact script reproduces on main | 90% | **HOLDS** (`r14_rerun.txt`: W·W̄ = +A; lift a ↦ +A extends into Pin⁺ only, a ↦ −A into Pin⁻ only) |
| P6 | CS ∈ (1/24)ℤ on all 112; outside controls not | 80% | **HOLDS 112 of 112** (denominators 1: 25, 2: 22, 3: 7, 4: 29, 6: 11, 8: 3, 12: 10, 24: 5); **0 of 40 outside** on the lattice; Re R(e^{iπ/3}) = π²/12 and Im R = Vol(4₁)/2 to 20 digits |
| P7 | outside the family: ¼ ⟹ swap and 0 ⟹ fix (of the geometric lift) | 60% | **FAILS as sealed, HOLDS one way:** 15 cusped amphichiral census manifolds outside the family — at ¼ **all 6 swap, and by the certificate of §2b none of their spin structures is mirror-invariant**; of the 7 decided at 0, the geometric lift is fixed on 4 and swapped on 3 (m136, s880, s883); 2 undetermined at length 7. **What the sealed cell did not test** — whether a zero member has *some* mirror-invariant spin structure — is open: m136 has 4 of 8 torsion-real (§2b) |
| P8 | every closed amphichiral census manifold is FIX-able (the geometric lift) | 70% | **FAILS as sealed:** of the 37 (all at CS ≡ 0 mod 1), 25 decided — the geometric lift fixed on 11, swapped on 14; 12 undetermined at length 7. The same caveat: only the geometric lift was read |

## 2. The law, stated with the scope the computation gave it

- **CS ≡ ¼ ⟹ no spin structure is mirror-invariant.** Holds on every amphichiral manifold tested: the family's seven
  (B1475: every spin structure) and six outside it (m135, s463, s725, s881, s891, s911), 13 of 13 — **certified in §2b
  without enumerating isometries**. No ¼ member has a torsion-real spin structure.
- **At CS ≡ 0 the geometric lift is fixed** on all six zero members of the ℚ(√−3) family and on 4 of 7 decided outside
  it, **and swapped on m136, s880, s883 and on 14 of 25 closed manifolds.** So the fate of the *geometric lift* is not a
  function of CS. **Whether a zero member always has SOME mirror-invariant spin structure — which would make
  "no spin structure survives the mirror ⟺ CS = ¼" an equivalence for the manifold — was not tested by the sealed
  cells** (they read the geometric lift outside the family) and is the next sealed arc: on m136 four of eight spin
  structures are torsion-real, so it is not excluded there.
- **A corollary from the closed data:** a genuine swap forces every orientation-reversing isometry to have fixed points
  (a free one would give M/τ a Pin⁻ structure, which pulls back to a τ-invariant spin structure) — fourteen closed
  amphichiral census manifolds have no free orientation-reversing involution, and m003 is the orientation cover of
  nothing (P3) for the same reason.
- **The 1/24 lattice.** The whole family's phase is quantised — 112 of 112, with 24 attained by five members — and
  nothing outside the family in the first forty one-cusped census manifolds is on it. The atom chat1 named
  (R(e^{iπ/3}): real part π²/12 quantising the phase, imaginary part Vol(4₁)/2 setting the modulus) is verified on
  this bench; the derivation is Neumann's. Among the family's 41 chiral rank-one members: 14 at 0, 3 at ¼, 24 elsewhere
  on the lattice.

## 2b. The certificate that needs no enumeration (post-seal, on the audit lane's R92)

R92 (2026-10-04) observed that the isometries act on Spin(M) affinely and that a bounded word search plus the span of
the found sign characters does not certify a swap. A swap is a non-existence claim and can be certified another way: if
any orientation-reversing isometry fixed a spin structure s, then conj R_n^{(s)}(t) ≐ R_n^{(s)}(t^{±1}) and, with duality,
R_n^{(s)} is real up to a unit at real t. `verification/r92_certificate.py` → `r92_certificate.json` (n = 1, 3; t = 2, 3,
0.6; every spin structure) on the twelve rank-one members of the outside census:

| CS | members | spin structures with real odd torsion |
|---|---|---|
| ¼ | the family's seven (m003, m207, s955, s957, s960, t12838, o10_150695) | **0 on every one** (0 of 2, 2, 4, 4, 8, 2, 2) |
| ¼ | outside: m135, s463, s725, s881, s891, s911 | **0 on every one** (0 of 8, 2, 2, 2, 2, 2) |
| 0 | the family's six: m004, m206, t12839, o10_150696; s961; o10_150707 | 2 of 2 on the first four; 8 of 8; 4 of 8 |
| 0 | outside: s464, s726, s882, s892, s912 | 2 of 2 on each |
| 0 | outside: m136 | **4 of 8; the geometric lift not among them** — its swap is certified, the manifold's class is not |

(`verification/r92_certificate_family.py` reads the family's rows off B1475's and this arc's own tables with the same
test; no new torsion is computed for them.) **Twenty-five of twenty-five:** a rank-one amphichiral manifold read here
has a torsion-real spin structure exactly when CS ≡ 0.

So the thirteen ¼ verdicts stand on a route R92's objection does not reach. Realness is necessary for invariance, not
sufficient: the zero rows are consistent with invariant spin structures and do not prove them (an exhibited witness
does, where one was found). s880, s883, s948 have H₁ of rank two and are outside this route.

## 3. The Pin bit (sm:B1382 on main), and a corrected cell

The sealed C4 assumed C·C̄ is a scalar (Schur); that holds only when τ² is the identity. For a general reversing
automorphism τ, τ² is inner — τ²(g) = w g w⁻¹ — and **C·C̄ = ε·ρ(w)**, which is exactly the referee's "W·W̄ = +A".
`verification/pin_sign_fixed.py` (post-seal, disclosed; `phase_1c.json`'s C4 rows are the mis-specified cell, kept):
for the three reversing τ's of m004 whose w has length ≤ 7, ε = +1 and the two lifts get **opposite** Pin types (the
other lift's sign is ε·χ(w) = −1). So the knot's spin lift is the parent's Pin type — sm:B1382's theorem verified on
main by the matrix route, and the referee's exact script re-run (P5). **The two faces of one bit:** on the knot the
construction cannot assign the lift because it is the parent's Pin type (free, 1 bit); on the swap members the mirror
moves it. On m206 and t12839 the w's exceed length 7 — reported, not needed.

## 4. The theorem and A5, under the owner's rule

(a) *A knot complement in S³ with an orientation-reversing symmetry has both spin structures mirror-invariant*
(B279's argument: H¹ = ℤ/2; the S³-bounding spin structure is preserved by any symmetry of the pair; hence the other
too). A5 — SE2's torsion-free tie-break — selected the family's only H₁ = ℤ member, so by theorem it selected a
member in the "all" class. (b) The converse fails (m206, t12839, o10_150696 are non-knots in "all"). (c) The sister A5
excluded, m003, is the smallest member of "none", at CS = ¼. (d) **The owner's rule of 2026-10-04 — "existence
emerges from the family as object; we shouldn't tie ourselves to m004" — is the frame:** A5 selected a member; the
object is the family (B1418); the record's statements about m004 are statements about one member unless they say
otherwise. GENESIS v1.11 (`adoption/amend.py`) records the rule, narrows GAP6 to its hypotheses (§5), and locates
FK12's bit on the family.

## 5. GAP6 narrowed (GENESIS v1.11)

My v1.9 sentence "no index built on a flat bundle can tell 27 from 27̄; chirality is a statement about curvature"
dropped its hypotheses: it is Chern–Weil on a *closed* bulk. With the object as boundary the index carries the
boundary's η — a flat-structure quantity — and the record's own class index (B1297, firing at ±1, ±2 in B1418) and the
spin swap (B1474, B1475) are flat data that tell. Narrowed to: no characteristic-class index on a closed bulk
distinguishes 27 from 27̄ over a flat frame; the boundary's spectral data do, and reach discrete data, not continuous
values (L247's census: 107 of 173 value-kills on flat premises). Credit codex's R89 and chat1's handoff, the same day,
from opposite sides.

## 6. What it means, and what it does not

- For **chirality**: the fermionic bit's fate under the mirror is a computable, discrete family invariant, forced by
  CS = ¼; on seven members of the object no mirror-symmetric fermionic configuration exists; the sign of the hand
  remains the ℤ/2 the object does not pick. The step to a four-dimensional chiral count (B279's η link) is Phase 2.
- For **generations**: nothing; the law is about one bit.
- **The imported expectation, stated separately:** none. **0 of 19.**

## 7. Errors in this arc

The sealed C4 mis-specified (§3); `census_lists.py` first stored closed names without their fillings (SnapPy's `.name()`
returns the cusped parent) so the closed run first tested the parents — repaired, the parents' run kept as
`census_swap_closed_run_parents.txt`; o10_150696's stored presentation could not be re-found (`randomize()` is not
deterministic) — the shortest of forty retriangulations used and its mirror automorphisms re-found; P2 off by one
member; P7/P8 wrong as sealed; **and an over-reading of mine, caught before landing by the certificate R92 prompted:** the first draft of this page said "CS = 0 fails to protect a mirror-invariant spin structure outside the family" — the cells read only the geometric lift there, and m136's four torsion-real spin structures show the sentence was not supported. Corrected throughout; the manifold-level question is sealed next.

**Provenance.** `verification/phase_1c.py` → `phase_1c.json`, `phase_1c_run*.txt`; `census_lists.py` → `census_lists.json`;
`census_swap.py` → `census_swap_cusped.json`, `census_swap_closed.json`, runs; `pin_sign_fixed.py` → `pin_sign_fixed.json`;
`r14_axiom_checks_referee.py` (the review lane's, pinned 5d58b935) → `r14_rerun.txt`; `adoption/amend.py` → GENESIS v1.11.
Lock `tests/test_b1476_spin_swap_1c.py`. Cross-refs L246, L247, L248, B1474, B1475, B1239, B1224, B279, sm:B1382, chat1.

**Addendum, 2026-10-07 (R60-7, landed with S72).** Disclosed and repaired: `census_swap.py` (B1476) replaced the shared
`realness.setup` by its `setup_any` at *import*, so every module that imported `realness` afterwards in the same
interpreter saw the rank-free setup — B1477's `cusp_shear.py` worked around it by saving `R.setup` before the import,
and the live tests ran in fresh interpreters meanwhile. The replacement is now scoped to one verdict (a context manager
in `census_swap.verdict`, `realness.setup` restored after); the import has no side effect, the verdicts are unchanged,
both arcs' tests pass.
