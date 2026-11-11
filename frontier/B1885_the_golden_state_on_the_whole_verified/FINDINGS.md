# B1885 — The golden state on the whole, verified on main: the web seat's card, cell by cell

*Main, 2026-11-11 (S306p). Three seats reached one object the same morning: a state on the level-5 quotient, and the
place where its density is greatest. The agy lane sealed and ran it on its own branch (agy:B1881). The advisor seat
recomputed its state and its peak. The web seat sealed its own card and asked main to verify it with main's own code.
This arc does that. Data-free: a classical form at 30 digits. No value of τ on record is read or compared, and no
frame is evaluated at any point named here. None of the seats' code is run. The lane's own comparison with
measurement is not read and not repeated. 0 of 19.*

## 1. The answer first

- **Every cell the web seat asked main to verify reproduces on main's own code.** 32 checks; 31 hold. The one that
  fails is main's own guess at how well the lane's point would agree (§ 5).
- **The state is Maass's form of the golden field at level 5.** It transforms with the quadratic character, to
  2.3 × 10⁻³⁰. It is odd under the mirror and changes sign under the dual involution.
- **It vanishes wherever a symmetry forces it:** on the mirror's two lines, at both elliptic points, at both points
  of discriminant −20, and along the whole second stretch of the arc.
- **Its density has exactly one greatest place on the first stretch of the arc.** It is a strict maximum in the
  plane: the gradient is 2.7 × 10⁻³⁰ of the peak and both curvatures are negative.
- **The place** is z\* = 0.251539778143593605 + 0.369767142958202424 i in the standard frame. It agrees with the web
  seat's to every digit main prints. The frame-free statement is t(z\*) = −6.20356305811 − 9.30138728277 i, on
  ∣t∣² = 125.
- **The agy lane's reported point is 1.5 × 10⁻⁹ away and is not the critical point.** It prints fifteen digits.
- **It selects nothing and derives no value.** It is one place read from one state under choices that stand (§ 7).
  It is not main's design for the read-out on the whole (§ 6).

## 2. The card, cell by cell

The web seat's card is in `relays/chat1_2026-11-11_golden_state/` on its branch, at c95349fb. Main read its relay in
full and ran none of its code.

| the seat's cell | the seat's outcome | main's check | main's number |
|---|---|---|---|
| G0, controls on the coefficients | holds: 1.6 × 10⁻³⁹ for n ≤ 60 | the Euler product against a direct count of ideals, n ≤ 40 | 1.1 × 10⁻²⁷ |
| G1, f(gz) = χ(d) f(z) on three moves | holds: 1.4 × 10⁻³⁹ | the same three moves at three points | 2.3 × 10⁻³⁰ |
| G1's control, the cosine series | fails by 8.5, as it should | the same control | fails by 3.0 |
| G2, the sign under the dual involution | −1 | read at two points, not predicted | −1 |
| G3, zeros at the two elliptic points | below 2 × 10⁻⁴¹ of the peak | f² there over the arc's top | 2.4 × 10⁻⁶⁶ |
| G4, one maximum on the first stretch | one, at θ = 0.30985501437 π | 41 points, then the root of the derivative | 55.7739025871°, the same angle |
| G5, a strict maximum in the plane | both curvatures negative | the Hessian | −82.8568 and −76.6622 of the peak |
| G5, nothing greater on a grid | holds; grid's top 0.99991 of the peak | 99 × 205 points of the strip | none above; top 0.99974 |
| the coefficients c(11), c(19) | −1.11318395792, −0.171571737965 | c(11) from main's product | −1.11318395792 |

- **Main's precision is 30 digits and the seat's is 40.** The agreements are to main's precision.
- **Two of G3's four zeros test nothing,** as the seat says: on x = 0 and x = ½ every term of a sine series
  vanishes. Main's run prints exactly 0 there.
- **G5's last clause, which failed for the seat by a fault of its design, is not repeated here.** Main checked the
  three clauses that hold.

## 3. What main adds

### 3.1 The trace test passes on main's own Hessian

At a critical point of f² where f is not zero the gradient of f vanishes, so the two second derivatives of f² sum to
2 f Δf = −2 (¼ + R²) f² / y². That is −159.519005666 times the peak. Main's Hessian gives −159.519005666. The test
is the web seat's referee's. It can fail: a Hessian that is not an eigenfunction's density fails it.

### 3.2 The state's boundary conditions on the cell

The cell is bounded by x = 0, x = ½, the circle ∣z∣² = 1/5 and the circle ∣z − ½∣² = 1/20. It has three right angles
and a cusp, so its area is π/2, a quarter of the line's surface.

| side | the reflection | the state under it | so on that side |
|---|---|---|---|
| x = 0 and x = ½ | the mirror, and the mirror after one step | odd | the state is zero |
| ∣z∣² = 1/5 | the mirror after the dual involution | even: two signs of −1 | its normal derivative is zero |
| ∣z − ½∣² = 1/20 | the last, followed by the move with rows (−2, 1), (−5, 2), which has χ = −1 | odd | the state is zero |

Checked numerically at 30 digits (A2, A3). **The greatest place lies on the one side where the state does not have
to vanish.**

### 3.3 One sign in the cell, and what that shows

On 14,432 points of main's grid inside the cell the state has one sign. A grid is not a proof.

- **If the state has no zero in the open cell, it is the lowest state of its own symmetry class.** That is the
  standard fact for a positive solution of such a problem.
- **That is not the statement that it is the lowest twin-odd state.** The twin-odd states fall in four classes, by
  the sign under the mirror and under the dual involution. The two classes even under the mirror have continuous
  spectrum from ¼. The fourth class has the two circles' conditions exchanged, and no symmetry of the cell
  exchanges the circles: their radii are 1/√5 and 1/(2√5). So its lowest state is not fixed by this one.
- **"Lowest" and "simple" are not verified on main.** The web seat's referee has a scan, in double precision, that
  finds no state below this one in any class. Main has not repeated it.

### 3.4 The same recipe at levels 13 and 17: where it must vanish

By hand first: at a point fixed by a move g the state satisfies f = χ(d) f, so it vanishes when χ(d) = −1.

| level | points with a symmetry of their own | χ(d) there | the state there |
|---|---|---|---|
| 5 | two of order 2, d = ±2 | −1 | zero (2 × 10⁻⁶⁶) |
| 13 | two of order 2, d = 5, 8 | −1 | zero (below 10⁻³⁰ of the scale) |
| 13 | two of order 3, d = 3, 9 | +1 | not zero: 1.4 of the scale |
| 17 | two of order 2, d = 4, 13 | +1 | not zero: 1.36 of the scale |

- **At level 5 the state vanishes at every point that has a symmetry of its own. At 13 and 17 it does not.**
- The advisor seat reports that at 13 and 17 the density is greatest at such points. Main checked where the state
  must vanish and where it need not. It did not search for the greatest place at those levels.

### 3.5 The place depends on the measure

"Density" above is f², taken against the hyperbolic area. Against the chart's Euclidean area the density is f²/y²,
and near the peak that is greatest 0.057 away, at ∣z∣² = 0.163, off the circle. So the area clock enters the
read-out a third time, as the web seat's referee says. Main's grid reproduces its figure of 0.056.

## 4. What is forced and what is found

- **Forced by parity, before any number:** a state odd under the mirror vanishes on the mirror's fixed set. So no
  greatest place of its density is fixed by the mirror, and every greatest place comes as a mirror pair. The card
  could not have failed on that.
- **Forced by the sign −1 under the dual involution:** the state vanishes on the second stretch of the arc.
- **Found, by a grid and not by a proof:** the greatest place is one pair and no more, and it lies where it lies.
- **One pair or two, by the surface.** On the line's surface the density has one greatest pair. On the one-twin
  surface the point has two preimages, so there are two pairs, which the exchange of the twins carries to each
  other. Which surface an outcome is counted on goes with the mark. The register row P-776 states both and
  chooses neither.

## 5. The agy lane's reported point

Main read the lane's point in the web seat's sealed header. Main has not read the lane's files.

| | at main's point | at the lane's reported point |
|---|---|---|
| the gradient of the density, over the peak | 2.7 × 10⁻³⁰ | 1.24 × 10⁻⁷ |
| the density, below the peak | 0 | 9.34 × 10⁻¹⁷ of the peak |
| ∣z∣² − 1/5 | 0 to 30 digits | 1.33 × 10⁻⁹ |
| distance between the two points | | 1.5 × 10⁻⁹ |

- **The lane's point is right to 1.5 × 10⁻⁹ and no further.** Its last six printed digits are not the peak's.
- **Main's own expectation H6 fails as written.** It said the two would agree to 10⁻⁹. It was not blind (§ Disclosed).
  It is kept as failed in the run.
- **Not verified by main:** the web seat reports that the lane's printed gradient does not fit its printed point,
  and that its printed curvatures fail the trace test. Those rest on lines of the lane's files main has not read.
  They are relayed to the lane as the seat's findings.

## 6. Against the eight conditions taken for the design (P-776)

The advisor seat's eight conditions are what main's design for a read-out on the whole must meet. This arc is a
check of seats' work. It is typed against them so that nobody reads it as the design.

| | the condition | this computation |
|---|---|---|
| R1 | every ingredient listed and typed | listed in § 7; typed there as choices |
| R2 | a state of the whole, not a quantity of one history | yes: a function on the level-5 quotient |
| R3 | existence and uniqueness first | existence yes; that it is the lowest, and simple, is **not shown** |
| R4 | symmetry computed first and apart | yes: the parities and the forced zeros are by hand, then checked |
| R5 | what counts as a place, written in advance | main's criterion of B1881 § 6: a pair the mirror exchanges. This place is one |
| R6 | the result survives its chosen ingredients | **not met**: the place moves with the measure (§ 3.5) |
| R7 | the same construction at other levels | in part: the forced zeros at 13 and 17, not the greatest place |
| R8 | no measured number | none is read here |

- **One clause of P-776 is no longer kept, and this is said plainly.** The row says main's own design is written
  against the eight conditions before main reads the lane's result. Main has now seen the lane's reported point.
  A design by main cannot be blind to it.
- **What main still keeps:** the point is compared with no value of τ on record, and no frame is evaluated at it.
  Any later comparison is a look and must be entered as one.

## 7. What is not shown, and the choices that stand

- **Not shown:** that this is the lowest twin-odd state; that its eigenvalue is simple; that the greatest place is
  one pair, beyond a grid; anything at all about a value.
- **The choices, none of which is removed here:** level 5; the mark and the surface an outcome is counted on; the
  twin-odd sector; this state within it; the area clock, which the record counts as chosen (B1815) and which enters
  the operator, the inner product and the measure; reading a state by the greatest place of f²; the frame in which
  a coordinate is quoted.
- **By main's criterion,** which is a reading and not a result, a pair that the mirror exchanges is an outcome at
  which "only even ticks are observed" can be delivered. For any state odd under the mirror, an outcome that is one
  orbit is of that kind. What puts an observer at one member of the pair is open (the foundation's FK16).

## Seen first

Swept from main at 64bf79ebc, before this page was written and after the first run.

- `VERDICT topic-sweep /Maass|dihedral|Grössenchara|Grossenchara|Hecke character|golden state|spectral parameter/ (full text): 43 of 1633 arcs on main match (NEGATIVE 12, OPEN 4, PROVED 27); 3 register rows match (QUEUED 3)`
- `VERDICT topic-sweep /elliptic point|forced zero|quadratic character|nebentypus|Legendre symbol/ (full text): 17 of 1633 arcs on main match (NEGATIVE 3, PROVED 14); 0 register rows match (none)`
- `VERDICT topic-sweep /peak of the density|density peaks|greatest place|where its density|\|z\|\^2 = 1/5|Fricke/ (full text): 85 of 1633 arcs on main match (NEGATIVE 14, OPEN 5, PROVED 66); 3 register rows match (QUEUED 3)`

On record and used: B1881 (the two level-5 quotients, the dual involution, the arc, and the criterion of its § 6);
B1879 § 7 (the condition on even ticks); B1815 (the clock is chosen); B1872 and B1733 (the allowed subweave and its
mark). The record's Maass forms are those of the figure-eight complement (B790 to B797, B922). It holds no state on
either level-5 curve before this morning.

Literature: Maass, *Über eine neue Art von nichtanalytischen automorphen Funktionen*, Math. Ann. 121 (1949), for the
construction. Main rebuilt it from the definition and checked the automorphy numerically. It took no number from
any table.

## Disclosed

- **The first run had 26 checks and 3 failed.** Two were main's own fault: at levels 13 and 17 the automorphy was
  tested at a point whose image lies so low that the series needed 1400 and 2500 terms, and it was cut at 400. The
  checks read 2.9 × 10⁻¹¹ and 2.5 × 10⁻⁶. Mended: the test points now keep the point and its image near height
  1/p, three moves are tested at each level, and the series refuses to be evaluated where its cut is not
  negligible. No statement about the state failed. The third is H6 (§ 5).
- **Six checks were added after the first run,** on reading the web seat's relay in full: A1 to A6 in the script.
  None was an expectation of main's. Each is labelled "added" in the run.
- **Not blind.** Before writing the script main had read the web seat's sealed header, which prints the lane's
  point, and a commit headline of the seat's that gives the gradient at that point.
- **The run is at lowest priority** beside another job; it takes about four minutes.
- **The lock reads the committed run** and recomputes a part of it at 20 digits. It does not rerun the whole.

## Reproduce

```
python3 -B frontier/B1885_the_golden_state_on_the_whole_verified/verification/golden_state_on_main.py
```

It writes `golden_state_on_main.json` and `golden_state_on_main_run.txt` beside itself. It ends with
`CHECKS: 32, FAILING: 1`, the one being H6.
