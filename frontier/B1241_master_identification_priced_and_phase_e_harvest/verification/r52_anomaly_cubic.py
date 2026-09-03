#!/usr/bin/env python3
"""B1241 -- fc R52 recomputed: the one-generation anomaly cubic on the anomaly-free plane (B8070's refutation numbers).

One generation Q(3,2,yQ), u^c(3bar,1,yu), e^c(1,1,ye), d^c(3bar,1,yd), L(1,2,yL); multiplicities 6,3,1,3,2.
The three linear anomaly conditions ([SU(3)]^2 U(1), [SU(2)]^2 U(1), grav^2 U(1)) cut the 5-space to a plane;
the cubic anomaly restricted to it must factor as -2 yL (2yL+3yd)(4yL-3yd)/3 (fc R52 = B8070 FINDINGS l.84,
the structure-genesis head -- B8070 is NOT on main; only the number is verified here).  Three anomaly-free lines:
hypercharge (1,-4,6,2,-3), the u<->d swap (1,2,6,-4,-3), the vector-like line yL = 0.
"""
import json, sympy as sp
yQ, yu, ye, yd, yL = sp.symbols('yQ yu ye yd yL')
mult = {yQ: 6, yu: 3, ye: 1, yd: 3, yL: 2}
su3 = 2*yQ + yu + yd            # colour triplets: Q counts twice (doublet), u^c and d^c once
su2 = 3*yQ + yL                 # doublets: Q three colours, L once
grav = sum(m*y for y, m in mult.items())
sol = sp.solve([su3, su2, grav], [yQ, ye, yu], dict=True)[0]
cubic = sp.factor(sum(m*y**3 for y, m in mult.items()).subs(sol))
target = -sp.Rational(2, 3)*yL*(2*yL + 3*yd)*(4*yL - 3*yd)
eq = sp.simplify(cubic - target) == 0
print("linear plane:", sol)
print("cubic on the plane:", cubic)
print("equals fc R52 / B8070 l.84 form:", eq)
lines = {}
for name, sub in [("hypercharge", {yd: -2*yL/3}), ("u<->d swap", {yd: 4*yL/3}), ("vector-like", {yL: 0})]:
    v = {str(k): sp.simplify(vv.subs(sub).subs(yL, -3)) for k, vv in sol.items()}
    v["yd"] = sp.simplify(yd.subs(sub).subs(yL, -3)); v["yL"] = sp.simplify(yL.subs(sub).subs(yL, -3))
    lines[name] = [str(v[k]) for k in ("yQ", "yu", "ye", "yd", "yL")]
    print(f"  {name:12s} (yQ,yu,ye,yd,yL) at yL=-3:", lines[name])
ok = eq and lines["hypercharge"] == ["1", "-4", "6", "2", "-3"] and lines["u<->d swap"] == ["1", "2", "6", "-4", "-3"] \
     and lines["vector-like"][0] == "0" and lines["vector-like"][4] == "0"
json.dump({"plane": {str(k): str(v) for k, v in sol.items()}, "cubic": str(cubic), "equals_R52_form": bool(eq), "lines": lines, "ok": ok},
          open(__file__.replace(".py", ".json"), "w"), indent=1)
print("R52 anomaly cubic:", "REPRODUCES" if ok else "DIFFERS")
