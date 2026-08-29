# B1211 — THE DECLARATION GAP: the programme's newest theorems were invisible, because the gate reads a field the seat fills in

**Verdict**: `OPEN` (instrument arc) · **2026-08-29** · **Gate 5 clean** · continues B1210 into the
541 substantive arcs its criterion did not reach

## 0. What the deep sweep was for, and what it actually found

B1210 fenced its own pool honestly: `creates_law` plus the registered synthesis surfaces reached 421
arcs, and **610 substantive arcs were left unswept**. This arc swept them, scoring each on two
independent axes — **result-strength** (does the claim assert a theorem-grade fact?) and
**thesis-proximity** (does it speak the paper's three movements?).

**The finding was not a missing claim candidate.** The ranked list surfaced *the programme's own most
recent theorems* as unswept — B1183, B1184, B1200, B1182 — which is impossible if the sweep's
criterion is sound. Checking directly:

| arc | on a registered synthesis surface? |
|---|---|
| B1182 C4′ resolved | **none** |
| B1183 the one-class theorem | **none** |
| B1184 the quine split verdict | **none** |
| B1192 the relational bit exists | **none** |
| B1195 κ, the bit's law | SM_SPECIFICATION_LEDGER |
| B1196 selector-free | **none** |
| B1200 Φ₃, one polynomial three faces | **none** |
| B1203 two probes | **none** |

**Seven of eight.** `THEOREM_REGISTRY.md`'s last row was **B1145** — the entire observer-layer
closure, the densest theorem cluster the programme has produced, was registered nowhere.

## 1. The mechanism, and it is sharper than B1207's

`gate_theorem_registry` enforces *"every arc declaring `creates_law = true` appears in the
registry."* That catches **over**-declaration. It is structurally blind to **under**-declaration —
an arc declaring `false` is invisible to it. And **the seat that writes the claim also writes the
flag**, so the gate inherits the seat's judgement, including its mistakes.

This seat declared `creates_law = false` on an arc **titled THE ONE-CLASS THEOREM**. No row was ever
required; nothing surfaced it; B1210's mechanical pool could not see it; and only the *memory*-written
spec carried it into the paper at all.

> **A GATE THAT READS A SELF-DECLARED FIELD IS ONLY AS GOOD AS THE DECLARATION.** B1207's lesson was
> *a gate only works where it is reached*. This is the next one in: **a self-declaration gate is not
> an independent check — it is the seat's own judgement, wearing a gate's uniform.**

## 2. The repair

**Seven arcs corrected** to `creates_law = true`, each carrying a **dated `creates_law_corrected`
note** — the claim, verdict and evidence are untouched; only the mis-declared metadata moves:

`B1182` the V₄ named-action torsor identification · `B1183` the one-class theorem · `B1184` the
quine split verdict · `B1185` the three-mechanisms theorem · `B1192` the relational bit's existence ·
`B1196` selector-freedom + the three-regime dichotomy · `B1200` the Φ₃ three-faces law.

**Seven THEOREM_REGISTRY rows landed in the same commit** — written as claim rows, so they double as
P3's evidence rows.

**Two controls, because a review that flipped everything it looked at would be a sweep, not a
judgement.** `B1203` stays `false` on its own words — *"only THE READING is new … an interpretation
joining banked facts, not a theorem."* `B1204` stays `false` because it reads the **shape** of this
record's own successful forcings — a taxonomy of the corpus's arguments, not a new theorem about the
object; it uses theorem-grade language *about* theorems, which is exactly what tripped the lexical
screen.

## 3. The counter-check, installed — and it fired on installation

`declaration_check.py` flags arcs whose **claim talks like a theorem while the flag says otherwise**.
Locked **forward-only from B1180** (history is never flipped; the 26 corpus-wide candidates are
recorded, not retro-flipped). The lock accepts **either** a flip **or** a dated recorded decision:
**what it forbids is silence** — an arc that talks like a theorem and never says why it is not one.

It caught **B1185 and B1204 immediately**, neither of which this seat had re-read. One was a theorem;
one was not. That is the instrument working in both directions on its first use.

## 4. The instrument needed its own scope correction — the third of that species today

The first pass **lost B1183 and B1200**, because its disown-list contained *"cited, not"* and
*"harvest"* — words that appear in the **fences** of genuine theorems, where an arc limits a
*borrowed* computation rather than its own result. B1183's fence (*"B760's … are THEIR locked
computations (cited, not re-run)"*) was read as a disclaimer about B1183.

> **The pattern, now nameable**: this is the **third** scope failure of the same species in one
> session — B844's greedy regex ate a colon-free reason whole; B1210's matcher applied every verb in
> a claim to every reference in it; this one applied a fence on an input to the arc itself.
> **Lexical instruments over this corpus need clause- or region-scope**, because an arc claim is one
> long sentence carrying fenced material about many things. Fixed here to strong self-limits in the
> **headline region** only.

## 5. The reusable finding

**Memory and mechanism are complementary, not redundant.** The memory-written spec caught the
observer-layer theorems the mechanical pool structurally could not see; the mechanical pool caught
the older forced material (the Levi deflation, the ℤ₆ footing) that memory had smoothed over. B1210
concluded *"a spine assembled from memory reproduces the memory"* — true, and this arc supplies the
other half: **a spine assembled from a criterion reproduces the criterion.** The paper needs both
passes, and now has both.

## 6. Fences

The detector is **lexical**: it screens, it does not adjudicate. It caught 3 of the 6 arcs this seat
judged by reading (B1182/B1183/B1184) and missed B1192/B1196/B1200, whose claims state their results
without the word *theorem*. **Coverage of the remaining unswept arcs as paper claim candidates is not
claimed** — the deep sweep's ranked list is a screen for the editorial pass, not a disposition.
