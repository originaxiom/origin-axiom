# Probe B1 — Gluing identity vs. discrete Chern-Simons flatness

> **Speculative frontier work.** Everything here is a *logged observation*, not a
> claim (see `../../GOVERNANCE.md` §5). Nothing in this directory is promoted to
> `CLAIMS.md`. The `open` claims O1–O5 remain `open`.

## The question

`ROADMAP.md` probe B1, from the handoff document's "Step 3B":

> Does the boundary-to-bulk gluing identity `W = S_L(m,Q) − F_R(q,s) + m·s` map
> onto a discrete Chern-Simons flatness condition `F = 0`?

In Witten's 2+1 Chern-Simons gravity the gauge connection splits as
`A_conn = ω + e` (ω = spin connection, e = dreibein/frame field), and the
equation of motion is flatness `F(A_conn) = dA_conn + A_conn∧A_conn = 0`.

## What the probe computes (`probe.py`)

Two computations that can be done **exactly**:

**[1] Frame / spin-connection decomposition of `log(A)`.**
`log(A) = (log φ² / √5)·(H + 2(E+F))` where `H` is the boost generator (spin
connection direction) and `E+F` the symmetric frame generator. Verified against
`scipy.linalg.logm` to 2.8e-16.

- spin-connection coefficient `a = log(φ²)/√5 ≈ 0.4304`
- frame coefficient `d = 2·log(φ²)/√5 ≈ 0.8608`
- **frame-to-spin ratio `d/a = 2` exactly**
- **torsion component (coefficient of the antisymmetric `E−F`) is exactly 0** —
  `log(A)` is symmetric, so the discrete connection is torsion-free.

**[2] The gluing identity as a holonomy composition law.**
`S_A = ext_{m,s}[S_L − F_R + m·s]` holds (this is proven claim P7). The
extremised intermediate data is `m = q, s = Q − q` — i.e. the shared *edge*
between the two boundary half-moves, integrated out.

## Honest verdict — B1 is a **qualified yes**, bounded

**What the gluing does reproduce.** Extremising over the shared variable is
exactly the composition law for canonical transformations / holonomies. A flat
connection *is* a consistent holonomy representation of the path groupoid;
discrete flatness (plaquette holonomy = identity) *is* that composition law. So
the gluing identity reproduces the holonomy-level structure that discrete
flatness encodes — and `log(A)` does split cleanly into a torsion-free frame
plus spin connection, the ingredients of the Witten connection `ω + e`.

**What it does not do.** This is the holonomy / representation-variety level
only. The gluing does **not**:

- produce the Chern-Simons action, or its level `k`;
- distinguish 2+1 *gravity* from any other flat-`SL(2,ℝ)`-connection theory;
- supply a curvature 2-form whose vanishing is the dynamical content of `F = 0`.

So B1's answer: the gluing is **structurally compatible with, and reproduces,
discrete flatness at the holonomy level** — but it does not *derive* Chern-Simons
gravity. The `frame-to-spin ratio = 2` and `torsion = 0` results are exact and
suggestive, but "suggestive" is not "proven" (`GOVERNANCE.md` §6).

## Status

- No claim promoted. O1–O5 remain `open`.
- Logged in `../../PROGRESS_LOG.md`.
- Next frontier step would be to identify a concrete Chern-Simons gauge in which
  the gluing variables *are* `(ω, e)` and check whether a level `k` is forced —
  that is the real open problem and is not closed here.
