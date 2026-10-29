"""m(tau) for a = DR is invariant under SL(2,Z) (Y transforms by i P . P up to scalars); so a near-axis point of LR's geodesic
can be evaluated at its fundamental-domain image, where every series converges. Checks referee_check.py's direct route
against B1691's truncated q-series at the geodesic's ends."""
import json, pathlib
import mpmath as mp
src = (pathlib.Path(__file__).with_name("referee_check.py")).read_text().split("# ---- 1.")[0]
ns = {"__file__": str(pathlib.Path(__file__).with_name("referee_check.py"))}; exec(src, ns)
mp.mp.dps = 50
basis, masses = ns["basis"], ns["masses"]
def reduce(t):
    while True:
        n = mp.nint(t.real); t = t - n
        if abs(t) < 1 - mp.mpf(10) ** -30: t = -1 / t
        else: return t
c, r = mp.mpf(1) / 2, mp.sqrt(5) / 2
out = {}
for jj in (1, 2, 40):
    th = mp.pi * jj / 80; t = mp.mpc(c + r * mp.cos(th), r * mp.sin(th)); tf = reduce(t)
    b, bf = basis(t), basis(tf)
    out["pi*%d/80" % jj] = {"tau": mp.nstr(t, 6), "fd_image": mp.nstr(tf, 6), "true_m_direct": mp.nstr(masses(b[1], b[0])[1], 10),
                            "true_m_at_fd_image": mp.nstr(masses(bf[1], bf[0])[1], 10)}
pathlib.Path(__file__).with_name("geodesic_fd_check.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
