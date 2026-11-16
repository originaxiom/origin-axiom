# A finite-series certificate for the proposed cross-form contraction

2026-11-16. PHYSICAL-C5 author hand analysis of X-FRONTIER-3, pending
independent review. No scientific code ran. The upstream symbolic outputs
retain their submitted evidence status.

## 1. Preserve the proposed local algebraic completion

The deciding source is verify_x_frontier_3.py lines 571–703 at
af08bc3d272c01a85e7341da91cfcc43d230d64c. It constructs D5 Clifford
operators on a half-spinor and proposes

    q=E_+ + f_+ T_+,
    r=E_- + f_- T_-,
    a=b [X_(2,2)+(f_+ X_(-2,2)+f_- X_(2,-2))/sqrt(2)
                                      +f_+ f_- X_(-2,-2)/2].         (1)

Its exact matrix commutators test [a,q]=[a,r]=0. This is a constructive
candidate for the pointwise holomorphic equations. Uniqueness is limited
to the stated monomial completion unless a larger classification is
provided. The global field carrying b, its tensor weights and puncture
regularity remain part of the physical construction.

## 2. The five-term series has a hand justification

The source evaluates a homological perturbation series through k=4.
A finite stopping rule needs a certificate. Such a certificate follows
from its principal weights, under its specified contraction identities.

Let H=H_+ + H_- on the ordered 16-dimensional module. Its spectrum lies
in [-3,3]. Use the direct-sum H on the two-copy 32-dimensional module.
Both E operators raise H by one and both T operators lower it by three.
The unperturbed Koszul Laplacian commutes with total H. Its Moore–Penrose
inverse has weight zero. Consequently h1 and h2, which contain the
adjoints of E, lower total H by one. These statements use the ordinary
Hermitian Clifford-module metric in this finite source calculation.

The diagonal blocks of hV in lines 665–671 contain h times a T
perturbation, so lower H by four. The single possible off-diagonal block
contains h times a from (1). Its H shifts belong to {3,-1,-5}.
The block pattern is upper triangular, so a nonzero word contains at
most one such off-diagonal block.

For h_10 V_01 there is no off-diagonal block and (h_10 V_01)^2=0.
For h_21 V_12 and h_32 V_23, every word of length four either lowers
H by sixteen, or lowers it by at least 12-3=9. Both exceed the available
weight span six. Therefore

    (h_21 V_12)^4=0, (h_32 V_23)^4=0.                  (2)

The k=0,...,4 sum used by the source thus contains the entire inverse
series for these finite matrices. The apparent missing tail can be
discharged by (2), assuming the named weights and contraction identities
have their asserted values. A verifier can add explicit matrix checks
of these powers and of d h+h d=1-p. No truncation counterexample is
claimed here.

## 3. The global operator retains its own duty

The finite complex includes a formal horizontal form direction. It does
not solve the actual spatial Dolbeault equation, the real moment equation
or the full complete-domain problem for a variable coefficient b(z).
Those require the global bundle map, actual source Grams and controlled
field response. A pointwise finite contraction can be used in that proof
once its maps act on the declared global sheaves and physical domains.

If the reported cancellation of b in all reduced differentials survives
those checks, it is a scoped positive about this completed family. It
would help avoid repeating an ineffective deformation. Its reported
rank-two singlet comparator uses an explicitly assigned zero row and
column. The proposed endpoint change is represented by inserting
eps_end=1/5 into that matrix. A derived endpoint law and its actual
deformed operator are still required before interpreting that insertion
as a realizable lifting mechanism.

This hand certificate preserves the useful local result and specifies
where the global calculation must continue. It supplies neither an
independent rerun of the matrix cancellation nor a universal exclusion
of both cross-form modes in every stationary physical realization.
