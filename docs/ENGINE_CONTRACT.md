# Origin Axiom Engine — Contract Specification (v1.0-draft)

## 0. Purpose

This document defines the **contractual behavior** of the `origin-axiom` engine.

The engine is a **reproducible toy-universe framework** implementing a
*non-cancelling scalar rule* and a **phenomenological mapping**
from microscopic residuals to effective cosmological observables.

This contract specifies:
- what the engine guarantees,
- what it explicitly does not claim,
- the invariants it enforces,
- and the conditions under which results are meaningful.

This document is normative.  
Anything not stated here is **out of scope**.

---

## 1. Conceptual Core

### 1.1 Origin Axiom (Operational Form)

The Origin Axiom is implemented as a **non-cancelling constraint** on a
complex scalar amplitude \( A \) defined over a discrete configuration space
(lattice, chain, or mode set).

Operationally:
- The system is forbidden from reaching a **globally cancelling state**
  where the total amplitude magnitude vanishes.
- When the unconstrained evolution approaches cancellation,
  a constraint is applied that enforces a minimal residual amplitude.

This is **not** a metaphysical claim.
It is a **dynamical rule** imposed on toy systems.

---

## 2. Engine Inputs

The engine accepts the following inputs:

### 2.1 Microphysical / Toy Inputs
- Lattice or chain size \( N \)
- Coupling parameters (e.g. nearest-neighbor coupling, nonlinear terms)
- Numerical parameters (time step, steps, tolerance \( \epsilon \))
- Initial conditions (coherent, random-phase, defected, etc.)
- Random seed (explicit or implicit)

### 2.2 Optional θ★ Parameter
- An external phase-like parameter \( \theta^\star \)
- Supplied via configuration (`theta_star_config.json`)
- Typically sourced from the `origin-axiom-theta-star` project

θ★ is treated as:
- an **external dial**
- not derived inside this engine
- optional (the engine can run θ★-agnostic)

---

## 3. Guaranteed Outputs

Given fixed inputs and a fixed random seed, the engine guarantees:

### 3.1 Deterministic Reproducibility
- Identical inputs → identical numerical outputs
- All canonical runs are reproducible by script + seed

### 3.2 Non-Cancellation Invariant
- The global scalar amplitude never reaches total cancellation
- A residual amplitude floor is enforced whenever needed

### 3.3 Residual Energy Measurement
- The engine computes a **residual energy density**
  associated with the enforced non-cancellation
- This residual can be measured as a function of θ★ (if supplied)

### 3.4 Effective Vacuum Mapping (Phenomenological)
- Residual micro-scale energy is mapped to an
  **effective vacuum energy density**
- This mapping is explicit, configurable, and documented
- It is **not derived from first principles**

### 3.5 FRW-Level Toy Cosmology
- The effective vacuum energy can be injected into
  a flat FRW background
- The engine computes:
  - scale factor evolution
  - age of the universe
  - deceleration parameter
  - distance measures
  - linear growth proxies

These outputs are **toy observables**.

---

## 4. What the Engine Does NOT Claim

The engine explicitly does **not**:

- derive the absolute value of the cosmological constant
- solve the cosmological constant problem
- replace ΛCDM
- perform precision cosmology
- claim uniqueness or necessity of θ★
- assert observational agreement beyond controlled toy comparisons

Any such interpretation is out of contract.

---

## 5. Invariants

The following must always hold in canonical runs:

1. **Non-Cancellation Invariant**
   - Global cancellation is forbidden by construction

2. **Deterministic Evolution**
   - No hidden randomness beyond declared seeds

3. **Explicit Mapping**
   - All mappings between micro → macro are visible and logged

4. **No Silent Calibration**
   - Any scaling or normalization is explicit in code and metadata

---

## 6. Known Failure / Inactive Regimes

The engine behavior is known to change when:

- Initial conditions are already far from cancellation
- The constraint never activates (coherent configurations)
- Nonlinear terms dominate dynamics
- Phenomenological FRW mapping is altered

These regimes are documented and not considered bugs.

---

## 7. Scope Boundary

This engine is intended as:
- a **scientifically honest scaffold**
- a **falsifiable toy framework**
- a **platform for further Acts**

Future Acts may extend or replace components,
but this contract defines **v1.0 meaning**.