# B1434 — THE ARCHITECTURE CENSUS: two generated states carry a generation-shaped background at their own level, which the root cannot; orbits of three at the three-fold level are common across the grammar, not the root's; and every background everywhere counts one

cc, 2026-10-01. Sealed at `5f3fdf01` (PREREGISTRATION.md, sha-256 `8a1282fd…`) before any index was computed on a
state other than the root. Occasion: the owner's direction of 2026-09-30 to account for the whole allowed
architecture, and lead L222. **Verdict: PROVED (the census, 68 levels, 942 268 modules, three primes each, no level
differing at any prime). Of seven sealed predictions, four held (P1, P2, P3, P6) and three failed (P4, P5, P7).**

## 0. Seen from above

The record has computed the Standard-Model-frame index on the root's tower (sm:B1375, B1427, sm:B1506, B1432), on the
sister's tower for lifted backgrounds (xB027), and on members of the root's class (B1418). It had not run the complete
census — lifted and non-lifted — over the states the genesis grammar generates. This arc does, for every signed word
state to length six and every cyclic level with fibre torsion to 330.

## 1. The sealed predictions, read

| | prediction | prior | outcome |
|---|---|---|---|
| P1 | every generation-shaped background has \|count\| = 1 | 85% | **YES** — all 8 800 |
| P2 | h¹(λ) = 1 at every locus | 90% | **YES** — all 5 156 |
| P3 | some state other than the root carries a generation-shaped background at its own level | 55% | **YES** — two of 23 |
| P4 | the three-fold cover of every state carries orbits of three | 45% | **NO** — 10 of 12 |
| P5 | orbits of three at a three-fold level never lift | 60% | **NO** — five levels lift |
| P6 | signs split equally wherever backgrounds exist | 80% | **YES** — every level |
| P7 | every deck orbit has size greater than one | 70% | **NO** — two levels, and they are P3's states |

## 2. What was found

**(a) Two states carry generation-shaped backgrounds at their own level.** The root has none and cannot: its fibre has
no finite character.

| state | manifold | H₁ | loci (non-square) | firing | backgrounds | lift | ν^c |
|---|---|---|---|---|---|---|---|
| (−, LLRLR) | m369, chiral, vol 4.7517 | ℤ/12 ⊕ ℤ | 12 (6) | 40 | **8** | none | absent |
| (−, LLLRLR) | s639, chiral, vol 5.1335 | ℤ/15 ⊕ ℤ | 15 (0) | 72 | **16** | all | generation's sign |

Each count is ±1, four and eight of each sign. Checked three further ways (`verification/own_level_checks.py`): on
SnapPy's own presentations of m369 and s639 with a third prime set; and in exact arithmetic, where the full index
tables over ℚ(ζ₁₂) and ℚ(ζ₁₅) equal the prime-field tables entry by entry. On their double covers the same
backgrounds appear as deck-fixed orbits of size one: pullbacks, as they must be.

**(b) Orbits of three at the three-fold level are common.** Ten of the twelve three-fold levels in range carry
generation-shaped backgrounds, all in deck orbits of three:

| state | backgrounds | of which lift | ν^c with the generation's sign |
|---|---|---|---|
| (+, LR) the root → s961 | 48 | 0 | 48 |
| (−, LR) the sister m003 | 96 | 0 | 0 |
| (+, LLR) m009 | 48 | 48 | 0 |
| (−, LLR) m010 | **0** | — | — |
| (+, LLLR) | 72 | 0 | 24 |
| (−, LLLR) | 48 | 0 | 48 |
| (+, LLRR) | **0** | — | — |
| (−, LLRR) | 144 | 144 | 0 |
| (+, LLLLR) | 216 | 216 | 72 |
| (−, LLLLR) | 48 | 48 | 0 |
| (+, LLLLLR) | 720 | 240 | 48 |
| (−, LLLLLR) | 360 | 0 | 96 |

So three is the size of a deck orbit on a three-fold cyclic cover of most states, not a property of the root or of
s961. The root's row is not unique in any column: (−, LLLR) also has 48, none lifting, every one a whole generation.

**(c) One count per background, everywhere.** 8 800 generation-shaped backgrounds on 68 levels of 24 states: every
charged-sector count is ±1, every locus has h¹ = 1, the signs split equally on every level, and the index is
deck-invariant on every level. The law the record found on the root's tower is a law of the grammar to length six.

**(d) Levels that are one manifold under two decks.** (−, LR) at level six is the root's level six as a manifold;
its 2 160 backgrounds fall into orbits 6: 2 064 and 3: 96 under the sister's deck against 6: 2 112 and 3: 48 under
the root's. The orbit structure belongs to the deck, not to the manifold.

## 3. What it means

- **For the question that occasioned it.** The widened frame does hold something the root's own level lacks: a
  generation-shaped background on a state itself, with no cover and no deck, on m369 and on s639. What it holds is
  one background with count one. It is not three, and nothing in this census selects m369 or s639.
- **For three.** B1432's reading, "three is an orbit of the root's deck on the root's only three-fold cover", loses
  its last two words. The orbit is generic. If three generations are to come from this mechanism, what singles out a
  state is not the mechanism.
- **For the root.** Nothing in the census distinguishes the root except that it is the state with nothing at its own
  level, torsion 1.

## 4. The fence

Main's B1297 class index on reducible non-split doublet modules. Non-semisimple backgrounds. The three members of
an orbit are three backgrounds. **The frame is main's E₆/27 frame carried to every state as an instrument**; that it
is the right frame on a state whose trace field is not ℚ(√−3) is neither claimed nor tested. No physics reading, no
value, index is not a generation count.

## 5. Caveats

1. Prime fields: three primes per level, every firing module re-checked at two; no level differed. Exact arithmetic
   only for the two own-level tables.
2. Scope: word length six, torsion 330, cyclic covers dual to the fibre. States with the orientation-reversing half
   step, non-cyclic covers and fillings are outside.
3. The states are taken up to rotation and swap; a state and its mirror are one row.
4. (−, w) at even level is (+, w) at that level as a manifold; both rows are kept because the decks differ.

## 6. Registered

- Why (−, LLR) and (+, LLRR) carry no orbit of three while ten others do: a criterion in the fibre torsion or in the
  deck's action on it. Lead.
- The own-level law: which states carry a generation-shaped background at level one, beyond length six. Lead.
- Whether m369's and s639's backgrounds survive in a frame built from their own arithmetic rather than the root's.

## Verification

`verification/architecture_census.py` (the sealed instrument), `run_parallel.py` (the runner, calling it unchanged),
record `architecture_census.json` and the four `census_slice_*_run.txt`; `control_m004_tower.json` (C1, before the seal);
`own_level_checks.py`, record `own_level_checks.json`. Lock: `tests/test_b1434_architecture_census.py`.
