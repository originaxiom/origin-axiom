"""B1953's exact facts on level 5's Weil space (no frame, no data)."""
import itertools
import numpy as np
z = np.exp(2j * np.pi / 5); psi = lambda x: z ** (x % 5)
X = np.roll(np.eye(5), 1, axis=0).astype(complex); Z = np.diag([psi(x) for x in range(5)])
P = np.array([[1.0 if (x + y) % 5 == 0 else 0.0 for y in range(5)] for x in range(5)])
D = lambda a, b: psi(3 * a * b) * np.linalg.matrix_power(X, a % 5) @ np.linalg.matrix_power(Z, b % 5)
V = [(a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0)]
SIXY = {"Q": 1, "u": -4, "e": 6, "d": 2, "L": -3, "H": 3, "singlet": 0}; DEG = {"Q": 2, "u": 2, "e": 2, "d": 4, "L": 4, "H": 1, "singlet": 0}


def facts():
    T5 = np.diag([psi(2 * x * x) for x in range(5)]); F5 = np.array([[psi(x * y) for y in range(5)] for x in range(5)]) / np.sqrt(5)
    G = np.array([[abs(np.trace(D(*v).conj().T @ D(*w))) / 5 for w in V] for v in V])
    S = sum(D(*v) for v in V); Y6 = (np.eye(5) - 5 * P) / 2
    return {
        "twist_is_the_degree": all(SIXY[f] % 5 == (3 * DEG[f]) % 5 for f in SIXY),
        "basis_of_sl5": float(max(np.abs(G - np.eye(24)).max(), max(abs(np.trace(D(*v))) for v in V))),
        "parity_reverses_the_label": float(max(np.abs(P @ D(*v) @ P - D(-v[0], -v[1])).max() for v in V)),
        "even_combinations_commuting_with_the_parity": sum(1 for v in V if np.abs(P @ (D(*v) + D(-v[0], -v[1])) - (D(*v) + D(-v[0], -v[1])) @ P).max() < 1e-12) // 2,
        "trace_against_the_parity": float(max(abs(np.trace(D(*v) @ P) - 1) for v in V)),
        "hypercharge_is_the_sum": float(np.abs(Y6 + S / 2).max()),
        "weil_T_no_phases": float(max(np.abs(T5 @ D(a, b) @ T5.conj().T - D(a, b - a)).max() for a, b in V)),
        "weil_S_no_phases": float(max(np.abs(F5 @ D(a, b) @ F5.conj().T - D(-b, a)).max() for a, b in V)),
    }


if __name__ == "__main__":
    f = facts()
    print("1. 6Y = 3k mod 5 for every field of exterior degree k: %s" % f["twist_is_the_degree"])
    print("2. the 24 operators D(v) = zeta^(ab/2) X^a Z^b: an orthonormal traceless basis of sl(5) (%.1e); P D(v) P = D(-v) (%.1e); %d even combinations commute with P" % (f["basis_of_sl5"], f["parity_reverses_the_label"], f["even_combinations_commuting_with_the_parity"]))
    print("3. tr(D(v) P) = 1 for every v (%.1e);  6Y = -(1/2) the sum of the 24 (%.1e)" % (f["trace_against_the_parity"], f["hypercharge_is_the_sum"]))
    print("4. rho(T) D(a, b) rho(T)^-1 = D(a, b - a) (%.1e); rho(S) D(a, b) rho(S)^-1 = D(-b, a) (%.1e): no phases" % (f["weil_T_no_phases"], f["weil_S_no_phases"]))
