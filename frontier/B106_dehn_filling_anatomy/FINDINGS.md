# B106 — the trace map at the DEHN-FILLING fixed points (the third class)

**Status: `computer-assisted` (D1 exploratory raw data; D4 high-precision; D3 census).** Executes the CC-web
"Final Computations" handoff D1/D4/D3. The Jacobian was computed before at the *trivial* rep (the Dickson
tower, B89-T) and the *geometric* rep (the adjoint torsion, B98/B99); here at the **Dehn-filling** reps — the
third class, never computed, where degree=rank lives. The Dehn-filling reps are **irreducible**, so (unlike
the degenerate trivial rep) the trace-coordinate Jacobian is clean. NO physics (the eigenvalues are
mathematical data); no Origin-core claim; P1–P16 untouched. Script `probe.py`; test
`tests/test_b106_dehn_filling_anatomy.py`.

## D1 — the Jacobian: three fixed-point classes, three distinct signatures
The figure-eight trace map `T₁²` (`a→aba, b→ab`) at each fixed point (raw data, the GATE):

| fixed point | stability (stable, unstable, neutral) | eigenvalue character |
|---|---|---|
| **trivial** (tower) | 3, 3, 2 | real — the **Dickson tower** (`φ²`, `6.85`, `17.9`, …) |
| **geometric** (torsion) | 3, 3, 2 | **complex** — the twisted-Alexander / adjoint torsion |
| **SL(3) W1, W2** (Dehn-filling) | **1, 1, 6** | partially **ELLIPTIC** — 6 on the unit circle, one hyperbolic pair (8.08, 0.124) |
| **SL(4) principal, secondary** (Dehn-filling) | **4, 4, 7** | partially **ELLIPTIC** — 7 on the unit circle (incl. roots of unity) |

So the **Dehn-filling reps are "center-like" / partially elliptic** — qualitatively unlike the hyperbolic
trivial and geometric reps. The neutral directions include the tangent to the (2-dim) component plus genuine
**elliptic (root-of-unity)** eigenvalues — e.g. the SL(4) principal carries `±i, −1`, the secondary `ω, ω²`.

**[V93 hygiene — the root-of-unity claim is verified, not gauge noise].** The SL(4) Jacobian here is built by a
`pinv` over QR-selected words at a *repeated-eigenvalue* rep, so the B84 gauge-noise gate applies: a
rank-deficient `pinv` can manufacture seed-dependent eigenvalues that mean nothing. We pass the gate.
`d1_neutral_eigenvalues_are_roots_of_unity()` recomputes the neutral eigenvalues across **≥3 independent
`realize_bundle_rep` seeds** and finds them **exactly roots of unity and seed-stable**: principal
`angles/2π = {0, ±1/4, ±1/2}` (`= 1, ±i, −1`), secondary `angles/2π = {0, ±1/3}` (`= 1, ω, ω²`). The
fine root-of-unity *values* are therefore real structure, not pinv artifact; the coarse `4-4-7` *count* was
already robust (topological). Locking test: `test_d1_neutral_eigenvalues_are_roots_of_unity_seed_stable`.

**Honest negative.** The **stability type does NOT encode the degree=rank exponent**: both SL(4) components
have the *same* signature `(4,4,7)`, yet the principal has exponent 4 and the secondary 3. So the exponent is
**not** read off the Jacobian — **no mechanism is claimed** (the hinge test is not met by the stability data).

## D4 — the eigenvalue anatomy: `Lᵢ = c·Mᵢ^k` per eigenvector (high precision)
The meridian `μ` and longitude `[A,B]` **commute** on the Dehn-filling components (off-diagonal `≲1e-9` in the
shared eigenbasis); simultaneously diagonalized, the paired `(Mᵢ, Lᵢ)` satisfy, **eigenvector-by-eigenvector**,

```
   Lᵢ = c · Mᵢ^k,   c a root of unity,
```
verified to high precision (the per-eigenvector deviation, mpmath/`numpy.eig`):

| component | `k` | `c` | `c^k` | per-eigenvector `|Lᵢ − c·Mᵢ^k|` |
|---|---|---|---|---|
| SL(3) W1 | 3 | `1` | `1` | 3.1e-09 |
| SL(3) W2 | −3 | `1` | `1` | 3.2e-10 |
| SL(4) principal | 4 | **`−1`** | `1` | 2.8e-10 |
| SL(4) secondary | 3 | **`i`** | `−i` | 5.2e-15 |

So **degree=rank holds eigenvector-by-eigenvector**, with the B89/B88 scalar `c` (a root of unity, `1` at
SL(3), `−1` / `i` at SL(4)). The secondary's `Mᵢ` differ from the principal's (different A-spectrum), as
expected. *(The earlier "branch noise" that killed an attempt is avoided by the simultaneous-diagonalization +
the explicit scalar `c`.)*

**[V93 hygiene — what is corroboration vs. what is new].** Split the credit honestly:
- The **SL(4) principal** (`c=−1`, `M⁴=L`) **corroborates B89/B83**, where `L=(−1)^{n−1}Mⁿ` is *already proved
  symbolic-exact over ℚ(ω)* (`c=(−1)^{n−1}=−1` at `n=4`). It is **numerical re-confirmation, not a new advance**.
- The **new content** here is (i) the **SL(4) secondary** (`c=i`, `M³=L`, **`computer-assisted/numerical`**
  ~5e-15 — *not* proved; the `c=i` scalar is the open piece, see Phase-4 `c→θ`), (ii) the **SL(3) W2**
  per-eigenvector relation, and (iii) the **per-eigenvector method** itself (simultaneous-diagonalization +
  explicit `c`), which is the clean carrier when the global stability signature does not encode the exponent.

## D3 — the SL(4) census completion
On the two known SL(4) Dehn-filling components: **`M⁴=L` (principal, `c=−1`, `c⁴=1`)** and **`M³=L`
(secondary, `c=i`)** hold (scalar-deviation `≲1e-9`); the **conjugate relations `M⁴·L=1` and `M³·L=1` are
ABSENT** on both (deviations `O(1)`). This contrasts with SL(3), where W1 gives `M³=L` *and* W2 the conjugate
`M³·L=1`. **Exhaustiveness** over *all* rank-4 spectra needs the symbolic `Fix(T₁²)` (the B71 route at rank 4)
— **open**; the conjugate could in principle live on a spectrum the census didn't search.

## Verdict
The third fixed-point class is now computed. The Dehn-filling reps are **partially-elliptic** trace-map fixed
points (distinct from the hyperbolic trivial/geometric reps); degree=rank holds **per eigenvector**
(`Lᵢ=c·Mᵢ^k`); the SL(4) conjugate A-variety relations are absent on the known components. The degree=rank
**mechanism remains open** — the Jacobian *signature* does not encode the exponent (honest negative); the
clean carrier is the **per-eigenvector relation** (D4), not the global stability type.

```bash
python frontier/B106_dehn_filling_anatomy/probe.py
python -m pytest tests/test_b106_dehn_filling_anatomy.py -q
```
No physics claim; proven core P1–P16 untouched.
