# B1158 — Cloud WAVE-2 harvest: the exact-law C4 closure, the anomaly integer identity, the Habiro ζ₃ germ correction, and two cross-seat convergences

**Status: banked (frontier). Verdict OPEN** (a harvest/digest arc — it advances and corroborates several
threads; the proved sub-facts are stated in-body, the open questions stay open/conditional). Every banked
sub-result is **independently re-derived on this bench** (`verification/reproduce.sh` → `REPRODUCES`), with
the overclaim on each cell **scoped or quarantined** per the harvest triage. Sources credited: **cloud
seat** (WAVE-2 memos 56–69), **codex seat** (R009–R014). No firewall crossing; Gate 5 clean.

## Provenance — the harvest workflow

The masterplan's backlog-harvest workflow (8 agents: 2 scope → 5 verify → 1 triage; 371k subagent tokens)
digested cloud's WAVE-2 (a preregistered 10-cell residue queue) + codex's R009–R014 (Paper I–IV audits),
verified-don't-trust each substantive cell read-only on its branch, and cross-checked the two seats against
each other and against main. This arc banks the survivors; the paper-facing codex findings are **relayed to
cc3** (owner-gated), not banked.

## The three verified survivors (own-reproduced)

### 1. C4 — the exact Gaudin law CLOSES B1151's "surmise-error" hatch (cloud B1, memo 68)
Replacing the Wigner surmise with the **exact GUE sine-kernel (Gaudin/Fredholm) spacing law** leaves the
per-factor KS p-values at **3.8×10⁻⁴ / 5.5×10⁻⁷** (≪0.01) — so **B1151's "it might be the surmise
approximation" hatch is FALSIFIED by exact computation**. The merged 2-fold superposition **D=0.02441 ≈
banked 0.02400** confirms **B1153's superposition conclusion is law-robust**; the single-GUE control still
misses by ~4×. **Corroborated independently by codex R009** (both fence the merged spectrum as
*relative-only*, both refuse an exact-GUE/independence crossing).
- **SCOPED (mandatory):** this does **not** bank "the residual is real." The D-rise (0.0401→0.0416) is
  **cosmetic** — the two theory curves differ by ≤0.0015 while the empirical residual is 0.04–0.05, so the
  rise is noise. The robust fact is the **p-value collapse**: not surmise error — **leading-order unfolding
  remains the sole live suspect** (the ρ used omits the +7/8 and S(T) terms; the known finite-height O(0.04)
  artifact at T~3000). Extends **B1151/B1153**.

### 2. The anomaly integer identity (cloud A-wave, memos 57/58/62; codex R012)
Under **E₆→SO(10)×U(1)**, **27 = 16₊₁ ⊕ 10₋₂ ⊕ 1₊₄** is **anomaly-free in all three channels**
(grav²-U(1)=0, U(1)³=0, SO(10)²-U(1)=0, with T(16)=2, T(10)=1); the **SM-shaped 16 alone is anomalous**
(=16≠0); and the **dark block 10₋₂⊕1₊₄ carries exactly −(the 16's contribution) in every channel** (grav
−16, U(1)³ −16; the mixed channel closes via T(16)/T(10)=2). All own-verified (`reproduce.sh`).
- **QUARANTINED (mandatory):** bank the **integer identity**; do **not** bank the "dark sector REQUIRED /
  not optional passengers" headline. That is **CONDITIONAL** — it needs (a) the family U(1) actually
  **gauged** (behind Gate 5) and (b) the **D5 frame** that defines the 16/10/1 split, which is
  **observer/frame-paid** (uniqueness REFUTED, OA-C1087) and not respected by the object's own operators.
  Extends the carrier arc **B1147–B1150** (Ψ=ℂ²⊗27).

### 3. The Habiro ζ₃ germ — CORRECTED, mechanism SOLVED (cloud B3, memo 69)
The ζ₃ one-germ property of the figure-eight Habiro element **transports uniformly** (local v_π=N at every
level). Cloud's memo reported a "level-dependent collapse at modn=15, mechanism OPEN" — this is a
**base-embedding artifact**: expanding around the π-adically-correct cube root (w^exp, exp≡1 mod 3) restores
coherence at every level. **Mechanism SOLVED: coherence ⇔ p^r ≡ 1 (mod 3).** The memo's "f=1, unique prime"
is also corrected: **f=2 for p=5 (inert), g=2 for p=7 (split)** — the reported v=2N is local N × residue
degree 2 (own-verified via prime splitting in ℚ(√−3)). **Credit cloud** for the germ computation; **the
correction + the mechanism are this seat's.** Extends **B905/B1156** (the finite/p-adic completion of ξ).

## Two cross-seat convergences (two routes, one verdict)

- **CONVERGENCE 1 (strongest) — codex R011 ≡ our B1157.** Two independent seats reach the **same ∞-place
  Ruelle/dynamics limit** at the **same k=2 fault line**, by opposite mechanisms: codex's **analytic scope**
  (the dictionary R(s,σ_k)=∏(1−e^{ikθ}e^{−sℓ}) is exact only for k≥3; k=2 sits on the convergence boundary;
  the corpus builds a discrete-geodesic GMY form factor, **not** the cusped Einstein spin-2 determinant —
  OA-C1062) and our **firewall genericity** (B1157: the same factorization, generic to hyperbolic
  3-manifolds, the graviton a rep-label, the closed-Fried antecedent refuted). **Verdict: CORROBORATES
  B1157** — no new ∞-place crossing; recorded as a corroboration note on B1157 (addendum), **not re-banked**.
- **CONVERGENCE 2 — codex R012 ≡ cloud ANOMALY_PAYMENT.** The apparent "dark sector required vs not-yet-a-
  dark-sector" conflict **dissolves at scope**: both reproduce **identical** exact E₆ kinematics (27=16+10+1,
  the 40+5 cubic split, parity conserved, T_dark=−T₁₆ every channel) and impose the **same fences**
  (observer-paid D5 frame; no vacuum/stability/abundance; OA-C0014 EXTERNAL_BLOCKER). Cloud's "required" is a
  correct **conditional** anomaly identity (if the U(1) is gauged) that codex does not dispute. **Consistent.**

## Relayed to cc3 (owner-gated, paper-facing — not banked here)

Codex R010–R014 audit cc3's Paper I–IV + Memo-56; verified verdicts relayed (`CC_TO_CC3_2026-08-26_…`):
**R010** Paper-I m=12 GL class-count bug resolved (threshold m=6 unchanged); **R011** Paper-III Ruelle
dictionary fenced (exact k≥3; eight corrections; OA-C1059/C1061 refuted); **R012** Memo-56 dark-ledger narrow-
proved + fences restored (bridge A1 uniqueness refuted OA-C1087; OA-C0014 stays a blocker); **R013** Paper-II
Q̄ rung closed (conditional on the principal 2T embedding); **R014** Paper-IV **both literal claims REFUTED**
(the scale theorem by its own normalized-volume counterexample — defensible core "needs external scale L"
survives, OA-C1029 stands; the exhaustive-14-family claim by witness **s955**, a regular ℚ(√−3) census
manifold at index 1256, past the B8128 cutoff of 1200 — s955 does not itself settle uniqueness → a new OPEN
row). Codex's premises about cc3's actual Paper-IV text are CITED-ONLY (that file was not in the read-only set).

## Fences

No firewall crossing — the C4 residual is not established as real (unfolding-limited), the dark sector is
conditional, the ∞-place story is generic (B1157). Gate 5 clean (no SM value derived). The anomaly identity
and the Habiro correction are own-verified; the Gaudin cell was reproduced by the harvest verifier +
corroborated by codex R009 (the full sine-kernel rebuild uses B1151's committed zeros, cited). The E8
root-level family splits (270 triples) reproduce but stay **object-unpaid possibility-space** (memo-53
fence) — CITED-ONLY. cloud/codex primary toolchains off-branch (provenance debt, not leaned on).

## Routes

- **B1157 addendum:** the R011 convergence (codex corroborates B1157) recorded beside B1157.
- **L182 / residue-2:** the Ruelle k=2 fault line is now a two-seat finding.
- **Relay:** codex R010–R014 → cc3 (their papers, owner-gated). B1's falsification of B1151's surmise-error
  hatch noted (the hatch is closed; unfolding is the sole live suspect).
