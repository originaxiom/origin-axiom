#!/usr/bin/env python3
"""B718 label check (B1235 addendum, 2026-09-02): is the constant C in b718_probe4.py
'pi^2 * (cusp longitude)' or 'pi^2 * (cusp AREA)'?

The dimensional argument decides it without a computation: the probe forms C / L^2 with L a
length on the cusp torus; C / L^2 is dimensionless only if C carries the weight of an AREA
(weight +2 under g -> k^2 g, the B1022 weight ledger), never a length. The numerics below show
WHY the label slipped: at m004's maximal cusp the longitude LENGTH and the cusp AREA are the
same number, 2*sqrt(3) = 3.4641..., because |meridian| = 1 there. Same number, different weight.
"""
import math
import snappy

M = snappy.Manifold("m004")
M.set_peripheral_curves("shortest")
area = float(M.cusp_areas()[0])
tr = M.cusp_translations()[0]                 # (meridian, longitude) translations at the max cusp
mer, lon = abs(complex(tr[0])), abs(complex(tr[1]))
print(f"m004 maximal cusp: |meridian| = {mer:.6f}   |longitude| = {lon:.6f}   area = {area:.6f}")
print(f"2*sqrt(3) = {2*math.sqrt(3):.6f}")
same = abs(lon - area) < 1e-6 and abs(mer - 1.0) < 1e-6
print(f"|longitude| == area at the maximal cusp: {same}   (because |meridian| = 1 there)")
print("weight under g -> k^2 g: |longitude| +1, area +2, C/L^2 dimensionless requires C ~ area (+2).")
print("VERDICT: the Neumann-Zagier constant labelled 'pi^2 * (cusp longitude)' at b718_probe4.py:95"
      " is pi^2 * (cusp AREA) -- deficit ~ pi^2 A / L^2 (Neumann-Zagier), A = 2*sqrt(3) at the"
      " maximal cusp. Line 148 (12 = |longitude|^2 inside L^2 = 12 + p^2) is CORRECT as written:"
      " there the longitude LENGTH is what enters. One label corrected; no value changes.")
