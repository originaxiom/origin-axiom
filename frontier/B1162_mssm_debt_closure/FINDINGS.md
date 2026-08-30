# B1162 — The MSSM-debt closure (cloud D1–D5) + the height-308 witness verified on-bench: the object forces a complete SM *structure*, walls SUSY, withholds the values

**Status: banked (frontier). Verdict OPEN** — a comprehensive closure/harvest arc that (a) **finishes WF-3**
by verifying codex's MSSM witness on our own bench (Sage; no longer single-homed) and (b) integrates cloud's
five-debt closure (memos 71–75), each cross-checked against our banked chain. Every load-bearing piece is
own-verified or corroborated by a banked main result; the two cloud cells needing cloud's stack are cited
with the alignment audit's zero-contradictions. `verification/reproduce.sh` → `REPRODUCES`. No firewall
crossing; Gate 5 clean. Cloud + codex credited. Lock `tests/test_b1162_mssm_debt_closure.py`.

## The witness, finished (WF-3's second half)

B1159 built the condition ledger but *relayed* the witness (single-homed off-branch). Now the witness is
**verified on our bench**: codex's height-308 SU(5) bundle cert re-run in Sage (`verification/witness_sage.txt`):
- **H0(Y,V) = 0** (exact global augmented-kernel dimension = 6) — no unwanted global sections;
- the **Φ-induced C372→C312 rank gate = 312, surjective over ℚ(ζ₁₂), H1(K1\*)=0**;
- **char-0 local freeness certified**; all three chart-orbit ideals = unit [1].
Honest fences intact (codex's own): **minimality heuristic only, stability unproved**. The witness's own
top line independently states B1161's result — *"every rational trace/norm map has Galois-stable kernel; a
marked H-valued tensor could evade it"* — i.e. the free-orbit no-go + the W₀ escape. The witness is now
**dual-homed** (codex off-branch + main-Sage-verified); the D1 provenance debt is discharged for the bundle
cert (codex R017 pays the rest).

## Cloud's five-debt closure (memos 71–75), cross-checked

| debt | cloud memo | result | our cross-check |
|---|---|---|---|
| **D1** alignment audit | 75 | B1159's ledger aligns with the bench — **zero contradictions**; the anomaly discriminant re-derived as **−18(u−2)(u+4)** | **own-verified IDENTICAL** to our B1160/B1161 −18(t−3)(t+3) (u=t−1) — `reproduce.sh` |
| **D2** hypercharge | 70 | forced to the SM direction | = **B1160** (own-verified) |
| **D3** breaking chain | 72 | the SM chain is **unique** — exactly **2 of 27** are (color-singlet, weak-singlet, Y=0): the lepton block's two neutral states (ν^c-like + S-like); standard E₆ double-breaking is the *only* SM-preserving chain | consistent with standard E₆ GUT (the 27's two SM-singlets); cloud cert (cloud stack, cited) |
| **D4** family index | 74 | **one 27 = ONE generation** — the trinification ℤ/3 (36 automorphisms, T³=1) rotates quark→lepton→antiquark *within* a generation; three-ness lives only in E₈'s (3,27) | **confirms B1161** generation-index NULL (own-verified: trace field degree 2 → never 3) |
| **D5** SUSY | 71 | **SUSY NO-GO** — the carrier admits no supercharge: (A) π₁-equivariant Q none (locked/unlocked sectors 6·spin1⊕6·spin0 vs 15·spin½ disjoint); (B) gauge-equivariant Q none (the 27's commutant is scalars); (C) the beat β²=meridian but β is even + semilinear, not a supercharge. Contradicts no observation (superpartners unobserved) | cloud cert (cloud stack, cited); consistent with the carrier structure B1147–B1150 |

Plus **memo 73** closes the C4 residual arc: the per-factor GUE deviation survives θ-exact *and*
local-empirical unfolding unchanged (D_ζ=0.0416, D_L=0.0502) — **not surmise error (memo 68), not unfolding
error, but intrinsic finite-height statistics** at T=3000, the known O(1/log T) class. This **confirms
B1158's** scoping (unfolding was the sole suspect; now shown exhausted → finite-height, generic).

## The synthesis — structure forced, dynamics & values withheld, proven across five debts

With the debt executed 5/5, the honest verdict reaches its sharpest form. The object **forces a remarkably
complete SM *structure***: the E₆ spine, the carrier/lock/clock, the **unique maximal Yukawa** (memo 52),
the **no-bare-mass theorem** (SEAM-Y), **hypercharge content** (D2, dual-homed B1160/B1161), the **unique
SM-preserving breaking chain** (D3), **exactly one generation** (D4). And it **walls the dynamics/values**:
**SUSY is a no-go** (D5), the **up-Yukawa is zero** (SEAM-Y), the **values are provably free** (the value
wall), the **heterotic framework is imported** (OA-C1002) and its selection needs the **missing archimedean
W₀** (B1161; the W₀ attempt is live). This is the program's one verdict — *structure forced, dynamics and
values withheld* — now instantiated across the whole visible sector, not a single crossing.

## What is bank-grade vs cited

- **BANK-GRADE (own-verified this bench):** the witness cohomology (Sage: H0(Y,V)=0, the rank gate, local
  freeness — `witness_sage.txt`); the D1 alignment discriminant (= our B1160/B1161); D4 = our B1161
  generation-NULL; D2 = our B1160.
- **CITED (cloud's stack single-homed, provenance debt, corroborated by alignment):** D3 (the 2-door
  breaking chain) and D5 (the SUSY no-go) — cloud's `breaking_chains.py` / `susy_test.py` assert GREEN but
  need cloud's deeper stack (a `check_charge_bracket`), so cited, not re-run; consistent with standard E₆
  GUT + the carrier structure + memo 75's zero-contradictions alignment. Cloud flagged one in-run
  preregistration error in D3 (the ψ-charges came out {1,−2}, filed) — honest.

## Fences

No firewall crossing — the object forces STRUCTURE (reps, charges, breaking chain, generation count,
anomaly-derived ratios per B950), never a measured VALUE; SUSY is a NEGATIVE (no-go), the values stay
withheld, the heterotic/W₀ observer bits stay open. Gate 5 clean. The witness minimality/stability are
codex's own open fences (heuristic/unproved), carried. Cloud/codex primary stacks single-homed where noted.

## Routes

- **B1159 debt-map:** the debts are now EXECUTED 5/5 (D1 aligns, D2 forced, D3 unique-chain, D4 one-gen, D5
  SUSY no-go) — the ledger closes; the residual observer bits are exactly link A (heterotic/W₀) + the values.
- **W₀ (live):** the one remaining structural obstruction; the W₀ construction workflow is running.
- **SUSY no-go (D5):** a new NEGATIVE — routes to the kill-graph reasoning (no supercharge on the carrier).
- **cc3 B8143:** independent corroboration of B1160 (D2), queued for a light fold-in.
