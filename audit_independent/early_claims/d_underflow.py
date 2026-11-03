"""(d) Defect 4D: size of the th2^a component of F_a relative to the others, at Im tau 2.5-4 (is it IEEE underflow?)"""
import mpmath as mp, json
mp.mp.dps = 30; out = []
for y in (2.5, 3.0, 3.5, 4.0):
    q = mp.exp(1j*mp.pi*mp.mpc(0.1, y))
    t2, t3, t4 = (mp.jtheta(k, 0, q) for k in (2, 3, 4))
    for a in (6, 18, 22, 26):
        r = abs(t2/t3)**a
        out.append({"Im tau": y, "a": a, "|th2/th3|^a": float(r), "as float64 complex": abs(complex(t2**a)), "underflows_to_zero": complex(t2**a) == 0,
                    "lost_if_added_to_1": float(r) < 2.2e-16})
for o in out: print(o)
json.dump(out, open("d_underflow.json", "w"), indent=1)
