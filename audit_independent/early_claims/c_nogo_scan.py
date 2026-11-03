"""(c) Is Theorem 2's 'no-go' a theorem? Empirical scan of FR-FIB with main's primitives: random census lines (orders 1-12)
and tau in the band, all 13 directions x 2 radii x 8 readings; full 3x3 CKM.  Count rows with hierarchical quark masses
and mc/mt < ms/mb, and among them how often |V_ub| < |V_td| and sin(delta) > 0.5."""
import json, math, pathlib, sys, itertools, time
from fractions import Fraction as Fr
import numpy as np

ROOT = pathlib.Path("/Users/dri/.gemini/antigravity/scratch/origin-axiom-independent-audit")
OUT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification"))
import cm_zero_line as Z
M_ = Z.mods(); B = M_["B"]
rng = np.random.default_rng(2026)
lines = sorted({min((Fr(a, N), Fr(b, N)), (Fr((-a) % N, N), Fr((-b) % N, N))) for N in range(1, 13) for a in range(N) for b in range(N)
                if math.gcd(math.gcd(a, b), N) == 1})
print("lines", len(lines))
NPTS = int(sys.argv[1]) if len(sys.argv) > 1 else 120
stats = {"rows": 0, "defined": 0, "hier": 0, "hier_vub_lt_vtd": 0, "hier_flip": 0, "any_vub_lt_vtd": 0, "any_flip": 0,
         "hier_sin_gt_0.5": 0}
examples = []; t0 = time.time()
for p in range(NPTS):
    line = lines[rng.integers(len(lines))]; tau = complex(rng.uniform(-0.5, 0.5), rng.uniform(1.0, 4.0))
    try:
        ch = {}
        for sn, ql, qr in Z.SECTORS:
            w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
            R = B.residues(x, yy, tau); ch[sn] = (R, B.cA(x, yy, tau, R))
        Lmax, L2 = Z.radii(tau)
    except Exception as ex:
        print("skip", line, tau, ex); continue
    for d in Z.DIRS:
        a = Z.direction(d, tau)
        for L in (Lmax, L2):
            for rd in itertools.product((0, 1), repeat=2):
                U = {}; ms = {}; ok = True
                for (sn, ql, qr), r in zip(Z.SECTORS[:2], rd):
                    R, c = ch[sn]
                    S = a[0]*B.QI + a[1]*B.QJ + a[2]*B.QK
                    if r: S = B.EPS @ S.conj() @ B.EPS.T
                    u = {k: (math.sqrt(2*math.pi*L + c[k])*R[k] if c[k] is not None and 2*math.pi*L + c[k] > 0 else 0) for k in B.UNITS}
                    Y = B.coupling(S, B.weighted_M(u))
                    u_, s, _ = np.linalg.svd(Y); o = np.argsort(s); s = s[o]; U[sn] = u_[:, o]; ms[sn] = s/s[2]
                    if min((s[1] - s[0])/s[2], (s[2] - s[1])/s[2]) < 1e-8: ok = False
                stats["rows"] += 1
                if not ok: continue
                stats["defined"] += 1
                V = U["up"].conj().T @ U["down"]; A = np.abs(V)
                J = float(np.imag(V[0, 1]*V[1, 2]*np.conj(V[0, 2])*np.conj(V[1, 1])))
                s13 = A[0, 2]; c13 = math.sqrt(max(1e-300, 1 - s13**2)); s12 = A[0, 1]/c13; s23 = A[1, 2]/c13
                den = math.sqrt(max(0, 1 - s12**2))*c13**2*math.sqrt(max(0, 1 - s23**2))*s12*s13*s23
                sd = abs(J)/den if den > 1e-14 else 0.0
                vlt = A[0, 2] < A[2, 0]; flip = vlt and sd > 0.5
                hier = (ms["up"][0] < 0.1*ms["up"][1] < 0.01) and (ms["down"][0] < 0.3*ms["down"][1] < 0.03) and ms["up"][1] < ms["down"][1] and A[0, 1] > 0.05
                stats["any_vub_lt_vtd"] += vlt; stats["any_flip"] += flip
                if hier:
                    stats["hier"] += 1; stats["hier_vub_lt_vtd"] += vlt; stats["hier_flip"] += flip; stats["hier_sin_gt_0.5"] += sd > 0.5
                    if vlt and len(examples) < 20:
                        examples.append({"line": [str(line[0]), str(line[1])], "tau": [tau.real, tau.imag], "dir": d, "L": L, "rd": rd,
                                         "mu/mt": ms["up"][0], "mc/mt": ms["up"][1], "md/mb": ms["down"][0], "ms/mb": ms["down"][1],
                                         "Vus": A[0, 1], "Vcb": A[1, 2], "Vub": A[0, 2], "Vtd": A[2, 0], "sin_delta": sd})
    if p % 10 == 0: print(p, round(time.time() - t0), stats, flush=True)
print("FINAL", stats)
json.dump({"stats": stats, "examples": examples, "npts": NPTS,
           "hier_definition": "mu/mt < 0.1 mc/mt < 0.01; md/mb < 0.3 ms/mb < 0.03; mc/mt < ms/mb; |V_us| > 0.05"},
          open(OUT / "c_nogo_scan.json", "w"), indent=1, default=float)
