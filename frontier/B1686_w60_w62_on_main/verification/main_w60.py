"""P-222, part 1: the SM seat's W60 (the quark sector with a Wilson line) checked by main's own code, written from
W60_RULE.md and the seat's recorded read-out, not from its script.

    python3 main_w60.py spectra [--workers 8]   # the eigenvalues (cached in spectra_w60/)
    python3 main_w60.py read                    # the cells, from the cache, into main_w60.json

Units: W60's torus has periods 1 and omega (area A = sqrt(3)/2) and spacing h = 1/N, so H_W60 = N^2 H_unit. The
potentials are heat-trace differences against a reference with t0 = 30/lambda_K (lambda_K of the reference at that N):
  two dimensions:  Delta log det(phi) = - int_{t0}^inf Delta K(t) dt / t      = - sum [E1(lambda(phi) t0) - E1(lambda(ref) t0)]
  six dimensions:  Delta V6(phi)     = - int_{t0}^inf Delta K(t) t^{-3} dt    = - sum [I(lambda(phi)) - I(lambda(ref))],
                   I(l) = l^2 Gamma(-2, l t0)
A boson's potential is +1/2 Delta log det (2d) and Delta V6 (6d); a fermion's has both signs reversed."""
import json, os, sys, math, itertools
import numpy as np
from scipy.special import exp1

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
CACHE = os.path.join(HERE, "spectra_w60")
A = math.sqrt(3) / 2
OMEGA = complex(-0.5, math.sqrt(3) / 2)
# K: the rule's 300 is far above what the cutoff needs (t0 = 30/lambda_K keeps the neglected short-time part below e^-36 at
# K = 150); main uses K = 150 and checks K-independence against three K = 300 spectra kept in spectra_w60_K300/
K_MATTER, K_AB = 150, 300
SPECIAL = [(0, 0), (0.25, 0), (0, 0.25), (0.25, 0.25), (1 / 6, 1 / 6), (1 / 3, 1 / 3)]
GRID = [(a / 24, b / 24) for a in range(12) for b in range(12)]
CONTROL = [(0.25, 0), (0.5, 0), (1 / 3, 1 / 3), (0.1, 0.37), (0.4, 0.15)]
AB_REF = (0.5, 0.5)
P2_POINTS = [(0.13, 0.31), (0.07, 0.42), (0.21, 0.05)]


def _canon(a, b):
    """the representative of the 1/24-grid point (a, b) (integers mod 12) under the exact symmetries: period 1/2,
    phi -> -phi, and the order-3 rotation phi -> (phi2, -phi1 - phi2) (verified exactly on the lattice at small N)"""
    orb = set(); todo = [(a % 12, b % 12)]
    while todo:
        x = todo.pop()
        if x in orb: continue
        orb.add(x); u, v = x
        todo += [((-u) % 12, (-v) % 12), (v % 12, (-u - v) % 12)]
    return min(orb)


def grid_representatives():
    return sorted({_canon(a, b) for a in range(12) for b in range(12)}) and [(a / 24, b / 24) for a, b in sorted({_canon(a, b) for a in range(12) for b in range(12)})]
PAR = [(0.5, 0.0), (0.0, 0.5), (0.5, 0.5)]
# the stated content (W60's read-out): quarks, 3 generations x (Q 6, u^c 3, d^c 3) states, each a complex fermion in
# rho_Q (x) L, charges (units of 6Y) 1, -4, 2; weight -2 per state; the Higgs, a complex doublet in the three parity
# sectors jointly, charge 3, +2 per parity sector
QUARKS = [("Q", 1, 3 * 6), ("u^c", -4, 3 * 3), ("d^c", 2, 3 * 3)]


def key(N, phi, rank):
    return os.path.join(CACHE, "N%d_r%d_K%d_%.10f_%.10f.npy" % (N, rank, K_MATTER, phi[0] % 1.0, phi[1] % 1.0))


def tasks():
    T = []
    for phi in SPECIAL: T += [(96, phi, 2), (192, phi, 2)]
    for phi in grid_representatives(): T.append((96, phi, 2))
    for phi in P2_POINTS:                                    # direct checks of the symmetries at N = 96
        for img in (phi, (phi[0] + 0.5, phi[1]), (-phi[0], -phi[1]), (phi[1], -phi[0] - phi[1])):
            T.append((96, (img[0] % 1.0, img[1] % 1.0), 2))
    # the content's lines, directly (not from the interpolant): w0, the Higgs's lines, the 2-torsion lines
    for w in [(1 / 3, 1 / 3), (1 / 9, 1 / 9), (2 / 9, 2 / 9)]:
        for _, q, _n in QUARKS:
            phi = ((q * w[0]) % 1.0, (q * w[1]) % 1.0)
            T += [(96, phi, 2), (192, phi, 2)]
    seen = set(); out = []
    for t in T:
        k = key(*t)
        if k not in seen: seen.add(k); out.append(t)
    return out


def solve(task):
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    from lattice import Torus, lowest
    N, phi, rank = task
    path = key(N, phi, rank)
    if os.path.exists(path): return path
    T = Torus((N, 0), (0, N))
    H = T.operator(phi, rank=rank) * N ** 2
    w = lowest(H, K_MATTER if rank == 2 else K_AB, sigma=-1.0)
    np.save(path + ".tmp.npy", w); os.replace(path + ".tmp.npy", path)
    return path


def ab_spectrum(N, phi, K=K_AB):
    from lattice import lattice_spectrum_abelian
    return lattice_spectrum_abelian(N, N, phi, K) * N ** 2


def I6(lam, t0):
    lam = np.asarray(lam, float); x = lam * t0
    return np.exp(-x) / (2 * t0 ** 2) - lam * np.exp(-x) / (2 * t0) + lam ** 2 * exp1(np.maximum(x, 1e-300)) / 2


def dV6(lam, ref, t0):
    return float(-(np.sum(I6(lam, t0)) - np.sum(I6(ref, t0))))


def dlogdet(lam, ref, t0):
    return float(-(np.sum(exp1(lam * t0)) - np.sum(exp1(ref * t0))))


def exact_dV6(phi, ref=(0, 0), M=60):
    """the abelian six-dimensional term, exact (Poisson): -(A/4 pi) 128 sum_{l != 0} (cos 2 pi phi.l - 1)/|l|^6"""
    m, n = np.meshgrid(np.arange(-M, M + 1), np.arange(-M, M + 1), indexing="ij"); m = m.ravel(); n = n.ravel()
    nz = (m != 0) | (n != 0); m, n = m[nz], n[nz]
    l6 = np.abs(m + n * OMEGA) ** 6
    f = lambda p: -(A / (4 * math.pi)) * 128 * np.sum((np.cos(2 * np.pi * (m * p[0] + n * p[1])) - 1) / l6)
    return float(f(phi) - f(ref))


def periodic_dV6(phi, M=60):
    """rho_Q's periodic part with the line: the trace of rho_Q along l is 0 off 2L, -2 on 2L minus 4L, +2 on 4L"""
    m, n = np.meshgrid(np.arange(-M, M + 1), np.arange(-M, M + 1), indexing="ij"); m = m.ravel(); n = n.ravel()
    nz = (m != 0) | (n != 0); m, n = m[nz], n[nz]
    tr = np.where((m % 2 == 0) & (n % 2 == 0), np.where((m % 4 == 0) & (n % 4 == 0), 2.0, -2.0), 0.0)
    l6 = np.abs(m + n * OMEGA) ** 6
    return float(-(A / (4 * math.pi)) * 128 * np.sum(tr * (np.cos(2 * np.pi * (m * phi[0] + n * phi[1])) - 1) / l6))


def load(N, phi, rank=2):
    return np.load(key(N, phi, rank))


def read():
    root = next(q for q in [os.path.abspath(os.path.join(HERE, *[".."] * k)) for k in range(1, 8)]
                if os.path.isdir(os.path.join(q, "frontier")) and os.path.isfile(os.path.join(q, "GENESIS.md")))
    sys.path.insert(0, os.path.join(root, "frontier", "B1684_w59_on_main", "verification", "main_check"))
    import main_w59 as w59
    out = {}
    # ---- P1: the abelian control at N = 192 (and 96), reference (1/2, 1/2) ----
    p1 = {}
    for N in (96, 192):
        ref = ab_spectrum(N, AB_REF); t0 = 30 / ref[-1]
        rows = []
        for phi in CONTROL:
            lam = ab_spectrum(N, phi)
            ld = dlogdet(lam, ref, t0); ld_ex = w59.logdet_epstein(phi, OMEGA) - w59.logdet_epstein(AB_REF, OMEGA)
            v6 = dV6(lam, ref, t0); v6_ex = exact_dV6(phi, AB_REF)
            rows.append({"phi": list(phi), "dlogdet": ld, "dlogdet_exact": ld_ex, "abs_err_logdet": abs(ld - ld_ex),
                         "dV6": v6, "dV6_exact": v6_ex, "abs_err_V6": abs(v6 - v6_ex),
                         "rel_err_V6": abs(v6 - v6_ex) / abs(v6_ex) if abs(v6_ex) > 1e-9 else None})
        p1[N] = rows
    out["P1_abelian_control"] = p1
    # ---- the matter at the special points ----
    sp = {}
    for N in (96, 192):
        ref = load(N, (0, 0)); t0 = 30 / ref[-1]
        sp[N] = {"t0": t0, "lambda_K": float(ref[-1]), "lowest10": (ref[:10] / N ** 2).tolist(), "points": []}
        for phi in SPECIAL:
            lam = load(N, phi)
            sp[N]["points"].append({"phi": [round(phi[0], 6), round(phi[1], 6)], "fermion_2d": -0.5 * dlogdet(lam, ref, t0),
                                    "fermion_6d": -dV6(lam, ref, t0), "periodic_part_6d_fermion": -periodic_dV6(phi)})
    out["matter_special_points"] = sp
    r96, r192 = load(96, (0, 0)), load(192, (0, 0))
    # in W60's units (H_W60 = N^2 H_unit): the same continuum eigenvalues at both N (a first version divided by N^2,
    # comparing lattice units across N; corrected before the record)
    out["convergence_lowest10_rel_change"] = (np.abs(r192[:10] - r96[:10]) / r192[:10]).tolist()
    # ---- P2: symmetries on the lattice (N = 96, from fresh solves at generic phi) are in main_w60_symmetry (small N exact) ----
    # ---- the grid at N = 96 ----
    ref = r96; t0 = 30 / ref[-1]
    gl = lambda a, b: load(96, tuple(x / 24 for x in _canon(a, b)))
    G = np.array([[-dV6(gl(a, b), ref, t0) for b in range(12)] for a in range(12)])  # fermion 6d
    G2 = np.array([[-0.5 * dlogdet(gl(a, b), ref, t0) for b in range(12)] for a in range(12)])
    p2 = []
    for phi in P2_POINTS:
        imgs = [load(96, (img[0] % 1.0, img[1] % 1.0)) for img in (phi, (phi[0] + 0.5, phi[1]), (-phi[0], -phi[1]), (phi[1], -phi[0] - phi[1]))]
        p2.append({'phi': list(phi), 'spectra_max_rel': float(max(np.max(np.abs(x - imgs[0]) / imgs[0]) for x in imgs[1:])),
                   'V6_max_abs': float(max(abs(dV6(x, ref, t0) - dV6(imgs[0], ref, t0)) for x in imgs[1:]))})
    out['P2_direct_N96'] = p2
    out["grid96_fermion_6d_min"] = float(G.min()); out["grid96_fermion_6d_argmin"] = [int(x) for x in np.unravel_index(G.argmin(), G.shape)]
    out["grid96_fermion_6d_max"] = float(G.max()); out["grid96_fermion_6d_argmax"] = [int(x) for x in np.unravel_index(G.argmax(), G.shape)]
    out["grid96_fermion_2d_min"] = float(G2.min()); out["grid96_fermion_2d_argmax"] = [int(x) for x in np.unravel_index(G2.argmax(), G2.shape)]
    per = np.array([[-periodic_dV6((a / 24, b / 24)) for b in range(12)] for a in range(12)])
    out["grid96_corr_with_periodic_part"] = float(np.corrcoef(G.ravel(), per.ravel())[0, 1])
    out["grid96_diffraction_over_periodic_at_(1/6,1/6)"] = float((G[4, 4] - per[4, 4]) / per[4, 4])
    np.save(os.path.join(HERE, "grid96_fermion_6d.npy"), G)
    # ---- the content's net term, against w = 0 (boson-sign values: a fermion's potential is -dV6 per state x 2) ----
    def matter_dV6(N, phi):                                   # boson-sign Delta V6 of the rho_Q sector at phi, direct
        rr = load(N, (0, 0)); return dV6(load(N, phi), rr, 30 / rr[-1])
    def higgs(w):
        return sum(2 * (exact_dV6(((p[0] + 3 * w[0]) % 1, (p[1] + 3 * w[1]) % 1)) - exact_dV6(p)) for p in PAR)
    net = {}
    for N in (96, 192):
        row = {}
        for name, w in (("w0=(1/3,1/3)", (1 / 3, 1 / 3)), ("(1/9,1/9)", (1 / 9, 1 / 9)), ("(2/9,2/9)", (2 / 9, 2 / 9))):
            q_part = sum(-2 * n * matter_dV6(N, ((q * w[0]) % 1, (q * w[1]) % 1)) for _, q, n in QUARKS)
            row[name] = {"quarks": q_part, "higgs": higgs(w), "net": q_part + higgs(w)}
        for w in PAR:                                          # the 2-torsion lines: rho_Q sees nothing (q w = 0 mod 1/2)
            row["2-torsion %s" % (w,)] = {"quarks": 0.0, "higgs": higgs(w), "net": higgs(w)}
        net[N] = row
    out["net_term"] = net
    # ---- the global minimum of the net term over every line: the matter by trigonometric interpolation of the N = 96
    #      grid (period 1/2; 12 x 12 nodes), the Higgs exact ----
    C = np.fft.fft2(-G)                                        # boson-sign matter Delta V6 on the grid
    kk = np.fft.fftfreq(12, d=1.0 / 12)
    def matter_interp(phi):
        x = (np.array(phi) % 0.5) * 24                        # grid units
        e1 = np.exp(2j * np.pi * np.outer(kk, [x[0]]) / 12).ravel(); e2 = np.exp(2j * np.pi * np.outer(kk, [x[1]]) / 12).ravel()
        return float(np.real(e1 @ C @ e2) / 144)
    # the interpolant against the direct solves at the content's lines
    chk = []
    for w in [(1 / 9, 1 / 9), (2 / 9, 2 / 9), (1 / 3, 1 / 3)]:
        for _, q, _n in QUARKS:
            phi = ((q * w[0]) % 1, (q * w[1]) % 1); chk.append(abs(matter_interp(phi) - matter_dV6(96, phi)))
    out["interpolant_max_abs_err_at_direct_points"] = float(max(chk))
    fine = (np.arange(180) + 0.5) / 180
    best = (1e9, None)
    vals = np.zeros((180, 180))
    for i, a in enumerate(fine):
        for j, b in enumerate(fine):
            w = (a, b); v = sum(-2 * n * matter_interp(((q * a) % 1, (q * b) % 1)) for _, q, n in QUARKS) + higgs(w)
            vals[i, j] = v
            if v < best[0]: best = (v, w)
    out["net_fine_grid_min"] = {"value": best[0], "w": list(best[1])}
    out["net_at_2torsion_N96"] = [net[96]["2-torsion %s" % (w,)]["net"] for w in PAR]
    out["net_2torsion_below_fine_grid_min"] = bool(min(out["net_at_2torsion_N96"]) <= best[0] + 1e-9)
    json.dump(out, open(os.path.join(HERE, "main_w60.json"), "w"), indent=1)
    return out


if __name__ == "__main__":
    if sys.argv[1] == "spectra":
        os.makedirs(CACHE, exist_ok=True)
        nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
        T = tasks(); print(len(T), "tasks", flush=True)
        if nw == 1:
            for t in T: print(solve(t), flush=True)
        else:
            from multiprocessing import Pool
            with Pool(nw) as P:
                for p in P.imap_unordered(solve, T): print(os.path.basename(p), flush=True)
    elif sys.argv[1] == "read":
        o = read(); print(json.dumps({k: o[k] for k in ("net_fine_grid_min", "net_at_2torsion_N96", "grid96_corr_with_periodic_part")}, indent=1))
