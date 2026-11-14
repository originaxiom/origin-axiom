# W-F3: a cone point on the torus fibre (orders 2 to 6) kills every gap of a character except the invariant-vector term, and every record sector module; the gaps the frame reads need the puncture. With a relay of the agy-exp lane's points for main

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free). This note closes card W-F3
(`relays/cards/CHAT1_W-F3_the_cone_point_loophole.md`, 99e416f0f). The question was the agy-exp lane's, relayed by the
author.

**How it was checked.** Computed once, on this seat's own code; expectations committed first.
- **The sealed run.** The script (sha256 `d1c77bf6…5b91f9be`) was run once. Two of its three expectations were met.
- **Post hoc 1.** It was committed before its run and met both of its expectations.
- **The method.** Exact ranks over one prime field, 9,646,561, prime to every k used. The helpers are W-C8 part 2a's,
  taken by text.

## 1. The question, and which k

The open choice left by W-F1 and W-F2 is the puncture against a cone point. A cone point closes the fibre, so the
3-dimensional object closes too. The lane asked: is h¹(V) = h¹(V*) then forced for every finite order?
- **The twist.** This seat read the question with the orientation character: h¹(V) against h¹(V* ⊗ w). The untwisted
  form was not tested on the odd levels.
- **Which k.** This card's k is the cone order **on the torus fibre** (λᵏ = 1, λ = [a, b]). W-F1's A4 and W-F2's row use
  the order K on the sphere S²(2,2,2,K). Since λ is conjugate to (abc)⁻², the computed k = 2 to 6 are the sphere's orders
  K = 4, 6, 8, 10 and 12.
  - W-F1's flat K = 2 is the closed torus, λ = 1.
  - Odd sphere orders (K = 3, 5, …) have no torus double cover. **They are not computed here.**

## 2. The results

The setting: the tick's levels n = 2 to 6, fibre cone orders k = 2 to 6 against k = ∞, every character (t-value any 2e-th
root of unity), and the extensions of one fibre-torsion character (χ(μ) = 1) by another with ℓ non-trivial on the fibre
(W-C8 part 2a's family).

| line | result |
|---|---|
| K1 | for k = 2 to 6, no class of H¹(G; ℓ) is non-zero on λ. In fact no non-coboundary class appeared for any fibre-torsion ℓ. **The record's sector modules (B1438's u(λ) = 1) cannot be formed.** On the orientable levels 4 and 6 even the non-split modules are gone: 0 at every computed k, against 12 and 210 at k = ∞ |
| K2 (sealed) | **Not met as written.** At k = 2 to 6, on the odd levels 3 and 5, two characters keep a non-zero gap. The sealed derivation had the invariant-vector term but set it to zero, while K2 was stated for every character |
| K3 | at k = ∞ some module has a non-zero gap on every level from 3 to 6: 8, 8, 22 and 72 modules |
| Q1 (post hoc 1) | for k = 2 to 6, every level from 3 to 6 and every character: gap = h⁰(V) − h⁰(V* ⊗ w). This is duality on the closed orbifold, with p prime to k, and Euler characteristic 0 |
| Q2 (post hoc 1) | **the two characters are exactly the trivial character (gap +1) and w (gap −1), on the odd levels only.** On the even levels no character has a gap at k = 2 to 6 |

**So the lane's question, read with w, comes out yes on everything computed, with one correction.** For fibre cone
orders 2 to 6:
- **Characters:** only the invariant-vector term h⁰(V) − h⁰(V* ⊗ w) remains. That term is non-zero only for the trivial
  character and w, and only on non-orientable levels. Higher-dimensional modules with invariants can carry it too: for
  example [[1, c], [0, 1]] with c(t) = 1.
- **Sector modules:** every gap they carry needs the puncture.
- **All finite orders:** "every finite k" follows from k·c(λ) = 0 and from duality. It is not computed beyond k = 6.

**For the table of opposites (W-F2 § 3).** The puncture against cone points was a choice. Now, for the fibre orders
computed (sphere orders 4 to 12):
- If a chiral count in the frame's sense is required, these cone points are dead and the puncture is strengthened, on
  that condition. "A chiral count" means a gap read by a sector module, or a character's gap beyond the invariant-vector
  term.
- Without the requirement, they stay a choice.
- The odd sphere orders are not computed.

## 3. What the wall teaches

On a cone point the longitude has finite order. For every coefficient character, on which λ acts trivially, a cocycle
then vanishes on λ (k·c(λ) = 0). This is the same mechanism as the Klein-bottle cusp in W-C8 part 2a, where λ ~ λ⁻¹. A
record sector module, which needs c(λ) ≠ 0, needs a longitude of infinite order that no symmetry sends to its inverse:
an orientable puncture.

## 4. Not computed

- Fibre orders above 6, levels above 6, and the odd sphere orders.
- Modules of dimension above two.
- The Selberg step. The cone relation is imposed on the group; the closed manifold cover is not built.

## 5. The agy-exp lane's points for main, relayed at the author's word (not checked by this seat)

- **The lane asks main to check two things before P-845 runs.**
  - Weighting words of length n by length gives the letter-count measure (by Furstenberg's law of large numbers), not
    hyperbolic area. Hyperbolic area needs primitive closed geodesics ordered by hyperbolic length ℓ ≤ T, with the
    parabolic classes L^{5k} and R^{5k} excluded.
  - Whether the frame is integrable at all four cusps of X₁(5).
- **The lane asks main to approve SM-C8**, with the SM seat's three amendments, **and SM-C9.**
- **The lane asks main to take B1825 off the SM seat's plate.** B1825 uses measured data, which that seat's firewall
  blocks, and the seat is idle waiting on main.

## 6. Files

`relays/chat1_2026-11-14_wf3/`: `wf3_checks.py` (sealed), `SCRIPT_SHA256.txt`, `wf3_checks_out.txt`,
`wf3_checks_err.txt` (empty), `wf3_posthoc_1.py` and its output.

This note was read by one session before it was pushed, and its corrections are applied.

0 of 19.
