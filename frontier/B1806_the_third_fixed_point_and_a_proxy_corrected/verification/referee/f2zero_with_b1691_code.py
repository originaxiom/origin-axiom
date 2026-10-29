"""B1691's own C2 control (section(n, 3, drop=(2,)): no D2R component), evaluated at tau = i with B1691's own at() and its
own slope rule (e = 5, 6; three directions) -- the row the draft did not run. Also the exact ratio s2/s1 from at()'s
P = s1 s2 and Q = s1^2 + s2^2 (at()[0] = P/Q is the leading-order proxy)."""
import io, json, contextlib, importlib.util, pathlib, sys
import mpmath as mp
Bdir = sorted(pathlib.Path(__file__).resolve().parents[3].glob("B1691_*"))[0] / "verification"
sys.path.insert(0, str(Bdir))
spec = importlib.util.spec_from_file_location("te", Bdir / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
mp.mp.dps = 40
I = mp.mpc(0, 1)
exact = lambda x: (1 - mp.sqrt(1 - 4 * x * x)) / (2 * x) if x > 0 else mp.mpf(0)   # s2/s1 from P/Q = r/(1 + r^2)
out = {}
for n in (4, 6):
    a, used = te.section(n, 3, drop=(2,))
    x0 = te.at(a, I)[0]; sl = []
    for th in (0.3, 1.9, 4.1):
        v = [te.at(a, I + mp.mpf(10) ** -e * mp.exp(1j * th))[0] for e in (5, 6)]
        sl.append(round(float(mp.log(v[0] / v[1]) / mp.log(10)), 3))
    out[str((4 * n - 1)) + "/2, f2 = 0"] = {"components_used": sorted(set(used)), "proxy_at_i": mp.nstr(x0, 4), "slope_in_eps": sl}
for n in (1, 3, 5):
    a, _ = te.section(n, 1); x = te.at(a, I)[0]
    out[str(4 * n - 1) + "/2 seed1 at i"] = {"proxy": mp.nstr(x, 12), "exact s2/s1": mp.nstr(exact(x), 12)}
pathlib.Path(__file__).with_name("f2zero_with_b1691_code.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
