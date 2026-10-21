"""B1691's second addendum: the parameter-free section DR (weight 3/2, unique) at the points the principle selects -- omega,
i (the tick LR's axis passes through it, B1630), the top of LR's geodesic (sqrt5/2 i, the lowest closed thread, B1629) --
and along tau = i y; m2/m3 by B1646's exact formulas (no asymptotics)."""
import io, json, contextlib, importlib.util, pathlib
import mpmath as mp
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("te", HERE / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
mp.mp.dps = 40
m = lambda tau: te.at(te.B[1], tau)[0]
pts = {"omega": mp.mpc(-0.5, mp.sqrt(3) / 2), "i": mp.mpc(0, 1), "top of LR's geodesic": mp.mpc(0, mp.sqrt(5) / 2)}
c, r = mp.mpf(1) / 2, mp.sqrt(5) / 2
geo = [m(mp.mpc(c + r * mp.cos(th), r * mp.sin(th))) for th in [mp.pi * j / 80 for j in range(1, 80)]]
out = {"m2/m3_at": {k: float(m(t)) for k, t in pts.items()},
       "on_LR_geodesic_min_max": [float(min(geo)), float(max(geo))],
       "along_i_y": {str(y): float(m(mp.mpc(0, y))) for y in (1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3)}}
# the inverse read-out: the Im tau at which DR's m2/m3 equals each value B1693 recorded (no new data read)
B1693 = {"up m_c/m_t": 0.0036847735647212647, "down m_s/m_b": 0.018724903134906656, "lepton m_mu/m_tau": 0.05887328180682186}
out["Im_tau_needed_for_B1693s_values"] = {k: float(mp.findroot(lambda y: m(mp.mpc(0, y)) - v, 2.2)) for k, v in B1693.items()}
if __name__ == "__main__":
    json.dump(out, open(HERE / "the_principles_points.json", "w"), indent=1); print(json.dumps(out, indent=1))
