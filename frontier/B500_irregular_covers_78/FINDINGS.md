# B500 — Gate A class 2c: **SEALED (horizon → index 8)** — the index-7/8 cover censuses are canonical multisets; at index 8 the B349 collapse clause gets its honest correction (the canonical datum is the *isometry-class* multiset)

**Status: banked (frontier), Closure Campaign Phase 2, class 2c (prereg
`docs/CLOSURE_CAMPAIGN_2026-07.md` + local `README.md`; outcome enum SEALED / COUNTEREXAMPLE /
TOOL-BLOCKED/BUDGET-CAPPED). Verdict: SEALED — a horizon extension (index ≤ 6 → index ≤ 8),
not a theorem (C-guardrail). Budget: hard cap 90 min; actual total ≈ 1 s (enumeration wall
0.10 s at index 7, 0.09 s at index 8) — the BUDGET-CAPPED branch is implemented, logged, and
not taken. Firewalled; nothing to `CLAIMS.md`.**

Gate A (S032-A) asks whether any invariant of the single seed hands the object a forced
choice — a distinguished member of an otherwise indistinguishable set (B330's three-condition
test). B349 answered "no" for the full cover census of 4₁ through index 6; this probe extends
the horizon to indexes 7 and 8 with B349's own machinery (reused via importlib, not
re-derived), B350's exact monodromy algebra, and two independent SnapPy enumeration routes.

## 0. Controls (prereg: fail ⇒ INVALID; all PASS)

- **B349's index ≤ 6 census reproduced exactly** (B349's own code rerun): counts 2 / 4 / 11 at
  index 4 / 5 / 6, the banked canonical multisets, and every index-5/6 invariant-multiplicity
  group collapsing to a **single** isometry class. ✓
- **B350 cross-validation, extended.** The cyclic members' SnapPy `H₁` torsion equals B350's
  `coker(Aⁿ−I)` Smith normal forms exactly for `n = 2..6` (`[5]`, `[4,4]`, `[3,15]`,
  `[11,11]`, `[8,40]`), and B350's exact ladder extends: `n=7 → (29,29)`, order
  `841 = 29² = L₁₄−2`; `n=8 → (21,105)`, order `2205 = 21·105 = L₁₆−2` — the P8/C5 Lucas
  orders, two independent routes (subgroup enumeration vs. monodromy algebra), one answer. ✓
  (Observed shape through `n = 8`, not claimed beyond: odd `n` → `(Lₙ, Lₙ)`; even `n` →
  `(Fₙ, 5Fₙ)`.)

## 1. Index 7 — 9 covers; the B349 pattern holds intact

Enumeration: SnapPy `low_index` and `snappea` routes agree (identical multisets); every cover
has volume `7·v₄` (max defect `7.1e−15`, certified-numerical tier; counts/H₁ exact).

| type | H₁ | cusps | count | isometry classes | rep symmetry (full-group gate) | chirality |
|---|---|---|---|---|---|---|
| cyclic | ℤ/29⊕ℤ/29⊕ℤ | 1 | 1 | — | order 56, full | amphichiral |
| irregular | ℤ³ | 3 | 4 | **1** (collapse) | order 2, full | chiral |
| irregular | ℤ/14⊕ℤ | 1 | 4 | **1** (collapse) | order 2, full | chiral |

Both ×4 multiplicity groups collapse to a single isometry class — the same self-identification
as B349's index ≤ 6 (non-conjugate subgroups, one geometric object; the covering isometries
live in the commensurator). Same-class members share the canonical-retriangulation signature
**and** the exact degree-2 sub-cover census. **Every within-index invariant multiplicity is
resolved by isometry at index 7.**

## 2. Index 8 — 10 covers; the probe's one new structural fact

Routes agree; volumes `= 8·v₄` (max defect `1.1e−14`).

| type | H₁ | cusps | count | isometry classes | rep symmetry | chirality |
|---|---|---|---|---|---|---|
| cyclic | ℤ/21⊕ℤ/105⊕ℤ | 1 | 1 | — | order 64, full | amphichiral |
| irregular | ℤ² | 2 | 1 | — | order 16, full | amphichiral |
| irregular | ℤ/3⊕ℤ/3⊕ℤ² | 2 | 3 | **2 — sizes [2, 1]** | order 4 / order 16 | chiral / amphichiral |
| irregular | ℤ/3⊕ℤ² | 2 | 2 | **1** (collapse) | order 4, full | chiral |
| irregular | ℤ/30⊕ℤ | 1 | 2 | **1** (collapse) | order 4, full | chiral |
| irregular | ℤ/5⊕ℤ² | 2 | 1 | — | order 32, full | amphichiral |

**The `ℤ/3⊕ℤ/3⊕ℤ²` multiplicity group of size 3 does NOT collapse.** It refines into two
isometry classes: the pair `{4_1~irr~0, 4_1~irr~9}` (isometric; chiral; symmetry ℤ/2×ℤ/2) and
the singleton `{4_1~irr~3}` (amphichiral; symmetry order 16). The separation is **exact-tier**:
the degree-2 sub-cover censuses differ as multisets of `(H₁ torsion, betti)` —
pair: `{ℤ/3²⊕ℤ², ℤ/3⁴⊕ℤ², ℤ/3²⊕ℤ/15⊕ℤ²}`; singleton: `{ℤ/3²⊕ℤ² (×2), ℤ/3⊕ℤ/15⊕ℤ²}` — a pure
subgroup-enumeration/SNF integer computation, a π₁ (hence homeomorphism) invariant, no
hyperbolic numerics anywhere in the separation. The canonical-retriangulation signatures and
the symmetry groups concur.

**So B349's clause (iii) — "every within-index invariant multiplicity is resolved by
isometry" — is index ≤ 7-specific.** Its honest, correct form at index 8: **the canonical
datum is the multiset of isometry classes.** Every *residual* same-invariant multiplicity (the
2× classes) is isometry-identified, and the non-collapsing member is separated by finer
canonical invariants (sub-cover census, signature, symmetry group, chirality) —
**classification, not choice**. This is the opposite direction from a forced choice: a
COUNTEREXAMPLE needs an unsymmetrizable mark on a member that canonical data *cannot*
separate; here more canonical data resolves the multiplicity completely. No member of any
invariantly-indistinguishable set is distinguished at either index.

## 3. The orientation-honest oriented census (structural, MB-guard-clean)

The base is amphichiral (`symmetry_group().is_amphicheiral()` under the `is_full_group()`
gate — the B128-validated control), so the index-k cover multiset is **closed under
mirroring**, and the mirror bijection preserves every invariant, hence every multiplicity
group and every orientation-blind isometry class. A *chiral* class of size `s` therefore
refines, as oriented manifolds, to the mirror-symmetric multiset `{s/2 · X, s/2 · X̄}` (a
σ-invariant subgroup would lift the orientation-reversing isometry and contradict chirality,
so `s` is forced even — checked: all chiral classes have even size); an amphichiral class is
its own mirror. Oriented refinements: index 7 — both ×4 chiral classes → `{2X, 2X̄}`;
index 8 — the three ×2 chiral classes → `{X, X̄}` each. **No oriented member is distinguished
either** — B348's "amphichirality kills the sign" landing in the cover class. (Tier:
structural deduction from mirror-closure + MB-guard chirality; *not* from oriented isometry
testing, which `is_isometric_to` cannot honestly provide.)

## 4. MB-guard note

`is_isometric_to()` is orientation-**blind** (REPRODUCIBILITY MB/B128) and is used here
**only for identification** — B349's stance, still sufficient honestly: gate A asks whether
the object *distinguishes* a member, and identification by *any* self-isometry already
defeats a forced choice. Chirality is read **only** from `symmetry_group().is_amphicheiral()`
gated on `is_full_group() == True` (True for every class representative above). The
`isometry_signature(verified=True)` tier is **Sage-gated in this install — TOOL-BLOCKED for
that tier only** (named, not silently downgraded); the decisive index-8 separation does not
rest on it (exact sub-cover census above), and unverified signatures are used solely as a
concurring cross-check of the partition.

## 5. Honest scope (C-guardrail)

Index ≤ 8 is a **computational horizon, not a theorem**. The class "all irregular covers"
stays formally open beyond it. The index-8 correction sharpens what any future statement must
say: the canonical multiset lives at the **isometry-class** level (H₁-multiplicity collapse
was a low-index accident, dead as a general mechanism at index 8). The other named residual
classes (CS/η beyond CS=0, `SL(n≥3)` gluing invariants, extended-Bloch/`K₃` torsion) are
other probes' work, not this one's.

## The fence

`probe.py` (runnable, ~1 s, budget-logged with the 90-min cap and the BUDGET-CAPPED branch,
exit 0) → `b500_census.json` (controls, per-index censuses/rows/partitions, sub-censuses,
signatures, symmetry data, budget log, verdict); lock
`tests/test_b500_irregular_covers_78.py` (SnapPy behind importorskip; fast: B350 SNF/Lucas at
7–8, B349 control census, the index-7 headline census + collapse, the cyclic cross-check at
7–8, the banked index-8 headline + verdict/doc integrity; the full index-8 partition
recompute with signatures and symmetry groups behind `pytest.mark.slow`). Reused: **B349**
(machinery + control), **B350** (exact SNF/Lucas ladder), **B330** (mechanism), **B348**
(sign-kill pattern), **B323** (commensurator level), **B495** (house style, sibling seal).
Lit: standard low-index subgroup enumeration (SnapPy `low_index` + SnapPea kernel);
canonical retriangulations (Culler–Dunfield–Goerner–Weeks).

**Nothing to `CLAIMS.md`; firewall untouched.**
