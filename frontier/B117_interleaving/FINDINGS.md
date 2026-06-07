# B117 — The tower is the Sym two-sequence; the "promotion" is a Sym¹ absence

**Status:** the headline reframing of the B111–B116 run. The (n²−1)-dim trivial-point tower is **one object** — the
Sym plethysm two-sequence (B103/B58) — not two separable halves (a "sign half" + a "power half"). The B111/B113
"promotion" framing is **superseded**. Verify-don't-trust: every claim below is re-derived in `probe.py` and locked
in `tests/test_b117_interleaving.py`. No physics; nothing to `CLAIMS.md`; P1–P16 untouched.

## The two decompositions interleave

The tower carries two gradings that cut across each other:

- **HEIGHT / θ-split (B112):** θ=−w₀ acts on the (n−h) height-h roots of A_{n−1} by the reversal i↦(n−h+1)−i;
  its (±1)-eigenspaces give the (char(Mʰ), char(−Mʰ)) split. *Exact only n≤5* (B116: diverges at n=6).
- **SYM (B103/B58):** the tower = ⨁_d Sym^d(M)^{μ_d}. Each Sym^d contributes eigenvalues (−1)ʲφ^{d−2j} at
  **multiple** heights |d−2j|. **This is the actual tower** (matches the resolved SL(5), B61+B62).

The tower factorization is their intersection; the SYM side is primary.

## The dimension identity DERIVES the two-sequence's shape (3a)

    (n+1)(n+2)/2 − (n²−1) = −(n−4)(n+1)/2      (roots {−1, 4})

The full module set {Sym⁰…Sym^n} has dim (n+1)(n+2)/2; the tower has dim n²−1. The difference vanishes **iff n=4**
— the unique perfect fit. n<4 is a **surplus** (must omit modules), n>4 a **deficit** (must double modules). This
*derives* B103's `two_sequence_mult` μ_d = [2≤d≤n] + [0≤d≤n−3]:

| n | surplus | μ_d | doubled |
|---|---------|-----|---------|
| 3 | 2 | {0,2,3} | — (Sym¹ omitted) |
| 4 | 0 | {0,1,2,3,4} | — (perfect) |
| 5 | −3 | {0,1,2²,3,4,5} | Sym² |
| 6 | −7 | {0,1,2²,3²,4,5,6} | Sym²,Sym³ |
| 7 | −12 | {0,1,2²,3²,4²,5,6,7} | Sym²,Sym³,Sym⁴ |

The n≥6 doubling is exactly the two-sequence overlap [2≤d≤n−3]. **The "n≥6 doubling is open" worry is resolved.**

## The "promotion" is a Sym¹ ABSENCE (3b — supersedes B111/B113)

At n=3 the unique subset of {0,1,2,3} with Σ(d+1)=8 is **{0,2,3}** (enumerated all 16 subsets). Sym¹ is simply
**absent** — forced by the surplus. The char(−M) at height 1 comes from **Sym³'s** height-1 contribution
((−1)¹φ^{3−2·1} = −φ), *not* a "promoted Sym¹". At n=4 all modules are present; nothing is promoted. So the
height-1 behaviour is a **selection** (which Sym^d appear), never a promotion.

## degree=rank = Sym^n presence (6 — honors the DO-NOT)

μ_n = 1 for **all** n≥2 (the [2≤d≤n] arm always includes d=n), so **char(Mⁿ) is always a tower factor** — which is
degree=rank (Mⁿ=L) at the characteristic-polynomial level. **Status precision (do NOT claim "by dimension"):**

- **n=3:** dim-forced (the unique subset {0,2,3} contains 3).
- **n=2,4:** rep-theory (B33/V18, B103), **NOT** a dimension necessity (at n=4, {0..3} sums to 10, fillable by
  multiplicities in principle — Sym⁴'s presence is not forced by dim alone).
- **n≥5:** the two-sequence form (B103).

**Verification:** Sym⁰..⁴ char-poly product = the B80 *proved* n=4 tower (degree 15, all roots match, `3c`).

## Path 4 — the n=6 cross-check (consistency, not decisive)

The two-sequence predicts the n=6 bulk: char(Mʰ) mult {1:2, 2:3, 3:2, 4:1, 5:1, 6:1}, char(−Mʰ) {1:2, 2:1, 3:1,
4:1}; the |k|=3 total = a₃+b₃ = 2+1 = **3** (= max(n−d,1), the V17 correction). B66 (26/35, gauge-corrupted)
measured 2 — the known under-count (B58 Phase A). n=6 is gauge-corrupted, so this is a consistency check, not a
decisive test; the doubled modules Sym²,Sym³ are the overlap [2≤d≤n−3].

## The reframe + the re-aimed prize

The tower = the Sym two-sequence (**one object**); "promotion"/"two-halves" is superseded; degree=rank's char(Mⁿ)
= Sym^n presence. **The prize is to prove the two-sequence μ_d for all n** (B103's standing open problem — the
realization/trace-ring wall), not to "close two separate halves."

**Ledger:** V104. **Reuses:** `B103.two_sequence_mult` / `B103._Jm_n4_exact`, `B58.sym_counts`.
