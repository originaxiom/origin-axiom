"""CHECK 8 (agy Theorem 15 Part C docstring: 'the S^3-integrated quartic I_4(Phi) takes 5/4 on C_0 and 5/8 on C_L, C_R';
Theorem 14 relay section 2 item 7: g_L, g_R act on the three classes as 3-cycles and S = g_L g_R^-1 g_L as the
transposition fixing C_0).  Pure linear algebra; quartic Q(U, z) = |z|^4 + |z^dag conj(U) sx U^T z|^2 (derived and
checked on the D5 matrices in check 6).  The S^3 average by 200 000 Haar points (same points for every U) and exactly:
Q(U, z) = Q(1, U^T z) with U^T unitary, so the average cannot depend on U."""
import json, math, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
Fi = np.array([[1j, 0], [0, -1j]]); Fj = np.array([[0, 1], [-1, 0]], dtype=complex)
gL = (np.eye(2) + Fi) / math.sqrt(2); gR = (np.eye(2) - Fj) / math.sqrt(2); sx = np.array([[0, 1], [1, 0]], dtype=complex)
els = [np.eye(2, dtype=complex)]; fr = list(els)
while fr:
    nw = []
    for g in fr:
        for s in (gL, gR, gL.conj().T, gR.conj().T):
            p = g @ s
            if not any(np.allclose(p, h) for h in els): els.append(p); nw.append(p)
    fr = nw
St = [g for g in els if np.allclose(g.conj() @ sx @ g.T, sx) or np.allclose(g.conj() @ sx @ g.T, -sx)]
cos = [[g @ h for h in St] for g in (np.eye(2), gL, gR)]
cid = lambda g: next(i for i, cs in enumerate(cos) if any(np.allclose(g, c) for c in cs))
perm = lambda g: [cid(g @ cs[0]) for cs in cos]
S = gL @ np.linalg.inv(gR) @ gL
rng = np.random.default_rng(3); Z = rng.normal(size=(200000, 2)) + 1j * rng.normal(size=(200000, 2)); Z /= np.linalg.norm(Z, axis=1)[:, None]
def avg(U):
    M = U.conj() @ sx @ U.T; v = np.einsum('ni,ij,nj->n', Z.conj(), M, Z); return float(np.mean(1 + np.abs(v) ** 2))
avgs = sorted(set(round(avg(U), 6) for U in els))
out = {"perm_gL": perm(gL), "perm_gR": perm(gR), "perm_S": perm(S), "S3_average_values_over_48": avgs,
       "S3_average_exact_note": "mean of 1 + |z^dag sx z|^2 on S^3 = 1 + 1/3 (|z^dag sx z|^2 = 4 Re(z1 conj z2)^2, mean 1/3)"}
print(out); (HERE / "check8_s3_integral_and_cycles_out.json").write_text(json.dumps(out, indent=1))
