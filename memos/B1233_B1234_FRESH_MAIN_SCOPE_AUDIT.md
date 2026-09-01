# R036 — fresh-main hostile audit: one refutation and one scope repair

Source state: `origin/main@a5138424` (B1234). Verdict: **B1233 contains one
exactly refuted claim; B1234's three computed cells stand but its headline join
is not certified.** No unrelated B1233/B1234 result is regraded here.

## B1233: the origin is local, not global

B1233 studies the real polynomial

```text
K(x,y,z) = x^2+y^2+z^2-xyz-4.
```

Its executable labels `(0,0,0)` a global minimum after checking only
`K(0)=-4` and the positive Hessian `2I`. Those facts prove a strict **local**
minimum. They cannot prove globality, and the exact diagonal restriction refutes
globality on the stated affine real space:

```text
K(t,t,t) = 3t^2-t^3-4 -> -infinity,
K(10,10,10) = -704 < -4.
```

The real critical locus itself is consistent with the local statement: the
origin and the four signed points `(+-2,+-2,+-2)` having sign product `+1`.
The origin has Hessian signature `(3,0)`; the other four have `(2,1)` and value
zero. Completeness is elementary: if one coordinate vanishes, the three gradient
equations force all three to vanish. Otherwise, dividing `2x=yz`, `2y=xz`, and
`2z=xy` pairwise gives `x^2=y^2=z^2`; substitution fixes the common absolute
value to `2` and the sign product to `+1`.

There is a possible repaired theorem, but it needs a domain declaration. On the
compact `SU(2)` trace box `[-2,2]^3`, `K >= -4`. If `xyz <= 0` this is immediate.
If `xyz > 0`, put `a=|x|`, `b=|y|`, `c=|z|` and use

```text
a^2+b^2+c^2-abc = (a-b)^2+c^2+ab(2-c) >= 0.
```

Thus the origin is the unique global minimum on that box. B1233 names no such
domain, so the banked sentence must be narrowed rather than silently supplied
with one.

## B1233: arithmetic does not forbid continua

The synthesis sentence "arithmetic cannot emit a continuum" is false as a
general mathematical principle. The integer-defined curve

```text
x^2+y^2=1
```

has the real one-parameter family

```text
x=(1-t^2)/(1+t^2),  y=2t/(1+t^2),  t in R,
```

with `t=y/(1+x)`. Arithmetic equations can therefore define positive-dimensional
real moduli. The narrower corpus observation may still be useful: the particular
maps run so far output integers, torsion, rational/algebraic values, or finite
menus. But that is an empirical inventory requiring its own census, not a
consequence of arithmeticity.

The executable-scope claim also needs narrowing. `audit.py` evaluates fourteen
booleans, one of which is the invalid global-minimum test; its compound prose
lists 15 confirmations and seven refutations. Among the prose claims not
executably rechecked there are the other Jones values, the full Fricke identity,
critical-locus completeness, Markov integer-point classification, class numbers,
the genus-field identification, Markov-number membership, the spin count, and
the simply-laced central-charge statement. Some are sound prior facts; the issue
is the phrase "every checkable claim was recomputed here."

## B1234: preserve the cells, narrow the join

R036 does not attack B1234's exact core:

- orientation double covers: `40/40` amphichiral against `6/200` control;
- the orientation cover of `m000` is isometric to `m004`, volume ratio `2`;
- both displayed presentations have `48` surjections onto `SL(2,3)=2T`.

Those computations establish that A6 manufactures the mirror self-isometry and
that a formal `2T` quotient exists on both sides. They do **not** compute:

- the trace field (`same_trace_field` is a literal string in the certificate);
- restriction of any `m000 -> 2T` map along the index-two cover subgroup;
- a dependency graph from A6 to the eight named walls;
- the physical identification I-6 between the manifold quotient and the
  transverse ALE group.

More strongly, B1234's arrow

```text
A6 -> amphichirality -> all eight walls
```

contradicts the immediately preceding bank. B1224 proves that amphichirality
forces only `CS in {0,1/4}` and exhibits amphichiral `m003`, `m135`, and `m207`
at `1/4`. B1226 then explicitly refutes `CS=0 iff amphichiral` in both
directions and types `m004`'s zero as a **contingent datum**. Since the
`k`-blindness link needs `CS=0`, amphichirality alone cannot cause even that
first named wall. A6 contains the stronger free-deck datum, but B1234 supplies
no proof that freeness selects the zero torsion class; that is a separate live
question.

Consequently, `48=48` is equality of cardinalities, not yet inheritance of the
same quotient through the cover. McKay still earns the abstract `2T <-> affine
E6` representation graph (I-1); it does not earn the physical transverse-ALE
identification (I-6). And A6 explains the **mirror/chirality/CP constraint**, not
the universal slogan "costs every value": the CS-zero/k-blind wall still needs
an unproved free-deck-to-zero step, while rank, generation, Mostow scale, and
arithmetic value-disjointness have independent mechanisms. B1234's exact core is
therefore retained while its prose join is typed as a candidate dependency
statement.

The next discriminating calculation is precise: enumerate the 48 `m000`
surjections, restrict each through an explicit index-two subgroup map for the
orientation cover, and compare the resulting maps and `Aut(2T)` orbits with the
48 `m004` surjections.

## Fresh-state hygiene

At `a5138424`, the identification rows actually count
`3 EARNED / 3 REFUTED / 3 UNEARNED`; the standing prose still says `3/2/2`.
The new relay row is also embedded in the two-column definition table rather
than the disposition table, and the relay date header remains `2026-08-27`.
These are record defects, not mathematical results.

## Reproduce

```text
python3 certificates/r036_fresh_main_scope_audit/fresh_main_scope_audit.py
```
