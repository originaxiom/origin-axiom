"""D9 verification: proper chirality test over B1186's 112-family.
Method: SnapPy symmetry_group().is_amphicheiral() (uses orientation-reversing self-isometries
of the canonical triangulation), cross-checked by Chern-Simons: CS != 0 mod 1/2 forces chirality
(amphichiral => CS in {0, 1/4} mod 1/2 -- B1224). Controls: m004 (amphichiral, CS 0), m015 = 5_2 (chiral).
"""
import json, snappy
fam = json.load(open("frontier/B1186_family_is_112/verification/family_census.json"))["members_B"]
assert len(fam) == 112
def probe(name):
    M = snappy.Manifold(name)
    try:
        amph = M.symmetry_group().is_amphicheiral()
        order = M.symmetry_group().order()
    except Exception as e:
        amph, order = None, str(e)[:40]
    cs = float(M.chern_simons())
    # normalize CS mod 1/2 to (-1/4, 1/4]
    r = (cs + 0.25) % 0.5 - 0.25
    h1 = str(M.homology())
    return amph, order, cs, r, h1
print("controls:")
for c in ["m004", "m015"]:
    print(" ", c, probe(c))
rows = []
n_amph = n_chir = n_und = 0
for nm in fam:
    a, o, cs, r, h1 = probe(nm)
    rows.append((nm, a, o, cs, r, h1))
    if a is True: n_amph += 1
    elif a is False: n_chir += 1
    else: n_und += 1
print(f"\n112-family: amphichiral {n_amph}  chiral {n_chir}  undecided {n_und}")
print("\nnamed witnesses:")
for nm in ["o10_150700", "t12840", "s955", "m202", "s118", "m004", "m003"]:
    for row in rows:
        if row[0] == nm: print(" ", row)
# consistency: any 'amphichiral' with CS not in {0,1/4} mod 1/2 would contradict B1224
bad = [r for r in rows if r[1] is True and min(abs(r[4]), abs(abs(r[4])-0.25)) > 1e-6]
print("\namphichiral-but-CS-forbidden (should be empty):", bad)
# chiral rows with CS = 0 or 1/4 (chiral but CS silent) -- these are the ones mirror-isometry would miss anyway
sil = [r[0] for r in rows if r[1] is False and min(abs(r[4]), abs(abs(r[4])-0.25)) < 1e-6]
print("chiral with CS in {0,1/4} (CS-silent chirality):", len(sil), sil[:12])
json.dump([dict(name=r[0], amphicheiral=r[1], sym_order=r[2], cs=r[3], h1=r[5]) for r in rows],
          open("chirality_112.json","w"), indent=1)
