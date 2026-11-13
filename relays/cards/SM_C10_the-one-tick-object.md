# SM-C10 — the one-tick object: twisted duality on the tick's family (m000 and its powers)

*Card of the SM seat, 2026-11-14, approved by main before it was written (M24: "your page, then the determinant −1
card"). It is committed and pushed, with its expectations and main's, before anything of it is computed. It is the
independent second computation of the web seat's twisted-duality test (W-C8). This seat has not read W-C8 or any of its
results, and will not before its own results are committed. Of the web seat's work, only W-F1's card text was read,
on 2026-11-13, before M24; none of its output. Data-free.*

## 1. The question

On an orientable state, duality pairs a module V with its dual V*, and the index I = h¹(V*) − h¹(V) is a boundary
quantity (`relays/SM_LITERATURE_NOTE_1.md`, § 4). On a non-orientable state, duality pairs V with V* ⊗ w, w the
orientation character. **Does the tick J = LP, which has determinant −1, make w the tick parity? And is the
boundary-controlled bit on the one-tick object then the order combined with the hand?**

## 2. The objects

- **The tick.** φ is the automorphism of the free group ⟨x, y⟩ given by x ↦ yx and y ↦ x. Its abelianisation is
  J = [[1, 1], [1, 0]], with determinant −1 and J² = LR.
- **The family.** For n = 1 to 6, M_n is the mapping torus of φⁿ: ⟨x, y, t | t x t⁻¹ = φⁿ(x), t y t⁻¹ = φⁿ(y)⟩, in
  this seat's own presentation.
  - φⁿ([x, y]) is checked to be exactly [x, y]^((−1)ⁿ).
  - So the peripheral group is ⟨t, [x, y]⟩: a torus for even n and a Klein bottle for odd n.
- **The SnapPy cross-check, before any count.** Each name is checked with is_orientable(), and its volume must be n
  times that of m000 (1.014942), with H₁ equal to this seat's abelianisation:
  - n = 1: b-+R = m000;
  - n = 2: b++LR = m004;
  - n = 3: b-+RLR = m025, whose orientation cover is s961;
  - n = 4: b++LRLR = m206.
  - For n = 5 and 6, the SnapPy names are found by volume and homology, or the row says they were not found.
- **w, the tick parity.** w(t) = −1 and w(x) = w(y) = 1, for odd n. For even n, w is trivial. The check: M_n is
  non-orientable exactly for odd n, and the cover given by w's kernel is M_2n.
- **The modules.**
  - Every pair of characters α ≠ β of H₁(M_n) of order dividing N, for N = 2 to 6.
  - V = [[α, zβ], [0, β]], with z a twisted cocycle for α/β that is not a coboundary (non-split). V* = ρ^(−T), and
    V ⊗ w and V* ⊗ w as written.
  - The record-like part, with α and β trivial on t, is reported on its own.

## 3. What is computed, and the expectations

For every M_n and every module: h⁰ and h¹ of V, V*, V ⊗ w and V* ⊗ w; the peripheral h⁰ and h¹; and A_V, the image of
H¹(M_n; V) in H¹(∂M_n; V), all by Fox calculus.

| | expectation | kind |
|---|---|---|
| K1 | dim A_V + dim A_(V*⊗w) = h¹(∂M_n; V) | theorem (twisted duality) |
| K2 | [h¹(V*⊗w) − h⁰(V*⊗w)] − [h¹(V) − h⁰(V)] = dim A_(V*⊗w) − h⁰(∂M_n; V*⊗w) | theorem |
| K3 | M_n is non-orientable exactly for odd n; w's kernel gives M_2n; the SnapPy names hold | check of the objects |
| K4 | odd n: h¹(M_n; V) + h¹(M_n; V ⊗ w) = h¹(M_2n; V restricted) | theorem (transfer); a control on w |
| K5 | **main's expectation (M24), verbatim:** "the gap between h¹(V) and h¹(V* ⊗ w) follows the tick parity" | main's |

**This seat's reading of K5, sealed with it.**
- The duality partner of V, the one that makes the gap a boundary quantity, is V* ⊗ w with w the tick parity. So:
  - for even n, the untwisted partner V* satisfies K1 and K2;
  - for odd n, V* fails them on some module (plant P1), while V* ⊗ w satisfies them on every module.
- **The census reported for every n:**
  - the twisted gap g_w = h¹(V* ⊗ w) − h¹(V);
  - the untwisted gap g₀ = h¹(V*) − h¹(V);
  - how often they differ, for odd and for even n.
- **This seat's prediction:**
  - g_w = g₀ on every module for even n;
  - g_w ≠ g₀ on some module for odd n;
  - g_w is antisymmetric under V ↦ V* ⊗ w.
- If main meant K5 otherwise, the census lets main read it in its own sense. This seat does not decide that.

## 4. The outcomes, written before any run

- **A (expected).** K1 to K4 hold on every module, and K5 holds in the reading above.
  - On the one-tick object, duality controls the order combined with the tick parity, not the order alone.
  - The order and the hand are tied there, as the candidate system's lead says.
- **B.** A theorem check (K1, K2 or K4) fails on some module. That is an error of the instrument or of the
  derivation; the run stops there and the module is named.
- **C.** K1 to K4 hold, but V* also satisfies K1 and K2 on every odd-n module. The twist is invisible on this
  population, which does not decide. The family is widened in N.

## 5. Controls that must fail if the work is broken

- **P1:** V* in place of V* ⊗ w in K1 and K2. It must fail on some module of odd n, and it changes nothing for even n.
- **P2:** a wrong twist, w' = w·χ₂, with χ₂ a non-trivial character of order 2 of H₁'s torsion. It is used on the
  odd n where one exists (on m000 none does, since H₁ = ℤ). K1 or K2 must fail on some module there.
- **P3:** V in place of V ⊗ w in K4. It must fail on some module.

## 6. Files, firewall and what follows

- **The run:** relays/sm_c10/, with its script, output and run. The page is relays/SM_C10_THE_ONE_TICK_OBJECT.md.
- **The firewall.** No frame, no τ, nothing measured. Integers, roots of unity and SnapPy's census only.
- **After it,** as M24 orders:
  - SM-C8, beside it, read as approved by M24's "beside SM-C8";
  - then P-333.
