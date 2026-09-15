# CHIRALITY_REFRESH.md

## HEADLINE
Chirality after the all-seat refresh — 2026-09-09

## WHAT IT IS
A cross-seat documentary audit (custody refresh + source correction), not a new B arc or numerical proof.

## VERDICTS AND CLAIMS
- "There IS a conditional chiral construction on this branch" — sourced m202 model: R18 four/one, R19 three/zero away from exceptional locus, R20 nontrivial C3 orbit (RETAINED).
- "There is NOT yet a source-selected, globally anomaly-consistent physical three-generation theory" (OPEN).
- R19 charge trace: "Tr(u) = 48, Tr(u^3) = 48, Spin(10)^2-u = 6" — anomalies of the extra U1, not SM hypercharge (COMPUTED).
- R22: opposite-chirality spectator vectors emerge from the same scalar source R21's cancellation needs (OBSTRUCTION, scoped).
- R23: "cancels local defect anomalies for supported gauge variations, but Stokes retains the complete outer boundary" — net anomaly remains at boundary for constant gauge parameter (SCOPED NEGATIVE, "not a universal no-go").
- Main B1324: "66 chiral covers in its fixed 87-cover enumeration, including 54 multi-cusped ones whose index it leaves open" (RECEIVED, not re-certified here).
- B1355 curved candidate: "survives" but its "A-type-only conclusion is too broad" per Acharya–Witten §2.3 (CORRECTION to SM seat's B1355).
- "(E6 x U1)/Z3 is a candidate compatible with appropriately charged 27s, not a global form computed from this cone's charge lattice" (SCOPED).
- Verification-package report "reports its own seal pass; that is not an independent physics proof or a rerun of all its locks here" (CAVEAT).
- R23 test status: "24 new tests pass... expanded focused selection is 93 passed. The 43-file regression is 309 passed, 13 failed, 8 errors, with the SAME 21 old failed/error IDs as R22" (RECEIPTS).
- "All 288 then-indexed latest artifact digests match" (VERIFIED, integrity check).
- "Reporting gates remain 27 PASS / 3 FAIL on old attribution, vacuity and marker debts" (STATUS, unresolved debts).

## CORRECTIONS TO MAIN OR TO ITSELF
- To SM seat: "The SM relay at 1703c0d8 correctly registers R15--R22 but explains their distinction by saying that a source curves the connection. That is not this construction: F_A=0 and [A,phi]=0 on the smooth source complement."
- To SM's B1351: "B1351 section 2(ii) concludes from H*(T2;L)=0 that the index vanishes whatever the Morse partition. R23's exact solid-torus/disc restriction cone disproves that algebraic implication."
- To SM's B1355: "B1355's finite centralizer on H/2T obstructs that restricted substitution, not the entire hyperkahler-U1 family. Its A-type-only conclusion is too broad."
- To outside memo 189: identifies "an additional safety issue in main's selector runner: the timeout handler continues before restoration; snapshot restoration is not in a finally block. Thus its advertised non-mutation is not guaranteed on that path."
- Self-correction note (B1354 caveats reaffirmed, not retracted): "Its OWN caveats say that lower coefficients were specialized, all branches were not classified, no all-orders self-duality theorem was proved... Those caveats govern the stronger headline."

## ROADMAP ITEMS
N/A (not a status/roadmap doc, but §5 "Strategy that preserves the progress" lists forward directions):
- "stay on the sourced path and compute its actual GLOBAL mass-map and end response"
- "construct a physical end/relative sector or a massive-U1 mechanism in the SAME theory"
- "keep B1355 as a candidate and restore the general E7-to-E6 unfolding route it over-excluded"
- "Source selection, Spin(10)-to-SM breaking, a controlled neutral-sector 4D limit, common gravity and discriminating observables remain separate duties."

## CONFLICTS WITH MAIN
- Claim: "Main B1324 reports 66 chiral covers in its fixed 87-cover enumeration, including 54 multi-cusped ones." Checked: `git -C <repo> grep -n "66" -- frontier/B1324_arc_b_and_the_dictionary/FINDINGS.md` confirms "66 of the 87 covers of m004 to degree 10 are chiral." NONE (matches main exactly).
- Claim: main's selector-runner timeout handler skips restoration, not in a `finally` block. Direct inspection of `scripts/checks/instrument_freshness.py` lines 113–129 confirms: on `subprocess.TimeoutExpired` the code does `bad.append(...); continue` (line 118) before reaching `pathlib.Path(r).write_text(snapshot, ...)` (line 129) — restoration is indeed skipped on that path and is not wrapped in `finally`. NONE (claim corroborated, not contradicted).

## WHAT MAIN WOULD HAVE TO VERIFY
Independently rerun R18–R23's sourced-m202 computations and confirm the Tr(u)=48 anomaly traces; check Acharya–Witten §2.3/Witten (3.11)-(3.14) citations against B1355's actual claims; and patch `instrument_freshness.py`'s timeout path to restore the snapshot in a `finally` block (confirmed live bug, not yet contradicted or fixed in main at HEAD).
