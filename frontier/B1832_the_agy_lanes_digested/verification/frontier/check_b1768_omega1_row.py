"""agy:B1768's segment 'period matrix', the omega_1 = dx/w^2 = dx/y = pi^* dz row (branch-convention-free test).  Any path on Y from a
branch point over e_i to one over e_j projects to a path on E from z_i to z_j, so int omega_1 = z_j - z_i (mod Lambda = Z + Z tau, up to
sign), with z(e1) = 1/2, z(e2), z(e3) in {tau/2, (1+tau)/2}, z(infinity) = 0.  B1768 states row 1 = (0.500000, 0.166535 + 1.1037i, 0.468377)
for segments [e2, e3], [e3, e1], [e1, infinity).  Test each against the allowed set."""
import json, math, pathlib, itertools
y = math.sqrt(84) / 3; tau = complex(1 / 3, y)
def allowed(dz):                                      # all values +-dz + m + n tau, nearest to a given number
    return [s * dz + m + n * tau for s in (1, -1) for m in range(-3, 4) for n in range(-2, 3)]
cases = {"[e2,e3]": (0.5 + 0j, [0.5, -0.5]), "[e3,e1]": (complex(0.166535, 1.1037), [tau / 2, (1 + tau) / 2]), "[e1,inf)": (complex(0.468377, 0), [0.5])}
out = {}
for k, (lane, dzs) in cases.items():
    d = min(abs(lane - v) for dz in dzs for v in allowed(dz))
    near = min((v for dz in dzs for v in allowed(dz)), key=lambda v: abs(lane - v))
    out[k] = {"lane": [lane.real, lane.imag], "nearest_allowed": [near.real, near.imag], "distance": d}
    print("%-9s lane %s ; nearest allowed value %s ; distance %.4f" % (k, lane, complex(round(near.real, 6), round(near.imag, 6)), d))
json.dump(out, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1); print("exit 0")
