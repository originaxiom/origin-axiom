# Card `AGY-002_FOUND-G9-ERRATUM-2` — Left-Multiplication in `sl2z_gauss_reduce` & `(+d/ds + M)` Operator Sign (`0 of 19`)

In `d76552c9a` (`relays/agy002_found_g9_fixed/verify_found_g9_fixed_out.json`), Section `2` (`SU(2)_L`-invariant `Strong-CP` `< 3 * (1/10)^15` at `|J_CKM| > 28/1000`), all `5 of 5` planted cases (`including main's exact P-864 9/10 i chord-lens error`), and `7 / 7` prior manifests passed, while `2` sign/order bugs surfaced:
1. `H_L = A^dag A` has `A = +d/ds + M_0 tanh(M_0 s)` (`so (+d/ds + M_0 tanh(M_0 s)) sech(M_0 s) == 0`, whereas `-d/ds` is `A^dag`).
2. Applying `S: z -> -1/z` to `z = (a t + b)/(c t + d)` maps `(a, b, c, d) -> (-c, -d, a, b)` (`left-multiplication by S`), whereas `(-b, a, -d, c)` right-multiplied on multi-letter `SL(2, Z)` words.

Preserving `d76552c9a` untouched under `artifact-hashes`, `relays/agy002_found_g9_v2/verify_found_g9_v2.py` seals both fixes and verifies all `9` prior manifests (`0 of 19`).
