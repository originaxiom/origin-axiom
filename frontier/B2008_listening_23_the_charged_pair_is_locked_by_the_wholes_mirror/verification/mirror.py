"""B2008, listening card 23 (main, 2026-11-26; data-free): the swap tau = (x,y,z) -> (y,x,z).
P1 (sympy): tau C tau = C^-1, tau sigma tau = sigma, tau permutes the six moves. P2 (numpy): at each level tau preserves the
orbit, [P_tau, W] = 0, P_tau Pi_1 = Pi_2 P_tau. Writes mirror_perms.json for P3 (GAP, mirror_gap.py).
    python3 -B mirror.py > mirror_run.txt"""
import contextlib, io, json, pathlib
import numpy as np, sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
x, y, z = sp.symbols("x y z")
def comp(f, g): return tuple(sp.expand(e.subs({x: g[0], y: g[1], z: g[2]}, simultaneous=True)) for e in f)
I = (x, y, z); C = (y, z, x); Ci = (z, x, y); T = (y, x, z)
L = (x, z, x*z - y); R = (z, y, y*z - x); Li = (x, x*y - z, y); Ri = (x*y - z, y, x)
X = comp(C, comp(L, Ci)); Xi = comp(Ci, comp(R, C)); S = comp(R, Ci)
six = {"L": L, "R": R, "L^-1": Li, "R^-1": Ri, "X": X, "X^-1": Xi}
img = {}
for k, m in six.items():
    tm = comp(T, comp(m, T)); img[k] = next((kk for kk, mm in six.items() if mm == tm), None)
print("P1 (sympy): tau C tau = C^-1: %s; tau sigma tau = sigma: %s; tau m tau for the six moves: %s; all among the six: %s" % (
    comp(T, comp(C, T)) == Ci, comp(T, comp(S, T)) == S, img, all(v is not None for v in img.values())))
src = (HERE.parent.parent / "B2004_listening_19_the_mechanism_of_the_halving_the_modular_group_and_its_order_six_character" / "verification" / "mechanism.py").read_text().split("WORDS = words(10)")[0]
ns = {"__file__": str(HERE / "mirror.py")}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(src, "b2004_head", "exec"), ns)
out = {}
for N, start, lab in ((27, (3, 3, 3), "mod 27"), (81, (3, 3, 3), "mod 81"), (243, (3, 3, 3), "mod 243"), (5, None, "leaf mod 5"), (7, None, "leaf mod 7")):
    pts, idx, pC, pS, moves = ns["orbit"](N, start); n = len(pts)
    pres = all((v[1], v[0], v[2]) in idx for v in pts)
    pT = np.array([idx[(v[1], v[0], v[2])] for v in pts]) if pres else None
    if pres:
        from scipy.sparse import csr_matrix
        Pm = lambda p: csr_matrix((np.ones(n), (p, np.arange(n))), shape=(n, n))
        PC, PS, PT = Pm(pC), Pm(pS), Pm(pT); PCi = PC.T.tocsr()
        W = PS @ PC + PCi @ PS + PS @ PC @ PC + PC @ PS + PC @ PS @ PC + PCi @ PS @ PCi
        comm = abs(PT @ W - W @ PT).max()
        w = np.exp(2j * np.pi / 3); Id = csr_matrix(np.eye(n)) if n <= 6000 else None
        Pi = lambda q: (Id + (w ** (-q)) * PC + (w ** (-2 * q)) * (PC @ PC)) / 3
        exch = abs(PT @ Pi(1) - Pi(2) @ PT).max()
        print("P2 (%s, %d points): tau preserves the orbit: %s; [P_tau, W] = %s; |P_tau Pi_1 - Pi_2 P_tau| = %.1e; tau is an involution: %s" % (
            lab, n, pres, comm, exch, bool(np.all(pT[pT] == np.arange(n)))), flush=True)
        if start is not None: out[lab] = {"C": [int(i) for i in pC], "S": [int(i) for i in pS], "T": [int(i) for i in pT]}
    else:
        print("P2 (%s): tau preserves the orbit: False" % lab)
(HERE / "mirror_perms.json").write_text(json.dumps(out))
