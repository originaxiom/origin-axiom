# The integration census — every lane, what main has verified, what it only holds (2026-10-13)

*Main seat (cc), after S114, at the owner's request (2026-10-13): "process properly all the seats, and integrate the
knowledge from them, so no calculation, computation or achievement is lost."*

Nothing is lost in the sense of being unrecorded: every lane is pinned at its head and its items are rowed
(`docs/HARVEST_LEDGER.md`, `docs/RELAY_LEDGER.md`). This page records how deep each row goes, where main relies on
something it has never recomputed, and the queue that pays that debt. It was built from two reading passes over the
lanes and the ledgers, and checked by main against the ledger rows it cites.

## 1. The lanes

| lane | head = pin | integration depth |
|---|---|---|
| SM-derivation seat | `6877cc87` (2026-10-09) | 53 W-items. 18 are verified on main, wholly or in part (W1–W4, W6, W9, W10, W19–W22, W26, W39, W41, W43, W45, W50, W51). Most of the rest are registered, and seven of those are relied on (§2). |
| audit lane (physical bridge) | `7416a63b` (2026-10-13) | 101 commits of 2026-10-09..13 and 34 relays, read at headline level (S114). No packet re-run on main except B1629's replay, which main took. |
| fork lane (the codex app seat) | `0c6570ba` (2026-10-13) | Its 49 commits and genesis root review read at headline level (row 1087); rows 1017–1048 registered. |
| web seat (chat1) | `d40c1ab6` (2026-10-06) | Its verification pass is now rowed (row 1088); the background census itself stays registered (row 899). |
| cloud (outside bench) | `13d2c5b6` (frozen 2026-09-18) | Memos 218–236 registered at headline level. |
| sep16 | `3205984b` (2026-09-29) | xB014–xB034 registered; xB020 partly verified (B1472). |
| review (outside referee) | `5d58b935` (2026-10-01) | Read in full. |
| LP (listening thread) | `8b6df98f` (2026-10-06) | LP01 read at headline level; not verified on main (R60-3). |
| hypatia, hostile | at head | Watched, dormant. |
| weave archive | `d7e4afeb` (2026-10-11) | **Incomplete until the owner uploads one file** (§5). The thirteen earlier weave runs live only in the owner's download until then. |

## 2. Verification debt: what main relies on but has not recomputed

Ranked by how much rests on it.

1. **W46 — the four-dimensional index is n times the fibre's index.** It carries GENESIS v1.37 and v1.39's "±3 given Λ
   and the unit" and THE_WEAVE's statement about the weave's surface. B1632 and B1634 recomputed W45's χ_{3/2} only.
   W46's puncture weights (3/2, 1, ½) and its cusp shift were never recomputed. The fork lane's `cusp_spin_extension`
   adds a specific warning: testing W46's sign alone is not testing the extension change. **First in the queue.**
2. **W44's c-gauge frame** (98 subgroups). It is behind GENESIS v1.36's "the 13 unreduced in every frame on record".
3. **W52's count (11 of 13 at weight 3).** Cited in THE_WEAVE. B1637 is checking it and the fit behind it.
4. **W24 and W30** (the six-dimensional census; the order-3 flux allowed, not forced). Cited in GENESIS three and two
   times.
5. **W23, W27 and W28** (at most two complete generations in E₈ frames on the fibre; "derived given Λ"; the qubit).
   Each is cited in GENESIS. W28 is consistent with B1606.
6. **W47** (no forcing of the cusp's unit). It is consistent with B1632's twist table, where a flat twist moves χ by at
   most one.

**Two stale rows, corrected now.** W41's multiplier (row 1052) and W45's χ_{3/2} (row 1063) are verified on main (B1632,
B1634), and both rows now say so. W41's explicit zero-mode form and its norm test remain the seat's.

## 3. Results from the other lanes that main has not verified, ranked

1. **A charged three on a connected double cover** (audit lane, `silver_cover_families`, `silver_cover_currents`):
   three left-handed 10 + 5̄ with gauge currents, on a supplied E₈ parent and an unselected boundary, 82 chiral
   components. It is the only result anywhere on the record that yields three with gauge content.
   **Tension with GENESIS:** T-NO-INDEX-IN-THREE (B1604) says no count on a cusped 3-manifold or its covers is an index
   with the shape identity. The lane works on a different object, a 2D punctured elliptic cover with an E₈ parent. Main
   must check whether this three is the Λ-given ±3 in another dress or something new.
2. **A non-zero inter-family cubic** on that cover (`silver_cover_cubic`), against a zero cubic on the earlier selective
   domain. That boundary dependence is itself a count-relevant fact.
3. **The fork lane's flavour-charge constraints** (`matter_line_compatibility`, 60 exact checks; `puncture_symmetry`,
   2,681 exact checks). They tie the two diagonal flavour charges to (a, −a) and exclude intermediate subspaces. They are
   direct inputs to the free-number count, and cheap to re-run (exact arithmetic).
4. **The fork lane's carrier-premise results** (`positive_carrier`, `cohomology_carrier`). Positive-word fidelity, order
   and substitutions do not force a faithful F₂ carrier, and the quotient F₂/F₂‴ keeps the doublet. This bears on
   GENESIS GM4; the lane leaves GM4 itself untouched. Exact arithmetic, cheap to re-run.
5. **The fork lane's analytic domain work** (`puncture_fredholm`: index dim Λ − 3; the total domain; a uniform vertical
   cusp gap). It firms up W45/W46 as statements about operators. These are authored analyses awaiting specialist
   review.
6. **The audit lane's E₈ embedding** of the puncture coefficient (a conditional join) and **its four-dimensional
   Yang–Mills lift of the cusp unit** (the lift duty for FK10's unit, without selecting it).
7. **The audit lane's Higgs-pair quartic, zero** on its domain, and boundary-dependent. It is the only Higgs-sector
   quantity on any lane.

## 4. Engaged too little

- **W49:** the generations are one zero mode three times (T = ℓ ⊗ M), so the end conditions that keep three are exactly
  those blind to M. It bears on FK10 and the count.
- **W25:** the weave's bundles are self-conjugate, so FK11's dictionary cannot come from them.
- **W36:** the bulk gives no SU(5) chirality on a two-dimensional object.
- **W48:** three would need 24 lattice-free chiral bosons.
- **Not yet in the seat's dossier:** main's correction to W50 ("degenerate at i" depends on the weight mod 4) and the
  golden theorem (B1636–B1639). Relayed.

## 5. What only the owner can do

- ~~Upload the weave archive.~~ **Done 2026-10-13 at the owner's "do as u recomend"** (efadcdea): the recovery ZIP,
  unchanged, restored by the branch's own script run locally; 291 members, 289 manifest entries and 254 original members
  byte-verified; the receipt VERIFIED. The branch workflow was removed because the tracked-forbidden gate forbids
  tracked `.github/` files. Read the same day (HARVEST_LEDGER row 1090).
- The open owner decisions now live in `docs/POINT_REGISTER.md` (disposition OWNER).

## 6. The queue

1. **W46 on main** (the next verification arc).
2. **The fork lane's exact-arithmetic packets** (§3, items 3 and 4): re-run, then a GM4 reading.
3. **The cover three against T-NO-INDEX-IN-THREE** (§3, item 1): same object or a new one.
4. **W44's c-gauge frame**, then W24 and W30.
5. **The near-fixed-point mechanism on the ruled branch.** τ = ω's retirement (GENESIS v1.35) rested on B1618, whose
   argument used the inner automorphisms, and B1634 has since scoped those away. Near the tick's point i, couplings of
   weight 3 mod 4 drop to rank 2. Not yet computed.

## 7. The frame audit (B1640) and the point register

At the owner's question ("where our naivities lies … what angle are we missing"), three referee lenses read the record's
frames rather than its results: the mathematical chain, the physics dictionary and frames, and patterns across the whole
record. Main re-ran what they found with its own sealed instrument (B1640, GENESIS v1.42):

- **At ω only the single pieces of T ⊗ T are degenerate**; T̄ ⊗ T and mixed couplings are not (B1635's own read-outs).
  τ = ω's retirement stands as "no hierarchy found".
- **The multiplier carries a hand**: two binary conventions pick the theta multiplier or its conjugate; the record's allows
  the index's weight 3/2 and the golden coupling, the conjugate neither; the hand is not derived.
- **TM1 cannot come from one τ** on the ruled branch.
- **Positivity excludes −I from the updates, not from the group** the multiplier uses.
- **The naivety, in one line:** the record audits results and never premises; "forced", "every" and "no choice" were frame
  claims nobody tested; and the dictionary (holomorphy, Kähler term, every field in one T, τ evaluated rather than a field)
  was imported unstated. The owner's reading: **"if the principle is the seed, we miss the field."** The SM seat's §60–§61
  (W54, W55) reach the same place from the fits: the weave fixes shapes, not sizes; nothing on record tells the sectors
  apart; what would is the Higgs sector's flavour structure.
- **The strongest unpursued lead** (two lenses independently): the couplings as overlaps of the fibre's zero modes (L251).

Every point the lenses, the intake and this census raised — 86 of them — is rowed in **`docs/POINT_REGISTER.md`** with a
disposition and one queue, enforced by the gate `point-debt` (the owner, 2026-10-13: "fail to address all the points we
made … lets prevent that this time"). The queue in §6 is superseded by the register's.

*This census is a reading, not a verification. Every "registered" above stays registered until an arc recomputes it.*
