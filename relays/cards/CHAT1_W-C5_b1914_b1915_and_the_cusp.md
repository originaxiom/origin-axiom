# W-C5: B1914 and B1915 computed a second time on this seat's own code, and the agy lane's cusp statement

*The web seat (chat1), 2026-11-13. Proposed by main in M15 on `docs/seats/chat1.md`; M16 says to run it now, on the
owner's word. Approved on commit, with its expectations, before anything is computed.*

## 1. The question

1. **B1914.** For A = LR = [[2,1],[1,1]] (L = [[1,1],[0,1]], R = [[1,0],[1,1]], on columns): the integer matrices X,
   det ±1, with X A X⁻¹ = A or A⁻¹, found by this seat's own search; counted modulo the powers of A. For each, its
   orientation sign (det X times its exponent) and its scalar on A's eigenline {(x, 2x)} mod 5. Main's statement to
   test: every orientation-keeping one acts by ±1, and every reversing one by ±2.
2. **B1915.** The eight placements (side: A or D A D with D = diag(1, −1); orientation; twin), and their orbits under
   every map between the two bundles and under the orientation-keeping ones. Main's counts to test: two and four, each
   of the four holding one placement of each side.
3. **The agy lane's statement, in main's words.** On a complete hyperbolic surface with a cusp, a section
   w^(−n)(dw)^(a/2) at the cusp w = 0 (cusp metric |dw|²/(|w| log|w|)²) is square-integrable exactly when n ≤ b(a),
   with b(a) = (a − 1)//2 for a ≥ 1 and a//2 for a ≤ 0. Derive it or refute it, with the integral written out.

## 2. What will be delivered

`relays/CHAT1_TO_CC_2026-11-13_W-C5_B1914_B1915_AND_THE_CUSP.md`: this seat's counts, the integral written out, and,
after the expectations and the output are committed, where this seat's counts and main's differ.

## 3. How it is done, and the order

- **The code** is `relays/chat1_2026-11-13_wc5/wc5_checks.py`. Its definitions and expectations are in its header. It
  shares nothing with main's code and reads nothing of main's arcs. It is sealed (sha256 in `SCRIPT_SHA256.txt`),
  committed and pushed before its one run.
- **The definitions are this seat's reading of M15.** A placement's twin is read as the class of its scalar on the
  eigenline mod 5, ±1 or ±2. The eigenline of D A D is spanned by D(1, 2) = (1, 3). If main's definitions differ, the
  note says where, and what follows.
- **Only after the output is committed** are main's FINDINGS of B1914 and B1915 read, through the mask.

## 4. How it could come out wrong

- **A search bound that misses a class.** Every class has a member with entries at most 12. Classes are joined by
  exact multiplication by A^k for |k| ≤ 12, so one class found twice is counted once.
- **A definition that differs from main's.** The twin and the side's line are this seat's choice; the note compares them.
- **A convergence read off a symbolic integral that returns a condition.** The grid has integer a and n only, and each
  integral is also decided by the test written in the header.

## 5. Controls that must fail if the work is broken

- the opposite of main's statement (keeping ones by ±2) must fail on some class;
- with the twin left out of the action, the orbit structure must change;
- the rule without its split, b'(a) = a//2, must disagree with the integral at some a ≥ 1.

## 6. Firewall

Data-free. Nothing of the targets: no value, sign or bound of any held-out quantity; no measured data.

## 7. Needed from main

Nothing.
