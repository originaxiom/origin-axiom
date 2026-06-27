# B237 — L48 resolved (silver carries no 2O) + the binary-polyhedral quotient structure is manifold-specific

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; P1–P16 untouched; firewall intact.**
Run: `sage-python silver_2O.py` (SnapPy + GAP). A verify-don't-trust catch on chat1's L48 reasoning.

## The question (L48 / H33)
Silver (`m=2`) has trace field containing `ℚ(√2)` = the octahedral group `2O=E₇`'s character field (the field
golden *excludes*). Does π₁(silver bundle) actually carry a `2O` **quotient**, or is `ℚ(√2)` only a field
coincidence? Chat-1's partial answer: "almost certainly no — and **all** metallic bundles carry `2T` (mod 3) and
`2I` (mod 5)."

## The computation (GAP `GQuotients` — all surjections π₁ → G, definitive)

| bundle | 2T=E₆ (24,3) | 2I=E₈ (120,5) | 2O=E₇ (48,28) | S₄ (octahedral rotation, 24,12) |
|---|---|---|---|---|
| **golden** `m004` (m=1) | **2** | 0 | 0 | — |
| **silver** `b++RRLL` (m=2) | 0 | 0 | **0** | **2** |
| **bronze** `b++RRRLLL` (m=3) | **10** | **2** | 0 | — |

## Verdict
1. **L48 answered, definitively: silver does NOT carry `2O`** (`GQuotients=0`). The `ℚ(√2)` match is a **field-only
   coincidence**; the group never closes — consistent with `|2O|=48 ≠ p(p²−1)` (B234). *(Chat-1's conclusion was
   right.)*
2. **Chat-1's supporting claim is REFUTED (verify-don't-trust):** it is **not** "all metallic bundles carry `2T`
   and `2I`." The binary-polyhedral quotient structure is **manifold-specific** — golden → `2T` only; **silver →
   `S₄`** (the octahedral *rotation* group), carrying **none** of the binary `2T/2I/2O`; bronze → `2T`+`2I`. The
   "monodromy-matrix-mod-p" heuristic chat1 used (every integer matrix reduces into `SL(2,F_p)`) does **not** equal
   "π₁(bundle) surjects onto `SL(2,F_p)`."
3. **Clean new fact: `2O` is absent from golden, silver, *and* bronze** — the only binary-polyhedral group that
   never appears as a π₁-quotient (it is never `SL(2,F_p)`). Silver realizes the octahedral group only at the
   **rotation** level (`S₄`), never the **binary/spin** level (`2O`). A sharper "what golden excludes, silver
   includes" than chat1's: silver includes the octahedral *field* `ℚ(√2)` and the octahedral *rotation* group `S₄`,
   but **not** the binary octahedral group `2O`.
4. **Mechanism note:** `GQuotients` sees the **geometric-holonomy** quotients — golden's is `2T=E₆` (the hyperbolic
   field `ℚ(√−3)`, B210). Golden's `2I=E₈` is the **homological-monodromy** McKay (the `ℚ(√5)` field, B210), a
   *different* representation and **not** a π₁(bundle) quotient — hence `2I:0` for golden here. The two McKay
   structures (geometric vs homological) are genuinely distinct, as the table makes vivid.

## L47 cross-check (confirms B235)
`m009`/`m010` (vol 2.667) contain `√−7`, not `√−3` — they are the `d=−7` commensurability class, **distinct** from
the figure-eight (`m004`, `d=−3`). So `ℚ(√−7)` exists in 3-manifold land but never in the figure-eight's
(arithmetic) commensurability class — the trace-1 ladder closes at `{√5, √−3}` (B235). Source: Goodman–Heard–
Hodgson arXiv:0801.4815 Table 1.

## Anchors
B210/B212 (golden/silver congruence McKay), B234 (`2O` never `SL(2,F_p)`; the field-vs-group distinction), B235
(the trace-1 ladder closure). GAP `SmallGroup` ids: `2T=(24,3)=SL(2,3)`, `2I=(120,5)=SL(2,5)`, `2O=(48,28)=`
binary octahedral, `S₄=(24,12)`.
