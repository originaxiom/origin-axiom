# THE DEPARTURE THE LINE CANNOT SEE — pre-registration (the web seat, 2026-11-06)

**For:** the owner's goal ("Find a process in the object that places τ, the line and an energy scale, so we stop
choosing them"), as main framed it at S305m/S305n: P-717 (one departure from the golden ground path, by "the minimal
run the last finite rung cannot see", read out at the excursion's apex), P-714 and P-715.
**Kind:** data-free. Pure SL(2, ℤ) arithmetic and hyperbolic geometry: no frame value, no θ-function, no data file, no
held-out quantity, no θ̄, no inter-sector value. One of the lines named below has slope 2/5, a family address; it
enters only as a pair of fractions.
**Written before** `departure_check.py` is run. The predictions in § 3 were derived by hand first; the script checks
them.

## 1. Seen first (swept on main at cfb11d1c6)

- `VERDICT topic-sweep /own order.?5|order.?5 pair|anti.?invariant|ker ?\((RL|LR|M|A) ?\+ ?I\)|det\((RL|LR|M|A) ?\+ ?I\)|fox|5.colou?r|colou?ring/ (full text): 79 of 1589 arcs on main match (NEGATIVE 16, OPEN 2, PROVED 61); 7 register rows match (DONE 4, QUEUED 3)`
- `VERDICT topic-sweep /homoclinic|heteroclinic|one departure|run of (five|six|5|6)\b|L\^?[56] ?R|L⁵R|L⁶R/ (full text): 6 of 1589 arcs on main match (NEGATIVE 2, PROVED 4); 7 register rows match (DONE 4, QUEUED 3)`

Bearing on it:
- **B1733** (PROVED): a thread A fixes a line of exact order N up to sign iff N divides the larger Smith invariant of
  A ∓ I. At order 5 it fixes one pair {v, 2v}; when A ≡ ±I mod 5 it fixes all twelve order-5 lines. The choice
  v ↔ 2v is the 3-manifold's orientation, a real bit wherever the frame has a hierarchy.
- **P-284 / B1720** (the thread rule): τ at the thread's apex, the line among the lines its monodromy fixes up to sign.
- **P-312**: the trace form of B1733 at order 5 is tr ≡ ±2 mod 5.
- **P-465**: the golden ground path, with "LR's own order-5 pair".
- **P-717** and its S305n control: τ* = ½ + (2 + √5/2)i from L⁵R(LR)^k.

The line convention is the record's: (α, b) ↦ (α, b)γ⁻¹ under τ ↦ γτ (B1733 § 1; T: (α, b) ↦ (α, b − α)). The frame
identifies ±w.

## 2. What is stated, before computing

**(L) The line is the history's own** (P-284's thread rule, B1733).
- For a closed thread: the order-5 lines its monodromy fixes up to sign, in the marking of its highest apex.
- For a homoclinic history (golden, one departure, golden): the order-5 lines fixed up to sign by both asymptotic
  golden lifts, in the marking of the apex.
- The golden monodromy has det(LR − I) = −1 and det(LR + I) = 5, the figure-eight's determinant ∣Δ(−1)∣. So it fixes
  no nonzero line and exactly one order-5 pair (its two D₅ colourings): the line's order 5 comes from the monodromy,
  not from a choice of rung.

**(D) The departure is the one the level-5 rung cannot see** (P-717's own criterion, read as written).
- A run of n letters is seen at level 5 as n mod 5 (T⁵ ↦ 1 in Γ/⟨⟨T⁵⟩⟩ ≅ A₅). The golden path has every run 1.
- So a one-run departure is invisible at level 5 iff n ≡ 1 mod 5, minimally n = 6. That is the insertion of T⁵ into
  the golden path.
- A run of 5 is seen as a run of 0: the letter is deleted and its neighbours merge into a run of 2, which is a
  departure in P-465's sense.

**(A) The read-out point** is the excursion's apex, as in P-717. The excursion is palindromic, and the apex is the one
point of the history fixed by its reflection.

## 3. Predictions (hand-derived; the script checks each)

**P1. The golden pair.**
- ker(RL + I) = {±(1/5, 2/5), ±(2/5, 4/5)} and ker(LR + I) = {±(1/5, 3/5), ±(2/5, 1/5)}.
- ker(RL − I) = ker(LR − I) = 0.
- RL and LR are ±unipotent mod 5 (tr 3 ≡ −2).

**P2. Level-5 visibility.** L^n R (LR)^k ≡ (LR)^{k+1} mod 5, as matrices, iff n ≡ 1 mod 5. For n = 5 the two are not
conjugate in SL(2, 𝔽₅) unless k ≡ 4 mod 5 (where the traces agree).

**P3. Apexes.**
- The one-run homoclinic excursion of length n runs from −1/φ to n + 1/φ, with apex n/2 + i(n − 1 + √5)/2.
- n = 5: ½ + 3.1180i, as P-717 has it.
- n = 6: **τ*₆ = i(5 + √5)/2 = 3.6180i, with Re τ = 0 exactly**, from the palindrome centred on an integer.
- The closed approximants L⁶R(LR)^k converge to τ*₆, with Re τ = 0 at every k, by two methods: the matrix orbit
  with S-conjugates, and the continued fractions.
- The L⁵R(LR)^k values reproduce P-717's control: 3.354, 3.149, 3.1225, 3.11868, ….

**P4. The line along the closed approximants (B1733's rule, at the highest apex, Re τ in [0, 1)).**
- n = 6: the own order-5 lines are exactly {±(1/5, 0), ±(2/5, 0)} for k ≢ 4 mod 5. All twelve are own lines for
  k ≡ 4 mod 5, where (LR)^{k+1} ≡ ±I mod 5. The golden pair is therefore an own pair at every k.
- n = 5: order-5 own lines exist only where tr ≡ ±2 mod 5, i.e. k ≡ 0, 4, 5, 9 mod 10, and they are not one pair
  for every k.

**P5. The homoclinic history.**
- The incoming golden lift is RL (fixing −1/φ). The outgoing one is TⁿLRT⁻ⁿ = T^{n−1}RLT^{1−n} (fixing n + 1/φ).
- In the apex marking their own pairs agree iff n ≡ 1 mod 5. Equivalently, T^{n−1} lies in the line's stabiliser
  Γ_{±w}: the excursion is homoclinic in the line's own curve H/Γ_{±w}.
- n = 6 (Re 0): both are {±(1/5, 0), ±(2/5, 0)}.
- n = 5 (Re ½): in {±(1/5, 4/5), ±(2/5, 3/5)}, out {±(1/5, 0), ±(2/5, 0)}.
- The palindrome's reflection (about Re τ = c, acting on lines as (α, b) ↦ ±(α, −b − 2cα), from the frame's mirror
  covariance, P-336, and T) swaps the in and out pairs. It therefore fixes a pair iff n ≡ 1 mod 5.

**P6. The departure's excess length.**
- lim_k [ℓ(L^nR(LR)^k) − ℓ((LR)^{k+1})] = 2 log((n − 1 + √5)/√5), with ℓ = 2 arccosh(tr/2).
- For n = 6 that is 2 log(1 + √5) = 2.3482: an O(1) number, not a hierarchy.

**What would refute (D) + (L) as a consistent reading:**
- an n = 6 approximant (k ≢ 4 mod 5) whose own order-5 pair is not the golden pair at its apex;
- or n = 5 approximants that share one pair at every k;
- or the in and out pairs agreeing for some n ≢ 1 mod 5.

## 4. What this does not do

- It computes no frame value at τ*₆ or anywhere else, and it reads none of the six.
- It does not compare τ*₆ with P-373's strip. That would make the six a criterion (P-708).
- Whether any card is spent on either candidate is Review 75's and the owner's.
- **Choice 1 (one departure) is not derived here.**
- **The scale is not placed at this level.** The history's numbers are dimensionless: § 3's apex, Lagrange value,
  excess length, the golden period 4 log φ, and the frame's nome. Mapping any of them to log(μ/unit) is a dictionary
  entry that the history does not supply; no clock is forced (B721, B1816). This is consistent with P-715's swept
  wall (B151, B660, B719, B811, B980).

0 of 19.
