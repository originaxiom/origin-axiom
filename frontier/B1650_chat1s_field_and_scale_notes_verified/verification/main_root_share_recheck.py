"""Main's independent recheck of chat1's root-share check (chat1's name: T-ROOT): spot-check its volumes and CS with main's own SnapPy calls, then recompute
the root share p, the chiral share f and N_eff at c = 6 from the volumes with main's own arithmetic (weights A, B, C)."""
import json, math, random, subprocess, warnings
warnings.filterwarnings("ignore")
import snappy
# chat1's thread table at its pinned commit (the web seat's branch, fetched into main's repository)
T = json.loads(subprocess.run(["git", "show", "047b8f7a4:relays/chat1_2026-10-14_the_scale/t_root_threads.json"], capture_output=True, text=True).stdout)
out = {"n_threads": len(T)}
random.seed(6); sample = random.sample(sorted(T), 60); dv = dcs = 0.0; pi2 = math.pi ** 2
for w in sample:
    z = snappy.Manifold("b++" + w).complex_volume(); v, cs = float(z.real), float(z.imag)
    cs = (cs + pi2 / 2) % pi2 - pi2 / 2
    dv = max(dv, abs(v - T[w][0])); d = abs(cs - T[w][1]); dcs = max(dcs, min(d, abs(d - pi2)))
out["spot_check_60"] = {"max_dvol": dv, "max_dcs_mod_pi2": dcs}
lengths = {}
for w in T: lengths[len(w)] = lengths.get(len(w), 0) + 1
def weight(w, kind):
    n = len(w)
    return 2.0 ** -n if kind == "A" else 3.0 ** -n if kind == "B" else 1.0 / (n * (n - 1) * lengths[n])
c = 6.0
for kind in "ABC":
    W = {w: weight(w, kind) * math.exp(-c * T[w][0] / (6 * math.pi)) for w in T}
    Z = sum(W.values()); p = W["LR"] / Z
    f = sum(x for w, x in W.items() if abs(T[w][1]) > 1e-6) / Z
    H = -sum((x / Z) * math.log(x / Z) for x in W.values() if x > 0)
    out["c6_" + kind] = {"root_share": p, "chiral_share": f, "N_eff": math.exp(H)}
print(json.dumps(out, indent=1)); json.dump(out, open("main_troot_recheck.json", "w"), indent=1)
