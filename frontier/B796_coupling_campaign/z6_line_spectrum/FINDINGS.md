# P3 — the ℤ₆ line-operator spectrum, enumerated

**Seat:** cc3 (audit). **Branch:** `audit/b775-braver-questions`. **Gate 5-Q**
— structure only; every quantity is a representation label or a lattice class,
nothing is compared to a measured value.

**Run:** `python3 frontier/B796_coupling_campaign/z6_line_spectrum/z6_lines.py`
— all assertions pass.

---

## Why

The prediction register grades **P3 the framework's sharpest distinguishing
claim** and states its falsifier as *"a line-operator spectrum inconsistent
with the ℤ₆ quotient."* That names a **kind** of evidence, not an object. B862's
own phrasing is honest about it: *"falsifiable in principle."* **In principle**
is where the claim stopped.

A prediction that cannot name what must not exist is not yet falsifiable in
practice. This arc enumerates the spectrum so P3 can name things.

## What was computed

For `G = G̃/Γ` with Γ central, lines split two ways and the quotient moves them
in **opposite** directions:

| | effect of quotienting |
|---|---|
| **Wilson** (electric) | labelled by reps trivial on Γ — quotienting **removes** lines |
| **'t Hooft** (magnetic) | labelled by `π₁(G) = Γ` — quotienting **adds** lines |

Dirac quantisation locks the two sides. A global form is therefore not a choice
of which lines to keep; it is one lattice.

With `z = (ω·I₃, −I₂, e^{iπ/3})` the electric condition is
`e(t,d,Y) := t/3 + d/2 + Y ∈ ℤ`, and magnetic class *n* carries flux
`(n/3 mod 1, n/2 mod 1, n/6)` in (colour, weak, hypercharge).

## Result 1 — the particle spectrum cannot fix Γ, and the arc shows why

`e` is an **integer** for every SM multiplet — so it vanishes mod 1, mod ½, and
mod ⅓ alike. All observed matter descends to **all four** candidate forms.

This reproduces Tong 1705.01853 from the descent condition alone, with no
external input. It is also the reason P3 needs lines.

## Result 2 — the magnetic spectrum separates all four forms

| Γ | classes | colour flux? | weak flux? | **both together?** |
|---|---|---|---|---|
| 1 | 1 | no | no | no |
| ℤ₂ | 2 | no | **yes** | no |
| ℤ₃ | 3 | **yes** | no | no |
| **ℤ₆** (derived, B862) | **6** | **yes** | **yes** | **YES** |

**Four distinct signatures** (asserted in code, not eyeballed). The minimal
monopole of the ℤ₆ theory — class n=1 — carries hypercharge magnetic charge
**1/6 together with colour flux 1/3 and weak flux 1/2**. It is *not* a pure
hypercharge monopole, and **no other global form permits an object carrying
both colour and weak flux.**

That is the positive signature, and it is what to look for.

## Result 3 — n=1 is minimal in the strict sense

The Dirac pairing of class n=1 with each multiplet is `e` itself: `1,0,1,0,1,0,1`
over `Q, u^c, d^c, L, e^c, ν^c, H`. **gcd = 1.** A gcd above 1 would mean a
magnetic charge 1/gcd of this one stays local against all matter, and n=1 would
not be smallest. It is 1, so n=1 is the floor.

*(An earlier draft argued this by "saturating Dirac quantisation against charge
e/3" — rhetorical rather than proved. The gcd is the actual argument and is what
the script now computes.)*

All 7×6 = 42 pairings are integral: **one consistent spectrum**, not two lists.
And the converse bites — each Wilson line the quotient forbids is non-local
against the minimal monopole (pairings 1/3, 1/2, 1/6, 2/3).

## Result 4 — an audit finding about the register itself

**P2's confirmation lends no evidential support to P3.**

P2 (charge quantisation of observed matter) holds in **all four** global forms,
by Result 1. It is CONFIRMED and WEAK. P3 is fixed only by the line spectrum:
UNTESTED and STRONG. They share a lattice, not a test. The register lists both
among its eight and calls two "distinguishing" — correct as far as it goes, but
the two must not be read as mutually reinforcing, and nothing currently says so.

## The falsifier list — what P3 should say instead

**Magnetic (the discriminating ones):**

- **F1** — a minimal-hypercharge monopole with **no colour flux** → excludes ℤ₆, ℤ₃
- **F2** — a minimal-hypercharge monopole with **no weak flux** → excludes ℤ₆, ℤ₂
- **F3** — any monopole whose flux triple is **not one of the six rows** (the
  table forces colour 1/3 ↔ hyper 1/6 and weak 1/2 ↔ hyper 1/2)
- **F4** — a **pure-hypercharge** monopole below hypercharge magnetic charge 1
  (ℤ₆ permits one only at n ≡ 0 mod 6)

**Electric:**

- **F5** — a genuine bare colour-triplet line `(3,1)₀` → forbidden by ℤ₆, ℤ₃
- **F6** — a bare weak-doublet line `(1,2)₀` → forbidden by ℤ₆, ℤ₂
- **F7** — an isolated hypercharge-1/6 colour singlet → forbidden by ℤ₆ (P2, as a line)

**Confirming rather than killing:**

- **C1** — the minimal monopole carrying colour **and** weak flux together.
  Unique to ℤ₆.

## Scope — stated because the register has overstated before

- **No monopole has been observed.** None of F1–F4 is currently tested. P3 moves
  from *"testable in principle"* to *"testable, with a stated list."* It does
  **not** move to CONFIRMED. This arc adds no status column claiming otherwise.
- F5–F7 concern **line operators** — probes, not particles. "Observing" them
  means a lattice or theoretical determination of the spectrum, not a detector
  event.
- The derivation of Γ = ℤ₆ is **B862's**. This arc takes it as given and does
  not re-prove it. If B862 falls, this list describes nothing.

## What this does not do

It does not make P3 easier to test. Monopole detection remains the hard part,
and the framework supplies no mass scale for these objects — the weight ledger
puts every derived quantity at weight 0, so **no monopole mass is predicted and
none can be**. The prediction is about **charge correlation**, and that is
scale-free: if a monopole is ever seen, its flux triple is the test, whatever
its mass.

---

**Relay:** row filed in `docs/RELAY_LEDGER.md`. **cc3 does not merge.**
