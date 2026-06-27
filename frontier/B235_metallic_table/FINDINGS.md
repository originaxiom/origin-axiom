# B235 — the metallic family table (L49) + the ℚ(√−7) probe closed (L47) + the F₄ retraction (H24)

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; P1–P16 untouched; firewall intact.**
The three chat-1 follow-ups. Run: `python metallic_table.py` (pyenv); `sage-python l47_snappy_probe.py` (SnapPy).

## (1) L49 — the metallic family table (the paper's §4 backbone)

| m | n=m²+4 | minimal model | c | SUSY | trace field | McKay match (field vs group) | Seifert dual | \|H₁\| |
|---|---|---|---|---|---|---|---|---|
| 1 | 5 | M(4,5) | 7/10 | **yes** | ℚ(√5) | **2I=E₈ (group+field)** | S²(5,4,3) | 83 |
| 2 | 8 | M(7,8) | 25/28 | no | ℚ(√2) | 2O=E₇ (**field only** — golden excludes) | S²(8,7,3) | 227 |
| 3 | 13 | M(12,13) | 25/26 | no | ℚ(√13) | none | S²(13,12,3) | 627 |
| 4 | 20 | M(19,20) | 187/190 | no | ℚ(√5) | 2I=E₈ (**field only**, n≠5) | S²(20,19,3) | 1523 |
| 5 | 29 | M(28,29) | 403/406 | no | ℚ(√29) | none | S²(29,28,3) | 3251 |
| 6 | 40 | M(39,40) | 259/260 | no | ℚ(√10) | none | S²(40,39,3) | 6243 |

Collects B204/B218/B224/B227/B228/B231/B234. The **field-vs-group** column carries the B234 distinction:
`m=1` is the only row where the E₈ *group* `2I=SL(2,F₅)` closes (n=5 prime) **and** SUSY fires; `m=4` carries the
E₈ *field* `ℚ(√5)` but no group and no SUSY; `m=2` carries E₇'s *field* `ℚ(√2)` but never the group `2O`. `|H₁| =
(2m²+7)²+2` (B227; m=1 → 83 cross-checks B229).

## (2) L47 — the ℚ(√−7) probe: **CLOSED** (the trace-1 ladder is *closed*, not generative)

Two independent verifications, both saying ℚ(√−7) does **not** appear:
- **SnapPy** (`l47_snappy_probe.py`): the figure-eight's invariant trace field is `ℚ(√−3)`, and **every cover up
  to degree 6 has invariant trace field `ℚ(√−3)`** — no `√−7`. Reason: `4₁` is **arithmetic** (Bianchi group
  `PSL(2,O₃)`), so all covers lie in one commensurability class and the invariant trace field does not enlarge.
- **Algebraic (the reason):** the trace-1 ladder `disc = 1−4·det` is realized only at the two **unit**
  determinants — `det=+1` (holonomy, `SL(2,ℂ)`, `disc −3 → ℚ(√−3)`) and `det=−1` (homological monodromy,
  `GL(2,ℤ)`, `disc +5 → ℚ(√5)`). The `ℚ(√−7)` rung needs `det=2` (`x²−x+2`), a **non-unimodular** element, which
  neither the holonomy (det 1) nor the homology (det ±1) provides.

**Verdict:** the trace-1 ladder **closes at `{√5, √−3}`** — explained by **unimodularity** (`det∈{±1}`) **+
arithmeticity** (`4₁` Bianchi). It is *not* generative. This resolves chat2's "if the object stops at `{√5,√−3}`,
that closure is itself a fact" — the closure is now a *fact with a reason*. (The trace-1 congruence law H27/B234
stands; its "next rung" is simply unreachable for this object.)

## (3) H24 corrected — the exceptional footprint is **3/5**, not 4/5 (F₄ retracted)

Chat-1's own re-audit retracts the F₄ link, and an **independent c-matching check confirms it**: a conformal
embedding `SU(3)_k ⊂ (F₄)₁` requires `c(SU(3)_k)=8k/(k+3)` to equal `c((F₄)₁)=26/5`, which has **no integer
solution** (`k=39/7`). So **no `SU(3)_k` conformally embeds in `(F₄)₁`** — the `SU(2)₃→SU(3)₂→(F₄)₁` route (chat1
D3) is **void**. (Chat-1's stated reason — Dynkin index 6 ⟹ `SU(3)₆` — also fails: `c(SU(3)₆)=16/3≠26/5`; the
clean statement is "no integer level works at all.")

**Exceptional-group footprint = 3/5:** **G₂** (Fibonacci `=(G₂)₁`), **E₆** (hyperbolic field `ℚ(√−3)`, `2T`),
**E₈** (monodromy field `ℚ(√5)`, `2I`); **E₇ excluded** (triply, B234); **F₄ retracted**. *(The genuine F₄ fact is
the **generic** conformal embedding `(G₂)₁×(F₄)₁ ⊂ (E₈)₁` (`c=14/5+26/5=8`) — i.e. `(F₄)₁` is the commutant of the
Fibonacci `(G₂)₁` in `(E₈)₁`. But that holds for the abstract categories, not via the object's arithmetic — by the
specificity filter (H28) it is a **universal** rhyme, not an object-specific footprint entry.)*

## Anchors
B204/B218/B224/B227/B228/B231 (the table's cells), B234 (field-vs-group, the trace-1 congruence law, the
specificity filter), B210 (dual McKay). Leads closed/refined: L47 (closed), L49 (assembled); H24 corrected.
Literature: arithmeticity of `4₁` / Bianchi `PSL(2,O₃)` (standard); conformal-embedding central charges (standard).
