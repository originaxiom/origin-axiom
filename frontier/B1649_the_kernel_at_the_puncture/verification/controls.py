"""B1649 controls (run before the seal; no cell computed): types and plumbing on banked or algebraic cases only."""
import os, sys, json
os.environ.setdefault("OA_FRONTIER", os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")))
src = open("the_kernel_at_the_puncture.py").read().split("rng = np.random.default_rng(1649)")[0]
ns = {"__file__": os.path.abspath("the_kernel_at_the_puncture.py"), "__name__": "controls"}
exec(compile(src, "defs", "exec"), ns)
mp, np = ns["mp"], ns["np"]
t = mp.mpc(0.11, 1.17)
Y = ns["Y_of"]([1, 0, 0, 0], t)                                    # B1642's sealed case: antisymmetric
asym = max(abs(Y[a, b] + Y[b, a]) for a in range(3) for b in range(3)); scale = max(abs(Y[a, b]) for a in range(3) for b in range(3))
iso = mp.matrix([1, 1j, 0]); a = [0, 0.3, -0.2, 0.5]
Yc = ns["Y_closed"](a, iso); kill = max(abs(x) for x in (Yc * iso))  # algebra: an isotropic vector is killed
D = mp.matrix([[3, 0, 0], [0, 2, 0], [0, 0, 1]]); absV, su, sd = ns["mixing"](D, D)
print(json.dumps({"B1642_case_antisym_rel": float(asym / scale), "closed_form_kills_isotropic": float(kill),
                  "mixing_of_identical_is_identity": bool(np.allclose(absV, np.eye(3))), "masses_ordered": [float(x) for x in su]}))
