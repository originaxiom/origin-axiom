"""STEP A v2 -- tables for DESIGN.md from step_a_v2.json (+ analysis_leading.json): python3 -I summarize.py > summary.txt

The plan's classification (PLAN.md 3.4) is printed beside a refined one:
  RUNAWAY      the lowest point found has Im tau > 6 (the potential decreases toward the cusp; no interior vacuum)
  SADDLE       the refinement ended at a point with a negative Hessian eigenvalue (no minimum certified there)
  FLAT(k)      k Hessian eigenvalues below the plan's threshold AND the valley follow moved the point by about the step
               (Fubini-Study or hyperbolic) with |dV| < 1e-20: a k-dimensional valley of minima
  WEAK-ISO     eigenvalues below the plan's threshold but above the two-step noise floor and the valley follow does not
               stay at constant V: an isolated minimum with an exponentially small (e^{-2 pi Im tau}) transverse curvature
  ISOLATED     every eigenvalue above 1e-6 x the largest (the plan's criterion)
"""
import json, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
d = json.loads((HERE / "step_a_v2.json").read_text())


def refined(r):
    if "best" not in r:
        return "RUNAWAY(no interior minimum)"
    cls = refined_interior(r)
    return ("RUNAWAY(interior %s)" % cls) if "runaway" in r else cls


def refined_interior(r):
    """noise-level eigenvalues: |E| < 1e-11 x max, or unstable between the two steps (> 10% change, i.e. truncation-
    dominated); FLAT(k) when the valley follow at the small step (0.05) moved the point by more than half the step at
    |dV| < 1e-12 |V|; ISOLATED when every eigenvalue is positive and stable (marked 'weak' below 1e-6 x max)"""
    b = r["best"]
    if b["grad_inf_after_newton"] > 1e-12:
        return "UNCONVERGED(grad %.0e, Im tau %.2f)" % (b["grad_inf_after_newton"], b["tau"][1])
    if b["n_negative"] > 0:
        return "SADDLE"
    E1, E2 = b["hess_eigs"], b["hess_eigs_step2"]; emax = max(abs(e) for e in E1)
    noise = [k for k in range(6) if abs(E1[k]) < 1e-11 * emax or abs(E1[k] - E2[k]) > 0.1 * abs(E1[k])]
    if not noise:
        return "ISOLATED" + ("" if min(E1) > 1e-6 * emax else "(weak, min %.1e)" % min(E1))
    vf = [v for v in r.get("valley_follow", []) if v["step"] == 0.05]
    if vf and max(vf[0]["fs_moved"], vf[0]["tau_moved"]) > 0.025 and abs(vf[0]["dV"]) < 1e-12 * max(abs(b["V"]), 1e-30):
        return "FLAT(%d)" % len(noise)
    return "UNRESOLVED(%d noise-level)" % len(noise)


def line(r):
    if "best" not in r:
        return "%s %-4s n=%d mu2=%.1f m0^2/mu2=%.2f lv=%.1f | %s %s" % (r["menu"], r["tnorm"], r["n"], r["mu2"], r["m02"] / r["mu2"],
                                                                      r["lv"], refined(r), r.get("runaway"))
    b = r["best"]; fn = r.get("free_numbers")
    sp = fn["speed_per_param"] if fn else {}
    return ("%s %-4s n=%d mu2=%.1f m0^2/mu2=%.2f lv=%.1f | %-9s plan:%-5s | tau=%+.5f%+.5fi mirror=%-13s | min/max eig %.1e | "
            "free rank %s %s | b2 %s | c %s" % (
                r["menu"], r["tnorm"], r["n"], r["mu2"], r["m02"] / r["mu2"], r["lv"], refined(r),
                "iso" if b["isolated"] else "flat%d" % b["n_flat"], b["tau"][0], b["tau"][1], str(b["mirror_fixed"]),
                b["min_over_max"], fn["rank"] if fn else "-",
                ("(%.2g %.2g %.2g)" % (sp.get("log mu2", 0), sp.get("log m02", 0), sp.get("log lv", 0))) if fn else "",
                "max %.1e" % max(b["b2"]), "min %.3f" % min(b["c_coefs"])))


cfgs = d["D"]["configs"]
print("== D: %d configurations" % len(cfgs))
for r in cfgs:
    print(line(r))
print()
print("== D summary by (menu, convention, n): refined classes over the primary grid (m0^2 = 0.01 mu^2) and the checks")
agg = collections.OrderedDict()
for r in cfgs:
    key = (r["menu"], r["tnorm"], r["n"])
    agg.setdefault(key, collections.Counter())[refined(r)] += 1
for key, c in agg.items():
    print("  %s %-4s n=%d: %s" % (key[0], key[1], key[2], dict(c)))
print()
print("== free-number rank and speeds (ISOLATED primary-grid points, N/sup convention)")
for menu in ("Z", "H"):
    for n in range(2, 9):
        rows = [r for r in cfgs if r["menu"] == menu and r["n"] == n and r["tnorm"] == "N" and r.get("free_numbers")
                and "runaway" not in r]
        ranks = collections.Counter(r["free_numbers"]["rank"] for r in rows)
        lv = [r["free_numbers"]["speed_per_param"]["log lv"] for r in rows]
        mu = [r["free_numbers"]["speed_per_param"]["log mu2"] for r in rows]
        m0 = [r["free_numbers"]["speed_per_param"]["log m02"] for r in rows]
        mir = collections.Counter(str(r["best"]["mirror_fixed"]) for r in rows)
        if rows:
            print("  %s n=%d: ranks %s | speed per log mu2 %.2g-%.2g, log m02 %.2g-%.2g, log lv %.2g-%.2g | mirror %s" % (
                menu, n, dict(ranks), min(mu), max(mu), min(m0), max(m0), min(lv), max(lv), dict(mir)))
print()
print("== regimes at the interior vacua (primary convention): copies with c_i < 0 (light singlets) and their b_i^2 / u*")
import sys; sys.path.insert(0, str(HERE))
from search import u_star
for r in cfgs:
    if "best" not in r or r["tnorm"] != "N":
        continue
    b = r["best"]; us = u_star(r["mu2"], r["m02"])
    neg = [(i + 1, round(c, 4), round(b["b2"][i] / us, 4)) for i, c in enumerate(b["c_coefs"]) if c < 0]
    if neg:
        print("  %s n=%d mu2=%.1f lv=%.1f m0^2/mu2=%.2f: %s -> %s" % (r["menu"], r["n"], r["mu2"], r["lv"], r["m02"] / r["mu2"],
              neg, refined(r)))
print()
for key in ("A", "B", "C"):
    if key in d:
        print("==", key, json.dumps({k: v for k, v in d[key].items() if k not in ("reading",)}, default=str)[:1500])
if "G" in d:
    print("== G")
    for k in ("n1", "n2", "n3"):
        for r in d["G"][k]:
            print("  %s at-level=%s V-bound=%.2e n_flat=%d isolated=%s min/max=%.1e" % (k, r["at_joint_level_set"], r["V_minus_bound"],
                  r["n_flat"], r["isolated"], r["min_over_max"]))
if "H" in d:
    print("== H: symmetric configurations (stationary; minimum?)")
    for m in ("menu_Z", "menu_H"):
        for n, rr in d["H"][m].items():
            print("  %s n=%s: %s" % (m, n, [(x["point"], round(x["V"], 6), "%.0e" % x["grad_inf"], x["minimum"]) for x in rr]))
L = {}
for part in ("Z", "H", "scan"):
    f = HERE / ("analysis_leading_%s.json" % part)
    if f.exists():
        L.update(json.loads(f.read_text()))
if L:
    print("== decoupling limit (lambda v -> 0); m02 speeds below the 2-D optimiser's resolution: use section D's IFT instead")
    for m in ("menu_Z", "menu_H"):
        for n, r in L.get(m, {}).items():
            s_ = r["speeds"]
            print("  %s n=%s tau0*=%.5f%+.5fi Q eigs/lv2 %s gap %.2g%s | speeds mu2 (tau %.3g, S %.3g)" % (
                m, n, r["tau0"][0], r["tau0"][1], [round(e, 5) for e in r["Q_eigs_over_lv2"]], r["Q_gap_ratio"],
                " (S* degenerate: a CP^1)" if r.get("S_star_degenerate") else "",
                s_["log mu2"]["tau_hyperbolic"], s_["log mu2"]["S_fubini_study"]))
    for row in L.get("n2_scan_menu_Z", []):
        print("  scan mu2=%.2f tau*=%.6f%+.6fi line=%s c=%s" % (row["mu2"], row["tau"][0], row["tau"][1], row["mirror_line"],
                                                               [round(c, 4) for c in row["c_coefs"]]))
