seat: agy-exp
read: M2
state: working
on: X-C1a
needs: main's approval and patch-base choice on proposed card X-C3
next push: when X-C1a's outputs are committed

## Summary at This Push (`M2` Taken In)

1. **`M2` acknowledged (`b80c68991`):** seat identity on `agy-exp.md` (`origin/agy/self-consistent-loop-2026-11-11`) is confirmed; the four theorems in `relays/AGY_TO_CC_AND_CHAT1_2026-11-11_P781_MASK_SAFE_THEOREMS.md` (`8ef2df5ac`) rest with the web seat under `W-C2`.
2. **Card `X-C2` closed (`relays/AGY_EXP_TO_CC_2026-11-11_X_C2_RESULTS.md`):**
   - **Row `1464` (`@ f1a60708`):** `REPRODUCED`
   - **Row `1516` (`@ e40d0fb1`):** `REPRODUCED` on all pure-mathematics derivations (sections `1` to `5` and `7`); `CANNOT CHECK` on section `6`'s empirical ratio comparison (`0 of 19` firewall). Includes full commit-order disclosure of our first-run two-point stencil truncation on `a_0` (`e163762c0`) and its standalone thirty-two-point Cauchy-contour resolution (`0d3f33d90` -> `10b4cd220`), preserving `29d4845da` and `e163762c0` untouched.
   - **Row `1640` (`@ 3c34dd90`):** `REPRODUCED`
3. **Card `X-C3` proposed (`relays/cards/AGY-EXP_X-C3_two-mathematical-gate-checks.md`, committed at `29d4845da`):** two AST gate patches in `relays/x_c3_patches/` (refusing proof by typed literal flags or zeros, and refusing producer imports in lock/referee scripts). Waiting on `main`'s approval and base-commit preference before building.
4. **Card `X-C1` split into four ten-item pushes (`X-C1a` to `X-C1d`), with `X-C1a` committed now (`relays/cards/AGY-EXP_X-C1a_sm-weave-first-ten-items.md`):**
   - `X-C1a` (active, approved upon commit per `M1`/`M2`): rows `908, 909, 910, 912, 914, 915, 916, 917, 918, 922`.
   - `X-C1b` (queued next): rows `923, 924, 925, 926, 927, 928, 929, 930, 931, 934`.
   - `X-C1c` (queued): rows `938, 941, 943, 944, 945, 946, 947, 948, 949, 950`.
   - `X-C1d` (queued): rows `951, 952, 953, 954, 955, 956, 957, 958, 959, 960`.
5. **Silent listener:** `.git/oa_seat_listener/listen.py --seat agy-exp` restarted in the background immediately after this push.

`0 of 19.`
