# CELL F — L104, the CP decider: **CONVENTION**

**Question (B660/S2, honest partial banked).** Does there exist
g in GL(5,K), K = Q(sqrt(-3)), with (Lambda^3 g).Y = Ybar — the chord
3-form vs its Galois conjugate?

**Verdict: CONVENTION.** Two independent explicit solutions exhibited
and verified exactly (all 10 components over K, Fraction arithmetic,
no floats in any decisive step). The Y-vs-Ybar asymmetry is a basis
convention, not a forced CP-like distinction.

## The two solutions

1. **g = M, the persisted wave-1 sigma matrix itself** (cheap step 1).
   The lower-triangular matrix in `cellC/sigma_matrix_golden.json`,
   read K-linearly (no coefficient conjugation), satisfies
   **(Lambda^3 M).Y = Ybar exactly** in the convention
   (g.Y)_{ijk} = sum g_{ia} g_{jb} g_{kc} Y_{abc} (rows = sigma*'s row
   convention). det M = 1. The banked B660 statement "the deck swap
   gives -Y not Ybar" is the *antilinear* statement about
   sigma* = M o conj as a map; its K-linear matrix part alone was
   never persisted before wave 1 and turns out to BE the answer.
   (M^T does not work — the row convention is load-bearing.)

2. **A structurally independent g from the K-normal form** (step 3),
   persisted in `cellF/g_certificate.json`: det g = 1,
   (Lambda^3 g).Y = Ybar verified exactly, and moreover
   **conj(g).g = I exactly** — u -> g.conj(u) is an antilinear
   involution, i.e. a genuine Galois descent datum for Y.

## Why no K-obstruction could survive (the theorem behind the verdict)

For a trivector T on a 5-space over any field k (char != 2) of the
banked GENERIC/OPEN type (flattening B(v,w) = T^v^w of rank 4):

- ker B = <v0> is a line, and v0 in ker B **forces** T = v0 ^ S with
  S a nondegenerate 2-vector on the quotient (the Lambda^3<w>
  remainder dies on 0 = T^v0 = v0^T');
- Darboux over any field puts S into e1^e2 + e3^e4 exactly, the
  scalar being absorbed into v0.

So the generic type is a **single GL(5,k)-orbit** — no arithmetic
invariant exists over K at all. Both Y and Ybar were brought to
N = e0^(e1^e2 + e3^e4) exactly (verified), and g = u2^{-1} u1. The
B660 X^3 = c irreducible-cubic obstructions were artifacts of the
monomial/diagonal ansatz: the general group absorbs the cube through
the kernel-line scaling; no cube root is ever needed.

## Decisive numbers

- Y support (banked, B660/S2): {023, 034, 123, 124, 134, 234}; Y != Ybar.
- rank(B_Y) = rank(B_Ybar) = 4; kernel lines
  v0(Y) = (0, 0, -3991680/13 (1+sqrt(-3)), 0, 1), v0(Ybar) = its conjugate.
- dim_K Stab_{gl(5)}(Y) = **15** (exact 10x25 K-linear system), orbit
  dimension 10 = the open orbit; structure = 4-dim unipotent x| GSp4
  (dim 4 + 11 = 15). The full solution set of g.Y = Ybar is the
  15-dimensional coset Stab(Y).g.
- Scalar freedom: omega.g, omega^2.g also solve
  (omega = (-1+sqrt(-3))/2 in K, omega^3 = 1).
- Prereg step 4 (mod-p evidence) superseded: an exact K-point exists.

## Verification discipline

- All claims asserted in-script (`l104_decider.py`), full log in
  `cellF_output.txt`.
- Independent minimal re-implementation of the action re-confirmed:
  act(I,Y) = Y, act(M,Y) = Ybar, act(g_cert,Y) = Ybar, and the
  left-action axiom act(A.M, Y) = act(A, act(M,Y)) on a random exact A.
- Controls: conj(M).M = I reproduced (banked wave-1 law); Y != Ybar
  nontrivial; both normal forms reached N exactly.

## Interpretation for the campaign

The CP question at the level of the chord 3-form's field of
definition is **decided: convention.** Y admits a descent datum
(conj(g).g = I), so nothing in the 3-form alone pins a complex
chirality over K. Any forced CP-like fact must therefore live in
structure *beyond* the bare GL(5)-orbit of Y — e.g. the interaction
of sigma* with the boundary/solo split or the ladder grading, where
the acting group is smaller than GL(5).

## Files

- `frontier/B662_successor_campaign/cellF/l104_decider.py` — the decider (exact).
- `frontier/B662_successor_campaign/cellF/cellF_output.txt` — full run log.
- `frontier/B662_successor_campaign/cellF/g_certificate.json` — the explicit g, det g, conventions, verdict.
