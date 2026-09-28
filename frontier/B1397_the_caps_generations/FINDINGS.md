# B1397 — THE CAP'S GENERATIONS: a flux cap's chirality is linear in the charges, so its spectrum is anomaly-free exactly when the flux is orthogonal to hypercharge. It cannot cancel the frame's anomalous count, only replace it. The net number of generations it gives is even in every E₆ frame, any integer in the E₇ frame, and zero in the E₈ frame. So three generations cannot come from flux caps in the record's own E₆ frame. In the E₇ frame, three is the degree of a flux along E₇'s own U(1), which is an input.

**Date:** 2026-09-28 · **Seat:** cc (the SM-derivation branch) · **Occasion:** after B1396. B1395's one finite-energy charge-odd
datum is a flux on a capped cusp torus, and B1389's third job is that a completion must carry the frame's gauge anomaly. What does a
flux cap actually give? · **Status:**
- PROVED: the cap's index rule and the anomaly identity (Riemann–Roch on a torus; the absence of a quartic Casimir in E₆, E₇, E₈), and
  the generation counts (the frames' charges and flux lattices).
- COMPUTED: every frame and 625 flux directions, exact over ℚ, with B1389's vectors.

**Not sealed** (§1). **Fence:** the seat's frames (B1389); the cap as in B1396 (a torus carrying the charged sectors' bundles
tensored with a line bundle); the flux commuting with the Standard Model and with SL(2)_β's cusp holonomy. · **Price:** unchanged,
0 of 19 · **Numbering:** B1397.

## 0. Seen from above

- **The rule.** On a capped cusp torus carrying a U(1) flux F of degree n, every charged sector μ has net chirality ⟨F, μ⟩·n. That is
  its Riemann–Roch index: a flat bundle on a torus has degree 0, and the flux adds ⟨F, μ⟩·n per unit rank.
  - SL(2)_β doublets count here, unlike in the frame's bulk rule, which gives them 0 (B1389).
  - The frame's bulk rule was sign(⟨H, μ⟩)·N. The cap's rule is the same with the sign replaced by the charge itself.
- **Linear means anomaly-free.** E₆, E₇ and E₈ have no independent quartic Casimir. So every Standard-Model anomaly of a spectrum
  linear in the charges is proportional to tr(F·Y), and it vanishes exactly when the flux is orthogonal to hypercharge.
  - B1389's frames failed because sign(·) is not linear.
  - A flux cap adds no anomaly, so it cannot cancel the frame's. A capped completion replaces the frame's count with its own.
- **What it gives.** With F orthogonal to Y, the spectrum is complete SU(5) multiplets, and the net number of generations g is:

| frame | flux directions (⊥ Y) | net generations g | achievable |
|---|---|---|---|
| F78 (7d E₆ super-Yang–Mills) | dγ | 2dn | even |
| F27 | dγ | −2dn/3 (dn ∈ 3ℤ) | even |
| F27+78 | dγ | 4dn/3 (dn ∈ 3ℤ) | multiples of 4 |
| F133 (E₇ ⊃ E₆ × U(1)_t) | dγ + e·t | (4d/3 + e)·n | every integer |
| F248 (E₈ ⊃ E₆ × SU(3)) | dγ + h (h in SU(3)'s Cartan) | 0 | zero |

- **So in the record's own frame (E₆) three is impossible from flux caps.** The 10s of the 78 sit in SL(2)_β doublets, so they
  come in pairs. The 27's 10s carry γ = −2/3, and its flux must be a multiple of 3.
- **The E₇ frame can give any number.** Its U(1) flux gives n chiral 27s, so three is possible there as the flux degree, an input.
  At a rotated Eisenstein cusp, under B1396's continuity, every sector's flux degree is a multiple of 3. The smallest symmetric E₇ cap
  then gives exactly three generations. Where a sector's flat line sees the cusp, its three modes are ℤ/3's regular representation
  (B1396).
- **E₈ gives none.** A flux commuting with SU(5) lies in SU(5)′, and its trace over the five copies of the 10 vanishes.

## 1. Why this arc was not sealed

The outcome was derived by hand from the frames' charges and the Casimir identity. Then a probe with B1389's vectors checked the hand
values: F78 with γ gives 2, F133 with t gives 1, F = Y is anomalous. Only after that was this instrument written. Nothing was open by
the time anything was computed, and nothing was chosen on a result. The scan below verifies the hand formulas; it does not test them.

## 2. The statements

**Setting.**
- The frames are B1389's: the SM inside SU(5) ⊂ SU(6), with E₆ ⊃ SL(2)_β × SU(6); the 78 = (3, 1) + (1, 35) + (2, 20) and the
  27 = (1, 15) + (2, 6̄). γ is the U(1) of SU(6) ⊃ SU(5) × U(1), in the record's normalisation (B1368): the 15's 10 at −2/3 and its 5 at
  4/3.
- F133 adds E₇'s U(1)_t with 133 = 78₀ + 1₀ + 27₁ + 2̄7₋₁. F248 is E₈ ⊃ E₆ × SU(3) with 248 = (78, 1) + (1, 8) + (27, 3) + (2̄7, 3̄), as
  in B1389's post-seal E₈ frame.
- The cap (B1395, B1396). A cusp torus T_c carries, for each sector μ, the bulk's flat bundle restricted to T_c, tensored with
  ℒ^{⟨F, μ⟩}, where ℒ is a line bundle of degree n.
- F must commute with the Standard Model, which stays unbroken. It must also commute with SL(2)_β's parabolic cusp holonomy, the frame's
  geometric representation (B1368). A flux along SL(2)_β's Cartan would need a split bundle on T_c, where the bulk's is non-split. So
  F lies in the Cartan of the commutant: span(Y, γ) in E₆, plus t in E₇, plus SU(3)'s Cartan in E₈.

**(1) The cap's index is linear.** The net chirality in the SM representation of sector μ is ⟨F, μ⟩·n. For a spin-0 sector the
bundle has rank 1. For an SL(2)_β doublet it is the geometric representation's rank-2 flat bundle, whose cusp holonomy is parabolic
and whose degree is 0, twisted by ℒ^{⟨F, μ⟩}. Its index is 2⟨F, μ⟩n, one ⟨F, μ⟩n per weight.
- *Proof.* Riemann–Roch on a genus-one curve: index = degree, and degree is additive with deg(flat) = 0. The two weights of a doublet
  carry the same F-charge because F commutes with SL(2)_β. ∎
- Each ± pair of weights is counted once, as in B1389. The reps present are self-conjugate as a whole: the 27 with the 2̄7, and the real
  adjoints.

**(2) Linear means anomaly-free, exactly for F ⊥ Y.**
- For every SM anomaly (SU(3)³, SU(3)²Y, SU(2)²Y, Y³, gravitational–Y), the cap's coefficient is n·STr_R(F T_a T_b T_c) summed over
  the frame's representations R, with T's in the SM.
- E₆, E₇ and E₈ have no independent quartic Casimir: their Casimir degrees are 2, 5, 6, 8, 9, 12; 2, 6, 8, 10, 12, 14, 18; and 2, 8,
  12, 14, 18, 20, 24, 30. So tr_R(X⁴) = c_R (tr X²)², and polarising gives STr_R(F T_a T_b T_c) = c_R·Σ tr(F T)·tr(T T) over the three
  pairings.
- tr(F T) vanishes for the non-abelian SM generators, since F commutes with them. So every anomaly vanishes exactly when tr(F Y) = 0.
- Witten's SU(2) anomaly also vanishes: the doublets come in complete generations and vector-like pairs. ∎
- **Consequences.** A flux with a hypercharge component makes the X,Y partners (3, 2)₋₅/₆ chiral and leaves Y-anomalies, so it is out.
  A flux orthogonal to Y adds no anomaly, so a cap cannot cancel B1389's. A consistent capped completion must replace the frame's
  count, not add to it.
- **Why the frame's own count failed.** A step function of the charge is not linear. The capped completion does no worse: its walls
  are charge-blind (B1393, B1395 (d)) and its chirality is the flux's.
- The U(1)_F anomalies themselves (F·SM², F³, gravitational–F) do not vanish in general. U(1)_F is made massive by a Green–Schwarz
  axion, as B864 requires of every abelian direction other than hypercharge.

**(3) The generation count.** With F ⊥ Y, F commutes with SU(5). The spectrum is then complete SU(5) multiplets, and anomaly freedom
makes net #10 = net #5̄ = g, with vector-like 5 + 5̄ pairs and singlets aside. Counting the 10s:
- **78 (the (2, 20)).** The 20 = 10 + 1̄0 with the 10 at γ = +1, in an SL(2)_β doublet, gives 2dn.
- **27 (the (1, 15)).** The 10 at γ = −2/3 gives −2dn/3, plus e·n in F133 (t-charge 1), or plus h_i·n for copy i in F248.
- **The flux lattice.** Every index must be an integer. The 78's γ-charges are integers (0, ±1, ±2), so dn ∈ ℤ. The 27's are
  ≡ 1/3 mod 1, so dn ∈ 3ℤ once the 27 is present. In F133 the lattice is dn ∈ ℤ and (d/3 + e)n ∈ ℤ. In F248 it is dn ∈ ℤ and
  (d/3 + h_i)n ∈ ℤ.
- **Hence:**
  - F78: g = 2dn is even.
  - F27: g = −2dn/3 ∈ 2ℤ.
  - F27+78: g = 4dn/3 ∈ 4ℤ.
  - F133: g = (4d/3 + e)n = dn + (d/3 + e)n ∈ ℤ, and every integer occurs. F = t with n = g gives g chiral 27s.
  - F248: g = 2dn + Σ_i(−2d/3 + h_i)n = Σ_i h_i n = 0. ∎

**(4) At a rotated cusp.** Under B1396's continuity the flux bundle's weights at the rotation's three fixed points are trivial, so
every sector's flux degree ⟨F, μ⟩·n is a multiple of 3.
- In the E₇ frame that gives g = dn + (d/3 + e)n ∈ 3ℤ, and the smallest non-zero value is three.
- Whether a sector's three modes are ℤ/3's regular representation is B1396's question for that sector's flat line: they are where
  the line sees the cusp. B1396 proves this for rank-one lines; SL(2)_β doublets are not covered.
- In the E₆ frames g is a multiple of 6 at such a cusp (of 12 in F27+78).

## 3. The verification (`verification/cap_generations.py`; record `cap_generations_run.txt`, data `cap_generations.json`)

**Banked identity, run first.**
- B1389's own controls pass, and the 78 has 36 root pairs.
- F78 with F = γ, n = 1, gives exactly two generations.
- F133 with F = t, n = 1, gives one net generation plus a vector-like 5 + 5̄.

**The hand cases** (minimal integral n):

| frame | F | n | anomaly-free | X,Y chiral | g |
|---|---|---|---|---|---|
| F78 | γ | 1 | yes | no | 2 |
| F27 | γ | 3 | yes | no | −2 |
| F27+78 | γ | 3 | yes | no | 4 |
| F133 | t | 1 | yes | no | 1 |
| F133 | γ − t/3 | 1 | yes | no | 1 |
| F133 | γ + 2t/3 | 1 | yes | no | 2 |
| F248 | γ + (1, −1, 0) | 3 | yes | no | 0 |
| F248 | (1, 1, −2) | 1 | yes | no | 0 |
| F78 | Y | 6 | **no** | yes | — |
| F27+78 | Y + γ | 6 | **no** | yes | — |

**The scan.** 625 flux directions over the five frames: a ∈ {0, 1, −1/2}, b on a grid of 15 rationals (x/y with |x| ≤ 3, y ≤ 3),
and six values of c for F133 or five Cartan elements h for F248. Each is analysed at its minimal integral n and at 2n and 3n: 1 875 rows, **0 failures**. The
checks:
- anomaly-free exactly when a = 0 (F ⊥ Y);
- no X,Y chirality and no exotic at a = 0;
- g equal to the hand formula of (3) whenever a = 0.

Achievable g over the scan:
- F27: even values only, up to ±12.
- F78: even values only, up to ±18.
- F27+78: multiples of 4 only, up to ±24.
- F133: every integer from −18 to 18, and others beyond.
- F248: {0}.

## 4. What this settles, and what it does not

**Settled.**
- **The capped route in the E₆ frame cannot make three.** Its generations come in pairs: the 78's 10s are SL(2)_β doublets, and the
  27's flux quantum is 3.
- **A cap cannot cure B1389's anomaly.** A capped completion is consistent only by replacing the frame's count.
- **Three from caps needs E₇'s U(1).** There the number is the flux degree, an input. At a rotated cusp the smallest symmetric value
  is three.
- **E₈ caps are vector-like.**

**Not settled.**
- **Whether physics caps the cusps at all.** Sources remain (the lane's R24/R28).
- **Where an E₇ U(1) would come from in this geometry.** The record's E₇ points (B1353, B1360) are candidates, not derived.
- **Why three.** Nothing here selects a flux degree.

0 of 19.

## 5. Fences

- **The frames and their charges are B1389's** (B1368's vectors). The generation count reads net 10s in complete SU(5) multiplets.
- **The cap's physics is not derived.** Chiral zero modes on a torus carrying the charged sector's bundle are B1396's model, and B1395
  §3's Hořava–Witten reading is not used.
- **A single flux direction per cap.** Several caps add their counts, so parity is preserved in the E₆ frames.
- **F commutes with SL(2)_β's parabolic cusp holonomy.** A cap whose own structure breaks SL(2)_β is outside.
- **The lattice is the frame's representations'.** With a 56 of E₇ or other matter, the lattice would be finer.

## 6. Prior art

Swept before banking:
- `scripts/checks/already_banked.py "flux induced chirality anomaly free quartic Casimir cap torus generations"` and "flux generations
  even E7 U(1) 27 cap torus Riemann-Roch".
- `git grep` on main (`987c0c8f`), the audit lane (`aff8a569`) and this branch, for flux-induced chirality, the quartic Casimir,
  generation parity and E₇'s U(1) flux.

**Found.**
- F-theory hypercharge-flux references (Donagi–Wijnholt), cited on main's and this branch's literature pages.
- This branch's "pullbacks give 2·degree, always even" (a different mechanism: the pullback three).
- The Pin/CP parity statements (B1382, B1383), another route to an even count.
- Main's "|Fix on the cusp| = 2·(#fixed lines)".

None states the cap's generation count or its anomaly.

**The literature.** Standard, no novelty claimed for the rules:
- flux-induced chirality on a torus (Riemann–Roch);
- anomaly freedom of spectra linear in the charges in groups with no quartic Casimir;
- E₇ → E₆ × U(1) with a U(1) flux giving n 27s (the heterotic and F-theory staple).

The parity statement for the seat's E₆ frame, and its reading against B1389's anomaly, are this branch's.
