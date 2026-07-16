# P3 — THE PSL-FACTORING READING OF THE KILL RULE (statement + assembled evidence;
# cc2, 2026-07-16; no new compute — every citation banked)

**The statement (theorem candidate):** at E6 rungs k >= 3, the stage-typed kill rule's
kills (split primes p === 1 mod 3; deep 3-powers 3^a, a >= 3) are PSL-FACTORING
events: the theta-odd block's local constituent at the killed CRT factor of
ord(T_k) factors through PSL(2, p^a) — the central -I dies representation-
theoretically — while at surviving factors the constituent is SL-faithful. The
"halving iff even component order" clause is then pure group theory: the kill
changes the clock exactly when <A1 mod p^a> contains -I.

**Assembled evidence (all banked):**
1. E6 k = 2, MECHANIZED (Q2, loops-era): the local core at 7 IS the 3-dim irrep of
   PSL(2,7) — placement forced by the banked eigenvalue fingerprint {1, i, -i}
   (trace +1 on the PSL(2,7) order-4 class); the characters at 4 and 3 proven
   A1-blind by direct abelianization computation. The kill at 7 = PSL-factoring,
   at this rung a proven fact.
2. E6 k = 6 (the non-vacuous deep-3 kill): the banked R2 kernel element
   A1^18 === (I mod 4, -I mod 27) maps to the identity — the mod-27 central -I is
   killed exactly as PSL-factoring predicts; clock 18 = 36/2 (banked).
3. E6 k = 7 (the vacuous split kill): ord(A1 mod 19) = 9 odd, so <A1> misses the
   center — vacuity is a property of the cyclic subgroup, not the rep; consistent.
4. The stage invariance (N2/D4): SU(3) kills NOTHING (banked faithful at the
   would-be-kill rungs k = 4, 6, 11) — under this reading, the A2 stage's local
   constituents are SL-faithful where E6's factor through PSL: which quotient the
   local constituent selects is a STAGE datum carried by the modular data.

**The one priced step to theorem:** exhibit the PSL-factoring constituent explicitly
at one rung beyond k = 2 — decompose the k = 6 odd block (dim 61, exact matrices
banked in level6_blocks.npz) under SL(2,4) x SL(2,27): compute Tr rho(g) exactly for
a generating set of words g (the block's S, T matrices are exact), inner-product
against the SL(2, Z/27) character table (order 17,496; tables constructible), and
read off whether every 27-local constituent has -I in its kernel. Bounded exact
computation; priced at one focused cell. Until then this note is a STATEMENT with
one proven instance + two consistent instances, not a theorem.

**Why it matters:** it converts the kill rule from arithmetic bookkeeping into
representation theory — the stage "chooses" local quotients, and the clock law's
entire structure (N2 + Q2) becomes: clock = the order of A1's image through the
selected local quotients. One mechanism, every rung.
