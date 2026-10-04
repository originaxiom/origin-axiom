# HANDOFF — the research program out of the riddle, with every claim's robustness
### chat1 seat, 2026-10-02/04. **No branch, no arc numbers, does not persist.**
### Purpose: let another seat RE-RUN each claim independently. Seal before reading our numbers.

--------------------------------------------------------------------------------
## 0. THE ARC OF THE REASONING (read this first; the worries are the payload)

1. The program has spent its life trying to **derive** the choices (chirality sign, generation
   count, values). Its own record — the Awareness Verdict, plenitude, every door probed — keeps
   proving the **object makes none of them.** We named the riddle: *the goal assumes the choices
   are derivable; the mathematics proves they are not.*
2. We reframed: not "derive the choice" but **"for each open choice, does CONSISTENCY fix it (as
   B1383 did for Pin+)? For survivors, how are they selected?"** — and ran it.
3. We then asked whether the program can make **predictions specific to m004**, found the
   **moduli barrier**, and probed whether it is airtight.

The single most important lesson, stated once: **every error tonight was one of four kinds**
(§4). Apply the four cures before trusting anything below, including our own results.

--------------------------------------------------------------------------------
## 1. TIER 1 — ROBUST (verified by independent routes or textbook)

| # | claim | how verified | script |
|---|---|---|---|
| 1 | **Generation window {3,4,5}** for an E6-27 world: CP floor N>=3 (Kobayashi-Maskawa, (N-1)(N-2)/2 phases) + asymptotic-freedom ceiling N<=5 (each 27 = 3 Dirac quark flavours incl. exotic D) | 27 colour content by **two routes** (SM count, trinification) agree; ceiling **only tightens** with extra coloured matter | v01 |
| 2 | **Chirality sign survives consistency**: all perturbative anomalies + Witten count are parity-odd, so both hands are anomaly-free | exact, ours vs mirror | v02 |
| 3 | **Parity rule**: a smooth bulk gives ind(V) != ind(Vbar) **only if dim = 2 mod 4** | Ahat degrees 0,4,8 / ch_k parity | v03 |
| 4 | **The frame-bundle scale-free ratio = index x sqrt3 L(2,chi_-3) / (128 pi^2)**; covolume = sqrt3 L/8; vol(m004)=12 x covolume | matches SnapPy **to 12 digits** | v04 |
| 5 | Frame bundle of a closed hyperbolic M is **M x S^3** topologically; for a rational homology sphere b(F)=(1,0,0,2,0,0,1); **only c3 is a rational Chern class; N_gen = int(c3)/2** (standard heterotic formula); 3 is topologically permitted | Kunneth + BSU(2) 3-connected | (in transcript) |
| 6 | Order-3 cusp holonomy on 2T reps is **forced by 2T's abelianisation Z3** (not a selection) | m004: mu order 3/6, lambda order 2, all 48 | (in transcript) |

**But note on #1 and #4 — GENERIC, not object-specific:** #1 holds for ANY E6 world; #4 is
**identical for m003 and m004** (twins share index 12) and scales with index across the class.
They carry the field Q(sqrt-3), not the object.

## 2. TIER 2 — COMPUTED BUT FRAGILE (re-run these first)

| # | claim | fragility | what it needs |
|---|---|---|---|
| 7 | **M_R ~ 1.3e10 GeV, M_U ~ 5.7e15 GeV** (unification through a parity-symmetric LR stage) | **one-loop, one implementation** | two-loop running, threshold corrections, an **independent code** (v06) |
| 8 | **tau_p ~ 6e34 yr** (proton lifetime) | **order-of-magnitude only**; tau ~ M_U^4; halve M_U -> excluded, double -> untestable | state as "10^34-10^36 yr", do not sharpen |
| 9 | **J fixes the frame bundle's shape** (only size is a modulus) | holds for **Ad(K)-invariant** Hermitian metrics only | check against the **actual** metrics of Otal-Ugarte-Villacampa (Nucl.Phys.B 920, 2017), not the abstract (v05) |

**Correction carried in #7:** for a *unified* LR world the W_R sits at ~1e10 GeV, **not at the
LHC.** LHC W_R searches (W_R > ~2-5 TeV) test a *different*, low-scale LR scenario.

## 3. TIER 3 — INTERPRETATION / READING (not computed; do not bank as results)

- **The moduli barrier is not airtight.** Our *reading*: "values are choices" is an **AXIOM**
  (link 18); the supporting theorem (line 1817: flat sl3 deformations are pure cusp data, no
  interior modulus) is **about FLAT structures**; physics needs **curvature** (#3, Chern-Weil,
  int c3 != 0), so the flat theorem does not reach physical values. *Needs a check that no
  framing puts physical values back in the flat sector.*
- **Chirality as a superselection bit**, selected by spontaneous breaking of an E6 left-right
  symmetry (trinification SU(3)_L x SU(3)_R; SO(10) D-parity), the hand a random fluctuation.
  Requires the world to be LR-symmetric in the UV — a hypothesis.
- **Minimality -> N = 3.** Extends the program's minimality principle (proved on geometric
  objects) to a physical count. A hypothesis, not a theorem.
- **"Structure permits, a choice selects."** A synthesis across doors, not a theorem. Note:
  we tested an over-unified version ("one principle kills all routes") and it FAILED — only 3
  of 8 routes died on unitarity/chi=0.

## 4. THE FOUR FAILURE MODES, AND THEIR CURES (apply to everything above)

| failure | cure | the instance that taught it |
|---|---|---|
| single implementation | **two implementations, no shared code** (SM lane: "NO NEGATIVE FROM A BUG") | most of tonight ran once |
| local fact -> general law | **base rate before significance** (B727, B1518) | frame-bundle ratio looked object-specific until m003 matched |
| paper read as record | **see the record first** (B1517) | the dynamics line was already xB032 |
| interpretation as result | **separate columns**: theorem / computed / cited / interpretation | §3 above |

## 5. RETRACTIONS — do not reuse these
- "a 4D curved bulk is the one open door" — **killed by the parity rule** (#3)
- "W_R is being tested at the LHC now" — **wrong for the unified case** (#7)
- "the Higgs selects chirality spontaneously" — **physics error**; SM parity violation is
  explicit (corrected by the physical-bridge seat's intake)
- "torsion in Gamma gives orbifold singularities in the frame bundle" — **wrong**: Gamma\G is
  smooth (left action is free); torsion makes the *base* an orbifold
- "the frame-bundle ratio singles out m004" — **generic**, m003 identical
- numerical bugs caught: torsion used as tau instead of sin(tau) (mod 2pi); a "phase transition"
  that was a divergent-regime (beta<2) truncation artifact; mpmath nsum on a periodic character
  (0.7725 vs true 0.78130); an unpadded Betti list

## 6. LITERATURE GAPS CLOSED (verified absent from the record and the paper)
Strominger system on compact SL(2,C)/Gamma (Biswas-Mukherjee CMP 2013; the 2014 **flat-gauge
no-go** contradicting it; Otal-Ugarte-Villacampa NPB 2017 **non-flat** invariant solutions) ·
rigidity of SL(2,C)/Gamma (algebraic dimension 0; Ghys homogeneity; Huckleberry-Margulis no
hypersurfaces; flat bundles have vanishing rational Chern classes) · the **Z3 heterotic orbifold**
on (C/O_3)^3 (27 = 3^3 fixed points from the ramified prime |1-omega|^2=3; chi=72; 36 generations
standard, 3 with Wilson lines) · Fu-Yau non-Kahler heterotic (generations vanish, chi=0) ·
left-right symmetric models and W_R bounds · the 3d-3d correspondence (DGG) · the tetrahedral census.

## 7. THE ONE THREAD WORTH CONTINUING — done robustly from the start
**L(2,chi_-3) in a physical partition function.** The **volume conjecture is PROVED for the
figure-eight** (coloured Jones grows like exp(N vol / 2 pi)), and vol(m004) = 12 x sqrt3 L/8, so
L(2,chi_-3) genuinely sits in the asymptotics of a quantum Chern-Simons partition function of
the object. The review lane already computed the 3D index (S23).
**Question:** does L(2,chi_-3) control the 3D index's asymptotics as it controls the coloured
Jones? **Fence, up front:** every hyperbolic knot's volume controls its own growth, so the
*mechanism* is generic; the *value* is shared across the class. A robust connection to physics
at the resolution of the field — honest, and more than the night began with.
**Protocol for it:** pre-register the predicted asymptotic constant; compute against published
3D-index series with two independent implementations; report the base rate (does every member of
the class give its own index-multiple?) before any significance.
