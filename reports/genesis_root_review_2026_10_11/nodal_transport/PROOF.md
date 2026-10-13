# Local node transport and its exact contraction

This is a local theorem for the existing coefficient and plumbing, not a global physical index. The supplied rank-six field, lifted moves and nodal geometric model are retained. It provides actual peripheral data for the total-space domain duty carried by fibre_family; it does not choose that domain.

## The map from the node to the based group

Use the primitive nodal smoothing xy=q already used in cusp_spin_extension. The two coordinate meridians mu_x and mu_y commute, each maps to one positive loop in q, and the vanishing circle in a fixed fibre is mu_x mu_y^-1. The complement of the two axes in a small bidisc retracts to a two-torus. The standard nodal local equation is also described in Stacks Lemma53.20.11; its general completed equation is xy=h. Here q is the primitive smoothing parameter, not an unannounced ramified base change. [Primary local model](https://stacks.math.columbia.edu/tag/0C58).

In the existing cusp mapping-torus group

    G = <a,b,t | t a t^-1=a, t b t^-1=ab>,

the subgroup <a,t> is a copy of Z^2. Projection to the t exponent proves independence: a^m t^n=1 forces n=0, then m=0 because F2 is torsion free. To retain the base point correctly, do not assume the meridian corresponding to one coordinate equals the symbol t in every chart.

Every element over one positive base loop has the form h t with h in F2. If it commutes with a, then h commutes with a. The reduced-word centralizer of the primitive generator a in F2 is <a>; this also follows from its unique axis in the free-group tree, as in word_lifts. Hence the centralizer elements over that base loop are exactly a^k t. The relation mu_x mu_y^-1=a forces

    mu_x -> a^(k+1)t,    mu_y -> a^k t,
    k any integer.

The exponent-pair matrix of these two generators in <a,t> has determinant1, so this is an injective peripheral map for each framing, not only a formal relation. It exhausts the stated based framings with this vanishing cycle and projection. Exchanging branches reverses the vanishing cycle. Reversing loop orientations or simultaneously changing the coefficient frame gives equivalent versions below. This does not classify new base covers or replace the given primitive degeneration.

The distinction between [a,b] and the based word a b^-1 a^-1 b fixed by the chosen L,R is already recorded in word_lifts. Both evaluate to -I in this coefficient, but their based paths must not be silently equated. Carrying every k makes the result independent of that meridian-framing ambiguity. It is not an extra physical parameter.

## The actual matrices force an eighth root on each branch

In the ordered parity blocks (2,0),(0,2),(2,2), written as powers of i, set

    a0=diag(i,-i), b0=[[0,1],[-1,0]],
    A=diag(-a0,a0,-a0), B=diag(b0,-b0,-b0),
    T=P13 tensor diag(exp(i pi/4),exp(-i pi/4)).

These are the literal W24/W46 matrices, not the three-dimensional cohomology representation substituted for the local six. Direct multiplication gives

    T A T^-1=A,   T B T^-1=A B,
    [A,B]=-I6,   A^4=I6,   T^4=-I6.

Thus W is a representation of G with the advertised geometric automorphism. For either overall lift sign eps=+/-1 the node matrices are

    U=eps A^(k+1)T,    V=eps A^k T.

They are commuting unitary matrices, U V^-1=A, and U^4=V^4=-I6 for EVERY integer k. In particular their eigenvalues belong to the four odd eighth roots of unity and neither has eigenvalue1. Inversion and conjugation preserve the fourth-power identity. Independent spin signs on the two flat angular circles also preserve it. These signs are comparisons of flat-link spin structures, not a derivation of the actual total-space spin connection.

One can read the complete joint spectrum by simultaneously diagonalizing A and T. A joint eigenvector with A=exp(2 pi i a) and T=exp(2 pi i t0) gives node exponents ((k+1)a+t0,ka+t0), reduced modulo1. The exact verifier constructs this basis and checks it against the literal matrices. No branch framing is selected by an attractive exponent table.

## A contraction proves the local cohomology statement

Put P=U-I and Q=V-I. Since U^4=-I,

    P^-1 = -(I+U+U^2+U^3)/2.

Both left and right inverse identities follow by the telescoping product U^4-I=-2I. Because U and V commute, P^-1 commutes with Q. The cellular cochain complex of the angular two-torus is

    C6 --d0--> C12 --d1--> C6,
    d0=[P;Q],    d1=[-Q,P].

Define h1=[P^-1,0] and h2=[0;P^-1]. Matrix multiplication gives

    h1 d0=I6,
    d0 h1+h2 d1=I12,
    d1 h2=I6.

This is an explicit chain contraction. The original local system's ordinary cohomology on this bidisc complement is therefore zero in every degree. The annular vanishing circle separately has A-I invertible, so its ordinary local-system cohomology is zero as well. Neither statement says the whole elliptic fibre has zero index or zero modes. Its marked puncture and global cohomology are different data, preserved by the previous proof.

For the FLAT angular metric dtheta_x^2+dtheta_y^2 with each period2pi, diagonal joint phases alpha,beta give squared covariant frequencies (m+alpha)^2+(n+beta)^2. Every distance to an integer is at least1/8 under every spin sign, hence the sum is at least1/32. This is a reference-link estimate only. The total metric varies, has a long and short fibre direction, and couples horizontal and vertical derivatives. This bound by itself is not a uniform end gap, graph-domain theorem or proof of a total Dirac index.

## What the local data do and do not determine

For the canonical logarithmic extension one may choose simultaneous exponents alpha,beta in [0,1). In an equivariant-section convention its scalar local generators are x^alpha y^beta; changing to flat-frame residues reverses the corresponding holonomy sign, without affecting the statements above. Multiplication by q^n=(xy)^n adds the integer n to BOTH exponents and changes neither U nor V. This holds for every integer n, not just a finite scan. It changes extension/divisor data, not the punctured local system. Imposing a canonical exponent interval is a specified extension prescription; it is not a dynamical derivation of a nonzero unit.

On the local eightfold power cover in BOTH coordinate directions, U^8=V^8=I, and the pulled-back local system has the ordinary trivial-coefficient torus cohomology (6,12,6). That does not contradict the original contraction. The finite deck action must be retained on descent; the averaging operator (I+U+...+U^7)/8 vanishes since U^4=-I. Counting cover invariants before that projection would count a different object.

The useful output is explicit nonresonant local transport and a contraction for the actual rank-six coefficient, robust to the stated basing and spin conventions. Local flat holonomy alone cannot distinguish the existing integer cusp extensions; this is a scoped statement about one discriminator, not a no-go for an action, anomaly, source or global admissibility rule selecting one. The older genus count and W45/W46's conditional index are not retracted by this local zero.

To finish the carried total-space step, use these matrices in the metric-dependent normal operator and the actual coefficient/spin extension; then prove uniform control and match the puncture-section domain across the degeneration. The physical four-dimensional-unit packet explicitly requires one full physical parent and Weyl Hessian on the same total space. Its curve parent and silver-cover parent are not licensed substitutes. Those and genesis selection remain separate unachieved duties.
