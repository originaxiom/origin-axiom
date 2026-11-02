# AGY Audit Verification Package (2026-11-02)

Self-contained verification scripts, JSON results, and stdout logs accompanying `relays/AGY_TO_CC_2026-11-02_FULL_AUDIT_BLIND_SPOTS_AND_REFRAMING.md`.

## Contents

1. **`independent_core_recompute.py`** (`independent_core_recompute_results.json`, `independent_core_recompute_out.txt`)
   - First-principles independent recomputation of `T-ROOT` (`m004` hyperbolic volume, monodromy $LR$, Alexander polynomial $\Delta_{\text{m004}}(t) = t - 3 + t^{-1}$, Gieseking orientable double cover $(LP)^2 = LR$), `T-FIBRE-c6` ($\text{tr}[L, R] = -2$, $c = 6$), `C25` (`B1758` exact $\text{SU}(5)$ + chiral anomaly nullspace for $6Y$), and `THE WEAVE` (`B1600`/`B1638` rank-1 Yukawa no-go theorem).

2. **`verify_closed_form_c.py`** (`verify_closed_form_c_results.json`, `verify_closed_form_c_out.txt`)
   - Verifies **Theorem 1**:
     - Exact 100% sector independence of $c_s(\tau, w)$ across `up`, `down`, and `lepton` (max difference $0.00 \times 10^0$).
     - Exact 1D strip Parseval + Euler digamma + Hurwitz–Lerch closed form for $c_s(\tau, w)$ matching `b1656_funcs.py`'s 2D grid quadrature `cA` to $2.98 \times 10^{-13}$.
     - Resolution of `B1788` Hypothesis `(b)`: proves $c_j^\infty + c_k^\infty - c_1^\infty - c_i^\infty = 0 \iff \{3\alpha\} \in \{1/4, 3/4\} \iff \alpha \in \{1/12, 1/4, 5/12\}$.
     - Refutation and exact replacement of `B1788` Hypothesis `(a)`: proves $E(c_1 - c_i) = \frac{1}{2}\|3\alpha\|_{\mathbb{Z}}$ and $E(c_j - c_k) = \frac{1}{4} - \frac{1}{2}\|3\alpha\|_{\mathbb{Z}}$, matching the empirical exponents on $\alpha = 2/5, 1/7, 4/9$.

3. **`verify_ckm_inversion.py`** (`verify_ckm_inversion_results.json`, `verify_ckm_inversion_out.txt`)
   - Verifies **Theorem 2**:
     - Exact 4D nullity $R_1^2 + R_i^2 + R_j^2 + R_k^2 = 0$ vs. 3D non-nullity $R_i^2 + R_j^2 + R_k^2 = -R_1^2 \ne 0$ for all twisted points $w \ne 0$.
     - Exact matrix identity $Y_s = \vec{h}\,\vec{m}_\perp^T + \vec{m}_\perp\,\vec{h}^T - (\vec{h}\cdot\vec{m}_\perp)I_3 - u_1^{(s)}[\vec{h}]_\times$ and $Y_s\vec{h} = Y_s^T\vec{h} = (\vec{h}\cdot\vec{h})\vec{m}_\perp^{(s)}$ (verified to $10^{-16}$).
     - Locking of $u_1^{(s)}$ to $\hat{h}^*$, inversion of $\theta_{12}^{(u)}/\theta_{12}^{(d)} \gg 1$, the $(1,3)\leftrightarrow(3,1)$ CKM corner transposition ($|V_{ub}| \gg |V_{td}|$), CP phase suppression $\sin\delta_{\text{CP}} \lesssim O(\theta_{12}^{(d)}/\theta_{12}^{(u)})$, and the analytic `(0.735, 0.735, 1.361)` Lagrange-multiplier compromise.

4. **`verify_stepb_and_census_audit.py`** (`verify_stepb_and_census_audit_results.json`, `verify_stepb_and_census_audit_out.txt`)
   - Verifies the unread `B1825` (`Step B`) `run.json` readout and observable-by-observable $\chi^2_{\text{ten}}$ breakdown, the four `scripts/stepb/` and `cm_zero_line.py` architectural/numerical defects (`kten.py` choice `30900` ignore, `cells.py` $7,680$ order-12 massless-electron choices in `physical_choice`, $2:1$ CKM reading duplication, and `F_6..F_26` asymptotic collapse / `float64` underflow), and the 3-manifold `m004` topological and $\mathbb{Z}_3$ colour-center Wilson line torsion checks.

5. **`verify_operator_gate_and_4d_higgs.py`** (`verify_operator_gate_and_4d_higgs_results.json`, `verify_operator_gate_and_4d_higgs_out.txt`)
   - Verifies the executed three-step elevation in `src/origin_axiom/` (`twisted_norms.py`, `operator_gate.py`, `stepb_audit.py`) and `tests/test_elevation_operator_gate.py`: runs `Gate 0` (`evaluate_operator_gate`) on `FR-FIB` (`0/4` clauses passed) vs `FR-COV` (`4/4` clauses passed) in $1.35\text{ ms}$, verifies the 4D quaternionic Yukawa identity $Y_s^{\text{4D}}$ to $9.93 \times 10^{-16}$, demonstrates how a single shared scalar quaternion component $a_0$ flips $|V_{ub}|/|V_{td}|$ from $11.28$ to $0.6778 < 1.0$ and raises $\sin\delta_{\text{CP}}$ from $0.0842$ to $0.6997$ on `B1825`'s exact best address, and benchmarks `closed_form_cA` ($48.5\times$ speedup over 3-sector 2D Gauss–Legendre quadrature).

## Reproduction

From the repository root:

```bash
python3 relays/agy_audit_2026_11_02/independent_core_recompute.py
python3 relays/agy_audit_2026_11_02/verify_closed_form_c.py
python3 relays/agy_audit_2026_11_02/verify_ckm_inversion.py
python3 relays/agy_audit_2026_11_02/verify_stepb_and_census_audit.py
python3 relays/agy_audit_2026_11_02/verify_operator_gate_and_4d_higgs.py
pytest tests/test_elevation_operator_gate.py -v
```
