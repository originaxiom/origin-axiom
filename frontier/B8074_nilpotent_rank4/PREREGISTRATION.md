# PREREGISTRATION — B8074: does the rank ceiling cover nilpotents?

**Sealed before the first run.** Reproducer `nilpotent_rank4.py`. Gate 5: no physical
identification; every statement is about `e₆`, its Levi subalgebras and its nilpotent orbits.

## BANKED IDENTITY: what the pipeline reproduces before any new number is read

Before reading anything new the script must reproduce, in the same process, three banked facts:
`dim e₆ = 78` with 72 roots; the Bala–Carter centraliser dimensions
`dim z(e) = 46` for orbit `2A1` and `dim z(e) = 36` for orbit `A2`; and the inner real-form
census of `frontier/B907_real_form_selector/` — the 64 sign characters giving fixed dimensions
`{78×1, 46×27, 38×36}` and nothing else. `frontier/B8071_reality_gate/reality_gate.py` already
reproduces the last of these; if it does not reproduce here, the run stops.

## PRIOR ART: the bank grep run at design time

`grep -rn "rank obstruction\|rank-preserving\|maximal torus" docs/GUT_REQUIREMENTS_LEDGER.md
frontier/B952_gut_ledger_rank/` and a read of `docs/GUT_REQUIREMENTS_LEDGER.md` §D and
`frontier/B952_gut_ledger_rank/FINDINGS.md`. Established before designing:

- §D states the obstruction as **"a theorem, not an estimate"**: *"the centralizer of a set of
  **semisimple** elements contains a maximal torus, hence has full rank … therefore every
  measurement in the cascade is rank-preserving, and no number of them can ever reach rank 4."*
- B952's own scope line: *"Does NOT say the object cannot reach the SM, only that **measurement
  alone** cannot."*
- §D itself names the remedy: *"a Higgs VEV, a Wilson line / Hosotani flux, or an orbifold
  projection — i.e. requirement #11."*
- No arc in the bank tests the **word "semisimple"** in that hypothesis.

## The question

Two parts, both decidable:

1. **Is the hypothesis load-bearing?** For `x` a nonzero nilpotent, can `Z_G(x)` contain a maximal
   torus? (If a maximal torus `T ⊆ Z_G(x)` then `x ∈ z_g(T)` = a Cartan subalgebra, which contains
   no nonzero nilpotent. So `rank ≤ 5` for every nonzero nilpotent — to be **verified
   computationally**, not merely asserted.)
2. **Which nilpotent orbits reach rank 4, and is the 27 still complex on them?** Decided over all
   64 standard Levi subalgebras of `e₆` — an exhaustive finite check, no sampling.

## Declared outcomes — all live

| result | reading |
|---|---|
| rank 4 occurs for some nilpotent orbit **with the 27 complex** | §D's bar is **too narrow as stated**: it covers centralisers of semisimple elements and the nilpotent class escapes it. A **scope note** on §D, not a refutation — §D is true as written. |
| rank 4 occurs only with the 27 **self-dual** | rank is bought with chirality; that trade is the finding. |
| no nilpotent centraliser reaches rank 4 | §D's conclusion holds beyond its stated hypothesis and gets a strengthened statement. |

## Controls — run before the result is read

1. **Bala–Carter agreement**: representatives must give `dim z(e) = 46` (`2A1`) and `36` (`A2`),
   matching the published tables, and `ad(e)` must be **verified nilpotent**.
2. **The semisimple case must behave as §D says** — centralisers of semisimple elements must
   contain a maximal torus. If §D fails my own test, my test is wrong, not §D.
3. **Non-genericity**: the rank-4 outcome must **not** hold for all orbits. If every orbit gives
   rank 4 the instrument is measuring nothing.
4. **Self-duality is computed from the weight multiset** (`wt(M*) = −wt(M)`), not inferred from a
   name.

## Scope stated in advance

Over **ℂ** (exact ℚ arithmetic in the Chevalley basis). Which real forms the orbits and their
centralisers admit is `frontier/B8071_reality_gate/`, not this arc.

**Not established here:** that the *object* reaches any particular orbit. The ω-covariant purity
reading that places it on `2A1` is mod-`p` work in `frontier/B8068_j2t_charge_field/` and is
**owed**, not claimed. This arc classifies which orbits exist and what their centralisers are.
