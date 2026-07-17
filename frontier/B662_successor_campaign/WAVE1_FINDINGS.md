# B662 WAVE 1 — FIVE CELLS ADJUDICATED (main seat, 2026-07-17;
# prereg 41f8d5ec; five parallel agents; every decisive fact
# spot-verified by this seat before banking)

## CELL A — L101 RESOLVED: (i₁, i₂) = (1, 3) IS METALLIC-UNIFORM (PROVEN)

The proof (cellA/PROOF_NOTE.md): i₂ = 3 from two lemmas — the
centralizer of a noncentral parabolic forces any commuting partner
into ±(I + tN) with the SAME fixed line (noncentrality, not
commutation alone, is what forces sharing — the flagged subtlety,
handled); Symᵏ of a nontrivial unipotent is a single Jordan block ⇒
exactly one fixed line per block, signs die on even k. i₁ = 1 proved
twice: an elementary two-parabolic route needing no algebraic-group
theory, and the Zariski-density route made rigorous (density from
tr[X,Y] ≠ 2 + a noncentral parabolic via the closed-subgroup
trichotomy). Uniformity: monodromy RᵐLᵐ has trace m²+2 > 2; the only
cited input is hyperbolization (faithful holonomy, parabolic cusp).
Verified 30/30 exact on BOTH banked objects (fig-8 over ℚ(√−3);
silver over L) — including the van Kampen [LONG, a] = 1 certificate
replay and the exact common fixed vector of the silver peripheral
pair. **CONSEQUENCE: the dimension grammar (3/5/1) upgrades to
THEOREM for the whole metallic family** (the reduction B656/G5 +
this uniformity; per-block face B657/W0b).

## CELL B — Q-BLOCK ANSWERED: (h⁰, h¹) = (0, 6) on the adjoint 78 —
## the reduction confirmed on a THIRD module

(The agent built the apparatus; the main seat completed the run.)
The adjoint letters Ad(ρ(a)), Ad(ρ(b)) on the 78-dim algebra (exact
over ℚ(√−3); gates: Ad(g)Ad(g⁻¹) = I, peripheral commutation at 78):
**i₁ = 0, i₂ = 6** (as the blocks [23,17,15,11,9,3] with no Sym⁰
predict), and the Fox computation gives **(h⁰, h¹) = (0, 6)** — with
ONE-PER-BLOCK reproducing on every adjoint block (each (h⁰,h¹) =
(0,1), all six exponents m = 1,4,5,7,8,11) and per-block sums equal
to the full-78 run. B654's Q-BLOCK conjecture (h¹(M;78) = 6, h⁰ = 0)
is CONFIRMED; the (i₁,i₂) reduction and the one-per-block refinement
now hold on THREE modules (27, 27̄ implicitly, 78) — the dimension
grammar mechanism is module-general, exactly as the reduction says.

## CELL C — L103 REPAIRED: sigma_matrix_golden.json persisted

The golden σ*-matrix on the banked five-class basis (the SAME basis
as every banked Y table): lower-triangular, diagonal
(ζ₆, ζ̄₆, −ζ₆, −ζ̄₆, 1); matches B638's in-flight printout on all 25
entries — a pure persistence gap, not a computation gap. Laws
verified: σ*² = id mod B¹ (5/5); conj(M)·M = I = M·conj(M) — and
this seat re-verified conj(M)·M = I INDEPENDENTLY from the persisted
JSON alone. Cross-check vs B660/S4's evaluator done at the invariant
level (the S4 in-repo re-run is blocked on a seat-local cache — the
sealed json was used): both sides agree on the basis-free invariant
(generic rank-4 orbit; B∧B ≠ 0). NEW HINT ROWS (registered, unjudged):
S4's v₀-mediated tensor W has support exactly {034, 124, 134} and
**W[034]/W[134] = 24ζ₆ exactly — the same 24ζ₆, same slot labels as
the banked golden spectator identity — and W[134] = conj(Y[134])
exactly** (H130).

## CELL D — THE σ*-EQUIVARIANCE THEOREM: the chord data is defined
## over k(Γ) (PROVEN for the two banked objects)

The silver content: Gal(L/ℚ(i)) = Klein four {1, s↦−s, s↦4i/s, στ};
each element acts on the banked letters by sign-character-twisted
conjugation with EXACT 1-dim intertwiner spaces (P1); the weld is a
descent datum (P2, λ = (−1,+1,−1)); ONE lift conjugates all 12
double letters (P3, 36 exact 27×27 identities); the cubic is
derivation-invariant (P4); and decisively (P5): the banked H¹ basis
is itself a ℚ(i)-form — each Galois twist fixes all five
representatives at COCYCLE level (15/15, G = I₅), so no class-descent
lemma was needed. Assembly: Y and C are Galois-fixed ⇒ ∈ ℚ(i) = k(Γ),
FORCED, not observed; Y[023]'s nonzero imaginary part generates —
the chord field is EXACTLY k(Γ). fig-8 is the degenerate case
(trace field = k(Γ), Neumann–Reid per B659). This seat's independent
spot-check: the checkerboard s-parity of the banked 2×2 letters
(a, c odd-diagonal/even-off; b reversed) confirmed from
entries_L.json. Scope honesty: theorem for the two banked objects;
the two non-automatic steps for the general member are named (weld
compatibility; exact-fixed-basis-or-descent). **THE SUBFIELD LAW
UPGRADES TO THEOREM (two objects; general mechanism identified).**

## CELL E — L102 RESOLVED: BLOCK-DIAGONAL — sector-respecting
## proposes FORCED

The canonical boundary-restriction decomposition (defined
object-uniformly; the golden control REPRODUCES the banked
block-diagonality — the construction is sound): **the silver portal
IS block-diagonal in the canonical basis** (P(B) = B* on both
objects; boundary dims 2/2; gauge-exhibited block-diagonal exact).
B657's upper-triangular mismatch was basis choice, exactly as the
banked caveat suspected. The portal law's SECTOR-RESPECTING property
now stands on two objects in a canonical construction —
FORCED-candidate (third object = the remaining test).

## Ledger deltas (this wave)

LAW_MAP: dimension grammar → THEOREM (metallic family); subfield law
→ THEOREM (two objects); portal law row updated (sector-respecting
canonical, two objects); OPEN_LEADS: L101, L102, L103 RESOLVED;
HINT_LEDGER H130. Locks: tests/test_b662_wave1.py.
