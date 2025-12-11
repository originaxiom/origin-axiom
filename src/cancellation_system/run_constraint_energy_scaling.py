"""
Experiment: Energy-scaling test for the non-cancelling constraint.

Goal:
    - Same initial condition, different constraint strengths / tolerances.
    - Measure:
        * total energy vs time,
        * long-time averages,
        * any systematic drift as constraint is tightened/loosened.

This is a placeholder. Next step:
    - Import the core scalar-universe integrator from src/ (once we settle on the
      canonical implementation),
    - Expose a CLI to sweep over a "constraint parameter",
    - Save outputs into data/processed/cancellation_system/energy_scaling/.
"""
if __name__ == "__main__":
    raise SystemExit("TODO: implement run_constraint_energy_scaling.py")
