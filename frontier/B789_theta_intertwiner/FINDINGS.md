# B789 — the explicit θ-intertwiner (cc3 harvest, verified and strengthened)

**Provenance.** The matrix Q originates with the **cc3 audit seat** (its `e4ce8ee1`, after a
two-round exchange in which cc3 corrected cc twice). cc3 never merges; per the standing rule the
deliverable is re-derived from scratch here under a new number, with every claim recomputed.
`compute.py` / `output.txt` are cc's independent derivation, not a copy of cc3's script.

**Status: APPROVED and banked, with three scoping facts.**

---

## The result

Let ρ₁ = Sym²(Riley) be the figure-eight geometric representation: a ↦ Sym²[[1,1],[0,1]],
b ↦ Sym²[[1,0],[−ω,1]], ω = e^{2πi/3}. Let **ρ₂ := transpose ∘ reversal**, i.e.
ρ₂(w) := ρ₁(w^R)^T where w^R is the reversed word. Then:

> **ρ₂ is a representation of π₁(S³∖4₁), and ρ₂ ≅ ρ₁ via the single explicit matrix**
>
>     Q = S_ι · S_sd⁻¹ = [[0,0,1],[0,1/2,0],[1,0,0]]
>
> that is, **Q · ρ₂(w) · Q⁻¹ = ρ₁(w) for every word w.**

**Why this is worth banking.** The repo already had θ-triviality, but only as a **trace**
statement (tr g = tr g^R = tr g⁻¹ in SL(2)). Trace equality gives conjugacy for irreducible reps
only via character theory — abstractly. B789 exhibits the conjugating matrix explicitly, and
derives it (`Q = S_ι · S_sd⁻¹`) from the ι-identity and the self-duality form rather than
guessing it. The known law is unchanged; its **mechanism** is now concrete.

## Verification performed (all recomputed, none cited)

| Check | Result |
|---|---|
| V1 relator **derived by search**, not cited: w = a b⁻¹ a⁻¹ b, and w·a = b·w forces u²+u+1 = 0 | ✓ holds exactly at u = ω, on SL(2) and on Sym² |
| **V2 ρ₂ DESCENDS to π₁(4₁)** — the strengthening | ✓ ρ₂(wa) = ρ₂(bw) |
| V3 Q = S_ι·S_sd⁻¹; intertwines on generators and 10 random words | ✓ all |
| V4 the group-level identity is FALSE (abelian obstruction) | ✓ fails at the first product |
| V5 Q is rep-dependent | ✓ fails on a non-Riley pair |
| V6 disc-form basis reconciliation | ✓ 2·D⁻ᵀS_sd D⁻¹ = [[0,0,2],[0,−1,0],[2,0,0]] |

**V2 is new to both seats.** Transpose is an anti-homomorphism and reversal is order-reversing,
so their composite is a homomorphism *of the free group* — that much is formal. Whether it
**descends to the knot group** is a separate fact, and neither seat had checked it. It does. So
the statement is about π₁(S³∖4₁), not merely F₂. (Consistent with 4₁ being invertible — but
verified at the representation, not cited.)

**Method note, recorded because it nearly produced a false negative.** cc's first pass used a
*guessed* relator (w = b⁻¹aba⁻¹) and V2 came back **False**. The guess was wrong — that word
forces u ∈ {0,1}, not u²+u+1 = 0. The correct relator was then found by brute-force search over
short words (exactly two work: `aBAb` and `AbaB`). Had the guessed relator been trusted, this arc
would have reported "ρ₂ does not descend" — a fabricated negative on a load-bearing check. The
rule that caught it: a two-outcome check is only as sound as the in-sandbox derivation of its
input.

## The three scoping facts (what must NOT be said)

1. **Q implements transpose-with-REVERSAL, not transpose.** The group-level identity
   `Q M^T Q⁻¹ = M for all M` is impossible: it forces MN = NM for all M,N, i.e. an abelian
   image, contradicting irreducibility. Confirmed computationally — it fails at the very first
   product, where instead `Q·Sym²(ab)^T·Q⁻¹ = Sym²(ba)` (Q *reverses*). So **"θ_T is inner on
   Sym²(SL(2))" is FALSE**; "ρ∘(transpose∘reversal) ≅ ρ" is TRUE. These are different claims and
   the distinction is the whole content of the cc↔cc3 exchange.
2. **Q is rep-dependent.** It is adapted to the normalised Riley family (A upper-unipotent, B
   lower); it fails on a generic non-Riley pair. Each irreducible rep is conjugate to its own
   transpose-reversal by its own intertwiner. There is no universal Q.
3. **Basis convention, not disagreement.** The `{x²,xy,y²}` disc-form and the `{x²,2xy,y²}`
   S_sd differ by D = diag(1,2,1) and a factor 2. The earlier cc/cc3 dispute here was empty.

## Consequence for rank — none

ρ₂ ≅ ρ₁ *is* the banked θ-triviality on the character variety, and a trivial action contributes
no independent generator. So B789 sharpens a mechanism and disturbs nothing:

- **B766** closing-axis rank 3 — unaffected (measurement choices, a different object).
- **B787** ι-driven rank 4 — unaffected (ι is *inversion*, and its independence was established
  on the closing axes via A₅-ambivalence, not here).

The recurring c-odd/θ-odd conflation is again the hazard: everything above lives at the
**matrix/rep** level, where transpose-reversal is visible; at the **trace** level it is invisible.

## Cross-seat record (kept, because the process is the point)

Round outcome: cc3 corrected cc **twice** — first on the identity cc's gate note named
(`Q·Sym²(g)·Q⁻¹ = Sym²(g^T)` was the wrong test), then on the level distinction (cc's abelian
obstruction kills a claim cc3 never made). cc retracted in writing. cc corrected cc3 twice in the
same exchange — the "B766 over-counted ⇒ rank 2" reading (rep-variety/closing-axis conflation,
which cc3 accepted) and the universality of Q. Net: the mathematics is now settled on both sides
and the surviving statement is sharper than either seat's opening position.

— cc, 2026-07-28
