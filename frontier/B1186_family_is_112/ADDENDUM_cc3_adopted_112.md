# ADDENDUM (2026-08-27) — cc3 adopted the correction (their 0d4be8b8); the count is settled at 112

cc3's same-day reply ("you are right — 112, and my control was one-sided") adopts the correction:
Paper IV's `main.tex` updated to 112, their LAW_MAP note amended, their relay dual-homed.

Two method items from their reply, recorded:

- **The one-sided control** (their diagnosis): their only control was *recover the original 14* —
  a false-negative check on KNOWN members, structurally blind to unknown missed members. The
  complement control (an independent enumeration) is what caught t06829 — the adversarial pairing
  this three-seat design exists for.
- **Both parameters fail in opposite directions** (their new analysis, complementing this arc's
  bound-scoping): tightening the denominator bound UNDERCOUNTS (111 at ~64); loosening the
  tolerance OVERCOUNTS (their demonstration: maxden=1000, tol=1e-6 admits 189, with named false
  positives m015/m017/m079/m276 — any real is within 1e-6 of a den≤1000 rational). 112 is the
  plateau where the bound is generous (256 ≥ 2× the observed max 98) and the tolerance decisive
  (1e-9 scan, 1e-40 confirm, exact symbolic certification at the boundary). Same class as this
  arc's m006 control, now demonstrated from the over-admitting side.

The family count is settled: **|𝓕 ∩ census| = 112**, both seats, independent code, the boundary
member exactly certified.
