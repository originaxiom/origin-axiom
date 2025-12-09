# Toy Universe v0.1: Non-Cancelling Scalar on a Discrete 3-Torus

To test the Origin Axiom in a controlled setting, we construct a minimal “toy universe” in which the non-cancelling phase twist is implemented explicitly and its dynamical consequences can be studied numerically.

The goal is **not** to reproduce our universe in detail, but to create a simple, well-defined model that:

- respects locality and approximate homogeneity,
- admits nontrivial structure and dynamics,
- incorporates the axiom as a global constraint on allowed configurations.

---

## 1. Microstructure: Discrete 3-Torus

We model space as a finite 3D cubic lattice with periodic boundary conditions (a discrete 3-torus). Sites are labeled by integer triples
$\mathbf{n} = (n_x, n_y, n_z)$
with $n_i \in \{0,\dots,N_i - 1\}$ and identifications $n_i \equiv n_i + N_i$.

Each site has six nearest neighbors,
$\mathcal{N}(\mathbf{n}) = \{\mathbf{n} \pm \hat{x},\ \mathbf{n} \pm \hat{y},\ \mathbf{n} \pm \hat{z}\}$,
where unit vectors denote shifts along each axis with wrapping at boundaries.

Properties:

- **Locality:** nearest-neighbor interactions only.  
- **Approximate homogeneity \& isotropy:** translational invariance, cubic symmetry.  
- **Topological closure:** compact space without edges (periodic boundaries).  
- **Computational simplicity:** discrete Laplacians and updates are straightforward.

---

## 2. Field Content: Complex Scalar $\Phi$

At each site $\mathbf{n}$ and time $t$ we place a complex scalar
$\Phi_{\mathbf{n}}(t) \in \mathbb{C}$,
which we can write as
$\Phi_{\mathbf{n}} = R_{\mathbf{n}} e^{i\varphi_{\mathbf{n}}}$.

Interpretation:

- Real/imaginary parts (or amplitude/phase) form a yin–yang pair: two interpenetrating components that **flow into** each other rather than annihilating.  
- A single complex scalar is the minimal field content capable of carrying a global phase and interference.

Gauge fields, spin, and multiple species are absent at this stage; they are expected, if at all, as **emergent effective structures** in later, richer models.

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

- $c$ – effective propagation speed  
- $m$ – mass-like parameter  
- $\lambda$ – strength of local nonlinearity

This choice yields:

- finite-speed propagation,  
- interference and wave behavior,  
- potential for localized, stable structures due to nonlinearity.

A discrete action or Hamiltonian $H[\Phi,\dot{\Phi}]$ consistent with this equation can be written down. In practice we implement the dynamics as a leapfrog time integration in code and use the corresponding discrete **energy functional** as a diagnostic.

---

## 4. Global Amplitude and the Non-Cancelling Constraint

Define a global complex amplitude:
\[
A(t) = \sum_{\mathbf{n}} \Phi_{\mathbf{n}}(t).
\]

Without extra constraints, the dynamics might drive the system toward a configuration where $A(t)$ lies on a “cancelling manifold” (loosely, where the universe cancels itself in a global plus-minus match). The Origin Axiom forbids such states.

We therefore impose:

> **Constraint:** Physical trajectories must avoid a small neighborhood $\mathcal{F}_{\theta_\*}$ of a forbidden configuration $A_\*(\theta_\*)$ in the complex plane.

In Toy Universe v0.1 we mainly study a simple choice where the forbidden configuration is **global cancellation** $A \approx 0$ (with a phase structure encoded in $\theta_\*$). We implement this via a **hard constraint**:

- Define
  $\mathcal{F}_{\theta_\*} = \{A \in \mathbb{C} : |A - A_\*(\theta_\*)| < \epsilon\}$  
  with some small $\epsilon$.
- During time evolution, if a proposed update would send $A(t)$ into $\mathcal{F}_{\theta_\*}$, we modify the field (e.g. by a small global rescaling) so that the new $A(t)$ lies just outside the forbidden region.

In code, this is realised by a constraint function that is called after each free leapfrog step and applies a simple “push” away from the cancelling manifold.

---

## 5. Diagnostics: Energy and Global Amplitude

To monitor the behaviour of the toy universe, we track:

- the global amplitude magnitude $|A(t)|$, and  
- a discrete energy functional
  \[
  E = \sum_{\mathbf{n}} \left[
    \tfrac12 |\dot{\Phi}_{\mathbf{n}}|^2
    + \frac{c^2}{2} \sum_{\mathbf{m}\in\mathcal{N}(\mathbf{n})} |\Phi_{\mathbf{m}} - \Phi_{\mathbf{n}}|^2
    + \tfrac{m^2}{2} |\Phi_{\mathbf{n}}|^2
    + \tfrac{\lambda}{4} |\Phi_{\mathbf{n}}|^4
  \right].
  \]

Numerically:

- Without the axiom constraint, $E(t)$ is approximately conserved (up to integration error), providing a sanity check on the implementation.  
- With the constraint turned on, the system is gently repelled from global cancellation while still exhibiting wave-like dynamics. We can then compare $|A(t)|$ and $E(t)$ with and without the constraint.

Simulation outputs are stored in `data/processed/` as `.npz` files and explored in analysis scripts / notebooks.

---

## 6. Role of this Toy Universe

Toy Universe v0.1 is deliberately simple. It is **not** meant to be a realistic cosmology. Its role is to provide:

- a concrete microstructure (discrete 3-torus),  
- a clear field content (one complex scalar),  
- explicit dynamics (discrete nonlinear Klein–Gordon),  
- and a first implementation of the Origin Axiom as a global constraint.

From here we can:

- vary $\theta_\*$ and see which choices yield rich, stable dynamics,  
- explore alternative microstructures (1D chains, hexagonal lattices, random graphs),  
- and refine how the axiom is encoded (e.g. via an explicit term in the action).

This forms the experimental backbone for later, more sophisticated models that attempt closer contact with cosmology and quantum field theory.
