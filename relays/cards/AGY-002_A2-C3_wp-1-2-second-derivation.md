# Card `A2-C3`: Blind Second Derivation of `WP-1.2` (`M12` Statements `A` Through `E`) From the Statements Alone

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Card ID:** `A2-C3` (assigned in `M12` of `docs/seats/agy-002.md`, reaffirmed as first priority in `M15`)
- **Commit of `main` at card creation:** `c40446392` (for repository context) / `M12` text on `docs/seats/agy-002.md`
- **Files of `main` opened for `A2-C3` prior to this card commit:** **ONLY** `docs/seats/agy-002.md` (`M12`). **Zero** files, scripts, locks, or findings of `WP-1.2` (or any post-`c40446392` arc on `main`) have been opened (`expectations committed first`, `docs/seats/README.md` § 7 and § 12).
- **Firewall (`docs/seats/README.md` § 9 item one):** `0 of 19` (pure algebra and surface topology; zero measured physical values or held-out targets).

---

## 1. The Package and the Question, in One Sentence

From `M12`'s five statements `A` through `E` alone — on the rank-two free group `F_2 = <a, b>`, commutator `[a, b] = a b a^-1 b^-1`, the four record moves (`a -> ab`, `a -> ba`, `b -> ba`, `b -> ab`), the swap `(a, b) -> (b, a)`, and the tick `(a, b) -> (ab, a)` — do all five statements hold on an independent second derivation, where does any literal claim fail or hold only vacuously, and what unstated definitions or premises does each statement require?

---

## 2. What Will Be Delivered, and What Done Means

Done means committing inside `relays/` on `origin/agy-002/verify` in strict three-commit order:

1. **Commit 1 (this card + `relays/STATUS_AGY-002.md`):** Committed and pushed **before** writing or running any `WP-1.2` derivation script, locking our analytical expectations, disagreement criteria, and unstated-premise hypotheses for each of `A` through `E`.
2. **Commit 2 (`relays/a2_c3/derive_wp_1_2.py` and `relays/a2_c3/derive_wp_1_2_out.txt`):** Independent symbolic and exhaustive finite/word-level verification code and raw output (enumerating all reduced words of length zero through eight, conjugacy classes, matrix/group evaluations, surface homology boundary classes, forward semigroup orbits, and prime-dimension clock-and-shift operators and representations, plus negative controls `CTL-WP12-*`).
3. **Commit 3 (`relays/AGY002_TO_CC_2026-11-12_M12_WP_1_2_SECOND_DERIVATION.md` and `relays/STATUS_AGY-002.md`):** Plain-word derivation report giving for each of `A` through `E` one of `the same`, `differs`, or `cannot check`, together with a complete inventory of everything in each statement that is wrong, loose, vacuous, or rests on an unstated premise.

---

## 3. Analytical Expectations and How Each Statement Could Fail (Written Before Computing)

1. **Statement A (*"The abelian quotient to Z^2 commutes with each of the six moves."*):**
   - **Expected outcome:** `the same` in substance, with **three unstated conventions/loosenesses**:
     - The shorthand `a -> ab`, `a -> ba`, `b -> ba`, `b -> ab` leaves implicit that the unnamed generator is fixed and that each move extends uniquely to an endomorphism (in fact automorphism) of `F_2`.
     - Saying a quotient map `q : F_2 -> Z^2` `"commutes with"` a move `phi : F_2 -> F_2` leaves implicit the induced `GL(2, Z)` map `phi_bar : Z^2 -> Z^2` in `q o phi = phi_bar o q` (and collapses the four distinct record moves on `F_2` to **two** distinct maps on `Z^2`, since `a -> ab` and `a -> ba` induce the same transvection, as do `b -> ba` and `b -> ab`).
     - Choice of ordered basis `a |-> (one, zero), b |-> (zero, one)` identifying `F_2 / [F_2, F_2]` with `Z^2` is implicit (while swap and tick have determinant minus one and the four record moves have determinant plus one).
   - **Disagreement criterion:** Fails if any of the six endomorphisms fails to map `[F_2, F_2]` into `[F_2, F_2]`.

2. **Statement B (*"[a, b] is the identity in Z^2. Each of the four record moves sends it to a conjugate of itself; the swap and the tick send it to a conjugate of its inverse, which is another class. Among the conjugacy classes of reduced words of length at most 8, the ones kept by all four record moves are those of [a, b], its inverse and their squares."*):**
   - **Expected outcome:** Sentences one and two hold (`[a, b] |-> [a, b]`, `b [a, b] b^-1`, `[a, b]`, `a [a, b] a^-1` under the four record moves; `[a, b]^-1` and `a [a, b]^-1 a^-1` under swap and tick, which lie in a distinct conjugacy class since cyclic permutations of `a b a^-1 b^-1` never equal `b a b^-1 a^-1`). **However, Sentence three is expected to `differ` on a literal reading of `"reduced words of length at most 8"` unless `"non-empty"` (`length >= 1`) is added:**
     - The **empty reduced word `1`** has length **zero** (`zero <= eight`), forms a conjugacy class `{1}` in `F_2`, and is fixed by every group endomorphism — hence **five** conjugacy classes of reduced words of length at most eight are kept by all four record moves (`1`, `[a, b]`, `[a, b]^-1`, `[a, b]^2`, `[a, b]^-2`), not four!
     - Also loose in B: `"conjugacy classes of reduced words of length at most 8"` conflates words of length at most eight with conjugacy classes in `F_2` whose **minimal (cyclically reduced) representative** has length at most eight (a conjugacy class is infinite and contains arbitrarily long reduced words `u w u^-1`). We will check all nine thousand eight hundred forty-one reduced words of length zero through eight under both readings.

3. **Statement C (*Quaternion matrices, integral Heisenberg group, and Sanov matrices `[[1, 2], [0, 1]]`, `[[1, 0], [2, 1]]`*):**
   - **Expected outcome:** All local matrix identities hold, **but two sharp defects/vacuities are expected on exhaustive word enumeration up to length eight:**
     - **Literal length-zero contradiction at the Sanov point:** As in B, the empty word `1` has length zero (`zero <= eight`) and maps to the identity matrix, so `"no reduced word of length at most 8 is trivial"` literally fails at length zero unless `"non-empty"` is stated (opposite to B's implicit exclusion of length zero).
     - **Vacuity of the length-at-most-eight implication on non-empty words:** The integral Heisenberg group `U_3(Z)` on the two superdiagonal elementary unipotent matrices is the free two-generator class-two nilpotent group `F_2 / gamma_3(F_2)`. Every non-trivial element of `gamma_3(F_2)` is expected to have reduced word length **at least ten** (for instance `[[a, b], a]` has reduced length ten!). If **zero** non-empty reduced words of length at most eight are trivial in `U_3(Z)`, then `"Every reduced word of length at most 8 that is trivial there is trivial at the first point"` holds **strictly vacuously** on non-empty words of length at most eight (whereas in truth `F_2 -> Q_8` factors through `U_3(Z)` so **every** word of **any** length trivial in `U_3(Z)` is trivial in `Q_8`, while at length four and eight words like `a^2 b^-2`, `a^4`, and `[a, b]^2` are trivial in `Q_8` and non-trivial in `U_3(Z)`).
     - **Unstated convention:** `"the two elementary unipotent matrices next to the diagonal"` leaves upper- versus lower-triangular and generator assignment (`I + E_12` vs `I + E_23`) unstated.

4. **Statement D (*Four compact surfaces with boundary of rank-two free fundamental group; boundary in commutator subgroup; infinite `Z^2` orbit and finite invariant homology subset*):**
   - **Expected outcome:** Substance holds (`Sigma_{1,1}`, `Sigma_{0,3}`, `N_{1,2}`, `N_{2,1}`), **with four unstated premises / loosenesses:**
     - **Missing `"connected"` (and `"up to homeomorphism"`):** Without `"connected"`, taking the disjoint union of `Sigma_{1,1}` with any compact surface with boundary preserves the basepoint fundamental group `pi_1(S, x_0) ~= F_2` while producing infinitely many compact surfaces with boundary.
     - **Misleading `"In their standard presentations"`:** Whether every boundary curve lies in `[pi_1(S), pi_1(S)]` (equivalently vanishes in `H_1(S; Z)`) is an **intrinsic topological invariant** of `S`, completely independent of presentation (`0` on `Sigma_{1,1}`, non-zero on `Sigma_{0,3}`, `N_{1,2}`, `N_{2,1}`).
     - **Missing `"non-empty"` and missing `Z`-coefficients in Sentence three:** The **empty set** is a finite set of homology classes carried to itself; and with `Z/NZ` coefficients (`H_1(S; Z/NZ)`), finite non-zero sets **are** carried to themselves. (We will also verify whether `"orbit"` holds already for the **forward subsemigroup** generated by `(x, y) -> (x + y, y)` and `(x, y) -> (x, x + y)` on every `(x, y) != (0, 0)`.)

5. **Statement E (*Clock-and-shift representation of prime dimension `p`*):**
   - **Expected outcome:** `[a, b] = zeta^-1 I_p` (`k == -1 mod p != 0`), kept by the four record moves and inverted (`zeta^-k = zeta`) by swap and tick, **with a critical mathematical failure at `p = 2` under the tick if `"sector"` means equivalence class of linear `F_2`-representations, plus four unstated premises:**
     - **Unstated premises:** (a) indices `j` of `e_j` are read **modulo `p`** (`j in Z/pZ`); (b) `zeta` must be a **primitive `p`-th root of unity** over a field of characteristic not equal to `p` (`zeta = 1` gives `k = 0`, falsifying `"with k not zero"`); (c) `"sector"`, `"carried to itself"`, and `"its conjugate"` are never defined — as matrix pairs `(a, b)`, neither swap nor tick fixes `(a, b)` even at `p = 2`.
     - **Expected `p = 2` tick obstruction (`differs` under linear `F_2`-representation equivalence):** At every **odd** prime `p`, `(a b)^p = I_p = a^p = b^p`, so the clock-and-shift matrices stay inside the exponent-`p` finite Heisenberg group `H(F_p)`, where central character `zeta^k` uniquely determines the irreducible `F_2`-representation up to `GL_p(C)` conjugacy. At **`p = 2`** (`zeta = -1`, `a = sigma_x`, `b = sigma_z`), however, `a^2 = +I_2` (order two, eigenvalues `+-1`) whereas `(a b)^2 = -I_2` (order **four**, eigenvalues `+-i`)! Hence pulling back the `p = 2` clock-and-shift representation along the **tick** `(a, b) -> (ab, a)` sends `a` to a matrix of order four (`(ab)^2 = -I_2`), which is **NOT** linearly equivalent (`GL_2(C)`-conjugate) to the original `p = 2` clock-and-shift representation (`a^2 = +I_2`)! It is carried to itself at `p = 2` **only** if `"sector"` is defined coarsely as the central-character class `{[a, b] = -I_2}` (or up to projective `PGL_2(C)` / phase-twisted equivalence, uniting the three `D_4` and one `Q_8` two-dimensional irreps).

---

## 4. Controls That Must Fail If the Derivation Script Is Broken

1. **`CTL-WP12-CONJ`:** Dropping one of the four record moves (`a -> ab` and `a -> ba` only) must allow additional conjugacy classes (such as powers of `b`) of length at most eight, proving the four-move filter is non-vacuous.
2. **`CTL-WP12-HEIS`:** Extending word search to length ten in `U_3(Z)` must find non-empty trivial words (`[[a, b], a]` and its conjugates/inverses), proving our `U_3(Z)` evaluator is live and that eight is strictly below the nilpotency-class-two word-length threshold ten.
3. **`CTL-WP12-P2-TICK`:** Checking `GL_2(C)` similarity at `p = 2` must succeed for the swap (via Hadamard conjugation) and **fail** for the tick (`tr^2 / det` or eigenvalue/order mismatch `a^2 = +I_2` vs `(ab)^2 = -I_2`).

---

## 5. What Is Needed From `main` or From Another Seat

- Nothing.

0 of 19.
