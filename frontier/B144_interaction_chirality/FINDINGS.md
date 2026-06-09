# B144 — chirality of cusp-glued interactions: the firewall extends structurally (MB12) + the redirect (V133)

Campaign 1 at the bottleneck (chirality), run with the **MB12** discipline (check a target for vacuity *before*
computing toward it). Applying MB12 collapses the naive "find a chirality crack" campaign and yields the real,
structural result. MATH tier; firewalled; nothing to `CLAIMS.md`; P1–P16, B85, the merged B124–B143 untouched.

## The MB12 vacuity chain (the targets that *look* like the wall but can never fail)

1. *"an **orientation-independent** invariant distinguishing M from M̄"* — **vacuous** (orientation-independent ⟹ equal
   on M, M̄ by definition). [the synthesis's `notion (ii)`, withdrawn]
2. *"an **orientation-sensitive** invariant that does **more than flip sign/conjugate**"* — **also vacuous**:
   `CS(M̄)=−CS(M)`, `WRT(M̄)=WRT(M)*`, `η(M̄)=−η(M)` for **every** 3-manifold (functoriality under orientation
   reversal). No invariant value exceeds the predictable mirror action.
3. The only non-vacuous topological notion is **chiral = no orientation-reversing self-homeo** (`is_amphicheiral`
   False) — **generic, already achieved** by fiber-composites (B128). Not the wall.
4. *"**preferred** handedness (mirror not reachable in the family) vs **convention** (reachable)"* — **vacuous for
   seed-heterogeneous gluing** (the mirror-closure identity below).

## The structural result (what B144 banks)

**Mirror-closure identity (verified, GL(2,ℤ)).** For two amphichiral pieces glued along a torus by `φ ∈ GL(2,ℤ)`, the
mirror of the composite is
`M̄(m1,m2,φ) ≅⁺ M(m1,m2, h₂·φ·h₁⁻¹)`, where `h_i ∈ GL(2,ℤ)` (det −1) is the orientation-reversing peripheral action of
piece `i`'s amphichiral self-homeo. Since `h₂·φ·h₁⁻¹ ∈ GL(2,ℤ)` always (checked), **the mirror is just another
composite of the same pieces ⟹ the family is mirror-closed ⟹ no preferred handedness can arise.**

So the firewall — *no preferred handedness* — **extends to cusp-glued interactions, structurally**, because the
construction's `R↔L` mirror is a symmetry at **every** level: single seed (CS=0), B128 fiber-composite, and now
cusp-composite. **Seed-heterogeneity injects contingency (B131's discrete κ-fork) but not chirality-breaking — they are
different axes.** Premise verified: both metallic pieces `b++RL`, `b++RRLL` are amphichiral (SnapPy `is_amphicheiral`,
both True), so an orientation-reversing `h_i` exists and the identity applies; and **chiral-(i) composites are generic**
(for generic `φ`, `φ ≠ h₂φh₁⁻¹`, so `M ≇⁺ M̄`) — chiral JSJ composites *exist*, extending B128 to the new category, but
their mirror is always in the family (no preferred side).

## The one-instance gate (a verify-don't-trust) — honest obstruction

Attempting the explicit closed composite in Regina: each piece truncates (`idealToFinite`) to a single boundary torus
(constructible), but **identifying the two boundary tori by a specified `φ` is not a single Regina call** (the boundary
triangulations must be matched, and the closed result is non-hyperbolic) — **explicit closed-composite certification is
not in-session-tractable.** Per the plan's contingency, the **structural argument** (mirror-closure from per-piece
amphichirality + JSJ canonicality) is the load-bearing result and stands without the build. *(No surprise — the gate
did not reveal a mirror-closure failure; it revealed a tooling limit. If a future build shows `reflect(M)` not iso to
the predicted mirrored-gluing composite, that would be the crack — to be re-verified, not banked as a crossing.)*

## The redirect (POSTULATED — the genuinely new direction)

Preferred handedness — what the SM's parity violation needs — requires **breaking the construction's `R↔L` mirror
symmetry**, which seed-heterogeneity does **not** do (it only permutes the family). The new lead is therefore a
**chirally-asymmetric input**: a substitution / interaction *not fixed by swap+reverse*. That is the only place
preferred handedness could live; more seeds will not produce it. (Registered in `../../docs/OPEN_LEADS.md`.)

## Reproduce

```
python -m pytest tests/test_b144_interaction_chirality.py -q          # 3 passed, 1 skipped (regina, runs under sage)
~/.local/bin/sage-python frontier/B144_interaction_chirality/probe.py
```

The GL(2,ℤ) mirror-closure identity + the chiral-(i)-generic demo run unconditionally; the amphichirality premise is
SnapPy-gated (records B128 values if absent); the Regina build is gated and reports the obstruction.

**Tier.** MATH. New guard **MB12** (`../../REPRODUCIBILITY.md`); fixes the (i)/(ii) section of
`../../docs/STRATEGIC_SYNTHESIS.md`; updates `../../speculations/S032` and `../../docs/OPEN_LEADS.md`. Nothing to
`CLAIMS.md`; P1–P16, B85, B124–B143 untouched. Ledger **V133**.

**Anchors:** B143 (the venue verdict — algebraic venue mirror-blind), B131 (the κ-fork interaction; contingency axis),
B128/`K011` (chiral fiber-composites; the `R↔L` mirror symmetry), B139/B140 (the orientation-reversal facts that make
the invariant-based targets vacuous), `docs/STRATEGIC_SYNTHESIS.md`. External: JSJ decomposition (canonicality);
functoriality of CS/WRT/η under orientation reversal; Regina (truncation).
