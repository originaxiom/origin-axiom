# Cold Read of `B1936` (`M24`) — Exterior Parity of `Lambda*(C^5)` vs Frame C's Global Higgs Bit

- **Seat:** `agy-exp`
- **Card / Message:** `M24` cold read of `B1936` (*"Matter sits in the even half of `Lambda*(C^5)`, and parity consistency would fix the Higgs world as the record's practice"*), read at `origin/main` `d1d2f9073` after `X-EXACT-W` was sealed and pushed (`48926341b`, `1cdd9eefb`), with expectations committed first (`2a67770de`).
- **Empirical firewall:** `0 of 19.`

---

## 1. Verdict in Plain Terms

`B1936`'s Part `1` and its conditional deduction in Part `2` are **algebraically exact** and accomplish something non-trivial: they **eliminate the hypercharge-sign convention (`+6Y` vs `-6Y`)** by locking each sector's Higgs requirement directly to matter's own mod-`5` charge half. However, **inside Frame C, `B1936`'s premise does assume a one-bit boson–fermion grading rule equivalent to what it concludes**: requiring the holomorphic Higgs boson `S` to share spinor matter's `Lambda*(C^5)` degree parity (`kh mod 2 == mp`) yields `W_- = (up S~, down S, lepton S)` for both signs of `6Y`, whereas requiring the holomorphic Higgs boson `S` to carry the **fundamental vector / Clifford operator parity** (`kh mod 2 != mp`, the standard `(-1)^F = (-1)^{deg}` super-grading on `Lambda*(C^5)`) yields `W_+ = (up S, down S~, lepton S~)` for both signs of `6Y`. Thus `X-SCAR` and `B1936` are completely consistent: Frame C still carries `1` genuine bit until Frame D (`W-B1`) or dynamical selection (`X-SURVIVAL` `S4`) settles which grading holds.

---

## 2. What Holds Unconditionally (and Slightly Stronger Than `B1936` States)

1. **Canonical Chiral Partition of `(Z / 5Z)^x` Without Choosing the Multiplier `2`:**
   In the all-left-handed chiral Weyl presentation, one generation's five non-singlet multiplets have integer `6Y` charges `(+1, -4, +2, -3, +6)`, which reduce modulo `5` to just two residues:
   - `1 mod 5` on the `SU(5)` ten-plet (`+1, -4, +6`), and
   - `2 mod 5` on the `SU(5)` five-bar (`+2, -3`).
   Hence `(Z / 5Z)^x = M union (-M) = {1, 2} union {3, 4}` canonically splits the four non-zero mod-`5` charges into matter's chiral half `M` and its conjugate `-M`, with `6Y -> -6Y` simply exchanging `M <-> -M`.

2. **Uniqueness of the Exterior-Degree Multipliers `m in {2, 3}`:**
   Testing all four group automorphisms `phi_m(y) = (m * y) mod 5 in {1, 2, 3, 4}` for `m in (Z / 5Z)^x = {1, 2, 3, 4}`:
   - `m = 1` maps `M = {1, 2}` to `{1, 2}` (mixed parity: odd and even);
   - `m = 4` maps `M = {1, 2}` to `{4, 3}` (mixed parity: even and odd);
   - **`m = 2` maps `M` to `{2, 4}` (all even) and `m = 3` maps `M` to `{3, 1}` (all odd).**
   Thus `B1936` does not even need to pick the factor `2` in `k = 2 * (6Y) mod 5` by hand: demanding that one chiral Weyl generation occupy a single parity class of `{1, 2, 3, 4}` uniquely selects `m in {2, 3}`.

3. **Convention-Free Relative Sector Lock:**
   For any trilinear chiral coupling `y_a + y_b + y_H = 0 mod 5`:
   - `down` and `lepton` combine `1 + 2 = 3 mod 5`, requiring `y_H = -3 = 2 mod 5 in M` (**always inside matter's own half `M`**);
   - `up` combines `1 + 1 = 2 mod 5`, requiring `y_H = -2 = 3 mod 5 in -M` (**always inside the conjugate half `-M`**).
   Flipping `6Y -> -6Y` sends `M` to `{4, 3}`, `y_H(down, lepton)` to `3 in M`, and `y_H(up)` to `2 in -M`. The relative placement (`down, lepton in M`; `up in -M`) is completely independent of the hypercharge sign convention.

---

## 3. Where the Premise Repackages Frame C's One Bit (Three Structural Points)

1. **Spinor Grading (`==`) vs Boson–Fermion Super-Grading (`!=`) on `Lambda*(C^5)`:**
   In `Spin(10) > SU(5)`, chiral matter is a **Weyl spinor** (`16_+ = Lambda^{even}(C^5)`), whereas the complexified Higgs (`5 (+) 5-bar = Lambda^1(C^5) (+) Lambda^4(C^5)`) is a **vector boson** that couples to two spinors via Clifford action `e_i ^ (.) + iota_i(.)` — an operator of **odd** exterior degree (`+- 1`)! As holomorphic representations of `SU(5)` on `C^5`, **both** `Lambda^1(C^5)` (odd degree `1`) and `Lambda^4(C^5)` (even degree `4`) are holomorphic exterior powers; only the single-doublet reality tie `Phi_{up} = Phi_{down}~` forces one to be `S` and its conjugate to be `S~`.
   - **Rule `Pi_+` (`B1936`'s premise, `kh mod 2 == mp`):** Holomorphic bosons share the exterior parity of holomorphic spinor fermions (`S` goes to `Lambda^4` when matter is `Lambda^{even}`) `=>` **`W_- = (up S~, down S, lepton S)`** for both signs of `6Y`.
   - **Rule `Pi_-` (Super-graded / fundamental-vector premise, `kh mod 2 != mp`):** Under the canonical `Z_2` super-grading `(-1)^F = (-1)^{deg}` on `Lambda*(C^5)`, spinor fermions occupy `Lambda^{even}(C^5)` while the fundamental holomorphic vector boson `C^5 = Lambda^1(C^5)` has odd degree `1` (`S` goes to `Lambda^1` when matter is `Lambda^{even}`, and to `Lambda^4` when matter is `Lambda^{odd}`) `=>` **`W_+ = (up S, down S~, lepton S~)`** for both signs of `6Y`.
   Because Frame C never twists the Higgs by `y_H`, nothing in Frame C prefers `Pi_+` over `Pi_-`; postulating `Pi_+` carries the exact `1` free bit identified by `X-SCAR`.

2. **Weyl Basis in `B1936` vs Dirac Kernel in Frame C (`B1656`):**
   `B1936` §2 writes *"Matter's kernels are holomorphic and all in one class (§ 1)"*. That statement is true for the chiral Weyl list `(+1, -4, +2, -3, +6)`, whereas Frame C's actual `B1656` Dirac kernel `K_{q_L, q_R}` takes `(q_L, q_R) = (+1, +4), (+1, -2), (-3, -6)` with `q_L in M` (even degree) and `q_R = -Y_6(psi^c) in -M` (odd degree), while **both** theta factors `vartheta[(q_L + q_R)a/2]` and `vartheta[(q_L - q_R)a/2]` in `K_{q_L, q_R}` are holomorphic in `tau`. `B1936`'s parity statement should therefore explicitly say *"chiral left-handed Weyl multiplets"* rather than *"matter's kernels"* in Frame C.

3. **How the Bit Can Settle Without Assuming `Pi_+`:**
   `B1936` §2 rightly refrains from claiming `W_-` is settled in Frame C and points to Frame D (`W-B1`), where `y_H` twists the Higgs fiber directly. Independently, within Frame C's existing Hilbert space, integrating out the chiral fermions along allowed histories (`X-SURVIVAL` `S4`, modular-invariant Kähler Berezin log-determinant `sum_f d_f <ln det(Im tau * Y_f^dagger Y_f)>`) breaks `W_-` vs `W_+` dynamically in favor of `W_-` (`+230` SE on `P_5`, `+85` SE on `P_{15}`) with zero parity postulate.

`0 of 19.`
