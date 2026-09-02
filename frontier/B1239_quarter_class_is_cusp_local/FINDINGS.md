# B1239 — THE ¼ CLASS IS CUSP-LOCAL: codex R040 (free deck ⇒ CS = 0) reproduced, re-graded, and pushed two theorems further

**Date:** 2026-09-02 · **Seat:** cc (main) · **Source:** codex R040 `certificates/r040_free_deck_cs/` on `origin/codex/seat-r001`
(integrate-don't-merge: nothing merged, every number recomputed here) · **Lead:** L194 · **Wall:** B1234 row 13–14 (the k-blind wall)

**Verdict: PROVED (two statements, both corollaries of cited inputs) + VERIFIED (codex's census, sharpened by 58 orders) + the residue located.**

---

## THE PRIZE FIRST

L194 asked whether a *free* orientation-reversing deck involution kills the ¼ class of the Chern–Simons invariant — the
structural reason A6's orientation double covers sit at CS = 0 in 40/40 while amphichiral manifolds in general hit ¼ at
36 %. Codex's R040 answered "theorem for closed, census for cusped". Reading their chain on the bench with the one fact they
did not use — **SnapPy computes closed CS only mod ½** (CGHN p.14, read: *"If M is closed the Chern–Simons invariant is well
defined modulo 1, but Snap and SnapPea still only compute modulo ½"*) — the question resolves into three pieces of very
different grade:

1. **Closed manifolds: ¼ is excluded by ANY orientation-reversing isometry, free or not, and without Kawauchi.**
   APS (as printed in CGHN p.15): 3η(M) ≡ 2cs(M) + τ (mod 2), τ = number of 2-primary summands of H₁(M;ℤ). η is odd under
   orientation reversal and isometry-invariant, so η(M) = 0 for every closed amphichiral M; τ is an *integer*; hence
   2cs ∈ ℤ, cs ∈ {0, ½} mod 1, **cs ≡ 0 mod ½**. Kawauchi's theorem (free ⇒ Tor H₁ = A⊕A ⇒ τ even) only decides 0 versus ½
   mod 1 — the very distinction SnapPy's readout cannot see. **Tested on the entire closed census (11 031 manifolds): 37
   amphichiral, 37/37 zero class** (max distance 7.8 × 10⁻¹⁶), while the same census holds 17 quarter-class manifolds (all
   chiral) and cusped amphichiral manifolds hit ¼ at 11/25 in the first 3000 — the prediction discriminates and holds.
   `verification/r040_quarter_is_a_cusp_phenomenon.py`.

2. **Cusped manifolds whose reversing isometry fixes no cusp: ¼ is excluded — a corollary proved here** (the swap corollary,
   §3): fill each swapped pair (c, τc) along (s, τs); τ extends to the closed filling, whose cs lies in ½ℤ by (1); the two
   added core geodesics have torsions θ and −θ, cancelling exactly; CGHN's analytic term is therefore ≡ 0 mod ½ at every
   equivariant filling and tends to cs(M) as s → ∞. **Tested on the entire cusped census (61 911 manifolds, 2 804
   multi-cusped): bucket A (some reversing isometry fixes no cusp) 28/28 zero** (4.7 × 10⁻¹⁶); bucket B (amphichiral, every
   reversing isometry fixes a cusp) **6 zero / 5 quarter**; bucket C (chiral) 8 / 3 / 2754. The corollary's prediction is
   falsifiable — bucket B is where it would have failed — and it held. `verification/r040_swap_corollary.py`.

3. **The residue is exactly m004's own situation.** The ¼ class lives only on τ-invariant cusps. m004 is the orientation
   double cover of the Gieseking manifold m000, whose single cusp is a Klein bottle: τ fixes m004's cusp and acts on it
   freely (glide-reflection type). For that case there is **no theorem** — only two invariant slopes exist, so the limit
   argument of (2) has nothing to take a limit over, and odd-degree covers cannot change the cusp type (an odd cover of a
   Klein bottle is a Klein bottle). The data: **1260/1260 orientation double covers at zero class to 9 × 10⁻⁶⁴**, 1182 of
   them with Klein-bottle-type invariant cusps; and among amphichiral manifolds with a τ-invariant cusp, ¼ occurs (bucket
   B; and every one-cusped amphichiral manifold has one, which is where L194's 13 quarter-class 112-family members sit). **L194 is therefore refined, not closed:** the conjecture is
   now cusp-local — *an orientation-reversing isometry acting freely on every cusp it preserves excludes ¼* — with the
   proof burden reduced to one cusp type and a named tool (the cusped η–cs relation of Meyerhoff–Ouyang, cited, unread).

**What this does to the wall.** B1234's k-blind row (`FINDINGS.md:13`, "CS = 0 ⇒ ∂S/∂k = −CS = 0") rests on CS(m004) = 0,
which is *computed* (B1224/B1227) and stands untouched. What changes is the *explanation* A6 offered for it: "free deck ⇒
CS = 0" is now a theorem for closed manifolds (where freeness is not even needed), a theorem for cusp-swapping isometries,
and an open lemma precisely at the object. Under THE LENS this is a specification, and a sharp one: the structural reason
for the object's CS = 0 is a statement about a single Klein-bottle cusp.

---

## §1 Codex R040 reproduced (and what its certificate actually computes)

Codex's `free_deck_cs.py` has two blocks. The "closed theorem" block is a hard-coded parity chain (α = 0, η = 0 → 2cs ≡ 0)
that computes nothing; the theorem rests on two citations (Kawauchi 1981 Thm III; CGHN 2003 p.14–15). The census block is
real: 1260 `NonorientableCuspedCensus` → `orientation_cover()` → `chern_simons()` classified mod ½ at TOLERANCE 1e−6.

**Rerun here** (`r040_census_rerun.py`): 1260/1260 zero class at double precision (max distance 1.8 × 10⁻¹⁵ — codex's
tolerance is loose by nine orders) **and at quad-double** (`high_precision()`, max 9.04 × 10⁻⁶⁴, tolerance 1e−20). Quarter
class 0. Volume ratio 2 throughout; every cover orientable; 1260 distinct cover names (isometry-distinctness of the covers
not checked — irrelevant to a universal statement). Base cusp kinds: KB 861, KB+KB 311, KB+KB+T 10, KB+T 42, T 25, KB×3 9,
T+T 1, KB×4 1.

**Closed control** (`r040_closed_control.py`), which codex did not run: the 17 `NonorientableClosedCensus` manifolds →
orientation double covers → CS via the parent route (unfill all cusps, compute, refill; a direct call answers *"isn't
currently known"*). 17/17 zero class at ~10⁻⁶⁴; volume ratio 2; **Tor H₁ a square in 17/17** (ℤ/2+ℤ/2 ×5, ℤ/3+ℤ/3 ×2,
trivial ×10) and **τ even in 17/17** — Kawauchi's *conclusion* confirmed computationally on every closed case available,
though the paper itself remains cited-not-read (JSTAGE download truncated five times).

**The convention finding.** 300 closed-census CS values all lie in (−0.2476, 0.2487]: SnapPy's closed CS is reduced mod ½,
exactly as CGHN p.14 says. Consequence: codex's closed theorem (cs ≡ 0 mod **1**) has content — the exclusion of ½ — that
**no SnapPy number can test**. What the numerics test, closed or cusped, is the ¼ class mod ½. That reframing is what made
§2 visible.

## §2 The closed chain re-graded: what needs Kawauchi and what does not

| Statement (closed hyperbolic M) | Inputs | Grade | Observable? |
|---|---|---|---|
| cs(M) ∈ {0, ½} mod 1 for every M with an orientation-reversing isometry | APS relation (CGHN p.15, read); η odd under orientation reversal | THEOREM (cited inputs; derivation one line) | YES — 37/37 on the closed census, bite: 17 chiral at ¼ |
| cs(M) ≡ 0 mod 1 when the isometry is a **free involution** | the above + Kawauchi Thm III (cited, not read; conclusion 17/17) | THEOREM conditional on the citation | **NO** — SnapPy reduces mod ½ |

Codex graded the second row and offered the first row's evidence for it. The first row is the one the numbers touch, and
it does not need freeness. The 251/1260 cusped covers with τ odd (`r040_torsion_parity.py`; 697/1260 with non-square
Tor H₁) show the closed *mechanism* does not transfer to cusped covers — no contradiction, Kawauchi is a closed theorem — but
also that τ's parity was never what excluded ¼: an integer τ suffices.

## §3 The swap corollary (proved here from cited inputs)

**Statement.** Let M be a cusped orientable hyperbolic 3-manifold with an orientation-reversing isometry τ such that
τ(c) ≠ c for every cusp c. Then cs(M) ≡ 0 mod ½.

**Proof.** The cusps fall into τ-swapped pairs (c, τc). Choose a slope s on each c of a set of pair-representatives and fill
c along s and τc along τ(s). For s outside a finite exceptional set per cusp (Thurston's hyperbolic Dehn filling, multi-cusp
form) the result M′ is closed hyperbolic; τ extends over the solid tori (it carries the meridian of one to the meridian of
the other) to a fixed-point-free-on-cusps orientation-reversing homeomorphism, isotopic by Mostow to an isometry, so by §2
row 1, cs(M′) ∈ ½ℤ mod 1. By CGHN p.14 (read), cs(M′) = A(s) − (1/2π) Σ θᵢ where A is the term that varies analytically on
Dehn filling space and θᵢ are the torsions of the added core geodesics. The core geodesic in τc is the τ-image of the one in
c; torsion flips sign under orientation reversal and is isometry-invariant, so θ_{τc} = −θ_c and the sum vanishes exactly.
Hence A(s) ≡ 0 mod ½ at every equivariant filling. A is continuous into ℝ/½ℤ and the equivariant fillings converge to the
complete structure as s → ∞, where A equals cs(M) by definition; a continuous function vanishing along a sequence vanishes
at the limit. ∎

**Where it fails, and why the failure is the map of the residue.** If τ(c) = c, the τ-invariant slopes on c are the two
eigen-directions of a determinant −1 matrix: finitely many equivariant fillings, no limit. Odd-degree covers do not help
(an odd cover of a Klein bottle is a Klein bottle, so a τ-invariant cusp of Klein-bottle type lifts to τ̃-invariant cusps);
even-degree covers multiply cs by an even number, erasing the ¼ information. The ¼ class can therefore only occur on
τ-invariant cusps — and the census agrees to the manifold: bucket A 28/28 zero, every quarter-class amphichiral manifold in
bucket B.

## §4 The residue, and L194 refined

The one open case is a τ-invariant cusp. On such a cusp τ acts either with fixed circles (reflection type; the quotient has
a reflector cusp) or freely (glide type; the quotient has a Klein-bottle cusp). Free decks give only the second kind, and
there the census says zero 1182/1182 to 10⁻⁶⁴; amphichiral manifolds whose reversing isometries all fix a cusp reach ¼ (5
in bucket B; the 112-family's 13 quarter-class members of L194's bite control, none an orientation double cover). **L194 refined:** *an orientation-reversing isometry acting freely on every cusp it
preserves excludes the ¼ class.* Discriminating experiment: an amphichiral manifold with fixed points in the interior but a
free action on its invariant cusp — the refined conjecture predicts zero, the "free everywhere" reading is silent. SnapPy's
`Isometry` objects expose only the linear part of the cusp action (`cusp_maps()`), not the translation, so freeness on the
cusp cannot be read off directly; the instrument is a t3m-level trace of the vertex-link action (queued in L194). The
literature tool is the cusped η–cs relation (Meyerhoff–Ouyang 1997), **cited, not read** — if it takes the APS form with a
cusp-basis correction that a glide-type action kills, the residue closes by the §2 argument.

## §5 Placement

- **B1234 `FINDINGS.md:13–14`** (k-blind wall; "CS = 0 itself | B1224/B1227"): the computed CS(m004) = 0 stands; the
  structural gloss "A6's free deck selects CS = 0" is now: closed — theorem without freeness; cusp-swapping — theorem;
  invariant Klein-bottle cusp (m004) — open lemma, 1260/1260 evidence. Addendum in B1234.
- **B1235 cell 2 / A6** (40/40): superseded upward by 1260/1260 at 10⁻⁶⁴ plus the two theorems; addendum in B1235.
- **L194**: refined in place (text above), bite control extended, instrument named. Not closed; not a new lead.
- **Codex R040**: VERIFIED with three sharpenings relayed — (i) the numerics test ¼, not ½; (ii) Kawauchi is unnecessary
  for the observable statement and unobservable where necessary; (iii) tolerance 1e−6 is nine orders loose. Their scope
  declaration (closed = theorem, cusped = census only, no implication for B1234's other seven walls) is adopted verbatim.
- **Gate 5:** clean — no measured value anywhere in this cell.
- **Identifications:** none made (Identification Rule: the arc identifies nothing; the two isomorphism classes it names —
  "τ-invariant cusp" and "Klein-bottle cusp of the quotient" — are the same object by definition of the quotient).

## §6 Errors

**E52 instance #7 (mine, self-caught in one step).** My first amphichirality detector was `M.is_isometric_to(mirror(M))` —
the exact instrument B1181 used and B1235 retracted five days ago (SnapPy's isometry test is orientation-blind; it reported
5₂ ≅ mirror(5₂)). Caught by the chiral control before any number was written; replaced by `symmetry_group()
.is_amphicheiral()` (B1235's detector) and, for per-isometry work, `is_isometric_to(M, M, return_isometries=True)` filtered
by cusp-map determinant −1 — validated against `symmetry_group().order()` and `.is_amphicheiral()` on 600/600 census
manifolds, determinants consistent across cusps. Note for the toolbox: `isomorphisms_to()` does **not** canonize (m006: 2 of
its 4 symmetries) and is not a substitute. The two-sided control rule (E52) is what caught it; the class survives its
naming on the seat that named it.

## §7 Verification (all in `verification/`, all run 2026-09-02; `reproduce.sh` reruns the fast ones)

| file | what | result |
|---|---|---|
| `r040_census_rerun.py` / `.json` | codex's 1260-cover census at double + quad-double | 1260/1260 zero; max 1.8e−15 / 9.04e−64 |
| `r040_closed_control.py` / `.json` | 17 closed covers via the parent route; H₁ torsion | 17/17 zero; Tor H₁ square 17/17; τ even 17/17 |
| `r040_torsion_parity.py` | τ parity / squareness on the 1260 cusped covers; cusp-kind partition | τ odd 251; non-square 697; 26 all-torus bases, all zero |
| `r040_quarter_is_a_cusp_phenomenon.py` / `.json` | full closed census (11 031) amphichiral → class; cusped control | 37/37 zero; 17 chiral at ¼; cusped amphichiral 11/25 at ¼ |
| `r040_swap_corollary.py` / `.json` | full cusped census, buckets A/B/C by cusp permutation of reversing isometries | A 28/28 zero; B 6/5; C 8/3/2754 |
| `cghn_p14_p15.txt` | the two read passages (extracted from the PDF on the bench) | convention; APS relation as printed |

## §8 Fences — what is NOT claimed

- Nothing about the value of any physical constant; nothing about k beyond what B1234 already states.
- The closed row-2 theorem (cs ≡ 0 mod 1 under a free involution) is codex's and Kawauchi's; this cell adds only that it is
  unobservable by the tool used to support it and unnecessary for the observable statement.
- The swap corollary is a corollary of cited results (APS via CGHN; CGHN's filling decomposition; Thurston; Mostow); it is
  not registered as a programme law (`creates_law: false`, reviewed block in `arc_verdict.json`).
- L194's residue is OPEN. 1260/1260 at 10⁻⁶⁴ is evidence, not proof. Nothing here proves CS(m004) = 0 structurally; the
  computed value stands on B1224/B1227.
