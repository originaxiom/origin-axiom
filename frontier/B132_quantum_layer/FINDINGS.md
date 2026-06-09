# B132 — The quantum layer: SU(2)_k eigenvalue field content, the quantum selection criteria, the Lee–Yang bridge (V121; CORRECTED by B133/V122)

> **⚠ CORRECTION (B133/V122).** The original B132 headline — *"chirality shifts the eigenvalue arithmetic
> (achiral → ℚ(√−3), chiral → ℚ(ζ₁₂))"* — is **WITHDRAWN as a sampling artifact**. The eigenvalue *orders* are correct;
> their *attribution to chirality* is wrong. The field content is **quantum-group arithmetic** (word spin-content mod 4,
> the SU(2)_k T-twist), present in **achiral words too**. The decisive control: at k=4, **achiral words alone span all
> three fields** (`RRLL`→ℚ(ζ₁₂), `RRRLLL`→ℚ(√−3), `RLRLRL`→ℚ), and the k=4 vanishing is also not chirality-linked
> (achiral `RRLRLL`,`RLRRLL` vanish). So **S7 (chirality-arithmetic) and S5 (chiral fragility) are withdrawn**; what
> stands is the m-mod-4 mechanism + the single-seed m=1 criteria + Lee–Yang. Tombstone `K-H`; guard `MB6`
> ("reproduction ≠ interpretation — run the control"). See the corrected `knowledge/K015`.

Internalizes a cross-session "Chat-1" handoff (10 results), **re-derived in-sandbox** (verify-don't-trust). The handoff
was built on a **stale snapshot** (pre-B130/B131); its numbering and one "open" item collide with merged work
(reconciled below). The genuinely new content is a whole **quantum layer** on top of the classical character-variety
results (B127–B131): the SU(2)_k Witten–Reshetikhin–Turaev data `Z_k` of the metallic once-punctured-torus bundles.

**One-line result (corrected).** The SU(2)_k eigenvalue **field content is quantum-group arithmetic** — the word's
spin-content mod 4 (the T-matrix twist `exp(·πi/4)`), present in achiral and chiral words alike, **not** a chirality or
manifold property; the classical trace fields stay disjoint (ℚ(√−3)∩ℚ(i)=ℚ). The robust **single-seed** facts: the
figure-eight (m=1) is the unique perfectly coherent seed (`|Z_k|=1` at every level; `Z_{k=4}=ω`), the vanishing period
is `|O_K^×|/2` for arithmetic m, and there are exactly two scales by m mod 4. The native physics is the **Lee–Yang
edge** (the σ₃ Galois conjugate, `d_τ=−1/φ`), not the Standard Model. MATH and physics in different tiers. Nothing to
`CLAIMS.md`; P1–P16, the functorial `Sym(W)→trace-ring` wall (B85), S031, and the merged B124–B131 untouched.

## Reconciliation (the handoff was stale)

- **B130** (no-forced-choice) and **B131** (two-seed fork) are **already merged** (PR #146/#147). The handoff's "KEY"
  open item — **Step 17, the two-seed internal fork** — *is* B131: gluing distinct seeds creates a discrete fork,
  heterogeneity makes the choice, the (1,2) fork is `κ∈{−4,−2}`. **This quantum field-fusion is its companion at the
  quantum level**: the same composition phenomenon seen as a *classical character-variety fork* (B131) and a *quantum
  eigenvalue-field fusion* (here).
- Renumbered: this batch = **B132 / K015,K016 / P009 / V121** (the handoff's B131–134, K013–15 names collided).

## The validated SU(2)_k convention (exact, precision-independent)

`S` = modular S-matrix; `T` = diag `exp(2πi·a(a+2)/(4(k+2)))` (**no c/24 framing**); Dehn twists `R=T`, `L=S T S⁻¹`;
the monodromy of an R/L word = the ordered product. At level `k` the rep has dim `k+1` and all eigenvalues are roots
of unity; an eigenvalue of **order d** generates `ℚ(ζ_d)` — order 6 or 3 → ℚ(√−3), order 4 → ℚ(i), order 12 → ℚ(ζ₁₂).
This reproduces the handoff's eigenvalue orders **exactly** (the eigenvalue-order method, §8 of the handoff).

## Verified results

- **S1c — eigenvalue field-fusion (single seeds m=1..7 at k=4).** m=1 `{6,6,6,2,2}` pure ℚ(√−3); m=2 `{6,4,4,2,2}`
  **fused ℚ(ζ₁₂)**; `m ≡ 2 mod 4` carries the order-4 (ℚ(i)) content (m=2,6 fuse); all others ℚ(√−3). The ℚ(i)
  content is quantum-group arithmetic (SU(2)₄, the T-phase `exp(mπi/4)` at spins j=1,3), controlled by `m mod 8`.
- **S7 — [WITHDRAWN by B133] the field content is quantum-group, not chirality (compositions at k=4).** The original
  reading ("achiral→ℚ(√−3), chiral→ℚ(ζ₁₂)+vanish") is a **sampling artifact**. The decisive control (all words below
  are achiral by `is_amphicheiral`):
  | word (achiral) | field | `|Z|` |
  |---|---|---|
  | `RRLL` | **ℚ(ζ₁₂)** | 1.880 |
  | `RRRLLL` | ℚ(√−3) | 2 |
  | `RLRLRL` | ℚ (rational) | 5 |
  | `RRLRLL`, `RLRRLL` | ℚ(ζ₁₂) | **0 (vanish)** |
  **Achiral words alone span all three fields** — so the field tracks **word spin-content mod 4** (the SU(2)_k T-twist),
  not chirality, not the manifold. The classical trace fields stay disjoint (ℚ(√−3)∩ℚ(i)=ℚ). Tombstone `K-H`; guard
  `MB6`. *(The B128 chirality recursion and B131 fork are classical and stand — they are not refined by this; the
  earlier "quantum companion" framing is withdrawn.)*
- **S1a — the self-referential loop.** `Z_{k=4}(M_1) = e^{2πi/3} = ω`, the generator of the trace field ℚ(√−3): the
  partition function at the saturation level *outputs the trace-field generator*. m=1-specific.
- **S3a — pure phase is m=1-unique.** `|Z_k|=1` at every non-vanishing `k` only for m=1 — the strongest m=1 selection
  criterion (the figure-eight's quantum theory is perfectly coherent at every level).
- **S2 — vanishing period = `|O_K^×|/2` for arithmetic m.** `Z_k` vanishes periodically iff the trace field is
  imaginary-quadratic-with-the-right-units: m=1 (ℚ(√−3)) period **3** = 6/2; m=2 (ℚ(i)) period **2** = 4/2;
  non-arithmetic m=3,4 are **aperiodic** (distinct gap sets). The vanishing is controlled by the unit group of the
  trace field's ring of integers.
- **S4 — exactly two quantum scales, by m mod 4.** First non-vanishing level `k=1` (`ℏ=2π/3`) for `m ≢ 2 mod 4`, and
  `k=2` (`ℏ=π/2`) for `m ≡ 2 mod 4`. The non-cancellation principle admits **two** allowed scales; the selection is
  seed-level (external).
- **S5 — [WITHDRAWN by B133] vanishing is word-composition, not chirality.** The earlier "chiral fragility /
  non-cancellation selects the symmetric vacuum" reading is withdrawn: **achiral** words `RRLRLL`, `RLRRLL` also vanish
  at k=4, and the (1,2,3)-vs-(1,2,1) difference was confounded with word length (no control was run). The vanishing
  levels are a per-word partition-function fact, not a chirality marker. *(The single-seed `|Z|=1` m=1-coherence, S3a,
  is unaffected and stands.)*
- **S6 — commensurability (SnapPy).** silver (RRLL, 1-cusp, CS=0, achiral) and L5a1 (2-cusp, CS=−0.125, **chiral**)
  share volume 3.6639 but are not isometric — same commensurability class; the 2-cusped member broke the achiral
  symmetry. (S5c: chiral compositions' torsion — (1,2,3) `ℤ/157⊕ℤ`, balanced-chiral RRLRRLLL `ℤ/2⊕ℤ/14⊕ℤ`.)
- **S8 — the Lee–Yang bridge (S030 upgraded).** At k=3 (N=5) the σ₃ Galois conjugate `q→q³` sends the quantum
  dimension `d_τ = +φ` (Fibonacci, unitary) to `−1/φ` (Lee–Yang M(2,5), non-unitary). The framework's native physics
  is the Lee–Yang edge singularity (non-equilibrium criticality, experimentally observed; Peng et al. 2015) — **not**
  the Standard Model, but real observed physics.

## Quarantined (did NOT reproduce — verify-don't-trust)

- **S9 — "RRL κ-degree = 3 refutes 'κ-degree=1 ⟺ arithmetic'": NOT reproduced.** B126's geometric-component method
  (eliminate x,y, degree of κ over ℚ(z)) gives RRL κ-degree **1 or 2** (composition-order dependent), never **3**, and
  the claimed cubic `4κ³+κ²−16κ−4` does not appear. **Not banked.** (A degree of 1 would be *consistent* with the
  criterion, not a refutation.) Recorded so the κ-degree-criterion claim is not propagated unverified.

## The Monadic Closure synthesis (S10 → `philosophy/P009`, firewalled, NOT a theorem)

The handoff proposes one "Monadic Closure Theorem" unifying all seven firewall directions. Banked as a **scoped
synthesis** (`P009`), POSTULATED, with the scrutiny the handoff requested: the "seven closures" are **not
independent** — they reduce to ~**3 root causes**: (i) *one trace field* (single monodromy) → arithmetic sealing (B129)
+ fork-free moduli (B130) + the quantum coherence Q1/Q2/Q3 (this batch); (ii) *det=−1* → amphichiral → CS=0 (B127);
(iii) *one cusp* → rank-1 abelian `T[M]` (B129, where covers reach rank 2). So "monadicity" is an evocative repackaging
of three structural facts, not seven independent theorems. Recorded as motivation, not a proven theorem.

## Reproduce

```
python frontier/B132_quantum_layer/probe.py
python -m pytest tests/test_b132_quantum_layer.py -q
```

All checks use the validated SU(2)_k rep (numpy only; the eigenvalue-order method is exact and precision-independent),
so they run unconditionally. (S6/S5c SnapPy facts are recorded; rerun with SnapPy to recompute.)

**Tier.** MATH (quantum topology / WRT invariants) + a firewalled physics reading (POSTULATED). Naming `knowledge/K015`
(chirality-arithmetic field-fusion) + `K016` (the consolidated m=1 selection criteria); `philosophy/P009` (Monadic
Closure synthesis); `speculations/S030` upgraded (Lee–Yang computed). Nothing to `CLAIMS.md`; P1–P16, B85, S031,
B124–B131 untouched. Ledger **V121**.

**Anchors:** B131 (`K014`, the classical fork — this is its quantum companion), B128 (`K011`, the chirality recursion —
this is its quantum refinement), B127/B125 (`K010`/`K009`, CS=0 + arithmetic), B129/B130 (`K012`/`K013`, sealing +
fork-free), B126 (the κ-degree method), S030 (Yang–Lee fork — now TESTED-POSITIVE). External: SU(2)_k modular data;
Sütő/Damanik–Gorodetski; Peng et al. 2015 (Lee–Yang).
