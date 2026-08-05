# HANDOFF TO CC — THE SELECTION & QUANTUM-COCHAIN CAMPAIGN (from seat cc3, 2026-07-17)
# For: verify -> bank -> push. cc assigns B-numbers; cc3 proposes structure.
# Provenance: cc3 = the owner's third seat (cloned from cc2 2026-07-17,
# structurally detached, own root [machine-path]). This is cc3's
# first originated campaign, owner-approved. Repo synced through B670
# (6442258) at campaign time. Repo untouched by cc3; Gate 5 never
# approached; all compute sonnet agents; preregs sealed BEFORE compute
# (PREREG_SCC.md cdd2cd39, wave-2 addendum in same file, final 84ba1c96 —
# SEALS.txt has the full hash chain in order).

## RECONCILIATION ADDENDUM (cc3, 2026-08-03) — read this before the claims below
Repo refetched: campaign-time B670 (6442258) -> now synced through B862
(9f055eef), ~180 bank entries later. NONE of the six claims below are
banked anywhere under any name (checked by content, not just title).
BUT three of the six overlap existing banked law in ways this addendum
corrects, so cc doesn't spend verification time re-proving what's
already in LAW_MAP/OPEN_LEADS. Per-claim disposition:
- C1: GENUINE, reframed. LAW_MAP already has unit-det<=>prime-conductor
  as "the same criterion" -- but only on B664's ONE-PARAMETER metallic
  slice (R^{n-2}L). What's new here is the SAME equivalence verified
  across the FULL 745-class primitive family, not the slice. Bank as an
  extension, not a fresh discovery.
- C2: GENUINE. LAW_MAP's existing non-uniqueness note ("NOT golden-
  unique: quiet+real recurs at n=3,12 mod 15") is a narrower, slice-
  internal periodicity fact. C2 tests strata-intersections across the
  FULL family and is a different, broader computation. Stands as-is.
- C3: DOWNGRADE to corroboration, not a law. LAW_MAP's shadow-class law
  entry (B665/B666) already gives the five-value set {0,1/phi,1,phi,2}
  as the general form, with its own bracketed caveat that the "for ANY
  word" universal claim is CONJECTURE, "supported not sealed" (a 547-
  word sample corpus, for a different stage). C3's 745-class computation
  is a complete enumeration to length 12, not a sample -- genuinely
  stronger evidence for the value-SET claim than what's banked. BUT:
  w2b_table.json has no mod-5 shadow-class column, so this never checked
  the POINTWISE formula (each word's value against its own shadow
  class), only the aggregate value distribution. Correct claim: "the
  achieved value set matches B665's law exactly, verified complete (not
  sampled) on all 745 primitive classes to length 12" -- a corroborating
  data point, NOT a new law, NOT a formula-level verification, and NOT
  independent of B665 (which is the law C3 is corroborating).
- C4, C5: GENUINE, confirmed distinct on inspection. Silver-uniqueness
  language recurs elsewhere in the repo (B471's commutator-parabolicity
  uniqueness, B360's bright/dark selection rule) but those are about
  metallic-PAIR commutators, a different object from C4's amphichiral-
  stratum uniqueness. B670's own "16 words x 12 stages" matrix is an
  unrelated, differently-indexed word list (a coincidental "16", not the
  d=5 field-class count C5 reports). Both stand as new.
- C6: GENUINE, the headline. Zero trace of the amalgam-wall/even-solo
  construction anywhere in the ~180 new entries.
NONE of this touches cc's current active threads (the SM global-form
cascade B862, the SSB/KMS reframe B848-852, the gated W3 Habiro/GSWZ
design cell) -- unrelated mathematics. This is atlas material for a
lull, not an interrupt.

## THE SIX CLAIMS (exact statements; scope labels are part of the claim)

C1 THE COLLAPSE THEOREM [proven, all 745 primitive classes, length <= 12]:
disc = (tr-2)(tr+2) with tr >= 3 forces: prime conductor <=> tr-2 = 1 <=>
unit det(A-I) <=> tr = 3; and trace 3 is realized by exactly one class
(RL; class number 1 at disc 5). Three banked criteria are ONE criterion.

C2 THE DEFLATION [computed, length <= 12]: no combination of the strata —
amphichirality (53 classes), prime-discriminant field (8 d-values:
{5,13,17,29,37,53,173,229}; 11 classes jointly with amphichirality),
clean field (52/53), landscape minimal-nonzero-real (51 classes) — cuts
to {RL} without C1. "Why disc 5" = "why minimal hyperbolic trace" +
corroborating strata. CONSEQUENCE: L91's "five independent criteria"
narrative needs restating (amendment proposed below).

C3 THE FIVE-VALUE SET, CORROBORATED [computed exactly, all 745; NOT a
new law -- see reconciliation addendum above]: |tr_odd| at SU(3)_2 takes
exactly five values family-wide: {0, 1/phi, 1, phi, 2}, with |tr_odd|^2
counts 188 / 153 / 249 / 147 / 8. This is the value set already given by
B665/B666's shadow-class law; the contribution here is that it is
verified on the COMPLETE primitive family to length 12 (745 classes, not
a sample), which is stronger corroboration for the law's "for ANY word"
generalization than the existing 547-word sample corpus -- but this
computation never checked the POINTWISE formula (per-word mod-5 shadow
class vs. value), only the aggregate distribution, so it does not itself
seal that conjecture. IDENTIFICATION (still holds): this set = 2 x THE
TONES (the 2I class cosines, B641). Bank as a corroborating data point
under B665, not as a standalone law.

C4 THE SILVER COROLLARY [computed, length <= 12]: among the 53
amphichiral classes, exactly ONE has cyclotomically entangled eigenvalue
field (d in {2,3,6}): the silver R^2L^2 (d = 2). The bifocal-entanglement
phenomenon is silver-unique within the amphichiral stratum.

C5 FIELD COMMUNALITY [computed, length <= 12]: d = 5 is realized by 16
distinct classes (incl. R^4L^4, tr 18) — the golden FIELD is communal;
the golden WORD is what is unique. (Kills any "unique clean field"
reading; W0b's golden-question falsified as posed, banked un-softened.)

C6 THE QUANTUM AMALGAM WALL + EVEN-SOLO NO-GO [exact, levels 1-4]:
deformation-type quantum-cochain targets are dead (Ocneanu rigidity:
DY H^2,3 vanish; surviving H^1_DY discrete Z/3; separately Maschke kills
finite-group H^1 readings). The mapping-torus/amalgam model (design
DESIGN_DA.md d7082991) gives h^1(D_q) = 0 (T-boundary) or 6 (trivial
boundary) at kappa 5 — MISMATCH vs classical 5 — and the NO-GO LEMMA:
h^1(M') = h^1(M) identically (ker(A-I) = ker(A^-1-I)), so the model's
solo term is always even; the classical 2+3 split is structurally
unreachable in this model class. The weld's linear stage action carries
no image of the classical cochain structure. kappa = 5 not singular in
{4,5,6,7}.

## VERIFICATION HOOKS (verify-don't-trust; cheapest decisive first)
V1 (1 min): C1 is two lines of algebra + the class-number fact; verify
the enumeration counts per length = (1,2,3,6,9,18,30,56,99,186,335)
against Moreau's necklace formula, total 745.
V2 (5 min): rerun w2a_amalgam/w2a_amalgam.py (17 s) — reproduces the
mismatch table + controls; verify the no-go lemma by hand (one line).
V3 (10 min): with cc's OWN B664 machinery, recompute tr_odd for: the
slice n = 3..14 (must match W2b's gate rows), the silver R^2L^2 (= 1,
real), R^4L^4 (must be minimal-nonzero AND real — RL-nonuniqueness
witness), and any 10 random rows of w2b_landscape/w2b_table.json; then
check the family value-set is exactly {0, 1/phi, 1, phi, 2} on the
sample and the counts on the full table.
V4 (5 min): recompute the amphichiral count (canonical(swap(reverse(w)))
== canonical(w)) and the entangled-amphichiral uniqueness (C4); the
prime-disc d-set (C5/W0b) independently.
V5 (opt): cross C4/W0c against SnapPy geometric amphichirality (B669
already has silver amphichiral — consistency expected, not assumed).

## PROPOSED BANK STRUCTURE (cc's numbering; revised per the addendum)
B-a: C3 as a ONE-LINE CORROBORATION under the existing B665/B666 shadow-
class law entry (complete-family confirmation of the value set to
length 12) -- NOT a new law row. B-b: C1+C2 as the SELECTION THEOREM +
the L91 amendment: replace "five independent criteria select the golden"
with "trace minimality selects; amphichirality, field cleanliness, and
landscape minimality are corroborating strata (shared by 53/52/51
classes resp.); the slice landscape theorem (B664) stands unchanged on
its slice; the unit-det<=>prime-conductor equivalence now verified
family-wide, not just on the slice." B-c: C4+C5 as corollaries to the
bifocal record (B663/B649) -- confirmed distinct from B471/B360/B670 on
inspection (see addendum). B-d: C6 as the quantum-cochain wall (with
DESIGN_DA.md as the sealed design; frontier feeds: tube-algebra
Hochschild [PRICED: needs SU(3)_2 F-symbols], Eichler-Shimura/Gamma(5)
[converges with L108]) -- this is the one item worth cc's attention;
the rest is atlas housekeeping.
Frontier feeds: the pointwise shadow-class formula itself (per-word mod-
5 class vs. value) was never checked here and would upgrade C3 from
corroboration to an independent proof if done; the 8 loudest classes
(|tr_odd| = 2) structure; the 51-member real-minimal stratum's
characterization.

## ARTIFACT MANIFEST (sha256 in SEALS.txt, chain order = seal order)
PREREG_SCC.md (final 84ba1c96) | SYNTHESIS_DB.md 2f5dcbe5 | DESIGN_DA.md
d7082991 | CAMPAIGN_CLOSE.md 031b615b | w0a_criteria/ (falsifier
SURVIVES; 745-class table) | w0b_fields/ (W0b FINDINGS: golden-question
FALSIFIED as posed) | w0c_inventory/ (23 banked + 8 refuted + 4 missing,
all cited) | w0d_quantum_scout/ (rigidity analysis + probe) |
w2a_amalgam/ (FINDINGS_CC3 07a2d6a8) | w2b_landscape/ (FINDINGS_CC3
ba3d48af; full 745-row table) | STATUS.md | SEALS.txt.
Packet: OA_CC3_selection_cochain_campaign_2026-07-17.zip (~/Documents + cc3
seat-work; sha printed at delivery, re-hashed after this handoff joined).
Main-seat verifications performed at cc3: one W0a row recomputed by hand
(LLRRLR: tr 15, disc 221, amphichiral — exact match); the W0a x W0b
strata cross run independently of both agents; W2b's tone identification
checked exactly (phi^2 = (3+sqrt5)/2 etc.).

## WHAT NOT TO BANK: C3-beyond-745 (conjecture only); any physics reading
## of any of this (none exists; Gate 5 untouched); the W2a boundary-
## convention choice as canonical (both conventions reported, neither
## tuned — the wall holds under both).
