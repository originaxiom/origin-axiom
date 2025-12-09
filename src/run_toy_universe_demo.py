import numpy as np
from toy_universe_lattice import ScalarToyUniverse

def main():
    # small lattice to start
    uni = ScalarToyUniverse(nx=16, ny=16, nz=16, c=1.0, m=0.1, lam=0.0, dt=0.01)

    # random tiny complex noise as initial condition
    rng = np.random.default_rng(42)
    phi0 = 1e-3 * (rng.standard_normal(uni.lat.shape) + 1j * rng.standard_normal(uni.lat.shape))
    uni.set_initial_conditions(phi0)

    print("Initial global amplitude:", uni.global_amplitude())

    steps = 100
    for i in range(steps):
        uni.step()  # no constraint yet
        if (i + 1) % 20 == 0:
            print(f"Step {i+1:4d}: |A| = {abs(uni.global_amplitude()):.5e}")

if __name__ == "__main__":
    main()
