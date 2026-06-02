# B67 -- The figure-eight A-polynomial from the trace map

**Status:** exact derivation; cross-validation of the trace-map framework against a
published knot invariant. Standalone math; no physics, no Origin claim.

## One-line result

The metallic SL(2,C) trace map's fixed-point set (figure-eight monodromy
`T_1^2`) reproduces the **Cooper-Long (1996) A-polynomial of the figure-eight knot
exactly**:

```text
A(M,L) = M^4 L^2 + (-M^8 + M^6 + 2M^4 + M^2 - 1) L + M^4.
```

## Idea

The figure-eight complement fibers over `S^1` with fiber a once-punctured torus and
monodromy `phi = [[2,1],[1,1]] = M^2`. A fiber representation extends over the bundle
iff its `SL(2,C)` character is **fixed by the trace map `T_1^2`** -- so the trace-map
fixed locus *is* the A-polynomial curve. At each fixed point we build the rep `(A,B)`
and the monodromy `t` (`tAt^-1 = A^2B`, `tBt^-1 = AB`), read off the meridian
`M = eig(t)` and longitude `L = eig[B,A]`, and eliminate the fixed-point parameter.

Key intermediate identity (meridian trace <-> longitude trace on the fixed locus):

```text
tr[A,B] = tr(t)^4 - 5 tr(t)^2 + 2.
```

## Files

- `probe.py` -- the derivation: trace map and fixed locus, explicit `A,B,t`,
  `tr(t)^2` and `kappa`, the symbolic elimination, and a numerical check that
  `A_CL(eig t, eig[B,A]) = 0` at sample fixed points. `main()` prints everything.
- `FINDINGS.md` -- full write-up, method, and honest scope (SL(3) is the open next step).

## Reproduce

```bash
python frontier/B67_figure_eight_apolynomial/probe.py
python -m pytest tests/test_b67_figure_eight_apolynomial.py -q
```

Verified: derived A-polynomial == Cooper-Long (literal equality); monodromy
equations to ~1e-15; `tr(t)^2 = (x^2+x-1)/(x-1)` to 50 digits.
