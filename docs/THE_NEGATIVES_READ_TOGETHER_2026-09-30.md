# The negatives read together (2026-09-30): what killed each step of the chirality chain

*Seat: cc (the SM-derivation branch). Written after the owner's question of 2026-09-30 and approved as the first of two steps.
0 of 19.*

## Why

The owner asked three things. Can the record read the pattern of its negatives and understand the problem more deeply? Is the work
tracking every relation the genesis permits, or only m004 and a few other objects? Did it part from genesis properly, or leave behind
something whose effect is needed now?

The seat's answer proposed two steps, and the owner approved them:
1. **Classify the kills**, naming the symmetry or rule that killed each, and enter the PROVED no-go results too, so the pattern is
   something the record can check. This note is that step.
2. **A sealed genesis-side arc** (B1504) on the remainder the pattern leaves. (It closed at design time as a theorem, so it was not
   sealed; see the currency note at the end.)

## What was done

- **Classified: the 16 kill-graph records this seat routed as placeholders** between 2026-09-26 and 2026-09-30 (`kill_form`
  `unrouted-unclassified`, judgement fields unset). Each now carries:
  - a kill form naming the symmetry or rule;
  - its faces;
  - `fact_computed = true`, with the script and lock that compute the deciding fact named in the note;
  - a hatch, a priority and a revival score.
- **Entered: ten PROVED arcs whose content includes a no-go the pattern cites.** They are B1351, B1385, B1389, B1390, B1392, B1393,
  B1394, B1395, B1396 and B1500. B833's lock records that kill records legitimately sit on PROVED arcs.
- **One reader.** This seat classified from each arc's FINDINGS, verdict and verification. That is not a calibrated panel: B738 found
  kill-form taxonomies convention-sensitive, and B842's panel standard applies to face attachment at scale. The families below are
  this note's convention, meant for reading, not a measurement.

`frontier/B738_pathfinder_compiler/kill_graph.json`; lock `tests/test_negatives_read_together.py`.

## The four families

A record's family is the first token of its `kill_form`, before the parenthesis.

1. **`symmetry-cannot-select`.** A symmetry acts on the candidates: it exchanges signs, conjugates charges or permutes generations.
   So no natural construction singles one out, and the result is zero, a degeneracy, or n copies of one. The form is B1203's.
2. **`closed-sum-zero`.** A closed or complete structure obeys a global identity that forces the total to zero: an Euler
   characteristic, Poincaré duality, Stokes, or a vanishing Dirac index.
3. **`frame-arithmetic`.** The frame's representation theory or lattice arithmetic excludes the target. Examples are spins never
   shared, the rank of an anomaly matrix, a classification list, the parity of a lattice, and fixed points in P¹(ℚ(√−3)).
4. **`end-datum-input`.** The count survives only at an end, and there it depends on a datum the object does not supply: a cut, a
   boundary condition, a flux degree or a perversity.

Two records keep core forms of B738's table: `absence-at-depth` (B1373) and `no-landing-site` (B1501).

## The table

| arc | verdict | family | the symmetry or rule that killed it |
|---|---|---|---|
| B1351 | PROVED | closed-sum-zero | Poincaré duality on a closed closing: χ = 0 and h¹(ψ) = h¹(ψ̄) for every character |
| B1361 | NEGATIVE | symmetry-cannot-select | the apexes' U(1)² allows only 27₁27₂27₃, so every mass matrix is hollow and σ₁ = σ₂ + σ₃ |
| B1363 | NEGATIVE | frame-arithmetic | Kac's order-3 and order-4 classes of E₆: none has the Standard Model as commutant |
| B1365 | NEGATIVE | frame-arithmetic | the D-term sign theorem: N and ν^c both carry γ = −5/3 |
| B1367 | NEGATIVE | symmetry-cannot-select | E₆'s trinification form gives the doublet and triplet blocks the same generation matrices |
| B1368 | NEGATIVE | frame-arithmetic | the 10 and the 5̄ never share an SL(2)_β spin |
| B1369 | NEGATIVE | symmetry-cannot-select | the region-swap parity on 79 of 83 free cusps, after a rank closure of 77 members |
| B1372 | NEGATIVE | frame-arithmetic | charge arithmetic at the cusp: 0 of 32 sign patterns |
| B1373 | NEGATIVE | absence-at-depth | on the real cone-manifold path the other eigenvalue is non-unitary at every point reached |
| B1385 | PROVED | symmetry-cannot-select | L3, the global parity; the word states fall first (b₁ = 1, no free cusp) |
| B1388 | NEGATIVE | end-datum-input | the count moves with the cut |
| B1389 | PROVED | frame-arithmetic | the 78's parity law: anomalous in every Higgs direction |
| B1390 | PROVED | frame-arithmetic | order-3 axes end at cusps (fixed points in P¹(ℚ(√−3))) |
| B1391 | NEGATIVE | symmetry-cannot-select | D₃ acts on the generations as its doublet: degenerate textures |
| B1392 | PROVED | closed-sum-zero | a Higgs class alive on every cusp gives a Fredholm problem with N = 0 |
| B1393 | PROVED | symmetry-cannot-select | charge conjugation: an end condition blind to the charge gives zero |
| B1394 | PROVED | symmetry-cannot-select | the Hopf trace: a symmetric source three over an acyclic bulk is three copies of one |
| B1395 | PROVED | end-datum-input | every finite-energy datum at a free cusp is charge-blind |
| B1396 | PROVED | symmetry-cannot-select | the cusp's Hopf trace: a symmetric cap over an acyclic bulk gives (n/3) copies of the regular representation |
| B1397 | NEGATIVE | frame-arithmetic | caps are linear in the charges: anomaly-free only for F ⊥ Y, then even in E₆ |
| B1398 | NEGATIVE | frame-arithmetic | every 10 of the 78 is an SL(2)_β doublet; the anomaly matrix has rank 3 |
| B1399 | NEGATIVE | frame-arithmetic | lattice parity: a shell of index m gives terms in multiples of m |
| B1500 | PROVED | end-datum-input | the cusp point is not Witt: one choice per point, contributing −1, 0 or +1 |
| B1501 | PROVED | no-landing-site | homogeneous G₂ cones: torus loci only A-type and hexagonal |
| B1502 | PROVED | closed-sum-zero | the links' H² = H⁴ = 0, and a homogeneous line bundle over a torus is trivial |
| B1503 | PROVED | closed-sum-zero | positive scalar curvature: the link's Dirac index vanishes, so the inflows cancel |

**The tally:** `frame-arithmetic` 9 · `symmetry-cannot-select` 8 · `closed-sum-zero` 4 · `end-datum-input` 3 · `absence-at-depth` 1 ·
`no-landing-site` 1, 26 records in all.

**Secondary memberships,** named inside the kill forms:
- B1369 (a rank closure first);
- B1385 (`frame-arithmetic` for the words);
- B1392 (`end-datum-input` at the free cusps);
- B1393 (its conclusion is `end-datum-input`);
- B1397 (`closed-sum-zero` by Stokes, §7).

## What the pattern says (a reading, not a theorem)

**Chirality is a choice of sign.**
- A symmetric structure cannot make that choice (family 1).
- A closed structure has nothing to choose (family 2).
- An open structure can carry the choice only as an input at its ends (family 4).
- Family 3 is the frame's own arithmetic. It decides what the counts can be (even, zero) once the sign is fixed.

**The chain's one positive** came where no symmetry negated the class: N = ±2 on cube~3.24 (B1386–B1387). B1388 then located that
count at the ends.

**This is the genesis principle's own theorem applied to chirality.** "Forced means natural" (B1384 §1) says the data force orbits,
not points. P022's addendum said as much on 2026-09-27: a non-zero index selects a sign, and a symmetry that exchanges the signs
forbids the selection. The record did not use the principle as a filter afterwards; the chain then confirmed it construction by
construction. It is also the shape of any index on a space with ends. The bulk terms vanish for flat, symmetric data, and the end
term needs a boundary condition.

**The remainder has two parts** (a reading of banked results):
- **The sign** is a selector of the same kind as orientation and the order bit (sL-3, the swap P's type).
- **The number** (one or three) depends on which level is physical, cover or quotient (sL-5). B1384 S3, B1390, B1396 and B1500
  ("one unit per cusp point") each end on it.

Both leads are ★★★, and neither has an entry after 2026-09-27. That was checked on this branch, on main (last commit 2026-09-18) and
on the audit lane (three commits since 2026-09-27, on a neutral-mode census).

## What genesis left on the table (checked against the record)

- **The relations used.**
  - Since B1385, the chain used two of the generated architecture's native relations: covers and isometries (B1386–B1399).
  - It then imported G₂ cone models that the architecture does not generate (B1500–B1503).
  - Not used since: P read as a move (the Gieseking state, which lies in m004's class, B1234); the word states, excluded only by the
    frame's free-cusp requirement; the ladder of m010; fillings, which appeared only as a negative, although B1500 showed the cone
    point's self-dual choice is a filling slope.
- **The basepoint.** Genesis puts the basepoint of the comparison at the puncture (P019's A5b) and makes the order bit a based
  datum (A7). B1380 S2 showed the orientation fork is visible exactly there: σ sends the peripheral word to its inverse, σ² to
  itself. No arc from B1386 to B1503 mentions the basepoint, A5b, A7 or the order bit. Whether the ends' datum is the genesis's
  based datum is B1504's question.
- **B1234's fork.** sL-3 closes one of two ways:
  - a datum odd under orientation that the object computes (a crack at the root);
  - or proof that every such datum is supplied from outside, which makes orientation the programme's one irreducible physical input.

  So far every chirality datum the chain found was supplied at an end, which is consistent with the second way. It has not been
  tallied against sL-3 until now.

## What the pass found about the instrument

- **An E45 instance:** routing without content. All 16 placeholders were this seat's. The first eight (the 2026-09-26 catch-up)
  used B836's bulk-routing form, and each later routing copied the seat's own earlier rows ("as for this seat's earlier routings").
  B1207's A3 (2026-08-29) had made "routed means routed WITH content" the house standard. Its lock names only B1203 and B1205, so
  nothing reached new records. The fix is machine-held: `tests/test_negatives_read_together.py` requires content on every record
  this seat routes (`routed_from` beginning `sm-branch-`).
- **Out of scope:** 167 other placeholders remain, from earlier bulk routings. This pass does not touch them.
- **Twelve records hold `faces_consulted` as a prose string** of the arcs consulted: B1084, B1086, B1094, B1096, B1108, B1137, B1140,
  B1142, B1258, B1259, B1262 and B1300 (B1300 is this seat's).
  - B842's lock counts them as faced, character by character. That is harmless against its floor of 600.
  - B1094's lock asserts a substring of the string form, so converting them to lists would break a lock.
  - Flagged, not changed.
- **Not entered by this pass:** the chain's earlier no-go arcs.
  - B1352 and B1354: self-duality kills the count, `symmetry-cannot-select` in form.
  - B1370: its verdict is OPEN.
  - B1377 and B1381: the tower's bounds, `frame-arithmetic` in form.

  A wider pass would read them.

## What changes

The mathematics does not change, and no value moves: 0 of 19. The kill graph can now say what killed each step of the chirality chain,
by family and by name. B1504 takes up the remainder on the genesis side.

## Currency (2026-09-30, later): B1504

- **Not sealed.** B1504's question closed at design time as a theorem, so there was no open outcome to seal. The owner approved a
  sealed arc; the record's rule for theorems (B1396, B1500, B1502) applied instead.
- **Its answer, on the sign (sL-3).**
  - The order bit is not a property of the oriented manifold, so no datum at a cusp point can depend on it.
  - The genesis's own puncture has exactly two symmetric self-dual completions, and neither is chiral: the meridian and the
    fibre's boundary.
  - Symmetry never forces a chiral end, because where a rotation would force one it leaves the gauge sector no symmetric completion.
  - The end's chirality is an input. What is left is physical: whether the completion carries a G₂ orientation (sL-8).
- **Its record.** B1504 is in the kill graph as `symmetry-cannot-select`, with `end-datum-input` as its conclusion. It was routed at
  banking (`routed_from` `sm-branch-2026-09-30-banking`), not by this pass, so the table and tally above are unchanged.
