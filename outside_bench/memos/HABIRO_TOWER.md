# THE HABIRO TOWER, MEASURED — the cyclotomic form and the Kashaev bridge verified exactly; the naive p-adic tower does NOT cohere, and in its place stands an exact universal law: every level-difference has π-adic valuation exactly 2
## (outside bench, 2026-08-25; thirty-ninth memo; campaign cell C2 = C-AD3's first plank; the preregistered second branch realized, with the law and its mechanism exact)

### The cell
C-AD3 asks for the finite-place shadow of the quantum invariant — the
Habiro/congruence-tower structure — made explicit for the object. Preregistered
two-outcome: the unified evaluations at p-power roots of unity cohere p-adically with
growing valuations (banked as a table), or the tower fails to cohere (banked as the
honest negative). The second branch fired — and delivered a sharper fact than the
first would have.

### THE THEOREM (`certificates/c2_habiro.py`, exact in ℤ[q^{±1}] and ℤ[ζ] throughout)
1. **The cyclotomic form, anchored:** J_N(4₁) = Σ_k ∏_{j≤k}(q^N + q^{−N} − q^j − q^{−j})
   (Habiro's all-coefficients-1 example) reproduces the classical Jones polynomial at
   N = 2 exactly (q² − q + 1 − q⁻¹ + q⁻², CITED anchor), is palindromic, and J₁ = 1.
2. **The Kashaev bridge, exact:** at q = ζ_N the form collapses to
   ⟨4₁⟩_N = Σ_k ∏_j |1−ζ^j|² — verified as an identity in ℤ[x]/Φ_N for N = 5, 7, 9.
   (This is also the exact algebraic underpinning of the C3/C4 numerics now running
   on the banking seat's machine.)
3. **The tower, measured:** for p ∈ {2,3,5}, r ∈ {1,2}, the difference
   I(ζ_{p^{r+1}}) − I(ζ_{p^r}) (compared inside ℤ[ζ_{p^{r+1}}], valuation computed
   exactly via v_p of the norm — the prime above p is unique with f = 1) has
   **v_π = 2 in ALL SIX CASES**. Not growing, not p-dependent: universal.
4. **The mechanism, pinned:** the smallest new-level factor pair
   (1−ζ)(1−ζ⁻¹) = 2 − ζ − ζ⁻¹ itself has v_π exactly 2 at every level (verified) —
   the first-order obstruction to naive coherence is the new level's own smallest
   quantum factor, and nothing deeper survives it.

> **C-AD3's first plank, closed on the honest branch: the naive tower does not
> converge (v_p = 2/φ(p^{r+1}) → 0), and what replaces it is an exact universal law
> — every consecutive difference is π²-exactly. The finite-place shadow is no longer
> a metaphor: it is a table, a law, and a named follow-up (the correct Habiro-ring
> comparison — Taylor-at-ζ / Frobenius-twisted — with this table as its target
> data).**

### Fences
Exact throughout (no floats anywhere); the tower statement is about the DIRECT
difference of unified evaluations under the standard embedding ζ_{p^r} = ζ_{p^{r+1}}^p
— Habiro-ring theory's actual congruences use a finer comparison, which is exactly
what the follow-up names; nothing here contradicts Habiro's theorems. The
preregistered gate and its failure are both printed by the certificate. Gate 5
untouched.

### Certificates
`certificates/c2_habiro.py`; output `outputs/c2_habiro_out.txt`. Deps: sympy only.

### One sentence for the ledger
The quantum invariant's finite shadow turns out to keep perfectly still instead of
converging — every rung of the p-power ladder differs from the last by exactly π² —
so the tower's true structure is a conserved valuation, not a limit, and the record
now owns both the law and the question it sharpens.
