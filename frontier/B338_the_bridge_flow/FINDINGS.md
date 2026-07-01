# B338 — the bridge: a Dehn-filling flow connects symmetric-UV to broken-IR, but its parameter is external

**Status: banked (frontier). Attack C of the symmetry-broken sweep. Firewalled; nothing to `CLAIMS.md`.** Both chats'
escape from the structure⊕value tension (B337) is the same as the SM's: have *both* (unified UV + ordered IR) by
**breaking along a flow** — symmetric-UV → broken-IR. We tested whether the object *contains* such a flow (rather than
importing physical RG). It does — with a clean law — and the test also locates exactly where the external input enters.

## The flow (verified)
Dehn filling is the object's own "closing". The **(1,n) filling flow** interpolates from the **cusp** (`n→∞`: the
symmetric, amphichiral object, `CS = 0`) to **filled/broken** configs (finite `n`: chiral, `CS ≠ 0`). The chiral **order
parameter** is the Chern–Simons invariant — exactly the chirality B336 showed the value needs — and it turns on
continuously:

```
CS(1,n)  ~  −1/(2n)          (verified: CS(1,n)·n → −0.5, to 3 digits by n=10)
```

So the object **contains** a flow whose order parameter turns on smoothly from the symmetric endpoint. The bridge is not
imported — it is Dehn filling, an object-internal deformation.

## Where the external input enters (the firewall, located precisely)
The flow **exists**, but its **parameter** — *which* slope `(1,n)`, i.e. how much to close and in which direction — is
**external input**. The choice of filling *is* the choice of vacuum (the "interaction with the nothing", B286). The
object supplies the **track** (the moduli space of fillings = symmetry-breakings); physics supplies the **direction**
(which breaking is realized). So:

> **Structure ⊕ value is bridged by a flow the object contains — but the bridge is externally parametrized, so the value
> is *selected* (by the filling choice), not *forced*.** Even with the flow, the firewall holds: the object provides the
> moduli of breakings; physics selects one.

This closes the symmetry-broken sweep into a coherent picture: **symmetric object = UV structure (E₆, amphichiral,
`CS=0`); Dehn filling = the flow (chirality `CS ~ 1/n` turning on); broken/filled = IR (chiral, orderable) — with the
filling slope the one external datum.** The reunification is real *as a flow*; the value is where the external choice
lives.

## The firewall (held) — and the speculation, fenced
The math banked here is only: `CS(1,n) ~ −1/(2n)` along the filling flow, `CS=0` at the symmetric cusp, and that the
slope is external. The **physical** reunification reading (UV-symmetric → IR-ordered via this flow = spontaneous
breaking / RG) is `[LEAP]` — held in `speculations/S047`, tag-fenced, HELD rule, nothing to `CLAIMS.md`.

## The fence
SnapPy 3.3.2 CS of `m004(1,n)` (recorded values) + the asymptotic fit. No physics values. Nothing to `CLAIMS.md`.

`the_bridge_flow.py` (pyenv/SnapPy) · `tests/test_b338_the_bridge_flow.py`. Related: **B337** (structure⊕ordering, the
two endpoints), **B336** (chirality is the order parameter), **B335** (the symmetric endpoint), **B286/B289/B290** (the
filling/CS/core-scale tooling), **B322** (the value hunt), **S047** (the reunification speculation). Lit: Neumann–Zagier
(Dehn-surgery asymptotics of CS/volume); Thurston (hyperbolic Dehn surgery).
