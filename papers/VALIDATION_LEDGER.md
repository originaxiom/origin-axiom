# Validation Ledger

Status: public-safe validation ledger. This file records actionable findings
and the repository decision taken for each. It adds no claims.

Do not record private correspondence, private identity details, raw chats, or
private staging context. Summarize only the technical finding and the repository
action.

## Allowed Status Values

```text
OPEN = logged but not triaged
TRIAGED = decision assigned
PATCHED = accepted finding implemented
CLOSED = no further action
```

## Allowed Decisions

```text
ACCEPT_FIX
ACCEPT_CLARIFY
NEEDS_REPRO
DISPUTE_WITH_REASON
OUT_OF_SCOPE
KILL_OR_RESCOPE
```

## Ledger

| ID | Date | Packet | Competence area | Outcome label | Summary | Actionable findings | Affected files | Decision | Status | Linked commit/PR |
|---|---|---|---|---|---|---|---|---|---|---|
| _pending_ | _YYYY-MM-DD_ | _PC02/PC11_ | _field only_ | _label_ | _one-sentence summary_ | _short list_ | _paths_ | _decision_ | _status_ | _commit/PR_ |
| V1 | 2026-06-01 | PC12 | character varieties / substitution dynamics | STANDARD_REPACKAGE | Internal literature screen: most PC12 blocks are standard methods (Lawton; Baake-Grimm-Roberts; Bellon-Viallet); only the fixed-line splitting (Thm 4) is apparently-new and elementary. | rescale PC12 to a computational note; credit standard methods; present Thm 4 as the lone new bit; quarantine the self-evidencing/FEP framing in paths/E21 | LITERATURE_POSITIONING.md, PAPER_CARD.md, DRAFT_NOTE_SKELETON.md, frontier/B54, paths/E21 | KILL_OR_RESCOPE | PATCHED | branch frontier/pc12-literature-and-hardening (uncommitted) |
| V2 | 2026-06-01 | PC12 | algebraic dynamics | ACCEPT_CLARIFY | B54 verifies [J(m,c),P]=0 for symbolic c (exchange block-diagonalization on the whole fixed line, generalizing B51); the self-evidencing lambda=m condition reduces to the identity 4c^2-2=m^2+2 and predicts no observable. | integrate B54 as standalone math; record self-evidencing as STALLED in paths/E21, not in PC12 | frontier/B54, tests/test_general_c_exchange_structure.py, paths/E21 | ACCEPT_CLARIFY | PATCHED | merged in PR #8 |
| V3 | 2026-06-02 | PC12 | algebraic dynamics | VERIFIED | B55 classifies the c=1 fixed-line sectors for general m: symmetric is mod-4 (Phi6 for m=1,3; Phi4 for m=2; degenerate (t-1)^2 for m=0); antisymmetric is (t-1)(t+1)(t^2-mt-1)=char(M) for all m. Corrects the earlier odd/even reading. | integrate as PC12 c=1 content | frontier/B55, tests/test_c1_fixed_line_structure.py, DRAFT_NOTE_SKELETON.md | ACCEPT_CLARIFY | PATCHED | branch frontier/c1-structure-and-splitting (uncommitted) |
| V4 | 2026-06-02 | PC12 | low-dimensional topology | DEAD | B56: figure-eight diagonal SL(2,C) reps have Fricke-Vogt I in {4, -17/2 +/- 7 sqrt5/2}, none = 1/4; the figure-eight/I=1/4 bridge is dead and the c=1 Eisenstein resemblance is a cyclotomic coincidence. | record as a negative control; keep the separate P12 gluing-equation echo; framing stays in paths/E21 | frontier/B56, tests/test_figure_eight_invariant_surface.py, paths/E21, docs/atlas/FAILURE_ATLAS.md | KILL_OR_RESCOPE | PATCHED | branch frontier/c1-structure-and-splitting (uncommitted) |
| V5 | 2026-06-02 | PC12 | number theory / algebraic dynamics | APPARENTLY_NEW | B57 classifies integer splitting of the antisymmetric quartic for m=1..6: {c=1,c=3} universal plus m-dependent extras; the Hilbert-class-field coincidence (h(-15)=2) is killed for m>=2. | extend PC12 Theorem-4 content; record the class-field kill | frontier/B57, tests/test_general_m_splitting.py, DRAFT_NOTE_SKELETON.md | ACCEPT_CLARIFY | PATCHED | merged in PR #10 |
| V6 | 2026-06-02 | E21 / PC12 | hyperbolic geometry / algebraic dynamics | VERIFIED (elementary) | Fisher info of D(I) = 16/disc(char(M^2)) = 16*g_WP(m^2+2) = (4/Delta_eig)^2 (Goldman/Weil-Petersson coefficient); exact but a chain-rule identity on arccosh(2I+1) plus disc=a^2-4=1/g_WP. | record in E21 as a quarantine control; do not promote the geometric reading | paths/E21_self_evidencing_closure/ | ACCEPT_CLARIFY | PATCHED | branch paths/e21-wp-aubry-controls (uncommitted) |
| V7 | 2026-06-02 | E21 | localization / spectral theory | DEAD | Aubry self-duality at lambda=m is vacuous (lambda=m is the trivial fixed point of lambda->m^2/lambda); off-diagonal model has no genuine self-duality at lambda=m for m>=2 (IPR test). No metal-insulator observable. | record as a negative control in E21 + FAILURE_ATLAS; removes a physical reading of lambda=m | paths/E21_self_evidencing_closure/, docs/atlas/FAILURE_ATLAS.md | KILL_OR_RESCOPE | PATCHED | merged in PR #11 |
| V8 | 2026-06-02 | PC12 | SL(n) character varieties / algebraic dynamics | NEEDS-EXPERTISE | B58 attempted the n=4 tower prediction: confirmed the SL(4) identity recursion (r-1)^4 + cubic derivative sequences, and that the fixed-line point is the degenerate identity representation (so representation-based numerics cannot recover the ambient Jacobian). The full 15-coordinate ambient SL(4,C) trace map (Procesi + substitution action) is required and not built. | keep the SL(4) prediction untested in PC12; building the ambient SL(4) trace map is the next probe | frontier/B58_sl4_tower_test/, tests/test_sl4_tower_test.py, DRAFT_NOTE_SKELETON.md | NEEDS_REPRO | PATCHED | branch frontier/b58-sl4-tower-test (uncommitted) |

## Triage Notes

Use one row per coherent technical finding. If one source produces unrelated
findings on PC02 and PC11, split them into separate rows.

Before changing any claim status:

```text
1. reproduce or verify the finding
2. patch docs/tests/proofs on a branch
3. rerun the relevant checks
4. update the affected paper card
5. add the linked commit or PR to this ledger
```
