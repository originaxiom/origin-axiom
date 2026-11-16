# Erratum Note `AGY-002_CLOSURE-G6-ERRATUM` (`0 of 19`)

In `e751f2f9d` (`relays/agy002_closure_g6/verify_closure_g6_out.json`), Sections `0`, `2`, and `3` (`all 243 histories`) and all `5 of 5` planted fault controls passed (`100%`), while the `Section 1` seesaw `Haar` check contracted `Y_e` and `Y_nu` with the Bergman reproducing vector `v_0(tau) = psi^{(6)}(0; tau, 0)`, which produces a **rank-`1` outer product** (`2D` nullspace rotating freely under `U(3)`, caught immediately by `Guardrail 3`), and squared the condition number via `kap @ kap^dag`.

Preserving `c41a7f346..e751f2f9d` untouched under `seal-immutable`, `relays/agy002_closure_g6_fixed/verify_closure_g6_fixed.py` contracts `Y_e` and `Y_nu` with the full-rank covariant vector `v_1(tau) = G_6(tau) v_0(tau)` and extracts `Takagi` singular vectors via direct `SVD`. `0 of 19.`
