# Phase B coverage (auto)

- arc packets landed: **64 / 131**; missing: [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]
- arc records digested: **770 / 1310** ({'main': 765, 'audit/b775-braver-questions': 5})
- log chunks landed: **11 / 11** ({'docs/progress/PROGRESS_2026-Q2.md': 2, 'PROGRESS_LOG.md': 7, 'docs/progress/REVIEWS.md': 2})
- test packets landed: **14 / 14**; test records: 1122 / 1122
- log consistency: {'NOT_IN_LOG': 246, 'DRIFT': 48, 'CONSISTENT': 461, 'CONTRADICTION': 12, 'CONSISTENT (as of the original 2026-08-09 banking; superseded in part by two same-day-batch 2026-09-01 addenda not yet reflected in the log)': 1, 'CONSISTENT for the surviving core claim (uniqueness at m=1); DRIFT for the E7/N=4 clause, which the log (and un-updated arc_verdict.json claim_one_line) still implicitly carries but which is now known false': 1, 'CONSISTENT for the fork-pricing core claim; DRIFT for the covering-direction detail, which the log (mirroring the arc) still states backwards': 1}
- belts: {'NONE': 316, 'RECOMPUTES': 245, 'RE-READS': 170, 'UNCLEAR': 39}
- test lock types: {'NOT_A_TEST': 7, 'RECOMPUTES': 763, 'COMPARES_TO_STORED': 326, 'TAUTOLOGICAL': 17, 'SKIPPED_OR_XFAIL': 2, 'SMOKE': 7}
