# B1177 addendum — the measurements landed (2026-08-27, same sitting; completed by B1178)

**The per-file collection sweep (1063 files):** TWO files carried the whole cost — 
`test_b371_two_state_sector.py` **156.95 s** (a module-level `REPORT = run()` executing ~157 s of exact
computation at import) and `test_cc2_r5_adopted.py` **36.05 s** (a 300-line module-level lock script);
everything else ≤ 7.7 s (mostly the ~4.3 s interpreter+conftest baseline). Full table committed
(`collect_per_file.txt`). **⇒ L184's execution was surgical, not structural — see B1178** (178.41 s →
15.14 s full-suite collection, 12×, outcomes preserved 5/5).

**The OA_SLOW first-ever run:** launched this sitting (50 gated files, fixed invocation); the slow halves
are genuinely long-running — the run continues past this bank; **last-green lands in the log + the next
touch records it here.** (Honest state: launched, not yet complete — no phantom green.)
