# B973 / L135 — SCOUT: the frame, the floor and M12 are ALREADY DEFINED here, and the reconstruction runs in 1.5 seconds

**Date:** 2026-08-08 · **Cell:** scout (definitional archaeology + validation probes)
· **Lane:** MATHEMATICS. Gate 5 untouched. Nothing to `CLAIMS.md`.

---

## 0. THE ANSWER, FIRST

**(c) Is there enough in the repo to reconstruct the frame independently, using only
banked facts and this bench's own instruments?**

> ## **YES — and this scout ran it end to end.**

Every object B958 said the repo lacked — the frame, the floor, M₁₂ — has a **complete,
unambiguous, bench-owned definition already in the repo**, and the whole chain rebuilds
from `frontier/B854_centralizer_exact/e6_centralizer.py` alone in **~1.5 s**, reproducing
every banked number **at a fresh prime never used before (p = 40883)**.

**B958's premise was too narrow.** B958 looked at `frontier/B909_frame_arc/` and found only
`cmt_correct.py`. But **`frontier/B911_cmt_document/` — the same bench, one day earlier —
already contains the independent construction**, in two scripts that this repo wrote,
against the definitional document `CMT_DRAFT.md`. B961 then built `frame.py` while stating
"the specific frame, floor and M12 need … solo's definitions stated precisely enough to
rebuild"; **those definitions are in `CMT_DRAFT.md` §2, in this repo, as a numbered
ingredient table.** No guessing was required and none was done.

**What IS genuinely missing** is named in §6 — and it is not a definition.

---

## 1. THE DEFINITIONS, ASSEMBLED (verbatim, with `file:line`)

### 1.1 The four charges g₈, g₁₄, g₁₆, g₂₂ — COMPLETE

Constructed from scratch, on this bench, in B854. They are the **2T-invariant vectors**,
one in each of four of the six principal-sl(2) blocks of 𝔢₆.

> `frontier/B854_centralizer_exact/e6_centralizer.py:232-239`
> ```python
> for n in [8, 14, 16, 22]:
>     P = sp.zeros(n+1, n+1)
>     for M in G:
>         P += symn(M, n)
>     P = sp.simplify(P / 24)
>     col = [P.col(j) for j in range(n+1) if any(P.col(j))][0]
> ```

> `frontier/B854_centralizer_exact/e6_centralizer.py:242-252`
> ```python
> INV = {}
> for n in [8, 14, 16, 22]:
>     v = hw_vector(n)
>     cur = v[:]; out = [F(0)] * DIM
>     for k in range(n+1):
>         a = Ipoly[n][k]
>         ...
>         cur = ad(f, cur)
>     INV[n] = out
> ```

The full definitional chain, all in that one file, all bench-written:
Cartan matrix (`:15-20`) → roots by `ip(a,a)==2` (`:28-29`) → bimultiplicative ε-cocycle
(`:34-51`) → Chevalley bracket table `BB` (`:71-96`) → **Jacobi verified on 4000 random
triples** (`:132-139`) → principal sl(2) triple (h,e,f) (`:141-178`) → block structure,
**E₆ exponents {1,4,5,7,8,11} recovered not assumed** (`:180-188`) → highest-weight vectors
(`:193-209`) → the 24 unit quaternions of 2T (`:215-224`) → the Sym^n projector /24 → the
four invariants.

**Why exactly {8, 14, 16, 22}:** those are the blocks in which 2T has an invariant. B854's
own FINDINGS names the mechanism: *"They come out as Klein's classical forms: `ΦΨ`, `t·ΦΨ`,
`(ΦΨ)²`, `t·(ΦΨ)²` — reproducing 2T's invariant ring (the E₆ singularity, generators in
degrees 6, 8, 12)."* (`frontier/B854_centralizer_exact/FINDINGS.md:26-28`). Blocks V₂ and
V₁₀ carry no 2T invariant, which is why the frame is four-dimensional and not six.

**Named:** these are **adjoint-sector** objects — elements of 𝔢₆ itself, not 27 vectors.
Every centralizer below is therefore rank-preserving, exactly as the banked ruling says.

### 1.2 THE FRAME — COMPLETE

> `frontier/B911_cmt_document/CMT_DRAFT.md:23-25`
> *"**The orthogonal frame** (ledger LI): the Killing Gram of the four charges is
> **diagonal**, signature **(2,2)**: {g₈, g₁₆} noncompact (+), {g₁₄, g₂₂} compact (−).
> The compact/noncompact split of the frame IS the organizing split of the charge story."*

> `frontier/B911_cmt_document/CMT_DRAFT.md:145`
> `| 2 | the frame | Killing Gram diagonal, signature (2,2); compact pair = {g₁₄, g₂₂} |`

So **the frame := the ordered 4-tuple (g₈, g₁₄, g₁₆, g₂₂) together with its Killing Gram**
— an orthogonal, signature-(2,2) basis of the abelian z(2T) = u(1)⁴. Nothing is left open.
**Rebuilt here** (§3, probe 1): Gram diagonal, signs (+,−,+,−), and the four norms come out
**identical to the recorded values** `+241532928`, `−317708697600`, `+988843239014400/13`,
`−889958915112960000/19`.

### 1.3 THE FLOOR — COMPLETE

> `frontier/B911_cmt_document/CMT_DRAFT.md:32-34`
> *"**The two-level lattice** (ledger LII CL1): z(any nonempty subset of {g₈,g₁₆}) = the
> **30-dim CORE**; z(any subset meeting {g₁₄,g₂₂}) = the **12-dim FLOOR** = z(torus).
> One compact measurement resolves the full superselection algebra to the floor."*

> `frontier/B911_cmt_document/CMT_DRAFT.md:45-46`
> *"**The floor's type** (ledger XXVII X1; cc R3): complexified floor = **A₂ ⊕ u(1)⁴**
> (dim 12, derived 8; the u(1)⁴ = the torus itself)."*

Operationally, in this repo's own code:

> `frontier/B911_cmt_document/cmt_recompute.py:118-131`
> ```python
> # floor = z(torus): kernel of ad14 restricted to core (all four then annihilate)
> ...
> fl = C14.nullspace()                              # floor in core coordinates
> ```

So **the floor := z_{𝔢₆}(g₈, g₁₄, g₁₆, g₂₂) = the centralizer of the whole charge frame**,
dim 12, `= su(3) ⊕ (the four charges)`. **`su(3)_colour := derived(floor)`.**

### 1.4 M₁₂, THE INVISIBLE 12 — COMPLETE

> `frontier/B911_cmt_document/CMT_DRAFT.md:117-127`
> *"**(vi) The invisible 12 = the SMT block.** The three compact-wall centralizers satisfy
> pairwise AND triple intersections = **the floor exactly**; span = **66**
> (inclusion–exclusion 3·30 − 3·12 + 12 = 66 closes); their Killing-perp **M₁₂**
> (dim 12 = 78 − 66, canonical) is **torus-invariant**, meets the core in **0**, carries
> **full-rank (12) action of all four charges**, and satisfies
> **dim ker((ad g₈ + ρ_i·ad g₁₆)|M₁₂) = 4 at each noncompact wall ρ_i**"*

> `frontier/B911_cmt_document/CMT_DRAFT.md:155`
> `| 12 | the invisible 12 | M₁₂ = K-perp of the 66-span; ∩core = 0; torus-invariant; charge-rank 12; ker 4 at μ-walls |`

And as executable code, twice:

> `frontier/B911_cmt_document/cmt_recompute.py:635-642`
> ```python
> # M12 = Killing-perp of span(W1,W2,W3)
> span_cols = W[0] + W[1] + W[2]
> ...
> M12 = nullspacep(rows)
> log(f"  invisible block M12 = Killing-perp of the compact span: dim {len(M12)} (12)")
> ```

> `frontier/B911_cmt_document/cmt_recompute2.py:396-421`
> ```python
> # ---- invisible 12: kernel signature at the true walls ---------------------
> span_cols = W[0] + W[1] + W[2]
> ... M12 = nullspacep(rowsK)
> ```

The `W_j` are the **compact walls**: the centralizers of the compact pencil at the roots of κ.

> `frontier/B911_cmt_document/CMT_DRAFT.md:62-69`
> *"**(i) The compact walls.** The compact pencil h(s) = g₁₄ + s·g₂₂ acts on core/floor
> (18-dim quotient; the floor is pencil-invariant — in fact pencil-killed). Its degeneration
> polynomial is **ν(s) = c · κ(s)⁶**, κ = **2771822592000·s³ + 3033676800·s² − 56402640·s −
> 6859** with κ **irreducible**, constant term **−19³** … discriminant squarefree kernel
> **{7, 11}** ⟹ quadratic resolvent **ℚ(√77)**"*

**Every constant in that chain is derivable from the build** — κ by an 18×18 determinant
interpolation with a *proven* degree bound, μ by a 48×48 one. Neither is an input. Verified
below.

### 1.5 W_frame — DEFINED **AND ALREADY REALIZED ON THIS BENCH** (B939)

The one object CMT_DRAFT marks as unverified —

> `frontier/B911_cmt_document/CMT_DRAFT.md:190`
> `| W_frame = ℤ₂×ℤ₂ (FS4); J1a involution-genericity | solo | **not recomputed** | **[SOLO-TIER, VERIFICATION PENDING]** … |`

— was in fact **computed here two arcs later**, and its element list is explicit:

> `frontier/B939_klein_assembly/assembly.py:349-353`
> ```python
> CHK("C8_frame_pattern_image_is_the_KLEIN",
>     patset == [(-1, -1, -1, -1), (-1, 1, -1, 1),
>                (1, -1, 1, -1), (1, 1, 1, 1)],
>     "P(C8) = W_frame = {identity, compact-flip, noncompact-flip, all-flip} "
>     "= the solo LIII / FS4 Klein, REALIZED")
> ```

i.e. **W_frame = the sign group {id, flip(g₁₄,g₂₂), flip(g₈,g₁₆), flip-all} acting on the
frame coordinates (g₈,g₁₄,g₁₆,g₂₂)**, realized inside Aut(𝔢₆) as the image of the census
subgroup `C8 = ⟨φ₊, σ_c, σ₋₁⟩` with kernel {1, σ₋₁}. `docs/LAW_MAP.md:210` banks it.
**So the CMT_DRAFT "[SOLO-TIER, VERIFICATION PENDING]" row is stale — B939 discharged it.**

---

## 2. THE RECONSTRUCTION RECIPE (each step's only input is the previous step)

| # | object | recipe | check it must pass |
|---|---|---|---|
| 1 | 𝔢₆ | `B854_centralizer_exact/e6_centralizer.py` | Jacobi 4000/4000; dim 78; exponents {1,4,5,7,8,11} |
| 2 | the four charges | `INV[8], INV[14], INV[16], INV[22]` — 2T-invariants of the principal sl(2) blocks | 6/6 brackets vanish; rank 4; K_C rank 0 |
| 3 | **the frame** | the Killing Gram `G_ij = tr(ad gᵢ · ad gⱼ)` | diagonal; signs (+,−,+,−); the four recorded norms |
| 4 | **the core** | `ker ad(g₈)` | dim 30; `ad(g₁₆)` kills it |
| 5 | **the floor** | `ker(ad(g₁₄)\|core)` = z(all four) | dim 12; `ad(g₂₂)`, `ad(g₁₆)` kill it; the 4 charges lie inside |
| 6 | **su(3)_colour** | `derived(floor)` | dim 8; perfect; centre 0 ⟹ A₂ (unique 8-dim semisimple) |
| 7 | **κ** | det of the 18×18 compact pencil `g₁₄+s·g₂₂` on core/floor, 19 nodes + 6 checks, deg ≤ 18 proven | ν = c·κ⁶; κ irreducible; κ(0) = −19³; disc kernel {7,11} |
| 8 | **the compact walls W₁,W₂,W₃** | `ker(ad g₁₄ + s_j ad g₂₂)` at κ's roots mod a split prime | dim 30 each; span 66 |
| 9 | **M₁₂** | Killing-perp of span(W₁,W₂,W₃) | dim 12; ∩core = 0; torus-invariant; charge ranks (12,12,12,12) |
| 10 | **the generation walls** | roots of `N(t) = det(ad(g₈+t·g₁₆) \| 𝔢₆/core)`, deg 48, 49 nodes + 6 checks | N = c·(cubic)¹⁶; z dim 46 |
| 11 | **W_frame** | the sign-flip Klein on (g₈,g₁₄,g₁₆,g₂₂); realized as `P(C8)`, B939 | order 4; lone flips excluded |

**Normalization hazard (load-bearing, `CMT_DRAFT.md:249-262`):** the raw B854 charges live in
the *solo* normalization; the banked B880-lane cubic is the g₁₆-integralized one, related by
`μ_solo(ρ) = 13³·CUBIC_banked(ρ/13)`. Running the pairing suite with the wrong lane's roots
gives a **structurally wrong** (all-18, no matching) answer, not a noisy one. Step 10 above
avoids the hazard entirely by deriving the walls from the build.

---

## 3. WHAT THIS SCOUT ACTUALLY RAN (compute, don't cite)

All six probes are in this directory; all use only `B854`'s build + `B961`'s `frame.py`;
no incoming code; exact ℚ where char-0, exact 𝔽_p where mod-p; no floats.

### Probe 1 — the frame and the floor, EXACT over ℚ (0.5 s)

```
frame Gram = diag(241532928, -317708697600, 988843239014400/13, -889958915112960000/19)
diagonal: True; signs [+1,-1,+1,-1]  -> signature (2,2)
dim z(g8) = 30; ad16 kills it: True                      (the core)
dim floor = 12; ad22 kills: True; ad16 kills: True
the four charges lie inside the floor: True
dim [floor,floor] = 8;  centre = 4
[[floor,floor],[floor,floor]] = 8  (perfect);  centre of [floor,floor] = 0
```
⟹ **floor = su(3) ⊕ u(1)⁴, dim 12** — 8-dimensional semisimple is uniquely A₂ (3+3 = 6,
3+3+3 = 9, so no decomposable option; simple dim-8 is A₂ alone). *This is the first exact,
from-scratch derivation of "the floor" on this bench, and it took half a second.*

### Probe 2 — κ and M₁₂, at a FRESH prime (1.5 s)

```
quotient dim = 18; deg nu <= 18 PROVEN (18x18, entries affine in s)
nu degree 18; 6 extra-node checks: True;  nu = c * (cubic)^6 : True
kappa = 2771822592000*s**3 + 3033676800*s**2 - 56402640*s - 6859
irreducible True; const -19^3 True; disc squarefree kernel [7, 11]
fresh split prime p = 40883
compact walls s = 25358, 36658, 37349 : dim z = 30, 30, 30 ;  triple span = 66
Killing rank mod p = 78
M12 = Killing-perp of the 66-span: dim 12
M12 cap core = 0 ; torus-invariant: True ; charge ranks [12,12,12,12]
```

**κ came out coefficient-identical to the recorded one, from an independent run.** p = 40883
is **new**: the record's primes are {40009, 40013, 40037, 40039, 40063, 40123, 40639, 40829}.

### Probe 6 — the generation walls DERIVED, so no incoming constant enters (6 s)

```
core killed by the pencil (first 30 columns zero): True
N(t) degree 48 (48); extra-node checks True
N(t) roots = the noncompact (generation) walls, DERIVED: [15447, 30135, 33694]
  equal to mu's roots mod p: True
  N = c * prod(t - r_i)^16 at 8 random points: True
```

### Probes 3–5 — SCOUT-TIER evidence on the presence side (one fresh prime; **not** a banking)

Since the reconstruction reproduces every banked frame number, five of B958's seven
presence-side claims were cheap to look at. **Each is paired with a control that could have
made it fail.**

| B958's claim | this scout, p = 40883 | control (non-vacuity) |
|---|---|---|
| `[M12,M12]` escapes by exactly 4 into the torus | dim[M₁₂,M₁₂] = **16**, ∩M₁₂ = **12**, ∩core = **4**, ∩floor = **4** | ✔ escape is 4, not 0 and not 16 |
| `[floor, M12]` = 12 with ZERO escape | rank = **12**, escape = **0** | ✔ `[z(x₁), M₁₂]` escapes by 50 in the same code |
| not a module over the FMT so(10) (escape 50) | escape = **50**; dim z(x₁) = 46 | ✔ the floor's escape is 0 in the same code |
| centre 0 | **0** | ✔ centre-of-derived(floor) code returns 0 here and 4 for the floor |
| twelve colour-blind lines (su(3) weights all (0,0)) | rank`[su(3)_floor, M₁₂]` = **0** | ✔ `[torus, M₁₂]` rank **12**; `[su(3)_floor, core]` rank **26** — the operator is not the zero map and the test can fail |
| orbit↔generation bijection (each μ-wall kills exactly 4) | kernels at the three derived μ-walls = **4, 4, 4** | ✔ a **generic** ρ gives kernel **0** |
| closure under exactly W_frame, three free orbits | **not run** — needs the weight-line decomposition | — |

**Tier discipline, stated plainly.** These are **one fresh prime, mod-p**. Per the bound
directions recorded at `CMT_DRAFT.md:161-166`, mod-p rank ≤ char-0 rank, so a mod-p **rank
0** (the colour-blindness leg) is **evidence, not a certificate**; the dimension results are
likewise mod-p tier. What this adds is a **third independent prime** on results the solo
seat recorded at 40039 and 40063 — computed on a frame this bench rebuilt from its own e₆.
**Nothing here is banked and nothing here verifies the presence side.**

### One error of my own, recorded

Probe 4's `[M12,M12] ∩ core` first returned **54**, which is impossible (the core is 30-dim).
Cause: I fed 66 non-independent bracket vectors into a dimension formula that assumes a
basis. Fixed in probe 5 by basis-reducing first ⟹ 4 and 4. The absurd number caught it;
had the bug produced a plausible number it would have looked like a finding.

---

## 4. WHERE THE PRIOR ART SITS (rule 5 — this is reproduction, not discovery)

| what | where it already was |
|---|---|
| the four charges, exact | **B854** (bench-owned, 2026-08-02) |
| frame Gram diagonal, (2,2), the four norms | **B911** `cmt_frame_check.py`; `CMT_DRAFT.md:26-31` |
| core 30 / floor 12 / floor type A₂⊕u(1)⁴ | **B911** stage 1; `CMT_DRAFT.md:32-46` |
| κ = c·(cubic), −19³, disc {7,11} | **B911** stage 2 (exact, 19+6 nodes) |
| M₁₂ = Killing-perp of the 66-span, all four properties | **B911** `cmt_recompute.py:635-664`, `cmt_recompute2.py:396-431` |
| μ-walls derived from the build (deg-48) | **B911** `cmt_recompute2.py` |
| W_frame realized in Aut(𝔢₆) | **B939** `assembly.py:349-357`; `docs/LAW_MAP.md:210` |
| dim Z(su(3)) = 16 | **B958**, **B961** |

**Everything this scout computed is a reproduction.** Its only new content is (i) the
archaeology itself, (ii) a **third** prime, and (iii) the correction in §5.

---

## 5. THE CORRECTION B958/B961 NEED

1. **`frontier/B958_presence_scope/FINDINGS.md:11`** — *"The repo contains no independent
   construction of M12 (the 'invisible 12')."* — and `:19` *"So the invisible 12 has never
   been independently constructed here."* **These are incorrect as stated.** B958 inspected
   `frontier/B909_frame_arc/` and generalized from it; `frontier/B911_cmt_document/` — a
   *cc* computation cell, whose own provenance note reads *"This arc (B911 computation seat)
   contributed the independent recomputation manifest of §4"* (`CMT_DRAFT.md:320-322`) —
   contains the construction, the definitional document, and the run logs. The accurate
   statement is: **B909 verified by running incoming code; B911 had already rebuilt it.**

2. **`frontier/B961_frame_instrument/FINDINGS.md:60-62`** — *"the specific frame, floor and
   M12 need either solo's definitions stated precisely enough to rebuild, or an independent
   derivation…"* — the definitions **were** already stated precisely enough, in
   `CMT_DRAFT.md` §0 and the §2 ingredient table, in this repo. B961's deferral was
   *conservative in the right direction* but the premise was wrong.

3. **A trap worth naming, since it is the exact "right object, wrong level" shape.**
   `frame.py:162-168` defines `su(3)_colour` as the **standard A₂ Levi of the Chevalley
   Cartan** (the first adjacent simple-root pair). The presence side's colour is
   **derived(floor)** — a *different* subalgebra of 𝔢₆. B958's necessary condition survives
   because it only used a dimension, and **this scout computed that the two agree**:
   `dim Z(su(3)_floor) = 16 = dim Z(standard A₂ Levi)`. But any test finer than a dimension
   **must use derived(floor)**, not the Levi. (Equal centralizer dimension is consistent
   with conjugacy; it is **not** a proof of it, and this scout did not prove it.)

4. **`CMT_DRAFT.md:190`'s W_frame row is stale** — B939 discharged it.

---

## 6. WHAT IS GENUINELY MISSING (and it is not a definition)

1. **Char-0 exactification.** Walls, M₁₂ and every presence-side dimension are **mod-p
   tier**. `CMT_DRAFT.md:268-270` names the fix (restriction of scalars over K, the FMT
   recipe). This is the real gap and it is a *tier* gap, not a definitional one.
2. **The weight-line decomposition of M₁₂** — the twelve multiplicity-one charge weights,
   needed for the W_frame-orbit and orbit↔generation claims. **Reconstructible** (simultaneous
   eigenlines of the four `ad(gᵢ)|M₁₂` over 𝔽_p — probe 3 already shows they act with rank
   12 and commute), but not run here.
3. **The presence side's own §LXXXIII–LXXXVI + §XCII text** is **not in the repo** — it is
   incoming material. But the repo does not *need* it to rebuild: B958's own §3 lists all
   seven claims, and this scout re-derived five of them from repo-side definitions alone.
4. **The exact rational seeds as 𝔢₆ roots** and the seed-Gram question — solo's own §LXXXV-O3
   was **withdrawn** as a labelling artifact (B946 §(a) concurred), so this is not owed.
5. **`I-4`: G₂⊕G₂ ⊄ 𝔢₆** — the one unpinned external import in the whole frame arc
   (`CMT_DRAFT.md:245`). Not needed for the frame/floor/M₁₂ construction; needed only for
   *typing* the compact walls as so(8)⊕u(1)².

---

## 7. MB12 VACUITY STATEMENT

Every check used here can pass **and** can fail, demonstrated in-run:

- *floor typing* — could have returned any dim; returned 8 with centre 0 while the floor
  itself has centre 4.
- *M₁₂ ∩ core = 0* — the same routine returns 4 for `[M₁₂,M₁₂] ∩ core` and 30 for core∩core.
- *colour-blindness* — the same routine returns rank 12 for the torus and 26 for the core.
- *μ-wall kernels = 4* — a generic ρ returns 0.
- *N(t) degree 48 / ν degree 18* — both had **proven** structural degree bounds plus 6
  surplus check nodes (the §LIV retraction lesson, applied).

The one check I will **not** call non-vacuous: mod-p rank **0** as evidence for char-0 rank
0. It runs the bound the wrong way and is recorded as evidence only.

---

## 8. VERDICT

> **L135's remaining half is NOT blocked and never was.** The frame, the floor, su(3)_colour,
> κ, the compact walls, M₁₂, the generation walls and W_frame are all defined in this repo,
> in bench-owned artifacts, precisely enough to rebuild — and the rebuild takes seconds and
> reproduces every banked number at a fresh prime.
>
> The honest deferral B958 wrote was **correct in method and wrong in premise**: it protected
> against guessing a definition that did not, in fact, need guessing.
>
> **Recommended next cell:** the weight-line decomposition of M₁₂ + the W_frame orbit test +
> the orbit↔generation bijection, at two fresh primes, followed by the char-0 exactification
> pass. That closes the presence-side debt with this bench's own instrument.

**Files:** `probe1_frame_and_floor.py`, `probe2_kappa_and_m12.py`, `probe3_colour_blind.py`,
`probe4_presence_structural.py`, `probe5_intersection_fix.py`, `probe6_mu_from_build.py`
→ `scout_probe*_results.json`, `scout.json`.
