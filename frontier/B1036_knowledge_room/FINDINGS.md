# B1036 — the knowledge room: the firewall runs backwards in five places, and nobody could see it

**Date:** 2026-08-11 · **Lane:** the governed-rooms sweep. Gate 5 untouched; zero anchors; nothing
to `CLAIMS.md`; **no mathematics disturbed.**
**Files:** `verify.py` → `results.json` (28 checks) · lock `tests/test_b1036_knowledge_room.py`.

**The room:** `knowledge/`, the "textbook layer" a new seat reads first — **26 explainers**, and
`knowledge/INDEX.md` is one of the **nine surfaces** `representation_sweep.py` reads when it asks
*"is this arc represented anywhere?"*

---

## 1. THE POSITIVE RESULT FIRST — the contradiction hunt came back clean

`knowledge/GOVERNANCE.md`'s rule is that nothing here is ever a claim. The obvious risk in a room
that summarises the corpus is that it summarises something since retracted. **It does not.**

- **0 of the 8 registered phrases in `docs/RETRACTED_PHRASES.md` appear anywhere in the room.**
- **Every applicable row in `docs/RETRACTIONS.md` is already carried in-line in the entry it
  touches** — K009 states *"this **corrects B123/K009**"* and explains the knot-vs-bundle scope
  error; K015 marks its chirality headline *"a sampling artifact, withdrawn"*; K017 says *"The
  arithmeticity arm is **REFUTED as stated**"*.

> **The room's mathematical hygiene is good, and K009 is a model of the discipline working.** That
> is worth banking as loudly as any defect, because it is the outcome the sweep was built to
> falsify.

## 2. THE PRIMARY FINDING — the room's own rule is prose-only, and it is being broken

`knowledge/GOVERNANCE.md`: *"Nothing here promotes to `../CLAIMS.md` … it introduces no new result
and is **never a premise of a proof**."*

**Nothing enforces that.** The `firewall-oneway` gate tests exactly three strings —
`gates.py:119`: `if "speculations/" in row or "philosophy/" in row or "story/" in row:` —
and **`knowledge/` is not among them**. Two breaches, both verified line by line:

**BREACH 1 — an explainer carries a THEOREM grade on the law register.** `docs/LAW_MAP.md:149`:

| row | status | witnesses |
|---|---|---|
| **Form forced, value Galois-chosen (K020)** | **THEOREM** (K020) + growing witnesses | **K020**; B642; L74/L67 |

K020 **names** the row, **authorises the grade**, and is listed **ahead of the arc**. The theorem is
B285/B314's; K020 narrates it.

**BREACH 2 — a *sealed* preregistration cites an explainer as its authority.**
`docs/SEAL_LEDGER.md:461`, inside B812's prereg, defining its axes as *"the programme's OWN proved
walls"*: *"S (needs the object to supply a SCALE → **excluded by K018**, three independent modes)"*.
**A sealed document cannot be amended.** The real authority is B164/B167/B168/B169.

Three lesser instances sit behind them: `LAW_MAP:99` (a law *named* after a K-entry),
`HINT_LEDGER` H50 (K006 and K018 as numbered premises of an adjudication that produced a banked
verdict), and `STRATEGIC_SYNTHESIS:47` (*"verified against `K006`"*).

**The pattern is exact and worth stating:** every breach cites **K006, K018 or K020** — the three
entries that *consolidate a whole arc cluster*. Those are the convenient ones to cite, and
precisely the ones that must not be. **The entries anchored to a single named result (K005, K009,
K011, K015, K017) are never misused.** *Consolidation is what makes an explainer citable as a
premise; that is the mechanism, not the sloppiness.*

## 3. K021 OVERSTATES THE GENERATION GRADE — against its own §8

`K021` §0: *"The object **forces** all the dimensionless **structure** (the gauge group E₆, the 27,
**three generations**, a democratic Yukawa)."*

**Its own §8 lists `C — multiplicity → generations` as an open gate.** And every current surface
grades it weaker: `THE_CLAIM` §1 says **STRUCTURAL** (*"a named debt inside a closed proof"*),
`SM_SPECIFICATION_LEDGER` says *"structural, count matches"* with the bijection **unverified**, and
B1031/X33 say B302 **locates** the ℤ/3 — *locating, not deriving* — with two caveats that must
travel with any statement of it (the registerability circularity, and the typing wall).

**Not a contradiction with B307's theorem** — K021 §3 and K020 §8 both correctly place the
generation ℤ/3 in the commensurator, which is where B307's own conclusion puts it. **It is a grade
overstatement in the entry a new seat reads for the founding identity**, and it contradicts itself
four sections later. **Softened in place with the citation**, not rewritten.

## 4. A FIFTH E1 — a factor of two, in the two documents no gate can see

The room holds two documents that are **not `K`-numbered**, and the gate's `on_disk` set is built
from `K\d{3}_*.md`, so **they are invisible to it by construction**:

| document | quotes |
|---|---|
| `THE_UNIQUENESS_ATLAS.md` G5 | *"topological entropy **log φ² = 2 log φ**"* — **[banked]** |
| `THE_GOLDEN_CAT_MAP_PRINCIPLE.md` | *"the cat map ITSELF: Lyapunov **4 log φ** = its metric entropy"* |

Recomputed here: `A = [[2,1],[1,1]]` has eigenvalue **φ²**, so `h_top(A) = log φ² = 2 log φ =
0.9624…`, and **`4 log φ` is exactly twice that.**

**The diagnosis is a convention gap, not an error.** Pesin's `h = Σ λ⁺` (positive exponents only)
gives **2 log φ**; summing `|λ|` over both the expanding and contracting directions gives
**4 log φ**. **Both are defensible; neither document declares which it uses**, and both sit in the
room a new seat reads first. **Exactly the shape of `B62 = 2 × P33`** (B1026) — and the fifth
undeclared-convention collision this refresh has found.

Two further undeclared symbols, minor and recorded: **`θ`** is used bare in K020 (for the
trinification ℤ/3 axis) and K026 (for the E₆ diagram fold) while **K005 is the entry *titled* about
θ and fixes it as `−w₀`**; and **`level`** carries three senses in K020 alone (the CS/anyon level
`k`, the congruence level, and §8's own L1–L4 stratification).

## 5. WHAT WAS REPAIRED (drafting, each citing this arc)

**Three documents stated the room's size. All three were wrong**, and the gate that guards the room
was **green throughout** — because `knowledge-index` validates **rows**, and these are **prose**:

| | said | actual |
|---|---|---|
| `knowledge/INDEX.md` | *"index of explainers `K001–K020`… All written (K001–K020)"* | **26** |
| `knowledge/GOVERNANCE.md` | *"`K001…K009`"* **and** *"WRITTEN (K001–K010). All ten explainers exist"* — **two ranges in one file**, frozen at the B124 refresh | **26** |
| `ARCHITECTURE.md:38` | *"`K001–K022`, all written"* | **26** |

Also repaired: **the index rendered as one table (K001–K016), then nine orphan `| … |` lines
(K017–K025) that markdown shows as literal text, then K026 as a bullet with no link** — now one
contiguous 26-row table; the two ungated documents are at least **listed**; and the header now
carries the split that governs currency — **`K001`–`K007` are standard background and do not decay;
`K008`+ consolidate the project's own results and age like `LAW_MAP` does.**

**And the pointer in the proven register.** `CLAIMS.md` sent readers to *"`knowledge/K020` (**the
current headline**)"*. **K020's newest anchor is B325** — 710 arcs back. Re-labelled to *"the
structural theorem as a Galois theorem, **consolidated at B325**"*, pointing current readers at
`THE_CLAIM` and `LAW_MAP`. **Not a firewall breach** — `CLAIMS` points *outward* to what it
deliberately does not claim — **a currency defect**, and nothing checked it because *"current"* is
prose.

## 6. WHAT DECAYS, MEASURED — and what does not

**7 STANDARD** (K001–K007: Fricke/character variety, metallic continued fractions,
Dickson/Chebyshev, Dehn filling, `−w₀`, 3d–3d, KKT/Sütő) — **their old anchors are not evidence of
decay**; the `B`-numbers point at where the project *uses* a textbook fact.
**19 decay-eligible** (K008+): **median newest anchor B197**, **12 of 19 below B250**, only K026
within 150 arcs of the frontier.

**Reporting a room-wide staleness figure without that split would have repeated the error B1030
filed against `THE_CLAIM` vs B1000.**

---

**Verdict: PROVED.** 28 mechanical checks.

**Registered, not repaired — L161:** the two gate holes (mention-not-row; `K\d{3}`-scoped so the
ungated documents can never trigger drift), `knowledge/INDEX.md`'s absence from
`doc_currency.py`'s `LIVING`, and the **five firewall breaches**, which need a decision about
whether `knowledge/` joins the `firewall-oneway` string list. **All are one-line changes to
gates — owner decisions, the L159/L160 pattern.** Also registered there: **K009 and K016 share the
filename slug `m1_selection_criteria.md`** and the same topic, K016 self-described as extending
K009, which was never retired.

**Self-correction — the ninth instance of one hazard in eight arcs, and the sharpest yet:
repairing the index moved the very number that motivated the repair.** `knowledge/INDEX.md` was the
**oldest of the nine sweep surfaces** at newest-anchor **B483**, 551 arcs behind the next; the new
K026 row carries **B917**, so an unscoped re-measurement would have reported the gap as far smaller
the moment it was recorded. Every freshness figure here is measured with this arc's own lines
removed.
