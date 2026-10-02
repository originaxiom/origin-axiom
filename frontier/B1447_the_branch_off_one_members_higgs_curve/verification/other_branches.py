#!/usr/bin/env python3
"""The branches at the other branch points: construct representations off each, test irreducibility, and run the
homotopy to a single eigenvalue of the meridian.  usage: other_branches.py <index of the record in all_branch_points.json>"""
import sys, json, pathlib, itertools
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import branch_obstruction as bo, branch_follow as bf, triplet_spectrum as ts, branch_parabolic as bp, search_parabolic as sp
from mpmath import mp, mpf, mpc, matrix, zeros, eye, nstr, norm, svd_c, polyroots, exp, pi, log
mp.dps = 60
bp.print = lambda *a, **k: None
def classes(R0, M):
    def cls(entries):
        idx = [9 * g + 3 * i + j for g in range(3) for (i, j) in entries]; Ms = zeros(18, len(idx))
        for c, k in enumerate(idx):
            for i in range(18): Ms[i, c] = M[i, k]
        ns, rk, S = bo.nullspace(Ms); cb = [bo.vec(bo.coboundary(R0, bo.m3([mpc(1) if (k // 3, k % 3) == e else mpc(0) for k in range(9)]))) for e in entries]
        B = zeros(27, len(cb))
        for m, c in enumerate(cb):
            for i in range(27): B[i, m] = c[i]
        Ub, Sb, Vb = svd_c(B, full_matrices=True); rb = sum(1 for i in range(len(Sb)) if abs(Sb[i]) > mpf(10) ** (-18)); best = None
        for v in ns:
            w = matrix(27, 1)
            for c, k in enumerate(idx): w[k] = v[c]
            comp = w - sum((Ub[:, k] * sum(Ub[i, k].conjugate() * w[i] for i in range(27)) for k in range(rb)), matrix(27, 1))
            if best is None or norm(comp) > norm(best): best = comp
        return best / norm(best)
    return cls([(0, 2), (1, 2)]), cls([(2, 0), (2, 1)])
if __name__ == "__main__":
    n = int(sys.argv[1]); rec = json.load(open(HERE / "all_branch_points.json"))[n]
    roots = polyroots([1, 0, -8, 12, 0, 0, 4], maxsteps=300, extraprec=300)
    ur = mpc(*[mpf(x) for x in rec["u"].strip("()").replace(" ", "").replace("j", "").replace("+-", "-").rsplit("+" if "+" in rec["u"][1:] else "-", 1)]) if "j" in rec["u"] else mpf(rec["u"])
    if "j" in rec["u"]:
        import re as _re
        m = _re.match(r"^\(([-0-9.]+) ([+-]) ([0-9.]+)j\)$", rec["u"]); ur = mpc(mpf(m.group(1)), mpf(m.group(2) + m.group(3)))
    u = min(roots, key=lambda r: abs(r - ur)); a = tuple(rec["a"])
    R0 = bo.block_rep(u, a, zsign=rec["Z_sign"], tsign=rec["meridian_sign"]); M = bo.dG(R0); cp, cm = classes(R0, M)
    out = dict(u=nstr(u, 15), Z_sign=rec["Z_sign"], a=list(a), meridian_sign=rec["meridian_sign"], starts=[])
    for s, k in itertools.product((mpf("0.1"), mpf("0.25")), range(4)):
        phase = exp(2j * pi * k / 4); st = dict(s=nstr(s, 3), phase_index=k)
        try:
            U = bo.unvec((cp + phase * cm) * s); R = {g: (eye(3) + U[g]) * R0[g] for g in (1, 2, 3)}
            R, res = bf.newton(R); assert res < mpf(10) ** (-40), "no representation: %s" % nstr(res, 3)
            st["algebra_dimension_on_the_branch"] = bf.burnside(R)
            E, tau = ts.monodromy_on_H1({1: R[1], 2: R[2]}, R[3]); st["abs_log_eigenvalues_chi_trivial"] = [nstr(abs(log(e)), 6) for e in E]
            f0 = bp.f(R); Rp = R; K = 24
            for kk in range(1, K):
                Rp, nb = bp.solve(Rp, [(1 - mpf(kk) / K) * c for c in f0]); assert nb < mpf(10) ** (-30), "not converged at step %d" % kk
            for _ in range(40):
                Rp, nb = bp.solve(Rp, [mpc(0), mpc(0)], iters=6)
                if nb < mpf(10) ** (-45): break
            assert nb < mpf(10) ** (-25), "target not reached: %s" % nstr(nb, 3)
            st.update(parabolic=True, invariants=sp.invariants(Rp), spectra=sp.spectra(Rp))
        except (AssertionError, ZeroDivisionError) as ex: st.update(parabolic=False, why=str(ex)[:90])
        out["starts"].append(st); print(n, st["s"], k, st.get("algebra_dimension_on_the_branch"), st["parabolic"], st.get("invariants", {}).get("tr_x", st.get("why")), flush=True)
        json.dump(out, open(HERE / ("other_branch_%02d.json" % n), "w"), indent=1)
