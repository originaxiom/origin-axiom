# B139 — "SM through multiplicity": firewall cartography (NOT a crossing) (V128)

Three Chat-2 informatory calculations decomposing *"can interaction/multiplicity produce the Standard Model?"*,
banked as **cartography of the firewall** — a sharper statement + one guard + one open probe. **Firewall-CONFIRMING,
not a result, not a physics crossing.** MATH tier; nothing to `CLAIMS.md`; P1–P16, B85, S031, merged B124–B138
untouched. The only physics that continues is the emergent K010 / κ=2 / Lee–Yang, firewalled.

## The decomposition (the organizing content)

| SM requirement | can multiplicity deliver it? | basis |
|---|---|---|
| multiple gauge couplings | **PARTIAL** (yes in principle) | coupling count = cusp count (3d-3d); an n-cusped object has n `U(1)`s |
| simple non-abelian factor | **BLOCKED** unless Gate-1 opens | each cusp → `U(1)` (Mostow); `SU(2)` needs cusp-swap = Weyl reflection (`S033`, prior LOW) |
| irreducible chirality | **STRUCTURALLY BLOCKED** (all computed invariants) | mirror = R↔L relabel → same trace/charpoly/Perron-field/volume; only CS-sign flips |
| discrete vacuum selection | **PARTIAL** | B131 trace-fork exists, gluing-driven, trace-level |

**The clean firewall statement (cartography).** *Multiplicity permits MORE structure (more abelian couplings, a
discrete trace-fork, chiral objects) but cannot permit the TWO structures distinguishing the SM from a generic
emergent gauge theory — a simple non-abelian factor (contingently; Gate-1/`S033`) and irreducible chirality
(structurally).* Banked as a framing note in `speculations/S029`, not a new result row.

## Item 1 — the chirality articulation (VERIFIED) + the load-bearing caveat

The SM-side view of P009's `det = −1 → CS = 0`: for any metallic-block word the mirror (`swap_{R↔L} ∘ reverse`) is a
relabeling preserving the trace ⟹ same char poly ⟹ same Perron field ⟹ same volume; **only CS flips sign**. The
bundle and its mirror are the **same geometry with opposite CS** (a symmetric pair). The SM's chirality-without-a-
mirror-partner (parity violation) is structurally absent — the mirror **distributes over the word**.

**Verified (`probe.py`):** for the six chiral words `RRL, RRRL, RRLRL, RRRLL, RRLLRL, RRRLRL`, the mirror monodromy
equals `Mᵀ` (so `tr` equal, same Perron discriminant `tr²−4`) — and the equality is **universal** (achiral words
too: `RL, RRLL, RLRRLL, RRRLLL`). SnapPy control: volume mirror-invariant, **CS flips sign**, `H₁` mirror-invariant
for all six. The clean reason: `R = [[1,1],[0,1]]`, `L = Rᵀ` ⟹ mirror sends `M → Mᵀ` ⟹ `tr(Mᵀ) = tr(M)` exactly.

> **THE LOAD-BEARING CAVEAT (rides with the banking).** "Structurally blocked" = **blocked at every invariant
> computed (trace, char poly, Perron field, volume, CS)** — NOT a proof that no invariant distinguishes a chiral
> bundle from its mirror. Banked claim: **"chirality is a CS-sign, not an inequivalence, across all standard
> invariants."** *Not* "chirality is impossible." (Annotated in `../../philosophy/P009`.)

## Item 2 — method guard MB9 (group-level ≠ gauge-level)

A non-abelian symmetry **group** is not non-abelian **gauge** content: the firewall is on the trace-ring / `T[M]` /
fixed-locus (abelian × discrete), not the monodromy group (non-abelian for any hyperbolic object). Generating a free
SL(2,ℤ) subgroup is generic and firewall-neutral. Banked in `../../REPRODUCIBILITY.md` as **MB9** (the handoff's
"MB8" number was taken by the CHAT-1 §E guard). Cluster: MB6 / MB8 / MB9 = the "right object, wrong level" family.

## Item 3 — open lead: does the chirality block survive the genus ladder?

Item 1's block rests on the mirror being a simple R↔L relabeling preserving the trace — **special to genus-1**
(SL(2,ℤ), two generators). At genus ≥ 2 the MCG is richer, the mirror may not be a relabeling, and B131 shows the
free invariant discretizes on the genus ladder — so genus ≥ 2 is the one place the chirality firewall might gap.
MATH, trace-level first pass (no Sage), the **falsifier for Item 1**. Even a break gives **emergent** chirality, not
the SM's fundamental chirality. Registered in `../../docs/OPEN_LEADS.md` (tag **B139-G**); unrun.

## Reproduce

```
python frontier/B139_firewall_cartography/probe.py
python -m pytest tests/test_b139_firewall_cartography.py -q
```

The trace-level facts run unconditionally (pure sympy); the CS-flip control is SnapPy-gated (skips cleanly).

**Tier.** MATH (cartography). Annotates `../../philosophy/P009` (SM-side articulation + caveat), `speculations/S029`
(the framing note), `../../REPRODUCIBILITY.md` (MB9), `../../docs/OPEN_LEADS.md` (B139-G). Nothing to `CLAIMS.md`;
P1–P16, B85, S031, B124–B138 untouched. Ledger **V128**.

**Anchors:** `../../philosophy/P009` (det=−1→CS=0 / monadic closure), B128/`K011` (the chirality recursion, the Z₂
mirror), B131/`S032`-B (the trace-fork; the genus-ladder discretization), `S029` (the abelian-wall firewall
program), `S033` (Gate-1). External: Mostow rigidity; SnapPy `complex_volume` / `symmetry_group`.
