# B140 — compute-session reconciliation: close B139-G, reframe S031, sharpen B138, record RᵐLᵐ + bundle fields (V129)

A Chat-2 compute session reconciled against the repo. Net effect **subtractive/clarifying** — close one open lead,
retract one (never-banked) over-claim, tighten two framings, record two facts. **No new frontier claim.** MATH tier;
firewalled; nothing to `CLAIMS.md`; P1–P16, B85, the merged B124–B139 untouched.

## Item 1 — B139-G CLOSED: the chirality firewall is genus-general

The lone open falsifier for B139 Item 1 (does the chirality block survive the genus ladder?) **closes**. The
load-bearing content is the **standard orientation-reversal theorem** (genus-independent): for an oriented hyperbolic
3-manifold `M`, the mirror `M̄` has **same volume, opposite Chern–Simons, conjugate-isomorphic trace field**
(orientation reversal conjugates the complex volume). The genus-1 `M → Mᵀ` relabeling (B139) is a *genus-1 mechanism*;
the **conclusion is general**.

**Verified in-sandbox:** genus-1 bundles `RRL, RRRL, RRLRL, RRRLL` and chiral knots `5_2, 6_1` — volume invariant, CS
opposite. **Soft spots (honest):** the chiral **genus-2** illustration (twister) and the trace-field computation both
need modules/Sage absent here — but the closure rests on the **theorem**, not the genus-2 numeric, so it is not a gate.
The earlier hedge ("genus ≥ 2 might be where chirality stops being a mere CS-sign") is **refuted by the theorem** — the
firewall is *stronger* than the genus-1 argument implied. The **residual** caveat is the general one: blocked at all
*standard* invariants, not a proof that no *cleverer* invariant distinguishes.

## Items 2–3 — reframe S031 (rigidity, rational φ-fixed) + sharpen B138 (φ vs φ²) — VERIFIED

**The crux (φ vs φ²).** The metallic incidence `N = [[m,1],[1,0]]` has **`det = −1`** (orientation-reversing) and
**`N² = RᵐLᵐ`** (verified m=1,2,3, `tr N² = m²+2`). So:
- the **single** map `φ_m` (det −1) has **isolated/discrete** fixed points — **S031's object**;
- its **square** `φ_m²` (det +1, `= RᵐLᵐ`) is the **bundle**, with a **positive-dimensional** fixed locus (B71's
  `V0/W1/W2` geometric character variety).

Verified on the SL(2) trace surface `(x,y,z)=(trA,trB,trAB)` (`φ_m` via the trace identities):
- **φ-fixed:** m=1 `{(0,0,0), (2,2,2)}`, m=2 `{(0,0,0), (2,2,2), (−2,−2,2)}`. The **unique irreducible** point is
  `(0,0,0)` (κ = −2 ≠ 2), **rational**; the others are reducible (κ = 2).
- **φ²-fixed:** a **positive-dimensional curve** (the geometric bundle variety).
- **SL(3):** the unique irreducible φ-fixed point is `Sym²(0,0,0)` with trace coordinates `(−1,−1,−1)`, commutator
  `3` — **rational** (even though the SL(2) rep realizing `(0,0,0)` is over ℚ(i)).

**The calibration (B129 stands).** "Sealed in `K_m` (= ℚ(√−3) at m=1)" is **true but loose**: `K_m` is the
**`φ²`-geometric-bundle** trace field. B129's exact "load-bearing leg" S1a computed the `Sym²` of the **geometric
figure-eight rep** (`trA = 2` unipotent, `ω ∈ ℚ(√−3)`) — that is the **`φ²`-bundle**, not the φ-fixed point. The
actual φ-fixed content is **ℚ** (a *tighter* seal, ℚ ⊂ ℚ(√−3)), so **B129's 0-escape conclusion (S1b) STANDS**; only
the framing tightens. This is a **φ-vs-φ² clarification + tightening**, not a refutation.

**The reframe.** S031's real content is **rigidity/uniqueness** of the principal fixed point, **not** field-sealing:
*the metallic trace map has a unique irreducible fixed point per rank — the rational principal `Sym^{n−1}` embedding —
and no exotic fixed points up the tower.* That reframes the open converse (B138's hard half) as a **rigidity problem**
(the `K003` Dickson/Chebyshev flavor) — cleaner than "why do points land in `K_m`."

**Retracted (never banked, lived only in a Chat-2 message):** "~35 non-principal φ-fixed points carry ℚ(√−3)" and
"the converse routes to Heusener–Muñoz–Porti." Both **wrong**: there are **no** non-principal irreducible φ-fixed
points (verified) — the converse is rigidity, **not** an HMP classification.

## Item 4 — record: the `RᵐLᵐ` identity

`[[m,1],[1,0]]² = RᵐLᵐ` (verified m=1,2,3), so the geometric (`φ²`) bundles **are** the `RᵐLᵐ` once-punctured-torus
bundles. The block sequence `(m,m)` is a cyclic palindrome ⟹ by **B134/K011** every metallic bundle is amphichiral
(figure-eight CS=0). Ties the metallic family directly to the B128/B134 chirality criterion.

## Item 5 — record (do NOT conflate with S031): the geometric-bundle trace fields

The **`φ²`-geometric** bundles have trace fields **m=1 → ℚ(√−3)**, **m=2 → ℚ(i)** (both imaginary quadratic — *why*
m=1,2 are the two arithmetic members), **m≥3 → higher-degree** — a **structural** fact (not a compute limit). Already
banked: m=1,2 (B125/B129); the m≥3 non-quadratic in S031. This is the **`φ²`-bundle** object, **distinct** from S031's
φ-fixed points — **not** S031 sealing. (In-sandbox `trace_field_gens` needs Sage; recorded from the prior banks.)

## Reproduce

```
python frontier/B140_compute_reconciliation/probe.py
python -m pytest tests/test_b140_compute_reconciliation.py -q
```

The sympy-exact items (incidence facts, φ/φ² loci, `Sym²(0,0,0)` rational) run unconditionally; the genus-1/knot
CS-flip is SnapPy-gated (skips cleanly); the genus-2 illustration (twister) and Item-5 trace fields need
modules/Sage absent here and are theorem-/prior-bank-backed.

**Tier.** MATH (cartography/reconciliation). Updates `docs/OPEN_LEADS.md` (B139-G → ANSWERED), `philosophy/P009` +
`speculations/S029` (genus ladder closed), `speculations/S031` (rigidity reframe + rational φ-fixed + φ-vs-φ² +
over-claim retracted), `frontier/B138` (the φ-vs-φ² mechanism), `knowledge/K011` (`RᵐLᵐ` identity), `knowledge/K010`
(bundle fields). Nothing to `CLAIMS.md`; P1–P16, B85, B124–B139 untouched. Ledger **V129**.

**Anchors:** B139 (Item 1, the chirality articulation), B138/`S031` (the φ-fixed object), B129/`K012` (the m=1
sealing — calibrated here), B71 (the `φ²` geometric components), B134/`K011` (the chirality recursion), `K003`/`K005`
(the principal Sym tower / the rigidity flavor), B125 (the m=2 field). External: orientation reversal conjugates the
complex volume (Neumann–Zagier / standard); Lawton (SL(3) trace coordinates).
