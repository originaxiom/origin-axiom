# SM literature note 1 — what the literature settles and sharpens on this seat's open fronts

*The SM seat, 2026-11-13; main at b1bcc7f50, last message read M23. This is not a card. The owner asked the seat to
see whether the literature helps on its open fronts. This page reports what was read, and one post hoc check on
output already committed. Nothing here is a value of the frame, and nothing was compared with a measured number.
The derivations in §§ 3–4 are this seat's, from standard duality. They are not reviewed. Proposals in § 5 wait for
main's word (§ 6).*

## 1. In short

- **SM-C7's identities are classical.** Hecke's integral formula and the Kronecker limit formulas for real quadratic
  fields already give steps 1 and 2. The record's own content is B1919: B1656's channel norm is the shifted Kronecker
  limit.
- **The same value at s = 0 has an orientation-odd reading.** In the untwisted case it equals the eta invariant and
  signature defect of the closed torus bundle (Atiyah; Atiyah–Donnelly–Singer; Müller). Whether the twisted value
  equals the twisted rho invariant has not been checked. If it does, the hand gets a natural carrier.
- **"Filling cannot supply the order" is a theorem.** Duality and Euler characteristic zero force h¹(V) = h¹(V*) on
  every closed manifold for the record's modules. The post hoc check holds on all 46 618 of E6's modules.
- **The record's index is a boundary quantity.** On E6's output, I = n − n* equals h¹(M; V*) − h¹(M; V) on every
  one of the 46 618 modules. By duality, that asymmetry is h⁰(∂M; V) minus the dimension of the boundary image of
  H¹(M; V). The order is how "half lives, half dies" splits between V and V*.
- **SM-C8 should be amended before it runs.** It has a vacuous-join trap, a quotient line that is not canonical, and
  an index identity it can carry as a control. The order-relevant part is one term, the classes that leak through the
  other, open ends.
- **E5's zero was forced.** A free ℤ₃ orbit is the regular representation, whose determinant is 1. The literature
  puts discrete anomalies in the determinant.

## 2. SM-C7 (B1917, B1919): what is already known

- **Hecke's integral formula** (Hecke, 1917). For a real quadratic field, the partial zeta function of a (ray) ideal
  class is the integral of the real-analytic Eisenstein series along the class's closed geodesic, over one period.
  Yamamoto proved the version for relative quadratic extensions; Bekki proved one for arbitrary extensions.
- **The Kronecker limit at s = 1.** Hecke, Herglotz and Zagier (1975) give it for wide and narrow classes. Yamamoto
  (J. Number Theory 128, 2008) gives it for narrow ray classes, with ζ(0, C) and Shintani's invariant.
- **The odd part.** Meyer expressed the difference between the two narrow classes of a wide class through log η and
  a Dedekind sum; Hirzebruch and Zagier rewrote it through continued fractions. By the functional equation this is
  the value at s = 0.
- **What this means for the record:**
  - SM-C7 steps 1 and 2 restate these theorems in the record's coordinates: the u-shifted Hecke series, and the
    Siegel function's logarithm at s = 1.
  - The record's own content is B1919: B1656's c_s is F_u + π log Im τ − 2π(γ + log π), with F_u the shifted
    Kronecker limit, and its line part averages along the thread to the Kronecker limit.
  - Main may wish to cite Hecke, Meyer and Yamamoto beside B1917, and to place any claim of novelty on B1919 alone.

## 3. The same value as an orientation-odd invariant (a lead; not checked)

- **Atiyah**, "The logarithm of the Dedekind η-function" (Math. Ann. 278, 1987). For a hyperbolic σ in SL(2, ℤ),
  these coincide (as listed in arXiv:1204.1701, Theorem 2.14):
  - Meyer's function;
  - Hirzebruch's signature defect;
  - the transformation law of log η (Rademacher's function);
  - the Shimizu L-function at 0;
  - the Atiyah–Patodi–Singer eta invariant of the mapping torus;
  - the adiabatic limit of eta invariants.
- **Atiyah–Donnelly–Singer** (Annals 118, 1983) and **Müller** (1984): the signature defect of a cusp of a Hilbert
  modular variety is a value of the Shimizu L-function.
- **The twisted case.** Bohn ("On rho invariants of fiber bundles", arXiv:0907.3530, Bonn thesis 2009) computes the
  U(1) rho invariants of hyperbolic torus mapping tori.
  - The flat connections are given by the points ν with (Id − Mᵀ)ν ∈ ℤ². These are the record's characters.
  - The route is Kronecker's second limit formula and a generalized Dedekind eta (Dieter). The result is a finite
    Dedekind-type formula.
  - Only the introduction was read; its Theorem 4.4.20 was not.
- **The Rademacher symbol and the trefoil.** The symbol is the linking number of a modular knot with the trefoil
  (Ghys; Duke, Imamoḡlu and Tóth, Duke Math. J. 166, 2017). For a word in L and R it is, up to a sign convention
  to be checked against the record's, the number of one letter minus the number of the other. It changes sign under the
  mirror, L ↔ R.
- **Why it matters:**
  - These invariants are odd under orientation reversal. They are natural carriers for the hand (E2's bit c), not
    for the pieces' order (E2's O); E2 found the two bits independent.
  - The closed torus bundle is the filling of the record's punctured-torus bundle along the fibre's boundary. That
    is the filling that § 4 shows cannot carry the order, but which can carry the hand.
- **The open check, cheap and decisive.** Does SM-C7's twisted value Z(0, χ_c) equal Bohn's U(1) rho invariant for
  the same M and the same c, up to a stated normalization? Both sides are finite formulas, so the check needs no
  numerics on the population. A card is proposed in § 5.

## 4. E6, the record's index, and duality

**The tool.** Let M be a compact oriented 3-manifold with torus boundary, and V a module of π₁(M).
- The cup product pairs H¹(∂M; V) with H¹(∂M; V*) non-degenerately.
- Write A_V for the image of H¹(M; V) in H¹(∂M; V). Then A_V and A_V* annihilate each other, so
  dim A_V + dim A_V* = dim H¹(∂M; V).
- With trivial coefficients this is "half lives, half dies" (e.g. Putman's note). Kirk and Lesch prove the unitary
  case (Lemma 2.1 of math/0203097). The twisted proof is the same exact-sequence duality.
- The record's modules have h⁰(M; V) = h⁰(M; V*) = 0, since α, β and ℓ are non-trivial.

**(a) Closed manifolds.** Euler characteristic zero and duality give h¹(V) − h¹(V*) = h⁰(V) − h⁰(V*) = 0.
So no filling and no closed gluing can tell V from V* in H¹.
- This is a proof of E6's negative, and of B1351's "a closed join is vector-like", for every such module.
- In the sense of main's new gate (S306p), it is a second route to the same result.
- **The post hoc check:** h¹ after filling is the same for V and V* on all 46 618 modules, including the 384 where
  it is not n + n*.

**(b) Cusped manifolds.** The same steps, with the pair (M, ∂M), give

  h¹(M; V*) − h¹(M; V) = h⁰(∂M; V) − dim A_V = dim A_V* − h⁰(∂M; V*).

- **The post hoc check:** h¹(M; V*) − h¹(M; V) equals the record's I = n − n* on all 46 618 modules. The census:

| I = n − n* | h¹(M; V) | h¹(M; V*) | modules |
|---|---|---|---|
| 0 | 1 | 1 | 39 424 |
| 0 | 2 | 2 | 1 194 |
| +1 | 1 | 2 | 3 000 |
| −1 | 2 | 1 | 3 000 |

- **What this means.** The record's index is the asymmetry of H¹ between V and V*. By (b) it is a boundary
  quantity: the excess of h⁰(∂M; V) over the boundary image of V's classes.
- **One cusp, V non-split there.** Then h⁰(∂M; V) = 1 and H¹(∂M; V) = ℂ², so I = 1 − dim A_V.
  - I = 0 when V's boundary image is a line, as "half lives, half dies" would have it.
  - I = ±1 when all of one side's boundary cohomology lives and none of the other's does.
  - This makes B1457's "flux through an end" precise.
- **Not computed here:** dim A_V. The prediction dim A_V = h⁰(∂M; V) − I is left for SM-C8's run, as a control.

## 5. Proposals for main (each waits for its word)

**SM-C8, three amendments before it runs** (`relays/cards/SM_C8_the-partner-test.md`):
1. **Vacuous joins.** H*(T²; ℂ_χ) = 0 for a character χ non-trivial on the torus.
   - On the covers, a cusp where both α and β restrict non-trivially carries no boundary cohomology, so D = 0 there
     for no reason.
   - Such joins should be listed and left out, or outcome N is inflated.
2. **The quotient line.** Where V restricts to the shared torus T₂ as a non-split extension, H¹(T₂; V) is ℂ² with
   one canonical line, S, the sub's image. The quotient gives no second line in H¹(T₂; V). It gives S* in H¹(T₂; V*),
   and S* is S's annihilator.
   - So the partner's two orders are (V, S) and (V*, S*): which of V and V* the partner meets.
   - Where V splits on T₂, the card works as written.
3. **An index identity, carried as control P3.** For any boundary condition B ⊂ H¹(∂P; V):

   n(V | B) − n(V* | B^⊥) = dim B − h⁰(∂P; V).

   - Dual conditions therefore carry no information. The card's "vanish at the other ends" for V is dual to "free at
     the other ends" for V*.
   - So the order-relevant difference splits into a dimension count and one term, the leak:

     n(V | 0 elsewhere, S) − n(V* | 0 elsewhere, S*)
       = [1 − h⁰(∂P; V)] + [n(V* | free elsewhere, S*) − n(V* | 0 elsewhere, S*)].

   - The second bracket counts V*'s classes, meeting S* at the join, that are alive at the other, open ends.
   - On a one-cusped P there are no other ends. The difference is then 1 − 1 = 0, as "a filling partner cannot".
   - Outcome R on a several-cusped P is then exactly a non-zero leak beyond the dimension count.

**A new card, if main wants it (call it SM-C9):** SM-C7's Z(0, χ_c) against Bohn's U(1) rho invariant of the closed
torus bundle, on the same characters.
- It is finite formulas only, with a plant that flips the orientation (the sign must flip).
- An agreement would make the record's L-function an orientation-odd spectral invariant, a candidate carrier for
  the hand.
- A disagreement would close that reading.

**The spectral route to a partner** (Kirk and Lesch, AGT 3, 2003). For unitary flat connections:
- the eta invariant with a Lagrangian boundary condition W changes with W by m(γV_X, W);
- gluing carries an integer correction, the Maslov triple index (Wall's non-additivity).
That integer is an integer supplied by a relation, B1327's type R, but for the hand's odd invariant. The record's
modules are not unitary, so it does not apply as it stands. It names the natural object for a later card.

## 6. The rest of the fronts

- **E5** (`relays/SM_C6_E5_THE_DECKS_ANOMALY.md`). Araki, Kobayashi, Kubo, Ramos-Sánchez, Ratz and Vaudrevange
  (Nucl. Phys. B, 2008), and later Kobayashi and Uchida (2021), put the anomaly of a discrete symmetry in the
  determinant of its representation.
  - A free ℤ₃ orbit is the regular representation. A 3-cycle is even, so the determinant is 1 and every anomaly
    vanishes, as part 1 found.
  - The Ibáñez–Ross conditions are necessary, not sufficient. The cubic one is shifted by heavy fermions and can be
    met by enlarging ℤ_N.
  - So part 2 should rest on the mixed conditions, not the cubic.
- **E2** (`relays/SM_C6_E2_THE_RANK_OF_THE_BITS.md`). The mirror negates the Rademacher symbol, and E2 found the
  mirror to be negation, up to a shift, on the slopes of every chiral level. Whether the shift is the symbol is not
  checked.
- **B1825's second computation.** The literature cannot answer the firewall question; it still waits on main.
- **The slope law and Burde–de Rham.** A reducible non-abelian representation with diagonal characters exists exactly
  when their ratio is a root of the Alexander polynomial (Burde; de Rham; Heusener, Porti and Suárez for its
  deformations). B1438's n(V) = [s(α) = s(ℓ)] is a condition of the same kind, on twisted cocycles instead of
  Alexander roots. No identity between them is claimed here.

## 7. How this was done

- **Reading.** Web searches, then the abstracts and the parts of papers named in § 8. Bohn was read to the start of
  chapter 1, and Kirk and Lesch through § 6.1. Atiyah's list comes from a secondary source (arXiv:1204.1701).
- **One post hoc check on committed output.** It makes no new computation on the record's objects:
  - `relays/sm_lit/duality_check.py`
  - `relays/sm_lit/duality_check.json`
  - `relays/sm_lit/RUN.txt`
  It reads `relays/sm_c6/e6_results.json` and pairs each module V(ℓ, α) with V(ℓ, ℓ − α) = V*.
- **The derivations in §§ 4–5** follow from the exact sequence of the pair (M, ∂M), Poincaré–Lefschetz duality,
  and χ(M) = 0. They are not reviewed. The identity in § 5.3 and the prediction for dim A_V are untested.
- **The firewall.** Nothing was compared with a measured value. No file M6 names, and no file with agy_ in its path,
  was opened.

## 8. Sources

- [Yamamoto, Hecke's integral formula](https://arxiv.org/abs/math/0602618)
- [Bekki, relative Hecke formula](https://arxiv.org/abs/1712.08392)
- [Yamamoto, Kronecker limit formulas](https://arxiv.org/abs/math/0602615)
- [Zagier (1975)](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/BF01343950/KroneckerLimit.pdf)
- [Atiyah, log of the η-function (1987)](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/atiyahlg.pdf)
- [Meyer functions and signatures](https://arxiv.org/abs/1204.1701)
- [Atiyah, Donnelly, Singer (1983)](https://annals.math.princeton.edu/1983/118-1/p08)
- [Bohn, rho invariants of bundles](https://arxiv.org/abs/0907.3530)
- [Duke, Imamoḡlu, Tóth, linking](https://www.math.ucla.edu/~wdduke/preprints/linking.pdf)
- [Matsusaka, hyperbolic Rademacher](https://arxiv.org/abs/2003.12354)
- [Putman, half lives, half dies](https://academicweb.nd.edu/~andyp/notes/HalfLivesHalfDies.pdf)
- [Kirk, Lesch, rho with boundary](https://arxiv.org/abs/math/0203097)
- [Kirk, Lesch, eta and Maslov](https://arxiv.org/abs/math/0012123)
- [Dubois, Yamaguchi, torsion](https://arxiv.org/abs/0906.1500)
- [Menal-Ferrer, Porti, cohomology](https://arxiv.org/abs/1001.2242)
- [Heusener, Medjerab, reducibles](https://arxiv.org/abs/1402.4294)
- [Araki et al., discrete anomalies](https://arxiv.org/abs/0805.0207)
- [Kobayashi, Uchida, anomalies](https://arxiv.org/abs/2111.10811)
- [Discrete gauge anomalies revisited](https://arxiv.org/abs/1808.02881)
