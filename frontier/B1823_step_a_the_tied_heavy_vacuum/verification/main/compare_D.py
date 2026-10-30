"""Step A v2, section D: the draft's run against main's rerun with a cancellation-free F and 24 extra starts deep in the
cusp (rerun_stableF/).  Per configuration: the plan's class (PLAN.md 3.4: isolated = every Hessian eigenvalue > 1e-6 x the
largest), the draft's refined class (summarize.py's rules, copied), runaways, tau* and V*.  Per n: the sealed reading,
'the global minimum is isolated at EVERY primary parameter point' (the 9 points mu^2 x lambda v at m0^2 = 0.01 mu^2, both
menus; the m0 check and the convention check reported apart).  Data-free."""
import json, pathlib, collections
H = pathlib.Path(__file__).resolve().parent
draft = json.loads((H.parents[0] / "step_a_v2.json").read_text())["D"]["configs"]          # verification/step_a_v2.json
rerun = json.loads((H / "rerun_stableF" / "step_a_v2.json").read_text())["D"]["configs"]


def refined_interior(r):
    b = r["best"]
    if b["grad_inf_after_newton"] > 1e-12:
        return "UNCONVERGED"
    if b["n_negative"] > 0:
        return "SADDLE"
    E1, E2 = b["hess_eigs"], b["hess_eigs_step2"]; emax = max(abs(e) for e in E1)
    noise = [k for k in range(6) if abs(E1[k]) < 1e-11 * emax or abs(E1[k] - E2[k]) > 0.1 * abs(E1[k])]
    if not noise:
        return "ISOLATED" + ("" if min(E1) > 1e-6 * emax else "(weak)")
    vf = [v for v in r.get("valley_follow", []) if v["step"] == 0.05]
    if vf and max(vf[0]["fs_moved"], vf[0]["tau_moved"]) > 0.025 and abs(vf[0]["dV"]) < 1e-12 * max(abs(b["V"]), 1e-30):
        return "FLAT(%d)" % len(noise)
    return "UNRESOLVED"


def classes(r):
    if "best" not in r:
        return dict(plan="no interior", refined="RUNAWAY(no interior)", runaway=True, sealed_pass=False, tau=None, V=None)
    b = r["best"]; ri = refined_interior(r); run = "runaway" in r
    plan = "iso" if b["isolated"] else "flat%d" % b["n_flat"]
    ok = bool(b["isolated"] and b["n_negative"] == 0 and b["grad_inf_after_newton"] <= 1e-12 and not run)
    return dict(plan=plan, refined=("RUNAWAY(interior %s)" % ri) if run else ri, runaway=run, sealed_pass=ok,
                tau=b["tau"], V=b["V"], runaway_at=r.get("runaway"))


key = lambda r: (r["menu"], r["tnorm"], r["snorm"], r["n"], round(r["mu2"], 4), round(r["m02"], 6), round(r["lv"], 4))
dk = {key(r): r for r in draft}; rk = {key(r): r for r in rerun}
assert set(dk) == set(rk) and len(dk) == 176, (len(dk), len(rk))
rows = []; changed = []
for k in sorted(dk):
    a, b = classes(dk[k]), classes(rk[k])
    same_tau = (a["tau"] is not None and b["tau"] is not None and abs(complex(*a["tau"]) - complex(*b["tau"])) < 1e-6)
    rows.append(dict(config=list(k), draft=a, rerun=b, same_tau=same_tau))
    if a["refined"] != b["refined"] or a["plan"] != b["plan"] or not same_tau:
        changed.append((k, a["refined"], a["plan"], b["refined"], b["plan"], a["tau"], b["tau"], b.get("runaway_at")))
print("configurations whose class or tau* changed in the rerun: %d" % len(changed))
for c in changed:
    print("  ", c[0], "| draft:", c[1], c[2], c[5], "| rerun:", c[3], c[4], c[6], ("runaway " + json.dumps(c[7])) if c[7] else "")
print()
print("the sealed reading per n (the 9 primary points per menu; then the m0 check; then the convention check):")
table = {}
for n in range(1, 9):
    out = {}
    for who, src in (("draft", dk), ("rerun", rk)):
        prim = [classes(src[k])["sealed_pass"] for k in src if k[3] == n and k[1] == "N" and abs(k[5] / k[4] - 0.01) < 1e-9]
        m0 = [classes(src[k])["sealed_pass"] for k in src if k[3] == n and k[1] == "N" and abs(k[5] / k[4] - 0.1) < 1e-9]
        cv = [classes(src[k])["refined"] for k in src if k[3] == n and k[1] == "cusp"]
        out[who] = dict(primary="%d/%d" % (sum(prim), len(prim)), passes=all(prim), m0_check="%d/%d" % (sum(m0), len(m0)), cusp=cv)
    table[n] = out
    print("  n=%d  draft %s pass=%s m0 %s | rerun %s pass=%s m0 %s | cusp convention (rerun): %s" % (
        n, out["draft"]["primary"], out["draft"]["passes"], out["draft"]["m0_check"], out["rerun"]["primary"],
        out["rerun"]["passes"], out["rerun"]["m0_check"], out["rerun"]["cusp"]))
(H / "compare_D.json").write_text(json.dumps(dict(changed=[[list(c[0])] + list(c[1:]) for c in changed], per_n=table, rows=rows),
                                             indent=1, default=str))
