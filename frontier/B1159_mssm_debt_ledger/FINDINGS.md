# B1159 — The object→MSSM debt-map: codex's conditional MSSM witness, every condition typed and verified

**Status: banked (frontier). Verdict OPEN** — a **reference/verdict arc** (the verified condition ledger),
not a physics claim. Built by WF-3 (the masterplan's move to "pay codex's conditional debt"), which read
codex's off-branch MSSM witness *and* re-derived the load-bearing algebra in-sandbox. **The verdict on the
owner's question — can the chain run object-forced to MSSM? — is NO, and the reasons are themselves
theorems.** No firewall crossing; Gate 5 clean (no SM value asserted). Lock
`tests/test_b1159_mssm_debt_ledger.py`.

## Provenance — the harvest+verify workflow

WF-3 (6 agents: 2 scope → 3 verify → 1 assemble; 397k subagent tokens) read codex's off-branch
`closure_campaign` witness (the height-308 SU(5) bundle, the heterotic bridge, the character-rule selector,
the Yukawa no-go) **and** cross-checked every link against main's banked seams, re-running codex's
certificates and re-deriving the key algebra. The two cleanest new facts were **re-verified on this bench**
(`verification/reproduce.sh` → `REPRODUCES`). Codex's primary derivations are **single-homed** (off-branch);
the provenance-debt relay (below) asks codex to commit them.

## The verdict (the honest north star, sharpened)

**SEAM-A is a wall in substance — I had over-framed it as a door.** Link A (the heterotic framework) is
**un-forced at every place**: the finite places don't select it (OA-C1002 — *re-derived this run by
multiplet count*: the same CY3 with (h¹¹,h²¹)=(1,4) yields IIA (1,5), IIB (4,2), het (N=1) — three
inequivalent string realizations, so heterotic is a *choice*), and the ∞-place carries no object-specific
content to select it (B1157 + the three-seat convergence: the Ruelle/torsion content is generic; B1156's
archimedean "door" opens onto the Vol=Vol tautology). The **one unsealed computation** (B1156's
finite-phase→Vol map, Andersen–Hansen closed→cusped) is **NEEDS-SPECIALIST**, and on all evidence is
expected to seal as MISMATCH. So the strict status is a **FLOOR leaning hard to WALL**, and either way it
**does not pay link A**.

## The debt, itemized and verified (`verification/condition_ledger.txt`)

| link | what | type | object-forces-it? |
|---|---|---|---|
| **A** | heterotic/worldsheet framework | **CRUX (imported)** | **No** — OA-C1002 (three string theories on one CY3, re-derived). SEAM-A doesn't pay it. |
| **B** | which E₈ (standard embedding) | forced-given-A | **Yes, conditionally** — SU(3)-commutant is E₆(78) in E₈ vs SO(26)×U(1)(326) in Spin(32)/ℤ₂; 78≠326 → E₈×E₈ only (re-derived). But E₆ arrival is *generic* (B727); inherits A's non-payment. |
| **C** | bundle / branch / Wilson line | **half-paid** | **Split** — the character **alphabet** is object-forced with **zero spectrum input** (Pic_ℚ={0,2,3,4,6,8,9,10} from the toric fan, verified); the **branch selection** needs two imported target-motivated rules (P1/P2), and Galois V₄ acts freely → uniqueness refuted, 11-dim moduli unselected. |
| **D** | a nonzero up-Yukawa | **WALL** | **No — proved obstruction.** μ_u=⟨i(a)∪i(b),c̃⟩=0 because H¹(X,G_X)=0 (re-derived by hand + sage cert); = SEAM-Y MISMATCH (B1154). Cohomological emptiness, coefficient-independent. |
| **E** | moduli, SUSY breaking, EWSB, scales | **WITHHELD** | **No** — the dimensionful no-go (B660/B666) forbids typing any dimensionful observable. |

## The bifurcation (the sharp statement)

- **Structural chain → the exact charged MSSM *spectrum*:** A ⟹ B ⟹ C-spectrum. **Payable iff A is paid**,
  and A is provably *not* object-forced. So it is a **conditional cohomological spectrum theorem** whose
  single unpaid premise is A (modulo P1/P2 and unselected moduli).
- **Value chain → the Yukawas/masses:** hits the **WALL** (D = SEAM-Y, up-Yukawa=0) + **withheld** (E).

**"The object all the way to MSSM" = a conditionally-forced *spectrum* sitting on top of a proved *wall*
where the masses are.** Structure forced (on A), values withheld — the program's one verdict, instantiated
at the Standard Model's doorstep. It is **not object-forced end-to-end, and not a breakthrough.**

## The one genuinely live door (relocated, not closed)

Since link A is walled, the heterotic *route* can't be made object-forced. The live alternative is to
**bypass A**: the ledger shows link C's character **alphabet is already object-forced with no spectrum leak**
— the foothold for deriving the MSSM spectrum from **E₆ + the character rule as pure algebra**, with
heterotic demoted to one physical dressing. What blocks the bypass today is C's **branch selection** (the
imported P1/P2 rules + the free Galois action). So the sharpest open question the program can actually work
is: *can P1/P2 be replaced by an object-intrinsic principle, closing C's branch selection without link A?*
— not "storm SEAM-A."

## Provenance debt (relay to codex, R49-1)

The load-bearing witness is single-homed; the branch carries only summaries. Codex should commit: **(D1)**
the height-308 bundle certificate (the 44-integer KZ coordinate vector, the Euler-kernel / augmented-H⁰
kernel / rank-C372→C312 / three-chart-ideal=[1] / char-zero local-freeness cert) and its runner; **(D2)**
the character-rule / C12 bundle-selector derivation (the branch has only the summary); **(D3)** the Yukawa
no-go chain-level evaluator. Relayed via `CC_TO_CC3`… (to codex).

## Fences

No firewall crossing — the witness is a **conditional cohomological spectrum theorem, not a vacuum**; Gate 5
clean (no mass/scale VALUE derived; the spectrum is reps+charges = structure). The multiplet count and E₈
branching are own-verified; C's alphabet Pic_ℚ + D's μ_u=0 were re-run/re-derived by WF-3 (the height-308
cohomology + Strominger persistence are sage-certified **off-branch, single-homed** — provenance debt,
flagged, not leaned on). SEAM-A's status is B1156's FLOOR (leaning wall); OA-C1002/SEAM-Y are main-verified.

## Routes

- **Move 2 reframed:** attack link A becomes **seal SEAM-A as a wall** (run B1156's finite-phase→Vol
  computation to convert leaning-MISMATCH → proved MISMATCH) — but it is NEEDS-SPECIALIST, so the honest
  bench step is a scoping/relay, not an in-sandbox close.
- **The live cell:** replace C's P1/P2 with an object-intrinsic selection principle (the bypass door).
- **Relay:** the provenance debt D1/D2/D3 → codex.
