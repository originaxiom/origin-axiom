# B385 (D3(a) residue) — PRE-REGISTRATION: the bright/dark pair discriminator

**Committed before computation. Target: the last open D3 item — a criterion on (m₁,m₂)
reproducing bright {(1,2),(2,3),(2,4),(3,4),(1,7),(3,7),(2,7)} vs dark
{(1,3),(1,4),(3,5),(1,5),(4,5)}; acceptance riddle: (1,3) dark vs (3,4) bright.**

## The new tools (why this is attackable now)

γ(W_m) = [[1+m², m],[m, 1]] mod 15 (derived from P64's intertwining legs; verified against
both banked γ's). The pair's Par-table is governed by the trace formula through the group
elements −γ_{m₁}^j γ_{m₂}^l (P64), and darkness = the vanishing of the table's anti-part
(√−3, √−15 components) at every graded window (P65 mechanism, now table-wide).

## T1 — the group-invariant hunt (registered bet)

For each of the 12 pairs compute G = ⟨γ_{m₁}, γ_{m₂}⟩ ≤ SL(2,ℤ/15) and tabulate: |G|; the
CRT images |G mod 3|, |G mod 5|; whether −I ∈ G (each factor); the multiset of det(−g−I)
classes over g ∈ G; the QR class of the images. BET: some single group invariant separates
bright from dark 12/12 — the primary candidate is a mod-5 image property (the 5-side carries
the seam's √5; P63's 5-side QR mechanism; P64's class-5 boundary carrying 1/48).
KILL: no tabulated invariant separates ⇒ darkness is NOT γ-group-theoretic; bank the table
and the negative (the criterion then needs character-level data — named next layer).

## T2 — the criterion statement + the riddle test (conditional on T1)

If an invariant separates: state the criterion in arithmetic form (an (m₁,m₂) congruence /
QR statement), re-verify on all 12 pairs from the criterion alone, and spell out the
(1,3)-vs-(3,4) resolution mechanism. Verify against one OUT-OF-SAMPLE pair if any banked
table exists beyond the 12 (else name the prediction for the next-computed pair).

Machinery: pure 2×2 mod-15 group enumeration (cheap, exact). Firewalled level-15 statements.
