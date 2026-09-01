# ADVERSARIAL VERIFICATION — T1_third_column

Verifier seat, 2026-09-01. Goal: refute the cell's BLOCKED verdict. Result: **could not refute.**

## VERDICT: CONFIRMED

## (1) Re-runs — all four scripts, byte-identical

All four scripts re-run from a clean scratchpad on this bench (python3, numpy, sympy), exit 0:

| script | re-run vs committed out | result |
|---|---|---|
| s1_reconstruct_sequence.py | diff vs s1_out.txt | IDENTICAL |
| s2_annihilation_theorem.py | diff vs s2_out.txt | IDENTICAL |
| s3_spread_replication.py | diff vs s3_out.txt | IDENTICAL |
| s4_missing_datum_probe.py | diff vs s4_out.txt | IDENTICAL |

Claimed numbers all reproduce: 0.000e+00 / 4.834e+00 (B1232 seed 20260901 re-run), 9.315 at
(0,0) and 15.76 max (generic bite, real 3x3x4 shape), 6.136 localized single-entry spread,
t1_verdict.json fields consistent with the outputs. Additionally I re-ran B1232's ORIGINAL
`frontier/B1232_.../verify_quotient_lemma.py` fresh: its output is byte-identical to its
committed `quotient_lemma_out.txt` (spread 4.834e+00), so the cell's "byte-level re-run"
claim (a reimplementation drawing the same RNG stream) is corroborated at both ends.

## (2) MB12 attack — the controls were run and they bite

- s3 case B (generic coupling) is a real failure mode: it exercises the same einsum path as
  case A; a broken instrument (e.g. conn entries dropped) would zero it and trip the assert.
  It gave 15.76 max — nonzero, order of B1232's 4.83. RUN and BITING.
- s3 case C shows localization (6.136 at (1,2), exactly 0.0 at (0,0)) — the OBSTRUCTED
  branch is distinguishable from the ANNIHILATES branch entry-by-entry. Failable.
- s2's exact-level bite: one conn entry set to zeta_12 gives deviation exactly zeta_12 != 0
  after reduction mod z^4-z^2+1. The criterion fails in both directions at the exact level.
- s1 convention controls all executed (asserts, not prose). I strengthened the attack: a
  full scan of ALL 12 possible twists shows k = -2 (mod 12) is the UNIQUE twist mapping
  B_raw = 3Reg+chi_1+chi_2 to R031A's committed 3Reg+chi_0+chi_11 — stronger than the
  cell's three named failing alternatives. Not refuted; reinforced.

## (3) Convention attack (E23 class) — survives restating

- Conventions are stated explicitly in s1's docstring (character normalization, raw vs
  physical, one application of chi_-2, Serre inverse phase, sub/quotient orientation,
  splitting parameterization matching B1232's verify_quotient_lemma.py).
- Independent alternative-identification attack: B_raw has TWO 4-dim isotypic blocks, raw
  chi_1 (conn 4 + tail 0) and raw chi_2 (conn 3 + tail 1). Only raw chi_2 = physical chi_0
  is compatible with R031A's committed transcript lines ("B_0 generator exponents (0,0,0,0)",
  "acts on B_0 by I_4 = zeta_12^0 I_4") — trivial action means physical chi_0. The raw-chi_1
  alternative (physical chi_11) has NO tail component, hence no (3,4,1). The identification
  is forced by committed data; the sequence survives the restating.
- M2's phase discipline ("carries chi_-3 ... must not be applied twice") matches the cell's
  stated convention (chi_-3 in Delta_G, chi_-2 applied once to B). Checked verbatim.

## (4) Gate 5 — clean

All four scripts read: inputs are character multiplicity vectors from committed memos, free
sympy symbols, zeta_12 arithmetic, seeded standard normals, and small exact rationals. No
measured SM value (mass, angle, coupling, ratio) appears in any script, output, or the JSON.
No held comparison was designed or needed — the observable tested is splitting-dependence.

## (5) Scope attack — citations audited against the committed sources

Every load-bearing citation was checked verbatim against the committed files:

- [M1] YUKAWA_CUP_PRODUCTS_308.md: conn multiplicities (2,4,3,3,2,3,2,3,2,3,3,3) (line 167);
  chi_-2 determinant linearisation and physical total 3Reg+chi_0+chi_11 (lines 169-173);
  raw coker (0,4,6,8,10) rank 16 and Serre-dual (0,2,4,6,8) (lines 401-405); H_u = C_0
  dim 1 Wilson table (line 75); "mu_u = 0, rank(mu_u) = 0" (line 19 — in fact COMMITTED in
  M1 itself, so the cell's "cited, not re-run" caveat on mu_u is over-cautious, not under).
- [M2] YUKAWA_DOWN_RESIDUE_SPEC_308.md: census 18+9+6+3=36, B_2 indices 6,7,8, selection
  rule rho+sigma=8 mod 12, skew (4,4) zero, "No numerical or exact 1x18 down-Yukawa row is
  present in the committed certificates" — all verbatim. The 27-count (Higgs/B_2 leg
  connecting: 18 conn/conn + 9 tail6/conn) recomputed independently: correct.
- [R031A] codex_certs_rerun.txt lines 1-10: input line, exponents (0,0,0,0), K-rank 4,
  P(B_0)=P^3 — all present as cited (an in-tree transcript, readable on this bench).
- B1232 FINDINGS: seed 20260901, banked 0.000/4.83, the fencing of "(3,4,1) sequence
  itself" as codex's still-running computation, and the "nine-entry tail/connecting block"
  phrase — all present. The cell's 27-vs-9 discrepancy flag is real and fairly typed (the
  9 = tail-family observable under the committed census; B1232's prose does read as if the
  annihilation condition were 9 entries).
- BLOCKED staleness attack: B1232 is the newest frontier arc (nothing after it but this
  campaign's own commits). I independently searched beyond s4's grep patterns:
  `evaluate_yukawa_down_connecting_308.py` and `YUKAWA_DOWN_CONNECTING_EVALUATOR_308.md`
  (both referenced by M1) are committed NOWHERE in the tree; no `1x18` value row, no
  GF(1009) connecting-row values, no .sage file. The missing-datum typing stands.
- The FINDINGS does not claim the couplings annihilate or obstruct; it claims exactly what
  s1-s4 show (sequence dims + criterion + validated instrument + typed missing datum) and
  fences the two cited-not-rerun facts. No overreach found. One nuance for the record:
  s1's "reconstruction" is character/dimension bookkeeping over M1's committed good-prime
  certificate multiplicities plus C12-equivariance of the sub/quotient maps — a derivation
  from the committed ledger, as stated, not a new cohomology computation; the FINDINGS'
  phrasing ("EXISTENCE AND DIMENSIONS ... derivable from the committed character ledger")
  matches this precisely.

## Residual weaknesses (none verdict-changing)

1. s4's probe-3 grep pattern is narrow; a value table under an unanticipated name could in
   principle hide. Mitigated by my independent searches (above) and by the specs' own
   committed proof-boundary statements. Risk: low.
2. s3 part 1 is a stream-equivalent reimplementation, not an execution of B1232's file; I
   closed this by running B1232's original file (byte-identical to its committed output).
3. The (3,4,1) conn/tail split of the chi_2 block inherits M1's good-prime provenance; M1
   itself declares the character convention closed against the char-0 index/Serre ledger.

## What was NOT re-run

The two facts the cell itself fences as cited: the runnable mu_u certs and R031A cert
scripts live on codex's absent macOS seat. Their in-tree transcripts (M1 line 19;
codex_certs_rerun.txt) were read directly and match the cell's citations.

Nothing in the cell directory was modified; this file is the only addition.
