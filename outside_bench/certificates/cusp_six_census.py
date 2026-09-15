#!/usr/bin/env python3
"""SIX CUSPS -- and whether going there restores what B1064 deleted.

Seal: outside_bench/seals/CUSP_SIX_PREREG.md (pushed before this ran).

B1190/GC-6 types the sigma gap as "six cusp-boson units where T[4_1] supplies one", the ONE
attributed to m004 having one cusp; B139 banks "coupling count = cusp count".  So: go to a
six-cusped cover.  But B1064 names a DEEPER obstruction -- the object's amphichirality forces
CS = 0, so d/dk S == 0, the quantized sector is deleted, and (E6)_1 is quantized-sector content.
A cover is not "the object's own action", so a cover is the natural candidate for B1064's
route (a).  This tests it.

C-1  do six-cusped covers exist, and at what degree?
C-2  does any cover carry CS != 0 -- i.e. does the cover route restore the quantized sector?
C-3  the volume ledger, in the banked units V_reg = Vol(m004)/2 and Vol_orb = Vol(m004)/12.

Gate 5 untouched: pure topology. No measured value.
"""
import sys, collections
import snappy

MAXDEG = int(sys.argv[1]) if len(sys.argv) > 1 else 6
M = snappy.Manifold("m004")
VOL = M.volume()
V_REG = VOL / 2
VOL_ORB = VOL / 12
CS0 = M.chern_simons()
print(f"base m004 : cusps {M.num_cusps()}  vol {float(VOL):.16f}  CS {float(CS0):.3e}")
print(f"units     : V_reg = Vol/2 = {float(V_REG):.16f}   Vol_orb = Vol/12 = {float(VOL_ORB):.16f}")
print(f"searching covers to degree {MAXDEG}\n")

rows = []
for deg in range(2, MAXDEG + 1):
    try:
        cov = M.covers(deg)
    except Exception as e:
        print(f"  degree {deg}: enumeration failed ({e})"); continue
    print(f"  degree {deg}: {len(cov)} covers", flush=True)
    for C in cov:
        try:
            nc = C.num_cusps(); v = float(C.volume()); cs = float(C.chern_simons())
        except Exception:
            nc, v, cs = C.num_cusps(), None, None
        rows.append((deg, C.name(), nc, v, cs, ""))

print("\n" + "=" * 78)
print("C-1  CUSP COUNTS BY DEGREE")
print("=" * 78)
bydeg = collections.defaultdict(collections.Counter)
for deg, name, nc, v, cs, ct in rows:
    bydeg[deg][nc] += 1
for deg in sorted(bydeg):
    print(f"     degree {deg}: " + "  ".join(f"{n}cusp x{c}" for n, c in sorted(bydeg[deg].items())))
six = [r for r in rows if r[2] == 6]
C1 = "C1-SIX-EXISTS" if six else "C1-NO-SIX"
print(f"\n     covers with EXACTLY SIX cusps: {len(six)}")
if six:
    mind = min(r[0] for r in six)
    print(f"     minimal degree carrying six cusps: {mind}")
    for r in sorted(six)[:8]:
        print(f"       deg {r[0]}  {r[1]:<22} cusps {r[2]}  vol {r[3]:.10f}  CS {r[4]:.3e}  [{r[5]}]")
print(f"\n     MAX cusps achievable, by degree (the datum the ask needs):")
for deg in sorted(bydeg):
    print(f"       degree {deg}: max cusps = {max(bydeg[deg])}")
print(f"     OUTCOME: {C1}   (searched to degree {MAXDEG})")

print("\n" + "=" * 78)
print("C-2  DOES ANY COVER RESTORE THE QUANTIZED SECTOR?  (CS != 0)")
print("=" * 78)
TOL = 1e-9
nz = [r for r in rows if r[4] is not None and abs(r[4]) > TOL]
print(f"     covers examined                : {len(rows)}")
print(f"     covers with |CS| > {TOL:g}        : {len(nz)}")
mx = max((abs(r[4]) for r in rows if r[4] is not None), default=0.0)
print(f"     max |CS| over all covers       : {mx:.3e}")
C2 = "C2-ALL-ZERO" if not nz else "C2-SOME-NONZERO"
print(f"     OUTCOME: {C2}")
if C2 == "C2-ALL-ZERO":
    print("     => CS(M~) = d*CS(m004) = 0 on every cover examined: d/dk S == 0 SURVIVES the cover,")
    print("        the quantized sector stays deleted, and B1064's route (a) VIA COVERS is CLOSED.")
    print("        Six cusps are AVAILABLE and DO NOT HELP.")
else:
    for r in nz[:10]:
        print(f"       deg {r[0]}  {r[1]}  cusps {r[2]}  CS {r[4]:.3e}   <-- EXHIBIT for route (a)")

print("\n" + "=" * 78)
print("C-3  THE VOLUME LEDGER (banked units)")
print("=" * 78)
print(f"     {'deg':>3} {'name':<22} {'cusps':>5} {'vol/V_reg':>12} {'vol/Vol_orb':>12}")
seen = set()
for r in sorted(rows):
    if r[3] is None: continue
    key = (r[0], r[2])
    if key in seen: continue
    seen.add(key)
    print(f"     {r[0]:>3} {r[1]:<22} {r[2]:>5} {float(r[3])/float(V_REG):>12.4f} {float(r[3])/float(VOL_ORB):>12.4f}")

print("\n" + "=" * 78)
print(f"SUMMARY: {C1} | {C2}")
print("=" * 78)
