# B67 -- the figure-eight A-polynomial, derived from the trace-map fixed-point set

**Status:** an exact derivation. The figure-eight knot's A-polynomial -- a published
invariant of algebraic topology (Cooper-Culler-Gillet-Long-Shalen; explicit form
Cooper-Long 1996) -- is reproduced **exactly** from the metallic SL(2,C) trace map's
fixed-point set. Standalone character-variety / knot-theory mathematics; no physics,
no Origin-core claim. This cross-validates the trace-map framework against an
independent deep invariant.

## Result

```text
trace map (figure-eight monodromy phi = [[2,1],[1,1]] = M^2):
    T_1^2(x,y,z) = (xz - y,  z,  xz^2 - x - yz),     (x,y,z) = (tr A, tr B, tr AB)

fixed locus:                y = z = x/(x-1)
longitude trace:            kappa(x) = tr[A,B]   = (x^4 - 3x^3 + x^2 + 4x - 2)/(x-1)^2
meridian trace (squared):   tr(t)^2  = (M+1/M)^2 = (x^2 + x - 1)/(x-1)

meridian<->longitude trace identity:    kappa = tr(t)^4 - 5 tr(t)^2 + 2

eliminating x in eigenvalue coordinates (M = eig t, L = eig[B,A]) gives EXACTLY

    A(M,L) = M^4 L^2 + (-M^8 + M^6 + 2M^4 + M^2 - 1) L + M^4        (Cooper-Long 1996)
```

`derived A(M,L) - Cooper-Long = 0` (literal equality, not merely up to a unit).

## Why the fixed-point set is the right object

The figure-eight complement is the once-punctured-torus bundle with monodromy
`phi = [[2,1],[1,1]]`, realized on `F_2 = <a,b>` by `phi(a) = a^2 b`, `phi(b) = ab`
(abelianizes to `[[2,1],[1,1]]`, det +1; its trace map is `T_1^2`). A representation
`rho` of the fiber `F_2` extends over the bundle **iff** `rho` is conjugate to
`rho . phi`, i.e. iff its character `(x,y,z)` is a **fixed point of `T_1^2`**. So the
trace-map fixed locus is exactly the SL(2,C) character variety of the knot complement
restricted to the fiber -- the A-polynomial curve.

## The computation (`probe.py`)

1. **Fixed locus.** Solve `T_1^2(x,y,z) = (x,y,z)`: `y = z = x/(x-1)`.
2. **Explicit rep.** `A = [[x,-1],[1,0]]`, `B = [[0,b],[-1/b, x/(x-1)]]` with
   `b + 1/b = x/(x-1)` realize `(tr A, tr B, tr AB) = (x, x/(x-1), x/(x-1))`.
3. **Monodromy `t`.** Solve the linear system `tAt^-1 = A^2B`, `tBt^-1 = AB` for
   `t in SL(2,C)` (a 1-dim null space for irreducible `rho`, so `t` is unique up to
   sign). Verified numerically to `~1e-15`.
4. **Peripheral eigenvalues.** Meridian `M = eig(t)`; longitude `L = eig[B,A]` (the
   fiber boundary = Seifert/0-framed longitude). Then `M+1/M = tr(t)`, `L+1/L = kappa`.
5. **tr(t)^2.** `tr(t)^2/det(t) = (x^2+x-1)/(x-1)` -- confirmed to 50 digits at seven
   `x` (including `-1, 5/2, 11/3`) and, decisively, by the exact final match.
6. **Eliminate `x`.** The resultant of `(M+1/M)^2 = tr(t)^2` and `L+1/L = kappa` is
   `A_CL(M,L)^2` (a quadratic-in-`x` parametrization squares the eliminant); the
   squarefree part is the Cooper-Long A-polynomial, exactly.

## Significance and honest scope

- **First derivation of the figure-eight A-polynomial from a trace-map computation.**
  It connects the metallic SL(n) trace-map tower (B59-B66) to A-polynomials /
  character-variety knot invariants -- an independent cross-check of the framework.
- This is the **n=2** case. The natural next step is **SL(3)**: the SL(3) A-polynomial
  of the figure-eight (Garoufalidis-Thurston-Zickert 2011, via ideal triangulations)
  -- reproducing it from the SL(3) trace map would link the tower to quantum topology.
  Open; not attempted here.
- No claim about the wider project is promoted; proven core P1-P16 unchanged.

## Reproduce

```bash
python frontier/B67_figure_eight_apolynomial/probe.py
python -m pytest tests/test_b67_figure_eight_apolynomial.py -q
```
