# AGY-002 Erratum 4: Card A2-WG96 `B1610` Double-Tick Order-`3` vs Order-`6` Spin Lift (`0 of 19`)

- **Card:** `AGY-002 / A2-WG96` (`relays/cards/AGY-002_A2-WG96_ej5-mapping-class-family-modes-vs-weave-g96-triplet.md`)
- **Authoritative Producer Artifact (`untouched`):** `relays/a2_wg96_v3/verify_a2_wg96_v3.py` (`1fe409150` / `9d3ec76ec`, `all_gates_passed = true`)

---

## Clarification of `W1` Item `5` (`Card line 39`)

In `relays/cards/AGY-002_A2-WG96_ej5-mapping-class-family-modes-vs-weave-g96-triplet.md` line `39`, the Card prose paired the unique order-`3` lift `g^3 = +I_2` with spectrum `{1, \omega, \omega^2}` (`turns {0, 1/3, 2/3}`). Because each double tick `\rho^2` of the `4` `B1610` founding-torsor rules has **two** `SU(2)` spin lifts `\pm g \in 2\mathrm{O}` (`order 3` with `g^3 = +I_2`, and `order 6` with `g^3 = -I_2`), and the induced cohomology operator satisfies `M_2(-g) = -M_2(+g)`:

1. **Order-`3` lift (`g^3 = +I_2`):** `M_2^3 = -I_6`, so `M_2` preserves `H_Q`, `W:T`, and `W:\overline{T}` (`< (1/10)^12`) and acts on both `3D` subspaces with spectrum `{-1, -\omega, -\omega^2}` (`normalized phase turns {1/6, 1/2, 5/6}`, as computed and recorded across all `4` rules in Producer `v3` at `9d3ec76ec`).
2. **Order-`6` lift (`g^3 = -I_2`, `B1610`'s `order6_lift`):** `M_2^3 = +I_6`, so `M_2` preserves `H_Q`, `W:T`, and `W:\overline{T}` (`< (1/10)^12`) and acts on both `3D` subspaces with spectrum `{+1, \omega, \omega^2}` (`normalized phase turns {0, 1/3, 2/3}`).

## Cold-Room Referee Bar

The independent Cold-Room Referee must verify **both** lifts (`g^3 = +I_2 -> turns {1/6, 1/2, 5/6}` and `g^3 = -I_2 -> turns {0, 1/3, 2/3}`) across all `4` torsor rules `\sigma`, `C(\sigma)`, `\mathrm{rev}(\sigma)`, `C(\mathrm{rev}(\sigma))` to `< (1/10)^12`. `0 of 19.`
