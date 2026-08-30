# B1156 — SEAM-A Gate 2: the a-priori MISMATCH is **REFUTED**; the seam is a genuine **FLOOR** with a named archimedean door

**Status: banked (frontier). Verdict OPEN (seam **INDETERMINATE/FLOOR** per the sealed grammar,
`frontier/B1146_seam_b/THREE_SEAMS_PREREG.md` sha e699ebc79c06a823).** This arc **sharpens B1155**:
it removes B1155's "leaning MISMATCH" and replaces it with a precise specialist floor. The archimedean
anchor is re-verified own-computation (`verification/reproduce.sh` → `REPRODUCES`); the refutation of
the a-priori MISMATCH echoes a banked arc (B1108, re-verified this session), not a fresh assertion.
Codex-side data are off-branch (provenance debt, flagged, not leaned on). No firewall crossing; Gate 5
untouched. Lock `tests/test_b1156_seam_a_gate2.py`.

## Provenance — the adversarial workflow

Sealed by **WF-1** (the masterplan's first workflow, `SEAM-A Gate 2`): 3 scouts (banked Habiro/CS
material · Kim/GSWZ theory · codex's finite-place datum) → gap synthesis → **2 attempts** (assemble ·
structural) → **3 adversarial refuters** (does-the-action-reach-Vol · is-Kim-arith-CS-really-torsion-only
· is-the-B800→GSWZ-normalization-legitimate) → seal. 10 agents, 422k subagent tokens. The seal is
**FLOOR**, reached by the refuters knocking down both attempts' forced verdicts. Full adjudication:
`verification/floor_adjudication.txt`.

## The seam (the prize, unchanged)

Does codex's heterotic realization (its **ℚ(ζ₁₂)/dP₆×dP₆** structure) appear as the **archimedean
∞-place** of the adelic object m004 — matching the arithmetic Chern–Simons / Habiro invariants of m004
on ℚ(√−3) (Kim)? **If yes, the heterotic axiom is *derivable*, not assumed.** Gate 1 (codex's ζ₁₂
construction) was met in B1155; **Gate 2 is the full arithmetic-CS action.** This arc is Gate 2's
sharpest attainable statement short of the specialist computation.

## What changed vs B1155 — three moves

### 1. A category correction (the phrasing the gate inherited was wrong)
There is **no "arithmetic-CS action *of m004*."** Arithmetic CS is a functional of a **field** F and a
**Galois representation** ρ, not of a 3-manifold. m004 enters only via its trace field K=ℚ(√−3) and its
shape z=e^{iπ/3}=(1+√−3)/2, which supplies **one** Bloch class **ξ=[z]∈K₃(ℚ(√−3))**. That one class has
**three inequivalent completions**:

| completion | invariant | value type |
|---|---|---|
| archimedean ∞ | Borel/Bloch–Wigner D(z) → **Vol(4₁)** | real transcendental ∈ ℝ |
| finite mod-n | **Kim CS_c(ρ)=inv_F(ρ\*c)** | torsion ∈ (1/n)ℤ/ℤ |
| p-adic | Lee–Park / GSWZ D_p(ξ) | ∈ ℚ_p/ℤ_p |

"Arithmetic CS **action**" names only the **finite** completion. Therefore **B800** (the state-integral
series, saddle (1+√−3)/2, V″=√−3) is the **p-adic** completion, **not** the finite Kim action — so
"assemble the Kim action from B800" was a category confusion (two different completions of the same ξ).

### 2. The a-priori MISMATCH is REFUTED (2 of 3 lenses)
B1155 leaned MISMATCH on: *"arith-CS is torsion-valued (1/n)ℤ/ℤ, so it cannot reach the real
transcendental Vol before any ρ is computed."* Two independent refuters showed this is a theorem about
the **finite μ_n truncation only** — Artin–Verdier H³(Spec O_F, μ_n)≅(1/n)ℤ/ℤ — secured **only by
stipulating** "arithmetic CS names the finite row by definition." The **full/Arakelov-compactified**
arithmetic CS over the **closed** Spec O_F (∞-place included) carries a **real archimedean summand =
the Borel/Bloch–Wigner regulator of ξ = Vol**. So the untruncated codomain **contains ℝ**; the
impossibility is truncation-dependent, **not** a codomain wall. This is exactly what **B1108** already
recorded ("the negative does not say no arithmetic theory [reaches Vol]… the object's volume must live
at the archimedean place") — re-verified this session.

### 3. MATCH is not sealable either
No map/equation sending codex's finite order-6 phase to Vol is constructed; equating a real
transcendental with a finite root-of-unity phase is false as stated. The honest finite-place result is a
**type-match** only (both are order-3/6 root-of-unity secondary-CS characters — B708's lk(3,5)=1,
B1108's "half a meeting"), **not** the archimedean-normalized period W₀ the derivation needs. The
ASSEMBLE attempt's v3(100)=147→GSWZ 146 reconciliation was **refuted** (inconsistent prefactor) — that
residual is a **p-adic** normalization item, **quarantined, not banked, immaterial to this gate**.

## The runnable anchor (own computation — `verification/reproduce.sh` → `REPRODUCES`)

- z=e^{iπ/3} satisfies **z²−z+1=0** (primitive 6th root; m004's geometric shape).
- **2·D(e^{iπ/3}) = 2.02988321281930725 = SnapPy Vol(4₁)** to 15 digits — the Borel regulator of ξ, the
  real archimedean summand the full arith-CS carries.
- V″(u₀) = **√−3** (the 1-loop datum, B800).

## Verdict: FLOOR — the exact remaining computation

Extend **Andersen–Hansen**'s proved root-of-unity ↔ Vol crossing from **closed Dehn surgeries on 4₁** to
the **cusped** complement m004: construct (or refute) the Arakelov-compactified arithmetic CS over closed
Spec O_F=ℤ[√−3], and decide whether its real archimedean summand furnishes a genuine map sending codex's
finite order-6 phase (exp(2πi/6)∈(1/12)ℤ/ℤ) to **Vol=2.02988321281930725**, vs merely relabeling Vol as
the regulator of ξ. Two specialist sub-bars: **(i)** object side — a stationary-phase/CS bridge with
content when CS=0 by amphichirality (B1108's unwalked door); **(ii)** codex side — the marked H³ basis /
period vector / Ω normalization that **OA-C1045/C1053 record as ABSENT** (without it codex supplies no
archimedean W₀). Neither is closable in-sandbox. This is **B708's** flagged NEEDS-SPECIALIST bar
specialized to **B1108's** registered-but-unwalked archimedean door.

## Fences

This seat did **not** construct the Arakelov-compactified action (Gate 2 remains NEEDS-SPECIALIST) and
did **not** re-run codex's off-branch ζ₁₂/dP₆ construction. The archimedean anchor is own-computed on
committed values (B1117 Vol, B682 the ζ_K(2) dictionary). The refutation of the a-priori MISMATCH rests
on B1108 (banked, re-verified). The v3 residual is quarantined. The prereg's "MATCH gets cc3's third
opinion" does **not** trigger (FLOOR, not MATCH). No firewall crossing claimed — the finite↔archimedean
pairing at √3 (B1155) is a structural adelic fact, not a physics bridge. Gate 5 untouched.

## Routes

- **Lead:** updates **L182** (the three-seams status) — SEAM-A moves from "leaning MISMATCH" to
  "FLOOR: the finite-phase→Vol map is the one open bar." Adds the Andersen–Hansen closed→cusped transfer
  as the named specialist computation.
- **Relay:** the Gate-2 floor + the two sub-bars route to **cc3** (arithmetic-CS action) and note the
  codex-side W₀ gap (OA-C1045/C1053). Not a kill — the seam is open and sharpened.
