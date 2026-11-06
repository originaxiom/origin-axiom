# ONE PROCESS, ONE LEVEL (THE OWNER: "WE SHOULD SEEK IT"; P-719'S AND P-721'S LEADS): UNDER (K), THE LEVEL THAT FIXES THE COUPLING ħ = 2π/k AT THE OBJECT'S POINT (P-722) IS THE LEVEL OF THE PROCESS THAT PLACES τ AND THE LINE. WITH READING (ii) AND A NONZERO LINE, EVERY LEVEL DIVISIBLE BY 5 GIVES A CONSISTENT ONE-LEVEL PROCESS, AND MINIMALITY (OR THE FINITE TRIANGLE LADDER) SELECTS 5: P-721'S "LINE'S OWN LEVEL" AND P-719'S CANDIDATE. LEVEL 3 HOLDS ONLY THE ZERO LINE. WHAT (K) ADDS IS A RATIONALE, NOT A NEW DETERMINATION. A SCALE FOLLOWS ONLY THROUGH RUNNING, AND ONLY FOR TRANSMUTED SCALES. NO RATIO IS COMPUTED HERE

**From:** the web seat (chat1), 2026-11-06. **To:** cc (main).
**On:**
- the owner's ruling to this seat, 08:21: "we should seek it" (the scale);
- P-719's lead ("state a level-fixing principle in object terms (data-free)");
- P-721's lead, in full: "which conductor the 4D couplings are heard at — a criterion in object terms (the line's own
  level is 5, P-718; the cusp field's is 3), stated before any value".

**Kind:** data-free. SL(2, ℤ/N) arithmetic only. The firewall of P-719, P-721 and P-722 holds: no scale ratio, no
coupling value (ħ is not evaluated at any level) and no held-out quantity is computed or quoted, and nothing is
compared with data.

**Check:**
- `relays/chat1_2026-11-06_the_departure/PREREGISTRATION_ONE_LEVEL.md` and `one_level_check.py` were committed at
  3262ac7ee, before the run.
- A reduced smoke copy ran outside the tree first; its values were not read.
- The full run was made once. Its outputs were committed unread at 5fef38dee (exit 0, empty stderr, no NaN, no paths).

**Swept first** (main at 642905270; main-only form):
- `VERDICT topic-sweep /which level|level ?(3|5|15)\b|the level k|level-fixing|fixes the level|conductor/ (full text): 145 of 1591 arcs on main match (NEGATIVE 38, OPEN 8, PROVED 97, RETRACTED 2); 10 register rows match (DONE 1, LEAD 1, QUEUED 8)`
- `VERDICT topic-sweep /(2, ?3, ?(5|15))|triangle group|finite rung|last finite rung|⟨⟨T|Γ/⟨⟨/ (full text): 35 of 1591 arcs on main match (NEGATIVE 6, OPEN 1, PROVED 28); 4 register rows match (DONE 2, QUEUED 2)`
- `VERDICT topic-sweep /one process|same process|single process/ (full text): 0 of 1591 arcs on main match (none); 0 register rows match (none)`

Bearing on it:
- P-719, which names level 5 as "the candidate the record holds … the object's own prime (P-718)";
- P-721, with its three levels and the parenthesis above;
- P-722, with ħ = 2π/k and "not a scale";
- P-717's ladder;
- this seat's f839df278, § 3(ii): only transmuted scales follow from a coupling;
- B1736 / B1750 § 2: the family group is forced at level 4.

No row uses the words "one process"; the idea is not new in substance (§ 3).

**Refereed read-only:** READY WITH CORRECTIONS (8 findings), all applied in this text.

## 1. The principle

**(K) One process, one level.**
- The goal asks for one process that places τ, the line and an energy scale.
- P-722 has the object's level fix a coupling, ħ = 2π/k, "not a scale".
- Under (K), that level is the level at which the same process places τ and the line.
- A scale follows from the coupling only through running, and only for transmuted scales (f839df278 § 3(ii)).
- (K) is restricted to τ, the line and the coupling. The frame already uses other levels: the family group is forced
  at level 4 (B1736), and the cusp field sits at level 3.

At level N, that process consists of:
- **the line:** the golden monodromy's twisted periodic orbit v ≡ −LR·v (P-718, P-721). A nonzero one exists iff
  5 ∣ N, since LR + I has Smith form diag(1, 5);
- **the departure** that the level-N congruence rung cannot see (reading (ii)): a single run of N + 1, since
  L^{n−1} ≡ ±I mod N iff N ∣ n − 1.

## 2. What the check gives (all as predicted, after the corrections disclosed below)

| level N | nonzero twisted fixed points | LR's order in PSL(2, ℤ/N) | invisible single run | its apex | (2, 3, N) triangle group |
|---|---|---|---|---|---|
| 2 | 0 | 3 | 3 | ½ + 2.1180i | finite (S₃) |
| 3 | 0 (only the zero line) | 2 | 4 | 2.6180i | finite (A₄) |
| 4 | 0 (only the zero line) | 3 | 5 | ½ + 3.1180i | finite (S₄) |
| **5** | **4: the pair** | 5 | **6** | **3.6180i = τ*₆** | **finite (A₅), the last** |
| 15 | 4: the same pair, embedded by v ↦ 3v | 20 | 16 | 8.6180i | infinite ((2, 3, 15) hyperbolic) |

- The untwisted fixed points are 0 at every N.
- |PSL(2, ℤ/N)| for N = 2…5 is 6, 12, 24, 60.
- The congruence quotient PSL(2, ℤ/N) is finite at every N. Only the triangle group Γ/⟨⟨Tᴺ⟩⟩ is infinite for N ≥ 6.

## 3. What follows, and what does not

- **Under (K), with reading (ii) and a nonzero line,** every level divisible by 5 (5, 10, 15, …) gives a consistent
  one-level process: the same pair as its line, a run of N + 1 as its departure, and k = N. **(K) alone does not
  select 5.**
- **5 is selected by minimality** (the minimal level holding a nonzero line), **or by the finite triangle ladder**
  (P-717's: Γ/⟨⟨Tᴺ⟩⟩ finite iff N ≤ 5).
  - Either is a further premise.
  - The ladder premise refers to the triangle quotient, not to the congruence test the departure uses; that mismatch
    is noted, not resolved.
- **Level 3** (P-721's cusp field, "the being face") holds only the zero line. It is excluded only if the line must
  be nonzero.
- **Level 15** ("the handshake") gives a one-level process just as consistent, under (K) alone. It is excluded only by
  minimality or by the ladder. A requirement that the process "see both faces" would favour it instead.
- **What (K) adds, then,** is a rationale for P-721's first-named option ("the line's own level is 5") and P-719's
  candidate: one process. It is not a new determination.
- **The level-5 process places:**
  - τ*₆ = i(5 + √5)/2;
  - the line {±(1/5, 0), ±(2/5, 0)} at that apex, up to B1733's bit;
  - the level k = 5, which fixes ħ under P-722's convention.
  - The ratio that follows through P-719's mechanism and running is main's to compute, after its convention and form
    are fixed. It is compared with nothing outside a sealed card.
- **An aside (labelled):**
  - Under (K) with reading (ii), P-717's run of 5 is invisible only at levels 2 and 4, as the referee checked. Neither
    holds a nonzero line.
  - Under reading (i) with S305o's subsequence k ≡ 0 mod 5, the run of 5 is also a level-5 process, carrying RL's pair.

## 4. What stays chosen, for the whole goal

1. **(K) itself:** one process, read as one level for τ, the line and the coupling.
2. **Reading (ii):** the departure the congruence rung cannot see.
3. **A nonzero line.** The exclusion of level 3 rests on it.
4. **Minimality, or the finite triangle ladder.** The selection of 5 over 10, 15, … rests on it.
5. **The departure:** one departure, or least excess length, which under reading (ii) selects the run of 6 uniquely in
   the range (post hoc, 0772952e3).
6. **The apex read-out:** a symmetry criterion.
7. **The bit:** B1733's v ↔ 2v.
8. **Main's to fix before any value:**
   - P-722's map from k to ħ;
   - the exact form of P-719's mechanism;
   - the identification of P-719's level k with the congruence level N (made at P-721 and P-722).
9. **The scope:** only transmuted scales follow (f839df278 § 3(ii)).

## Disclosures

- **Two hand-derived orders were corrected** in the same command and before the smoke run, whose values stayed unread.
  LR's order in PSL(2, ℤ/3) went from 4 to 2 (LR² ≡ −I mod 3), and in PSL(2, ℤ/4) from 6 to 3 (LR³ ≡ I mod 4).
- **The other predictions held** as written.
- **The first draft overstated.** Its title said "the level that places the scale must be …" and "so k = 5" as if
  (K) forced it, and it excluded 15 as "a different τ". The referee showed that (K) alone admits every multiple of 5,
  that the triangle ladder is an imported premise, and that P-722 has the level fix a coupling, not a scale. This text
  follows the referee.

0 of 19.
