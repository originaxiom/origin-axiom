# B2016 — Listening 30: the null control — the whole's small group on every one of its coset spaces; the halving in the whole's form holds on fewer than one in ten, among them the whole's own orbit

**Verdict: PROVED for its checks (exact: GAP's subgroup classes and coset actions, FLINT's sector polynomials).** Main,
2026-11-26, in the author's /loop "continue the listening line". Data-free. 0 of 19.

## Seen first

- **The guard:** on 2026-11-26 main named a null control as a guard against hearing the group's properties as the whole's.
  B2012 found one law that is the group's: the four-move pairing on every orbit.
- **B2009:** the halving is decided by the stabiliser's condition. **B2005:** the stabiliser of (3,3,3) is ⟨C⟩ at mod 27
  and 81. **B2014:** the halving is exact on (3,3,15)'s orbit, which has no fixed point of C.
- **Swept:** `VERDICT topic-sweep /null control|coset space|every subgroup|conjugacy classes of subgroups/: 6 of 1757 arcs on main match (NEGATIVE 3, PROVED 3); 1 register rows match (QUEUED 1)`.
  None runs the halving over a group's coset spaces.
- **The literature (standard):** a transitive action is the action on the cosets of a point stabiliser. Two transitive
  actions with conjugate stabilisers are isomorphic.

## The checks (expectations hashed before the run)

The test case is G_k acting on G_k/H for a representative H of every conjugacy class of subgroups. The six moves are read as
the words σC², σC, Cσ, C²σ, CσC and C²σC², and the sector polynomials are computed exactly.

| | G₃ (mod 27, order 216) | G₄ (mod 81, order 1944) |
|---|---|---|
| classes of subgroups | 45 | 100 |
| (a) p_neutral(2x)/2^d = (x² − 9) x S(x), the whole's form | **4** | **8** |
| (b) every charged mode paired, not in that form | 10 | 28 |
| (c) neither | 31 | 64 |
| the whole's stabiliser ⟨C⟩ | (a); index 72, C fixes 3 | (a); index 648, C fixes 3 |
| the classes in (a): \|H\| | 3, 9, 12, 36 | 3, 9, 12, 27, 36, 81, 108, 324 |

- **N0 holds:** the coset action on G/⟨C⟩ reproduces the whole's halving at both levels.
- **N1 holds:** at mod 27, (a) holds on 4 of 45 classes (9%). Every class in (a) has C fixing exactly three cosets and ρ
  non-trivial on H. The whole's stabiliser is among them.
- **N2 holds:** at mod 81, 8 of 100 (8%), with the same features.
- **Post hoc, labelled** (`overgroups_posthoc.py`, `overgroups_join.py`, written after the run was read): the classes'
  categories against whether H contains a conjugate of C, that is, whether G/H is a G-quotient of the whole's orbit
  G/⟨C⟩. Every class in (a) contains one (4 of 4 at mod 27, 8 of 8 at mod 81), and no class in (b) does. The converse fails:
  of the quotients of the whole's orbit, 4 of 8 at mod 27 and 4 of 12 at mod 81 do not halve (category (c)). So in the
  cases run the coset spaces that halve in the whole's form are quotients of the whole's own orbit, but not all of them.

## What the whole does, read in its own terms

- **The halving is not the group's.** The same group, with the same six moves, halves in the whole's form on fewer than one
  coset space in ten. On most of them (69% at mod 27, 64% at mod 81) the charged modes do not even pair.
- **The whole's own orbit is among the few that halve, and every other one that does is a quotient of it** (post hoc).
- **What they share,** in the cases run: ω's exchange fixes exactly three points, and the order-6 character is not trivial
  on the stabiliser. With B2009, the stabiliser is what decides.
- **So the halving is a property of the whole's orbit within its group.** That answers the question the null control was
  set to ask. The group's twist is necessary; the whole's stabiliser makes it hold.
- **No rate is read as physical, and nothing is compared with data.**

## Disclosures

- The card was hashed before any run.
- The first form of `cosets_gap.py` stopped at `import flint` before any output, because sage's Python has no python-flint.
  It was split into a sage exporter (`cosets_export.py`) and a FLINT classifier (`cosets_gap.py`).
- The exporter's first run stopped before output: GAP's FactorCosetAction refused the class of index 1. It now uses the action
  on the right cosets. Both changes are commented in the scripts.
- The exported actions (`coset_actions.json`, sha256 54f6b96b…) are regenerated, not committed.
- A conjugacy class of subgroups is represented by one subgroup; conjugate subgroups give isomorphic actions, so nothing is
  lost.
