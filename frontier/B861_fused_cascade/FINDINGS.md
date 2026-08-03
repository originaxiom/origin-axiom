# B861 — the fused cascade: ONE principle, applied to ONE object, selects E₆ → SO(10)×U(1) → SU(5)×U(1) → SM uniquely at every step

cc banking seat, 2026-08-03, continuing the joint session. Mathematics scope; nothing to
`CLAIMS.md`; Gate 5 untouched. **Not preregistered** — exploratory; footing = the computation is
elementary rep arithmetic, run twice (a first draft was caught wrong by its own output, §3).

## 1. The principle

> **Maximal residual symmetry among REGISTERABLE options**, where *registerable* = the
> **generation** (the 27's matter content under the candidate subgroup) remains chiral as a
> multiset after the θ-odd abelian factors are stripped — B860's criterion, theorem-grade there
> (exhibited intertwiner on the failing side, Schur obstruction on the surviving side).

This **fuses** the handoff's two imports (Michel's principle + a deviation clause) into one rule,
and it dissolves the deviation clause entirely.

## 2. The result

| step | menu (dim, registerable) | winner |
|---|---|---|
| (E₆)₁ | SO(10)×U(1) (46, ✓) · SU(6)×SU(2) (38, ✓) · Sp(8) (36, **✗**) · SU(3)³ (24, ✓) | **SO(10)×U(1)**, unique |
| SO(10)₁ | SU(5)×U(1) (25, ✓) · Pati–Salam (21, ✓) | **SU(5)×U(1)**, unique |
| SU(5)₁ | SU(4)×U(1) (16, **✗**) · SM (12, ✓) | **SM**, unique |

> **E₆ → SO(10)×U(1) → SU(5)×U(1) → SM. Unique at every step.**
> The handoff's *"the world's chain deviates from the extremal path exactly once"* **dissolves**:
> under the fused principle the world's chain **is** the extremal registerable path. The
> "deviation" was an artifact of ranking a non-registerable option (SU(4)×U(1), whose generation
> collapses to vector-like — B860).

Where the principle actually bites: Sp(8) at step 1 (the 27 restricts to the traceless Λ²(8) of
C₄, self-dual — no chiral matter at all) and SU(4)×U(1) at step 3. Everywhere else it is silent
and the symmetry ranking decides. **The criterion can fail and can pass — non-vacuous by
construction, locked.**

## 3. A first draft was WRONG, and the arc's own run caught it

The first draft applied the multiset test to the **cosets** at step 1 — and returned
**SU(3)³ as the step-1 winner**, because 16 ⊕ 16̄ cancels as a multiset. **Every coset of the
adjoint is self-conjugate as a multiset — the test is VACUOUS there.** The draft had silently
switched criteria between steps (cosets at 1–2, the generation at 3).

The repair is the uniform object: **the generation** — the 27's matter content — which exists at
every level of the chain. Under it, 27 → {16, 10, 1} keeps the 16 unpaired (chiral ✓); Sp(8)'s
27 is self-dual (✗); and B860's step-3 verdicts carry over unchanged.

Also fixed in the same pass: a **rep-name collision** — the "6" of SU(4) (Λ²4, self-dual) vs the
"6" of SU(6) (complex) — named apart in the conjugation table before it could silently break the
arithmetic. And **B859's step-1 scope note**: its coset-based kill of SU(6)×SU(2) does not
transfer to the generation criterion (the generation is chiral there; the option dies by ranking,
not by the gate). The step-1 *winner* is unchanged either way.

## 4. Honest boundaries

- **SU(3)₉'s 27-branching under the level-9 special embedding is UNRESOLVED here** — flagged in
  the script. It cannot affect the winner (dim 8 < 46 under either verdict).
- **Menu completeness (P5) is still the imported spine.** A chain missing from the classification
  breaks uniqueness silently. This is now the cascade's single external dependency.
- **The registerability premise** is one definition away from banked machinery (B599 + B593 +
  B860's dichotomy), but that definition — "chirality-registering measurement = a B599 pairing
  datum" — is still owed.
- **No values.** Group selection only; nothing touches couplings, masses, generations, or scale.

## 5. Selection-cost ledger, final form of this session

| | handoff (2026-08-03, solo) | after B859–B861 |
|---|---|---|
| gates | conformality (h∨ error at step 2) | **chirality / registerability** (framework-native) |
| principle | Michel, per step | **one fused principle** |
| deviation | "exactly once, at the chiral step" | **dissolved** |
| step-3 cost | one trit | **zero** (the bit is decided) |
| imports | Michel + menus + deviation | **menus (P5) + one definition** |

## Carried forward

1. **The single owed definition**: formalize registering as a B599 pairing datum → the fused
   principle becomes banked machinery end to end.
2. **Gate P5** — now the only external spine.
3. **Resolve SU(3)₉'s 27-branching** (hygiene; cannot move the winner).

`tests/test_b861_fused_cascade.py`
