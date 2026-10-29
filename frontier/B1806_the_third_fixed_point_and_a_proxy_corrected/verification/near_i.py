"""P-406 L2 near tau = i (exploratory, audit room; data-free): B1691's own C3 computation (near omega) re-run at the third
fixed point i, with B1691's code UNCHANGED except two substitutions: the point (omega -> i) and the residual generator
(rho(ST) -> rho(S) = e^{i pi/4} P, B1691's own W64 convention). Reads m2/m3 at i, its slope in eps = |tau - i|, and the
first generation's lift factor's slope; D's behaviour near i (needed for m1/m3) is NOT computed here."""
import json, pathlib, sys
B = sorted(pathlib.Path(__file__).resolve().parents[2].glob("B1691_*"))[0] / "verification"
src = (B / "the_exponents.py").read_text(encoding="utf-8")
for old, new in (("OM = mp.mpc(-0.5, mp.sqrt(3) / 2)", "OM = mp.mpc(0, 1)"),
                 ("ST = (mp.exp(1j * mp.pi / 4) ** 2) * Pm * Lm ** -1", "ST = mp.exp(1j * mp.pi / 4) * Pm")):
    assert src.count(old) == 1, old
    src = src.replace(old, new)
sys.path.insert(0, str(B))
ns = {"__file__": str(B / "the_exponents.py"), "__name__": "near_i"}
exec(compile(src, "the_exponents_at_i", "exec"), ns)
out = ns["out"]
res = {"rho_S_eigenvalues": out["C3_rho_ST_eigenvalues"], "rho_S_eigenlines_isotropic": out["C3_rho_ST_eigenlines_isotropic"],
       "near_i": out["C3_omega"]}
pathlib.Path(__file__).with_name("near_i.json").write_text(json.dumps(res, indent=1, default=str), encoding="utf-8")
print(json.dumps(res, indent=1, default=str)[:4000])
