import math, itertools, numpy as np, runpy, mpmath as mp
ns = runpy.run_path("ref1.py", run_name="ref1")
F, Bf, AL, AR, A_RL, A_RRL = ns["F"], ns["Bf"], ns["AL"], ns["AR"], ns["A_RL"], ns["A_RRL"]
fr = [F[:, 0], F[:, 1], F[:, 2]]
def R_np(t, K=40):
    n = np.arange(-K, K + 1); q = lambda x: np.exp(1j * np.pi * t * x)
    th2, th3, th4 = np.sum(q((n + 0.5) ** 2)), np.sum(q(n * n)), np.sum((-1.0) ** n * q(n * n))
    den = np.pi * th2 * th3 * th4
    return np.array([-th2 ** 2 / den, -th4 ** 2 / den, 1j * th3 ** 2 / den])
def par(u, v):  # 1 - |<u,v>|^2/(|u|^2|v|^2): 0 iff parallel
    return 1 - abs(np.vdot(u, v)) ** 2 / (np.vdot(u, u).real * np.vdot(v, v).real)
mobius = {"t+1": lambda t: t + 1, "t-1": lambda t: t - 1, "t/(t+1)": lambda t: t / (t + 1), "t/(1-t)": lambda t: t / (1 - t),
          "-1/t": lambda t: -1 / t}
taus = [0.13 + 1.21j, -0.31 + 0.95j, 0.4 + 1.6j]
perms = list(itertools.permutations([0, 1, 2])); signs = [(1, s2, s3) for s2 in (1, -1) for s3 in (1, -1)]
print("covariance R_B(g t) ~ A^{+-1} R_B(t): frames where L and R both covariant")
for pm in perms:
    for sg in signs:
        RB = lambda t: sum(sg[u] * R_np(t)[u] * fr[pm[u]] for u in range(3))
        res = {}
        for gname, A in (("L", AL), ("R", AR)):
            best = None
            for mname, m in mobius.items():
                for e, Ae in ((+1, A), (-1, np.linalg.inv(A))):
                    d = max(par(RB(m(t)), Ae @ RB(t)) for t in taus)
                    if best is None or d < best[0]: best = (d, mname, e)
            res[gname] = best
        if res["L"][0] < 1e-10 and res["R"][0] < 1e-10:
            print("  pm", pm, "signs", sg, "L<->", res["L"][1:], "R<->", res["R"][1:])
# R_np vs B1649's R_of and Y_of kernel
FR = ns["FR"]
B1642 = FR / "B1642_the_golden_coupling_as_the_zero_modes_residue" / "verification" / "residue_coupling.py"
g = {"__file__": str(B1642)}
exec(compile(open(B1642).read().split("rng = np.random.default_rng(1642)")[0], "defs", "exec"), g)
src = (FR / "B1649_the_kernel_at_the_puncture" / "verification" / "the_kernel_at_the_puncture.py").read_text()
def grab(name):
    i = src.index(f"def {name}("); j = src.index("\ndef ", i + 1); return src[i:j]
g["ONE"] = mp.eye(2); g["BLOCK_OF_UNIT"] = [1, 0, 2]
exec(grab("Y_of"), g); exec(grab("R_of"), g)
mp.mp.dps = 30
for t in (1j, complex(-0.5, math.sqrt(3) / 2), 0.3 + 1.1j):
    tm = mp.mpc(t.real, t.imag)
    Ro = np.array([complex(x) for x in g["R_of"](tm)])
    Y = g["Y_of"]([0.3 + 0.2j, 1.1 - 0.4j, -0.7 + 0.9j, 0.5 + 0.5j], tm)
    Yn = np.array([[complex(Y[a, b]) for b in range(3)] for a in range(3)])
    _, s, Vh = np.linalg.svd(Yn); ker = Vh[-1].conj()
    print(f"tau={t}: |R_np - R_of|/|R| = {np.linalg.norm(R_np(t) - Ro) / np.linalg.norm(Ro):.1e}; ker(Y_of) vs R_np: {par(ker, R_np(t)):.1e}; s_min/s_max {s[-1]/s[0]:.1e}")
# W68's line at omega
w = np.exp(2j * np.pi / 3); tw = complex(-0.5, math.sqrt(3) / 2)
Rw = R_np(tw)
print("R(omega) vs W68 l_omega=(-w,1,w^2):", par(Rw, np.array([-w, 1, w ** 2])), " vs (-w^2,1,w):", par(Rw, np.array([-w ** 2, 1, w])))
print("R(omega) normalised:", np.round(Rw / Rw[1], 6))
