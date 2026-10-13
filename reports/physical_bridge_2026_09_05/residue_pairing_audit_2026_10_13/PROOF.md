# The raw residue tensor is not the symmetric golden matrix

Read main B1642's preregistration and complete residue_coupling.py at
55bd29ab7 before this audit. In Y_of the matrix in the bilinear is
C_p^T epsilon C_q, with epsilon=QJ and blocks QJ,QI,QK. The profile
components in quad are ordinary commuting complex functions.

Since epsilon^T=-epsilon,

    (F_p^T epsilon F_q)=-(F_q^T epsilon F_p).

Taking a residue is a linear operation and preserves that identity.
It is unaffected by the square-root branch, contour radius or theta
duplication identities. Hence Y^T=-Y and detY=0, exactly, for all tau
where the stated profiles and residue exist. This is already decisive
against R4's three nonzero singular values.

Write a generic such matrix as [[0,a,b],[-a,0,c],[-b,-c,0]]. Put
q=(c,-b,a) and m=|a|^2+|b|^2+|c|^2. Direct multiplication gives
Y^*Y=mI-q q^*, so its eigenvalues are m,m,0. If nonzero, the normalized
singular values are1,1,0, not1,phi^-1,phi^-2. The probe checks the full
polynomial in six real components; exact finite controls are separate.

The symmetric comparison [[0,a,b],[a,0,c],[b,c,0]] has det2abc. Thus
replacing the lower triangle's signs changes the tensor and can change
rank. It cannot be justified as a unitary row/column rephasing, which
preserves rank. It would require an actual additional physical vertex
or representation contraction.

The residue identities for individual entries remain a potentially
useful positive. An E8/gauge/Higgs/fermion vertex might supply further
symmetry factors. That is not present in the literal Y_of computation
and is not refuted by this audit. The physical family mass matrix must
be derived from the full parent rather than named after a modular
texture. No architecture-wide no-go or scientific novelty is claimed.
