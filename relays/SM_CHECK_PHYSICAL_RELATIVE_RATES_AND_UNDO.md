# The SM seat's check of the physical lane's relative-rate and full-undo proofs: every claim holds

*The SM seat, 2026-11-18. The sources are RELATIVE_RATES_AND_THE_ROLE_OF_A_MOVE.md and
INTERNAL_REGISTRATION_AND_FULL_UNDO.md in reports/physical_bridge_2026_09_05/foundational_primitive_audit_2026_11_18/
on audit/physical-bridge-2026-09-05 at 798281903, both read in full; PACKAGES_AND_PREMISES.md was read for the package
definitions. The check is on this seat's own code, while that lane is not running:
`relays/sm_physical_check/check_relative_rates_and_undo.py`, output
`relays/sm_physical_check/check_relative_rates_and_undo.json`. It imports nothing from the lane. No data.*

Conventions used by the check, both the ones the sources state: maps compose right to left, (g h)(s) = g(h(s)), as
in the sources' (5); pullbacks act on column functions, (G f)(s) = f(g(s)), as in the rate file's (1).

## Relative rates and the role of a move

| | the claim | check |
|---|---|---|
| § 2 | F_x, F_r commute, square to I; F_x F_r flips both | **holds**, exactly |
| (1) | off-diagonals ≥ 0, rows and columns sum to 0, L symmetric | **holds** in a, b, c; off-diag. a + c/4, b + c/4 |
| (2) | exp[t(F − I)] = ((1 + e^−2t)/2) I + ((1 − e^−2t)/2) F | **holds** to 2e-16 |
| (3) | ΠF = FΠ, Π² = Π, P_s = e^−cs P⁰_s + (1 − e^−cs) Π | **holds** to 3e-15 (50 random a, b, c, s) |
| § 2 | P⁰_s = product of the factors (2); P_s > 0 entrywise, s > 0 | **holds** on the same 50 draws |
| § 2 | ⟨U, V, J⟩ = S4; mean of 24 pullbacks is Π; rate c/24 on each | **holds**, exactly |
| (4) | eigenvalues 0, −(2(a+b)+c) twice, −(4a+c); a basis | **holds**, symbolically |
| § 3 | zero eigenvalue simple; uniform law unique; detailed balance | **holds** (kernel dim. 1 at 3 rate choices) |
| (5) | E[f f(s)] = e^−λs for f_x and f_p | **holds** to 2e-15 |
| (6) | R(1,1,1) = 1, R(1,2,1) = 5/7 | **holds**, exactly |
| § 3 | C_p = C_x^R | **holds** to 3e-15 |
| § 3 | spectra not identified by a permutation plus a clock scaling | **holds**: {0, −5³} vs {0, −7², −5}; all 24 C |
| § 4 | L invariant under both translations and J | **holds**, symbolically |
| § 4 | U·U⁻¹ fixes F_r, Π; swaps F_x ↔ F_x F_r | **holds** |
| § 4 | I, F_x, F_r, F_x F_r independent; U L U⁻¹ = L iff a = b | **holds**: U L U⁻¹ − L = (a − b)(F_x F_r − F_x) |
| (7) | I + F_x + F_r + F_x F_r = 4Π; a = b gives (4a + c)(Π − I), R = 1 | **holds**, symbolically |
| § 4 | L' = C L C⁻¹, f' = C f, μ' = μ C⁻¹ keep μf and μ P_s f | **holds**, all 24 C at (1, 2, 1) |

## Internal registration and full undo

| | the claim | check |
|---|---|---|
| (1)–(3) | V⁻¹, U⁻¹, J⁻¹ = J are two-sided inverses; R(U⁻¹U s) = R(s) | **holds**, m = 2..7 |
| § 1 | e(h) = id does not force h empty | **holds** (V⁻¹V), one line |
| (4) | J U J(x, r) = (x + r, r) | **holds**, m = 2..7 |
| (5) | U V(x, r) = (x + 1, r + x + 1), V U(x, r) = (x + 1, r + x) | **holds**, m = 2..7 |
| § 3 | table (0,0) → (1,0) → (1,1) → (0,1) under V, U, V⁻¹ | **holds** |
| (6) | W = V⁻¹UV = (x, r + x + 1), W ≠ id_S | **holds**, m = 2..7; W has m fixed points (x = −1) |
| (7) | W⁻¹ = V⁻¹U⁻¹V = (x, r − x − 1), two-sided | **holds**, m = 2..7 |
| § 2, Z | V, J V J reach every pair; U totally invertible | **holds** on [−6, 6]² only |
| § 2, d | outputs after permutations separate; transitive; 4, 8 states | **holds**, (m,d) = (2,2),(2,3),(3,2),(3,3) |
| (8) | q(J(x, r)) = r, so J does not descend through q | **holds**, m = 2, 3, 5 |
| § 4 | with V, U only, every future x output is independent of r | **holds** on all of ⟨U, V⟩, m = 2, 3, 5 |
| § 4 | o_x and o_x J separate all of S_m | **holds**, m = 2, 3, 5 |
| (9) | ⟨U, V⟩ = {T(a, b, c)}, m³ distinct maps | **holds**, m = 2..5 |
| (10) | T(a,b,c) T(a',b',c') = T(a + a', b + b', c + c' + b a') | **holds**, m = 2..5, all pairs |
| § 5 | T(a, b, c)⁻¹ = T(−a, −b, ba − c) | **holds** |
| (11) | U V U⁻¹ V⁻¹ = C = (x, r + 1); C central in ⟨U, V⟩ | **holds**, m = 2..5 (V U V⁻¹ U⁻¹ = C⁻¹) |
| (12) | V^a U^b C^c = T(a, b, c) | **holds**, every triple |
| § 5 | m = 2: order 8, (UV)² = C ≠ id, UV of order 4; D4, not Q8 | **holds**: 5 involutions vs Q8's 1 |
| § 5 | m = 2: U, J fix (0,0); transitive; stabiliser 6; ⟨U, V, J⟩ = S4 | **holds**; stabiliser = ⟨U, J⟩ |
| (13) | H/~ ≅ G: \|G\| classes, h ~ k iff π(h) = π(k) | **holds** on S4 → S3, Heis(3) → Z3², D4 → Z2 |
| (14)–(16) | P_t > 0, doubly stochastic, S_N-invariant, unique; P_t^n; t^n E f² | **holds** in t, N = 2..5, n ≤ 5 |
| § 7 | 6 of 24 permutations join any pair; P_t on S4 with weights > 0 | **holds**, exactly |

## Countercontrols (each must fail, and does)

| plant | result |
|---|---|
| U L U⁻¹ = L at (a, b, c) = (1, 2, 1) | **fails**, as it must |
| R(1, 2, 1) = 1 | **fails** |
| f_p has the eigenvalue of f_x at (1, 2, 1) | **fails** |
| W = V⁻¹UV is the identity on S_3 | **fails** |
| W moves every state (stronger than the text) | **fails**: m fixed points, m = 2..7 |
| J descends through q(x, r) = x | **fails** |
| the transposed cocycle c + c' + a b' in (10) | **fails**, every m = 2..5 |
| ⟨U, V⟩ at m = 2 has Q8's involution count | **fails** |

## Reading

- **Every finite, algebraic and numerically checkable claim in both files holds:**
  49 claims, and all 8 countercontrols fail in the stated direction.
- **The rate file's central point checks:** R = (4a + c)/(2(a + b) + c) is invariant under a common clock
  scaling and is not fixed by stationarity or full support.
  U-invariance of the fixed law is exactly a = b, which forces R = 1.
- **The undo file's central point checks:**
  - full undo and an object-level remainder coexist in one model (W ≠ id, W⁻¹W = id);
  - the two-update group is the order-m³ Heisenberg group in the stated coordinates;
  - at m = 2 that group is dihedral, not Q8;
  - with J the group is S4.
- **Two points need care. Neither is a failure:**
  - **The commutator.** (11) depends on the stated ordering U V U⁻¹ V⁻¹ with right-to-left composition. The reversed
    ordering gives C⁻¹, which differs from C for m ≥ 3.
  - **W's fixed points.** W has m fixed points. The § 3 table's "record differs" is about its chosen input (0,0). It
    is not a property of every input, and the text does not claim that it is.
- **Steps checked here only as instances.** The general proof steps were checked on chosen instances, not proved:
  - the uniqueness argument for (13), on three instances;
  - the integer-register statements, on a finite window;
  - the positivity of P_s, on random rate draws.

  Each of these steps is a short hand argument in the source, and every instance agreed with it.

## What is NOT checked

- **The analytic premises, which are inputs:**
  - the continuous-time framework and the choice P_s = exp(sL);
  - the Poisson-process implementation of the c term;
  - the claim that every finite sequence of jump labels has positive probability on a finite interval. This was not
    computed, though it follows from the positivity of the rates;
  - the statements about infinite histories.
- **Physical interpretations:**
  - whether a relative rate is a physical parameter, or a clock convention under a further equivalence;
  - the distinction between active updates, passive redescriptions and fixed-law automorphisms, as a duty on the OA
    programme;
  - registers as observers, records or memory;
  - the five uses of "nothing";
  - anything about qualia, PF2, PF5, SM3 or gravity.
- **Steps done by hand only, or by reference:**
  - the § 1 argument about history ledgers versus physical memory;
  - "J cannot descend", beyond the finite check above;
  - the reuse of the AR1/AR2 criterion and of the November 7 quotient;
  - the § 8 literature attributions (Bennett's notes; Adámek, Milius and Urbat). Neither source was opened here.
- **The premise ledger and the outcome list in PACKAGES_AND_PREMISES.md**, beyond the finite claims above.
