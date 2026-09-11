# B1332 addendum — the strong cusp-locality mechanism is refuted, and the true statement is sharper

B1331 §3 ruled out Galois and named the surviving candidate:

> *the equality is **local at the cusp**. The peripheral holonomy is unipotent … so the boundary data
> cannot tell `V` from `V*` even when the manifold can.*

That has a sharp, decidable form, and if it held it would **be** the theorem.

## The test

Because `psi` is cusp-trivial, the cusp matrices `(A,B)` are **identical** for every cusp-trivial
`psi` — so all the `L_psi` are subspaces of **one** space `H^1(T;W)`, directly comparable with no
identification to choose. (Checked by assertion in every sector, not assumed.) Hence:

> **If `L_V` were determined by `(A,B)` alone, `L_psi` would be the same subspace for every `psi`,
> and `L_V = L_{V*}` would follow immediately.**

## The answer: no — and the shape of the "no" is the result

| | `L_psi` vs `L_1` (trivial) | `L_psi` vs `L_{psi^-1}` (i.e. `V` vs `V*`) |
|---|---|---|
| `s958` `Sym^2, Sym^4, Sym^2+Sym^2, Sym^2+Sym^4` | **different** (4/4) | **SAME** (4/4) |
| `t12833` same four germs | **different** (4/4) | **SAME** (4/4) |
| `t12835` same four germs | **different** (3/4) | **SAME** (4/4) |

> ## `L_V` **moves** with `psi` — it is not a cusp invariant — but it is **fixed by `psi -> psi^-1`**.

So the strong cusp-locality mechanism is **dead**: the boundary data does not determine `L_V`, and
therefore cannot be the reason `L_V = L_{V*}`. What survives is a strictly sharper statement than
either B1331's guess or its headline — the family `psi |-> L_psi` is non-constant yet invariant
under inversion. Whatever proves the theorem must act on that family and fix it under `psi -> psi^-1`
**without** being constant. Galois (B1331 §3) and cusp-locality (here) are both excluded; the
mechanism is neither.

(The one exception, `t12835` at `Sym^4`, has all three subspaces coinciding — a degeneracy, not a
counterexample: `L_psi = L_{psi^-1}` still holds there.)

## A near-miss worth recording

The first version of this test compared **all** characters together and reported "different
subspaces" for every germ — which reads as a refutation of B1331's *finding*, not merely of its
proposed mechanism. It was an artifact: the trivial character was in the pool, and it differs from
the others for reasons that say nothing about `V` versus `V*`. The pairwise breakdown above is what
the question actually asks. **A confound in the comparison set nearly produced a false refutation of
a correct earlier result** — the mirror image of the vacuity trap in §2 of the main findings, where
a too-weak test nearly produced a false confirmation.

Reproduce: `verification/cusplocal.py <manifold>`; logs in `verification/logs/`.
