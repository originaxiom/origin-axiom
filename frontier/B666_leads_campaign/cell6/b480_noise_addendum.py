"""CELL 6 / B480 addendum: show the RAW-FLOAT <r> on the exactly-degenerate
spectrum is an EIGENSOLVER-NOISE ARTIFACT, not a statistic -- i.e. any number in
a wide band (including the banked 0.16) can be produced by an equally 'valid'
run on different noise. Method: same exact validated U; break the exact
degeneracies with random unitary-conjugations (spectrum IDENTICAL in exact
arithmetic; only the float noise realization changes) and with tiny Hermitian
perturbations at the scale of eigensolver error (1e-10..1e-6), and watch <r>.
"""
import numpy as np
from b480_rederive import quantize_exact, raw_r_stat, A

rng = np.random.default_rng(1)

for N in (181, 301):
    U = quantize_exact(A, N)
    base = raw_r_stat(np.angle(np.linalg.eigvals(U)))
    print(f"N={N}: base RAW-FLOAT <r> = {base:.4f}")
    # same spectrum, different noise realizations (random unitary conjugation)
    vals = []
    for trial in range(6):
        Z = rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N))
        Q, _ = np.linalg.qr(Z)
        Uc = Q @ U @ Q.conj().T          # exactly the same spectrum
        vals.append(raw_r_stat(np.angle(np.linalg.eigvals(Uc))))
    print(f"  6 unitary-conjugated runs (identical exact spectrum): "
          f"{['%.4f' % v for v in vals]}")
    # tiny Hermitian phase perturbations at plausible solver-noise scales
    for eps in (1e-10, 1e-8, 1e-6):
        H = rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N))
        H = (H + H.conj().T)/2
        Up = U @ (np.eye(N) + 1j*eps*H)  # ~unitary to O(eps^2)
        v = raw_r_stat(np.angle(np.linalg.eigvals(Up)))
        print(f"  degeneracy broken at scale {eps:.0e}: <r> = {v:.4f}")
print("\nConclusion: RAW-FLOAT <r> on this exactly-degenerate spectrum wanders "
      "with the noise realization -- it is not a well-defined observable.")
