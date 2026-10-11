# The algebraic matter precursor needs less than the full free carrier

2026-10-11. Author: originaxiom. Local analytic proof with exact safeguards; independent acceptance and full publication certification pending.

For the specified quaternion doublet coefficients, the free group's degree-one cohomology and its lifted move representation survive unchanged on the proper quotient F2/F2'''. They do not survive on any metabelian quotient carrying the same doublet: there the cohomology is zero. This gives a precise dependency for the existing algebraic six-dimensional space, without claiming that the space is physical matter.

The result is a weakening of the required carrier for this construction, not a derivation of the carrier, coefficient system, geometry or physical dictionary from existence. The once-punctured-torus theorem conditional on faithful F2 is untouched.

## The information retained at each level

Write G_d=F2/F2^(d), where the superscript denotes the derived series, not a power or a generation label. The coefficient choices are fixed throughout the comparison.

| Carrier | All positive words retained | Sign-character H1 per nonzero parity | Quaternion point retained | Quaternion-doublet H1 per parity |
|---|---|---|---|---|
| G_1=Z² | No | 0 | No | Not defined with these generators |
| G_2=F2/F2'' | Yes | 1 | Yes | 0 |
| G_3=F2/F2''' | Yes | 1 | Yes | 2 |
| F2 | Yes | 1 | Yes | 2 |

The three nonzero parity characters give the first algebraic triplet in B1600. The three quaternion doublets give the later algebraic six, split by the central move action into two triplets. These are different constructions, not interchangeable occurrences of the number three.

The [proof](PROOF.md) establishes all-word statements. The finite checks below safeguard implementations and explicit witnesses; their counts are not the scope of the theorem.

## A relation that measures the extra information

Let c=[a,b] and r=[c,a c a^-1]. The word r lies in F2'' and is not trivial in F2; its freely reduced spelling is

    abABaabABAbaaBAA

of length sixteen. Its quaternion image is the identity. Nevertheless, after normalizing a doublet cocycle to z(a)=0, it satisfies

    z(r)=4 z(b).

Thus the relation r=1, which every metabelian quotient imposes, removes every nonzero class in that doublet H1. The calculation is exact for every parity twist. This is an explicit signed-word distinction required by the record's own coefficient construction, not an invented physical observable.

The next quotient does not impose r=1. It instead kills F2''', which all these cocycles already annihilate. A nontrivial element killed there is t=[r,a r a^-1], whose freely reduced length is fifty-four; its complete spelling is in the [second-run output](NATIVE_SECOND.txt). Two reduction algorithms verify that it is nonempty. Therefore G_3 is a proper quotient, not another presentation of faithful F2.

## Why the complete move representation survives

For any representation rho with solvable image of derived length at most d, a cocycle z defines a homomorphism w→(rho(w),z(w)) into the affine group V semidirect rho(F2). That group's derived length is at most d+1. Every cocycle therefore descends through F2/F2^(d+1), as do the coboundaries, giving an isomorphism on H1.

The quotient is characteristic, so that isomorphism commutes with the automorphism pullbacks and their specified intertwiners. For Q8, d=2. Hence the full lifted six-dimensional module, not just its dimension, survives on G_3. The exact central projectors retain ranks three and three. The central-lift sign is preserved, not silently divided out.

The formula is a general sufficient bound. Its sharpness here is established separately by the metabelian vanishing proof. Derived depth three is necessary and sufficient within this class for nonzero H1 with the prescribed doublet. It is not a generation prediction.

## Execution and correction

The original design, proof and source were sealed before execution at `32a85c10bd9507ef5ee508785794c0ec8caca69f`. The first run exited 1 while comparing an unexpanded exact matrix with zero. Diagnostic expansion gave the zero matrix; the discriminating relation still gave 4I. The mathematics and test population did not change.

[CORRECTION_V2.md](CORRECTION_V2.md) and verify_v2.py were sealed at `5d64cd31c81423866fb10e27153cb79d7e461614` before the second run. The repair compares exact polynomial entries and adds positive and negative comparator controls. The second run exited 0 with **3,626 exact assertions passing**, using SymPy exact arithmetic without numerical tolerances. Eight nontrivial F2'' fixtures and sixteen F2''' fixtures supplement the explicit relation and independent block-affine evaluator. The original scientific files remain unchanged.

The first raw traceback is retained locally byte-for-byte. Because it contains a private absolute path, the repository contains [a mechanically redacted copy](NATIVE_FIRST_PUBLIC.txt), with hashes for both copies in FIRST_FAILURE_HASHES.txt. This is a second-run success, not an unblemished first pass. The defect matches the repository's existing exact-expression comparison warning in ERROR_LEDGER E75; it was not a new mathematical obstruction.

## Seen first

The completed citation is:

    VERDICT topic-sweep /metabelian|derived series|solvable quotient|inflation.*cohom|cohom.*inflation/: 0 of 1408 arcs on pinned main; 19 other retained lanes match

[SOURCE_SCOPE.md](SOURCE_SCOPE.md) records the source pins, screened matches, primary literature and reading limits. Main's GENESIS, P000 and P008, B1600's report and the earlier local cocycle proof and code were read. The SM B1510 affine-extension work was located and its relevant scope inspected; no result from it is adopted here. The group-cohomology literature supplies the standard terminology of inflation; the particular descent and vanishing arguments are rederived in PROOF.md. No originality or repository-wide absence is claimed.

## What changes and what does not

The preceding positive-carrier check showed that positive-word retention does not force faithful F2. This check supplies the requested concrete discriminator: doublet cocycles detect a relation that the quaternion point alone misses. But it also prevents an overcorrection: those cocycles still do not require full F2, since G_3 retains them equivariantly.

Consequently there is no reason to make recovering full F2 from positive words a prerequisite for studying this algebraic module. Its weaker sufficient carrier is now explicit. The extra work must be attached to the actual subsequent dependency: geometric polarization, a differential operator and domain, or the physical field dictionary, whichever a claimed step uses.

No surface metric, Hodge polarization, holomorphic matter identification, boundary unit, kinetic action or empirical parameter follows from the quotient comparison. In particular, ordinary group H1 with doublet coefficients is not adjoint representation deformation theory and is not a physical chiral index. The next root task is to trace precisely which extra structure Λ and the end-law construction consume, using their existing producers and the physical branch's same-action work, rather than enumerate more quotient examples.

No shared B number is allocated and canonical GENESIS is unchanged. The theorem-shaped content is captured in [LAW_MAP_PROPOSALS.md](LAW_MAP_PROPOSALS.md) for normal review and adoption.
