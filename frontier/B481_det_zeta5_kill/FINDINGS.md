# B481 — is det(T) = ζ₅? Exact verdict: NO (float artifact) — the eighth kill, both readings closed

**Question (owner, 2026-07-08): is det(T) = ζ₅ exact (surviving in ℚ(ζ₆₀)) or floating-point?
If exact, a theorem about the critical point; if float, the eighth kill.** Adjudicated in
exact arithmetic under both plausible readings of "T."

## Reading 1 — T = a Weil operator at the critical point (level 15). NOT ζ₅.
Exact F_p (p ≡ 1 mod 60; cross-checked p = 61, 421, 541, 1201), determinants as exact
powers of ζ₆₀:

| operator | exact det |
|---|---|
| W₁, W₂, W₁W₂, [W₁,W₂] | **1** |
| Par, Par·W₁, Par·W₂, Par·W₁W₂ | **−1** |
| D (twist) | ζ₃ |
| F (DFT) | ζ₄³ = −i |
| W_R | ζ₃² |
| D@5, F@5, W₁@5 (mod-5 sub-operators) | 1, −1, 1 |

**Structural theorem (the opposite of the claim):** det restricted to ⟨W₁, W₂, Par, D, F⟩
lands in ⟨ζ₃, ζ₄, −1⟩ = the **12th roots of unity**. Since 5 ∤ 12, ζ₅ is NOT in the image
of the determinant homomorphism — no operator built from the critical pair can have
det = ζ₅, at any level. Not "not found" — forbidden.

## Reading 2 — T = the WRT modular T-matrix. Also NOT ζ₅ (but ζ₅ IS an eigenvalue).
SU(2)_k T-matrix, T_a = exp(2πi(h_a − c/24)), exact rational phases:

| k (r=k+2) | det T (with c/24) | det T (θ_a only) |
|---|---|---|
| 3 (golden, r=5) | **1** | ζ₁₀³ |
| 13 (r=15) | ζ₆ | ζ₆₀^41 |

No SU(2)_k det is a primitive 5th root. **BUT ζ₅ is exact in the T-matrix as an
EIGENVALUE, not the determinant:** at k=3 the spin-1 anyon (a=2) has h₂ = 2/5, so its
twist θ₂ = exp(2πi·2/5) = ζ₅². That is the likely source of the claim — ζ₅ genuinely lives
in the golden modular data as the twist of the middle anyon; it is real and exact. It is
just not det(T). (The θ_a-only det ζ₁₀³ = exp(2πi·108°) is also near-but-not ζ₅ = 72°.)

## Verdict
**det(T) = ζ₅ is FLOAT — the eighth kill.** Exact arithmetic gives, for every reasonable T:
determinants in ⟨ζ₁₂⟩ (Weil) or {1, ζ₆, ζ₁₀³} (WRT), never a primitive fifth root. What IS
exact and does survive: ζ₃ = det(D) (the twist's cube-root, the banked residue ω), −1 =
det(Par), and ζ₅² = θ₂ as a WRT twist eigenvalue. The critical-point determinant carries
2-, 3-, 4-torsion — never 5. Reproducers: `det_kill.py` (F_p, four primes),
`wrt_tmatrix.py` (exact rational phases). Firewall: pure arithmetic.
