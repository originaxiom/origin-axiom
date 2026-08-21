# V-2 — THE COMPACT-COLOR KERNEL SWEEP: derivation notes, checksum catches, fences

**Question (C-AR1).** The sign-lifts realizing so(3,1) ⊕ su(3) inside a real form of
E6 form a torsor over a finite 𝔽₂-kernel. Does any kernel element, over both lattice
classes, give a real form with COMPACT su(3) color?

**Verdict: NO-COMPACT-HOST**, exhaustive within a fully-specified and validated
construction. See the table at the end.

## 0. Why this had to be rebuilt from scratch

B1118/B1119 are harvest arcs: an outside bench's prose memo + captured stdout
(`anomaly_resolved_out.txt`) survive, but no in-repo runnable script builds the
sign-lift, the mirror involution, or the real-form machinery — the repo-side lock
(`tests/test_b1119_anomaly.py`) is a transcript-assert on `FINDINGS.md` text, not a
recomputation. So this arc could not "load and extend" prior code; it had to
independently *re-derive* the entire construction from the standard theory of real
forms via signed lifts of a Chevalley basis, then check it against the three
numbers B1119 reported (split +6, compact −78, variant A +2/(5,3)) as the
falsifiable target. All three reproduced exactly (see §4). Variant B's reported
(+6, su(2,1)/(4,4)) was **not** reproduced by any construction found here — flagged
honestly in §6, not hidden.

## 1. The corrected ad-invariant form

Chevalley basis {h_i, e_r}, this repo's vendored module (`e6_bracket_vendored.py`,
same one B1098/B1102/B1114 use). Verified first: `eta(r) := eps(r,-r) = -1` for
**all** 72 roots (the paper's convention `[e_r,e_-r] = -h_r`, confirmed not
assumed). The ad-invariant form:

- `B(h_i, h_j) = A[i][j]` (the Cartan matrix — positive definite, standard for
  finite type)
- `B(e_r, e_-r) = -1` (the CORRECTED sign; B1119's bug was `+1` here)
- all other pairs 0

Verified ad-invariant (`<[x,y],z> + <y,[x,z]> = 0`) on 300 random triples, exact,
zero failures. **Negative control**: the wrong (`+1`) form was built side-by-side and
correctly FAILS ad-invariance (13/300 on this run's random seed) — reproducing
B1119's own bug detection as a live check, not a cited fact.

Structural fact used repeatedly below: `B` restricted to any fixed A2 factor (2
simple coroots + 6 root vectors, untransformed) is **always** `(5,3,0)` — the
Cartan block contributes `(2,0)` (positive definite) and each of the 3
positive-root hyperbolic planes `{e_r, e_-r}` contributes `(1,1)`. This is a
property of the split basis, independent of any θ, and was verified directly
(not assumed) before trusting any θ-dependent reading of it.

## 2. hatch / I1 / I2, re-derived

Own re-run of B1114's construction (same method, own code): hatch A2 at simple
nodes (0,2); its principal sl2 triple = B1098's stored `(X,H,Y)`. The 12 roots
orthogonal to hatch's A2 split into two rank-2 components of 6 roots each — **I1**
(comp1) and **I2** (comp2). B1114 proved I2 = the joint centralizer of hatch's
triple and I1's principal triple = color; that fact is cited, not re-derived here
(this arc's own new content starts at the real-form layer).

## 3. The two lattice classes, found not guessed

The "mirror swap" is the order-2 outer diagram automorphism of E6. In this
module's labeling (Bourbaki-like, branch node 3, short arm at node 1, long arms
0–2 and 4–5), it is **π_mirror: 0↔5, 2↔4, fix 1,3** — verified as a genuine
order-2 root-system automorphism (preserves the Cartan matrix, bijects the 72
roots to roots, is an isometry on 500 random pairs, `π² = id` on all 72 roots).

**Computed, not assumed**: `π_mirror(hatch's 6 roots) = I1's 6 roots exactly`, and
`π_mirror(I2) = I2` **pointwise** (every one of I2's 6 roots is individually
fixed). This is CLASS A ("identity on color").

CLASS B needs an independent twist that still swaps hatch↔I1 but acts
non-trivially on I2. `w0(I2)`, the longest Weyl element of I2's own A2 (built from
3 reflections in I2's simple roots), was verified to fix hatch and I1 **pointwise**
(their roots are orthogonal to I2's, by the same orthogonality that built I1/I2 in
the first place) while permuting I2's own 6 roots non-trivially (not simple
negation — A2's own longest element is not −1; combined with A2's own diagram flip
it would be, mirroring the E6-level story one level down). `π_B := π_mirror ∘
w0(I2)` is verified as a second genuine order-2 root-system automorphism that
swaps hatch↔I1 and fixes I2 only *setwise*, not pointwise. This is CLASS B
("duality on color").

A broader search (explored, not shipped as a third class) tried composing
π_mirror with matched Weyl-twists of hatch and I1 too (12 further candidates,
brute-forced over `W(hatch) × W(I1) × {1, w0(I2)}` and filtered to genuine
involutions that still swap hatch↔I1 and fix I2 setwise). All 12 gave only
characters {+2, −2} — nothing new relative to classes A/B — so the two-class
reading is not just a guess of convenience, it appears to exhaust the "swap
hatch↔I1 via a matched Weyl twist" family.

## 4. Two Chevalley-automorphism ansätze ("both constructions", crossed with A/B)

Two shapes of signed lift both solve the automorphism equations for a general
root-system automorphism π:

- **antipodal** (generalizes the textbook Cartan involution of the split form):
  `θ(h) = -π(h)`, `θ(e_r) = ε(r)·e_{-π(r)}`
- **permute** (generalizes the trivial/compact-commuting twist):
  `θ(h) = +π(h)`, `θ(e_r) = ε(r)·e_{π(r)}`

For π = id, antipodal's base case (ε≡1) is exactly the split form's own Cartan
involution (character +6); permute's base case (ε≡1) is θ = the identity map
exactly (character −78, the compact control). Both were needed as controls; both
matched.

**The sign function ε: (72 roots) → {±1}** must satisfy, for both ansätze: (i)
evenness `ε(-r) = ε(r)`; (ii) the two-root cocycle
`ε(r+s)·eps(r,s) = ε(r)·ε(s)·eps(π(r),π(s))` whenever `r,s,r+s` are all roots;
**and (iii), found necessary by direct falsification, not assumed from the
start: `ε(π(r)) = ε(r)` whenever `π(r) ≠ r`.** Without (iii), the cocycle-only
"solutions" include sign choices for which `θ² ≠ I` — checked explicitly:
building the full matrix for several such elements showed `θ² ≠ I` exactly, i.e.
NOT an involution, hence not a Cartan-involution candidate at all. Constraint
(iii) was added and the kernel shrank accordingly (from a uniform 6 for every π
before the fix, to 4 for class A and 3 for class B after it, in both ansätze). All
72×2=144 constraint rows plus the ~800 cocycle rows are solved by exact 𝔽₂ Gaussian
elimination; consistency (no `0 = 1` row) is checked before ever reading off a
kernel.

## 5. THE KERNEL: k and its structure

| construction | π (lattice class) | k | \|kernel\| |
|---|---|---|---|
| antipodal | A (π_mirror) | **4** | 16 |
| antipodal | B (π_mirror·w0(I2)) | **3** | 8 |
| permute | A (π_mirror) | **4** | 16 |
| permute | B (π_mirror·w0(I2)) | **3** | 8 |

k is **not** a single number across "the" kernel — it depends on which lattice
class (the homogeneous cocycle system is π-independent in its two-root part, but
constraint (iii) is π-dependent: π_B moves more roots than π_A, so it imposes more
independent constraints, shrinking k from 4 to 3). All four systems are
consistent (a valid sign lift exists in every case). The 48 total elements (16 +
8 + 16 + 8) were enumerated exhaustively — every single one, not a sample — and
each was individually verified for `θ² = I` (exact 78×78 check) and checksum
membership. A stratified re-verification (300-trial random bracket-automorphism
check) was run on every element that superficially looked compact before trusting
it (see §7 — none survived, so this fired zero times in practice, but the gate is
live in the code).

## 6. THE CHECKSUM CAUGHT TWO DIFFERENT THINGS

**First-level (B1119's own method): the classification checksum.** Character must
be in {+6, +2, −14, −26, −78}; anything else means the instrument is lying. This
caught: (a) the wrong (+1) invariant form immediately fails ad-invariance (§1);
(b) an early attempt at π_B's construction (before constraint (iii) was found)
produced character −2 as a "solution" that is genuinely impossible — chasing why
led directly to discovering the missing `θ²=id` constraint.

**Second-level (this arc's own addition, not previously banked): PURITY.** A
character passing the classification checksum is NECESSARY but **not sufficient**
for the underlying θ to be a genuine, cleanly-split Cartan involution. Concretely:
Family "permute", class A, gave character **−26** — E6(−26) = EIV = M(𝕆,ℂ), the
form whose maximal compact is f4 ⊃ compact su(3), the form C-AR1 specifically
flagged as unreached. This looked like the answer. Rigorous re-verification
(`θ²=I` exact, 300-trial bracket automorphism, 0 failures) confirmed it IS a
genuine involutive automorphism of e6(ℂ) with character exactly −26. But the
color (I2) restriction, computed exactly, is `dim(θ=+1 part of I2) = 8,
dim(θ=−1 part) = 0`, and **the invariant form restricted to that full 8-dimensional
piece is `(5, 3, 0)` — indefinite, not `(8,0,0)` or `(0,8,0)`.** This is not a
computational accident: since θ fixes all of I2 pointwise for this element (same
mechanism as class A), the restriction is *exactly* the fixed structural fact from
§1 (`B|I2 = (5,3,0)` always, for the untransformed split basis) — it can never be
compact by this route, no matter which kernel element is chosen, because I2 simply
never moves. The −26 character is real; the color reading it would need to carry
compactness is not. Every element in the full sweep (§5) was checked for this
purity property, not just the −26 ones — see the table below.

## 7. THE FULL TABLE (every element, all four constructions)

| construction | character(s) seen | n elements | θ²=I | checksum-pass | color-pure | compact color |
|---|---|---:|---:|---:|---:|---|
| antipodal / A | +2 (uniform) | 16 | 16/16 | 16/16 | 4/16 | **0** |
| antipodal / B | +2 (uniform) | 8 | 8/8 | 8/8 | 0/8 | **0** |
| permute / A | −26 (×4), +6 (×12) | 16 | 16/16 | 16/16 | 0/16 | **0** |
| permute / B | +6 (uniform) | 8 | 8/8 | 8/8 | 0/8 | **0** |

Every character reached anywhere in the exhaustive sweep is checksum-legal:
{+2, +6, −26} ⊂ {+6,+2,−14,−26,−78}; zero impossible values escaped once
constraint (iii) was in place. **Color purity (a well-defined compact-vs-not
reading at all) is achieved ONLY in antipodal/A, and there the color signature is
FIXED at (5,3) — sl(3,ℝ), split, never compact — across its entire kernel** (the
4 pure elements out of 16 all read exactly `sig_plus=[0,3,0], sig_minus=[5,0,0]`,
i.e. the same (5,3) as variant A's base element; character is uniform at +2 for
the whole antipodal/A kernel regardless of purity). In every other construction,
the color-level restriction is indefinite for 100% of elements — not even a
candidate compact/non-compact reading exists there, let alone a compact one.

**Zero elements, across 48 exhaustively-enumerated and individually-verified
kernel elements spanning two independent Chevalley-automorphism ansätze and both
lattice classes, give color signature (8,0) or (0,8).**

## 8. Controls (reproduced before the sweep, per protocol)

| control | expected | got | match |
|---|---|---|---|
| split (antipodal, π=id) | char +6, dims (36,42) | +6, (36,42), globally pure | exact |
| compact (permute, π=id, θ=identity) | char −78, dims (78,0) | −78, (78,0) | exact |
| variant A base (antipodal, π=A) | char +2, color (5,3) | +2, color (5,3), pure | **exact** |
| variant B base (antipodal, π=B) | char +6, color su(2,1) (4,4) | char **−2** (impossible) at the naive base point; full kernel gives only {+2} once θ²=id is enforced | **NOT reproduced** |

## 9. Honest fence: variant B

B1118/B1119's variant B (mirror swap + "duality on color" → E6(6) split, character
+6, color su(2,1) signature (4,4)) was **not** reproduced by any construction
tried here, despite: the natural candidate (antipodal, π_B) whose base element
gives an impossible character; the same construction's full, properly-filtered
8-element kernel giving only +2 (never +6); a 12-candidate systematic search over
matched Weyl-twists of hatch/I1 within the antipodal family (only ever ±2); and
permute/A and permute/B, which DO reach +6, but with an indefinite (impure) color
restriction — not a validated match to "su(2,1)" in the clean Cartan-decomposition
sense variant A's reproduction demonstrated is achievable when it genuinely holds.
Per the task's own protocol this is reported as a discrepancy, not smoothed over:
**this instrument reproduces 3 of B1119's 4 reported control numbers exactly
(split, compact, variant A — including variant A's exact color signature, not
just its character), and does not reproduce variant B.** The compact-color
verdict below rests on the parts of the instrument that ARE validated (the
classification checksum behaved correctly throughout, including on the wrong-form
negative control and on the −26 near-miss; the purity check is a new,
independently-motivated structural criterion, not tuned to produce this
particular answer — it was discovered via the −26 anomaly, applied uniformly
afterward to all 48 elements including the ones that already matched known
numbers).

## 10. Scope of "both lattice classes" and what would extend this

"Both lattice classes" is read here as the two cosets of Out(E6) ≅ ℤ/2 realized
relative to the hatch/I1/I2 decomposition: class A (π_mirror alone) and class B
(π_mirror composed with I2's own outer twist) — the reading directly supported by
B1118's own phrasing ("mirror swap, identity on color" / "mirror swap, duality on
color") and independently corroborated by the 12-candidate search finding nothing
beyond these two. It is NOT a claim that Aut(e6, Chevalley basis) has been swept
in full (that group is large — W(E6) ⋊ ℤ/2, order 103680); it is a claim that the
constructions which (a) actually realize the Lorentz-hosting swap hatch↔I1 (B1114's
own requirement) and (b) are the natural one-bit "color twist" on top of that swap,
have been swept exhaustively, in both of the two independent Chevalley-automorphism
shapes that generalize compact-relative and split-relative constructions
respectively. A further, not-yet-tried direction: Weyl-twists of I2 OTHER than its
own longest element (there are only 6 elements of W(I2)=S3 total, all could be
tried; w0(I2) is the only non-identity involution among them, so this is likely
already exhausted for A2, but stated as an open corner rather than assumed closed).
