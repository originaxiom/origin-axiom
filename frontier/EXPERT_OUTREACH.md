# Expert outreach — pick, rationale, draft

**Date:** 2026-06-04. Exploratory/uncommitted. For consulting an external specialist on B67 +
the SL(n) tower / candidate `a_d` + PC12, honest about proof status.

## The pick: **Tudor Dimofte** (primary)

- **Email (public, University of Edinburgh):** `tudor.dimofte@ed.ac.uk`
  (Higgs Centre for Theoretical Physics / School of Mathematics; homepage `dimoftelab.com`).
  *Verify the address on his Higgs/School page before sending.*
- **Why him:** he is the cleanest match for your exact criterion — works on **both** character
  varieties **and** Chern–Simons / the **3d-3d correspondence** (which literally maps the character
  variety of a 3-manifold to a 3d gauge theory), complex CS, and Neumann–Zagier / A-polynomial data.
  That is precisely the neighbourhood of B67 (figure-eight A-polynomial from a trace-map
  fixed-point set) and Path 3 (A-polynomials of the metallic mapping tori). He is mid-career and
  active — likely to engage a well-posed, honest, *bounded* question.

### Strong alternative: **Stavros Garoufalidis** (SUSTech, Shenzhen; `stavros@mpim-bonn.mpg.de` /
SUSTech address — verify)
- Better fit if the focus is the **A-polynomial / AJ-conjecture** specifics (B67/B68) and quantum
  topology of character varieties, rather than the 3d-3d physics bridge. He literally works on
  A-polynomials, the AJ conjecture, and character varieties of knots/3-manifolds.

**Recommendation:** Dimofte first (matches "character varieties AND 3d-3d" exactly); Garoufalidis
if you want the A-polynomial/quantum-invariant read specifically.

---

## Draft email (one page; send under your own name)

**Subject:** A trace-map route to the figure-eight A-polynomial, and an SL(n) character-variety
multiplicity conjecture — a novelty/connection question

Dear Professor Dimofte,

I run a small, governed mathematics project on rank-two SL(n,ℂ) character varieties of F₂ and the
"metallic" substitution trace maps `φ_m(a)=aᵐb, φ_m(b)=a` acting on them. I'm writing for a bounded
expert read on whether two results are **new or already known** in the character-variety /
Chern–Simons literature you work in — I'd rather be told "that's in [reference]" than rediscover it.

**1. A concrete, checkable result (verified, exact).** Taking the figure-eight complement as the
once-punctured-torus bundle with monodromy `M²` (`M=[[1,1],[1,0]]`), the fixed-point set of the
induced SL(2,ℂ) trace map is `y=z=x/(x−1)`; eliminating the fiber coordinate reproduces the
Cooper–Long A-polynomial `M⁴L²+(−M⁸+M⁶+2M⁴+M²−1)L+M⁴` **exactly** (literal equality). I don't know
whether deriving the A-polynomial this way — as the trace-map fixed locus, via the
meridian/longitude trace identity `κ=tr(t)⁴−5tr(t)²+2` — is a known route or not; that's part of my
question.

**2. A structural conjecture (verified-match, NOT proven).** The fixed-line Jacobian of the SL(n)
trace map at the trivial representation factors over the "Dickson" pieces `char(±Mᵏ)`. We have a
candidate closed form for the multiplicities from the opposition involution `θ=−w₀` on the `A_{n−1}`
root system: `mult(char(Mʰ)) = ⌈(n−h)/2⌉`, `mult(char(−Mʰ)) = ⌊(n−h)/2⌋` for heights `h=2..n−1`,
plus an explicit "wrap" piece at height 1. It reproduces the full n=3,4,5 towers exactly. **It is a
conjecture**: the missing step is identifying the root-system split with the trace-map Jacobian —
which I believe needs the ambient SL(n,ℂ) trace ring, and which I have not proven.

**My questions, briefly:** (i) Is either result already in the literature (Cantat–Loray dynamics on
character varieties, Goldman's `Out(F₂)` action, your 3d-3d / NZ-data work)? (ii) Is the trace-map
route to A-polynomials of the metallic mapping tori (`φ_m`, m=1,2,3) something the 3d-3d
correspondence would already characterize — i.e., is computing their Neumann–Zagier data worthwhile,
or known? I make **no physical claims** — this is character-variety mathematics, and I'm seeking a
novelty/placement read, not validation.

I can send a 2-page note (the figure-eight derivation + the conjecture, both with their proof
status flagged) if useful. Any pointer — even a one-line "known, see X" — would be valuable, and I
appreciate your time.

With thanks,
Dritëro
[affiliation / link, optional]

---

## Notes for you before sending
- **Lead with B67** (concrete, exact, checkable) — it's the credible hook; the conjecture is
  secondary and clearly flagged as unproven.
- Keep the **honest proof-status line** ("It is a conjecture … I have not proven"). It's what makes
  a specialist take it seriously rather than bin it.
- Attach the **2-page note**, not the repo. The note should be: page 1 = B67 derivation (exact);
  page 2 = the candidate `a_d` with its three gaps (unproven identification, height-1/wrap motivated,
  `a₃(n=6)` open). Do **not** send the physics-thesis framing — it would undercut the math.
- If no reply in ~3 weeks, Garoufalidis is the clean second ask (reframe toward A-polynomial/AJ).

---

# 2026-07 — The gate-based outreach package (Gates B / C / D)

**Context.** Since the section above was drafted (2026-06-04, pre-gates), the frontier has been
mapped to four named gates (`docs/OPEN_PROBLEMS.md`). Gate A is in-sandbox (B330/B347/B348/B349);
Gates B–D need specialists. Each brief below is **self-contained, bounded, and honest about proof
status** — the same discipline as the B67 draft above. All addresses must be **verified before
sending**; send under your own name; attach the specific gate section of `OPEN_PROBLEMS.md` (or a
2-page extract), never the whole repo, never the physics-thesis framing.

## Gate B — the CRUX `T[4₁;E₆]` (3d-3d at exceptional gauge type)

- **Who:** a 3d-3d correspondence / complex Chern–Simons specialist. **Tudor Dimofte** (above)
  remains the primary fit — this is literally the DGG `T[M]` construction. Alternatives: a member
  of the Gang–Yamazaki or Terashima–Yamazaki lineage (state integrals), or **Sergei Gukov's**
  group (3d-3d origin; verify current contacts).
- **The bounded question:** "The DGG state-integral construction of `T[M;G]` is explicit for
  `G = SU(N)`/classical groups. Is there any construction — even conjectural — of `T[4₁; E₆]`?
  Concretely: does the figure-eight's `E₆` character variety (which exists; we computed the
  relevant components) admit a Neumann–Zagier-type datum an exceptional-group state integral
  could quantize? If yes, the *arithmetic* sub-question is whether the `2T ↪ E₆` embedding
  factors through a self-dual (quaternionic) or a complex `SU(2)` — that single fork decides a
  degeneracy question we can state precisely."
- **What we supply:** the `E₆` character-variety computations (B264/B274/B275), the cascade
  structure (B305/B306), the sharpened `27|₂T` branching atom (B326/B327/B329), the refuted
  routes (B310, B325 — so they are not re-walked).
- **What we do NOT claim:** any physics realization; the gate note itself says even a realized
  `T[4₁;E₆]` does not by itself extract values.

## Gate C — multiplicity → the generation count (commensurator / orbifold arithmetic)

- **Who:** an arithmetic-hyperbolic-geometry specialist (commensurators, orbifolds, trace
  fields): the **Maclachlan–Reid** school (e.g. **Alan Reid**, Rice; verify) or a
  SnapPy/Sage-fluent computational topologist (**Nathan Dunfield**, UIUC; verify — also a fit
  for the cover/enumeration side, cf. B349).
- **The bounded question:** "The figure-eight group's commensurator contains an intrinsic `ℤ/3`
  (the order-3 Eisenstein units in `PGL(2,𝒪₋₃)`). Under the 3d-3d dictionary, matter multiplets
  live on character-variety components. Does the `ℤ/3` commensurator action produce **three
  symmetric copies** of a given component's matter content (a genuine family replication), or
  does it only permute the trinification factors (the 'wrong' 3)? A definite answer either way
  closes or opens our gate — both outcomes are valuable to us."
- **What we supply:** B302 (the `ℤ/3` located, intrinsic), B307 (single-knot `C₃` trace-field
  obstruction — why replication must come from relation, not a bigger object), B321, B323 (the
  four-level framework), B349 (the cover census through index 6, where the commensurator
  identifications are visible as isometries).
- **Honest flag:** this gate has a stated *refutation* condition; we want the true answer, not a
  favorable one.

## Gate D — a non-Hermitian Damanik–Gorodetski theorem (spectral theory)

- **Who:** the theorem's own school: **David Damanik** (Rice) or **Anton Gorodetski** (UC
  Irvine); alternatively a non-self-adjoint-operators specialist (e.g. the Sjöstrand/Davies
  lineage; verify all addresses).
- **The bounded question:** "The Fibonacci Hamiltonian's trace map at real coupling gives Cantor
  spectrum / dimension theory (your theorems). Our object forces the *same* trace map but at the
  complex parameter `κ = √3·e^{±iπ/6}` — a non-self-adjoint transfer-operator cocycle. Is there
  any DG-type structure theorem (spectrum as a dynamically-defined set, dimension bounds) in the
  non-Hermitian regime, or is it known to be genuinely open? We have in-sandbox numerics of the
  complex-κ dynamics and can share the invariant-surface structure (the Sütő invariant is
  conserved for all `m`)."
- **What we supply:** K007/K010 (the Hermitian baseline, cited), B107 (the KKT identification),
  B317 (the object as a transcendental Painlevé-VI solution — relevant because it rules out
  algebraic shortcuts), L19/L20 (the parked leads).
- **Honest flag:** we do not claim the non-Hermitian spectrum *means* anything physical; the
  question is purely spectral-theoretic.

## Sequencing and hygiene
1. **One gate, one expert, one bounded question per email.** No cross-gate storytelling.
2. Lead with the concrete computed object (the `E₆` components / the `ℤ/3` commensurator / the
   complex-κ trace map), never with the program.
3. Keep the proof-status line in every draft; offer the 2-page extract, not the repo.
4. Log every send + reply in `PROGRESS_LOG.md`; a "known, see X" reply closes a gate honestly
   and is a *good* outcome (C-guardrail: we want the state of the evidence, not encouragement).
5. If a reply opens a collaboration, the firewall wording travels with the material: the object
   forces form, not values; no physics claims.
