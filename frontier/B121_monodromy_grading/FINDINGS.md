# B121 — the monodromy sl(2) grading of the adjoint: an external `det=−1` `GL(2,ℤ)`-rep, not the principal one

**Phase 2 of the physics-bridge sweep (the structural lead).** The `(n²−1)`-dim trivial-point tower carries **two**
`SL(2)`-actions, and they are genuinely different. The *negative* — "tower ≠ Kostant principal-sl(2)" — was already
banked (B89-T/B98); this is the **positive** characterization and the precise obstruction. Standalone rep theory;
the Hitchin/Langlands *reading* is firewalled in `../../speculations/S024_monodromy_hitchin.md`. No physics here; no
`CLAIMS.md`; the `ρ_n`/Sym-`μ_d` proof stays the prize; P1–P16 untouched.

## The two SL(2)-actions on the same `(n²−1)`-dim adjoint

- **(A) INTERNAL — the principal `sl(2) ⊂ sl_n` (Kostant).** The defining `n`-dim rep restricted to the principal
  `SL(2)` is `Sym^{n−1}` (`det=+1`, lands in `SL(n)`), and the adjoint is `Sym^{n−1}⊗Sym^{n−1} ⊖ triv =
  ⊕_{i=1}^{n−1} Sym^{2i}` — **even** highest weights `{2,4,…,2n−2}` only. This is the **Hitchin / Fuchsian section**
  (B101: `V0` = the principal `V2` sector for `SL(3)`).
- **(B) EXTERNAL — the monodromy.** The figure-eight mapping class acts on the `SL(n)` trace ring via `N ∈ GL(2,ℤ)`;
  at the trivial point this linearizes (B103) to `ρ_n(N) = ⊕_d Sym^d(M_m)^{μ_d}` — the Sym two-sequence (B117), with
  **mixed-parity** highest weights (the two-sequence support).

| n | tower (monodromy) highest weights | Kostant (principal) | agree |
|---|---|---|---|
| 2 | `{2}` | `{2}` | **yes** |
| 3 | `{0,2,3}` | `{2,4}` | no (odd `3`) |
| 4 | `{0,1,2,3,4}` | `{2,4,6}` | no (odd `1,3`) |
| 5 | `{0,1,2,2,3,4,5}` | `{2,4,6,8}` | no |

Both have dimension `n²−1`; they **agree only at `n=2`**.

## The obstruction is `det(M_m) = −1` (the positive content)

The tower has **odd** `SL(2)` highest weights for all `n≥3`, while Kostant is **even-only** — so the two reps are
**inequivalent for `n≥3`**, and (the **kill condition for this fork**) it is **not** a mere dimension coincidence.
The odd weights are the signature of `det(M_m) = −1`:
- the principal embedding uses the `det=+1` rep `Sym^{n−1}`;
- the monodromy uses the **seed `M_m` directly**, which sits in `GL(2,ℤ) ∖ SL(2,ℤ)` (`det=−1`).

Concretely, `Sym^d(M_m)` has eigenvalues `(−1)^j φ^{d−2j}` and
```
   det Sym^d(M_m) = (−1)^{d(d+1)/2}   (= −,−,+,+,−,−,… for d=1,2,3,4,5,6),
```
a sign in **every** block — whereas a `det=+1` partner gives all `+1`. The odd-highest-weight blocks are exactly the
`char(−M^h)` sectors (B112), and this is the same `det=−1` parity that produces B118's fixed-root sign `(−1)^{h+1}`
and the inversion identity `char(M^{−h})=char(−M^h)`.

## The relation (and what it is not)

> **INTERNAL principal `sl(2)` (Kostant, even, `det=+1` — the Hitchin/Fuchsian section)** and **EXTERNAL monodromy
> `GL(2,ℤ)` (the tower, mixed parity, `det=−1` — the mapping class group)** are two inequivalent `SL(2)`-actions on
> the **same** `(n²−1)`-dim adjoint, distinguished for all `n≥3` by the **`det=−1` parity obstruction** (the odd
> `Sym^d`). So "tower ≠ Kostant" is now characterized **positively**: the monodromy is the `det=−1` external action.

This connects the trace-map tower to the Hitchin picture without crossing the firewall: the principal side is the
Fuchsian/Hitchin section (B101), the monodromy side is the mapping-class-group action, and the gap between them is
exactly the `det=−1` parity that the whole program already singled out (B93/B94/B118). The geometric-Langlands /
class-S *reading* is in `S024` (firewalled).

**Ledger:** V109. **Reuses:** `B103.two_sequence_mult`. **Anchors:** B89-T/B98 (the negative), B101 (the principal =
Hitchin/Fuchsian), B112/B118 (the `det=−1` sign structure), B117 (the two-sequence).
