# F03: can the nonsplit cusp carry the required flux without blowing up?

2026-09-20, fork `audit/fork-2026-09-20`, input `50fa3771`.
This is a new fork-local mathematical checkpoint, not a shared B allocation,
an independent banking pass or a completed physical theory.

## Question, scope and expected outcomes

For EVERY smooth source-free harmonic equivariant map to H3 realizing the
rank-two m010 representation below on its complete one-cusped hyperbolic
base, must its cusp Busemann height develop angular oscillation comparable
to its exponentially growing positive mean? In particular, does the entire
class with oscillation o(exp(2r)) fail even WITHOUT a finite-energy hypothesis?

Expected analytic outcome, recorded before computation: yes. A global
positive-flux identity forces the mean height upward. Nonzero peripheral
translation then forces an exponential differential inequality unless the
height varies substantially across the torus. That inequality blows up at
finite r. The shrinking physical torus then implies a corresponding
pointwise angular-gradient lower growth bound. A weighted slice-energy
countercontrol must also show why the
angular dependence cannot simply be averaged away.

Alternative outcome: a sign, inequality, period, growth hypothesis or exact
control fails. Preserve the failed version and narrow the conclusion; do
not call the whole infinite-energy route impossible on that basis.

This is NOT a proof against every wild harmonic metric, against a sourced
equation, or against a rank-four metric not induced by the rank-two map.
It is not a chirality count. The physical action and source/domain questions
from F02 remain intact. No observed constants enter this probe.

## Precise inputs

- M is connected, complete, finite-volume, hyperbolic, dimension three, with
  exactly one rank-two cusp and no finite-distance boundary or source.
- The target is the curvature -1 upper half-space H3, written
  db^2+exp(2b)|dz|^2, b=-log(target height).
- The image preserves b, not merely its ideal endpoint. This is checked
  from unit-modulus diagonal entries of the whole marked triangular image.
- On the cusp, x1,x2 have period one, metric dr^2+exp(-2r)h0, area A0>0,
  h0 any fixed positive flat torus metric. Peripheral action on z is
  z(x+e1)=z(x)-1, z(x+e2)=z(x)+1. Hence K=|(-1,1)|^2_(h0^-1)>0.
- The rank-two representation uses u=(1+i sqrt(3))/2 and flag matrices
  A=[[u,1],[0,1-u]], B=[[-1,u^2],[0,-1]], relator aabaBaaBab,
  mu=AbAA, lambda=babA. Capitals mean inverse and products are left to right.
- Bbar(r) is the flat torus average of b. Omega(r)=Bbar(r)-min_T b(r,.)
  is its downward oscillation. No torus-invariance assumption enters the
  general inequality. The affine radial ansatz is only a contained case.

## Prior and literature boundaries

F01 already supplies the exact witness, finite-energy obstruction, local
cusp and positive global flux bound. F02 supplies the operator-domain
result and explains why finite background energy cannot silently be equated
with the static action. R15/R28 supply different, commuting through-flux
backgrounds. Reuse all of these, with their identities and scopes retained.

`already_banked.py 'nonsplit harmonic cusp infinite energy'` returned 113
lexical hits, no settled arc matching its three-term threshold. Current
reports/frontier/docs searches for Busemann, horospherical, infinite-energy,
Sagman, Lohkamp and Keller-Osserman were also checked. This is not a semantic
absence proof or a claim of novelty in the corpus/literature. The preceding
all-history resweep and its limitations remain the discovery record.

Sagman, arXiv:1911.06937v3, Theorem 1.1 assumes a reductive representation
and a surface source. Its sections 3.2--3.3 and 6.1 do not construct this
three-dimensional nonreductive witness. Section 6.1 instead uses a reductive
replacement for a length-spectrum question. Do not substitute that
replacement for the nonsplit coefficient system that carries the index.
Those HTML sections and definitions were personally read; the whole paper
and its broad Remark 2.6 are not imported as a universal three-dimensional
nonexistence theorem. https://arxiv.org/html/1911.06937v3

## Sealed exact controls

1. Relator/peripheral matrices and unit-modulus diagonal action; a diagonal
   dilation must fail literal Busemann invariance.
2. Derive the cusp Laplacian and radial harmonic-map equation from metric
   density and the energy variation, not by fitting an asymptotic profile.
3. Periodic Fourier energy decomposition for a non-square flat torus;
   unimodular changes of cusp coordinates preserve K.
4. The integrated positive-flux lower bound and multiplier identity for
   u''>=kappa exp(pu), including a finite-time exact comparison solution.
5. Positive local cusp B=-r+log(2/K)/2, with the opposite outward flux;
   K=0 local radial-growth control and an intentionally wrong sign/profile.
6. A smooth periodic slice with affine z-period and nonconstant b disproves
   the tempting lower bound using exp(2*mean b) alone. Preserve this control
   against overextending the obstruction to arbitrary angular behavior.
7. Linearization at the local cusp and its dimension dependence are exact
   checks, not new physical constants or arithmetic uniqueness evidence.

There is no numerical shooting grid, mesh certification or post-result
parameter enlargement. The global theorem rests on the written proof,
not on finite tests. Seal design, proof and test sources by SHA256 and commit
before execution. F01/F02 and other seats' sealed sources remain unchanged.
