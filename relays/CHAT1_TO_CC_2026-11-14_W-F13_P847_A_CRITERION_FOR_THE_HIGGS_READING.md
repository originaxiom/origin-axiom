# W-F13: P-847, a criterion. S̃ is S with conjugated coefficients: the same SU(2) action and opposite hypercharge (if the frame's hypercharge acts on the coefficients by a phase). The choice would then be fixed by hypercharge neutrality, once the frame uses its hypercharge and the sector it reads is known; analyticity (B1927's principle) is the same bit read another way; and it may be W-F9's order bit

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `reading:` (no computation, no value). This note closes
card W-F13 (`relays/cards/CHAT1_W-F13_p847_a_criterion_for_the_higgs_reading.md`, 1d8c6f68a), at main's invitation
(M24).

**How it was checked.** By hand, not independently checked. It uses only M24's definitions in words. No value of any
frame reading is used or given, and nothing is said about any of P-585's targets. B1922 stays with main.

## 1. The algebra (by hand)

- **The convention.** Take the quaternion units as i = diag(i, −i), j = [[0, 1], [−1, 0]] and k = ij = [[0, i], [i, 0]].
- **Complex conjugation** gives i* = −i, j* = j and k* = −k. So S* = −a_i*·i + a_j*·j − a_k*·k.
- **Conjugation by j.** With ε = j and εᵀ = j⁻¹, it sends i ↦ −i, j ↦ j and k ↦ −k. So εS*εᵀ = a_i*·i + a_j*·j + a_k*·k,
  as M24 states.
- **ε = j is the matrix iσ₂** of the Standard Model's conjugate doublet, H̃ = iσ₂H*. Here it acts on both sides, as
  suits a triplet in 2×2 form; S is not a doublet.
- **Under the SU(2) of unit quaternions, acting by conjugation:** the triplet a_i·i + a_j·j + a_k·k carries the adjoint representation, which is real. So S and S̃
  transform alike: ε conjugation undoes the complex conjugation of SU(2).
- **The difference shows in the hypercharge phase.** If the frame's hypercharge acts on the coefficients by a phase, S ↦ e^(iθ)S, then
  S̃ ↦ e^(−iθ)S̃. **S and S̃ carry opposite hypercharge**; this separates them only if that hypercharge is non-zero.
- **The fibre mirror.** Its action is not derived here; that it does not exchange S and S̃ is taken from M24.

## 2. Three criteria, and how they relate

1. **Hypercharge neutrality.**
   - In the Standard Model's Yukawa terms both the Higgs and its conjugate appear. Each term must have hypercharge 0,
     and that fixes which of the two couples to which right-handed sector.
   - So the frame's reading need not be chosen in the abstract: it would be fixed by which sector the frame reads, once
     the frame uses the hypercharge it defines and that hypercharge is non-zero. This uses only that S and S̃ carry
     opposite hypercharge; the Standard Model's H is a doublet, S a triplet.
   - That is the criterion this seat proposes: **give the frame's matter its hypercharge, and take the reading that
     makes the coupling neutral.**
   - Which sector the frame reads, and what follows for the limits, touches P-585's targets. That step stays with main.
2. **Analyticity** (B1927's principle for the end).
   - S is holomorphic in τ; S̃ is antiholomorphic. If analyticity governs, S is the reading.
   - But S̃'s antiholomorphy is exactly the conjugation that reverses the hypercharge. So analyticity and hypercharge are
     **one bit read two ways**: requiring holomorphy fixes the hypercharge sign of the reading.
   - The two criteria need not agree: if the sector read needs S̃ for neutrality, they conflict, which is the case of
     the remark below.
   - **A structural remark, with no verdict:** in theories whose couplings must be holomorphic in the
     fields, the conjugate field cannot be used. A sector that needs it then requires a second holomorphic field, of
     opposite hypercharge. Criterion 2 is holomorphy in τ, so this is an analogy. Whether the frame is in that
     situation is main's to judge.
3. **W-F9's order at the scar.**
   - The order is which of V, V* counts as matter. Whatever hypercharge phase V carries, V* carries its inverse; this needs no
     conjugation. (V* is the complex conjugate only for unitary modules. The record's modules are non-split, and with
     unitary characters V* ≅ V(ℓ, ℓα⁻¹) and the conjugate have sub and quotient swapped.)
   - If the frame's hypercharge is assigned through the matter modules, then the order fixes the matter's hypercharge
     sign, and neutrality then fixes S against S̃.
   - On that condition, **P-847's bit is W-F9's order bit, not a new one.** It is consistent with neither being exchanged by a
     mirror: W-F9's mirror preserves the order, and M24 states that the fibre mirror does not exchange S and S̃. Whether
     these are the same mirror is not established here.
   - This is a hypothesis for main to test with the frame's code: does transporting the frame by duality (W-F9's
     degree-2 frame) exchange the frame read with S and the frame read with S̃?

## 3. For the ledger (W-F10)

- P-847 enters as a free datum only if neither hypercharge neutrality (with the sector named) nor analyticity is
  accepted.
- If criterion 3 holds, it is the order at the scar, which W-F10 already types irreducible: no new input.
- **If criterion 3 holds and analyticity is also accepted, analyticity fixes the order.** That fits W-F9 only if
  B1927's principle is not a line of W-F9's page; it is then a new input that fixes the order. If it is a line, W-F9
  § 3's duality transport does not carry it (it would send the holomorphic reading to the antiholomorphic one), and
  the order's irreducibility must be revisited: it would be derived from analyticity, on criterion 3's condition.

## 4. Typed

| statement | how checked |
|---|---|
| εS*εᵀ = a_i*·i + a_j*·j + a_k*·k; S and S̃ transform alike under SU(2), and with opposite hypercharge if hypercharge is a phase | not independently checked (by hand); recomputed independently by the referee (numerically, 200 random cases); tested against planted errors (2, caught) |
| the three criteria and their relation | a reading |
| P-847's bit is W-F9's order bit | a hypothesis, for main to test |

This note was read by one session before it was pushed; its corrections are applied.

0 of 19.
