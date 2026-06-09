# B146 — B145 scrutiny calibration: tighten the conclusion + the preferred-handedness dichotomy

A scrutiny pass found B145 sound but over-scoped. MATH tier; K-A stays dead.

**Part A (verified corrections):** the axioms *permit* chirality (`RRL/RLL` det-1 Pisot chiral); "no single
**canonical** object is chiral" (not "chirality can't be forced"); the **two-mechanism** statement (chirality is
forced+generic but always self-mirror singles or mirror-paired composites ⟹ never preferred); symmetric-monodromy ⟹
amphichiral is **sufficient, not necessary** (`RRLLRL`).

**A5 (the catch):** B145's arithmeticity arm is **refuted as stated** — it used the *non-invariant* trace field; with
the **invariant** trace field, `RRL/RLL = ℚ(√−7)` are **chiral** imaginary-quadratic, so "no arithmetic chiral o-p-t
bundle" does not stand. The surviving canonical⟹self-mirror rests on the near-tautological volume/palindromic arms.

**B1 (the dichotomy):** `M` and `M̄` agree on every orientation-*independent* invariant (vol/`H₁`/trace field; CS
flips), so **no canonical selection can prefer a handedness**. This derives the asymmetry: κ-fork genuine (κ
orientation-independent), chirality-fork convention (handedness orientation-sensitive).

**B2 (open → B147):** is `RRL` (ℚ(√−7)) **fully arithmetic** (needs integral traces, Maclachlan–Reid)? If yes, "no
arithmetic chiral o-p-t bundle" is false.

```
python -m pytest tests/test_b146_b145_calibration.py -q
~/.local/bin/sage-python frontier/B146_b145_calibration/probe.py
```

**Tier.** MATH. Rewrites `K017`; syncs synthesis/OPEN_LEADS; extends the public-surface guard (no per-chat AI labels in
living docs; backlog flagged). Nothing to `CLAIMS.md`; P1–P16, B85, B124–B145 untouched. See `FINDINGS.md`; ledger **V135**.
