# B228 — the mechanism behind golden's SUSY-uniqueness: the ordinary/super coset coincidence at SU(2)₃

**Date:** 2026-06-26. **Status:** the L45 follow-on, answered cleanly **in-sandbox** (no Seifert-recipe literature
needed). B224 proved golden is the unique metallic mean whose chain is superconformal *by central-charge matching*;
this finds the **structural reason** — and it pins golden = `SU(2)₃`. Firewall: dimensionless CFT / coset
rep-theory; the SUSY is 2d superconformal, not a scale (`S040`). **Nothing to `CLAIMS.md`; P1–P16 untouched.**
Ledger **V231**.

## The mechanism

Two GKO coset constructions:

```
   ORDINARY  Virasoro minimal model  M(m,m+1)  =  (SU(2)_{m−2} × SU(2)₁) / SU(2)_{m−1}      [uses SU(2)₁]
   N=1 SUPER minimal model           SM(m')    =  (SU(2)_{m'−2} × SU(2)₂) / SU(2)_{m'}      [uses SU(2)₂]
```

A CFT is **both** an ordinary and a super minimal model iff these two cosets **coincide** (same numerator level
multiset + same denominator level):

```
   {m−2, 1} = {m'−2, 2}   and   m−1 = m'   ⇒   UNIQUE solution (m, m') = (4, 3) = the tricritical Ising,
   with denominator SU(2)₃ = the GOLDEN level.
```

The ordinary TCI coset `(SU(2)₂ × SU(2)₁)/SU(2)₃` and the super TCI coset `(SU(2)₁ × SU(2)₂)/SU(2)₃` are
**literally the same coset** (`SU(2)₂ × SU(2)₁ = SU(2)₁ × SU(2)₂`). So `SU(2)₃` (golden) is the **unique level**
where the ordinary (`SU(2)₁`-based) and super (`SU(2)₂`-based) coset constructions coincide.

## Why this deepens B224

B224 showed only `M(4,5)` (among unitary minimal models) has its central charge `7/10` in *both* the ordinary and
the N=1 superconformal series — a *numerical* coincidence. B228 gives the *structural* cause: the two coset
constructions are **the same coset** at `SU(2)₃`, and `(m,m')=(4,3)` is the **unique** algebraic solution of the
multiset/denominator condition. So golden's SUSY-uniqueness is not an accident of central charges — it is forced by
the coset combinatorics, and the distinguished object is precisely `SU(2)₃` (the golden/Fibonacci level).

## The metallic statement (answers the L45 follow-on)

The metallic chain `m` flows to `M(m²+3, m²+4)` (B224), GKO denominator `SU(2)_{m²+2}`. The ordinary/super
coincidence requires denominator `SU(2)₃`, i.e. `m²+2 = 3 ⇒ m = 1`. So **golden is the unique metallic chain whose
coset is also a super-minimal-model coset** — the in-sandbox answer to "is golden the unique metallic one that is
also a SUSY minimal model?" **Yes.** (This is the coset-level form of the Seifert-overlap question from L45/B227;
it does not need the SUSY-minimal-model Seifert recipe — the coset coincidence settles it.)

## Honest status / tiers
- the coset central charges (ordinary + super), and the uniqueness `(m,m')=(4,3)`: **`[exact]`** (exact rational;
  4 pytest locks).
- the super-coset `(SU(2)_{m'−2} × SU(2)₂)/SU(2)_{m'}`: the **standard super-GKO** (the `SU(2)₂` carries the
  `c=3/2` supercurrent); **`[cited]`**, verified in-sandbox by central-charge matching to the N=1 superconformal
  series.
- the "same coset" criterion (numerator multiset + denominator level): correct for `SU(2)` cosets (product
  commutes; same diagonal embedding). Novelty of the *framing* UNCHECKED (the GKO/super-GKO cosets are classical;
  the golden-uniqueness-as-coincidence is the contribution).

## Reproduction
- `python coset_coincidence.py` (pyenv) — the central charges, the unique coincidence, the metallic statement.
- `tests/test_b228_golden_susy_coset_mechanism.py` — 4 exact locks.

## Net
Golden = `SU(2)₃` is the **unique** level where the ordinary and N=1-super minimal-model coset constructions
coincide. This is the structural mechanism behind B224's golden-SUSY-uniqueness, and the clean in-sandbox answer to
the L45 follow-on: golden is the unique metallic chain that is also a SUSY minimal model. (`B224 → B227 → B228`;
firewalled reading `S040`; the explicit super-Seifert realization remains a literature follow-on, but the coset
coincidence already settles the uniqueness.)
