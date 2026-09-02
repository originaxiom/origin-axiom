# R51 — the family-wide amphichirality "closure" (B1181: 83/83; B1186: 112/112) rests on a vacuous instrument; the family is mostly chiral

**What the record says.** B1180 (family retraction, adopting cc3's B8147) left "amphichirality at ≥ 83 UNCHECKED by any
seat — an honest open". B1181 then banked THE AMPHICHIRALITY DEBT CLOSED: "83 OF 83 AMPHICHIRAL, zero exceptions …
SPOT-VERIFIED on this bench 5/5 by the reliable mirror-isometry method (m004, s955, o10_150700, o10_150684, t12840) —
deliberately NOT the isometry_signature route (the B1163-era vacuity trap)", and registered a LAW_MAP §G method-law on
it; B1163's family-wide W0 obstruction was upgraded "4-of-14 → 83-OF-83". B1186 (the family is 112) re-enumerated the
family and recorded `amphichirality_failures: []` (112/112).

**The instrument.** Both `B1181/verification/reproduce.sh` and `B1186/verification/family_census.py` test
amphichirality as `W = M.copy(); W.reverse_orientation(); M.is_isometric_to(W)`. SnapPy's `is_isometric_to` accepts
orientation-reversing isometries, so M is always isometric to its own mirror: **the test returns True for every
orientable manifold.** Verified here: True for all 112 members, and True for m015, m016, m009 and the chiral bundle
RRL, whose symmetry groups are not amphicheiral. It is the same vacuity as the `isometry_signature` trap B1165 named,
in a second guise. (The Phase C agents on rows #935 and #954 found the same false positives independently.)

**The non-vacuous tests (`r51.py`, `r51_results.json`).** For every member of B1186's family (B = shape field ℚ(√−3),
112 manifolds; A = all tetrahedra regular ideal, 77): (i) `symmetry_group().is_amphicheiral()` (orientation-aware);
(ii) the Chern–Simons obstruction — an amphichiral manifold has CS ≡ −CS, i.e. 2·CS ≡ 0 mod ½, so CS ∉ {0, ¼} mod ½
proves chirality independently of any isometry search.

| | B (112) | A, all-regular (77) |
|---|---|---|
| amphichiral by symmetry group | **38** | **34** |
| chiral by symmetry group | **74** | **43** |
| of which provably chiral by CS (CS ∉ {0,¼} mod ½) | 36 | (all 36 lie in B; e.g. m202 CS = 1/12, m410 −1/8, s959 −1/6, v3551 −5/24, o10_150700 −1/12) |
| `is_isometric_to(mirror)` | 112/112 True | 77/77 True |

**B1181's own five spot-checks:** m004 ✓, s955 ✓ (CS = ¼), o10_150684 ✓, t12840 ✓ — and **o10_150700, the "H1-killer",
is chiral** (symmetry group order 2, not amphicheiral; CS = −1/12, so provably). Four of five is what the banked "5/5"
actually is.

**What this changes.**
1. B1181's headline (83/83, "zero exceptions, zero undecided") is false; B1180's "UNCHECKED — an honest open" was the
   correct state. The LAW_MAP §G method-law row that B1181 registered ("enlarging a family can only help family-level
   claims") was drawn from a vacuous computation and should be withdrawn or re-derived.
2. B1163's "family-wide W0 obstruction upgrades 4-of-14 → 83-of-83; no sibling among 82 supplies what m004 withholds"
   loses its amphichirality leg: within the all-regular family 43 of 77 siblings are chiral. Whatever the W0 argument
   needs from amphichirality now holds for 34 members, not 77 (and m004's own amphichirality is untouched: D4, CS = 0).
3. B1186's `amphichirality_failures: []` should read 74 failures (43 in A). B1184's `reproduce.sh` uses the same
   instrument on m004 alone, where the answer happens to be right.
4. The seat's own R43 checked the metallic bundles m = 1..6 with the same vacuous call; re-checked here with the
   symmetry group: all six amphicheiral (order 8), CS = 0 — R43's row stands, its method line is corrected.

**Verdict: CONTRADICTED** (B1181 claim vs. computation; B1186 record vs. computation). Sweep #1212 (B1165's worry
that the family-wide spot-check was vacuous) is re-set from SUPERSEDED to STANDS — the worry was right twice.
