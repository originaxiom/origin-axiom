# Origin Axiom — Unified State of Knowledge

> 📌 **Historical snapshot — kept per GOVERNANCE §9; not the current state.** The living state: `CLAIMS.md` (the ledger) · `docs/OPEN_LEADS.md` + `docs/OPEN_PROBLEMS.md` (the frontier) · `CHANGELOG.md` (recent history) · `docs/INDEX.md` (the document map).

> ⚠️ **OUTDATED & MIXED-SOURCE (2026-06-15).** This briefing combines **two separate branches** and is now stale:
> - **Branch A (this repo)** — the trace-map / character-variety work, then banked through ~B155; the frontier is now
>   at **B325**.
> - **Branch B (Ω)** — an *external* history-enumeration handoff bundle (`origin_axiom_handoff_2026-06-15`, ledger
>   B868–B907). **The Ω branch is NOT in this repo's main line and its results are not verified here.**
>
> A fresh reader should **not** treat the Ω `B`-numbers as part of this repo's frontier. For the current state of
> *this repo*, read `../README.md` ("Current state — read next"), `../knowledge/K020`, `OPEN_PROBLEMS.md`, and
> `../CHANGELOG.md`. This file is kept for the cross-method convergence record only.

**A single source of truth across both branches, for briefing a fresh working session.**
Compiled (AI-assisted, cross-session) from: the trace-map / character-variety work (**Branch A**, banked in this
repo), and the **Ω** history-enumeration handoff bundle dated **2026-06-15** (`origin_axiom_handoff_2026-06-15`,
latest ledger batch B868–B907). Where the Ω side may have advanced past that date, items are marked
**[confirm-with-Ω-handoff]**.

Every claim carries a status label:
**[exact]** symbolic/exact-arithmetic proof · **[F_p]** exact in a finite field · **[num]** high-precision numeric ·
**[proved]** theorem-grade in-branch · **[open]** genuine research gap · **[killed]** falsified, stays dead ·
**[firewalled]** deliberately *not* claimed.

> **Provenance & verification status (verify-don't-trust).** Branch A is banked and tested in *this* repo (B1–B155,
> ledger V1–V148). Branch B (Ω) is a **separate handoff program**, *not* in this repo's main line; its B-numbering
> (B206…B907) is the Ω branch's own and does **not** collide with our B1–B155 (different objects). Of the Ω side,
> only the **core theorem** has been independently re-derived in-sandbox here (the Ω₄/TC-1 charpoly + signature, the
> shear actions, `det R=1`, `RᵀGR=G`, `det G`, the wall/(2,2) flip — no transcription errors). The exact L4–L10
> counts, the history-entropy `log 2` proof, the Fibonacci block-count audit (B588–B607), and TC-2 *as stated* are
> **handoff-claimed, not yet re-verified here** — treated as [confirm-with-Ω-handoff] until re-run under governance.
> Cross-branch convergence is **corroboration, not validation** (§3, §4).

> **B-number bridge.** Branch A's **B206** (the golden×phase object) is banked in *this* repo as
> **`frontier/B155_golden_phase_bridge/`** (ledger V148); "B206" below refers to that object. The Ω branch reached the
> same characteristic polynomial from its own enumeration as **Ω₄ / TC-1** (§3).

---

## 0. The one object and its premises

Strip both branches to the core and there is one object: the once-punctured torus $\Sigma_{1,1}$, its character
variety, and the action of the **metallic / golden substitution** $a\mapsto a^m b,\ b\mapsto a$. The founding
statement — *"reality is the residue of the impossibility of nothingness"* — is, formally, an **existence principle**:
it forces a self-referential fixed point $x=m+1/x$ (the metallic mean) and from there a self-similar structure. An
existence principle yields a **structure**, not a **dynamics** — this is the root of the firewall (§4). The chain from
the seed is forced, **but the seed rests on chosen premises** (≈5, counting the $b\to a$ closure), so this is
*discovered mathematics on a constructed premise*, **not** emergence from nothing. **[firewalled framing]**

---

## 1. Branch A — trace-map / character variety (this repo)

### Positive results
- **$\kappa = 2+\lambda^2$ — the figure-eight trace map *is* the Fibonacci–Hamiltonian trace map.** The Dehn-twist
  maps $t_a:(x,y,z)\mapsto(x,z,xz-y)$, $t_b:(x,y,z)\mapsto(z,y,yz-x)$ and their composite preserve the Fricke–Vogt
  invariant $\kappa=x^2+y^2+z^2-xyz-2$; rescaling gives $\kappa=4I_{\rm Fib}+2=2+\lambda^2$. $\kappa=2\Leftrightarrow$
  periodic/ac spectrum; $\kappa>2\Leftrightarrow$ zero-measure Cantor (quasicrystal). **The most robust result in the
  program. [exact]**
- **$L=-M^4$ on a distinguished $\mathrm{SL}(4)$ slice.** With meridian $\mu=A^{-1}t$, longitude $L=[A,B]$, and
  $A=\operatorname{diag}(1,1,\omega,\omega^2)$: the ring identity $[A,B](\det t)^2=-(\det t)\mu^4$ holds for all four
  family parameters; on $\det t=1$, $L=-M^4$. **[exact]** Its character is **peripheral**: $\mu^4[A,B]^{-1}=-I$ is
  central, so this is a **Dehn-filling-type slope** — the $\mathrm{SL}(4)$ analogue of Falbel's $\mathrm{SL}(3)$
  $M^3=L$ for the figure-eight — computable in principle by Zickert's Ptolemy machinery (done for $m004$ only at
  $n=2$). **Corrected (2026-06-16):** this family is a **codimension-1 slice** (the spectrum-pinned / $e_2=0$ locus) of
  a **3-dimensional** component, **not** the component. Verified three ways — a referee's mod-$p$ Jacobian (kernel 19),
  an exact $\mathbb{Q}(\omega)$ recomputation (rank 29, kernel 19; gauge 15 + $t$-scaling 1 + 4 family params span only
  18), and a direct off-slice deformation. The earlier "$\dim H^1=3 \Rightarrow$ component" was a non-sequitur
  ($H^1=3$ is the *component's* dimension; the family does not span it). **There is no "better theorem":** off the
  slice $L=-M^4$ fails in every form (no $P(M,L)=0$, no $P(M,L,e_2)=0$, no char-poly match). **[exact / num]**
  (Repo: `frontier/B89`, `frontier/B149`; degeneration thesis `frontier/B153`.)
- **B206 — the golden×phase bridge** (= `frontier/B155`, V148). $M_g$ with
  $\operatorname{charpoly}=(x^2-3x+1)(x^2-x+1)$ = figure-eight monodromy × primitive-6th cyclotomic, block-decomposing
  as $[[2,1],[1,1]]\oplus[[0,1],[-1,1]]$ (golden ⊕ order-6), glue $(\mathbb{Z}/2)^2$ (representative-specific: the
  block-diagonal form with the same $\chi$ has trivial glue); a primitive integral invariant form has
  $\det=-15=\operatorname{disc}\mathbb{Q}(\sqrt5)\cdot\operatorname{disc}\mathbb{Q}(\sqrt{-3})$ and **signature
  $(1,3)$**. $M_g$ is **nonderogatory** (min poly = char poly), so its $\mathbb{Q}$-conjugacy class is determined by
  $\chi$. **The keystone shared with Ω — see §3. [exact]**
- **Dimension-2 rigidity = Painlevé VI.** The character-variety dynamics at the relevant level is isomonodromy.
  **[exact, cited]**
- **degree = rank tower** for $n\le4$; the **metallic meridian** $\mu=A^{-m}t$ is the correct order-determined object
  (B154). **[exact for $n\le4$]**

### Negatives / kills (stay killed)
$\phi^\phi$ as axiom **[killed]**; $\phi$ via Hurwitz is the proven anchor; the cosmological-constant formula
**[killed by null test]**; the spacetime tower **[dead, B101/B96]**; the physics chapter **[closed, B107]**; the
two-tower multiplicity model died at SL(6) (mult$|k|{=}3$ = 2, not 3) **[killed]**; the cohomological capstone is
**foreclosed**; the holographic $\{p,q\}\leftrightarrow$ metallic correspondence is **non-selecting** ($\phi^2$ is a
promiscuous small algebraic integer — coincidence, not mechanism). Newly fallen (2026-06): the SL(4) **"component"**,
**"family for all $n$"**, and the **"$n=5$ impossibility"** (refuted by a Jordan-block counterexample: spectrum
$\{1,1,1,-1,-1\}$ has $\operatorname{tr}A=\operatorname{tr}A^{-1}=1$, $\det A=1$, yet $A^2\neq I$). **[killed]**

### Open
**Uniform-$n$** — $L=-M^4$ is proven (on the slice) only for $n\le4$; the closed form $k=4-m(o-3)$ / the metallic
A-polynomial exponent is the deep prize. The full 3-dim component's defining equations are open. **[open]**

---

## 2. Branch B — Ω enumeration / rewriting (cross-session handoff)

> Branch B is *not* in this repo's main line; the items below are the handoff's claims, with the verification status
> from the banner above. Only the core theorem (§2 "TC-1 / Ω₄") has been independently re-derived here.

### The approach (what Ω *is*)
Ω is an **exact, governed, level-by-level enumeration** of *positive unit-shear histories* — words over a small
generator set — pushed to ever-deeper length levels (L4 → L11, with exact counter-states banked at each). The pipeline
is a **reduction**:
```
history word → matrix → characteristic polynomial / spectral class
            → reciprocal / metric-compatible class
            → nondegenerate invariant-form sector → transition / automaton / rewriting data
```
The driving question is **growth / entropy**: how the count of admissible classes grows, what
automaton/semigroup/rewriting system generates it, and whether positive entropy can be *forced*. (Latest arc
B818–B877: a "uv" symbolic action / semigroup-growth / rewriting-system route and a route-decision; B878–B907:
literature-novelty audit, expert packet, paper skeleton. **[confirm-with-Ω-handoff]**)

### Positive results
- **TC-1 / Ω₄ — the unique minimal full metric seed.** At $n=4, L=4$ there is exactly **one** nondegenerate
  metric-compatible class, with charpoly $x^4-4x^3+5x^2-4x+1=(x^2-3x+1)(x^2-x+1)$ ("golden × phase") and **signature
  $(1,3)/(3,1)$**. **[exact; core theorem independently re-derived here]** — *This is B206 reached from the other
  side; see §3.*
- **TC-2** — a full (nondegenerate symmetric invariant) metric ⟹ **reciprocal/palindromic** characteristic
  polynomial. **[proved in-branch; clean statement not yet re-verified here]**
- **TC-4** — odd label-relabeling **cancels** the Pfaffian orientation (an orientation/asymmetry obstruction).
  **[proved in-branch]**
- **Constructive strict-full branching theorem (B588–B607, audit passed in-branch).** The admissible block counts are
  the **Fibonacci numbers** $1,1,2,3,5,8,13,21,\dots$ (matched through $n{=}12$); reciprocal quartic family
  $x^4-ax^3+(2a-2m-4)x^2-ax+1$, $\det R=1$, invariance identities verified. **[exact in-branch, audit
  PASSED_NO_BREAK_FOUND; not yet re-run here]**
- **Metric tiers.** The meaningful filter is *not* "∃ nonzero invariant form" but "∃ **nondegenerate** symmetric form
  with **Lorentzian or split** signature." Full candidates are reciprocal/nondegenerate; nonreciprocal $\dim G=1$
  classes are degenerate rank-1 artifacts. **[exact in-branch, sampled]**
- **History entropy $=\log 2$** is an allowed (banked in-branch) claim; the block-count growth itself is golden
  ($\sim\varphi^n$). **[proved in-branch for history entropy; not yet re-verified here]**

### Negatives / firewall (Ω "hard claim rules")
**Forbidden / not derived:** a physical spacetime metric; physical entropy; gravity / QM / cosmology; dark matter /
baryogenesis / CP violation; expert novelty without external review. The "Ω4 = 3+1" reading is kept explicitly as
**proxy pressure, not a dimension derivation**; the $(1,3)$ signature is **algebraic inertia, not a Lorentzian
spacetime**. **[firewalled]**

### Open
**Endpoint entropy** (vs. the settled history entropy) **[open]**; whether the forced boundary/action rule that would
make the asymmetry *non-arbitrary* can be derived internally **[open]**; external-specialist novelty **[open]**.

---

## 3. The unification — where A and B converge

This is the substance of "unifying," and it is **cross-method convergence**, not assertion:

1. **The same object.** Branch A's **B206** (character-variety reduction; `frontier/B155`) and Branch B's **Ω₄ / TC-1**
   (history enumeration + metric filter) land on the **same canonical object**: charpoly $(x^2-3x+1)(x^2-x+1)$,
   "golden × phase," **signature $(1,3)$**, minimal/lowest-growth. Two independent starting points reach one canonical
   $(1,3)$ object.
   *Status of the "clean next check" (now partially done, V148):* $M_g$ is **nonderogatory**, so its
   $\mathbb{Q}$-conjugacy class is fully determined by the shared charpoly — *any* matrix with this $\chi$ (including the
   Ω representative) is $\mathbb{Q}$-conjugate to $M_g$. But the **integer** Ω shear family $R_{a,m}$ reaches this
   charpoly only at the **half-integer** point $a=4,\ m=-\tfrac12$ — so there is **no integer $\Omega$ matrix literally
   equal/conjugate over $\mathbb{Z}$ to $M_g$**; the two programs meet at the **shared canonical object** (charpoly +
   signature + $\mathbb{Q}$-conjugacy class), not at a common integer lattice point. The honest unification is at the
   canonical-object level; "the same integer matrix two ways" would overstate it.
   **Decisive scope (the source-chat verdict, B156):** the convergence is on the *object*, **not** a mechanism. The
   two strict-full shears $A=S_{03}$ and $C=S_{23}$ **commute** ($E_{03}E_{23}=E_{23}E_{03}=0\Rightarrow AC=CA$), so the
   map $R\mapsto A,\ L\mapsto C$ **cannot** represent the *noncommutative* trace-map monodromy — and indeed the Ω
   R-cone endpoint entropy is $0$ (order-independent). So **Ω is the abelianized / non-collapse shadow of the tower,
   not its body.** The **Ω↔tower bridge audit** was subsequently **RESOLVED at the spectral level** (B158/V152,
   `OPEN_LEADS` L18): Ω = the **abelianized spectral image** of the metallic tower (the commutative $A,C$ cannot realize
   the noncommutative trace-map monodromy, so Ω is the non-collapse shadow, not a faithful body). *(This doc, dated
   2026-06-16, predates B158; the "never run" phrasing below is superseded — the spectral question is answered, Ω is an
   abelianized image, not fully standalone.)* **[resolved-spectral, B158]**
2. **The same golden/Fibonacci growth.** A's trace map *is* the Fibonacci–Hamiltonian ($\kappa=2+\lambda^2$); B's
   admissible block counts *are* the Fibonacci numbers (growth $\varphi$). Same arithmetic heartbeat.
   ([confirm-with-Ω-handoff] on the B-side count.)
3. **The same reciprocal/symplectic spine.** Both branches force **palindromic** characteristic polynomials (A:
   figure-eight monodromy $x^2-3x+1$; B: TC-2 reciprocity theorem).
4. **The same reduction lesson.** Both learned that the *raw* arena over-counts and the **observable object appears
   only after a quotient/filter** (A: trace-ring/cotangent overcounts the $(n^2-1)$ Jacobian; B: raw histories
   overcount the metric-compatible sector). The cross-branch map artifact already encodes this.
5. **The same firewall.** Both produce rich algebra/combinatorics + a real entropy result and **both stop at the
   identical boundary**: no physics derived.

**What this unification is:** a *mathematical* unification — the program's core object is **canonical**
(method-independent), which is strong evidence it is real and not a notational artifact of one approach. **What it is
not:** a physics derivation. A $(1,3)$ from "golden × phase" is suggestive, but both branches correctly refuse to call
it spacetime. **Internal convergence across instances is corroboration, not validation** — the external specialist
remains the only thing that clears the bar.

---

## 4. The shared firewall (what is NOT claimed, both branches)

The firewall is **logic, not mood**: it is the formal boundary between the **ontological** question (why something
rather than nothing — answered by an existence-fixed-point *structure*) and the **dynamical** question (how something
behaves — needs running scale / Hilbert-space evolution / forced asymmetry, which a static fixed point cannot contain).
Concretely, **none of these are claimed**: a physical spacetime metric; physical/thermodynamic entropy (the entropies
here are combinatorial); gravity, quantum mechanics, cosmology; dark matter, baryogenesis, CP violation; or
expert-level novelty prior to external review. Every clean negative in §1–§2 is the firewall reporting itself
faithfully.

---

## 5. Open frontier (ranked, both branches)

1. **External specialist** — a single qualified human (character varieties / higher Teichmüller / aperiodic order).
   Unmet; the decisive step.
2. **The Ω↔tower bridge audit** — **RESOLVED at the spectral level (B158/V152, `OPEN_LEADS` L18):** Ω is the
   **abelianized spectral image** of the metallic tower. Since $A,C$ **commute**, a faithful (noncommutative)
   realization does *not* exist; the audit settled that Ω is an abelianized image (the non-collapse shadow), not fully
   standalone. *(This "never run" entry is superseded by B158, which postdates this 2026-06-16 doc.)*
   (The B206 ≅ Ω₄ canonical-object identification + the in-repo re-derivation of the Ω side — counts L4–L9, TC-1/TC-2,
   history entropy — are **done**: V148/V149/V150, `frontier/B155`+`B156`.)
3. **Uniform-$n$ / metallic A-polynomial** ($k=4-m(o-3)$) — Branch A's deep prize ($n=5$ open).
4. **Endpoint entropy** and a **forced (non-arbitrary) boundary/asymmetry rule** — Branch B's deep prize.
5. **Off-slice 3-dim component equations** (Branch A) and the **uv-route growth estimate** (Branch B).

---

## 6. Sharing protocol — primary sources

**To brief a fresh session:** §0–§5 of this brief are self-contained and label every claim's status. Then attach the
branch-specific primary sources so the new session can verify rather than trust.

- **Branch A (this repo):** the two-results note (`papers/metallic_trace_map_note/NOTE.md` — $\kappa$, the $L=-M^4$
  slice with its 2026-06-16 correction, B206); `frontier/B155_golden_phase_bridge/`; `frontier/B153`/`B154`; the
  ledger `papers/VALIDATION_LEDGER.md`. *Purpose: the verified character-variety core + the slice correction.*
- **Ω handoff bundle (cross-session, not in this repo):** `MASTER_PROGRESS_LOG.md`, the Ω firewall doc, the
  TC-1/TC-2/TC-4 certificates, the B598–B607 theorem audit, and the latest post-2026-06-15 artifacts (B868–B877
  uv-route-decision; B878–B907 novelty audit / expert packet / paper skeleton). *Purpose: the Ω approach, its theorem,
  and its current edge.* Digest + independent core verification: `audit/handoff_2026-06-15/` (gitignored working room).

**Keep-synced rule:** the canonical object is **golden × phase, signature $(1,3)$, Fibonacci growth**. Any new result
is checked against it. Convergence between instances = corroboration; it does **not** substitute for external
validation. Kills stay killed; physics stays firewalled; "not derived," stated exactly, is itself a result.

---

*Tier: MATH throughout. Physics appears only to be firewalled. This brief is internally corroborated by two
independent branches converging on one object; it has had no external-specialist validation, which — with uniform-$n$
and endpoint entropy — remains the decisive next step. Nothing here promotes to `../CLAIMS.md`.*
