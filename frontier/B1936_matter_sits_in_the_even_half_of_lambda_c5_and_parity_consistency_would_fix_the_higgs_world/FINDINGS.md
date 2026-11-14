# B1936 — Matter sits in the even half of Λ*(ℂ⁵), and parity consistency would fix the Higgs world as the record's practice

**Verdict: OPEN.** Part 1 is exact. Part 2 is a candidate: its conclusion is exact given its premise, and the premise is
not yet established. Main, 2026-11-14, night, **committed before the run of 2026-11-15 reads any value**, so it cannot
have been chosen after the comparison. Register row P-847. 0 of 19.

## Seen first

- **Swept:** see B1934 and B1935, whose sweeps cover the level-5 Weil representation, SU(5)'s centre and the sectors'
  coincidences.
  - P-847 holds the global bit. Main, X-SCAR (agy-exp), and main's run of W-F16's test found no move of the act and no
    duality that removes it in frame C.
  - The web seat's W-F14 said that only "holomorphy required of a named sector" could fix it.
- **The literature:** standard. One SO(10) generation is Λ^even(ℂ⁵) = 1 + 10 + 5̄ (the 16), and the Hodge pairing
  Λ^k ↔ Λ^{5−k} conjugates. The pairing of hypercharge with exterior degree below is our charges' arithmetic.

## 1. The frame's level-5 charges sort the fields by exterior degree (exact; `degrees.py`)

With the frame's charges (6Y), the degree k = 2·(6Y) mod 5 places:
- Q, u and e at 2 (the 10);
- d and L at 4 (the 5̄);
- the right-handed neutrino at 0;
- the Higgs at 1 (the 5);
- every conjugate at 5 − k.

So one generation's matter lies in the even half of Λ*(ℂ⁵), the 16 of 32, and the Higgs in the odd half. Because 5 is
odd, conjugation flips the degree's parity. **Caveat:** charge mod 5 cannot tell degree 0 from degree 5, so the
singlet's parity is not fixed by charge.

## 2. The candidate: the Higgs world from parity (`higgs_by_parity.py`)

- **The premise.** The frame's holomorphic objects are exactly one parity class of Λ*(ℂ⁵).
  - Matter's kernels are holomorphic and all in one class (§ 1).
  - Conjugation flips holomorphy (S̃ is S with conjugated coefficients) and flips degree parity.
  - So if matter and Higgs sit in one graded Λ*(ℂ⁵), the holomorphic Higgs S shares matter's parity.
- **The conclusion.** Each sector's coupling needs its degrees to sum to 0 mod 5, which fixes the Higgs degree that
  sector needs. The sector whose Higgs shares matter's parity takes S. **For both signs of the hypercharge convention,
  the reading is (up S̃, down S, leptons S): W₋, the record's practice.** The hypercharge sign drops out as a
  convention, and the global bit is fixed.
- **What it would settle.** P-847's global bit, by the form W-F14 named: holomorphy required of a named sector. Parity
  names the sector.
- **What is not established.** The premise. Frame C does not build its Higgs with a charge (the code never uses the
  Higgs's hypercharge), so "one graded Λ*(ℂ⁵) for matter and Higgs" is an assumption about the frame. It becomes a
  construction in the pairs programme's frame D, where the Higgs carries its charge as matter does. Until then this is
  a candidate. It is to be read cold by the web seat (W-F13, W-F14) and by agy-exp (X-SCAR).

## 3. What it does not change
The run of 2026-11-15 keeps its four declared options, as its rule is sealed (B1932). This page is committed before any
value is read, so its standing is decided by the scrutiny of § 2's premise, never by the values. No value computed here.
