"""CHECK 10 (agy Theorem 15 Part C / relay Stage 1: w_LR = exp(i pi sx/4) lies in the stabiliser, fixes C_0 and exchanges
C_L <-> C_R).  Both conventions: the lane's T15 matrices M = U^dag sx U (w^dag M_L w = M_R) and the class action on the
left cosets U St (the action that check 8 used)."""
import json, math, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
Fi = np.array([[1j, 0], [0, -1j]]); Fj = np.array([[0, 1], [-1, 0]], dtype=complex); sx = np.array([[0, 1], [1, 0]], dtype=complex)
gL = (np.eye(2) + Fi) / math.sqrt(2); gR = (np.eye(2) - Fj) / math.sqrt(2); w = (np.eye(2) + 1j * sx) / math.sqrt(2)
ML, MR = gL.conj().T @ sx @ gL, gR.conj().T @ sx @ gR
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
out = {"w_in_St": any(np.allclose(w, h) for h in St),
       "T15_convention_w^dag_sx_w_eq_sx": bool(np.allclose(w.conj().T @ sx @ w, sx)),
       "T15_convention_w^dag_ML_w_minus_MR": float(np.abs(w.conj().T @ ML @ w - MR).max()),
       "T15_convention_w^dag_ML_w_plus_MR": float(np.abs(w.conj().T @ ML @ w + MR).max()),
       "left_coset_action_of_w": [cid(w @ cs[0]) for cs in cos]}
print(out); (HERE / "check10_wLR_out.json").write_text(json.dumps(out, indent=1))
