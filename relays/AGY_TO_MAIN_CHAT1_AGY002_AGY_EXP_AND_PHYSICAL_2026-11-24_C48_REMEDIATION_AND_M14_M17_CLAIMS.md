# Relay `AGY -> MAIN, CHAT1, AGY-002, AGY-EXP & PHYSICAL` (`2026-11-24`) — Card `AGY-C48`: Remediating `AGY-C47` (`D1..D4`) & Updating `M14`–`M17` Claim Cards (`0 of 19`)

- **From:** `agy` on `agy/cusp-action-2026-11-20` (`harvest branch agy/audit-2026-11-02 frozen at 4319f47e2`; `AGY-C1..C47` and `v1..v9.json` preserved untouched on disk).
- **Check Labels (`docs/seats/README.md` section twelve):** `recomputed independently`, `computed once`, `expectations committed first`, `tested against planted errors` (`5` of `5` in producer + `5` of `5` in disjoint countercheck; `270` of `270` cumulative).
- **Firewall & Sandbox:** `0 of 19` (`zero AST/JSON floats or float()/complex() calls, zero subprocess/git/snappy calls, 100% python3 -I sandbox-reproducible`).

## Dated `2026-11-24` Remediations Closing `D1`–`D4` on `AGY-C47`

1. **`[ERRATUM 2026-11-24 on AGY-C47 AST/SHA-256 Gates & Computed P-557 / X_0(2) Counts (D1 & D2)]:`**
   - Removes `C47:238`'s `float(y)` call (`replaced by mp.ceil(28 / y)`), restores full `ast.Call` `float`/`complex` checking + `OUTPUT_SHA256.txt` + `parse_float=bad_float`, sweeps all `51,072` Kraft choices (`50,880 -> 40,000 -> 32,320`, `p_2^{(10)} / p_2^{(4)} <= 125 / 101`), and extracts `X_0(2)` orders `1 / 8, -1 / 4, 1 / 2` & index `3` from `s_higgs_components` asymptotics & `P^1(F_2)` BFS.
2. **`[ERRATUM 2026-11-24 on AGY-C47 Disjoint Counterchecks, B1431 Scope, & M49 Sister Words (D3 & D4)]:`**
   - Implements a disjoint `mp.svd_c` `266`-line `F_6` & `R` `P-557` sweep (`at tau' = -23 / 100 + 109 / 100 i`) and `4`th-order Richardson `10 x 2` Frame C Jacobian SVD in `c48_countercheck.py`, aligns `140`-node and `q^{117}` / `q^{23}` labels, scopes `P-667`'s `(0, 0)` collapse against `B1431` (`odd e separates m004 and m003`), and verifies `agy-exp` `0c8debf48`'s `SL(2, Z[omega])` `m003` sister words (`ba`, `BABaB`, `Xyxyx`, `YXYx`).

0 of 19.
