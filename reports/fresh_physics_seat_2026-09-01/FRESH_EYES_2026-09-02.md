# Fresh eyes, 2026-09-02 — what the record may not be seeing

Written after the owner's pushback ("try to see what we're not seeing because you have fresh eyes").
Every claim below was checked against the record first (owner rule 1: sweep before an absence claim) and
computed where computable (R53). Each item carries its status: RECORD HAS IT / NEW / COMPUTED.

## 1. The E6/E8 instrument has a two-element image (NEW, COMPUTED — R53 Q1)

The route "field discriminant → conductor N → SL(2,Z/N) → McKay" emits a label only for N ∈ {1, 3, 5}
(checked exhaustively for N ≤ 24; primes > 5 already excluded by B206). Imaginary quadratic fields, the only
shape fields a hyperbolic manifold can have, reach only N = 3. So on the geometry side the instrument says
"E6" or nothing; on the monodromy side it says "E8" or nothing. "Golden hits exactly the two exceptional
McKay primes" (B210) is what the instrument does whenever it speaks. The label carries zero bits beyond
"shape field = Q(√−3)" and "monodromy field = Q(√5)".

## 2. The two sides use different reduction conventions (NEW)

B208 reduces by the integer det(γ+I) = m² + 4 and gets uniqueness at m = 1. B206 and B8118 reduce by the
field discriminant and get the Lucas family m ∈ {1, 4, 11, 29, 76, 199, …} on the E8 side and the 14-member
census family on the E6 side. Any "unique" statement in the record should say which convention it uses;
under the field convention (the one the E6 side needs) nothing is unique.

## 3. Everything m004-specific is two Fibonacci identities (COMPUTED — R53 Q3, Q4)

Within the 14-member Q(√−3) family the sole separator is H1 = Z (B1136). That separator is
det(A − I) = (φ − φ⁻¹)² = 1, and the sister's Z/5 is det(A + I) = (φ + φ⁻¹)² = 5. Both are identities of
the trace-3 monodromy. The 14 carriers are one commensurability class (indices 12, 24, 30 in PSL(2,O_{−3})).
The sister bit is invisible to the field, volume, triangulation, amphichirality, label, and the spin-structure
action (A ≡ −A mod 2). So "the object" that the physics is hung on is: the simplest pseudo-Anosov torus
bundle, characterised by (trace 3, torsion-free). No selection principle in the record reaches that pair
from the founding axiom; the record reaches it by a sieve (P10, B197) whose filters are chosen.

## 4. Amphichirality is a theorem the record owns and should use (RECORD HAS PIECES; R51, R43, R50)

m004, m003 and every carrier checked are amphichiral (symmetry_group().is_amphicheiral(), not the vacuous
mirror-isometry test that B1181/B1186 used). An amphichiral object cannot output a chiral spectrum without
an orientation input. Every chiral-physics statement downstream (hypercharge signs, 16 vs 16-bar, the
"one involution") therefore needs a named orientation choice. The record makes that choice in several
places without naming it as an input. This is a clean, provable, negative structural statement and is the
strongest thing the record could publish about the SM end.

## 5. Where testable content could live (opinion, unchanged)

The Fibonacci / quasicrystal side (metallic-mean spectra, cut-and-project, WRT periods m(m²+4)/gcd) makes
statements a physical system can be compared against (photonic quasicrystals, Fibonacci anyons, spectral
gaps). The SM end makes none. If the program wants one falsifiable target, it is on that side, and it
should be stated as a number with an error bar before any further arc production.

## What I recommend the owner do with this

1. Restate every "selects E6 / unique / hits the exceptional primes" sentence as "has shape field Q(√−3)";
   cite R53 Q1 for why nothing else was possible.
2. Record the convention split (integer vs field) once, in the LAW_MAP or an ERROR_LEDGER row.
3. Treat (trace 3, torsion-free) as an input, not an output, until a derivation from the axiom exists.
4. Publish the amphichirality obstruction as the record's main negative theorem.
5. Pick the one falsifiable target on the quasicrystal side, or withdraw the physical reading.
