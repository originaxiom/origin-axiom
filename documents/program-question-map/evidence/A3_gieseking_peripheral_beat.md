# A3 — Gieseking beat on peripheral (H_1)

Audit source: Golden Gate commit `15b3366937af19e643a54d564883253f013fc651`,
files `session_handoff/certificates/gieseking_beat.py` and
`session_handoff/certificates/twisted_double.py` (stage 5).  The exact
reproduction is [a3_gieseking_peripheral_beat.py](../experiments/a3_gieseking_peripheral_beat.py).
Their SHA-256 digests are respectively
`7b73758d9ce274bdc477ea7c877121bfdf01777dd2900a3e638602e7875c0a82` and
`4a0fb415c7681e052681ab4c1a703d666751776d8fb883edf5ccda44a5cfeba6`.

## Exact generators and action

Use \(q^2-q+1=0\), \(A=\begin{pmatrix}1&1\\0&1\end{pmatrix}\), and
\(B=\begin{pmatrix}1&0\\q&1\end{pmatrix}\).  The peripheral generators are

\[
 \mu=A=a,\qquad
 \lambda=bABaaBAb,
\]

where the latter is the first stage-5 word under the certificate's stated
search order.  Exact multiplication gives

\[
 \lambda=\begin{pmatrix}-1&-2+4q\\0&-1\end{pmatrix},
 \qquad [\mu,\lambda]=1.
\]

The first beat uses \(W=\begin{pmatrix}1&q\\0&1\end{pmatrix}\), with

\[
 \beta(g)=W\,\overline g\,W^{-1},\qquad \overline q=1-q.
\]

The exact peripheral word matches are

\[
 W\overline\mu W^{-1}=\mu,
 \qquad W\overline\lambda W^{-1}=\lambda^{-1}.
\]

Therefore, in the ordered basis \(([\mu],[\lambda])\), with columns equal to
the images of basis elements,

\[
 [\beta]_{H_1(\langle\mu,\lambda\rangle;\mathbb Z)}
 = \begin{pmatrix}1&0\\0&-1\end{pmatrix},
 \quad \det=-1,\quad \operatorname{ord}=2.
\]

In compact notation, the action is `diag(1,-1)`.

## Why the word matcher is exhaustive

The peripheral normal form is \(\mu^r\lambda^s\), \(r,s\in\mathbb Z\).  Put
\(c=-2+4q\), so \(\lambda=-I+cN\), \(N^2=0\).  For every integer \(s\),

\[
 \mu^r\lambda^s=(-1)^sI+(-1)^s(r-sc)N.
\]

The diagonal fixes the parity of s; the q-coefficient of the upper
right entry fixes s (it is ((-1)^{s+1}4s)); then the rational
coefficient fixes r. Thus the audit's `match_peripheral` solves all of
Z^2 exactly and is not a finite, arbitrary word-length window.

## Fiber-tick contrast

On the fiber basis ([x],[y]), the same certificate has

\[
 x=AB^{-1},\quad y=A^{-1}B,
 \qquad \beta(x)=xxy,\quad \beta(y)=YX,
\]

and hence

\[
 [\beta]_F=\begin{pmatrix}2&-1\\1&-1\end{pmatrix},
 \qquad [\beta]_F^2=\begin{pmatrix}3&-1\\1&0\end{pmatrix}.
\]

The latter is \(GL_2(\mathbb Z)\)-conjugate to the standard Fibonacci
monodromy \(\begin{pmatrix}2&1\\1&1\end{pmatrix}\) (conjugator
\(\begin{pmatrix}1&1\\0&1\end{pmatrix}\)).  It has infinite order, whereas the
peripheral action above has order two.  This is only an exact algebraic
comparison of the two induced actions; no physical interpretation is
claimed.

## Reproduction

```text
$ python3 documents/program-question-map/evidence/a3_gieseking_peripheral_beat.py
...
peripheral H1 matrix (basis mu,lambda) = [[1,0],[0,-1]]
det = -1; order = 2
```

The upstream `gieseking_beat.py` itself was also run from the immutable
commit via `git show ... | python3`; it reports exact intertwining, seven
short beat solutions, and the selected first solution above.  The stage-5
longitude is a representation-level lift; changing the (SL_2) lift by the
central sign changes the displayed lift but not the resulting peripheral
(H_1) action.
