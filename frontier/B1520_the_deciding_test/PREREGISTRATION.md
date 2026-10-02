# B1520 — PREREGISTRATION: THE DECIDING TEST ON THE BRIDGE'S VACUA — does the bridge's symmetric potential have a vacuum that no chirality-flipping symmetry fixes?

**Sealed 2026-10-02, before the two conjugacy routes, the follow-up and the read-out are run on the population.** Seat: cc (the
SM-derivation branch). Occasion: the owner's selection-rule handoff (`chat1_HANDOFF_SELECTION_RULE.zip`, sha-256
`655959b292c4bd95dc958f6b06be1b7c06473cc1254eba206e2a88a14be69499`; its handoff file `73c12046…`, its script `f73515af…`), sent to
this seat with: *"one vety important task, whenever its best time for you: you have my go just makensure you do it correctly,
informedly, and bug free in all load bearing math"*.

**What kind of seal this is.** The outcome on the population is largely decided by exact results already banked: this seat's B1512
(2026-10-01) and the audit lane's R47 (F14). §0 states what they decide. This seal fixes, before anything runs on the population:
- new code that shares nothing with B1512 or R47;
- two routes that share nothing with each other;
- the controls;
- the expected values, with priors.

A disagreement between the new code and the record will be reported as a discrepancy, never fitted. Main's B1455 (sealed, not run)
asks the same question; this is an independent run of it.

## 0. PRIOR ART: seen first, the repo and then the literature

**The repo sweep.**
- `scripts/checks/prior_work.py` on ten terms, after `git fetch --all`. The terms: selection rule, spontaneous, mirror-symmetric,
  dual family, strong inversion, amphichiral map, Ballas, 1/q, count-odd, charge conjugation. Every term is present on the heads.
  "count-odd" occurs only in main's B1455 PREREGISTRATION, this seat's B1519 FINDINGS and one B774 data file (unrelated).
- The heads, re-fetched just before the seal: main `12ed66bd`, this branch `27220af6`, the audit lane `1e3d17b9`, and two seat
  lanes, neither merged:
  - `seat/magical-wright-vwrmtt` `0043be2b`, a gate fix, unrelated;
  - `seat/determined-hopper-t1cmii` `e5f1aebf`, built on this branch: a creates_law re-audit of B1304–B1513, unrelated to this
    test.
- The audit lane moved from `69d6d0b9` to `1e3d17b9` during the design. Its new relay
  (`CODEX_TO_CC_AND_SM_2026-10-02_ACT_REGISTER_AND_V1_2.md`) and `ACT_REGISTER.md` were read. They state: *"Main B1455 is not
  duplicated and is not extended to R77's changed source theory."* The relay's three requests on GENESIS v1.2 are answered after
  this arc, through the arc process. They concern FK12's never-reads sentence, B723's two retractions and B130's elimination
  inference, and none bears on this test.
- Main's `topic_sweep.py` (run from a checkout of main): *VERDICT topic-sweep
  /spontaneous|symmetry.breaking|mirror.{0,30}(pair|orbit|minim|vacu|fix)|selector|selects|plenitude|totalitarian|dual family|1/q|
  Ballas|strong inversion|amphichiral map/: 100 of 1327 arcs on main match (NEGATIVE 14, OPEN 11, PROVED 74, RETRACTED 1); 7 other
  lanes match*.

**Read in full:**
- the handoff and its script;
- main's B1455 PREREGISTRATION;
- the audit lane's selection-rule intake (`9b566262`), its R77 relay, its act-and-register design (`69d6d0b9`) and its
  act-and-register milestone (`1e3d17b9`);
- R47's F14 (FINDINGS and CORRECTION) and R76 (FLAT_VACUUM);
- this seat's B1512 (PREREGISTRATION §3 and FINDINGS) and B1509's index instrument.

**Read at verdict-line level:** B128, B849, B1204, B1225, B1227, B1327, B1328 and B561.

**What the record already decides.** B1512's lemmas, each with an explicit exact intertwiner, state four facts:

| map | effect on Ballas' family ρ_q | B1512 |
|---|---|---|
| ι, the fibre's hyperelliptic involution (orientation kept) | fixes ρ_q | Lemma I, det C = 16q² |
| ε, the strong inversion (orientation kept) | ρ_q ≅ ρ_{1/q}∘ε | Lemma E, det E = 16q⁴ |
| α, the amphichiral map (orientation reversed) | ρ_q ≅ ρ_{1/q}∘α | Lemma A, det A = −16q³ |
| duality V ↦ V* | ρ_q* ≅ ρ_{1/q} | Lemma D, det D = −16q(q² + q + 1) |

B1512 also proved the index statements this test needs:
- L1, invariance under any automorphism that carries the peripheral subgroup to a conjugate (Lemma A, Consequence 4);
- the duality sign flip with the dual at 1/q (Lemma D, Consequence 3).

Together these imply:
- duality composed with ε fixes every ρ_q, which is outcome A for the chirality-flipping symmetries;
- εα, which reverses orientation, fixes every ρ_q;
- α alone pairs q with 1/q.

R47's F14 is the same statement for θ (inversion of both generators), with an explicit J(q). Since det J ≠ 0 for q > 0, θ is ε up to
ι, the deck and an inner automorphism (B1512 Lemma E).

**Main's B1455 does not cite B1512.** B1512 decides its predictions P2–P4 and P6. Its P1, that all eight simple maps
(m, n) ↦ (m^a, n^b), (n^a, m^b) are automorphisms, was found false at this arc's design. Only the four with a = b satisfy the
relator, and all four keep orientation (disclosed in §3; `symmetries.json`). Main will be told after this arc banks, so that B1455
can run blind if main wishes.

**The literature.**
- S. A. Ballas, *Finite volume properly convex deformations of the figure-eight knot*, arXiv:1403.3314v3 (sha-256 `36f54787…`).
  Pages 1–2 and 17–19 read, and all 21 pages searched for "dual", "orientation", "symmetr", "amphichir", "involution", "invert"
  and "inverse" (only "dual" and "orientation" occur, in unrelated senses). It gives:
  - the generators M_t, N_t (p. 17);
  - ρ_{1/2} hyperbolic;
  - the ρ_s pairwise non-conjugate (p. 2);
  - s = log(1/(16t⁴)), so q = 2t and q ↦ 1/q is s ↦ −s.

  Ballas–Long (all s) is cited through Ballas' Remark 1.2 and was not read.
- Skolem–Noether: every automorphism of a central simple algebra over a field is inner.
- Mostow–Prasad: Out(π₁M) ≅ Isom(M) for M hyperbolic of finite volume.
- The vacuum condition is the audit lane's R76: a stationary flat point of finite energy is harmonic, and the non-split extension's
  potential a t² + c t⁴ is lowest at the split limit. R76 cites Corlette and an equivariant cutoff argument; neither is re-derived
  here.

## 1. The question, exact

**The bridge's vacua (hypothesis H-vac, from R44, R54 and R76; not re-derived).** In the harmonic frame (GENESIS F-HE) on m004 at
level one:
- the vacua are flat bundles V_{q,μ} = μ ⊗ ρ_q (q > 0, μ ∈ ℂ* a central twist) with their harmonic metrics;
- at the exceptional points, also their split sums with trivial lines.

Uniqueness of the harmonic metric (R47's F13, as R47 cites it) makes a vacuum fixed up to gauge exactly when its flat bundle is
fixed up to isomorphism.

**The maps.** Out(π₁ m004) has eight classes. With duality, they give sixteen maps Φ = (σ, d): Φ(V) = σ*V for d = 0 and (σ*V)* for
d = 1.

**Lemma P (the potential is invariant).**
- R76's potential is the symmetric-space bienergy of the equivariant map f.
- An isometry σ of m004, of either orientation, preserves the Riemannian measure, hence the bienergy of f∘σ̃.
- For V* the equivariant map is P ↦ P^{−T} applied to f, an isometry of GL(n, ℂ)/U(n); target isometries preserve tension and
  bienergy.
- So V(Φx) = V(x) for all sixteen maps. The handoff's step 2 holds by a proof, not a sample.

**The index (main's B1297/B1446 class index).**
- L1: I(σ*V) = I(V) for every σ (B1512 Lemma A, Consequence 4; main B1455 L1).
- L2: I(V*) = −I(V) (the definition).
- L3: if Φ(V) ≅ V for some Φ with d = 1, then I(V) = 0 (main B1455).

The count-odd maps are the eight with d = 1.

**The test (the handoff's §4 made exact).** For every vacuum V_{q,μ}, is there a count-odd Φ with Φ(V_{q,μ}) ≅ V_{q,μ}? For each of
the sixteen maps, the run records:
- its action on the family: fixes q, sends q ↦ 1/q, or leaves the family;
- its action on the twist, μ ↦ μ^e with e = (σ's sign on H₁ = ℤ)·(−1)^d;
- its orientation.

## 2. Lemmas used by the instruments (proved here)

**Theorem T (route 2's criterion).**
- *Setting.* Let A, B be representations of ⟨m, n⟩ in GL₄ over a field K. Let w₁ = (empty), w₂, …, w₁₆ be words with
  G_ij = tr A(w_i w_j) invertible.
- *Statement.* If tr B(w_i w_j) = G_ij and tr B(w_i g w_j) = tr A(w_i g w_j) for g = m, n and all i, j, then A and B are conjugate
  over K.
- *Proof.*
  - The A(w_i) are a basis of M₄(K). The B(w_i) have the same Gram matrix, so they are a basis too.
  - The coefficients of A(w_i)A(g) in the basis are G⁻¹ times the traces tr A(w_i g w_j). The same traces give B(w_i)B(g) the same
    coefficients, since the trace form is nondegenerate.
  - So the linear map φ: A(w_i) ↦ B(w_i) satisfies φ(X A(g)) = φ(X) B(g), and by inverting, φ(X A(g)⁻¹) = φ(X) B(g)⁻¹.
  - With φ(I) = I this gives φ(A(w)) = B(w) for every word, so φ is an algebra automorphism of M₄(K). Skolem–Noether makes it inner.
- *Application.* Over K = ℚ(q) the entries are Laurent polynomials, so every trace equality is an exact identity. det G is a
  Laurent polynomial; at the design run it has no positive real root, so the criterion also holds over ℝ at every single q₀ > 0.
  A single unequal trace proves non-conjugacy over ℚ(q).
- *The exact locus.* At q₀ > 0 the two are conjugate if and only if all 768 Theorem-T traces agree at q₀: "if" by the theorem at
  q₀, "only if" because traces are class functions. So the set of q > 0 where a pair is conjugate is the set of positive roots of
  the gcd of all the nonzero trace differences. Route 2 computes that gcd exactly.

**Lemma Tw (the twist).** Φ(μ ⊗ ρ_q) = μ^e ⊗ Φ(ρ_q), since σ acts on H₁(m004) = ℤ by its sign and dualising inverts a character. So
a map that fixes q fixes μ ⊗ ρ_q for every μ when e = +1, and only for μ = ±1 when e = −1.

**Lemma G (the gauge lift in E8).**
- Every automorphism of e₈ is inner, since the Dynkin diagram has no symmetry. So the Chevalley involution ω (−1 on a Cartan 𝔥,
  e_a ↦ −e_{−a}) is Ad(g) for some g in E8 (the adjoint group).
- On a regular subalgebra sl₅ ⊕ sl₅ sharing 𝔥 (A4 + A4 by Borel–de Siebenthal), ω restricts to an automorphism of each factor
  that is −1 on its Cartan. Any such automorphism of sl₅ is X ↦ −Xᵀ followed by conjugation by a torus element. On the group
  this is g ↦ g^{−T} up to an inner automorphism: duality on both SL(5)'s.
- So the count-odd map duality∘σ, for a vacuum carried by the hidden SL(5), is the E8 gauge rotation Ad(g) composed with the
  isometry σ. On the 4d gauge group, the commutant SU(5), Ad(g) acts as charge conjugation.
- *Orientation.* When σ keeps orientation, the map is a symmetry of any E8-gauge-invariant, diffeomorphism-invariant action. When
  σ reverses orientation, it is a symmetry only of an action that is also parity-invariant, since a Chern–Simons term changes
  sign. The expected witness D.θ keeps orientation, and `decide.py` lists every count-odd map that fixes all vacua and keeps
  orientation.
- A vacuum fixed by such a map has an unbroken charge conjugation. The map commutes with 4d Lorentz transformations and sends a
  left-handed field in R to a left-handed field in R̄, so the 4d spectrum is vector-like in every SU(5) representation.
- `lift_e8.py` checks w₀ = −1 in W(E8) and the regular A4 + A4 (run at design; standard facts).
- *Fences.* The end conditions (GENESIS GAP2) must be σ-invariant. The full spinor and domain transport the audit lane asks for is
  not done.

## 3. The instruments (committed with this seal)

**Run before the seal (design-time structure, disclosed, not outcomes):**
- **`symmetries.py`** (`symmetries.json`).
  - The eight classes of Out(π₁): V = {id, θ, s, sθ} (θ inverts both generators, s swaps them) and τV, with τ: m ↦ m, n ↦ nmn⁻¹.
    Each is checked as an automorphism with the faithful geometric representation over ℚ(√−3) (own arithmetic).
  - Orientation by the trace of σ(m)σ(n): 2 + z kept, 2 + z̄ reversed. V keeps orientation and τV reverses it.
  - SnapPy: D4, order 8, amphichiral.
  - Main's eight simple maps: the four with a ≠ b are not endomorphisms.
- **`route_intertwiner.py --controls-only`**, **`route_traceform.py --controls-only`**, **`followup_index.py --controls-only`**,
  **`lift_e8.py`**: their outputs are committed.
  - Route 1 controls (C1–C10):
    - the identity and a rational conjugate are found isomorphic; ρ_{2q} and ρ_{1/q} (with no map) are not;
    - exact solving at an irrational point (the real root of x³ − x − 1, in the number field it generates): ρ against itself has a
      one-dimensional space with an invertible element, and ρ against ρ_{2q} has none;
    - a pair whose only intertwiner is singular (diagonal characters sharing one value) is reported not isomorphic;
    - at q = 1, ρ_q and ρ_{1/q} coincide and are found isomorphic;
    - the banked identities below (C9, C10).
  - Route 2 controls (C1–C7): the same four pairs, the relator, the gcd on known polynomials and the banked trace (C7). The exact
    loci are every q > 0 for the two positive pairs, none for ρ_{2q}, and exactly q = 1 for ρ_{1/q}.
  - Route 2's sixteen-word basis has a Gram determinant with all coefficients positive, so no positive root.
  - Follow-up controls: the identity alone, bare and dualised, at all six prime–root pairs. They give I(W₁) = −1 (B1509's banked
    value) and I(W₁*) = +1 (the definition, L2). Neither is an outcome.
  - E8: w₀ = −1, and A4 + A4 is regular.
- **A design fault, found and fixed before the seal.** Route 1 as first written would have counted a generator with det X ≡ 0 as
  an isomorphism, since it found no positive zeros of the zero polynomial. Control C7 now catches it. The invertibility test at a
  zero was also a fixed rational combination; it is now exact, the determinant of a generic combination as a polynomial in its
  coefficients. Logged in ERROR_LEDGER.
- **`decide.py`** reads the outputs. It reads no outcome ("undecided") if the two routes disagree on any of the 32 decisions, if
  route 2's Gram determinant has a positive root, or if any control or banked identity of the symmetries, the routes or the lift
  failed in the population run. It scores P1–P6 mechanically as written in §4. Its logic was tested at design
  on synthetic tables only, never on a computed one: A, B, C, undecided, and a failed follow-up each read as intended.

**BANKED IDENTITY:** each instrument reproduces banked values inside itself before its new numbers are read. The full runs repeat
the controls, and the read-out reads no outcome if any fails.
- Route 1 (sympy) and route 2 (own Laurent arithmetic), each on its own: the relator mnMNmNMnmN holds for ρ_q, and
  tr ρ_q(nMNmmNMn) = 3q + q⁻³, the longitude trace banked in B1510 (FINDINGS §2, Lemma R). These are route 1's C9–C10 and route 2's
  C5 and C7.
- The follow-up: I(W₁) = −1 at all six prime–root pairs (B1509, banked), computed in every row before any image is read. P6
  needs it.

**Run after the seal (the population):**
- **R1, `route_intertwiner.py`.** The intertwiner equations solved over ℚ(q), for 16 maps × 2 targets.
- **R2, `route_traceform.py`.** Theorem T over Laurent polynomials, for the same 32 pairs, with each pair's exact locus.
- **F, `followup_index.py`.** At q₀ = 17 ± 12√2 with μ = −1 (3 primes × 2 roots), I(W₁) and I(Φ W₁) for all 16 maps, with B1509's
  banked instrument. The construction of Φ W₁ is new.
- **`decide.py`.** The read-out.

## 4. Predictions, with priors

| | prediction | prior |
|---|---|---|
| P1 | R1 and R2 agree on all 32 decisions | 97% |
| P2 | duality: ρ_q* ≅ ρ_{1/q}, and ρ_q* ≅ ρ_q exactly at q = 1 (B1512 Lemma D). Scored on route 1's action for D.id and route 2's exact locus | 98% |
| P3 | no map leaves the family: each of the sixteen fixes q or sends q ↦ 1/q (no outcome C) | 95% |
| P4 | exactly eight of the sixteen fix every q. Among the eight bare maps, four fix and four pair; among the four bare orientation-reversing maps, two fix every q and two pair q with 1/q | 85% |
| P5 | **outcome A**: every vacuum μ ⊗ ρ_q (q > 0, μ ∈ ℂ*) is fixed by a count-odd map with e = +1. Expected witness: D.θ (θ inverts H₁ and pairs q; duality pairs back). **This is the registered kill, banked NEGATIVE** | 93% |
| P6 | the follow-up: I(W₁) = −1 at all six prime–root pairs (the banked identity), I(Φ W₁) = −1 for the eight bare maps and +1 for the eight dualised ones. So the chiral configurations come in count-flipped pairs over one vacuum, and both are lifted by the potential (R76) | 95% |
| P7 | the lift: w₀ = −1 and A4 + A4 regular (run at design: true; disclosed, not counted) | — |

The priors are informed by B1512 and R47, which were read, so this is a verification, not a blind discovery. The expected number of
true predictions among P1–P6 is 5.6 of 6.

## 5. Registered outcomes

**A (the kill).** Every vacuum is fixed by a count-odd map.
- *What it means.* By L3 no vacuum of the bridge carries a count. By Lemma G each keeps a charge conjugation.
- *What it is not.* A selection by the vacuum, which does not occur on this family.
- *How it is banked.* NEGATIVE, with its scope:
  - frame: F-HE, read in main's class-index terms;
  - object: m004's Ballas family at level one with central twists;
  - reach: one family;
  - hypotheses: H-vac and the uniqueness of the harmonic metric.

**B.** Some vacuum is fixed by no count-odd map. The follow-up is then I at that vacuum.

**C.** Some map leaves the family. The run reports where.

**Reported whatever the outcome:**
- the bare maps' action, including whether a geometric mirror is broken or kept;
- the gap between the handoff's "mirror" and the count-odd maps: a bare mirror keeps the count (L1), so a pair it exchanges carries
  equal counts.

## 6. What a result would and would not mean

**What A would say.** On the one family where the record has a finite-energy vacuum action, the vacuum cannot select chirality. The
chirality-flipping symmetry is unbroken at every vacuum. The chiral configurations are non-split extensions, which are not vacua; they
come in count-flipped pairs over the same vacuum, and the potential lifts both equally.

**What A would not say.**
- That no state, frame, source, end law or component selects. R77's added sources, non-flat backgrounds and other components of the
  character variety are outside it.
- That chirality must be an input everywhere.
- That the handoff's rule is evidence for anything. Its 8 of 8 restates theorems on record, as it says itself.

The price is unchanged, 0 of 19.
