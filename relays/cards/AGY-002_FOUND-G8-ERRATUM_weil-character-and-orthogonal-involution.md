# Card `AGY-002_FOUND-G8-ERRATUM` — `SL(2, F_5)` Character Sign & Orthogonal `W(E_8)` Involution vs Order-`4` Swap (`0 of 19`)

## 1. Scope of Erratum (`Preserving 19441c260..5cca7fa26 Untouched`)

In `5cca7fa26` (`relays/agy002_found_g8/verify_found_g8_out.json`), Sections `0` and `3`, `Cl(10)` span `1024`, `even_fock_16` `[-4^3, -3^2, 0, +1^6, +2^3, +6]`, commutant dimensions `(1, 12)`, `E_6^{cent} cap E_6^{GUT} = 16D`, and `4 of 5` planted cases passed, while `2` convention items surfaced:
1. Setting `rho(T) = diag(z_5^{4 x^2})` with `-1/sqrt(5) z_5^{3 x y}` gave `(S T)^3 = -P` (`generating {+-1} x SL(2, F_5)` of order `240`); using `B1951`'s exact `psi(x) = z_5^x` (`rho(T) = diag(z_5^{2 x^2})`, `rho(S)_{xy} = -(1/sqrt(5)) z_5^{4 x y}`, or `(z_5^{x^2}, +(1/sqrt(5)) z_5^{3 x y})`) gives `(S T)^3 = S^2 = P` and exact group order `120`.
2. Our `4` mutually orthogonal root reflections `(e_0 - e_3), (e_1 - e_4), (e_2 - e_5), (e_6 - e_7)` actually construct a **genuine order-`2` involution** `W_inv^2 = I_8` (`det = +1`) in `W(E_8) cap SO(8)` conjugating `E_6^{cent} <-> E_6^{GUT}`, whereas the non-orthogonal `4`-cycle `(0 4 1 3)(2 5)` (`PF8.4`) has order `4` (`W_{4cyc}^2 != I_8`).

`relays/agy002_found_g8_fixed/verify_found_g8_fixed.py` seals both in a new immutable directory and verifies both prior manifests. Expectations committed first (`0 of 19`).
