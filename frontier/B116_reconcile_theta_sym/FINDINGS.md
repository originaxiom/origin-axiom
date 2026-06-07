# B116 — reconcile the θ-split (B112) with the Sym two-sequence (B103): they diverge at n=6

**Status: `computer-assisted` + a CORRECTION to B112 (explicit downgrade).** The reconciliation B112 ↔ B103, run
to *join* the two halves of the `ρ_n` prize. What it found instead is a **verify-don't-trust correction** to
B112's all-`n` claim — banked visibly, like the V90/V91 downgrades. NO physics; no `CLAIMS.md`; the `ρ_n` proof
stays the prize; P1–P16 untouched. Script `probe.py`; test `tests/test_b116_reconcile_theta_sym.py`.

## The two decompositions of the `(n²−1)`-dim trivial-point tower
- **θ-split (B62/B112):** the opposition involution `−w₀` on the `A_{n−1}` root spaces. **B112 proved** its
  eigenspace combinatorics are `⌈(n−h)/2⌉` / `⌊(n−h)/2⌋` for all `n`.
- **Sym two-sequence (B103/B58, V27 membership rule):** the tower `= ⊕_d Sym^d(M)^{μ_d}`,
  `μ_d=[2≤d≤n]+[0≤d≤n−3]`. **B103 proved** this is the exact module-iso at `n=3,4`.

## Findings
1. **The Sym two-sequence = the actual tower.** `sym_counts(5)` = `{char(M^h): 1→2, 2→2, 3→1, 4→1, 5→1;
   char(−M^h): 1→1, 2→1, 3→1}` **exactly matches** the resolved SL(5) tower (B61 22/24 + B62's 2). It includes
   `char(M⁵)` (the degree=rank top power) **automatically** — it is `Sym⁵`'s top weight, so **no separate
   "promotion" is needed** on the Sym side.
2. **θ-split = the tower only for `n ≤ 5`.** Through `n=5`, the Sym two-sequence equals the θ-split **plus a
   single degree=rank promotion** (they agree on heights `2..n−1`, differ by one at height 1, plus Sym's
   `char(Mⁿ)`). **At `n ≥ 6` they DIVERGE** — exactly the banked **V26/V27** result:

   | `n=6` mode | Sym (= tower-candidate) | θ-split (B112) |
   |---|---|---|
   | `a₁` (`char M`) | 2 | **3** |
   | `a₂` (`char M²`) | 3 | **2** |
   | `b₂` (`char −M²`) | 1 | **2** |
   | `a₃` (`char M³`) | 2 | 2 (agree) |

   They still **agree** on the contested `a₃(n=6)=2` (a second independent vote, V27).

## The correction to B112 (explicit downgrade — verify-don't-trust)
B112 proves the θ-split **combinatorics** (the `⌈/⌊` eigenspace dimensions) for all `n` — a genuine `A_{n−1}`
root-system theorem, and it **stands**. But the **identification** of the θ-split with the **tower's**
`char(±M^h)` multiplicities — the long-standing **V25** unproven step — holds only for `n ≤ 5` (verified against
the exact `n≤4` tower and the SL(5) data) and is **contested at `n ≥ 6`** (the θ-split ↔ Sym divergence). So:

> **B112's "the sign half of `ρ_n` proved for all `n`" is corrected to "the θ-split combinatorics proved for all
> `n`; = the tower's sign structure for `n ≤ 5`; the all-`n` sign half is OPEN."**

The all-`n` sign half is blocked by the same θ-split-vs-Sym divergence that needs the **ambient SL(n) trace
ring** (the perennial wall). The **Sym two-sequence is the better tower-candidate** — it equals the actual tower
wherever the tower is known (`n≤4` proved, `n=5` resolved) and supplies `char(Mⁿ)` automatically — so **proving
the Sym two-sequence for all `n`** (B103's open problem) is the live route to the catalog, *not* the θ-split.

## Verdict
The reconciliation did not join the halves — it revealed that the θ-split (B112) and the Sym two-sequence (B103)
are **different decompositions that agree only through `n=5`** (V26/V27). The Sym two-sequence is the actual
tower; B112's all-`n` claim is downgraded to `n≤5`; the live route to the full catalog is the **Sym two-sequence
proof** (B103), with the `Mᵏ`-scalar arithmetic (B111) for the exponent. The honest gain: the prize is re-aimed
at the *right* object (the Sym two-sequence), and a real overclaim was caught before it propagated.

```bash
python frontier/B116_reconcile_theta_sym/probe.py
python -m pytest tests/test_b116_reconcile_theta_sym.py -q
```
No physics claim; the `ρ_n` catalog proof stays the central target; proven core P1–P16 untouched.
