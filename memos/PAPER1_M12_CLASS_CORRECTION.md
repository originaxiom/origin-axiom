# Paper I's m=12 class-count discrepancy is proper versus improper equivalence

## Verdict

The Paper-I theorem restricted to \(m\le 11\) is unaffected, including the
first repetition at \(m=6\).  Its recorded disagreement at \(m=12\) can now be
resolved exactly:

\[
h_{\mathrm{proper}}(148)=3,
\qquad
h_{GL}(148)=2.
\]

The paper's reduction routine returns three proper cycles but labels its output
as full \(GL(2,\mathbb Z)\)-equivalence.  The missed determinant-\(-1\)
operation is already visible on representatives.  The variable swap
\((x,y)\mapsto(y,x)\) sends

\[
-7x^2+6xy+4y^2
\quad\longmapsto\quad
4x^2+6xy-7y^2,
\]

so two of the three proper classes are one improper class.  The remaining
principal cycle is fixed by the improper action, leaving exactly two full
\(GL\)-classes.

The corrected counts through \(m=12\), for discriminant \(m^2+4\), are:

```text
proper: 1,1,1,1,1,2,1,1,2,2,1,3
GL:     1,1,1,1,1,2,1,1,2,2,1,2
```

## Consequence

Paper I should replace its unresolved-disagreement remark with this
proper/improper distinction and ensure its class-count routine quotients by a
genuine determinant-\(-1\) transformation, not only by the opposite form.
The threshold claim \(m=6\) remains correct.

This is arithmetic of indefinite binary quadratic forms.  It does not repair
the conditional substitution-to-oriented-manifold functor OA-C0003.

## Certificate

`certificates/r010_gl_class_m12.py` is a standard-library exact reduction and
orbit computation.  It enumerates proper cycles and then explicitly quotients
by the determinant-\(-1\) variable swap.
