"""main's independent check of the SM seat's joint p_V (§352 2a): own implementation, own seed, own sizes, plus a
three-target case and a strongly correlated case; under exchangeability the joint p must be uniform."""
import numpy as np
def joint_p(D):            # D: (N+1, T) distances; row 0 is the 'data'
    N1, T = D.shape
    # marginal p of each row among all N+1 rows (ties against the row): (#{rows with D <= own}) / (N+1)
    P = np.empty_like(D)
    for t in range(T):
        s = np.sort(D[:, t]); P[:, t] = np.searchsorted(s, D[:, t], side="right") / N1
    S = np.prod(P, axis=1)
    return np.sum(S <= S[0]) / N1          # rank of the data's product among all N+1 (data counted)
rng = np.random.default_rng(20261105)
for name, T, rho, N, R in (("2 targets, independent", 2, 0.0, 1500, 6000), ("2 targets, rho 0.9", 2, 0.9, 1500, 6000),
                           ("3 targets, rho 0.5", 3, 0.5, 1500, 4000)):
    C = np.full((T, T), rho) + (1 - rho) * np.eye(T)
    ps = np.array([joint_p(np.abs(rng.multivariate_normal(np.zeros(T), C, size=N + 1))) for _ in range(R)])
    se = lambda a: np.sqrt(a * (1 - a) / R)
    print("%-24s rate at 0.01: %.4f (±%.4f)   at 0.05: %.4f (±%.4f)" % (name, (ps <= 0.01).mean(), se(0.01), (ps <= 0.05).mean(), se(0.05)))
