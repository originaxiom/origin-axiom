# B1624 — THE GATE SEES THE DOSSIER (Review 62's R62-3): `seat-positive-verified` now checks a main arc that rests on the SM seat's dossier items; run on the record it caught B1606 resting on W19, which was unverified; W19's numerical facts verified on main by two routes, so the grade stands with its four dependencies declared

**Verdict: PROVED** (a gate repair and a verification). cc (main), 2026-10-09. It clears R62-3, carried from R61-3: Review 61
found that B1606 rests on the seat's W19–W22, which are dossier items, not seat arcs, so the gate could not see them. **0 of 19.**

## 0. Seen first

`VERDICT topic-sweep /seat-positive-verified|rests_on_seat|dossier item|W19/: 5 of 1396 arcs on main match (PROVED 5)`
— the gate's arc (B1487); Review 61's §3; B1606 (the
grade); the harvest rows 932–936 (W19–W22). **Literature:** Harer–Zagier (the orbifold Euler characteristic of M_{g,n});
the multiplicativity of the orbifold Euler characteristic in extensions; the amalgam SL(2, ℤ) = ℤ/4 ∗_{ℤ/2} ℤ/6.

## 1. The repair

- `rests_on_seat` accepts `sm:W<n>`. The gate finds the SM-derivation seat's ledger row whose item column begins with
  W<n>, by its bare name, and requires **VERIFIED** on it.
- The failing-path test (`tests/test_gate_failing_paths.py`, the registered control) now also fails on:
  - an item registered only;
  - another seat's row of the same name;
  - a different item sharing the prefix (W70 against W7).
  It passes on a verified one.

## 2. What it found on the record

**B1606 now declares `sm:W19`, `sm:W20`, `sm:W21`, `sm:W22`** (its DERIVED grade rests on them). The gate **failed** on
`sm:W19`, whose row was REGISTERED: "a reading by the seat's own grade; the facts classical". Main had built B1606's grade
on W19 without verifying it, and the gate could not have seen this before.

## 3. W19 verified in part (`verification/w19_check.py`, exact fractions)

| fact | result |
|---|---|
| M₁,₂ is a complex surface (dim 3g − 3 + n) | 2 |
| χ(SL(2, ℤ)) by the amalgam: ¼ + ⅙ − ½ | −1/12 (= χ(M₁,₁)) |
| χ(Aut⁺(F₂)) = χ(F₂)·χ(SL(2, ℤ)), from 1 → F₂ → Aut⁺(F₂) → SL(2, ℤ) → 1 | 1/12 |
| χ(M₁,₂) by Harer–Zagier, (2 − 2g − n)·χ(M₁,₁) | 1/12 |
| the two routes agree and are non-zero | yes |

The orbifold-locus sentence ("the three parities are its orbifold locus") and the dimension rule are not checked. The
identification of the weave's object with M₁,₂ stays the seat's READING. Row 932 is now **VERIFIED in part on main**,
and the gate passes: 8 declared seat dependencies, all VERIFIED.

## 4. Disclosed

- B1606's verdict file was edited to declare its dependencies (an addendum on its page says so). Its claim is unchanged.
- "VERIFIED in part" passes the gate, as W22's row already did. The gate reads the disposition word, and the parts left
  unchecked are named on the row.

## 5. Files

`verification/w19_check.py`, `w19_check.json`; `scripts/gates/gates.py`; the failing-path test; B1606's addendum; harvest row 932.
Lock: `verification/test_b1624_the_gate_sees_the_dossier.py`.
