"""B1957: the web seat's W-F13, section 1 (the algebra of the Higgs's two readings), checked by main.  Data-free.
i = diag(i, -i), j = [[0, 1], [-1, 0]], k = ij.  S = a_i i + a_j j + a_k k with complex coefficients; S~ = j S* j^T.
 H1  i* = -i, j* = j, k* = -k; conjugation by j sends i, j, k to -i, j, -k; so S~ = a_i* i + a_j* j + a_k* k.
 H2  for U in SU(2): (U S U^-1)~ = U S~ U^-1 (the two readings transform alike), on 200 random cases.
 H3  (e^(i theta) S)~ = e^(-i theta) S~ (opposite phase); and a control: S~ is not S for a non-real coefficient."""
import numpy as np
rng = np.random.default_rng(13)
qi, qj = np.array([[1j, 0], [0, -1j]]), np.array([[0, 1], [-1, 0]], complex); qk = qi @ qj
tilde = lambda S: qj @ S.conj() @ qj.T
if __name__ == "__main__":
    print("H1: i* = -i: %s; j* = j: %s; k* = -k: %s; j i j^-1 = -i: %s; j k j^-1 = -k: %s; j^T = j^-1: %s" % (np.allclose(qi.conj(), -qi), np.allclose(qj.conj(), qj), np.allclose(qk.conj(), -qk), np.allclose(qj @ qi @ np.linalg.inv(qj), -qi), np.allclose(qj @ qk @ np.linalg.inv(qj), -qk), np.allclose(qj.T, np.linalg.inv(qj))))
    w1 = w2 = w3 = 0.0
    for _ in range(200):
        a = rng.normal(size=3) + 1j * rng.normal(size=3); S = a[0] * qi + a[1] * qj + a[2] * qk; St = tilde(S)
        w1 = max(w1, np.abs(St - (a[0].conj() * qi + a[1].conj() * qj + a[2].conj() * qk)).max())
        v = rng.normal(size=4); v /= np.linalg.norm(v); U = v[0] * np.eye(2) + v[1] * qi + v[2] * qj + v[3] * qk
        w2 = max(w2, np.abs(tilde(U @ S @ np.linalg.inv(U)) - U @ St @ np.linalg.inv(U)).max()); th = rng.uniform(0, 6.28); w3 = max(w3, np.abs(tilde(np.exp(1j * th) * S) - np.exp(-1j * th) * St).max())
    print("H1: |S~ - (a_i* i + a_j* j + a_k* k)| over 200 random S: %.1e | H2: |(U S U^-1)~ - U S~ U^-1|: %.1e | H3: |(e^(i theta) S)~ - e^(-i theta) S~|: %.1e; control, |S~ - S| on the last S: %.2f" % (w1, w2, w3, np.abs(St - S).max()))
