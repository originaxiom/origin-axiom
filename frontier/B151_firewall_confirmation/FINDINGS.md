# B151 — firewall confirmation (L15): the firewall HOLDS — the unification is a symmetry identity and terminates at the wall (V140)

**The decisive boundary check, executed as a reading task.** L14 (B150) established that the unit's SL(2,ℤ) symmetry
**is** a known duality action (N=2\* / class-S) at the character-variety level — FORCED, primary-source-verified. That
bridge is **real**, which is exactly why the firewall must now be tested hardest: a real symmetry bridge makes a
scale-crossing feel more plausible than it is. L15 settles whether the unification extends past the firewall (to physical
magnitude) or terminates at it. MATH tier (physics-boundary), **firewalled**; nothing to `CLAIMS.md`; P1–P16, B85, the
merged B124–B150 untouched.

## The one question

In the 3d–3d correspondence applied to the figure-eight bundle (the unit, monodromy `RL`), does the complex volume /
Chern–Simons invariant enter the partition function **only as a dimensionless exponent** `~exp[(1/ℏ)·i·Vol_C]`, with
**all** dimensionful content carried by `ℏ↔k` (the level) and the squashing/lens-space radius — and **none** by the
invariant itself? **This is a fact about how the primary sources assign units, not a sandbox computation.**

## The anchor (the unit's actual numbers — computed, SnapPy, re-runnable)

- `complex_volume("4_1") = 2.0298832128 − 1.1e-15·i` ⟹ **Vol = 2.0298832128** (= 2·V_tet, the minimal cusped hyperbolic
  volume) and **CS = 0** (the figure-eight is amphichiral).
- `Vol+iCS ∈ ℂ/(π²ℤ)` (PSL₂; `ℂ/(4π²ℤ)` for SL₂) — a complex **number** mod a lattice, dimensionless (curvature ≡ −1,
  length ≡ 1): geometric "size", **not** physical scale (energy / mass / length).

**Pre-strengthening (banked).** The Chern–Simons part is the *candidate scale-carrier* — the orientation-sensitive, P-odd
piece tied to the chirality axis. For the figure-eight **CS = 0 identically**, so the unit's complex volume is **purely
the real hyperbolic volume**, with no CS content to carry anything across. The unit is the **least** likely object to
carry a scale. (Not a proof — the reading is what decides even the volume enters dimensionlessly — but a real observation
that the firewall is, if anything, stronger for this specific object.)

## The reading — where the units sit (all three primary sources)

| source | what carries the units | tag |
|---|---|---|
| **GTZ** (arXiv:1111.2828, Duke 2015) — `ĉ(ρ)=i(Vol+iCS) ∈ ℂ/4π²ℤ` via Neumann's extended Bloch group (Rogers dilog) | **(none)** — a dimensionless element of a quotient of ℂ by a lattice; geometric size in curvature units | **FIREWALL_HOLDS** |
| **Dimofte** (arXiv:1409.0857) — complex CS *at level k* via 3d–3d; state-integral; `T_n[M]` on squashed lens spaces `L(k,1)` | the **level k (↔ ℏ)** and the lens / squashing geometry — *not* the invariant; `Vol_C` is the fixed exponent saddle | **FIREWALL_HOLDS** |
| **Córdova–Jafferis** (arXiv:1305.2891) — "a squashing parameter in the geometry controls the imaginary part of the complex Chern–Simons level" | the **squashing parameter b** and the level — *not* the invariant | **FIREWALL_HOLDS** |

In every case the dimensionful/continuous content sits in `ℏ↔k` and the squashing/lens radius; the complex volume / CS
invariant enters **only** as a dimensionless element of `ℂ/4π²ℤ` in the exponent.

## The blade (binding)

A SYMMETRY identification is not a SCALE. The L14 bridge being real is the precise condition under which the firewall is
most tempting to over-read ("we found a true bridge, surely magnitude travels it"). It does not travel automatically. On
every claim: does a dimensionful quantity attach to the **invariant itself**, or only to `ℏ/k` and the radius? "The
partition function has units" is **not** a crossing — the units are in `ℏ/k`/radius. A crossing requires the **invariant**
to carry the scale; the reading exhibits the opposite in all three sources, and no apparent crossing was found. (Any
crossing claim would require — and this stage's discipline enforces — the exact primary-text location where a dimensionful
quantity attaches to the invariant.)

## Verdict — FIREWALL HOLDS, decisively

No κ-type or volume-type invariant of the unit can source a physical scale (energy density / mass / coupling). The
unification is **mathematical** — a SYMMETRY identity (L14) — and **terminates at the firewall**. A real bridge (L14) + a
confirmed wall (L15) is the strongest honest statement of where the one-object picture reaches: the cosmological-constant
question lies on the far side of a wall this structure does not cross. **This banks the firewall HOLDING — a real result,
the honest boundary of the physics aspiration, not a failure.**

## Reproduce

```
python -m pytest tests/test_b151_firewall_confirmation.py -q     # 5 passed (pyenv; SnapPy-gated live recompute)
python frontier/B151_firewall_confirmation/probe.py              # the anchor + the per-source reading + the verdict
```

The probe re-asserts the unit's anchor (figure-eight complex volume, via SnapPy when present) and encodes the per-source
reading; the test locks the anchor and the reading's *honesty structure* (every row tagged + cited; **no CROSSING without
exhibited primary text**; verdict FIREWALL_HOLDS). The test does **not** unit-test the papers' unit-assignment claims
themselves — cited prose is the honest boundary of a reading task.

**Tier.** MATH (physics-boundary, firewalled). Updates `docs/OPEN_LEADS.md` (L15 → CONFIRMED), `docs/STRATEGIC_SYNTHESIS.md`
§8 (L15 resolved). No `CLAIMS.md`. Ledger **V140**. **Anchors:** B150 (the L14 bridge this bounds), B148 (the unit), B141
(κ-fork / finiteness), `knowledge/K006` (the borrowed 3d-3d dictionary), `docs/STRATEGIC_SYNTHESIS.md` §8 (the dimensional
firewall). External: Garoufalidis–Thurston–Zickert arXiv:1111.2828; Dimofte arXiv:1409.0857; Córdova–Jafferis
arXiv:1305.2891.
