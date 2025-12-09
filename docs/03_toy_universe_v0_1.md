# Toy Universe v0.1: Non-Cancelling Scalar on a Discrete 3-Torus

To test the Origin Axiom in a controlled setting, we construct a minimal “toy universe” in which the non-cancelling phase twist is implemented explicitly and its dynamical consequences can be studied numerically. The goal is **not** to reproduce our universe in detail, but to create a simple, well-defined model that:

- respects locality and approximate homogeneity,
- admits nontrivial structure and dynamics,
- incorporates the axiom as a global constraint on allowed configurations.

---

## 1. Microstructure: Discrete 3-Torus

We model space as a finite 3D cubic lattice with periodic boundary conditions (a discrete 3-torus). Sites are labeled by integer triples
\[
\mathbf{n} = (n_x, n_y, n_z), \quad n_i \in \{0,\dots,N_i - 1\},
\]
with identifications \(n_i \equiv n_i + N_i\).

Each site has six nearest neighbors:
\[
\mathcal{N}(\mathbf{n}) = \{\mathbf{n} \pm \hat{x},\ \mathbf{n} \pm \hat{y},\ \mathbf{n} \pm \hat{z}\},
\]
where unit vectors denote shifts along each axis with wrapping at boundaries.

Properties:

- **Locality:** nearest-neighbor interactions only.
- **Approximate homogeneity & isotropy:** translational invariance, cubic symmetry.
- **Topological closure:** compact space without edges.
- **Computational simplicity:** discrete Laplacians and updates are straightforward.

---

## 2. Field Content: Complex Scalar Φ

At each site \(\mathbf{n}\) and time \(t\) we place a complex scalar:
\[
\Phi_{\mathbf{n}}(t) \in \mathbb{C}, \quad \Phi_{\mathbf{n}} = R_{\mathbf{n}} e^{i\varphi_{\mathbf{n}}}.
\]

Interpretation:

- Real / imaginary parts (or amplitude/phase) form a yin–yang pair: two interpenetrating components that **flow into** each other rather than annihilating.
- A single scalar is the minimal field content capable of carrying a global phase and interference.

Gauge fields, spin, multiple species are absent at this stage; they are expected, if at all, as **emergent effective structures** later.

---

## 3. Local Dynamics: Wave-Like Evolution

We use a discrete analogue of a nonlinear Klein–Gordon equation:
\[
\frac{d^2 \Phi_{\mathbf{n}}}{dt^2}
= c^2\, \Delta \Phi_{\mathbf{n}}
- m^2\, \Phi_{\mathbf{n}}
- \lambda\, |\Phi_{\mathbf{n}}|^2 \Phi_{\mathbf{n}},
\]
where the discrete Laplacian is
\[
\Delta \Phi_{\mathbf{n}}
= \sum_{\mathbf{m} \in \mathcal{N}(\mathbf{n})} \big(\Phi_{\mathbf{m}} - \Phi_{\mathbf{n}}\big).
\]

Parameters:

- \(c\): effective propagation speed  
- \(m\): mass-like parameter  
- \(\lambda\): strength of local nonlinearity

This choice yields:

- finite-speed propagation,
- interference and wave behavior,
- potential for localized, stable structures due to nonlinearity.

A discrete action or Hamiltonian \(H[\Phi,\dot{\Phi}]\) can be defined, but for v0.1 we focus on the equations of motion and simulation.

---

## 4. Global Amplitude and the Non-Cancelling Constraint

Define a global complex amplitude:
\[
A(t) = \sum_{\mathbf{n}} \Phi_{\mathbf{n}}(t).
\]

Without extra constraints, dynamics might drive the system toward a configuration where \(A(t)\) lies on a “cancelling manifold” (loosely, where the universe cancels itself in a global plus-minus match). The Origin Axiom forbids such states.

We therefore impose:

> **Constraint:** Physical trajectories must avoid a small neighborhood \(\mathcal{F}_{\theta_*}\) of a forbidden configuration \(A_*(\theta_*)\) in the complex plane.

We explore two implementations:

### 4.1 Hard Constraint (State Exclusion)

Define a forbidden set:
\[
\mathcal{F}_{\theta_*} = \{A \in \mathbb{C} : |A - A_*(\theta_*)| < \epsilon\},
\]
with small \(\epsilon\).

Physical trajectories satisfy:
\[
A(t) \notin \mathcal{F}_{\theta_*} \quad \forall t.
\]

In simulations, proposed updates that would place \(A(t+\delta t)\) in \(\mathcal{F}_{\theta_*}\) are rejected or modified (reflected), forcing the system to “skirt around” the cancelling configuration.

### 4.2 Soft Constraint (Holonomy Potential)

Add an axiom-induced potential to the action:
\[
S_{\text{ax}}[\Phi] = \int dt\, V_{\text{ax}}(A(t)),
\]
with
\[
V_{\text{ax}}(A) = \frac{\mu^4}{\big|A - A_*(\theta_*)\big|^p},
\]
for some \(p > 0\), scale \(\mu\), and forbidden configuration \(A_*(\theta_*)\).

As \(A \to A_*(\theta_*)\), \(V_{\text{ax}}\) blows up; the dynamics are repelled from the cancelling manifold. The configuration space has a **“hole”** corresponding to perfect cancellation; trajectories loop around it instead of through it.

---

## 5. θ\* as a Free Parameter and Observables

In v0.1, θ\* is treated as a **free parameter**. For each θ\* and parameter set \((c,m,\lambda)\), we can:

- Evolve Φ from random or structured initial conditions.
- Measure:
  - time-averaged residual \(\langle |A(t)| \rangle\),
  - spectra of fluctuations of Φ,
  - existence and stability of localized “particle-like” structures,
  - entropy-like measures (e.g. distribution of \(|\Phi|^2\), phase coherence).

We then ask:

- Does the system avoid trivial behavior (frozen or explosive)?
- Does it support long-lived, structured configurations?
- Does it exhibit an emergent arrow of time driven by the axiom-induced constraint?

The **selection problem for θ\*** becomes:

> Among all θ\* values, which yield dynamically rich, structured “worlds” rather than pathological or sterile ones?

Later, “universe-like” can be refined to include quantitative matches to specific physical scales and phenomena. At v0.1, the goal is **qualitative viability** of non-cancelling existence on a simple lattice.

