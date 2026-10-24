"""B1746 (P-357), POST HOC (labelled): the cube group's two-dimensional form spaces as Higgs pencils.
The three two-dimensional spaces of Gamma_4's forms on the null cone (cube_forms.py, part A): rho' at weight 6 and 8 and
rho' x sgn at weight 8.  Each scanned as h = A + lambda B (A, B an orthonormal basis of the space at tau; lambda fitted from
thirteen starts, read S in every sector and conjugated, c = 3) on B1742's grid, as B1743's pencils."""
import sys, json, math, pathlib, itertools
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "frontier" / "B1743_the_principled_pencils_and_the_nines_target" / "verification"))
sys.path.insert(0, str(HERE))
import pencils as P      # noqa: E402
import cube_forms as CF  # noqa: E402

SPACES = {"rho' w6": (6, 1), "rho' w8": (8, 0), "rho' x sgn w8": (8, 1)}
BASES = {k: CF.equivariant(d, tw) for k, (d, tw) in SPACES.items()}


def basis_at(key, t):
    ms, null = BASES[key]; v = CF.vt(t); H = np.array([CF.ev(ms, c, v) for c in null]); vh = np.linalg.svd(H)[2]
    return vh[0], vh[1]


def point(task):
    k, re_t, im_t = task; a, b = P.LINES[k]; B = P.R.CEN._modules()["B"]; M = P.SC.channels(re_t, im_t, a, b); out = []
    for key in SPACES:
        A_, B_ = basis_at(key, complex(re_t, im_t))
        for hor in ("L_max", "L_2"):
            for cj in (False, True):
                c, lam = P.fit_pencil(A_, B_, M, hor, B, conj=cj); out.append((key, k, re_t, im_t, hor, cj, c))
    return out


if __name__ == "__main__":
    from multiprocessing import Pool
    RES = [0.0625 + 0.125 * i for i in range(8)]; IMS = [round(2.0 + 0.1 * j, 10) for j in range(16)]
    tasks = [(k, r, y) for k in range(10) for r in RES for y in IMS]; rows = []
    with Pool(8) as Pp:
        for i, o in enumerate(Pp.imap_unordered(point, tasks, chunksize=4)):
            rows += o
            if i % 320 == 0: print("points", i, flush=True)
    for key in SPACES:
        for cj in (False, True):
            rr = [r for r in rows if r[0] == key and r[5] == cj]; b = min(rr, key=lambda r: r[6])
            print("%-14s read %-2s: min chi2_nine %8.2f at line %d, %.4f + %.2fi, %s; rows below 21.67: %d" % (
                key, "S~" if cj else "S", b[6], b[1], b[2], b[3], b[4], sum(r[6] < 21.67 for r in rr)))
    (HERE / "cube_pencils.json").write_text(json.dumps(rows) + "\n")
