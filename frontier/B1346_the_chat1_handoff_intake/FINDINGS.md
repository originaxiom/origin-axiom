# B1346 — THE chat1 HANDOFF, INTAKEN: 34/34 reproduced, F1 corrects a banked arc, F5 generalises, and Chat-2's nesting is refuted

**Date:** 2026-09-12 · **Seat:** cc · **Lane:** INTAKE + MATHEMATICS.
**Depends on:** B1083, B1297, B1330, B1331, B1341, B1345, B497, B134/B136.
**P0:** every number below is **recomputed on this bench**, not read from the handoff. The seat's
scripts were run, and the load-bearing claims were then re-derived independently.

---

## 1. Their verification, reproduced

`verify/master/verify_all.py` (22 checks) + `verify/master/stageC.py` (12 checks): **34/34 PASS on
this bench**, nothing read from cache. Controls included — `C-NULL` checks that must fail do fail,
`C-ALIVE` checks that must pass do pass. One portability defect: both scripts write to a hardcoded
`/home/claude/...` path *after* all checks (same class as this repo's own `test_no_hardcoded_paths`).

## 2. F1 — CONFIRMED, and it corrects a banked arc

The protection table, recomputed from SnapPy:

| object | H₁ | \|Sym(M)\| | \|Sym(cover)\| | F1's verdict |
|---|---|---|---|---|
| s958 | ℤ/3+ℤ | 2 | **6** | UNPROTECTED |
| v2873 | ℤ/6+ℤ | 4 | **12** | PROTECTED |
| t12833 | ℤ/6+ℤ | 2 | **6** | UNPROTECTED |
| t12835 | ℤ/6+ℤ | 2 | **24** | PROTECTED |

**Every order reproduces.** And t12835's no-computation argument checks: element orders in `S₄` are
`{1,2,3,4}` — **no 6** — so a subgroup of order 6 in the octahedral group is `S₃`, whose lift
inverts.

> **Consequence, and it is theirs:** B1330's headline — *952 in-domain sectors, three primes, seven
> germ shapes* — was run on **v2873, which is PROTECTED**. Its zero is *predicted* by B1297's own
> theorem. **It is a confirmation of a banked result, not evidence that the vanishing survives where
> protection is removed.** That is the vacuity class (E67/E2) on a headline scan.

This bears directly on this bench's own B1332–B1335: the index work should cite the protection split
when it cites B1330.

## 3. F2 / F3 — CONFIRMED at their stated numbers

F2: `1260/1260` at `cs = 0 mod ½` (max residue 1.5e-15); **Kawauchi's τ-even conclusion fails cusped
at 251/1260**; the `A+A` form fails at 697. F3: amphichiral population **283**, classes exactly
`{0, ¼}` with `195/88/0`, the quarter class **88**, involution does not discriminate (**21**), **no**
quarter-class manifold is a cover (`0/88`), control alive (`111/195` are covers), closed side
**37 amphichiral / 11 τ-odd**.

## 4. F5 — CONFIRMED, and it GENERALISES beyond what the handoff claims

Verified independently: `M = [[1,1],[1,0]]` is twist × swap with `det = −1` and characteristic
polynomial `x² − x − 1`; `S·R·S = L`; and the mechanism **`M² = X·swap(X)` holds for every `X ∈
SL₂(ℤ)`** (checked over all entries in `[−2,2]`). So the double tick is *a word followed by its own
mirror, by construction* — amphichirality is not a property to be discovered but a consequence.

**F5's §7.4 states the trade and does not compute it. Computed here:**

> Every metallic unit `λ_m` solves `x² − mx − 1 = 0`, so the **product of its roots is −1 for every
> `m`** — verified `m = 1…8`. **Norm −1 ⟺ det −1 ⟺ the swap.**
>
> **Therefore the forced self-mirroring at tick two is a property of the WHOLE METALLIC FAMILY, not
> of the golden alone.** The escape F5 names (`2+√3`, norm `+1`) works precisely because
> `x² − 4x + 1` is **not** of the form `x² − mx − 1` — it is outside the family.

**And this is the same fact as B1341's.** B1341 proved the obstruction to a least-action principle is
`det(L·P) = −1`. F5 proves that determinant is the swap, and that the swap is `norm(φ) = −1`. So:

> **`norm(λ_m) = −1` ⟺ `det = −1` ⟺ the tick carries the swap ⟺ the double tick is `X·swap(X)`,
> self-mirroring ⟺ chirality is zero ⟺ there is no action at the half step.**
>
> One fact in **five** languages, holding across the entire metallic family. The seat's line —
> *"the golden ratio and the handedness are the same coin; the programme spent it on φ"* — is
> confirmed and is stronger than stated: it spent it on **every** metallic choice available.

## 5. F6 — this bench's refutation of it was WITHDRAWN (B1345 addendum, E58)

Recorded here for the intake trail: B1345 §4 refuted F6 from a transcript paraphrase that had
inverted it. F6 says `I` is a partial sum of an identically-vanishing difference, so **nothing forces
its value** — which is B1335's statement from the other side. Withdrawn same day; `ERROR_LEDGER` E58.

## 6. Chat-2's structural finding 3a — REFUTED

Chat-2's handoff (a different, earlier seat), §3a: *"Drilling the shortest geodesic from `M(A₁) =
m004` produces `M(A₂)` — the silver bundle. Volume match: 3.6638623767 to 10⁻¹⁰ … **Previously
unrecorded in the programme**."*

| | |
|---|---|
| the volume match | **REAL** — 3.6638623767089, to 1e-13 |
| the identification | **FALSE** |

`drill(m004)` along its shortest geodesic (word `bC`) has **two cusps** and is **isometric to m129 —
the Whitehead link complement** (`5²₁` / `L5a1`). **m136, the silver bundle, has one cusp.** A
once-punctured-torus bundle has exactly one cusp, so the identification **cannot hold whatever the
volume agrees to**. `is_isometric_to(m136)` returns **False**; `is_isometric_to(m129)` returns True.

**m136 and m129 are a volume-sharing pair that differ** — and the control that catches exactly this
is in **chat1's own handoff**: `NEG.2 — TRAP: s958 and s961 share volume, differ`. One seat shipped
the trap's antidote while another walked into it.

## 7. What this intake adds to the record

* **B1330's headline needs the protection clause** (§2) — the single most consequential item here.
* **The metallic generalisation** (§4) is new and belongs with B1341: the chirality-zero is not a
  golden accident, it is forced for every `λ_m`.
* **Chat-2's 3a is withdrawn** before it reached a paper (§6).
* The seat's **error ledger 15–34** is itself worth reading — in particular #31, a live SnapPy trap
  (`M.name()` on a filled census manifold **drops the filling**; verified here: `OrientableClosedCensus[0]`
  reprs as `m003(-3,1)`, `.name()` returns `"m003"`, re-instantiating gives the cusped parent at a
  different volume), and #19, *"the absence instrument is what to distrust — 428 of 494 seat-index
  ids have no ledger row."*

**Still open, recorded not chased:** the `J(t12833)` discrepancy from B1345 §5 (this bench exhibits a
pair at 9, the seat reports 13); and the seat's own un-run gates (F5's prior-art status against
Goodman–Heard–Hodgson, F6 §8.4's). **Their standing caution is adopted: assume the un-gated results
are known until checked.**
