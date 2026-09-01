# R09 — THE SCALE CLUSTER: recomputation findings

Cell: `reports/fresh_physics_seat_2026-09-01/recompute/R09_scale_cluster/`
Date: 2026-09-01. Discipline: blind-first (own code run and outputs on
disk before any banked verification script was opened).

## Verdict: MATCH on all three claims, with a VACUITY-ADJACENT note on (a)

## Blind protocol — files read BEFORE computing
- Directory listings only, plus exactly two grep lines out of
  `frontier/B666_leads_campaign/cellS/PROOF_NOTE.md` (lines 23 and 98)
  to learn the claim's definition of L: Gal(L/Q(i)) = Klein four.
  (Line 98 unavoidably exposed the banked order-4/ab-4 row for that one
  group; nothing else of the banked table was seen before my run.)
- The full claim statement (groups, volume digits, formulas) came from
  the recompute brief itself.

## Files read AFTER my numbers were on disk (`blind_output.json`, `blind_run.log`)
- `frontier/B666_leads_campaign/cellS/PROOF_NOTE.md` (full),
  `verify_rigidity.py` (header/structure)
- `frontier/B1088_action_card/FINDINGS.md`, `b1088_action_card.py`
- `frontier/B250_volume_profile/FINDINGS.md`, `volume_profile.py`
- `frontier/B1034_l154_sigma/FINDINGS.md` (Sugawara bank)
- `frontier/B652_gate_b/GRAMMAR_TABLE.md`, `GATE_B_VERDICT.md` (premise status)

## (a) Scale-torsor theorem, B666 cell S: Hom(G, R+) = 0 — MATCH, VACUITY-ADJACENT

My from-scratch computation (`r09_recompute.py`, brute-force closure /
commutator subgroups; W(E6) as permutations of a from-scratch E6 root
system):

| G | my order | my |G^ab| | banked order | banked G^ab |
|---|---|---|---|---|
| Gal(L/Q(i)) = (Z/2)^2 | 4 | 4 | 4 | (Z/2)^2, order 4 |
| 2I = SL(2,5) | 120 | 1 (perfect) | 120 | trivial |
| PSL(2,7) | 168 | 1 (perfect) | 168 | trivial |
| 2I x Z/3 | 360 | 3 | 360 | Z/3 |
| SL(2,Z/15) | 2880 | 3 (via verified CRT SL(2,3)xSL(2,5); [G,G] = 8*120 = 960) | 2880 | Z/3, [G,G] order 960 |
| W(E6) | 51840 | 2 (det surjects; all 6 simple reflections conjugate, braid identity machine-checked on all edges) | 51840 | Z/2, [W,W] = 25920 |

Every row matches. Hom(G,R+) = 0 follows for each.

**Plain statement on depth: this is a near-tautology, not a deep
theorem.** The whole content is the one-liner: R+ is torsion-free, so
any homomorphism from a finite (or, continuously, profinite) group is
trivial — phi(g)^ord(g) = 1 forces phi(g) = 1. The six per-group
"instantiations" verify group orders and abelianizations, none of which
is needed for the conclusion (finiteness alone suffices). So:
**VACUITY-ADJACENT: true and banked correctly, but the word "theorem"
carries less weight than it suggests.** To the note's credit,
`PROOF_NOTE.md` par.4 says this itself ("two-line rigidity theorem") and
explicitly names the actual load-bearing premise: **that every framework
output is an algebraic number stabilized by a finite/profinite group,
with no continuous R+-parameter ("no dial") anywhere in the output
algebra** — consumed from B660/S3 rows 2-3 and B652, "the one assembly
ingredient this note consumes rather than reproves." B652's "no scale"
is a grammar/typing rule about the framework's own sealed grammar
(GRAMMAR_TABLE.md: "No scale (dimensionless only — R5 makes this
structural)"), i.e. an audited bookkeeping claim about the
construction, not an independently provable mathematical fact. The
scale no-go is exactly as strong as that premise.

**Controls run** (`r09_control.py`, exclusion claim => plant the
excluded thing): (1) the same machinery finds the explicit nontrivial
character SL(2,3) -> mu_3 in C* (exact sympy roots of unity, all 576
pairs multiplicative, nontrivial on 16/24 elements) — so the vanishing
into R+ is carried by the target's torsion-freeness, not by an
instrument that always answers 0; (2) Hom(Z, R+) is nontrivial
(phi(n) = 2^n, exact Fractions) — finiteness is load-bearing; (3)
x^3 = 1 has 3 roots in C but only x = 1 in R+ (exact solve). ALL PASS.

## (b) Vol(m004) and CS(m004) — MATCH (50 dps, two independent ways)

- Way 1 (Lobachevsky): Vol = 4*Lambda(pi/6), Lambda via Im Li2(e^{2i theta})/2,
  cross-checked against the defining series at 1e-9:
  **2.0298832128193072500424051085490405718833786150606**
- Way 2 (Dedekind zeta, K = Q(sqrt-3)): 9*sqrt(3)*zeta_K(2)/pi^2 with
  zeta_K(2) = zeta(2)*L(2,chi_-3), L via Hurwitz zeta
  3^{-2}(zeta(2,1/3) - zeta(2,2/3)), series cross-check:
  **2.0298832128193072500424051085490405718833786150606**
- |way1 - way2| = 6.2e-61 at 60 dps. Banked (B1088/B250):
  2.029883212819307250042405108549... — my value reproduces all 30
  banked digits (residual 4.06e-32 is pure truncation of the banked string).
- SnapPy high-precision agrees to all printed digits:
  2.029883212819307250042405108549040571883378615060599584034978214.
- Convention note: banked formula 6*Lambda(pi/3) (B250) equals my
  4*Lambda(pi/6) via Lambda(pi/6) = (3/2)Lambda(pi/3) — same number, not
  a discrepancy. The zeta_K route is genuinely independent of both
  banked scripts (neither B250 nor B1088 used it).
- CS(m004): snappy high-precision chern_simons() = -1.15e-65, i.e.
  **0** to 65 digits (convention: SnapPy CS, defined mod 1/2,
  complex-volume normalization). Matches the banked CS = 0 (theorem via
  amphichirality). Note m004 is amphichiral so CS = 0 is forced exactly;
  the numerical check is confirmation, not the proof.

## (c) c = 6*sigma both ways — MATCH

- Brown-Henneaux: c = 3l/(2G) with G = l/(4*sigma) gives sympy-exact
  **c = 6*sigma** (l cancels; banked B1088 sets l = 1, same result).
  This clause is pure algebra — it verifies the banked ALGEBRA, and its
  physical content is entirely in the identification G_N = 1/(4*sigma)
  (B1012), which this cell does not adjudicate.
- Sugawara: E6 root system built from scratch from the Cartan matrix
  (closure of simple roots under simple reflections): 72 roots, dim =
  72 + 6 = **78**, highest-root marks (1,2,2,3,2,1), dual Coxeter
  h_dual = 1 + 11 = **12** (simply laced; cross-check h = 72/6 = 12).
  c((E6)_1) = 78*1/(1+12) = **78/13 = 6** exactly (Fraction).
  Matches banked B1034 ("c((E6)_1) = 78/13 = 6 exactly (Sugawara,
  h_dual = 12)").

## Gate 5
No measured Standard Model value enters anything above: group theory,
Lobachevsky/zeta special values, and Lie-algebra integers only.

## Artifacts (this cell only)
- `r09_recompute.py` — blind recomputation (a)(b)(c)
- `blind_run.log`, `blind_output.json` — its outputs (written before any
  banked verification script was opened)
- `r09_control.py`, `control_run.log` — planted-hom controls, ALL PASS
