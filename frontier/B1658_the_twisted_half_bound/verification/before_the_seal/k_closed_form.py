"""EXPLORATION (main, firewalled; RANDOM null S0 only — the symmetric S0 = R(omega), Rbar(omega) is NOT evaluated here):
search for k_s's closed form. S0 = u v^T, M_R = p q^T (both rank one). Candidate invariants from the epsilon pairings."""
import numpy as np, pathlib
SRC = pathlib.Path("frontier/B1656_the_electrons_zero/verification/the_electrons_zero.py").read_text()
ns = {"__file__": "/tmp/fake_inst.py", "__name__": "inst"}
exec(compile(SRC.split("T0 = time.time()")[0], "inst_head", "exec"), ns)
OM, line_w, sector_twists, residues, weighted_M, coupling, SIXY, SECTORS, EPS = (ns[k] for k in ("OM", "line_w", "sector_twists", "residues", "weighted_M", "coupling", "SIXY", "SECTORS", "EPS"))
print("EPS =", EPS.tolist())
rng = np.random.default_rng(17); w = line_w(1/9, 1/9, OM)
def r1(M):
    U, s, Vh = np.linalg.svd(M); return U[:, 0]*s[0], Vh[0]          # M ~ p q^T
for sec, (fl, fr) in SECTORS.items():
    x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); MR = weighted_M(residues(x, y, OM)); p, q = r1(MR)
    rows = []
    for _ in range(6):
        u = rng.normal(size=2)+1j*rng.normal(size=2); v = rng.normal(size=2)+1j*rng.normal(size=2)
        S0 = np.outer(u, v); nS = np.linalg.norm(S0); S0 /= nS; u = u/np.sqrt(nS); v = v/np.sqrt(nS)
        X = rng.normal(size=(2, 2))+1j*rng.normal(size=(2, 2)); X /= np.linalg.norm(X); S = S0 + 1e-4*X
        s = np.linalg.svd(coupling(S, MR), compute_uv=False); k = (s[1]/s[0])/(abs(np.linalg.det(S))/np.linalg.norm(S)**2)
        e = lambda a, b: a @ EPS @ b
        c = dict(uEp=abs(e(u, p)), vEq=abs(e(v, q)), uEq=abs(e(u, q)), vEp=abs(e(v, p)), up=abs(u @ p), vq=abs(v @ q), uq=abs(u @ q), vp=abs(v @ p),
                 nu=np.linalg.norm(u), nv=np.linalg.norm(v), np_=np.linalg.norm(p), nq=np.linalg.norm(q), s0=s[0])
        rows.append((k, c))
    ks = np.array([r[0] for r in rows])
    # test candidate: k * s0 / (|p||q|) proportional to something?
    for name in ("uEp", "vEq", "uEq", "vEp", "up", "vq", "uq", "vp"):
        vals = np.array([r[1][name] for r in rows]); 
    cand = {
      "s0/(|p||q|)": np.array([r[1]["s0"]/(r[1]["np_"]*r[1]["nq"]) for r in rows]),
      "|uEp||vEq|": np.array([r[1]["uEp"]*r[1]["vEq"] for r in rows]),
      "|uEq||vEp|": np.array([r[1]["uEq"]*r[1]["vEp"] for r in rows]),
      "|up||vq|": np.array([r[1]["up"]*r[1]["vq"] for r in rows]),
    }
    print(sec, "k:", np.round(ks, 4))
    for n_, c_ in cand.items():
        print("   k*", n_, np.round(ks*c_, 4), " k/", n_, np.round(ks/np.maximum(c_, 1e-30), 4))
