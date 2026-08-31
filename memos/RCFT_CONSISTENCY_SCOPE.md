# R031B — primary-literature audit of the RCFT consistency route

## Verdict

B1229/B1230's `sigma` route remains open and is more conditional than its
current headline.  The Anderson--Moore/Vafa rationality implication is real,
but the premise needed to apply it to the geometric complex Chern--Simons
theory of `m004` is not established.  Even if that premise is granted,
rationality gives `sigma in Q`; it does not give a finite menu or remove the
need to specify a rational number.

The subsequent `Z/3` cut is also untyped.  Three different objects are being
identified without a map:

1. the trace field `Q(zeta_3)=Q(sqrt(-3))`, whose Galois group over `Q` is
   `Z/2`;
2. the order-three cyclic permutation in trinification;
3. a possible order-three simple-current/fusion group of a chosen RCFT.

Equality of the numeral `3` is not an identification.  Consequently the
B1230 C-5b recovery does not select `E6`.

## What the primary literature actually establishes

Anderson and Moore prove rationality of central charge and conformal weights
under finite holomorphic/antiholomorphic factorization of a modular-invariant
partition function.  Vafa obtains related root-of-unity/rationality
constraints from finite modular data.  These are implications from an RCFT
premise, not converses and not classifications:

- G. Anderson and G. Moore, *Rationality in conformal field theory*,
  [Commun. Math. Phys. 117 (1988)](https://doi.org/10.1007/BF01223375).
- C. Vafa, *Toward classification of conformal theories*,
  [Phys. Lett. B 206 (1988)](https://doi.org/10.1016/0370-2693(88)91603-6).

For compact gauge group at integral level, Chern--Simons quantization does
produce finite-dimensional WZW conformal blocks.  The actual route here is
complex/noncompact `PSL(2,C)` on a cusped hyperbolic manifold.  Witten's
complex-group quantization instead has infinite-dimensional physical Hilbert
spaces and explicitly leaves the existence of a related 1+1-dimensional CFT
unclear:

- E. Witten, *Quantization of Chern--Simons gauge theory with complex gauge
  group*, [Commun. Math. Phys. 137 (1991)](https://doi.org/10.1007/BF02099116).

The figure-eight state-integral literature constructs perturbative and
holomorphically factorized invariants, but finite state-integral blocks are
not a finite RCFT character decomposition.  The arithmetic-TQFT statement is
conjectural and ideal-triangulation integrals generally capture a subsector:

- T. Dimofte, S. Gukov, J. Lenells and D. Zagier, *Exact results for
  perturbative Chern--Simons theory with complex gauge group*,
  [arXiv:0903.2472](https://arxiv.org/abs/0903.2472).
- T. Dimofte, *Complex Chern--Simons theory at level k via the 3d--3d
  correspondence*, [arXiv:1409.0857](https://arxiv.org/abs/1409.0857).

Thus the load-bearing statement “the boundary of a Chern--Simons theory is
rational” is true only in a narrower compact/integral setting and is not a
theorem about the `m004` setup used by the programme.

## What MMS classifies

Mathur--Mukhi--Sen organize character candidates by the number `n` of
linearly independent characters and Wronskian index `l`.  The famous finite
classification is the `(n,l)=(2,0)` modular-differential-equation problem,
with regularity, integrality and positivity/physicality filters.  It is not a
classification of all RCFTs:

- S. Mathur, S. Mukhi and A. Sen, *On the classification of rational
  conformal field theories*,
  [Phys. Lett. B 213 (1988)](https://doi.org/10.1016/0370-2693(88)91765-0).
- A. R. Chandra and S. Mukhi, *Towards a classification of two-character
  rational conformal field theories*,
  [arXiv:1810.09472](https://arxiv.org/abs/1810.09472).
- A. Das, C. Gowdigere and J. Santara, *Wronskian indices and rational
  conformal field theories*,
  [arXiv:2012.14939](https://arxiv.org/abs/2012.14939).

The seven unitary level-one WZW entries are a filtered part of the `(2,0)`
candidate table, not an unrestricted RCFT menu.  The number of independent
characters is also not the number of primary modules: conjugate or triality
related modules can share a character.  Therefore neither “two characters”
nor a three-primary count is supplied by the object.

## Why B1230 is still not restriction-free

The exact WZW central-charge formula

```text
c(g_k) = k dim(g)/(k+h_dual)
```

does have exactly four `c=6` solutions among all simply-laced simple WZW
families at positive integral level:

```text
A2 at k=9, A6 at k=1, D6 at k=1, E6 at k=1.
```

R031B re-derives this without the reported `k<=12` search bound.  This is a
valid exact result inside the simply-laced WZW class.  It is **not
restriction-free**: the unearned restriction has moved from “two-character,
Wronskian zero” to “simply-laced WZW at positive integral level.”  General
RCFTs, cosets, orbifolds, minimal models, extensions and non-semisimple or
non-rational boundary theories are not covered.

Rationality alone also does not repair this.  `Q` is infinite and dense in
`R`; for arbitrary `N`, the `N` numbers `j/(N+1)` lie in `(0,1)`.  Declaring
`sigma` rational changes its arithmetic type but does not make it a finite
label or derive its value.

## The three distinct threes

The trace-field inference has a decisive order check:

```text
[Q(zeta_3):Q] = phi(3) = 2,
Gal(Q(zeta_3)/Q) = Z/2.
```

The RCFT Galois literature concerns the cyclotomic field generated by a
theory's already existing modular `S,T` data and its induced permutations of
primaries.  It does not map an arbitrary hyperbolic trace field to a fusion
group:

- P. Bantay, *The kernel of the modular representation and the Galois action
  in RCFT*, [arXiv:math/0102149](https://arxiv.org/abs/math/0102149).

Trinification supplies a separate cyclic permutation of three factors.  To
use it as a cut one must construct a typed homomorphism or functor from that
action to the boundary modular category/simple-current group.  No such map is
present in B1229/B1230 or in the cited literature.

## Additional inference: level blindness is not level selection

B1228's statement that `k=1` is forced because the object supplies no level
datum reverses the logic.  If the action at the selected geometric saddle is
blind to `k`, then `k` is unidentifiable there.  Choosing the smallest allowed
level is a minimality convention unless an independent consistency theorem
excludes every `k>1`.  Absence of a receiver for a datum does not select the
datum's default value.

## Correct status

The sigma chain is therefore:

```text
IF an ordinary finite RCFT boundary is constructed for the actual m004
complex-CS sector,
THEN c and h are rational.

IF that boundary also lies in a specified MMS/WZW class,
THEN a finite class-dependent menu may follow.

IF a typed map identifies the object's trinification action with a boundary
fusion/simple-current action,
THEN an order-three cut may be applied.
```

All three antecedents are open.  `sigma=1` remains open; even `sigma` being a
finite label is not presently established.

## Post-send scope note on outside-bench Q11

The outside bench sent Q11 to Tudor Dimofte immediately before this audit was
committed, from a branch whose mainline merge-base predates B1224--B1230.  The
email is a legitimate bounded request for a mechanism or obstruction, but two
sentences must not be imported back into the programme as established facts:

1. For `m004`, `CS=0` is an independently verified contingent datum.
   Amphichirality alone implies only `2 CS=0` in the value group; B1224/B1226
   exhibit amphichiral manifolds at the nonzero two-torsion value `1/4`.
   Therefore the email's causal phrase “because m004 is amphichiral, CS=0” is
   false even though its conclusion for `m004` is true.
2. A construction of some boundary invariant would not by itself fix
   `sigma`.  It would still have to prove a finite/selective boundary category,
   identify the relevant central charge with `6 sigma`, and type the nominated
   `E6` datum into that category.  B1230's four WZW solutions already show that
   `c=6` alone does not select `E6_1` inside its own stated class.

Likewise, `CS=0` makes the displayed classical geometric saddle action blind
to `k`; it does not by itself prove that the full quantum theory has no
integer-level sector.  These are record corrections only.  No unsolicited
follow-up communication is authorized or required by this audit.

Question-map disposition: update `OA-C1151` but retain `OPEN`; add a new
question-map row for the RCFT-boundary applicability question, also `OPEN`.

## Reproduce the exact controls

```text
PYTHONDONTWRITEBYTECODE=1 python3 certificates/r031b_rcft_scope/rcft_scope.py
```
