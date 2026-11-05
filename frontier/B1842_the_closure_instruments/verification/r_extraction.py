"""P-688 (draft): THE r EXTRACTION AND THE UNREAD COMMITMENT — data-free.

r = Δm²₂₁ / Δm²₃₁ from the Dirac neutrino Yukawa (masses ∝ its singular values, ascending m1 <= m2 <= m3: the frame's
own ordering, no relabel by data). The card computes r at the frozen row and NEVER prints it: commit_unread() writes the
value with a random salt to a file and prints only sha256(salt || repr(value)); the salt stays in the file, so the seal is
hiding (a rounded guess cannot be confirmed from the hash) and binding.

Control C-X (planted, run here): Y = U diag(m) V† with U, V seeded Haar unitaries and planted m (never measured values);
the pipeline must recover r to 1e-8 relative (the m2² − m1² cancellation bounds it for nearly degenerate planted masses), and
be invariant under the left/right rotations and an overall scale.
    python3 -B r_extraction.py        -> prints the control's deviations only"""
import json, hashlib, secrets, pathlib
import numpy as np


def r_of(Y):
    m = np.sort(np.linalg.svd(Y, compute_uv=False)); m2 = m ** 2
    return float((m2[1] - m2[0]) / (m2[2] - m2[0]))


def commit_unread(value, path, label):
    """write the value + a fresh salt to `path` (never printed); return the commitment hash"""
    salt = secrets.token_hex(32); body = repr(float(value))
    h = hashlib.sha256((salt + "|" + body).encode()).hexdigest()
    pathlib.Path(path).write_text(json.dumps({"label": label, "salt": salt, "value": body, "commitment": h}), encoding="utf-8")
    return h


def haar(n, rng):
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2)
    q, r = np.linalg.qr(z); d = np.diag(r); return q * (d / np.abs(d))


def control():
    rng = np.random.default_rng(16881); worst = worst_inv = 0.0
    for _ in range(20000):
        m = np.sort(10 ** rng.uniform(-4, 0, 3))                      # planted, log-uniform; never a measured value
        r_true = (m[1] ** 2 - m[0] ** 2) / (m[2] ** 2 - m[0] ** 2)
        Y = haar(3, rng) @ np.diag(m) @ haar(3, rng).conj().T
        worst = max(worst, abs(r_of(Y) / r_true - 1) if r_true > 1e-300 else 0.0)
        worst_inv = max(worst_inv, abs(r_of(7.3 * haar(3, rng) @ Y @ haar(3, rng)) / r_of(Y) - 1))
    print("C-X (r from planted singular values, 20 000 Haar draws): max rel dev %.1e; invariance under rotations and scale %.1e -> %s"
          % (worst, worst_inv, "HOLDS" if worst < 1e-8 and worst_inv < 1e-8 else "FAILS"))


if __name__ == "__main__":
    control()
