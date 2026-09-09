# Addendum (2026-09-02) — A03 verified; D11 seat-reported (B1235)

**A03 (verified):** `.gitignore:20–21` ignores `*.log` and `*.out` repo-wide. `verification/reproduce.log` and
`verification/our_uniqueness_chain.out` — this arc's named witnesses — are therefore untracked on every clone
(`git check-ignore` confirms). The fix is a committable extension, not an unignore.

**D11 (NOT re-verified here):** fab5cloud reports the arc's 6615 → 4 → 1 mixes conventions and the full tensor gives
6615 → 9 → 1. Their certs live on the `outside-bench` seat branch only. Recorded as a seat claim awaiting a bench
run on main; nothing in this arc is re-typed on it.
