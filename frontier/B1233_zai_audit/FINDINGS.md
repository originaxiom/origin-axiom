# B1233 — THE Z-AI AUDIT: 15 confirmed, 7 refuted, one real defect in our own record

cc banking seat, 2026-09-01. Owner: *"where z-ai is wrong and where is right — take every letter
seriously — verify never trust — digest and integrate all."* **Nothing was accepted on report.**

## Confirmed here (30+ digits, or symbolically exact)

| # | claim | status |
|---|---|---|
| 1 | **L(1/φ) = π²/10 = (3/5)ζ(2), L(1/φ²) = π²/15 = (2/5)ζ(2), sum = ζ(2)** | exact |
| 2 | Λ(m) = m²+4 is the **square of the Lagrange number** (τ_m + 1/τ_m = √(m²+4)) | exact, m = 1..7 |
| 3 | Jones: 4cos²(π/5) = φ², 4cos²(π/6) = 3, 4cos²(π/10) = 2+φ | exact |
| 4 | Fricke: tr[A,B] = x²+y²+z²−xyz−2 | symbolic |
| 5 | **the void (2,2,2) is a (2,1) saddle at κ = 0**; (0,0,0) is the **global minimum**, κ = −4, signature (3,0) | symbolic |
| 6 | Riley: tr[A,B] = v²+2; at v²−v+1 = 0 → √3·e^{±iπ/6} — **our banked B285 exactly** | exact |
| 7 | integer points of x²+y²+z² = xyz are **3× Markov triples**; the twist z→xy−z preserves it | verified |
| 8 | h(−3) = 1, h(5) = 1, h(−15) = 2 | verified |
| 9 | **2 is inert in both ends, splits only in the meeting field** | verified |
| 10 | genus field of −15 = ℚ(√−3,√5) = the Hilbert class field | verified |
| 11 | j(√−3) = 54000 exactly | verified |
| 12 | disc −15 j-pair: sum −191025, product −121287375 | verified |
| 13 | Λ(1),Λ(3),Λ(5) Markov; **Λ(7) = 53 is not** — pattern dies, as they said | verified |
| 14 | spin structures on m004 = 2 | verified |
| 15 | c(g₁) = rank, simply-laced | our own earlier check |

**The dilogarithm partition is the substantive one:** the golden grammar splits a weight-2 period
into two **forced rational weights**, 3/5 + 2/5 = 1.

## Refuted

**R1 — "for m004's cusp τ = 2√3i (or ω), so j = 0."** **False.** j(2√−3) = **2,835,807,690.42**.
j = 0 sits at ρ — **m003's** cusp shape. The parenthetical *"(or ω)"* smuggled in the **sister** and
did all the work. Same conflation class this session has been cataloguing.

**R2 — "at the q = 1 cutoff, j → 744 exactly."** Not a cutoff. q = e^{2πiτ} = 1 at τ = 0, where j
**diverges**. Writing 744 there is dropping every term but the constant.

**R3 — "k = 1 is the minimal level; your minimality principle closes it."** This is **exactly** the
default-value-from-absence error codex refuted and this bench **retracted two hours earlier**
(B1232). Minimality is not a receiver.

**R4 — "the disc −15 j-values are quartic."** **False — quadratic.** Sum and product are rational
integers, so [ℚ(j):ℚ] = 2. Their own numbers refute their conclusion.

**R5 —** H₋₁₅ written with constant term **+**121287375; the product of the roots is **negative**.

**R6 — "Morse–Hedlund: minimal aperiodic word = the Fibonacci word."** Imprecise: Morse–Hedlund
gives the **Sturmian class**; the golden slope needs Hurwitz on top. **Our own P019 erratum already
records this.**

**R7 — the headline: "the observer's bit IS the ideal class of ℚ(√−15)." REFUTED, not merely
unearned.** In V₄ = Gal(ℚ(√−3,√5)/ℚ), complex conjugation **fixes √5** (it is real) and flips √−3;
the class-group generator fixes √−15 = √−3·√5 and therefore **flips both**. **Different elements.**
B1174 already proved our four ℤ/2's are *one* involution c = complex conjugation; the class bit is a
**fifth** thing — and √5 isn't even in ℚ(ζ₁₂) (quadratic subfields ℚ(i), ℚ(√3), ℚ(√−3)), so it lives
in a V₄ our banked V₄ does not contain. Registered **I-8, REFUTED**.

## The one real defect — and it is theirs to claim

**A κ convention split inside our own repo.** `papers/P3_THE_PAPER/main.tex:696` defines
**κ(A,M) = tr[A,M] − 2**; the frontier record (B285, B126, B330, B131, `frontier/README`) uses
**κ = tr[A,B]** raw. The founding value is **ω** under one and **2+ω = √3·e^{iπ/6}** under the other.
Both are in the repo. **Harmonization owed.**

## Adopted as readings

- **The Morse landscape**: the void is **not** the ground state — an unstable saddle with two ascent
  directions; the global minimum is the **quaternionic** point (0,0,0), on the Markoff surface.
- **The Chowla–Selberg closure**: class-field values = algebraic units × universal transcendentals —
  the **product of two layers already closed**, so the "unsearched third layer" needs no scan.
- **The false-positive attractor species {3/8, 3/2, 3/5}** — low-height rationals with 3 in the
  numerator. That is what every near-miss in this programme has been.

## The convergence

Their *"consistency forces the discrete; the continuous is the residue"* and this bench's independent
finding the same day are the same result: **every derived item in our record is discrete, rational or
torsion; every underived item is continuous. Zero exceptions either way.** Two seats, one day, one
boundary — and the mechanism is now sayable:

> **The deriving machinery is arithmetic** — anomaly cancellation gives integers, kernels give finite
> groups, amphichirality gives torsion, trace identities give rationals — **and arithmetic cannot
> emit a continuum.**

## Reproduce

`sh frontier/B1233_zai_audit/reproduce.sh` — all 14 assertions, confirmations *and* refutations.
