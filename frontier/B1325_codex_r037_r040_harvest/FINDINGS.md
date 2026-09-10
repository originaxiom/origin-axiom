# B1325 — the codex harvest gap: R037 banked, R038–R040 rowed open

**Verdict: OPEN.** One record re-derived and banked (R037); three read, rowed and carried as named debts (R038-R040) — which is what makes the arc OPEN rather than PROVED. Everything
below was recomputed on this bench (Python standard library + SnapPy 3.3.2 for the presentation only);
nothing is taken on the seat's word.

## The gap

B1235 harvested codex at `4ec3e07f`. The seat is at **`f7a49536`** — four records ahead. Main had never
seen **R037, R038, R039, R040**, and six relay memos dated 2026-09-02 carried **no `RELAY_LEDGER` row**:
the invisible-work failure state that ledger exists to catch. The seat's pin is current, so this is not
drift — main simply stopped harvesting.

The gate could not see it either: `harvest_debt.py` skips a seat whose branch is not fetched, and the
codex branch was not fetched in this clone.

## R037 — re-derived here, and banked

`pi_1(m000) = <a, b | aabbAB>`. Its orientation character is **unique**: `w(a) = w(b) = 1`. Schreier
generators of `H = ker(w)` on the transversal `{1, b}`: **`aA, bA, aa, ab`**.

| | |
|---|---|
| `Surj(pi_1 m000, 2T)` | **48** |
| `Surj(pi_1 m004, 2T)` | **48** (both two `Aut(2T)`-orbits; `\|Aut(2T)\| = 24` computed here) |
| distinct restrictions to `H` | **24** |
| fibre sizes | **exactly 2, every fibre** |
| the fibre | the central twist `phi^w(g) = (-I)^{w(g)} phi(g)` — a homomorphism with the *same* restriction in **48 of 48** cases |
| `Aut(2T)`-orbit of the 24 images | **size 24 — a single orbit** |

Therefore **exactly one of m004's two 2T quotient classes extends over the non-orientable parent
m000**; the other is its unique nonzero central `H^1(m004; C2)` twist and does not extend. Codex's
count-level statement is confirmed at map level, independently.

**The fence is preserved verbatim:** the resemblance to B1208's one-extending-spin result is **not an
identification**, and **I-6 remains UNEARNED**.

**Why it matters.** §2 of THE PAPER opens on "a surjection `pi_1(m004) -> 2T`, of which there are
exactly two" and treats that count as the entry point. This says the **orientation parent selects one
of the two**. It is the third instance of one mechanism — R039 does it for the A4→2T lift, and §9's
spin-lift row already uses it ("extension-consistency with the non-orientable manifold our object
double-covers ... selects, over exactly one of the two lifts"). The paper uses the mechanism once and
does not name it.

## R038, R039, R040 — read, rowed, not banked

Not re-derived here. Rowed **OPEN** rather than left invisible.

- **R038** — A1 SU(6) rank reduction; `27 -> 10_2 + 5_-4 + 5bar_-6 + 5bar_4 + 1_0 + 1_10`, with a
  NEGATIVE (one decomposable VEV is not D-flat; moment norms 5/6 and 1/2).
- **R039** — A4→2T lift torsor; 24 A4 surjections each, two lifts apiece, exactly one extending over m000.
- **R040** — free-deck Chern–Simons. Two results codex asks to be graded **separately**: a **closed
  theorem** (Kawauchi I/III + CGHN/APS `3 eta = 2 cs + tau mod 2` ⇒ `cs = 0 mod 1`), and a **finite
  census** (1260/1260 non-orientable cusped orientation covers at `cs = 0`, max residual 1.8e-15).
  **Do not promote the census to a universal cusped theorem** — Kawauchi is closed, cusped eta is
  peripheral-basis-dependent, and the non-compact PSL class keeps an order-two ambiguity.

## Adjacent, independent, and weaker than R040

Recomputed here while R040 was still unread: **every orientation double cover is amphichiral** — the
deck involution is orientation-reversing and, by Mostow, isometric. **250 tested over the
non-orientable census, 250 amphichiral, 0 chiral.**

This is the elementary sibling of R040's CS statement, on the same free orientation-reversing
involution. **Codex reached the CS half first and over a larger census (1260).** What the two do not
share is the consequence for the chirality bit, recorded separately: axiom 5 does not merely select an
orientable manifold, it *guarantees* an amphichiral one.

## Also noted

R040's proof uses **APS** (`3 eta = 2 cs + tau mod 2`). `main.tex` contains no occurrence of Atiyah,
APS, eta invariant, signature defect or Hirzebruch. The machinery is in the programme and one branch
away from the paper.

Reproduce: `verification/r037_reproduce.py` (stdlib + SnapPy for the presentation), output captured in
`verification/r037_output.txt`.
