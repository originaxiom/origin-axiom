# B1914 — The line's last bit goes with the hand: every symmetry of the golden bundle that reverses its orientation exchanges the twins, and none that keeps it does (decision 4 of the input budget; P-718's Q1)

**Verdict: PROVED** (exact integer computation, with the symmetry group checked against SnapPy). cc (main), 2026-11-13
(S306p). Main's own code. No data; no value of the modulus on record is read, and nothing is compared with anything
measured. **0 of 19.**

## 1. The answer first

- **The question.** Decision 4 of the input budget is the line: its slope and offset (A02, A03), the charge premise at
  level 5, the class of lines (FL08). Its named route was a condition that can fail: a flat line on the fibre extends
  over a history exactly when the history fixes its character (B1867 § 4). Built and run, what does it decide, and what
  is left?
- **What it decides is already on record.** The golden ground LR fixes a non-trivial character only at order 5, exactly
  ±(1,2) and ±(2,4), each sent to its inverse (B1867 § 4; P-718, P-721; B1845 calls the same matrix RL). The census
  here reproduces it over every order up to 60. The departures LᵃR keep the pair exactly when a ≡ 1 mod 5, so the least
  beyond the ground is the run of 6, L⁶R, which is B1867 § 3's "the run of 6 equals the golden word at level 5"; with
  one, two and three golden periods its signs are +, −, + (B1867). The condition can fail: L²R, LR² and L³R with one to
  three golden periods do not keep the pair. A history alone does not force the order: the run-of-6 histories also fix
  lines of orders 2, 3, 4, 6 and more; the order 5 comes from the ground.
- **What no history can decide, also on record.** The two points are twins: (2,4) = 2·(1,2), and a matrix that keeps ±v
  keeps ±2v by linearity (B1872's correction of 2026-11-11). This is an identity, not a result; it is computed here
  only so the census is whole (of the 120 elements modulo 5, 10 keep the pair and none separates the twins; of the
  32,766 positive words of 1 to 14 letters, 2,687 keep the pair and none separates them). So P-718's Q1, whether the
  excursion picks one of the two points, has the answer no, for every history, by that identity.
- **What is new: the object's own symmetries and the twins.** The symmetries of the golden bundle are the integer
  matrices X with X·LR·X⁻¹ = LR or (LR)⁻¹. A full search with entries up to 12, and the two solution families of the
  linear equations up to 300, find 104, all of the form ±Jⁿ or ±JⁿK, with J = [[1,1],[1,0]] (J² = LR, determinant −1:
  the tick) and K = [[0,1],[−1,0]] (K·LR·K⁻¹ = (LR)⁻¹). Modulo the powers of LR they fall into eight classes, four of
  them reversing the orientation, as SnapPy's symmetry group of the figure-eight complement has it (D4, order 8,
  amphicheiral). Every one keeps LR's eigenline modulo 5 and acts on it as a scalar: **±1 when it keeps the orientation
  and ±2 when it reverses it.** So the twins are kept by every symmetry that keeps the orientation and exchanged by
  every symmetry that reverses it. The record had the tick's case (B1871, B1879; B1881's elliptic element); this is the
  whole group.
- **So the four placements (the hand, the twin) fall into two classes** under the object's symmetries:
  {(+ hand, v), (− hand, 2v)} and {(+ hand, 2v), (− hand, v)}.

## 2. What this means for the budget (main's reading)

- **Decision 4's route is spent.** The extension condition gives what the ground already gives (order 5, the
  eigenline) and cannot give the last bit.
- **The last bit is not a separate decision.** Counted up to every symmetry of the object, the hand and the twin carry
  one bit between them: two classes, not four. Counted up to the symmetries that keep the orientation, the twin is a
  bit beyond the hand, and no such symmetry removes it. Which count applies is the hand question (decision 1), and it is
  not decided here. B1872's sentence "which twin is a convention" holds for the allowed set of histories (the twins
  have one stabiliser); for a reading that tells the hands apart, which twin is the hand under another name.
- **What could decide it** is only a quantity that is not linear in the point. Any quadratic form q has
  q(2v) = 4q(v) = −q(v) modulo 5, so a Chern–Simons phase changes sign between the twins (P-718's row, S305y). The
  line's last bit is a sign of the same kind as the hand's rows.
- No input leaves the budget by this arc. The line's 266 choices were already the hand and one bit (B1845, P-718);
  this arc shows the one bit and the hand are one decision up to the object's symmetry.

## 1a. Seen first

`VERDICT topic-sweep /twin|orientation-reversing|amphich|symmetry group|the hand/: 188 of 1653 arcs on main match
(NEGATIVE 29, OPEN 14, PROVED 144, RETRACTED 1); 56 register rows match (DONE 22, QUEUED 34)`. Read for this arc: B1867
§§ 3–4 (the extension condition; the run of 6 at level 5), B1845 § 2 and P-718 (the eigenline, the diamond is not a
frame symmetry at a fixed modulus), P-721 (det(LR + I) = 5), B1872's correction (the twins; the identity; 10 of 120),
B1871 and B1879 (the tick; the exchange carries one hand onto the other), B1881 Q2–Q3 (the elliptic element exchanges
the twins). **Literature:** the centraliser of a hyperbolic matrix in GL₂(ℤ) is the unit group of its order, here
±φⁿ; the figure-eight knot is amphicheiral and its complement's symmetry group is the dihedral group of order 8
(standard; SnapPy computes it).

## 3. What is not shown

- The record's note that the mirror fixing a point of the modulus fixes each candidate line (P-718, S305t) concerns a
  reflection of one fibre at one modulus. Whether that reflection is a symmetry of the bundle is not computed here; the
  guard on read-out points keeps that point out of this arc. This arc's statement is about the bundle's own symmetries.
- Whether the values read on the two classes differ is B1845's finding at a fixed modulus; not re-examined.
- The orientation of a symmetry: X with X·A·X⁻¹ = A^e induces (x, t) ↦ (Xx, t) for e = 1 and (Xx, 1 − t) for e = −1
  on the mapping torus, of orientation sign det X · e (standard).
- The Chern–Simons phase itself is not recomputed; only the identity q(2v) = 4q(v) is used.

## Disclosed

Main wrote part (b) of the script as a finding before reading B1872's correction, which records the same fact as an
identity. It is relabelled in the script and on this page, and is not counted as a result.

## Files

- `verification/the_last_bit.py` → `the_last_bit.json`, `the_last_bit_run.txt` (seconds).
- The lock: `verification/test_b1914_the_last_bit.py` (three planted faults: two points that are not twins are
  separated; the swapped convention loses the line; an orientation read from the determinant alone mixes the two scalar
  sets).

## Reproduce

```
cd frontier/B1914_the_twin_and_the_hand_are_one_bit_every_mirror_of_the_bundle_exchanges_the_twins/verification
python3 -B the_last_bit.py && python3 -m pytest -q .
```
