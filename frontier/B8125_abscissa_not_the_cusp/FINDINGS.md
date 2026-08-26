# B8125 — abscissa not the cusp

**Arc dated:** 2026-08-22 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS.
**Gate 5:** no physical identification claimed in this arc.

> **RECONSTRUCTED 2026-08-26 from this arc's own banked record** (`arc_verdict.json`
> and `results.json`). **This seat stopped writing `FINDINGS.md` at B8110 and the
> omission ran unbroken through B8134 — sixteen arcs.** It went uncaught because the
> lock that detects it lives in a suite too slow to finish inside a session. **This
> document is faithful to the banked record but is NOT contemporaneous, and is marked
> so rather than backdated.**

## Verdict

**NEGATIVE**

THE n=2 ABSCISSA IS NOT A CUSP PHENOMENON -- REFUTED BY THE WEEKS MANIFOLD. The hypothesis was
that B8113's n=2 residue and its cusp-continuous-spectrum residue are one object, so that B739's
scattering determinant regularizes the abscissa. It is false. A log-fit produced a seductive
near-miss -- intercept d = 0.102679 against vol/(2 pi^2) = 0.102835, 0.15% -- which died the
moment c was pinned: d swings from 0.197 to -0.030 across c's own 20% uncertainty, so the
intercept was never determined, and the candidate had been printed in the same script that
produced the fit. B724's look-elsewhere rule, applied to this seat. THE DECISIVE CONTROL: on
m003(-3,1), the Weeks manifold -- closed, cusp-free, is_complete=False, filling (-3,1), volume
0.9427 -- S(2) grows identically, steps +0.050, +0.087, +0.079, +0.049 with no decay. The
divergence does not need a cusp. IT HAD TO FAIL: the abscissa is the critical exponent delta = 2
of the geodesic flow, an ENTROPY fact holding for every finite-covolume lattice in Isom(H^3);
the cusp contributes the CONTINUOUS SPECTRUM, on the other side of the trace formula. B8113's
three residues stay three. THE CLASS NAMED, and it is a one-line test for any future candidate
of this shape: does it survive on a CLOSED manifold? Tests one structural hypothesis and refutes
it. Uses partial sums over the length spectrum to cutoff 5.5 (m004) and 4.5 (Weeks); does not
prove divergence, and does not resolve whether the n=2 factor's conditionally-convergent limit
exists -- that remains open exactly as B8113 left it. Gate 5 untouched.

## Law created

This arc creates a law. **The statement of record is the `B8125` row in `docs/LAW_MAP.md`**, not this file.

## What the arc recorded

### `verdict`

REFUTED, by a control on a closed manifold

### `scope`

Tests one structural hypothesis and refutes it. Uses partial sums over the length spectrum to
cutoff 5.5 (m004) and 4.5 (Weeks); does not prove divergence, and does not resolve whether the
n=2 factor's conditionally-convergent limit exists -- that remains open exactly as B8113 left
it. Gate 5 untouched.

### `class_named`

do not look for unification between the geodesic-side and the cusp-side residues of the one-
loop. The geodesic side is governed by the flow's entropy, the cusp side by the continuous
spectrum; a fact true of closed manifolds cannot be a cusp phenomenon. The test for any future
candidate of this shape is one line: DOES IT SURVIVE ON A CLOSED MANIFOLD?

### `hypothesis`

that two of B8113's three residues are ONE object: that the n=2 factor's position at the
abscissa of absolute convergence is CAUSED by the cusp, so that B739/B8101's scattering
determinant is exactly what regularizes it. Named the previous turn as the only place left in
the 3d line where the B8112 shape -- two things that look different being the same -- was still
available.

### `verdict_line`

THE n=2 ABSCISSA IS NOT A CUSP PHENOMENON -- REFUTED BY THE WEEKS MANIFOLD. The hypothesis was
that B8113's n=2 residue and its cusp-continuous-spectrum residue are one object, so that B739's
scattering determinant regularizes the abscissa. It is false. A log-fit produced a seductive
near-miss -- intercept d = 0.102679 against vol/(2 pi^2) = 0.102835, 0.15% -- which died the
moment c was pinned: d swings from 0.197 to -0.030 across c's own 20% uncertainty, so the
intercept was never determined, and the candidate had been printed in the same script that
produced the fit. B724's look-elsewhere rule, applied to this seat. THE DECISIVE CONTROL: on
m003(-3,1), the Weeks manifold -- closed, cusp-free, is_complete=False, filling (-3,1), volume
0.9427 -- S(2) grows identically, steps +0.050, +0.087, +0.079, +0.049 with no decay. The
divergence does not need a cusp. IT HAD TO FAIL: the abscissa is the critical exponent delta = 2
of the geodesic flow, an ENTROPY fact holding for every finite-covolume lattice in Isom(H^3);
the cusp contributes the CONTINUOUS SPECTRUM, on the other side of the trace formula. B8113's
three residues stay three. THE CLASS NAMED, and it is a one-line test for any future candidate
of this shape: does it survive on a CLOSED manifold?

### `why_the_hypothesis_had_to_fail`

the abscissa of absolute convergence of the Ruelle zeta is the critical exponent of the geodesic
flow, delta = 2 for ANY finite-covolume lattice in Isom(H^3), compact or cusped. It is an
ENTROPY fact about exponential geodesic growth. The cusp contributes the CONTINUOUS SPECTRUM,
which enters the trace formula on the other side entirely. The two residues live on opposite
sides of the trace formula by construction and were never candidates to be the same object.

## Depends on

`B8113`, `B8112`, `B8101`

## Scope

As recorded above. Nothing in this reconstruction adds a claim the arc did not bank, and where
the arc recorded a limit, a flag or a self-caught error, that text is reproduced rather than
summarised away.
