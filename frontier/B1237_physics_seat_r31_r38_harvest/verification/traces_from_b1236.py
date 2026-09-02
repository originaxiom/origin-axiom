"""C42 witness from COMMITTED material: Tr(T3^2), Tr(Y^2), Tr(T3.Y) over the SM-shaped 27
exactly as B1236's A1 landing produces it (multiset of (colour, weak, Y) irreps). No cw.py, no prime."""
import sys, importlib.util
from fractions import Fraction as F
spec = importlib.util.spec_from_file_location("b", sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
hit = m.content_internal(F(-1,3), F(1,2), F(0))          # B1236's unique hit, recomputed here
assert hit == m.TARGET and m.dim(hit) == 27
DIMC = {"1":1, "3":3, "3b":3}
t3sq = ysq = t3y = F(0)
for (c, w, y), mult in hit.items():
    dc = DIMC[c]
    if w == "2":   t3s = [F(1,2), F(-1,2)]
    else:          t3s = [F(0)]
    for t3 in t3s:
        t3sq += mult*dc*t3*t3; ysq += mult*dc*y*y; t3y += mult*dc*t3*y
print(f"Tr(T3^2) = {t3sq}  Tr(Y^2) = {ysq}  Tr(T3.Y) = {t3y}  =>  Tr(T3^2)/(Tr(T3^2)+Tr(Y^2)) = {t3sq/(t3sq+ysq)}")
print("C42 WITNESSED FROM COMMITTED B1236:", (t3sq, ysq, t3y) == (3, 5, 0))
