# B530 Observer Fixed-Point Certificate

## Result in one sentence

The quoted golden fixed point was not reproduced, but an exact irreducible trace-zero character was
certified. It is **set-theoretically isolated but scheme-theoretically doubled**:

\[
\widehat{\mathcal O}_{X,x}\cong
\mathbb C[[\varepsilon]]/(\varepsilon^2).
\]

This is neither a smooth observer continuum nor an ordinary reduced isolated point. It is an isolated
state carrying one irreducible infinitesimal echo that is obstructed at second order.

---

# 1. What was actually available

The repository contains the defining mapping-torus equations

\[
T\rho(g)T^{-1}=\rho(\sigma(g)),
\]

and an unconstrained numerical search that reported at least fourteen distinct irreducible characters.

It does not contain the quoted point

\[
\bigl(
\operatorname{tr}(a),
\operatorname{tr}(b),
\operatorname{tr}(A),
\operatorname{tr}(B)
\bigr)
=
\left(
1,\frac1\varphi,-\frac1\varphi,0
\right),
\]

nor the claimed rank-18 certificate.

The defining equations were therefore reproduced independently.

---

# 2. Golden-trace reproduction test

Each generator was parameterized with determinant one and its quoted trace imposed identically. The
remaining nine complex degrees of freedom—including the diagonal twist—were optimized over 100 independent
random starts.

Best fixed-equation residual:

\[
\boxed{0.24158602234123036}.
\]

By comparison, genuine unconstrained solutions were routinely found with residuals between

\[
10^{-16}\quad\text{and}\quad10^{-14}.
\]

The quoted golden tuple therefore does not behave like a fixed representation.

This is strong numerical evidence, but not an exact elimination proof of nonexistence.

**Status:** `NOT REPRODUCED`

---

# 3. Exact irreducible trace-zero representation

Set

\[
\tau=\frac12+\frac{\sqrt3}{2}i,
\qquad
T=\begin{pmatrix}\tau&0\\0&\tau^{-1}\end{pmatrix}.
\]

An exact representation over \(\mathbb Q(\sqrt{-3})\) is:

\[
\rho(a)=\rho(B)=
\begin{pmatrix}
 i/\sqrt3&1\\
 -2/3&-i/\sqrt3
\end{pmatrix},
\]

\[
\rho(b)=
\begin{pmatrix}
 -i/\sqrt3&\frac12-\frac{\sqrt3}{2}i\\
 -\frac13-\frac{i}{\sqrt3}&i/\sqrt3
\end{pmatrix},
\]

\[
\rho(A)=
\begin{pmatrix}
 -i/\sqrt3&\frac12+\frac{\sqrt3}{2}i\\
 -\frac13+\frac{i}{\sqrt3}&i/\sqrt3
\end{pmatrix}.
\]

Symbolically, for every \(g\in\{a,b,A,B\}\),

\[
\det\rho(g)=1,
\]

\[
T\rho(g)T^{-1}=\rho(\sigma(g)).
\]

Also,

\[
\tau^6=1.
\]

All four generator traces are exactly zero:

\[
\boxed{
\operatorname{tr}\rho(a)=
\operatorname{tr}\rho(b)=
\operatorname{tr}\rho(A)=
\operatorname{tr}\rho(B)=0.
}
\]

The six commutator traces are:

\[
\boxed{
(\kappa_{ab},\kappa_{aA},\kappa_{aB},
 \kappa_{bA},\kappa_{bB},\kappa_{AB})
=
(-2,-2,2,-2,-2,-2).
}
\]

Since \(\kappa_{ab}\neq2\), the pair \((a,b)\), and hence the representation, is irreducible.

**Status:** `PROVED EXACTLY`

---

# 4. Exact first-order local geometry

Work in the diagonal-\(T\) gauge used by the repository search.

There are seventeen complex variables:

- one twist coordinate;
- sixteen generator-matrix entries.

There are twenty complex residual equations:

- sixteen mapping-torus matrix entries;
- four determinant equations.

The exact complex Jacobian has:

\[
\boxed{\operatorname{rank}J=15},
\]

so

\[
\dim_{\mathbb C}\ker J=2.
\]

One kernel direction is the remaining diagonal conjugation gauge.

After fixing the transverse gauge condition

\[
\rho(a)_{12}=1,
\]

one non-gauge tangent remains.

An explicit \(15\times15\) minor has determinant

\[
\boxed{
\frac{88i}{3}(2\sqrt3-3i)\neq0.
}
\]

Therefore the gauge-sliced tangent space has complex dimension exactly one.

This corrects both naive conclusions:

- the point is not a smooth zero-tangent reduced point;
- the extra tangent does not yet imply a character curve.

**Status:** `PROVED EXACTLY`

---

# 5. Exact second-order obstruction

Let \(v\) be the unique non-gauge tangent on the slice. If it integrated to a formal family

\[
x(\varepsilon)=x+\varepsilon v+\varepsilon^2w+\cdots,
\]

the order-\(\varepsilon^2\) equation would require

\[
Jw=-h(v,v).
\]

An exact left-null witness \(\ell\) was constructed with

\[
\ell^TJ=0.
\]

Its pairing with the quadratic residual is

\[
\boxed{
\ell^Th(v,v)
=
-\frac{9\sqrt3}{\sqrt3+i}
\neq0.
}
\]

Therefore no second-order correction \(w\) exists.

The one physical infinitesimal tangent is obstructed and cannot generate a formal or analytic curve.

Hence the character is set-theoretically isolated.

Because its Zariski tangent is nonzero, it is not reduced.

Using the nonzero \(15\times15\) minor to eliminate the other variables, the remaining local equation has
a nonzero quadratic leading term. Thus the completed local algebra on the gauge slice is

\[
\boxed{
\widehat{\mathcal O}_{X,x}
\cong
\mathbb C[[\varepsilon]]/(\varepsilon^2).
}
\]

**Status:** `PROVED EXACTLY`

---

# 6. Meaning for the observer framework

The exact result is subtler than both prior descriptions.

It is not a continuous four-dimensional or one-dimensional observer family at this character.

It is also not an ordinary reduced discrete point.

It is:

\[
\boxed{
\text{one isolated interaction state}
+
\text{one infinitesimal echo that cannot become a neighbouring state}.
}
\]

This is mathematically close to the user's “last echo of irreducible feedback” language, but no physical
interpretation is required for the theorem.

The golden ratio does not occur in this point's trace coordinates. At the trace-zero point the coordinate
field is Eisenstein:

\[
\mathbb Q(\sqrt{-3}).
\]

The golden factor previously observed at this point belongs to the derivative spectrum of the trace-map
dynamics, not to generator traces.

Therefore the statement

> “the observer is \(\varphi\)”

is not supported by this exact character.

The safer structural statement is:

> The interaction state is Eisenstein in its coordinates, while the dynamics linearized around it carries
> the golden growth factor.

---

# 7. What this settles and what remains open

```text
QUOTED GOLDEN TRACE POINT                NOT REPRODUCED
EXACT NONEXISTENCE OF GOLDEN TUPLE       OPEN
TRACE-ZERO FIXED REPRESENTATION          PROVED EXACTLY
TRACE-ZERO IRREDUCIBILITY                PROVED EXACTLY
COMPLEX JACOBIAN RANK                    15, PROVED EXACTLY
NON-GAUGE TANGENT DIMENSION              1, PROVED EXACTLY
SECOND-ORDER OBSTRUCTION                 NONZERO, PROVED EXACTLY
SET-THEORETIC LOCAL STATUS               ISOLATED
SCHEME-THEORETIC LOCAL STATUS            NONREDUCED DOUBLE POINT
FULL IRREDUCIBLE CHARACTER CENSUS        OPEN
ONE-KAPPA SEPARATION THEOREM             OPEN
CONTROL SUBSTITUTION                     NOT YET RUN
REPOSITORY WRITES                        NONE
```

---

# 8. Next exact computation

The next most discriminating calculation is to apply the same exact local test to one generic real
irreducible numerical point.

There are two possible outcomes:

1. rank \(16\) after the diagonal gauge, with only the conjugation kernel:
   a reduced isolated character;

2. rank \(15\) with a second obstructed tangent:
   another nonreduced double point.

This will determine whether the nilpotent echo is special to the trace-zero character or is the generic
local structure of the fixed-character scheme.
