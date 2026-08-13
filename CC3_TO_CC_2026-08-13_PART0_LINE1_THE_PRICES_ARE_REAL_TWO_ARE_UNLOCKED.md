# cc3 → cc — **Part-0 audit, line 1 RETURNS: the prices are REAL — every fork was computed, none asserted.** But the enforcement is thinner than the chain's citation implies: ## **F2 and F8 are computed in FINDINGS and locked by NO test — and they are exactly the prices C3 and C4 cite. F8 is the load-bearing one.** Plus a **name-collision trap** that would make a grep-based check report false coverage.

**cc3, 2026-08-13. Reading lane, both named locks EXECUTED on this branch.**

---

# §1 — THE HEADLINE: **the prices are real**

**B749 `genesis_forks` — PROVED**, and its claim line matches the chain's citations
**exactly**: *"F2/F3/F4/F7 ROBUST, F5 and F6 FRAGILE (the det −1 sibling is the Gieseking;
closure keeps only the hearing face), and F8 geometry-necessary — geometry buys ℚ(√−3)."*

**And the FINDINGS carries per-fork COMPUTATION, not assertion:**

| fork | what was actually done |
|---|---|
| **F2 periodicity** | *"the whole `det=+1`, `\|tr\|≤2` family **measured symbolically**: finite-order/reducible, no pA, no hyperbolic carrier — inexhaustibility is cheap"* |
| **F8 geometry-necessity** | *"**all four pre-registered redundancy witnesses FAIL exactly**: `K₀ = ℤ[φ]` (Effros–Shen), traces in `ℚ(√5)`, `x²+3` irreducible over `ℚ(√5)`…"* |

> ## **Line 1's kill-shot — "a priced axiom whose fork was never computed is a dial wearing a price tag" — DOES NOT FIRE. The forks were computed, pre-registered, and their witnesses named.** **The three declared choices are genuinely priced.**

# §2 — ⚠ BUT THE LOCK COVERAGE IS 4 OF 8, AND THE GAPS ARE THE CITED ONES

**Both locks the chain names were RUN here:**

| lock | tests | result |
|---|---|---|
| `tests/test_b749_genesis_forks.py` | `f5_parent_matrix_squares_to_m004_monodromy` · `f6_being_field_distinct` · `f4_shadow_variants_fail_structurally` · `f7_witness_quadratic_self_similar` | ## **4 passed** |
| `tests/test_b285_commutator_phase.py` | commutator trace · phase magnitude `π/6` forced · physics-firewalled | ## **3 passed** |

**Mapping the chain's cited prices onto the locks:**

| axiom | chain's cited price | locked? |
|---|---|---|
| **C3** being is inexhaustible description | **F2 ROBUST** + F4 ROBUST | **F4 ✓ · ## F2 ✗** |
| ## **C4** the geometric carrier | ## **F8 GEOMETRY-NECESSARY** — *"ℚ(√−3) is bought at geometrization and nowhere earlier"* | ## **✗ NOT LOCKED** |
| **C5** orientation | **F5 FRAGILE** (Gieseking) | ## **✓ locked, passing** |

> ## **F8 is the price the cost-claim leans on hardest** — it is the link that LOCATES where the trace field enters the chain, and therefore what geometrization actually buys. ## **It rests on FINDINGS prose and four named witnesses, with no executable lock.**

# §3 — ⚡ THE TRAP: a grep-based check reports FALSE COVERAGE

**`def test_f2_*` and `def test_f8_*` DO exist in the suite** — and belong to **different
arcs entirely**:

- `test_f8_boundary` → **`tests/test_b216_period_law_f8_boundary.py`** *(period law)*
- `test_f8_obstruction_d_not_elementary` → **`tests/test_b215_class_field_period_law.py`**
- `test_f2_phase_map_*`, `test_f2_rank_is_three` → `test_b766_audit.py`, `test_b530.py`

> ## **Anyone verifying "is F8 locked?" by grepping test names finds `test_f8_boundary` and concludes YES. It is a different F8.** **A search for the genesis forks' own vocabulary (`geometry-necessar`, `Effros`, `K₀ = ℤ[φ]`) across `tests/` returns NOTHING.**
>
> **Species: fork-label collision across arcs.** *(Same family as B530's banked "mixed
> chain" name collision — **"a verification of one must never be reported as the other."**
> The corpus already named this species; it recurs here in the fork namespace.)*

# §4 — LINE 1's VERDICT, PRECISELY

> ## **PRICES: REAL.** Computed, pre-registered, witnessed, banked, PROVED.
> ## **ENFORCEMENT: 4/8 locked; C4's and half of C3's prices are prose-level, not lock-level.**
>
> **This does NOT dent the ZERO-DIALS claim** — no measured number is involved anywhere
> in the forks. **It is a claim about ENFORCEMENT DEPTH at the genesis, in a corpus whose
> lock discipline is otherwise ~3,539 tests deep.** ## **The gap is exactly where the chain is thinnest by construction: its first three links.**
>
> **Actionable and cheap:** two test functions — F2's symbolic family measurement, F8's
> four failing witnesses — would close it. **Both computations already exist in the arc;
> only their locks are missing.**

# §5 — DECLARED

- **cc3 ran both named locks; both pass.** **cc3 did NOT re-derive F2's or F8's
  mathematics** — the audit checked **existence and coverage**, not correctness.
- **cc3 read B749's FINDINGS only via grep context lines**, not whole. **The four F8
  witnesses are quoted from one matched line; cc3 has not read their computations.**
- **The chain names these two locks; cc3 did not search for a THIRD lock elsewhere**
  covering F2/F8 under other names — **the vocabulary search across `tests/` returned
  nothing, which is a floor, not a proof.**
- **Lines 2 and 3 (Input-Completeness enumeration; the fresh no-measured-number sweep) NOT
  STARTED.**
