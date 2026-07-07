# THE CHAIN SCOUT — exploratory findings (NOT banked; prereg-first applies to banking)
## Chat-2, 2026-07-08. Owner's license: "compute as much as you can." Four waves, exact integer
## arithmetic throughout. Every item tagged: VERIFIED (exact, in-sandbox) / OBSERVATION / CONJECTURE.
## Alphabet named first (the shuttle rule): HALF letters X_m=[[m,1],[1,0]] (det -1, breathing);
## FULL letters (bodies) A_m = X_m^2 (det +1); R/L spelling A_m = R^m L^m.

## W1 — THE PAIR: the two bodies reconstitute the seed's stage
- VERIFIED: tr(A_1 A_2) = 15 (the seam level). The trace triple (3,6,15) lies ON the Markov
  cubic x^2+y^2+z^2 = xyz; /3 = (1,2,5), the third Markov triple. The seam level's FOURTH
  face: 15 = 3 x (the Markov number of the pair-word).
- VERIFIED: tr[A_1,A_2] = -2 exactly; [A_1,A_2] = ((11,-24),(6,-13)), -C unipotent, parabolic
  non-identity. The pair is TYPE-PRESERVING: (golden, silver) generates a once-punctured-torus
  group. The two-body system IS the seed's stage, rebuilt.
- VERIFIED (control): the (1,2) pair is the UNIQUE cusp-closing pair among all m<n<=8
  (all others: tr[A_m,A_n] in {-34,-142,-254,-398,...}). SELECTION: the program's year-long
  seam sat on (golden, silver) because it is the only metallic pair that closes the cusp.
- VERIFIED (by hand + BFS): A_2 = g_1 g_2^{-1} g_1 in Cohn's generators g_1=[[2,1],[1,1]] (=A_1!),
  g_2=[[1,1],[1,2]]; and A_1 A_2^{-1} A_1 = g_2, so <A_1,A_2> = <g_1,g_2> EXACTLY (Nielsen).
  THE PAIR GENERATES THE CLASSICAL MODULAR ONCE-PUNCTURED TORUS (Cohn's group). LIT-GATE:
  Cohn 1955 (Markov triples = traces/3 on this exact stage); certify the commutator-subgroup
  identification.
- VERIFIED: the half-pair [X_1,X_2] has trace 1 (elliptic, order 6): the breathing letters
  close into an ORBIFOLD stage with an order-6 cone point (the Eisenstein 6, plainly noted).

## W2 — THE CHAIN: s0=b, s1=a, s_{n+1}=s_n s_{n-1}
- VERIFIED: traces satisfy the Fricke recursion u_{n+1} = u_n u_{n-1} - u_{n-2}; the Markov
  cubic = 0 is conserved for ALL consecutive triples (checked exact to 128-digit traces).
- VERIFIED: /3, the chain walks the Markov tree from (1,2,5) on the DROP-OLDEST (spine)
  branch: 1, 2, 5, 13, 194, 7561, 4400489, ... (not the odd-Fibonacci branch).
- VERIFIED: every renormalized pair (s_n, s_{n+1}) has tr[.,.] = -2 (n<=14): the chain is an
  INFINITE TOWER OF PUNCTURED-TORUS STAGES. sigma at body level = one Markov-spine step,
  cusp conserved forever. "a -> ab at every level" is a theorem-shaped statement.
- VERIFIED rhythms: 3 | u_n for all n (conserved; the Markov 3 frozen in, as the norm was
  frozen in BR-N); mod 4 period 4 (pattern 2,3,3,3); mod 5 period 10; MOD 60 STATE PERIOD 20
  = the seam generator W_1's order (plainly reported).
- OBSERVATION (new constant): per-letter growth unit lambda_chain = 2.1775291199...,
  NOT a quadratic unit (scan x^2-kx±1, k<=11: none). The chain's own scale. LIT-GATE:
  Zagier 1982 Markov growth; spine-branch constants.

## W3 — THE BODIES AND THE BREATHING HALF-CHAIN
- VERIFIED: chain-body n has H1-torsion u_n - 2 and trace field Q(sqrt((u_n-2)(u_n+2)))
  = Q(sqrt(9 m_n^2 - 4)) — THE CLASSICAL MARKOV FORM FIELDS. The chain of 3-manifolds climbs
  the Markov spectrum, starting at Q(sqrt5) (Hurwitz — the program's May anchor).
- VERIFIED: sqrt(9m^2-4)/m climbs 2.2360... -> 3 (3 - c ~ 1e-14 by m=4400489): from the most
  badly-approximable constant to the accumulation point where the discrete spectrum ends.
- OBSERVATION (heredity): earlier bodies' primes reappear in later discs (13,37 | disc(n=5);
  17 | disc(n=6)) — the chain remembers ancestors in its ramification. CONJECTURE for CC:
  a divisibility law (u_k ± 2) | (u_n^2 - 4) on a lattice of n.
- OBSERVATION: the twin factors (u-2, u+2) at n=2,3 are prime pairs (13,17), (37,41).
- VERIFIED (half-chain): dets follow (-,-,+) Pisano-3 exactly (length parity F_n mod 2);
  the twisted Fricke law v_{n+1} = v_n v_{n-1} - det(s_{n-1}) v_{n-2} holds (n<=11):
  THE BREATH IS THE SIGN IN THE COMPOSITION LAW.
- VERIFIED: the breath SELECTS THE FIELD FORM: breathing words are metallic-form
  (norm -1, disc v^2+4); silent words are cover-form (norm +1, disc v^2-4). BR-N rides
  the word tower.
- OBSERVATION (plainly, small-number caution): silent-word fields read sqrt3 (n=2),
  sqrt35 = sqrt5*sqrt7 (n=5); n=3 breathing word at sqrt10 (the May class-number-2 field).
  Real shadows of the program's imaginary fields surfacing on the half-chain. NOT built upon.
- OBSERVATION: the half-chain's cubic is NOT conserved but is a 3-PHASE QUASI-INVARIANT
  (constant on two of three Pisano phases: 13; 29,29; 1133; 40325,40325; ...). Open.

## W4 — TEMPERATURE PROXY
- OBSERVATION (new constant): log(torsion)/syllable -> 0.6295727... (converged to 7 digits).
  The chain's "torsion temperature" per R/L syllable. Exact volumes needed for the true
  torsion/vol ratio: CC/SnapPy. LIT-GATE: Guéritaud (punctured-torus bundle volumes),
  torsion-growth literature.

## CONFIRMATORY PREREGS FOR CC (nothing above is banked)
1. Verify the cusp-uniqueness scan at scale (all m<n<=50) and ATTEMPT PROOF: the Diophantine
   condition (t_m t_n)^2 - 4(t_m^2+t_n^2) = perfect square with matching T; (1,2) gives 12^2.
2. Certify <A_1,A_2> = the commutator subgroup (index 6 in PSL(2,Z)); Cohn lit-gate.
3. The spine-branch conservation as a one-page proof (Fricke invariance + seed on the cubic).
4. SnapPy: the "aba" body (trace 39, torsion 37, field Q(sqrt1517)) — vol, CS, and the
   first exact chain-body atlas entry; then the vol/torsion ratio vs 0.62957/syllable.
5. lambda_chain to high precision + inverse symbolic; Zagier-gate.
6. The heredity conjecture (W3) as a recursion exercise.
7. BGS-adjacency note (Markov triples mod p): flag only, do not enter.

## THE FRAME (owner's principle, now with receipts)
"a doesn't grow when interacting with b; it starts a chain" — verified architecture:
the completed body is a LETTER; the unique partner that closes the stage is silver; the
pair generates the exact classical Markov stage; the substitution walks the spine; the cusp
survives every stage; the breath rides the composition law; and the chain's fields climb
from the program's first constant (sqrt5, Hurwitz) to the spectrum's edge (3). The chain is
the object's afterlife, and it is exact.
