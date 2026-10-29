# chat1 → cc (main), 2026-10-29: THE CONE AND THE SIGN — the record already holds the object's Lorentzian structure (B428: holonomy = Spin(3,1), H³ the mass hyperboloid, signature (3,1) geometric, not banked because every hyperbolic 3-manifold has it; B1115: signature as reading, not structure; B101 and B97: the (2,1) form in 2+1; B1708 and P-276: the Einstein vacua over every thread); this relay re-checks it exactly on the object (seven cells hold) and finds one sentence out of line with the rest, B716's "time, 4-dimensionality and Lorentzian signature are all the observer's"; the holonomy fixes the 3+1 signature and the slice but not the vacuum (Λ = 0, > 0, < 0), the nappe or the unit; P-282 is answered in 2+1 by B101's form, the discriminant; physical spacetime stays UNEARNED, and B428's control leg is why — 0 of 19

chat1 (the web seat), on the owner's word ("yes please. deriving physical spacetime would be progress"). That word
followed this seat's answer to his question: is physical spacetime already in the repository, unnamed by the rules?
Data-free. 0 of 19.

**Refereed read-only before the push: PASS WITH CORRECTIONS.**
- **Four blocking findings, all applied below:**
  - **The Seen-first line was false in substance.** B428, B1115, B1465 and B101 already hold S1, S2, S4, S5 and S7.
  - **B1750 (the arrow forced, as the walk's escape) was omitted.**
  - **The letters were transposed** against GENESIS's core convention.
  - **"Only the arrow and the unit are free" left out Λ.** The same holonomy carries de Sitter and anti-de Sitter
    vacua (THE_LADDER X4, P-276).
- **Sixteen non-blocking items,** applied below.
- **No rerun.** The referee re-ran the script, got byte-identical output, and reproduced both sweeps.

**A correction to this seat's own answer, first.**
- This seat told the owner tonight that the record "half-holds and half-denies" a canonical spacetime: B1708 builds the
  cone, and B716 denies the signature.
- That was incomplete. On 2026-07-05, B428 had already credited the holonomy as Spin(3,1), H³ as the mass hyperboloid
  and the (3,1) signature as geometric. It then declined to bank a spacetime claim for a stated reason, the control
  leg: "every hyperbolic 3-manifold has them … do not bank a spacetime claim on the current record."
- B1115 put the same point as signature-as-reading against signature-as-structure.
- So what the record holds is not a denial. It is a deliberate refusal, and the reason is right.
- What is out of line is one sentence of B716. This seat's sweep listed B428, B1115 and B101 among its hits, but they
  were not read before the rule was sealed.

**What this relay is not.** It does not derive physical spacetime. What it does:
- it re-checks exactly what the record holds;
- it aligns one sentence;
- it says what a derivation would still need.

**Seen first** (main at 2a4635a15; full text; each cut before its list of other lanes):
- `VERDICT topic-sweep /spacetime|space-time|Lorentzian|Milne|physical time|arrow of time|FLRW|Friedmann|cosmolog|Einstein equation|Ricci.flat|3\+1|four.dimensional spacetime|emergent (space|time)/ (full text): 136 of 1561 arcs on main match (NEGATIVE 37, OPEN 12, PROVED 87); 12 register rows match (DONE 4, QUEUED 8)`
- `VERDICT topic-sweep /discriminant.{0,40}(signature|Lorentz|Minkowski|time)|binary quadratic form|hyperboloid|Hermitian matri|SO\(3, ?1\)|SO\(2, ?1\)|Lorentz group|velocity hyperboloid|light.?cone|spacetime sign/ (full text): 25 of 1561 arcs on main match (NEGATIVE 3, OPEN 1, PROVED 21); 1 register rows match (QUEUED 1)`
- **What the record already holds, read for this relay:**
  - **B428** (§ "The spacetime chain"): steps 1–4 credited as true group theory, failing the control leg; "do not bank
    a spacetime claim".
  - **B1115** (D2): the geometric holonomy FORCED, 0 bits (Mostow). Signature-as-reading (PSL(2,ℂ) = SO⁺(3,1)) is
    available; signature-as-structure is not, since the centraliser is trivial.
  - **B1465 and GENESIS § 1 ([v1.15]):** ρ ⊗ ρ̄, "the Lorentz vector bundle" (the four of SO(3,1)), which is the
    action on Hermitian matrices.
  - **B101 (R1):** the Ad-invariant form on Sym² of the Fuchsian representation is unique, of signature (2,1), "the
    rigorous backbone of B97's (2,1) finding".
  - **B101 (R2):** Lorentzian occurs at k = 2 only, and does not climb the ranks.
  - **B1708:** the cone is Ricci-flat iff the curvature is −1; it names the Milne universe.
  - **THE_LADDER X4 and X5 (P-276):** "every thread is the space of an exact 4d vacuum (the Milne cone; with scale
    factors t, sinh t, sin t also de Sitter and AdS in open slicings)"; no dynamics and no initial condition.
  - **B1750, with B1083 and B1662:** the arrow of time is forced, as the walk's escape. The closer of B717 is retired as
    an explanatory move.
  - **B716** (probes 1–3), **B96 and B97**, **B981, B1104, B1114, B1134 and B1165**.
  - **The rows:** P-282, P-289, P-330, P-439, P-443.
- **What no arc or row does** (the referee's sweeps agree): set B716's sentence against B428, B1115 and B1708.

## How it was done

- **The rule** `THE_CONE_RULE.md` was sealed at aabd77104, with seven cells and their priors. The script was committed
  118 s later.
- **The script** `cone_checks.py` was committed at b3b496c2a, before its run. Its helpers were checked only on synthetic
  inputs. One helper was fixed in the self-test to allow a symbolic Λ₀₀, and that fix is in the commit.
- **One run:** exit 0. Its stdout went to /dev/null, since everything is also written to the output file. The output
  was committed unread at 764eee7d7, then read.
- **Its stderr** holds only SnapPy's link editor (plink) warning that its GUI is unavailable. Its library path was
  replaced by `<python>` at 372138566, the only change.
- **Every cell holds as sealed, with one caveat:** S2 was sealed as −dt² + t²(…) and checked as dt² − t²(…), the same
  metric up to a global sign convention.

**The letters.** This seat's script uses the transposed names: its L = [[1,0],[1,1]] and R = [[1,1],[0,1]] are
GENESIS's core R and L, so the output's "LR = [[1,1],[1,2]]" is the core's RL. Restated in the core convention
(L = [[1,1],[0,1]], R = [[1,0],[1,1]], LR = [[2,1],[1,1]]), by hand after the run, under substitution:
- L's invariant form is y²;
- LR's invariant form is −(x² − xy − y²).

The discriminants, 0 and 5, are unchanged. The LR/RL distinction is load-bearing on the record (B979), so § 2 uses the
core letters.

## 1. The cone, re-checked (cells S1–S3)

- **The holonomy acts on Hermitian matrices as SO⁺(3,1)** (S1a, S1b).
  - Riley's matrices x = [[1, 1], [0, 1]] and y = [[1, 0], [−ω, 1]] satisfy w x = y w, with w = x⁻¹ y x y⁻¹, exactly.
  - That they give m004's holonomy (discrete, faithful) is Riley's theorem. The referee confirmed it independently:
    - the relator's entries are proportional to z² − z + 1 for y = [[1, 0], [z, 1]], so z = −ω or −ω̄;
    - SnapPy's meridian pair satisfies the relation with tr(xy) = 5/2 − (√3/2)i.
  - Each generator acts by X ↦ A X A† as a real 4×4 Λ with Λᵀ η Λ = η, det Λ = 1 and Λ₀₀ = 3/2, exactly. SnapPy's
    generators of m004 do the same, with residuals of 10⁻¹⁵ to 10⁻¹⁴. This is B428's step 1, and GENESIS's ρ ⊗ ρ̄.
  - On this 4-dimensional representation the invariant form is unique up to scale (checked at review), and it is
    det X, of signature (1, 3).
  - The representation itself is a choice. The adjoint carries a different form: S6 below.
- **The slices** (S2).
  - H³ is the hyperboloid det X = 1, tr X > 0: B428's mass hyperboloid.
  - In X = t (cosh r, sinh r n̂), the pull-back of η is exactly dt² − t²(dr² + sinh²r dΩ²), with t² = det X.
  - The holonomy Γ is discrete and torsion-free, acts freely and properly on H³, and keeps t. So the open future cone
    {det X > 0, tr X > 0} divided by Γ is ℝ₊ × m004, B1708's flat cone. Γ does not act properly on the null cone.
- **The nappe** (S3).
  - X ↦ −X commutes with Γ and exchanges the two halves of the light cone. As a choice of half, the arrow is a
    convention in B1750's sense.
  - Once a half is taken, the spacetime does tell expanding from contracting: the vertex is at finite proper time in one
    direction only.
  - Every isometry of H³ lies in O⁺(3,1) and keeps each half. Complex conjugation of entries is one example: it acts as
    diag(1, 1, −1, 1), det −1, Λ₀₀ = 1, and sends Γ to Γ̄ (Λ(Ā) = C Λ(A) C). Mostow fixes Γ up to conjugation and
    orientation; for amphichiral m004, Γ̄ is conjugate to Γ, and the amphichiral symmetry lifts to g ∘ C with g
    normalising Γ.
  - So the object's amphichirality acts in the cone as a reflection of space, not as a reversal of time.
  - This relay does not relate the nappe to the walk's forced escape (B1750, B1083, B1662).

**What the holonomy fixes and what it leaves free.**

| item | status | scope |
|---|---|---|
| the dimension 3+1 and the signature (1, 3), on ρ ⊗ ρ̄ | carried by the holonomy, as group theory (B428 steps 1–4; B1115's signature-as-reading) | CONDITIONAL on GM3, GM4, SE1 and SE2 (the root m004), with Mostow; the mathematics generic |
| the slice: each spatial section a copy of m004 | the same | the same |
| the vacuum: Λ = 0 (the cone, scale factor t), Λ > 0 (de Sitter, sinh t) or Λ < 0 (anti-de Sitter, sin t) | free: the same holonomy acts on all three (THE_LADDER X4, P-276; B1708) | the sign of a 4d Λ is not fixed by H³'s curvature; compare B981's withdrawal |
| the unit (at Λ = 0, X ↦ λX rescales t; at Λ ≠ 0, Λ sets it) | free | — |
| the nappe | a convention (X ↦ −X) | the walk's arrow (B1750) is a separate, forced item |
| "this is physical spacetime" | UNEARNED identification | B428's control leg: every hyperbolic 3-manifold carries the same |

**Three different "times" on the record,** which this relay separates without relating them:
1. **The suspension circle of the fibration.** This is B716's internal Anosov time; it has no preferred direction and
   no beginning. In the cone it lies inside each slice, as a direction of space.
2. **The cone's proper time t.** It begins at the vertex, and it is canonical up to the nappe and the unit, once
   Λ = 0 is taken.
3. **The histories' clock** (P-439, and the briefing at 2a4635a15): moves or geodesic length along threads on the
   modular surface.

## 2. The sign (cells S4–S6), in the core letters

- **In 2+1, the moves keep the discriminant** (S4).
  - L and R act on binary quadratic forms ax² + bxy + cy² by substitution and keep b² − 4ac, of signature (2, 1).
  - The upper half plane of τ is the sheet {discriminant = −1, a > 0}: positive-definite forms up to positive scale. The
    modular surface is its quotient.
  - L's invariant form, y², has discriminant 0. It is null: the cusp.
  - LR's invariant form, −(x² − xy − y²), has discriminant 5. It is spacelike: the genesis word's axis, with field
    ℚ(√5).
  - **Conventions:** the (1, 3) form of § 1 has timelike positive. The discriminant has timelike negative
    (disc = −4 det S).
- **This is B97's form, and B101's** (S5).
  - X ↦ XJ, with J = [[0, 1], [−1, 0]], carries sl(2,ℝ) to symmetric matrices, and Killing(X, X) = 2 · disc.
  - It intertwines Ad with S ↦ M S Mᵀ, which is substitution by Mᵀ. So S4's action of a word is S5's Ad-action of its
    transpose, with the letters reversed. The form is the same.
  - B101 proved the Ad-invariant form on Sym² unique, of signature (2, 1).
- **In 3+1, the form is in the four, not the adjoint** (S6).
  - sl(2,ℂ) as a real Lie algebra has a Killing form of signature (3, 3).
  - B96 computed the volume Hessian, and B97 the Killing forms of sl(2,ℝ) and su(2). The (1, 3) form is in neither.
  - B428 had already placed it on the geometric side ("signature (3,1) geometric").

## 3. It is generic (cell S7)

m003's holonomy (SnapPy) also lands in SO⁺(3,1). This is B428's control leg, and the reason the record banks no
spacetime claim. Nothing here singles out m004, and nothing bears on the 19.

## 4. Proposals (they assign nothing)

1. **B716, a dated correction block (main's to write).** Align its sentence "time, 4-dimensionality and Lorentzian
   signature are all the observer's" with B428, B1115 and B1750:
   - the holonomy carries the 3+1 Lorentzian structure as group theory, with Einstein vacua over the object for every
     sign of Λ (B428, B1115, B1708, P-276);
   - it does so generically, so no spacetime claim is banked (B428's control leg);
   - there is no canonical 4d filling and no canonical Wick rotation, as probed;
   - the arrow is B1750's: forced, as the walk's escape;
   - the suspension circle has no direction and no beginning, while the cone's time begins at its vertex. This bears
     on the "no beginning" readings that cite B716: B1196 and COSMOLOGY_LEDGER.
2. **B97's "not on the geometric side" and B96's "closing the Lorentzian-emergence reading":** each should name the
   form it computed (Killing forms; the volume Hessian). B428 credits (3,1) on the geometric side.
3. **P-282: close it with B101 and B97 in 2+1, and with B428 and GENESIS's ρ ⊗ ρ̄ in 3+1,** if that is what it asks.
   - In 2+1, the moves keep a unique invariant form of signature (2,1): the discriminant.
   - In 3+1, the holonomy keeps det on ρ ⊗ ρ̄.
   - If P-282 asks for the sign of a kinetic term in a field theory on the object, it stays open.
4. **Wording.**
   - P-289 ("the read-out on a physical spacetime"), P-330 ("the first count read on a physical 4d spacetime") and THE
     COMPLETION MAP's C10 call the cone physical. Under B428's disposition they would read "a 4d vacuum over the
     object (its identification unearned)".
   - A GENESIS row could record the vacua as CONDITIONAL (on GM3, GM4, SE1 and SE2; the mathematics generic), beside
     the unchanged "Some arrow of X_gen is physical time: NOT DERIVED".
5. **What deriving physical spacetime would still need.** These are directions in this seat's suggested order, not
   claims that any would succeed.
   1. **Specificity, the control leg.** Something must tell m004's vacua from m003's. The record's candidates are:
      - B428's registered next interface target: how ρ into E₆ and ρ_geo into SL(2,ℂ), both from the same π₁(4₁),
        relate on the E₆ character variety;
      - P-289 and P-330: the Dirac index twisted by ρ_T on the cone, which uses the object's own representation.
   2. **The vacuum and matter.** Λ's sign and value, and a matter content. Any k = −1 FLRW universe can take m004 as
      its slices, even globally as a quotient. Given the identification, the object would fix the type and topology of
      space, not the expansion history.
   3. **The clock.** The histories are geodesics on the modular surface, so they live in the 2+1 picture: the
      hyperboloid of forms, whose quotient is that surface. They do not live in the 3+1 cone over m004. Relating the
      two pictures, and either of them to P-439's clock, is itself a question.
   4. **The nappe against the walk's arrow.** Is B1750's forced escape the cone's expanding half? That is unrelated
      here.

## What could not be done here, said plainly

- **Riley's theorem** (that his representation is m004's discrete, faithful holonomy) is cited, not re-proved. The
  referee's independent check is above.
- **Not examined:** whether a cusped hyperbolic space as our universe's slice meets observational constraints, and how
  the three times relate.
- **The literature:** the Milne universe and the hyperboloid model are named, not re-read. R. Riley, "A quadratic
  parabolic group", Math. Proc. Cambridge Philos. Soc. 77(2) (1975) 281–288, was confirmed at review.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE CONE AND THE SIGN: rule aabd77104; script b3b496c2a; output 764eee7d7 (all seven cells hold); stderr path scrubbed 372138566; refereed read-only | "this relay re-checks it exactly on the object (seven cells hold) and finds one sentence out of line with the rest, B716's "time, 4-dimensionality and Lorentzian signature are all the observer's"" | `relays/CHAT1_TO_CC_2026-10-29_THE_CONE_AND_THE_SIGN.md` @ the commit adding it; files in `relays/chat1_2026-10-29_the_cone/` @ 372138566 | — | B716, B428, B1115, B1708, B1750 | 2026-10-29 |
| — | web seat (chat1) | the same relay, §§ 2 and 4.3 | "P-282 is answered in 2+1 by B101's form, the discriminant" | the same | — | P-282, B97, B101 | 2026-10-29 |

0 of 19.
