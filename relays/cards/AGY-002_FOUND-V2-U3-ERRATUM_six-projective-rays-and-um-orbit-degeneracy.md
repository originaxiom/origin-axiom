# Erratum to Card `AGY-002_FOUND-V2-U3` — `6` Projective Rays in `{U_M^k h_*}` & Exact `6`-Fold Orbit Degeneracy (`0 of 19`)

## 1. Status of Original Card & First Producer Commit

- Original Card commit `2a7447548` (`relays/cards/AGY-002_FOUND-V2-U3_p873-q1-coleman-weinberg-higgs-plane-stabilization-and-cim-nogo.md`) and first producer seal `53d240cbc` (`relays/agy002_found_v2_u3/verify_found_v2_u3.py`, `SCRIPT_SHA256.txt`) remain immutable in git history.
- `53d240cbc` halted on Section `1` assertion `len(rays) == 12` because $U_M v_\pm = e^{\pm i\pi/6} v_\pm$ gives $U_M^6|_E = -I_E$, so $U_M^6 h_* = -h_*$ lies on the **same** projective ray in $\mathbb{C}P^5$ as $h_*$.

## 2. Two Exact Clarifications Tested in Companion `v2` & Cold-Room Referee

1. **Clarification `1` (`Section 1` `U_M` Orbit Count):**
   - The cyclic orbit $\{U_M^k h_*\}_{k=0}^{11}$ contains **`12` distinct unit vectors** in $S^3 \subset E \subset \mathbb{C}^6$ (`k = 0..11`, returning to $+h_*$ only at $k = 12$ to `< (1/10)^50`) lying on **`6` distinct projective rays** in $\mathbb{C}P^1 \subset \mathbb{C}P^5$ (`relative phases exp(-i k pi / 3) for k = 0..5`). Companion `v2` and the cold-room referee must assert **both** `um_signed_vector_count == 12` and `um_projective_ray_count == 6`.
2. **Clarification `2` (`Section 2` Exact `6`-Fold `[U_M^k h_*]` Orbit Degeneracy):**
   - Because `V_box`, `V_CW`, and `V_det` are $U(1) \times \langle U_M \rangle$-invariant, all `6` projective rays $\phi_m = m \pi / 3$ (`indices {0, 4, 8, 12, 16, 20}`, i.e. `idx % 4 == 0` on the `24`-pt equal-magnitude circle) take identical values (`orbit spread < (1/10)^10`).
   - Thus minimizing along the `[h_*]` orbit requires `|V(h_*) - min_{circle} V| < (1/10)^10`, `circ_argmin_idx % 4 == 0`, strict separation `V_box(phi = pi/6) - V_box(h_*) > 1` (`half-step barrier between U_M orbit rays`), and at `y = 17/10` `|V_box(h_*) - min_{S^3, 216pt} V_box| < (1/10)^10` with `s3_box_argmin[0] == 4` (`theta = pi/2`) and `s3_box_argmin[1] % 4 == 0`.

## 3. Firewall

Strict `0 of 19`; `v1` (`53d240cbc`) remains unmodified; all rational bars in Sections `0`, `1` (`aside from Clarification 1`), `2` (`with Clarification 2`), `3`, and `4` (`PFU3-1..PFU3-5`) remain unchanged.
