# Partial filling: a certified cusped, geometrically chiral witness

2026-09-07. Path-local verification of the owner's named candidate; no B ID.

## Verdict

**The core existence claim passes interval verification.** The decorated
triangulation `kLLLPLQkcefegijjiijiieldllxtxa_aBbBabBbbacb` is identified
combinatorially with a degree-five cover of m004. Filling cusp 0 at (2,1)
leaves two complete cusps and produces a certified hyperbolic manifold
whose normalized Chern--Simons invariant excludes the mirror-compatible
classes {0, 1/4} modulo 1/2.

This establishes geometric chirality with cusps retained. It is not yet
a physical chiral-fermion spectrum, a derived quantum level, the boundary
theory required by B1064, or a source-selected cover/cusp/slope.

## What was actually checked

- The numeric producer enumerates degree-five covers and records explicit
  triangulation isomorphisms to the input, including cusp permutations
  and peripheral matrices. An identity-peripheral match occurs. The
  cover degree is not inferred from a volume coincidence.
- The partial presentation has three cusp records, completeness
  [false, true, true]. SnapPy's total cusp-record count is not the count
  of surviving complete ends. Permanently filling cusp 0 produces two
  cusp records, both complete.
- Ordinary and high-precision numerical calculations give
  CS = +0.15759004087917847567899149801673152006645612249762745423
  and volume = 7.706911802810126654762022509212267553474512639...
  These decimal evaluations alone are NOT certificates.
- Sage 10.7 / SnapPy 3.3.2 `verify_hyperbolicity` succeeds at 100 and
  160 bits on both the partial presentation and the permanent filling.
  The certified shapes have positive imaginary parts.
- `complex_volume(verified_modulo_2_torsion=True)`, with interval pi and
  normalization Im(complex volume)/(2 pi^2), gives the interval certificate.
  At 160 bits its representative is approximately
  -0.092409959120821524321008501983268479933544 modulo 1/4,
  with interval diameter less than 4.2e-43.
- The native interval excludes every quarter-lattice point. The distance
  is greater than 0.0924099. The high-precision ordinary value differs
  from this representative by 1/4, within the verified ambiguity.
- The reverse-orientation interval is its negative modulo 1/4, with
  compatible volume. The 100/160-bit intervals are compatible and shrink.
  The m004 and unfilled-cover controls meet the quarter lattice; the
  5_2 positive control excludes it. Synthetic zero and 1/4 must fail
  the obstruction test, whereas 1/24 must pass it.

The first-run data, not rounded numbers in this prose, are in
[the numeric receipt](partial_filling_numeric_first_run.json) and
[the successful interval receipt](partial_filling_interval_control_first_run.json).

### Periods and the exact scope of the certificate

SnapPy's ordinary normalized CS is defined modulo 1/2. Its verified
complex-volume algorithm retains a further two-torsion ambiguity, giving
normalized CS only modulo 1/4. An orientation-reversing self-isometry
would imply CS = -CS modulo 1/2, hence CS belongs to {0, 1/4}.
Excluding the whole quarter lattice therefore suffices, despite the
coarser verified period. This does not certify the choice of the ordinary
+0.157590... lift over its alternative.

Source: [SnapPy verified-computation documentation](https://snappy.computop.org/verify.html),
read 2026-09-07; the ordinary normalization is documented in
[Manifold methods](https://snappy.computop.org/manifold.html).
The existing B1226/B1227 scopes already distinguish zero CS from
amphichirality. In particular, CS zero is not an iff classifier.

## First failures and reporting qualifications

Design, original producers and tests were sealed at b5924cca before
execution. The numeric producer succeeded. The original interval producer
computed all scientific intervals, then failed its reporting assertion:
Sage's rational string parser rejected a decimal lower-bound string.
[Original JSON](partial_filling_interval_first_run.json) and
[failure](PARTIAL_FILLING_INTERVAL_FAILURE.txt) remain unchanged.

The separate reporting control was sealed at 3a2a15c7, then repeated
the entire interval calculation and passed. It also re-evaluates the
native interval independently of serialized fields.
[Complete successful receipt](PARTIAL_FILLING_INTERVAL_CONTROL_RECEIPT.txt).

Precision qualification on that adapter: `QQ(MPFR_endpoint)` in the
sealed wrapper produces a rational approximation, not necessarily the
exact binary endpoint. Its docstring's word "exact" is too strong.
The scientific exclusion flag is computed from the native interval
before serialization and is unaffected; the rational field must not
be reused as an exact outward endpoint. The decimal interval summaries
and the conservative 0.0924099 bound above are not claims to exact endpoint
serialization. No sealed source is silently rewritten to hide this.

The quiescent focused run is **29 passed**, one optional-GUI warning,
39.15 seconds, covering the new numeric checks, charged-domain repair,
R14 and R15. The interval producer is a separate Sage run, not one of
those 29 tests. [Test receipt](CHARGED_DOMAIN_PARTIAL_CHECKS.txt).
Original R16 failures and prior broad-suite failures remain; no full-suite
or independent receiving-seat green is claimed.

## What this changes toward physics

It supplies a concrete geometric candidate for B1064 route (a), with
the previously requested simultaneous properties. It does not identify
CS(M) with a quantized level k. In complex Chern--Simons theory, k is a
coefficient of the action; the value at one geometric flat connection
is different data. Likewise, vanishing at that saddle does not by
itself delete the entire CS functional or quantum sector.
See [Gukov, section 1.1, equations (1.1)--(1.2)](https://arxiv.org/pdf/hep-th/0306165).

The next substantive test is to construct the actual boundary theory
for this marked filling: permitted fields, boundary conditions, anomalies,
level and partition function, then test the E6 level-one/c=6 identification
rather than infer it from a nonzero number. Filling also changes the
manifold. Any arithmetic, gauge or family construction to be carried
along must have an explicit surviving map. This separate candidate does
not replace the sourced m202 operator path in [R16](CHARGED_DOMAIN.md).

## Received counts and the latest proposed kill

The owner's clarification withdrew 18/22, subsequent grid counts, and
the degree-seven rational value as load-bearing evidence. The old grid
is dispositioned UNEXECUTED; this audit did not rerun it. Different
declared grids may have valid different counts. No census or rationality
theorem is banked here. A negative tetrahedron in one numerical
triangulation is not, by itself, proof that the manifold is nonhyperbolic;
the withdrawn degree-seven candidate is not globally killed here.

A later fetch receives outside-bench 879869ca. Its
`six_cusp_reachability.py` only loops over degrees 2 through 12.
The reported no-six-cusp result is not independently reproduced here.
**Even if correct, that bounded census cannot exclude higher covers.**
Also, B139 counts cusp-associated abelian data; it does not derive a
necessary identity "central charge six iff six geometric cusps".
B1190 GC-6 explicitly distinguishes the missing boundary identification.
Thus the incoming route-wide kill does not follow from its producer;
the bounded census can stand without closing the candidate.
