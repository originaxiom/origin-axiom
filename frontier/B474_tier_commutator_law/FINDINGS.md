# B474 — the tier–commutator correspondence: seat-1's claim refuted, the exact law found underneath

**Status: banked (frontier). Firewalled. Incoming: seat-1's final-handoff Priority 1
("zero dark points at quantum closure" — UNVERIFIED, float tiers). Adjudicated exactly
(F_p commutators × B459's exact tiers, the B468 machinery): the claim is the SEVENTH
float-kill — and the corrected table is a new exact selection-rule law. No H1.**

## The exact cross-table (240 points; commutator traces exact at p = 61; tiers exact ℚ(ζ₆₀))

| tier | tr = −5 | tr = −1 | tr = 3 | tr = 15 (closure) |
|---|---|---|---|---|
| free (120) | 8 | 32 | 80 | **0** |
| rs (20) | 0 | 0 | 0 | **20** |
| qs (20) | **20** | 0 | 0 | 0 |
| qrs (10) | 0 | 0 | 0 | **10** |
| dark (70) | 0 | 0 | 16 | **54** |

(Commutator-trace counts on the torus: −5: 28, −1: 32, 3: 96, 15: 84. Seat-1's numbers —
58 closure points, 0 dark at closure — were float artifacts; exact: 84 and 54.)

## The laws (exact, 240/240)

1. **Full activity requires non-commutation**: free ⟹ tr[W₁ʲ,W₂ˡ] ≠ 15 (120/120). The
   seam is fully alive ONLY where the quantum interaction does not close.
2. **The partial tiers are commutator-pure**: rs ∪ qrs ⟹ closure (30/30); qs ⟺ the
   non-free points of tr = −5 (20/20). Each partial-vanishing tier sits inside a single
   commutator level set.
3. **Darkness concentrates at closure**: 54/70 dark at tr = 15 (77%), the rest at tr = 3;
   no dark point has tr ∈ {−1, −5}. Seat-1's direction was inverted: darkness does not
   avoid closure — it lives there.

## Adjudication

The identification (j,l)-torus ↔ dual (x,y)-torus is nominal (both index ℤ/20×ℤ/12), so
the correspondence demands a mechanism: the candidate is CRT-laundering — both functions
plausibly factor through the same residue data ((B472): the commutator trace = the Weil
character of [A₁ʲ,A₂ˡ] mod 15; (B459/B431): the tiers ride the CRT lines). If the
derivation closes, the correspondence LAUNDERS into "two shadows of one residue map" —
which would still be a genuine structural unification (the selection rules ARE commutator
data), the strongest positive form of the year's selection-rule story. Derivation = the
next wave; the physics naming ("activity ⟺ non-abelianness") is HELD per the standing
rules. Note for the criticality program: closure addresses = CRT-central (B472), so law 1
reads "the seam's full activity lives away from the central locus."

## Reproduce
```
python3 cross_table.py     # the exact table (F_p commutators x exact tiers)
pytest ../../tests/test_b474.py
```
