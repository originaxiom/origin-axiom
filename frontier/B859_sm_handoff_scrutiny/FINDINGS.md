# B859 — the SM handoff scrutinised: one exact theorem verified, one gate error found and REPAIRED, the cascade survives on a framework-native criterion

cc banking seat, 2026-08-03. Mathematics scope; nothing to `CLAIMS.md`; Gate 5 untouched.
**Not preregistered** — this is verification of an incoming solo-tier handoff; its footing is
independent recomputation of every load-bearing claim.

## 0. What arrived

The solo seat's SM-campaign package (2026-08-03): HANDOFF.md, SM_STRUCTURE_LEDGER.md (thesis:
**the forced/selected boundary is the even/odd boundary**), and six reproducer scripts. Everything
solo-tier, nothing banked. This arc is the banking review its own staging queue (S1) requests,
run on the load-bearing computations.

## 1. VERIFIED — the Higgs-synthesis (OP) theorem, exactly

**OP = ½[j(τ) − j(−4/τ)] = 818626500·√3** at τ = 2i√3, the object's cusp shape:

| check | result |
|---|---|
| τ₁ = 2i√3 and −4/τ₁ = 2i√3/3 are **B853's two CM points** of disc −48 (forms (1,0,12), (3,0,4)) | **exact** |
| j₁ + j₂ = 2835810000 | to 5×10⁻³² |
| j₁·j₂ = 6549518250000 | to 2×10⁻²⁸ |
| j₁ − j₂ = 1637253000·√3 | exact |
| **OP is ODD under the class-group swap** τ₁ ↔ τ₂ | **exact** |

**The last line is the point.** An order parameter must be odd under the symmetry that breaks.
B849 found none at the manifold level and required one on the state space; **this supplies one, on
the CM points, odd under exactly the Cl(O₄) = ℤ/2 that B853/B855 identified as object-specific**
(h(−48) = 2 against m003's maximal-order h = 1).

**One naming correction:** τ ↦ −4/τ swaps the CM points but is **not** the standard Fricke W₄
(which is τ ↦ −1/(4τ), sending 2i√3 elsewhere). The map is right; the name should go.

**Also verified:** F17's conductor-4 theorem — h(−3f²) = 1, 1, 1, **2**: first torsor exactly at
f = 4. A4's DG pin — P(t) = t(t−1)(t²−5t+1), P(1) = 0, **P′(1) = −3**, matching B581's τ₁. And the
**sign-law certificate runs against this repo's own B581 data**: all six blocks, inside = m,
outside = m, circle = 0 — `sign(τ_m) = (−1)^m` stands (the script's hardcoded path repointed).

## 2. THE ERROR — the cascade's step-2 gate

`option_tree.py` computes SO(8) with **h∨ = 7. It is 6** (dim = rank·(h+1): 28 = 4·7). Every other
entry in the same script is correct. Two independent confirmations: the simply-laced identity, and
**SO(N)₁ = N free Majorana fermions ⟹ c = N/2**, so c(SO(8)₁) = 4.

**Consequence:** c(SO(8)×U(1)) = 5 = c(SO(10)₁). The option the handoff excluded as *"NOT conf,
c = 9/2"* **is conformal** — the standard SO(N) ⊃ SO(N−2)×SO(2) free-fermion split — and at
**dim 29** it beats SU(5)×U(1)'s 25 under the handoff's own maximal-residual-symmetry principle.
As stated, step 2 is not unique and the cascade fails. The handoff's own §2e records this exact
break as CORRECTED-BY-AUDIT — *"the conformality gate reinstated it"* — **the audit that restored
the cascade introduced the error.**

## 3. THE REPAIR — and it is better than the original

**Gate on chirality, not conformality.** `−1 ∈ W(G)` ⟺ every representation self-conjugate ⟺ no
chiral matter. For D_n, **−1 ∈ W iff n is even**:

- **SO(8) = D₄: −1 ∈ W** (verified by construction — all-minus is an even number of sign flips
  for n = 4). 8_v, 8_s, 8_c all real. **No chiral matter.**
- **Independently:** Borel–de Siebenthal on the extended D₄ diagram gives A₁⁴ and A₃+A₁ — **no
  A₄** — so the SO(8) branch cannot reach SU(5) at all. Two obstructions.

| step 2 | dim | conformal | chiral |
|---|---|---|---|
| **SU(5)×U(1)** | 25 | ✓ | **✓ — winner, unique** |
| Pati–Salam | 21 | ✓ | ✓ |
| SO(8)×U(1) | 29 | ✓ | **✗ dead** |

**Applied uniformly, the gate strengthens the whole cascade:**

- **Step 1**: the coset is what carries would-be matter, and the vector-like cosets die by the
  same criterion — Sp(8)'s **42** (C₄: −1 ∈ W) and SU(6)×SU(2)'s **(20,2)** (20 = Λ³(6) is
  self-dual, 2 pseudoreal). Viable: SO(10)×U(1), SU(3)³, SU(3)₉ → max-dim winner **SO(10)×U(1),
  unique**. This **retires part of the Michel import** — the framework's own even/odd criterion
  does the killing.
- **Step 2**: SU(5)×U(1), unique (above).
- **Step 3**: all three options chiral-viable — **the gate is silent**, the menu is {16, 12, 10},
  the SM is in it and non-extremal. **The "one trit at the chiral step" conclusion is unchanged.**

**And the repaired gate is framework-native:** the ledger's thesis is *"chirality is the odd
sector's name"* — the −1-in-W criterion **is** the even/odd boundary, the same fact that makes
E₆'s 27 and SO(10)'s 16 complex (−1 ∉ W for E₆, D₅) in the first place. The cascade is now
selected by the framework's own principle at steps 1–2, with the imported principle needed only
for the max-dim ranking.

## 4. Corrections to this seat's own work in the process

- First Weyl test was **vacuous** (root systems are always closed under negation); replaced by the
  correct −1-in-W criterion with brute-force confirmation on D₄/D₅.
- A central-charge slip (24/5 for SU(5) instead of 24/6) caught before reporting.
- The initial reading — "the cascade fails" — was **premature**; the owner's push to look for the
  repair rather than the kill was correct, and the repair exists.

## 5. What this arc does NOT establish

- **Menu completeness (P5) is still an import** — the five-chain list and the step-2/3 menus are
  taken from the classification, not re-derived. A wrong menu breaks uniqueness silently.
- **The max-dim ranking at steps 1–2 is still Michel-flavoured** — the chirality gate prunes, the
  ranking picks; only the pruning is framework-native so far.
- **Nothing here reaches values** — the cascade is about group selection, and the SM group's
  selection cost (one principle + one trit) is unchanged, not eliminated.
- Imports P1–P4, P6–P8, P10 remain **ungated**.

## Carried forward

1. **Gate the menu-completeness import (P5)** against the conformal-embedding classification —
   the single point where the cascade could still silently fail.
2. **Fix the Fricke naming** in the ledger before it propagates.
3. **The step-3 trit** is now the entire selection cost. The framework's own question: is there an
   odd-sector (observer-level) criterion that decides {16, 12, 10} the way −1-in-W decided
   steps 1–2?

`tests/test_b859_sm_scrutiny.py`
