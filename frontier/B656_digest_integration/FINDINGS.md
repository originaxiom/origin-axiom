# B656 — THE DIGEST-QUEUE INTEGRATION: cc2's G1–G5 verified and banked
# (main seat, 2026-07-17; packet seals 7/7; independent verification
# verify_g1_g4.py → verify_g1_g4_out.txt)

The coordinated digest queue (registered in B654's adjudication: G1–G5,
no duplication across seats) came back as one packet (prereg 5848c32d,
packet seals verified 7/7 on receipt; disclosed privacy patches in
ORIGINALS_MANIFEST.txt). Verdicts, most consequential first:

## G4 — CONFIRMED INDEPENDENTLY (12/12): THE CONDUCTOR-CLOCK LAW

cc2's claim: B596's "lawless" multiplier table is exactly
**clock(κ) = ord(A₁ mod 3κ)** — the naive modulus κ was wrong, the
conductor 3κ (= ord T at level κ−3) is right; the "non-uniform
multipliers {½, 1, 3/2, 2}" were conductor-vs-κ arithmetic all along.

This seat's verification (fresh order code vs the banked clock
machinery, all rows):

| κ | clock | ord(A₁ mod 3κ) | verdict |
|---|-------|----------------|---------|
| 4 | 1 | 12 | anomaly zone (dim-1 θ-odd block; character-blind) |
| 5 | 10 | 20 | anomaly zone (the half-period; Q2's abelian-twist-blind core) |
| 6–15 | — | — | **EXACT, 10/10** (12, 8, 12, 36, 60, 20, 12, 28, 24, 60) |

Consequences (banked):
- **B596's table row upgrades DATA → DERIVED.** The null-with-structure
  ("Pisano-anchored, not a uniform function of κ") stands as history;
  the law behind it is the conductor. B596 FINDINGS carries the
  addendum.
- **L84's sharpened clause ("any functorial map must explain the clock
  multipliers") is DISCHARGED** — by the identified functor itself:
  mod-conductor reduction produces every multiplier. Pairs with B650's
  order-level completion of the trace/det dictionary.
- The two anomaly rows are the clock law's OWN anomaly-zone clauses
  (κ=4: the antisymmetrization destroys order — clock 1 vs ord 12;
  κ=5: exactly the half-period — clock 10 vs ord 20), not exceptions
  to a different law.

## G1 — CONFIRMED INDEPENDENTLY (fresh group, fresh words):
## THE SIGN-HEARS-THE-DISCRIMINANT THEOREM

cc2's theorem (even-rank form): for B_w = tI − w − w⁻¹ over a Weyl
group on an even-rank lattice, **det(w) = (−1)^{v_p(det B_w)} for
every w IFF v_p(disc A) = v_p(t²−4) is odd**; for even v_p the
agreement is exactly the sign-balanced half. Proof: det B_w =
±∏ f(ζ) with f(x) = x²−tx+1; f(−1) = t+2 = det(A+I), f(1) = 2−t =
−det(A−I); conjugate eigenvalue pairs contribute evenly; on even rank
mult₊₁ ≡ mult₋₁ (mod 2). cc2's battery: 207,384 cases (W(E6)×W(A2),
four sealed words), 0 exceptions, with two of its own naive sealed
predictions honestly corrected by the theorem.

This seat's verification — a Weyl group NOT in the discovery battery
(W(D4), order 192) and two words never run (t=4, disc 12; t=8,
disc 60), plus a v_p=0 control prime (13) on every word:
every odd-valuation prime tracks **192/192**; every even case
(including v_3(45)=2, v_2(12)=2, v_2(60)=2 and all controls) sits at
**exactly 96/192**. The theorem generalizes beyond its battery.

Consequence: the identity card's det(A±I) (B654) is not bookkeeping —
it is the exact quantity the Weyl-sign structure hears, at every
prime, with the parity of the discriminant's valuation as the switch.
Unifies the P1 jewel, the sector halves, and the mirror quantity
(G3's B_id has det = det(A₁+I)⁶). New LAW_MAP row.

## Q-AREA (this seat's cell, landed with the packet): THE FACTOR 2
## IS UNIVERSAL — the area law is REFUTED

Both lawful silver triples (134, 023): **defect = 2·conj(Y) exactly;
defect = 4·conj(Y) is FALSE.** The fig-8's chain-defect factor 2 is
NOT its commutator area (fig-8 area 2, silver area 4 — the factor
stays 2). The B647 cell-2 defect law is object-independent:
a universal cocycle factor, not a van Kampen count. Bonus: the silver
defect lies entirely in the s-free coordinates — in ℚ(i), the
object's imaginary quadratic subfield — the subfield law (B654) again.
Banked in B654's FINDINGS + q_area_output.txt; fraction-level lock in
tests/test_b654_listening.py.

## G3 — ACCEPTED (gate 13/13 vs the banked P4 column; arithmetic
## retro-check by this seat)

The mirror generic law: Z₋₃(r) = ((r|5) − 1)/2 = −Z₊₃(r) for r coprime
to {2,3,5,7,17} (certified r = 13, 29, 31, 37; all 7 generic points).
The sector-carry synthesis: tr_even = (Z₊ + Z₋)/2 vanishes on doubly
generic rungs ⇒ the even sector carries a unit iff the mirror channel
resonates. Retro-explains P4's killed inert⟺even correlate — checked
arithmetically here: the correlate's 3/3 hits (15 = 3·5, 17, 20 = 2²·5)
are all mirror-resonant; its killer 23 is inert but coprime to
{2,3,5,7,17} — the false pattern died exactly where the true law
separates from its shadow. Both the pattern and its killer are now
theorems of the channel laws.

## G2 — ACCEPTED AS REDUCTION (the exact resonant period stays priced)

From the certified structure: the GENERIC subsequence of the ladder
has minimal period exactly **5 = disc(A₁)** — the same period the
record proved for the SU(2) figure-eight ladder (B204: P(m=1) = 5).
Two stages, one period, one discriminant — L24(c)'s first cross-stage
data point, internal. The full minimal period divides N₀ and is a
multiple of 5; its exact value awaits the resonant-phase law
(one more certification cell — machinery exists; priced, not claimed).

## G5 — ACCEPTED AS REDUCTION THEOREM (universality priced)

For ANY once-punctured-torus bundle with the 27-dim system and its
double (χ = 0, Poincaré duality via the banked intertwiner J,
Mayer–Vietoris + half-lives-half-dies on the cusp torus): the entire
dimension grammar {h⁰(M), h¹(M); h⁰(D), h¹(D)} is determined by TWO
local inputs — i₁ = dim V^holonomy, i₂ = dim V^{peripheral ℤ²}. With
(i₁, i₂) = (1, 3): h¹(M) = 3, h⁰(D) = 1, h¹(D) = 5 — the banked golden
values AND the silver reproduction. The 3/5/1 grammar is
monodromy-independent whenever (i₁, i₂) are; what remains (honest,
one bounded cell) is proving (i₁, i₂) metallic-uniform.
**Q-BLOCK reframed:** for the adjoint 78 the question is now just
(i₁, i₂) of the 78 — the reduction does the rest.

## Ledger deltas

LAW_MAP: new rows (sign-hears-the-discriminant; conductor-clock;
mirror generic + sector-carry; generic-period-5; dimension-grammar
reduction); the defect-factor row rescoped to UNIVERSAL. OPEN_LEADS:
L84's multiplier clause discharged; new leads L100 (resonant-phase
law), L101 ((i₁,i₂) metallic-uniformity). B596: DATA → DERIVED
addendum. Locks: tests/test_b656_digest.py, tests/test_b654_listening.py.
