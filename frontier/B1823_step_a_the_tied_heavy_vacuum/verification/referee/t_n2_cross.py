"""n = 2: the reported vacuum direction against Y1 x Y2 at tau* (bilinear cross product) and, for menu H, against R(tau*),
with the referee's independent forms (ref_model.py; DR by numerical differentiation).  FS distance via 2 arcsin(chord/2)."""
import sys, pathlib, json
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mpmath as mp
import ref_model as rm
mp.mp.dps = 30
D = json.loads((HERE.parent / "step_a_v2.json").read_text())["D"]["configs"]
def fsd(a, b):
    a = rm.unit(a); b = rm.unit(b)
    ov = mp.fsum(mp.conj(x) * y for x, y in zip(a, b)); ph = ov / abs(ov) if abs(ov) > 0 else 1
    chord = mp.sqrt(mp.fsum(abs(x * ph - y) ** 2 for x, y in zip(a, b)))
    return 2 * mp.asin(chord / 2)
rows = []
for r in D:
    if r["n"] != 2 or "best" not in r or r["tnorm"] != "N":
        continue
    b = r["best"]; tau = mp.mpc(*b["tau"]); S = [mp.mpc(*c) for c in b["S"]]
    trip = rm.MENU[r["menu"]][:2]
    Y = [rm.triplet_value(k, a, tau) for k, a in trip]
    cr = [Y[0][1] * Y[1][2] - Y[0][2] * Y[1][1], Y[0][2] * Y[1][0] - Y[0][0] * Y[1][2], Y[0][0] * Y[1][1] - Y[0][1] * Y[1][0]]
    row = dict(menu=r["menu"], mu2=r["mu2"], m02=r["m02"], lv=r["lv"], isolated=b["isolated"], tau=b["tau"],
               FS_to_cross=float(fsd(S, cr)))
    if r["menu"] == "H":
        row["FS_to_R"] = float(fsd(S, rm.Rvec(tau)))
        Rv = rm.Rvec(tau); dR = rm.DRvec(tau)
        row["R.R"] = float(abs(mp.fsum(x * x for x in Rv))); row["R.DR"] = float(abs(mp.fsum(x * y for x, y in zip(Rv, dR))))
    rows.append(row); print(row, flush=True)
(HERE / "t_n2_cross.json").write_text(json.dumps(rows, indent=1))
