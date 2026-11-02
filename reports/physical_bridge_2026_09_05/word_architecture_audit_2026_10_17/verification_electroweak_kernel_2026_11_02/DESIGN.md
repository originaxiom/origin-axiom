# Complete two-triple kernel: finite-control design before implementation

November 2, 2026. AFTER the authored analytical proof,
BEFORE creating, importing, collecting or executing checks.py.
This is a verification design, not prospective discovery or permission
to execute. The old eight-control package is unchanged.

## Question, population and decision

Finite exact controls for the complete248 two-triple decomposition,
source flat/spin phases and zero-mode arithmetic in
ELECTROWEAK_TWO_TRIPLE_PHYSICAL_KERNEL.md. Prior: the author expects
all six named methods of ElectroweakKernelChecks below to pass.
Every method must run exactly once with no skips, xfails, missing
population or interruption. Preserve a failed run and halt its claim;
corrected sources require a separately recorded seal before rerun.

The finite tests do NOT prove the complete graph-domain contraction,
closed-range transfer, full physical operator isometry or a generated
physical action. Those remain separately reviewed analytical duties.
Counts are complex chiral REPRESENTATION DIMENSIONS unless explicitly
labelled multiplicity per irreducible coefficient. The gaugino/C3
kernel is counted once as physical Weyl data, not again as a chiral.

## Declared conventions and sources

Retain the original once-punctured elliptic complete domain, S^2=K,
extending spin eta, unitary chi of exact order three, old E8 coordinate
frame w=(0,0,0,-1,1,-2,0,2), QY=(5,5,5,-3,-3,-3,-3,-3)/2 and
Q_em=(2/3,2/3,2/3,0,0,0,0,0). The actual old pole law is
b(a)=floor(a/2) for a<=0, ceil(a/2)-1 otherwise; degree-zero sections
are present exactly when eta^a L is trivial. No compact Euler proxy.

The faithful D5 vector model and E,G,H are the previous branch's explicit
ten matrices. Use that source, but do not import or rerun its unreviewed
module as a scientific producer without an exact declared binding.
The new implementation may reconstruct the same matrices directly,
with source hashes and a transparent duplicate/arithmetic limitation.

For the spinor control use the32-dimensional exterior algebra of C5
with orthonormal ordered wedges, creators c_i-dagger and their actual
annihilation adjoints. For X=[[A,B],[C,-A^T]], B,C skew, its spin action is

  sum A_ij c_i-dagger c_j - Tr(A)/2
    + (1/2)sum B_ij c_i-dagger c_j-dagger
    + (1/2)sum C_ij c_i c_j.

Even/odd parity give the two actual16-dimensional half spinors.
Root adjoints and the commutator map must be checked before trusting
their weights. No literal transpose replaces a Hermitian adjoint.
Only total S powers are used: there is no S^(1/2) or new fourth root.

Proposed runtime: CPython3.12.1, SymPy1.14.0, mpmath1.3.0,
PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1, SYMPY_GROUND_TYPES=python,
optimization disabled. It has not been revalidated for this package.
No empirical target, random sample or fitted datum is read.

## Six methods, with positive and rejecting controls

1. `test_explicit_two_triple_split_and_orthogonal_form`: reconstruct
   B_Z,J,E,G,H, check B_Z J=E5/sqrt10, the two stated unitary frame
   changes with transported orthogonal form, and the two independent
   compact triples. Check all cross commutators, their sum giving E/H
   and G their difference. Omitting the J frame must fail the literal
   tensor identity. A collapsed G=E must not retain two nonzero triples.
2. `test_full_D5_A3_population_and_actual_half_spinors`: reconstruct
   all240 E8 roots and eight Cartans, classify40 D5 roots,12 A3 roots,
   60 integer cross roots and128 half roots by actual coordinates.
   Construct the Fock spin action above, check its adjoints and a
   spanning set of D5 brackets; recover joint weights of both16s by
   exact spectral projectors for H_+,H_-. Each of the16 pairs of
   weights(±3,±1) in the H normalization must occur once in EACH half.
   The full table must sum to248 and its diagonal restriction recover
   (24,11,21,11,1). Dropping one half spinor must fail both populations.
3. `test_actual_Koszul_generator_change_and_extreme_grading`: construct
   rational principal modules for all(j,k) in the full table, with
   their actual positive binomial Gram; build the two-generator Koszul
   maps, verify all differentials and the invertible a,b change in
   each exterior degree. Recompute the finite graded cohomology to
   obtain the four declared extreme S exponents and dimensions1,2,1.
   Keep the degree1 signs and determinant slot. At b=0 the inverse
   must fail for a genuine two-sided module; do not extend an interior
   contraction through that singular endpoint.
4. `test_full_root_flat_phases_and_colour_EM_assignment`: compute
   QY mod3 and EM from EVERY E8 root, distinguish D5 adjoint, A3
   adjoint, cross vector and both half-spinor populations. Check
   the colour6 lines chi^(+/-1), the4 singlet L=O and colour L=chi,
   and the conjugate assignments; recover nine untwisted A3 adjoint
   directions and six nontrivial-line components. A wrong use of
   order-seven charge aliases must change a known root's character.
5. `test_exact_pole_counts_all_spins_and_complete_physical_totals`:
   compute h0,h1 with the actual cusp endpoint and all four spin
   characters; apply the four-line formula to every module and
   coefficient character. Recover63/87 chirals,9 vectors/gauginos
   and72/96 total physical left zero modes. Recompute the OLD R=0
   order-three roster as112/136 chirals and12 vectors, without using
   the new interior contraction at that endpoint. Wrong b(2)=1 must
   fail an endpoint comparator. Omitting C3/gaugino must fail the
   full physical count without being disguised as extra chiral matter.
6. `test_charged_roster_pairs_and_massless_up_control`: assemble the
   full colour/EM multiplicity table from the module/source populations,
   not a saved transcript. Recover four EACH conjugate up components,
   two EACH conjugate down components, two/four EACH charged singlets,
   one/three colour adjoints and15/19 neutral singlets. Verify equal
   conjugate counts and the12-to9 gauge jump, with the full chiral
   dimension check as an independent sum. A missing companion or
   doubled conjugate population must fail. The up-zero conclusion
   comes from actual(2,0)/(0,2) dimensions, not an asserted Yukawa zero.

## Implementation and execution boundary

Commit this design before creating checks.py. Static AST, test-name
population and source-hash metadata may be inspected after implementation;
no scientific import, collection or execution is admitted by this design.
Do not borrow the eight-control, radial or P210 acceptance.

Complete source/input/test/environment closure, own wrapper engineering
verification, genuine independent proof/code review, main's separate
exact acceptance and strict prospective admission on a clean quiescent
checkout remain required. No output path or runnable wrapper is provided.
Failed historical experiments and all earlier seals remain unchanged.
