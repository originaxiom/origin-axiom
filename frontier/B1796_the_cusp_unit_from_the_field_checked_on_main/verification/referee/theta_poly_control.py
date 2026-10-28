"""Referee B1796 -- negative control for theta_poly_route.py: with the S-law's sign flipped (a multiplier that is not
rho_R's), the equivariant counts must differ from the free-module counts; with the right sign they agree.
    python3 -B theta_poly_control.py"""
import sys, types, pathlib
HERE = pathlib.Path(__file__).resolve().parent
src = (HERE / "theta_poly_route.py").read_text()
head = src.split('print("completeness')[0]          # definitions only
ns = {}
exec(compile(head, "theta_poly_route_defs", "exec"), ns)
right = {d: len(ns["space"](d, "basis")[1]) for d in (1, 3, 5, 7, 9)}
flipped_src = head.replace("epsS = (-I) ** (1 - d)", "epsS = -((-I) ** (1 - d))")
assert flipped_src != head
ns2 = {}
exec(compile(flipped_src, "theta_poly_route_flipped", "exec"), ns2)
flipped = {d: len(ns2["space"](d, "basis")[1]) for d in (1, 3, 5, 7, 9)}
fm = {d: ns["dimM"](d - 1) + ns["dimM"](d - 3) + ns["dimM"](d - 5) for d in (1, 3, 5, 7, 9)}
print("free module:", fm)
print("right sign :", right, "agree:", right == fm)
print("S flipped  :", flipped, "differs:", flipped != fm)
