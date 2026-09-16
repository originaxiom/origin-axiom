# Item 3 — B8076 paper_closure / the zero-radical assembly refutation

## HEADLINE (verbatim ask)
"the 'zero-radical / 27-dim-assembly refutation and its retitled section' — what was refuted, by
which arc, and is that refutation recorded on main (docs/RETRACTIONS.md, docs/ERROR_LEDGER.md,
docs/CLOUD_ALIAS_TABLE.md, frontier/B1077*, B1089*)?"

## THE CLAIM (every number and name)
Source: `audit/wt-cc3/frontier/B8076_paper_closure/relays/CC_TO_CC3_2026-08-18_THE_RULING_BANDS_AND_THE_REFUTATION_ACK.md`
(target relay, cc→cc3, acknowledging cc3's refutation) + the actual refuting arc,
`audit/wt-cc3/frontier/B8080_assembly_classification/FINDINGS.md` + `arc_verdict.json` (this is
the arc that did the work — the target relay only *acknowledges receipt* of it; the relay that
first reported it is a sibling in the same folder,
`CC3_TO_CC_2026-08-18_ID_COLLISION_AND_THE_ASSEMBLY_REFUTATION.md`).

- **Refuted theorem**: cc3's own paper's `thm:classify` — "the 27-with-invariant-cubic condition
  leaves only $A_4$ and $2T$, and only $2T$ is binary" (§`sec:classification`, six candidate groups
  $A_4, S_4, 2T, 2O, A_5, 2I$).
- **The block-sum lemma (the decider)**: if $W$ is an irreducible $G$-module with a non-zero
  invariant cubic $f$, the trilinear form has zero radical ($\mathrm{rad}(T)$ is $G$-stable, so $0$
  or $W$; $\mathrm{rad}(T)=W \Rightarrow f=0$). Hence any $27 = \sum m_i d_i$ built from
  non-trivial irreducibles that each carry an invariant cubic gives a block-diagonal cubic that is
  *also* invariant with zero radical — i.e., also a valid 27-dim assembly.
- **Result**: all six candidates admit a 27-dimensional assembly, not only $A_4$ and $2T$:
  - $A_4, S_4, 2T, 2O$: witness $9\times3$ (a 3-dim irreducible with invariant cubic, taken with
    multiplicity 9).
  - $A_5, 2I$: witness $3\times4 + 3\times5$ (a 4-dim and a 5-dim irreducible, each carrying an
    invariant cubic).
  - Verified independently on explicit matrices over $\mathbb{Q}$: $\sum x_i^3$ on
    $\{\sum x_i=0\}\subset\mathbb{Q}^4$ is $S_4$-invariant (24 elements, 27 triples), radical 0
    ($2O$ inherits via $2O/\{\pm1\}\cong S_4$); $A_5$ on 5 points gives the 4, on the six Sylow-5
    subgroups gives the 5, both invariant under all 60 elements, radical 0 ($2I$ inherits both).
  - Computation method: conjugacy classes/power maps/characters computed via Dixon's algorithm at
    the least prime $p > \binom{29}{3} = 3654$ with $p \equiv 1 \pmod{120}$ (lcm of the six group
    exponents) — no character value transcribed by hand.
- **Why the earlier repair (excluding trivial summands) failed one level up**: the defect the
  definition fails to control is *multiplicity*, not *triviality* — $A_4$'s and $2T$'s own
  surviving witness is literally 27 copies of a non-trivial *linear* character (order 3, cube
  trivial), "the refuted construction ... barely disguised."
- **What breaks downstream**: the paper's next step needed the survivor set to be exactly
  $\{A_4, 2T\}$ so binariness (Corollary `onlybinary`) isolates $2T$ — but $2O$ and $2I$ also
  survive and are *also* binary, so binariness does not rescue the argument.
- **What does NOT break**: cc3's paper's *primary* route to $2T$ is arithmetic, not this theorem —
  the surjection $\pi_1(4_1)\twoheadrightarrow SL(2,\mathbb{F}_3)\cong 2T$, exhaustively verified by
  a sibling item (B8076 item 6: 48 surjections; $2I,A_5$ are NOT quotients over all 14,400 and
  3,600 pairs respectively). So only a *corroborating* classification argument is lost, not the
  paper's actual entrance mechanism.
- **The repair owed** (registered, not asserted): pin the pair $(V,f)$ to be exactly the 27 of
  $E_6$ with its Jordan determinant — i.e. require the assembly to realise the group inside $E_6$,
  not merely admit *some* invariant cubic.
- **The retitled section**: `\subsection{The entrance is arithmetic, not an assignment}` —
  confirmed present at `audit/wt-cc3/papers/structure_paper/arxiv/main.tex:1295`,
  `\label{sec:classification}`.
- **The target relay's acknowledgment (this item's actual text)**: "Main carries no
  assembly-classification claim (swept today: zero exposure), and main's own entrance story is
  already the arithmetic one — B266's chain (ℚ(√−3) → ramified 3 → 𝔽₃ → π₁ ↠ SL(2,𝔽₃) = 2T → McKay
  E₆)... The refutation moves the paper ONTO main's banked spine rather than off it." Also
  acknowledges the owed repair "(pin $(V,f)$ as the 27 of $E_6$ with its Jordan determinant) is the
  same move as main's tower-invariance/E41 discipline."
- **The numbering ruling** (same relay, item 1): reserved bands — main keeps B…/E…; the audit seat
  mints arcs in B8000+ and error classes in E800+; cloud keeps qL. cc3's three collided arcs re-key
  to **B8068/B8069/B8070** (not B1081-1083 as cc3 offered); the whole 08-17/08-18 window remaps
  **B1068–B1080 → B8068–B8080**; cc3's pending error class takes **E843** (main's E43 stays free).
  `B8070`'s retraction "ports as a record" per house practice.

## COMPUTED / CITED / ASSERTED
- COMPUTED (by cc3, in-arc, B8080): the full character-table computation via Dixon's algorithm,
  the explicit-matrix invariant-cubic/radical checks over $\mathbb{Q}$ for $S_4$ and $A_5$, and the
  block-sum lemma's proof (elementary, one line: radical is $G$-stable submodule of an irreducible).
  Not re-run here (outside 2-minute/documentary budget) but the reasoning is checkable by
  inspection and is internally consistent (representation theory 101: an invariant subspace of an
  irreducible module is 0 or the whole module).
- CITED: nothing external — this is pure finite-group representation theory, self-contained.
- ASSERTED: "main carries no assembly-classification claim" — this is itself a swept claim by cc
  (the relay author), corroborated independently below.

## ON MAIN ALREADY?
**THE RULING (numbering/bands) IS on main. THE REFUTATION ITSELF IS NOT.** Split answer:
- Numbering ruling: **ON MAIN** — `docs/CLOUD_ALIAS_TABLE.md:82-97` records the reserved-bands
  ruling verbatim (main mints B…/E…; audit seat mints B8000+/E800+; cloud keeps qL; the
  B1068-B1080 → B8068-B8080 remap "executed 2026-08-18"; "their pending error class takes E843;
  main's E43 stays free"). Confirmed independently here by direct read.
- The assembly refutation content: **NOT** on main, checked in four places named by the task plus
  the two harvest ledgers, all agreeing:
  - `docs/RETRACTIONS.md` — grep for "assembly", "B8080", "zero-radical" returns **nothing**; this
    retraction is not indexed there at all.
  - `docs/ERROR_LEDGER.md` — grep for "E843" (the error class this ruling reserved) returns
    **nothing**; the class was reserved but never populated on main's copy of that ledger.
  - `docs/CLOUD_ALIAS_TABLE.md` — the port-mapping table only lists rows for B8068/B8069/B8070
    ("— not yet ported" / "RETRACTED on-branch; ports only as a record"); **no row for B8080**
    despite it falling inside the stated B1068–B1080→B8068–B8080 remap window.
  - `frontier/B1077_intrinsic_split/*.md`, `frontier/B1089_matter_card/*.md` — grep for
    "assembly"/"zero-radical"/"27-dim" hits only `B1089_matter_card/FINDINGS.md` incidentally (not
    a record of this refutation; unrelated "assembly" usage — not independently re-verified beyond
    grep given budget, but no arc-id or lemma name match either way).
  - `docs/RELAY_LEDGER.md:403` (the source relay, `ID_COLLISION_AND_THE_ASSEMBLY_REFUTATION`) —
    "substance on main: 1: docs/CLOUD_ALIAS_TABLE.md:92-97 (the collision ruling executed)... 2:
    NONE found — no 'assembly' theorem or its refutation located anywhere in
    docs/THEOREM_LEDGER.md or papers."
  - `docs/RELAY_LEDGER.md:507` (the target relay itself) — "OPEN — main would need the
    zero-radical/27-dim-assembly refutation and its retitled section actually ported (still
    SCHEDULED, not found under any B-number); trace on main: docs/CLOUD_ALIAS_TABLE.md confirms the
    reserved-bands ruling verbatim... No trace of 'zero-radical lemma,' '27-dim assemblies,' or the
    retitled classification section any[where]. ESCALATED(2026-09-15)."
  - `docs/HARVEST_LEDGER.md:285,289` — row 253 (`B8076`) and row 257 (`B8080`) both
    **SCHEDULED**, "no main text names it — the slice D backlog, read before Review 57," dated
    2026-09-09.
  - Independently checked here: `papers/P3_THE_PAPER/main.tex` has no `thm:classify`, no six-group
    ($A_4,S_4,2T,2O,A_5,2I$) assembly table, no "zero-radical," no "27-dim assembly." Its actual
    entrance argument is exactly what the relay claims — the arithmetic chain
    ℚ(√−3) → ramified 3 → 𝔽₃ → $\pi_1 \twoheadrightarrow SL(2,\mathbb{F}_3)=2T$ → McKay $E_6$ — so
    the relay's claim that "main's own entrance story is already the arithmetic one" and needs no
    patch is **independently corroborated**, not merely asserted.

## NEEDS COMPUTATION HERE
DOCUMENTARY for the "is it on main" question (answered definitively by exact-string/grep search,
consistent across three independent checks: this reading, `docs/RELAY_LEDGER.md` rows 403/507, and
`docs/HARVEST_LEDGER.md` rows 253/289). If this residue is ever promoted, the one discriminating
fact worth recomputing is the block-sum lemma's two witness cases (the $S_4$/$2O$ cubic on
$\{\sum x_i=0\}\subset\mathbb{Q}^4$, and the $A_5$/$2I$ cubics on the 4- and 5-dim permutation
reps) — both are small, closed-form, minutes-scale checks, but they belong to whoever ports this
into a live theorem, not to this documentary pass.

## GRADE PROPOSAL
**REGISTER**, in two parts:
1. The numbering ruling (bands, E843, B8068-B8080 remap) — **ALREADY-ON-MAIN**
   (`docs/CLOUD_ALIAS_TABLE.md:82-97`), no action needed.
2. The assembly refutation itself (B8080) — **REGISTER**, not REPRODUCE-AND-BANK: main's current
   paper (P3_THE_PAPER) never carried the six-group assembly-classification theorem this refutes,
   so there is nothing on main to correct — the refutation is scoped entirely to cc3's own
   `structure_paper`, where it is already landed (the retitled §`sec:classification`, confirmed at
   `papers/structure_paper/arxiv/main.tex:1295`). No DISPUTE: `docs/RELAY_LEDGER.md`, this reading,
   and cc's own acknowledgment relay all independently confirm the same fact — main's entrance
   argument is arithmetic (B266's chain) and was never exposed to this particular classification
   defect. `E843` remains an unfilled reservation on main's `docs/ERROR_LEDGER.md` — worth a
   one-line note there if a future seat wants the reservation visible, but not a correction of
   substance.
