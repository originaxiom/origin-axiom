# B2012 — Listening 27: the blind re-listen, compared with the record — of its twenty observations four were on the record, six sharpen it, eight are new, and two are split; every new one main checked holds, among them a universal pairing law that belongs to the modular group, not the whole

**Verdict: PROVED for its checks (exact: FLINT over the integers; mod 135 modulo three primes; sympy; exhaustive counts;
M2a failed as worded, M2b held).** Main, 2026-11-26, in the author's /loop "continue the listening line". Data-free. 0 of 19.

## Seen first

- **The record's side of the comparison:**
  - B1983 (the leaves over every finite field) and B1989 (the finite orbits over ℂ, with the binary dihedral families
    owed);
  - B1990 (the point counts' four values), B1993 (the cusp's integer readings) and B2000 (the linearisations);
  - B2004 (the modular group, W = T − D), B2008 (the mirror) and B2011 (the mixed level mod 135).
- **Swept, one line per theme:**
  - `VERDICT topic-sweep /two-subspace|principal angle|lambda \+ 2|f\(x ?- ?2\)/: 0 of 1753 arcs on main match (none); 0 register rows match (none)`;
  - `/point count|#X|points mod p|p\^2 \+ .*p \+ 1|Legendre/`: 7 arcs (B1990 the relevant one);
  - `/finite orbit|exceptional orbit|16-point|72-point|algebraic solution|Painlev/`: 11 arcs (B1989 the relevant one);
  - `/Hasse|integer point|no integral|local-global/`: 3 arcs, none on the moves;
  - `/k ≡ 5 mod 8|two halves|2-adic halves/`: 6 arcs, none on the moves.
- **The literature (standard, cited from memory, not checked at source):**
  - Halmos's two-subspace theorem;
  - point counts and strong approximation on Markoff-type surfaces (Bourgain, Gamburd and Sarnak; W. Chen);
  - Hasse failures for integer points on them (Ghosh and Sarnak);
  - the finite orbits (Dubrovin and Mazzocco; Lisovyy and Tykhyy; Cantat and Loray).

## The listener

- **What it was given:** only the system's statement: F2, L: b ↦ ab, R: a ↦ ab, the action on (x, y, z), and
  k = x² + y² + z² − xyz.
- **Our arcs:** it did not read them.
- **Priming:** it disclosed that its context showed the memory index and five commit subjects before it started. Those
  name S₄, S₃ × ℤ₃, mod 27, mod 729, the halving and the swap of the readings.
- **What it chose:**
  - the four-move sum T₄ = L + R + L⁻¹ + R⁻¹;
  - every leaf mod every prime up to 71, prime powers and mixed moduli, finite orbits over ℂ, and integer leaves.
- **Where its work is:** its scripts and outputs are in `verification/listener/`, copied unchanged.
- **Conventions:** its k is κ + 2, with κ main's level, so k = 0 is the cusp and k = 4 is "nothing".

## The comparison (the table is the result)

| listener | observation | on the record? | main's check here |
|---|---|---|---|
| B1 | the moves act through ℤ₂ * ℤ₃; the mirror swaps L and R; the sign changes are permuted | **ON RECORD:** B2004, B2008, B1993 (primed) | — |
| B2 | fixed points (0,0,0) and (2,2,2); the two singular leaves | **ON RECORD:** the common point and "nothing" (B1988, B1990) | — |
| B3 | the linearisation at the origin generates S₄, PSL(2, p) mod p, and predicts the orbits mod p² over each fixed point | **SHARPENS:** B2000 (Jacobians), B1985 (the neighbourhood), B2006 (S₄, primed) | — |
| B4 | a 6-point orbit {(±t,0,0), …} on every leaf k = t² | **NEW:** B1989 named the binary dihedral families as owed | **N2 holds** |
| B5 | on k = 4 the finite orbits are the torsion orbits, all congruence | **SHARPENS:** B1989's level-2 orbits, B1990's p² + 1 | — |
| B6 | five finite orbits off k = 4 (16, 36, 72, 40, 40) | **ON RECORD:** exactly B1989's 2T, 2O, 2I orbits, found independently | — |
| B7 | their genus 0, levels 12 to 60, none congruence | **NEW** | not checked |
| B8 | their T₄ spectra, mostly integers and ±2 | **NEW** (a consequence of B16) | not checked |
| B9 | #X_k(𝔽_p) = p² + p(3χ(k − 4) + χ(k(k − 4))) + 1 | **SHARPENS:** B1990 had the four corrections, not which leaf takes which | **N3 holds** (every k, 3 ≤ p ≤ 71) |
| B10 | each leaf mod p is the reductions of the finite orbits plus at most one orbit (619 leaves) | **SHARPENS:** B1983 (the cusp's leaf one orbit; others split) | **M1:** one instance holds |
| B11 | the sign changes give blocks; Alt or Sym on the blocks | **NEW** | not checked |
| B12 | the large orbits' genus and level mod p | **NEW** | not checked |
| B13 | the p-adic shells around a finite orbit are single orbits | **SHARPENS:** B1985, B1987 (shells over the common point) | not checked |
| B14 | large orbits lift whole from p to p² for p ≥ 5; not at 2 and 3 | **SHARPENS:** B1987, B1996 | not checked |
| B15 | two equal orbits on the leaves k ≡ 5 mod 8 at every 2-power; the 3-adic leaves fragment | **NEW** for 2 (the separating quantity is unknown); 3 ON RECORD in kind (B2005, B2006) | **N8 holds** |
| B16 | T₄'s spectrum pairs λ with λ + 2, by the two-subspace theorem | **NEW** (0 arcs) | **N1 holds** |
| B17 | λ₂ > 2√3 on 80 large orbits: not Ramanujan | **NEW** for T₄ (B1996's slow decays are for P_L + P_R over the common point) | not checked |
| B18 | mixed moduli split along a common finite quotient | **NEW** | not checked |
| B19 | integer leaves: k ≡ 3 mod 4 and k ≡ 3, 6 mod 9 never attained; 15 leaves solvable everywhere with no point found | the k = 0 orbits ON RECORD (B1993); **the rest NEW** | **N6a, N6b hold** |
| B20 | the singular leaf mod p is the origin and one orbit of p(p + 3χ(−1)) | **ON RECORD:** B1983, B1990 | — |

- **The count:**
  - ON RECORD: 4 (B1, B2, B6, B20).
  - SHARPENS: 6 (B3, B5, B9, B10, B13, B14).
  - NEW: 8 (B4, B7, B8, B11, B12, B16, B17, B18).
  - Split: 2. B15's 2-adic halves are new, its 3-adic fragmentation on record. B19's k = 0 orbits are on record, its
    congruences and Hasse leaves new.
- **What main heard that the listener did not:**
  - the six-move covariant unfolding and ω's 1 + 2 (B2000, B2001);
  - the halving on the 3-tower, its derivation, its exceptions, and its failure at mixed levels (B2002 to B2011);
  - the small group G_k (B2005 to B2007);
  - the rate law over the common point at the primes 3, 5 and 7 (B1997, B2011);
  - the mirror's lock as a theorem (B2008; the listener saw only that τ swaps L and R).

## Main's checks (expectations hashed before the run)

| id | result |
|---|---|
| N1 | **holds** (`blind_checks_run.txt`). T₄ = S(C + C²) + (C + C²)S pointwise on every orbit, so T₄ = 3(SP + PS) − 2S. The characteristic polynomial is exactly R(x + 4) R(x + 2) (x − 4)^{d₁} (x + 4)^{d₂} (x + 2)^{d₃} (x − 2)^{d₄} over ℤ (R is the characteristic polynomial of 3P(1 + S)P without its roots 6 and 0, so the card's Q(x) is R(x + 4); the plane computation is checked by sympy in `two_subspace_run.txt`; Review 87) on the largest orbits at p = 7, k = 5 (64 points); p = 11, k = 6 (60); p = 13, k = 9 (112); and on the orbit of (3,3,3) mod 27 (72) and mod 81 (648). At mod 135 (2880 points) it holds modulo three 62-bit primes, a deviation from the card's "exact" (an exact run there would take hours) |
| N2 | **holds:** the orbit of (t, 0, 0) is the 6 points (±t, 0, 0), (0, ±t, 0), (0, 0, ±t) on k = t², for symbolic t |
| N3 | **holds** for every leaf and every prime 3 ≤ p ≤ 71 |
| N6a | **holds:** x² + y² + z² − xyz takes the residues 0, 1, 2 mod 4 and 0, 1, 2, 4, 5, 7, 8 mod 9 |
| N6b | **holds:** each of the 15 leaves is solvable mod 8, 16, 27, 81, 5, 25, 7, 49, 11 and 13, and has no integer point with \|x\|, \|y\| ≤ 3000. This is evidence that they have none; a proof needs the reduction theory of Markoff-type surfaces (not checked) |
| N8 | **holds:** k = 5, 13 and 29 each carry exactly two orbits, of 1152, 4608 and 18432 points, mod 2⁵, 2⁶ and 2⁷ |
| M1 | **holds:** both 40-point orbits over ℚ(√5), through (φ, 1, 0) on k = (5 + √5)/2 and through (1 − φ, 1, 0) on k = (5 − √5)/2, reduce with √5 ↦ 0 one to one onto the orbit of (3,3,3) mod 5 |
| M2a | **fails as worded:** at mod 189 = 27 · 7 (2016 points, the product of 72 and 28; C fixes 3) the halving fails. The gcd has degree 663 of the charged 671, and the 8 unpaired roots are those of (x² − x − 1)(x² + x − 1)(x² + x − 4)(x² − x − 4) (`mixed_levels_run.txt`) |
| M2b | **holds:** at mod 54 = 27 · 2 (288 points) the halving holds exactly |

- **Post hoc, labelled** (`mixed_posthoc.py`, written after M2's run was read): the halving also holds exactly at mod
  108 = 27 · 4 (288 points; the orbit mod 4 has 4 points) and mod 162 = 81 · 2 (2592 points).

## What the whole does, read in its own terms

- **A pairing law that belongs to the modular group, not to the whole.**
  - On any orbit, the four moves are S after C or C², and C or C² after S. So T₄ = 3(SP + PS) − 2S, where P projects on
    C-invariant functions and E = (1 + S)/2 on S-invariant ones.
  - Two projections in general position meet at angles θ. On each such plane T₄ is [[4cos2θ, sin2θ], [sin2θ, 2cos2θ]],
    with eigenvalues 3cos2θ ± 1, exactly 2 apart (main's derivation).
  - The four intersections give 4, −4, −2 and 2.
  - So every finite orbit of the moves, on every leaf and at every modulus, carries the pairing λ ↔ λ + 2. This is the null
    control's kind of fact: it needs only C³ = S² = 1.
  - B2004's W = T − D is the same two-subspace mathematics for the six-move sum. The 3-tower's halving is not of this kind:
    it needs B2009's condition on the stabiliser, and it fails at mod 135 and 189.
- **The halving and the mixed levels:**
  - In the levels run it holds at 27, 81 and 243, and at 54, 108 and 162, where the 2-part keeps the orbit at 4 points
    (B1998's unopening 2-tower).
  - It fails at 135 and 189, where the factor 5 or 7 brings the cusp's whole leaf (40 and 28 points).
  - At 5 that leaf is the reduction of the icosahedral 40-point orbit (M1). At 7 no finite orbit known to the record reduces onto it [Review 87: the known orbits lie on
    k = 2, 3, (5 ± √5)/2, t² and 4; 5 is not a square mod 7, and t² ≡ 0 only at the origin; B1989's list is not proved
    complete], and the halving
    fails all the same. So the failure is not the icosahedral origin.
  - A table of the levels run, not a law.
- **The finite orbits over ℂ were heard twice, independently:** the listener's five are B1989's.
- **The listener heard the dihedral family B1989 owed.** It is a 6-point orbit on every leaf k = t².
- **The rule behind B1990's corrections:** χ(k − 4) and χ(k(k − 4)).
- **Integer leaves:**
  - two congruence obstructions: 3 mod 4, and 3 or 6 mod 9;
  - fifteen leaves that are solvable at every modulus tried but have no point with |x|, |y| ≤ 3000.
- **On the leaves k = 5, 13 and 29 (each ≡ 5 mod 8),** the moves keep two equal halves at 2⁵, 2⁶ and 2⁷ [Review 87: scoped
  to the leaves run]. Nothing found so far
  separates them.
- **No rate is read as physical, and nothing is compared with data.**

## Disclosures

- The card was hashed before any run.
- **N1 at mod 135** was checked modulo three primes, not over ℤ as the card said.
- **The listener's observations main did not check** (B7, B8, B11, B12, B13, B14, B17, B18) are registered at the
  listener's word. Its scripts were read, not run.
- **The listener is main's own delegated agent, not a seat.** Its blindness was by instruction. It disclosed one channel
  of priming (the session context). Where an observation matches words in those commit subjects (S₄, the swap), it is
  marked primed.

## What is open

- Why the halving fails when a factor 5 or 7 joins the 3-tower, and survives the 2-part, by B2009's stabiliser condition.
  G₁₃₅ and G₁₈₉ are too large for character tables, so another route is needed.
- What separates the two 2-adic halves on k ≡ 5 mod 8.
- A proof that the 15 leaves have no integer point, by the reduction theory.
- The listener's unchecked items, and its own list of what the system invites (escape rates, periodic points, the
  spectral gap as p grows).
- The census over every orbit and prime, and the null control on a bare modular-group action (the remaining guards).
  N1 is one null-control fact already.
