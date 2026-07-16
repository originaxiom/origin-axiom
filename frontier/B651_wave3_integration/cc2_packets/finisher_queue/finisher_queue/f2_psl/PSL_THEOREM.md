# F2 — THE PSL-FACTORING THEOREM (central-element form) — upgrade of P3_NOTE.md
# (cc2, 2026-07-16; f2_run.log = the exact table, pure integer arithmetic)

**Theorem (E6 stage, k = 2..8, the <A1>-visible form).** Let n = ord(T_k), and for a
CRT factor q = p^a of n say the central -I_q is REALIZED if some A1^j === (-I mod q,
I mod every other factor). Then across all rungs k = 2..8 (19 factor-rows, 7
realized): the realized central is KILLED by the theta-odd block (its exponent j is
a multiple of the banked clock) EXACTLY at split primes (7, k=2) and deep 3-powers
(27, k=6), and SURVIVES exactly at shallow 3-powers (9 at k=3; 3 at k=5, 7, 8).
Zero exceptions. Non-realized centrals (all dyadic and inert factors here, and 19
at k=7) are vacuous, matching the rule's vacuity clause.

**Corollary (modulo the cited congruence property, Bantay / Ng–Schauenburg):** at the
killed rows the whole representation kills the central -I_q — every q-local
constituent of the theta-odd block factors through PSL(2, q). At the surviving rows
at least one constituent is SL-faithful. The stage-typed kill rule of N2/Q2 is
therefore REPRESENTATION THEORY: the clock = the order of A1's image through the
local quotients the stage selects (PSL at split/deep-3 for E6; SL everywhere for
A2, per D4's faithful rungs). One mechanism, every rung; the k=2 instance is fully
mechanized (Q2: the PSL(2,7) 3-dim with fingerprint {1, i, -i}).

**Evidence class:** the central-element table is EXACT (integer arithmetic; no
floats, no reps needed); the constituent-level reading depends only on CSP (cited,
known). The optional identification of WHICH PSL(2,27) irreps appear at k=6 stays
priced (character inner products; not needed for this statement).

**Proposed record placement:** with N2's law and Q2's mechanization, this closes
the clock arc's mechanism chain: L81(b) -> law (N2) -> anomaly dissolution (Q2) ->
local-quotient theorem (this note). Falsifier for future rungs: any realized
central violating the typing (e.g. a killed inert central, or a surviving split
one) at k >= 9 breaks the theorem — one integer computation per new rung.
