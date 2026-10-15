"""EXPLORATION (main, firewalled): B1657's isotropic vacua in B1656's quaternionic, twisted frame. Load B1656's sealed
instrument's definitions (above T0) without running its cells; for each sector on the line (1/9, 1/9) at omega take the
residue quaternion M_R (null: det M_R = 0) and Higgs quaternions S with det S = 0 (null) and generic; read the spectra."""
import numpy as np, pathlib
SRC = pathlib.Path("frontier/B1656_the_electrons_zero/verification/the_electrons_zero.py").read_text()
ns = {"__file__": "/tmp/fake_inst.py", "__name__": "inst"}
exec(compile(SRC.split("T0 = time.time()")[0], "inst_head", "exec"), ns)
OM, line_w, sector_twists, residues, weighted_M, coupling, SIXY, SECTORS = (ns[k] for k in ("OM", "line_w", "sector_twists", "residues", "weighted_M", "coupling", "SIXY", "SECTORS"))
rng = np.random.default_rng(3)
w = line_w(1/9, 1/9, OM)
for sec, (fl, fr) in SECTORS.items():
    x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM); MR = weighted_M(R)
    sv = lambda S: (lambda s: s/s[0])(np.linalg.svd(coupling(S, MR), compute_uv=False))
    gen = sv(rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)))
    # null Higgs quaternions: rank-one 2x2 matrices S = u v^T; and S proportional to MR, to adj(MR), to MR^dagger
    u, v = rng.normal(size=2) + 1j*rng.normal(size=2), rng.normal(size=2) + 1j*rng.normal(size=2)
    adj = np.array([[MR[1, 1], -MR[0, 1]], [-MR[1, 0], MR[0, 0]]])
    print(sec, "det MR/|MR|^2 = %.1e" % (abs(np.linalg.det(MR))/np.abs(MR).max()**2),
          "| generic S:", np.round(gen, 4), "| null S=uv^T:", np.round(sv(np.outer(u, v)), 4),
          "| S=MR:", np.round(sv(MR), 4), "| S=adj MR:", np.round(sv(adj), 4), "| S=MR^dag:", np.round(sv(MR.conj().T), 4))

print("\n--- one null Higgs S0 = u v^T shared by the sectors, perturbed by eps X: coefficient k_s = (m2/m3)/(|det S|/|S|^2)")
for trial in range(3):
    u, v = rng.normal(size=2) + 1j*rng.normal(size=2), rng.normal(size=2) + 1j*rng.normal(size=2)
    S0 = np.outer(u, v); S0 = S0/np.linalg.norm(S0); X = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)); X = X/np.linalg.norm(X)
    row = []
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM); MR = weighted_M(R)
        ks = []
        for eps in (1e-3, 1e-4):
            S = S0 + eps*X; s = np.linalg.svd(coupling(S, MR), compute_uv=False)
            ks.append((s[1]/s[0])/(abs(np.linalg.det(S))/np.linalg.norm(S)**2))
        row.append(f"{sec}: k = {ks[0]:.4f} ({ks[1]:.4f})")
    print("trial", trial, " | ".join(row))
