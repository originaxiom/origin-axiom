# B559 — Black-hole probes: holographic entanglement + the figure-eight as a 3D-gravity saddle

Two computable black-hole questions, run on owner request (2026-07-13). Both are
**STRUCTURE facts** — the entanglement scaling of the object's chain, and the
hyperbolic geometry of the figure-eight — read through standard gravity
dictionaries. **Nothing here produces a physical scale or an SM claim; firewalled.**
Locks: `tests/test_b559_blackhole.py`.

## Probe 1 — does the object's chain carry black-hole (area-law) entropy?

**Prereg (before compute):** the Fibonacci chain has a singular-continuous
spectrum ⇒ predict CRITICAL scaling S ~ (c_eff/3)·log L with c_eff *below* the
clean chain's c=1; NOT area-law (that is the disorder control), NOT volume.

**Method.** Free fermions at half filling, correlation-matrix entanglement
entropy, N up to 1597; on-site Fibonacci potential ±½. Controls: clean periodic
(known c=1) and strong disorder (known area-law). One boundary point:
S=(c/6)log L; two: S=(c/3)log L. (`frontier/physics_probes/holo_arealaw.py`.)

**Result (prereg CONFIRMED).**
| chain | one-cut log-slope | ⇒ c_eff | verdict |
|---|---|---|---|
| periodic (control) | 0.161 | ≈0.97 | critical, c≈1 ✓ |
| **Fibonacci (object)** | **0.121** | **≈0.7–0.8 (fit-dependent)** | **critical (not area/volume)** |
| random (control) | 0.004 | ≈0 | area-law ✓ |

Two-cut slopes track ~2× the one-cut (0.271 vs 0.316 vs −0.06), the CFT/RT
signature. **Verdict (robust part):** the object's chain is **CRITICAL — log-law
entanglement, NOT area-law, NOT volume** (locked: `fib` log-slope > 0.08, random
disorder-averaged slope < 0.03, `fib` linear-slope ≈ 0). So it is **not** a
gapped/holographic *bulk*; if anything it is a candidate holographic *boundary*
(a 1D CFT). The **black-hole area-law signature is ABSENT.**

**Honest caveat (reconciles with seat-1's tight-binding Probe A).** The *precise*
effective central charge is **fit-dependent and NOT robustly locked**: a
6×one-cut-slope fit gives c_eff ≈ 0.7–0.8 over one L-window, but the tight-binding
entanglement **oscillates with L** (the known quasiperiodic effect), so whether
c_eff is strictly below the clean c=1 flips between L-windows. So we claim
"critical, not area-law" (robust) — **not** a sharp c_eff value. The sharp
c = 7/10 identification (tricritical Ising, B221) lives in the **anyon/fusion-path
chain**, not this tight-binding model; extracting a clean CFT here needs that
construction (the rung-1 fusion category — open). c_eff is also coupling-dependent
(this is V=½; cf. B447/B555 and the B559 c_eff-scan follow-on).

## Probe 2 — the figure-eight as a 3D-gravity saddle, vs BTZ

Dictionary (banked **B520**): a loxodromic element of trace x is a BTZ black hole
with entropy S = arccosh(x/2). For a closed geodesic of complex length λ,
x = 2cosh(λ/2) ⇒ S = arccosh(x/2) = λ/2 (Re = horizon/entropy, Im = rotation ⇒ a
*rotating* BTZ). Geometry from SnapPy (authoritative).

**Figure-eight facts.** Vol = 2.0298832128, **CS = 0** (amphichiral ⇒ the
gravitational action Vol + i·CS is **REAL**, no framing phase). Its closed
geodesics form a discrete "black-hole spectrum" with **Eisenstein-integer traces
in ℚ(√−3)** (Bianchi PSL(2,O₃)):

| Re λ | Im λ | trace x | Re(S)=Re(λ)/2 |
|---|---|---|---|
| 1.08707 | −1.72277 | 2−ω = (3−i√3)/2 | 0.5435 (systole) |
| 1.66289 | −2.39212 | 1−i√3 | 0.8314 |
| 1.72511 | −0.92184 | 3−ω = (5−i√3)/2 | 0.8626 |
| 2.17414 | −2.83765 | (1−3i√3)/2 | 1.0871 |

**Structural verdict.**
- **BTZ** = H³/⟨one loxodromic⟩ = solid torus: ONE geodesic (the horizon),
  *infinite* volume, action needs regularization, one complex trace (mass+i·spin).
- **Figure-eight** = H³/Γ, Γ non-abelian: *infinitely many* geodesics, **FINITE**
  action 2.0298832, CS=0. It is **not one black hole** — it is a complete
  finite-volume 3D-gravity *instanton* (a subleading saddle in the Maloney–Witten
  sum over geometries), carrying a whole discrete spectrum of rotating-BTZ-like
  geodesics.

**Two-ends note (firewalled, cf. B258).** The figure-eight's GEOMETRIC geodesics
live in **ℚ(√−3)** (Eisenstein), while the object's own "golden loxodromic" x=5
(B520, S=arccosh 2.5=1.5668) lives in **ℚ(√5)**. The banked BTZ entropy applies to
both, but they are the two ENDS of the two-ended unification — the hyperbolic
(ℚ(√−3)/E₆) end vs the golden (ℚ(√5)/E₈) end — not the same trace.

## One fact, three faces (HINT — firewalled)
CS = 0 for the figure-eight **is** its amphichirality — the SAME amphichirality
chat-1 invoked for Door 2 (mapping-torus involution) and the SAME CS = 0 that
kills dark energy (no scale/θ, L15). Amphichiral ⇒ real action ⇒ no gravitational
scale. Recorded as a rhyme, not a claim.
