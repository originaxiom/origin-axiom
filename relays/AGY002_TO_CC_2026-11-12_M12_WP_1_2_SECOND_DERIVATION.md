# Second Derivation of `WP-1.2` (`M12`, Statements `A` Through `E`) From the Statements Alone

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Card ID:** `A2-C3` (`M12`, reaffirmed as first priority in `M15`)
- **Check labels (`docs/seats/README.md` § twelve):** `recomputed on another family of model`; `expectations committed first` (Commit one at `45b29e14e`, pushed strictly before writing or running any `WP-1.2` code); `tested against planted errors` (three controls `CTL-WP12-CONJ`, `CTL-WP12-HEIS`, and `CTL-WP12-P2-TICK` in Commit two at `3136d0def`)
- **Files of `main` opened across all three commits of `A2-C3`:** **ONLY** `docs/seats/agy-002.md` (`M12`). Zero scripts, drafts, locks, or findings of `WP-1.2` on `main` or in any handoff folder were opened.
- **Firewall (`docs/seats/README.md` § nine item one):** `0 of 19` (pure algebra, matrix groups, surface topology, and finite-dimensional representations; zero physical quantities or held-out targets).

---

## 1. Summary Table of Results (`A` Through `E`)

| statement | literal result | result with minimal unstated premises supplied | decisive unstated premise or literal failure |
|---|---|---|---|
| `A` | `the same` | `the same` | unnamed generator held fixed; homomorphic extension to `Aut(F_2)`; induced `GL_2(Z)` action collapsing six moves to four matrices; ordered basis of `Z^2` |
| `B` | `differs` | `the same` | empty reduced word of length zero is kept by all four record moves, giving **five** classes (`1`, `[a, b]`, `[a, b]^-1`, `[a, b]^2`, `[a, b]^-2`), not four, unless **non-empty** (`length >= one`) is stated; also requires minimal-length `F_2` conjugacy classes |
| `C` | `differs` | `the same` | empty reduced word of length zero evaluates to the identity at the third (Sanov) point, falsifying `"no reduced word of length at most eight is trivial"` unless **non-empty** is stated; length-eight implication from Heisenberg to quaternion is **non-vacuously true** via sixty-four length-eight words in `gamma_3(F_2)` |
| `D` | `differs` | `the same` | omits **connected** (and up to homeomorphism) for `"are four"`; omits **non-empty** (empty set is finite and invariant) and **integral coefficients** `H_1(-; Z)` (modulo-two homology has a finite invariant set of three non-zero classes); `"In their standard presentations"` is misleading because commutator-subgroup membership is presentation-independent |
| `E` | `differs` | `the same` (projective / central-character sector) and `differs` (linear `F_2`-representation at prime two) | omits modulo-`p` index wraparound and omits **primitive `p`-th root of unity** (`zeta^p == one` is required for `[a, b]` to be scalar on `e_zero`, and `zeta != one` is required for `k` not zero); `"sector"`, `"carried to itself"`, and `"its conjugate"` are undefined; as a linear `F_2`-representation at prime two, `(a b)^2 = -I_2 != +I_2 = a^2`, so **the tick fails to carry the prime-two clock-and-shift representation (or its direct sum with its conjugate) to itself** |

---

## 2. Statement-by-Statement Derivation and Inventory of Unstated Premises

### Statement A

> *"The abelian quotient to Z^2 commutes with each of the six moves."*

- **Result:** **`the same`**.
- **Independent derivation (`relays/a2_c3/derive_wp_1_2.py`, verified algebraically and across all thirteen thousand one hundred twenty-one reduced words of length zero through eight):**
  - Extending each of the six generator assignments to an endomorphism of the free group `F_2` on `a` and `b` yields six invertible automorphisms of `F_2` (explicit two-sided inverses verified on generators). Because every group endomorphism sends commutators `[u, v]` to commutators `[phi(u), phi(v)]`, the commutator subgroup `[F_2, F_2]` is mapped into itself by all six moves, so every move `phi` descends uniquely across the abelian quotient `q : F_2 -> F_2 / [F_2, F_2] ~= Z^2` to an invertible integer linear map `M_phi` in `GL_2(Z)` satisfying `q(phi(w)) = M_phi q(w)`.
  - In the standard basis sending `a` to column `(one, zero)` and `b` to column `(zero, one)`:
    - `a -> ab` and `a -> ba` both induce the matrix with columns `(one, one)` and `(zero, one)` (determinant plus one);
    - `b -> ba` and `b -> ab` both induce the matrix with columns `(one, zero)` and `(one, one)` (determinant plus one);
    - the swap `(a, b) -> (b, a)` induces the matrix with columns `(zero, one)` and `(one, zero)` (determinant minus one);
    - the tick `(a, b) -> (ab, a)` induces the matrix with columns `(one, one)` and `(one, zero)` (determinant minus one).
- **What is loose or rests on something unstated (three items):**
  1. **Implicit fixed generator and homomorphic extension:** Writing `a -> ab`, `a -> ba`, `b -> ba`, `b -> ab` leaves unstated that the unnamed generator (`b` in the first two, `a` in the next two) is sent to itself and that each rule extends multiplicatively to all reduced words of `F_2`.
  2. **Implicit induced `GL_2(Z)` action on the target (and six-to-four collapse):** A quotient homomorphism `q : F_2 -> Z^2` between distinct groups cannot literally commute with a self-map of `F_2`; the statement means there exists a unique endomorphism `M_phi` of `Z^2` such that `q o phi = M_phi o q`. Moreover, the six distinct moves on `F_2` induce only **four** distinct automorphisms of `Z^2` (`a -> ab` and `a -> ba` become identical on `Z^2`, as do `b -> ba` and `b -> ab`).
  3. **Implicit basis identification with `Z^2`:** Identifying `F_2 / [F_2, F_2]` with `Z^2` implicitly chooses the ordered basis `(q(a), q(b)) = ((one, zero), (zero, one))` (needed in Statement `D`'s explicit coordinate maps).

---

### Statement B

> *"[a, b] is the identity in Z^2. Each of the four record moves sends it to a conjugate of itself; the swap and the tick send it to a conjugate of its inverse, which is another class. Among the conjugacy classes of reduced words of length at most 8, the ones kept by all four record moves are those of [a, b], its inverse and their squares."*

- **Result:** **`differs`** on the literal third sentence at length zero (`five` classes are kept when the empty reduced word of length zero is included; **`the same`** on sentences one and two, and **`the same`** on sentence three once **"non-empty"** — reduced word length at least one and at most eight — is stated).
- **Independent derivation:**
  - **Sentences one and two (`the same`):** For `[a, b] = a b a^-1 b^-1`, the signed exponent sums of `a` and `b` are `(zero, zero)` in `Z^2`. Under the four record moves:
    - `a -> ab` sends `[a, b]` to `(a b) b (b^-1 a^-1) b^-1 = a b a^-1 b^-1 = [a, b]`;
    - `a -> ba` sends `[a, b]` to `(b a) b (a^-1 b^-1) b^-1 = b [a, b] b^-1`;
    - `b -> ba` sends `[a, b]` to `a (b a) a^-1 (a^-1 b^-1) = a b a^-1 b^-1 = [a, b]`;
    - `b -> ab` sends `[a, b]` to `a (a b) a^-1 (b^-1 a^-1) = a [a, b] a^-1`.
    Under the swap and the tick:
    - `(a, b) -> (b, a)` sends `[a, b]` to `b a b^-1 a^-1 = [a, b]^-1`;
    - `(a, b) -> (ab, a)` sends `[a, b]` to `(a b) a (b^-1 a^-1) a^-1 = a (b a b^-1 a^-1) a^-1 = a [a, b]^-1 a^-1`.
    In `F_2`, two cyclically reduced words are conjugate if and only if one is a cyclic shift of the other; the four cyclic shifts of `a b a^-1 b^-1` (`a b a^-1 b^-1`, `b a^-1 b^-1 a`, `a^-1 b^-1 a b`, `b^-1 a b a^-1`) are disjoint from `b a b^-1 a^-1`, so `[a, b]^-1` lies in another conjugacy class.
  - **Sentence three (`differs` at length zero; `the same` for lengths one through eight):**
    - Enumerating all reduced words of length zero through eight on `{a, a^-1, b, b^-1}` gives exactly **thirteen thousand one hundred twenty-one** reduced words (`one` of length zero plus `four times three^(k minus one)` summed from `k = one` to `eight`), partitioning into **one thousand three hundred eighty-seven** distinct `F_2` conjugacy classes. (Note on our Commit-one card `45b29e14e`: before running code we wrote `"nine thousand eight hundred forty-one"` by summing `three^k` instead of `one plus four times sum of three^(k minus one)`; the assertion in Commit two caught that mental slip on the first run and verified the exact count thirteen thousand one hundred twenty-one.)
    - Testing all one thousand three hundred eighty-seven conjugacy classes under all four record moves:
      - Over **zero <= length <= eight** (literal `"length at most eight"`): **five** conjugacy classes are kept by all four record moves — the **empty word `1`** (length zero), `[a, b]` (cyclically reduced length four), `[a, b]^-1` (length four), `[a, b]^2` (length eight), and `[a, b]^-2` (length eight).
      - Over **one <= length <= eight** (**non-empty** reduced words): **four** conjugacy classes are kept — `[a, b]`, `[a, b]^-1`, `[a, b]^2`, and `[a, b]^-2`.
    - Checking collective versus individual invariance: every conjugacy class whose orbit under the four record moves stays within cyclically reduced length at most eight has orbit size one, so `"kept"` gives the same five (or four non-empty) classes whether read class-by-class or as a finite invariant set of classes. Under `{a -> ab, a -> ba}` alone (`CTL-WP12-CONJ`), eighty-seven classes are kept (including `b` and its powers up to exponent eight), confirming the four-move filter is live.
- **What is wrong, loose, or rests on something unstated (two items):**
  1. **Omission of `"non-empty"` (length zero):** The empty word is a reduced word of length zero (at most eight), defines the trivial conjugacy class `{1}`, and is fixed by all six moves. Excluding it tacitly in `B` contradicts `C`'s final sentence, where excluding length zero is ALSO tacitly required for the opposite reason (`1` IS trivial!). Both `B` and `C` require `"non-empty reduced word(s) of length at most eight"`.
  2. **Looseness of `"conjugacy classes of reduced words of length at most eight"`:** No non-trivial `F_2` conjugacy class consists solely of words of length at most eight — iterating `a -> ba` on `[a, b]` produces `b^n [a, b] b^-n` of reduced word lengths four, six, eight, ten, twelve, escaping length eight at the third step. The statement requires defining the length of a conjugacy class via its minimal (cyclically reduced) representative, or speaking of conjugacy classes in `F_2` that admit at least one reduced representative of length at most eight.

---

### Statement C

> *"At a -> diag(i, -i), b -> the matrix with rows (0, 1) and (-1, 0): the traces of a, b and ab are 0; [a, b] is minus the identity; the commutator of [a, b] with each of a, b and their inverses is the identity. In the integral Heisenberg group, with a and b the two elementary unipotent matrices next to the diagonal: [a, b] is not the identity, and the same four triple commutators are. Every reduced word of length at most 8 that is trivial there is trivial at the first point. With a -> rows (1, 2), (0, 1) and b -> rows (1, 0), (2, 1): the commutator of [a, b] with a is not the identity, and no reduced word of length at most 8 is trivial."*

- **Result:** **`differs`** on the literal final clause (`"no reduced word of length at most eight is trivial"` at the third point is false for the empty reduced word of length zero, which evaluates to the two-by-two identity matrix; **`the same`** on every other clause, and **`the same`** on the final clause once **"non-empty"** is supplied).
- **Independent derivation:**
  - **First point (quaternion group `Q_8` inside `SL_2(C)`, `the same`):** With `a = diag(i, -i)` and `b` having rows `(zero, one)` and `(minus one, zero)`, the product `a b` has rows `(zero, i)` and `(i, zero)`. Thus `tr(a) = i - i = zero`, `tr(b) = zero + zero = zero`, `tr(a b) = zero + zero = zero`; `[a, b] = a b a^-1 b^-1 = -I_2`; and because `-I_2` is central, `[[a, b], g] = I_2` for each `g` in `{a, b, a^-1, b^-1}`.
  - **Second point (integral Heisenberg group `U_3(Z)`, `the same` — and non-vacuously true at length eight!):**
    - Mapping `a` and `b` to the two superdiagonal three-by-three elementary unipotent matrices `I_3 + E_{one, two}` and `I_3 + E_{two, three}` (or swapped, or lower-unitriangular by transpose), `[a, b] = I_3 +- E_{one, three} != I_3`, which is central in `U_3(Z)`, so all four triple commutators `[[a, b], g]` equal `I_3`.
    - **Self-correction of our Commit-one expectation (`45b29e14e` -> `3136d0def`):** Before running code, we hypothesized in Commit one from `[[a, b], a]` (reduced length ten) that the third lower-central subgroup `gamma_3(F_2) = ker(F_2 -> U_3(Z))` had minimum non-empty word length ten, which would have made the length-eight implication vacuously true on non-empty words. Exhaustive Commit-two enumeration over all thirteen thousand one hundred twenty-one reduced words of length zero through eight (and through length ten in `CTL-WP12-HEIS`) **refuted our Commit-one guess**: `ker(F_2 -> U_3(Z))` has **zero** words at lengths one through seven (and zero at length nine), **exactly sixty-four non-empty reduced words at length eight**, and two hundred eighty-eight at length ten! Why eight instead of ten? Because in a triple commutator such as `[[a, b^-1], b] = (a b^-1 a^-1 b) b (b^-1 a b a^-1) b^-1`, one `b b^-1` pair cancels in the middle, leaving the reduced word `a b^-1 a^-1 b a b a^-1 b^-1` of length **eight** (equivalently `[a, b] [b^-1, a^-1] = a b a^-1 b^-2 a^-1 b a`, trivial in every class-two nilpotent group by commutator bilinearity).
    - Every one of those **sixty-five** reduced words of length zero through eight trivial in `U_3(Z)` (`one` of length zero plus `sixty-four` of length eight) evaluates to `+I_2` at the quaternion point! In fact, the quaternion point has **two thousand five hundred twenty-one** trivial reduced words of length zero through eight (`one` at length zero, `thirty-six` at length four such as `a^4` and `a^2 b^-2`, `two hundred sixteen` at length six, and `two thousand two hundred sixty-eight` at length eight including `[a, b]^2`), and algebraically `ker(F_2 -> U_3(Z)) = gamma_3(F_2)` is contained in `ker(F_2 -> Q_8)` at **every** word length because `Q_8` is also nilpotent of class two.
  - **Third point (Sanov subgroup of `SL_2(Z)`, `differs` at length zero):** With `a` having rows `(one, two), (zero, one)` and `b` having rows `(one, zero), (two, one)`, `[[a, b], a]` evaluates to the matrix with rows `(minus three hundred thirty-five, one thousand five hundred fifty-two)` and `(minus one hundred twenty-eight, five hundred ninety-three)`, which is not `I_2`. Across all thirteen thousand one hundred twenty-one reduced words of length zero through eight, **zero non-empty** reduced words evaluate to `I_2` (in fact none at any positive length, by Sanov's theorem that these two parabolic matrices freely generate a rank-two free subgroup of `SL_2(Z)`), **whereas the empty reduced word of length zero evaluates to `I_2`**.
- **What is wrong, loose, or rests on something unstated (two items):**
  1. **Literal falsity at length zero in the final clause:** `"no reduced word of length at most eight is trivial"` fails on the empty reduced word `1` (length zero) unless **"non-empty"** is added.
  2. **Unstated matrix-group convention at the Heisenberg point:** `"the integral Heisenberg group, with a and b the two elementary unipotent matrices next to the diagonal"` leaves unstated whether upper- or lower-unitriangular three-by-three integer matrices are meant and which of `a, b` occupies `(one, two)` versus `(two, three)` (the kernel `gamma_3(F_2)` is unaffected, though `[a, b]` switches sign in its corner entry). Also note that restricting `"Every reduced word of length at most eight that is trivial there is trivial at the first point"` to length at most eight is mathematically sound and non-vacuous at length eight, even though the implication actually holds for reduced words of **arbitrary** length.

---

### Statement D

> *"The compact surfaces with boundary whose fundamental group is free of rank two are four: the torus with one boundary curve, the sphere with three, the projective plane with two, the Klein bottle with one. In their standard presentations every boundary curve lies in the commutator subgroup on the first of them only. A non-zero vector of Z^2 has an infinite orbit under the two maps (x, y) -> (x + y, y) and (x, y) -> (x, x + y); so a finite set of homology classes that the moves carry to itself is the zero class alone."*

- **Result:** **`differs`** as written without `"connected"` (up to homeomorphism), `"non-empty"`, and `"integral homology"` (**`the same`** once those three omitted hypotheses are supplied).
- **Independent derivation:**
  - **Surface classification:** Every compact **connected** surface `S` with `r >= one` boundary curves deformation-retracts onto a finite connected graph of Euler characteristic `chi(S) = one - rank(pi_1(S))`. Setting `rank(pi_1(S)) = two` forces `chi(S) = minus one`.
    - Orientable (`chi = two - two g - r = minus one`, `g >= zero`, `r >= one`): `(g, r) = (one, one)` (torus with one boundary curve) and `(zero, three)` (sphere with three boundary curves).
    - Non-orientable (`chi = two - c - r = minus one`, `c >= one`, `r >= one`): `(c, r) = (one, two)` (projective plane with two boundary curves) and `(two, one)` (Klein bottle with one boundary curve).
    Up to homeomorphism of compact **connected** surfaces, there are indeed four.
  - **Boundary curves in `[pi_1, pi_1]` (`the same` in substance, presentation-independent):** Expressing `pi_1(S) ~= F_2 = <a, b>` and mapping boundary curves to `H_1(S; Z) ~= Z^2`:
    - Once-bordered torus: single boundary `[a, b]` maps to `(zero, zero)`, which lies in `[pi_1, pi_1]`.
    - Thrice-bordered sphere: three boundaries `a`, `b`, `(a b)^-1` map to `(one, zero)`, `(zero, one)`, `(minus one, minus one)`, none zero.
    - Twice-bordered projective plane (`a^2 b c = 1`, free on `a, b` with `c = b^-1 a^-2`): two boundaries map to `(zero, one)` and `(minus two, minus one)`, neither zero.
    - Once-bordered Klein bottle (`a^2 b^2`): single boundary maps to `(two, two)`, non-zero.
  - **Infinite `Z^2` orbit (`the same` already for the forward semigroup):** Let `T_1(x, y) = (x + y, y)` (induced on `Z^2` by `b -> ba` and `b -> ab` on row coordinates, or transposed on column coordinates) and `T_2(x, y) = (x, x + y)` (induced by `a -> ab` and `a -> ba`). For any `(x, y) != (zero, zero)` in `Z^2`: if `y != zero`, then `T_1^n(x, y) = (x + n y, y)` yields infinitely many distinct vectors for `n >= zero`; if `y == zero`, then `x != zero` and `T_2^n(x, zero) = (x, n x)` yields infinitely many distinct vectors for `n >= zero`.
- **What is wrong, loose, or rests on something unstated (four items):**
  1. **Omission of `"connected"` (and `"up to homeomorphism"`):** The fundamental group `pi_1(S, x_0)` depends only on the path-component of the basepoint `x_0`. If `S` is disconnected — for instance, the disjoint union of the once-bordered torus (containing `x_0`) with `m >= one` closed disks or annuli — `S` is a compact surface with boundary whose fundamental group at `x_0` is free of rank two, giving infinitely many homeomorphism types unless **"connected"** (and equivalence **up to homeomorphism** / diffeomorphism) is stated.
  2. **Misleading qualifier `"In their standard presentations"`:** Whether a boundary curve represents an element of the commutator subgroup `[pi_1(S), pi_1(S)]` (up to conjugacy, which fixes the normal subgroup `[pi_1, pi_1]`) is equivalent to vanishing in `H_1(S; Z)` and is an **intrinsic topological property** of `S`, invariant under every automorphism of `F_2` and every choice of presentation. Qualifying it by `"In their standard presentations"` falsely suggests presentation-dependence.
  3. **Omission of `"non-empty"` (and set-versus-element phrasing) in the final clause:** The **empty set** of homology classes is finite and is carried to itself by all six moves (`M(empty) = empty`). Only a **non-empty** finite set of integral homology classes carried into itself by the moves is forced to be the singleton `{zero}` (whose sole element is the zero class).
  4. **Omission of integral coefficients `Z` for `"homology classes"`:** In homology with finite coefficients `H_1(S; Z / N Z)` (such as modulo two), the finite set of three non-zero classes `{(one, zero), (zero, one), (one, one)}` is carried to itself by all six moves. `"Integral homology classes"` (`H_1(S; Z)`) must be stated explicitly.

---

### Statement E

> *"In the clock-and-shift representation of prime dimension p (the shift sends e_j to e_{j+1}, the clock multiplies e_j by zeta^j; a is the shift, b the clock): [a, b] is a scalar zeta^k with k not zero; the four record moves keep that scalar; the swap and the tick send it to zeta^-k. So one such sector is carried to itself by the swap and the tick at p = 2 and at no odd prime, and a sector together with its conjugate is carried to itself at every p."*

- **Result:** **`differs`** as written (literally false unless `zeta` is a **primitive `p`-th root of unity** with basis indices read modulo `p`, and **false at prime two under the tick if `"sector"` means linear `F_2`-representation equivalence class**; **`the same`** once `zeta` is a primitive `p`-th root of unity in characteristic not equal to `p`, indices are modulo `p`, and `"sector"` is explicitly defined as the central-character / projective commutator-eigenvalue class `{[a, b] = zeta^k I_p}`).
- **Independent derivation (`relays/a2_c3/derive_wp_1_2.py`, `CTL-WP12-P2-TICK`):**
  - **Exact commutator calculation and why `zeta` must be a primitive `p`-th root of unity:** Reading `j` in `{zero, one, ..., p minus one}` modulo `p` (`a e_j = e_{j + one mod p}`, `b e_j = zeta^j e_j`):
    - For `j` in `{one, ..., p minus one}`, `(a b a^-1 b^-1) e_j = zeta^(j minus one minus j) e_j = zeta^(minus one) e_j`.
    - For `j = zero`, `b^-1 e_zero = e_zero`, `a^-1 e_zero = e_{p minus one}`, `b e_{p minus one} = zeta^(p minus one) e_{p minus one}`, and `a e_{p minus one} = e_zero`, so `(a b a^-1 b^-1) e_zero = zeta^(p minus one) e_zero`.
    - Therefore `[a, b] = diag(zeta^(p minus one), zeta^(minus one), ..., zeta^(minus one))` is a **scalar** matrix **if and only if** `zeta^(p minus one) = zeta^(minus one)`, i.e. **`zeta^p = one`**.
    - Even when `zeta^p = one`, at `zeta = one` we get `[a, b] = I_p = zeta^zero` (`k = zero`), falsifying `"with k not zero"`. Because `p` is prime, `[a, b]` is a scalar `zeta^k I_p` with `zeta^k != one` (`k == minus one mod p != zero`) **if and only if `zeta` is a primitive `p`-th root of unity** over a field of characteristic not equal to `p`!
  - **Action of the six moves on the scalar `[a, b] = zeta^k I_p` (`k == minus one mod p`):**
    - Because `[a, b]` is scalar (hence central in `GL_p`), Statement `B`'s free-group identities immediately imply that each of the four record moves sends `[a, b]` to a conjugate of `[a, b]`, which equals `zeta^k I_p`, while both the swap and the tick send `[a, b]` to a conjugate of `[a, b]^-1`, which equals `zeta^(-k) I_p`.
    - Comparing scalars: `zeta^(-k) = zeta^k` holds if and only if `zeta^(two k) = one`, which for primitive `zeta` of prime order `p` and `p` not dividing `k` holds **if and only if `p = two`** (`zeta = minus one`, where `zeta^(minus one) = minus one = zeta^(plus one)`). And the unordered pair of scalars `{zeta^k, zeta^(-k)}` is preserved by swap and tick at every prime `p` (collapsing to the singleton `{minus one}` at `p = two`).
  - **Decisive split between projective/central-character sectors and linear `F_2`-representations at prime `p = two` (`CTL-WP12-P2-TICK`):**
    - Statement `E` begins `"In the clock-and-shift representation of prime dimension p"` and then switches to the undefined noun `"sector"` (`"one such sector is carried to itself by the swap and the tick at p = 2"`).
    - **At every odd prime `p` (`p = three, five, seven, ...`):** By the Weyl commutation relation `a b = zeta^(minus one) b a`, we have `(a b)^p = zeta^(-p(p minus one)/two) a^p b^p`. Because `p` is odd, `(p minus one)/two` is an integer, so `p` divides `p(p minus one)/two` and **`(a b)^p = +I_p = a^p = b^p`**. Moreover, the discrete Gaussian diagonal matrix `D_one = diag(zeta^(((p + one)/two) j (j minus one)))` is well-defined modulo `p` and satisfies `D_one a D_one^-1 = a b`, `D_one b D_one^-1 = b`. Consequently, at every **odd** prime `p`, all four record moves carry the linear `F_2`-representation `rho_k` to an **isomorphic (`GL_p`-conjugate) linear `F_2`-representation**, and both the swap and the tick carry the `two p`-dimensional direct sum `rho_k (+) conjugate(rho_k)` to itself up to `GL_{two p}` conjugacy (verified by explicit `GL_three` and `GL_six` intertwiners in `derive_wp_1_2.py`).
    - **At `p = two` (`zeta = minus one`, `a` the Pauli shift `[[zero, one], [one, zero]]`, `b` the Pauli clock `diag(one, minus one)`):** Here `p(p minus one)/two = one` is **not** divisible by two, so `a^2 = +I_2` and `b^2 = +I_2` (order **two**, eigenvalues `plus/minus one`), whereas **`(a b)^2 = -a^2 b^2 = -I_2` (order four, eigenvalues `plus/minus i`)**!
      - Under the **swap** `(a, b) -> (b, a)`, `(b, a)` **is** `GL_2(C)`-conjugate to `(a, b)` via the Hadamard matrix `[[one, one], [one, minus one]]`.
      - Under the **tick** `(a, b) -> (ab, a)` (and likewise under `a -> ab`), the pulled-back linear `F_2`-representation sends generator `a` to `a b`, whose square is `-I_2 != +I_2 = a^2`. Therefore **no invertible `GL_2(C)` intertwiner exists**! Even more starkly, because `a` and `b` at `p = two` have purely real entries, `conjugate(rho) = rho`, and on the four-dimensional direct sum `rho (+) conjugate(rho) = rho (+) rho`, pulling back along the tick still sends `a` to `(a b) (+) (a b)` of square `-I_4 != +I_4`, so **neither `rho` nor `rho (+) conjugate(rho)` is carried to itself as a linear `F_2`-representation by the tick at `p = two`**!
      - What actually happens to two-dimensional irreducible `F_2`-representations with `[a, b] = -I_2` at `p = two`: there is a four-point discrete family indexed by the signs `(a^2, b^2)` in `{+I_2, -I_2}^2` (really `Hom(F_2, Z/two Z)` twists). Three of them — `(+I_2, +I_2)` (clock-and-shift), `(-I_2, +I_2)`, and `(+I_2, -I_2)` — factor through the dihedral group `D_4` of order eight and are **permuted transitively** by the six moves (matching the modulo-two homology orbit of size three in Statement `D`!), while the **fourth** representation `(-I_2, -I_2)` — which is **Statement `C`'s first point (the quaternion group `Q_8`)**, NOT clock-and-shift! — is the unique linear `F_2`-representation carried to itself by all six moves (`GL_2(C)` intertwiners verified for all six moves on `Q_8` in `derive_wp_1_2.py`)!
      - Thus Statement `E`'s conclusion at `p = two` holds **only** if `"sector"` is defined as the **projective representation / central-character class** `{[a, b] = zeta^k I_p}` (modding out `U(one)` scalar phases on generators, i.e. in `PGL_p(C)` or the quotient algebra `<a, b> / ([a, b] - zeta^k)` without imposing `a^p = b^p = one`), and **fails** if `"sector"` means linear `F_2`-representation isomorphism class!
- **Summary of unstated premises and ambiguities in `E` (four items):**
  1. **Modulo-`p` index convention:** `e_j -> e_{j + one}` must specify `j` in `Z / p Z` (`e_p = e_zero`).
  2. **Primitive `p`-th root of unity over characteristic not `p`:** `zeta` must satisfy `zeta^p = one` and `zeta != one` (and characteristic not `p` so `zeta != one` exists).
  3. **Undefined terms `"sector"`, `"carried to itself"`, and `"its conjugate"`:** As ordered matrix pairs `(a, b)`, neither swap nor tick fixes `(a, b)` at any prime; as linear `F_2`-representations up to `GL_p` similarity, the tick **fails** at `p = two` on clock-and-shift (and even on `rho (+) conjugate(rho)`), whereas Statement `C`'s `Q_8` point succeeds; only as central-character classes `[a, b] = zeta^k I_p` (or `PGL_p` projective classes) does `p = two` have one self-conjugate invariant sector.
  4. **Singleton collapse of `"a sector together with its conjugate"` at `p = two`:** Under central-character equivalence, at `p = two` a sector `zeta^one = minus one` equals its own conjugate `zeta^(minus one) = minus one`, so the union `{S_k, S_{-k}}` has cardinality **one** at `p = two` and cardinality **two** at every odd prime `p`.

---

## 3. Complete List of Repository Files Opened for `A2-C3`

1. `docs/seats/agy-002.md` (`M12`, `M15`)
2. `docs/seats/README.md` (protocol rules only)
3. `scripts/gates/gates.py` (`_VENDOR_RE` and `arrival_sentences` hygiene check on our own `relays/` files only)

Zero other repository files were opened during `A2-C3`.

0 of 19.
