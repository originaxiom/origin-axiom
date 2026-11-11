# Self-Consistent Fixed-Point Loop Engine (`Φ(X*) = X*`)

Clean-room, pre-registered, zero-parameter (`0 of 19` data-free) implementation and independent zero-trust referee audit of the composite self-consistency fixed-point loop $\Phi(X^*) = X^*$.

## Architecture

- `PREREGISTRATION_PLAN.md` & `SEAL_SHA256.txt`: Pre-registered candidate domains, thresholds, and falsifiers sealed prior to execution.
- `src/phi_loop/sector1_parent_anomaly.py`: **Sector 1 (`BE-1`)** — Cusp modular `(T, S)` single-channel sewing across all crystallographic root systems ($1 \le r \le 24$), distinguishing symmetric Euclidean Gram matrices ($\langle \alpha_s, \alpha_s \rangle = 2$) from asymmetric Cartan matrices, plus explicit 240-root $\mathfrak{e}_8$ verification of $h_4$, $\zeta_{\operatorname{Spin}(10)}$, and the 3-branch weave orbit.
- `src/phi_loop/sector2_history_state_loop.py`: **Sector 2 (`BE-2`)** — Intrinsic torsion discovery via Smith normal form, bundle extension $W_H^T v \equiv \pm v \pmod{\mathbb{Z}^2}$, SnapPy hyperbolic 3-manifold topology/volume/systole checks, and exact unwrapped 1D Kaluza–Klein Schrödinger solver comparing twisted `(T)` vs. untwisted `(S1)` states across candidate histories, negative controls, bounded exhaustive families, and metallic siblings $m \in \{1, 2, 3, 4\}$.
- `src/phi_loop/sector3_weave_potential.py`: **Sector 3 (`BE-3`)** — Exact modular/Kronecker-limit & shifted-lattice 1-loop effective potentials $V_{\text{eff}}(\tau, w)$ for weave modules (`End ρ_Q`), the 248D $\mathfrak{e}_8$ `120_+ ⊕ 128_-` content, and torsion Wilson lines of orders $N \in \{1..6\}$.
- `src/phi_loop/sector4_chirality_hand.py`: **Sector 4 (`BE-4`)** — Explicit $248 \times 248$ $\mathfrak{e}_8$ adjoint construction, proof that $\dim Z_{\mathfrak{e}_8}(\mathfrak{u}(3)_{c,\text{EM}}) = 46$, exhaustive test of $(2,2)_{25}$ coset left-right weak splitting under $[\Phi, \Phi^\dagger] = 0$ with mandatory random Haar unitary basis-scrambling (`Guardrail 3`), and 4D conjugate-matter chiral index theorem.
- `src/phi_loop/composite_loop_engine.py`: Composite orchestrator verifying the SHA-256 pre-registration seal, running all four sectors, evaluating falsifiers `T0`–`T4`, and emitting `outputs/phi_loop_results.json`.
- `scripts/referee_phi_loop.py`: Independent zero-trust referee (`Guardrail 6`) with AST-enforced **zero imports** from `phi_loop`.
- `tests/test_phi_loop_suite.py`: Comprehensive `unittest` verification suite.

## Execution

```bash
PYTHONPATH=src python3 -m phi_loop.composite_loop_engine
python3 scripts/referee_phi_loop.py
PYTHONPATH=src python3 -m unittest discover -s tests -v
```
