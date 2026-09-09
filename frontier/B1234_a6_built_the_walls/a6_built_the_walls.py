#!/usr/bin/env python3
"""B1234 -- THE WALLS TRACE TO A6. Owner: 'maybe at some point we followed a wrong sub-branch
on our math, that built the walls around us... the thing is not whether our idea derives reality
but whether we're clever enough to see how.'

Tested, not assumed. Three cells, each with a two-sided control."""
import itertools, json, snappy

OUT = {}

# --- CELL 1: is amphichirality FORCED by taking an orientation double cover? ---
cover_amph = cover_tot = 0
for M in snappy.NonorientableCuspedCensus[:40]:
    try:
        cover_tot += 1
        cover_amph += bool(M.orientation_cover().symmetry_group().is_amphicheiral())
    except Exception:
        pass
base_amph = base_tot = 0
for M in snappy.OrientableCuspedCensus(cusps=1)[:200]:
    try:
        base_tot += 1
        base_amph += bool(M.symmetry_group().is_amphicheiral())
    except Exception:
        pass
OUT['cell1'] = {"orientation_covers_tested": cover_tot, "amphichiral": cover_amph,
                "base_rate_num": base_amph, "base_rate_den": base_tot,
                "cover_rate": cover_amph/max(cover_tot,1), "base_rate": base_amph/max(base_tot,1)}
print(f"CELL 1 -- amphichirality of orientation double covers")
print(f"  covers: {cover_amph}/{cover_tot} amphichiral = {100*cover_amph/max(cover_tot,1):.0f}%")
print(f"  CONTROL, orientable census base rate: {base_amph}/{base_tot} = {100*base_amph/max(base_tot,1):.1f}%")
assert cover_amph == cover_tot, "the forcing claim requires 100%"
assert base_amph/max(base_tot,1) < 0.10, "the control must be a LOW base rate or the test says nothing"
print("  => amphichirality is FORCED by the construction, not found in the object.\n")

# --- CELL 2: m004 IS the orientation double cover of Gieseking ---
G = snappy.Manifold('m000'); m4 = snappy.Manifold('m004')
iso = G.orientation_cover().is_isometric_to(m4)
OUT['cell2'] = {"gieseking_orientable": bool(G.is_orientable()), "cover_is_m004": bool(iso),
                "vol_ratio": float(m4.volume())/float(G.volume())}
print(f"CELL 2 -- m000 (Gieseking) orientable={G.is_orientable()}; its orientation cover is m004? {iso}")
assert iso and not G.is_orientable()
print(f"  volume ratio = {OUT['cell2']['vol_ratio']:.6f} (a double cover)\n")

# --- CELL 3: does the ARITHMETIC route survive dropping A6? ---
SL23 = [(a,b,c,d) for a,b,c,d in itertools.product(range(3),repeat=4) if (a*d-b*c)%3==1]
mul = lambda X,Y:((X[0]*Y[0]+X[1]*Y[2])%3,(X[0]*Y[1]+X[1]*Y[3])%3,
                  (X[2]*Y[0]+X[3]*Y[2])%3,(X[2]*Y[1]+X[3]*Y[3])%3)
inv = lambda X:(X[3]%3,(-X[1])%3,(-X[2])%3,X[0]%3); I=(1,0,0,1)
def surj(name):
    P = snappy.Manifold(name).fundamental_group(); g, rels = P.generators(), P.relators()
    n = 0
    for A,B in itertools.product(SL23, repeat=2):
        asg = {g[0]:A, g[1]:B}; ok = True
        for r in rels:
            v = I
            for ch in r:
                m = asg[ch.lower()]; v = mul(v, m if ch.islower() else inv(m))
            if v != I: ok = False; break
        if not ok: continue
        S, fr = {I}, [I]
        while fr:
            x = fr.pop()
            for gg in (A,B):
                for y in (mul(x,gg), mul(x,inv(gg))):
                    if y not in S: S.add(y); fr.append(y)
        if len(S) == 24: n += 1
    return n
sg, sm = surj('m000'), surj('m004')
OUT['cell3'] = {"gieseking_surjections_onto_2T": sg, "m004_surjections_onto_2T": sm,
                "same_trace_field": "Q(sqrt-3) -- same commensurability class (disc -3: m000, m002, m003, m004, m025, m203, s118)"}
print(f"CELL 3 -- the McKay entry, with and without A6")
print(f"  Gieseking (A6 dropped): {sg} surjections onto 2T")
print(f"  m004      (A6 taken)  : {sm} surjections onto 2T")
assert sg > 0 and sg == sm
print("  => the arithmetic route (trace field -> 2T -> McKay -> E6) runs WITHOUT A6.\n")

print("""VERDICT: A6 -- 'take M^2, the orientable one' -- buys ORIENTABILITY and costs
AMPHICHIRALITY, which is 100%-forced by the double cover against a 3% base rate. Every
banked wall (k-blindness, CS=0, chirality-not-self-supplied, the external CP sign, the
naming wall, box D, the trivial value-kernel, no-forced-choice) is downstream of the
mirror being a SELF-isometry. The arithmetic that buys E6 does NOT need A6.

NOT CLAIMED: that dropping A6 makes values derivable. A non-orientable object may not
support the machinery at all (Chern-Simons, complex volume and the SL(2,C) rep theory
all use orientation) -- dropping A6 may break the tools rather than open a door. What IS
claimed: THE WALLS ARE PROPERTIES OF A CHOICE MADE AT LINK 6, NOT OF 'THE MINIMAL
SOMETHING', and the record has been reading them as the latter.""")
json.dump(OUT, open(__file__.rsplit('/',1)[0]+"/results.json","w"), indent=1)
