# R08 — Recomputation cell: the generation obstruction (B298 / B307 / B1161)

Date: 2026-09-01. Discipline: BLIND-FIRST. Verdict summary: **MATCH on all banked numbers**,
with one **VACUITY note** on the pyenv/test-lock layer and one **scope note**.

## Files read BEFORE computing (claim capture only)
- `frontier/B298_generation_obstruction/FINDINGS.md` lines 1–25
- `frontier/B307_totally_real_obstruction/FINDINGS.md` lines 1–25 — NOTE: B307's head
  contains its proof sketch inline (unavoidable while capturing the claim); the theorem
  reconstruction below was still done independently with citations and step checks, and
  every census/field number was recomputed blind.
- `frontier/B1161_frontier_sweep/FINDINGS.md` lines 1–30
- NOT opened before computing: any `verification/`, `verdict.py`, arc `.py`, `tests/` lock,
  or `b1161_results.json`.

## Files read AFTER my numbers were on disk
`B307/FINDINGS.md` (full), `B307/totally_real_obstruction.py`, `B307/verdict.py`,
`tests/test_b307_totally_real_obstruction.py`, `B298/FINDINGS.md` (full),
`B298/generation_obstruction.py`, `B298/verdict.py`, `tests/test_b298_generation_obstruction.py`,
`B1161/FINDINGS.md` line 33 + `verification/reproduce.sh` + `verification/frontier_checks.txt`
+ `b1161_results.json` (grep).

## Blind computations (this dir)
- `blind_m004_trace_field.py` → `blind_m004_output.json`: m004 shapes (400-bit) both satisfy
  `x²−x+1` (algdep, residual-checked, irreducible); poldisc = nfdisc = **−3**; signature (0,1);
  primitive element of the whole shape field is degree 2 under two coefficient sets;
  `nfisisom` confirms ≅ banked `x²−x+1`. Holonomy traces (snappy HP): tr(a): `x²+3x+3`,
  tr(b): `x²−2x+4`, tr(ab) = −2 (rational), tr(aB): `x²−4x+16`, tr(abAB): `x²−3x+3` — all in
  `Q(√−3)`. By Neumann–Reid (cusped ⇒ shape field = invariant trace field) this is the
  invariant trace field. **B1161/B298 m004 claim: MATCH** (x²−x+1, degree 2, disc −3, Z/2).
- `blind_census_scan2.py` → `blind_census_output_v2.json`: OrientableCuspedCensus[:500],
  shape field per manifold via two-precision algdep (search at 500 bits, verify the relation
  at 1100 bits; threshold 1e−200·maxcoeff; irreducible; two independent primitive elements
  must agree). Result: **32 degree-3 fields / 500; all 32 signature (1,1); all 32 Galois S3;
  0 cyclic (C3); no cubic has square disc.** **B307 census claim: MATCH (32 / (1,1) / 0).**
  Caveat: 88/500 rows returned no field ID (high-degree fields beyond deg-24/precision
  bounds); a cubic cannot fail this pipeline at these settings (cubic relations have small
  coefficients; control m015 found instantly), so the count 32 is robust.
  v1 (`blind_census_scan.py`) is kept as an instructive failure: a single-precision
  `algdep` residual test accepts spurious low-degree relations and reported "all 500 degree 2"
  — exactly the E23-style instrument error this cell exists to catch, fixed in v2.
- `blind_controls2.py` → `blind_controls_output.json` (CONTROLS — the instrument finds the
  excluded thing when planted):
  * conductor-7/9/13 cyclic cubics: nfdisc **49/81/169**, signature (3,0), Galois A3=C3,
    disc square — matches B307's side facts exactly;
  * a planted fake "manifold" whose shape list generates the conductor-7 C3 field, pushed
    through the SAME field_of_shapes→classify path as the census: flagged **C3** (nfdisc 49);
  * m015 = 5₂: cubic, nfdisc **−23**, signature (1,1), **S3** — matches the banked 5₂
    refutation; `nfisisom` confirms my `x³−64x+512` ≅ their `x³−x²+1` (`after_phase_checks.json`);
  * all 127 cyclic cubics of conductor < 200: totally real (3,0).
- `after_phase_checks.json`: also re-verified B298's route "3-fold covers of m004": snappy
  gives exactly **1** cover, `H1 = Z/4 + Z/4 + Z` — **MATCH**.
- Note: cypari 3.3.2 here double-frees tearing down `polsubcyclo` t_VECs (crash at GC /
  interpreter exit, results computed correctly before it); worked around via keepalive +
  `os._exit(0)` after writing JSON.

## Independent reconstruction of the B307 theorem (done before reading their proof body)
**Theorem.** The trace field and invariant trace field of a finite-volume hyperbolic
3-manifold — in particular any hyperbolic knot complement — are never totally real; since a
cyclic cubic (C3) field is totally real, no hyperbolic knot has a C3 (invariant) trace field.

Step 1 (C3 ⇒ totally real): K/Q Galois of degree 3. If τ: K→C were non-real, normality gives
σ(K)=K for all embeddings, so τ⁻¹∘(complex conjugation)∘τ ∈ Gal(K/Q) has order 2 — impossible
in a group of odd order (Lagrange). Cross-checks: Kronecker–Weber puts K inside Q(ζ_f)⁺
(odd degree can't meet the index-2 imaginary layer) — Washington, *Cyclotomic Fields*, Ch. 2;
conductor–discriminant gives disc = f² > 0, and a cubic with positive disc has 3 real roots.
Empirically re-verified: 127/127 cyclic cubics of conductor < 200 have signature (3,0).

Step 2 (hyperbolic ⇒ complex place): Γ ≤ PSL(2,C) discrete, finite covolume, hence
non-elementary/irreducible. If all traces were real, the irreducible rep would be conjugate
into SL(2,R) or SU(2); SU(2) discrete ⇒ finite (compactness), and PSL(2,R) stabilizes a
totally geodesic H² ⇒ infinite covolume in H³ — both impossible. So the identity embedding of
KΓ (and of kΓ, applying the same to Γ^(2)) is a complex place; neither field is totally real.
Citations: Reid, "A note on trace-fields of Kleinian groups", Bull. LMS 22 (1990);
Maclachlan–Reid, *The Arithmetic of Hyperbolic 3-Manifolds*, GTM 219, §3.3 (Thm 3.3.7);
Neumann–Reid, "Arithmetic of hyperbolic manifolds" (1992) for shape field = invariant trace
field on cusped manifolds. Steps assessed sound; the theorem is stronger than the knot claim
(all finite-volume manifolds, all totally real fields, any odd-order-Galois field — not just C3).

## Diff against the banked proof (read after)
B307 uses **exactly this route**: (i) C3 ⇒ Galois ⇒ no order-2 automorphism ⇒ no complex
embedding ⇒ totally real; (ii) invariant trace field always has a complex place (they cite
Maclachlan–Reid); (iii) disjoint. Sound. Their parenthetical "(the geometric rep is not
conjugate into PSL(2,R))" compresses step 2 — the full argument also needs SU(2) excluded —
but the cited Maclachlan–Reid theorem carries it; not an error. Their census instrument
(`totally_real_obstruction.py`, sage: `invariant_trace_field_gens().find_field(prec=200,
degree=6)`) is methodologically independent of mine (shape field + two-precision algdep)
and we agree number-for-number: 32 / all (1,1) / 0 C3.

## VACUITY note (layer-specific, does not touch the claims)
The pyenv `verdict.py` + `tests/test_b307_*.py` lock encodes the census results as hardcoded
constants (`N_CYCLIC_C3 = 0`, `CUBIC_SIGNATURES = {(1,1): 32}`) and asserts them — that layer
could not have failed and is a transcription lock, not a check (same pattern for B298's route
table and B1161's `reproduce.sh`, which recomputes disc/degree of the *hardcoded* poly
`x²−x+1` but not the identification with m004). The real instruments (B307's sage scan,
B298's snappy cover count) are genuine, and this cell independently re-verified both the
identifications and the counts, so the vacuity is confined to the lock layer.

## Fence / scope check — PASSES
The obstruction forbids only the single-object Z/3-symmetric-triple (Galois-C3-trace-field)
route. Banked statements respect that: B307 says "three generations, **if arithmetic**, come
only from multiplicity" and routes the 3 to the commensurability class (B302) — explicitly
relational, not single-object; B298 calls the orbifold-3 an *external input* (not forbidden,
just not object-paid) and labels the cubic-carrier statement a conjecture; B1161's row says
the honest object content is one generation and the "3" is external. Minor wording note:
`verdict.py`'s bare constant `GENERATIONS_FORCED_TO_MULTIPLICITY = True` ("the only route
left") reads stronger than the theorem alone licenses — the FINDINGS' "if arithmetic"
qualifier is the correct scope, and the FINDINGS carry it.

## Verdicts
- **B1161/B298 (m004 field): MATCH** — banked x²−x+1 / deg 2 / disc −3 / Z/2; mine identical
  (two routes: shapes + holonomy traces).
- **B307 theorem: MATCH (sound)** — my independent reconstruction is the same argument;
  each step checks out with classical citations.
- **B307 census: MATCH** — banked 32 / all (1,1)=S3 / 0 C3; mine 32 / 32×(1,1) / 0, by an
  independent method, with a passing planted-C3 control.
- **Side numbers: MATCH** — 5₂ disc −23 S3 (1,1); C3 targets 49/81/169 all (3,0);
  m004 3-fold covers = 1 with H1 = Z/4+Z/4+Z.
- **Lock layer: VACUITY (noted)** — hardcoded-constant asserts could not have failed;
  claims themselves verified here independently.
