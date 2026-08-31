"""B1226 Cell 2 -- the SM parameter count is a CATEGORY ERROR (owner, 2026-08-31).

"19 parameters" / "26 parameters" is a flat list of things that are not the same
KIND of thing.  Type each one by THIS PROGRAMME'S OWN law -- B1168: an object-canonical
quantity is beta-even AND dimensionless -- and the flat list splits into four boxes with
four different suppliers.  Nothing here is a physics claim; it is a typing of the target.
"""
import json
from collections import defaultdict

# (name, n_copies, dimensionful, cp_odd, scale_anchored, note)
P = [
 ("gauge couplings g1,g2,g3", 3, False, False, True,  "dimensionless but RUN: need a renormalisation point, itself a scale"),
 ("theta_QCD",                1, False, True,  False, "CP-odd, dimensionless, no scale needed"),
 ("quark masses u,d,s,c,b,t", 6, True,  False, True,  ""),
 ("charged lepton masses",    3, True,  False, True,  ""),
 ("CKM angles th12,th13,th23",3, False, False, False, ""),
 ("CKM phase delta",          1, False, True,  False, "CP-odd"),
 ("Higgs vev v",              1, True,  False, False, ""),
 ("Higgs mass m_H",           1, True,  False, False, ""),
 ("neutrino masses",          3, True,  False, True,  "beyond the 19"),
 ("PMNS angles",              3, False, False, False, "beyond the 19"),
 ("PMNS phase delta",         1, False, True,  False, "CP-odd; beyond the 19"),
 ("Newton G (or M_Pl)",       1, True,  False, False, "the force the SM omits"),
 ("cosmological constant L",  1, True,  False, False, "the force the SM omits"),
]

def box(dimful, cpodd, scaled):
    if dimful:            return "C-DIMENSIONFUL"      # the scale wall
    if cpodd:             return "D-BETA-ODD"          # the untried box
    if scaled:            return "B-SCALE-ANCHORED"    # dimensionless but needs a point
    return "A-BETA-EVEN-PURE"                          # B1225's proved-closed box

SUPPLIER = {
 "A-BETA-EVEN-PURE":  ("NOBODY -- object CANNOT SELECT (B1225 no-canonical-selector, PROVED)",
                       "object-canonical by B1168, but selection within the class is impossible"),
 "B-SCALE-ANCHORED":  ("READER -- object is scale-blind (B811 H128 kill: scale-free cannot emit scale-dependent)", ""),
 "C-DIMENSIONFUL":    ("READER -- the scale wall (B1226 cell 1: contingent on CS=0, NOT a symmetry)", ""),
 "D-BETA-ODD":        ("OBJECT CONSTRAINS -- amphichirality forces a Z/2 (B1224); object gives a BIT, not a value", ""),
}

tot = defaultdict(int); members = defaultdict(list)
for name, n, d, c, s, note in P:
    b = box(d, c, s); tot[b] += n; members[b].append((name, n, note))

sm19 = sum(n for name,n,*_ in P if "beyond" not in P[[p[0] for p in P].index(name)][5] and "omits" not in P[[p[0] for p in P].index(name)][5])
counts = {"SM_19": 19, "with_Dirac_neutrinos_26": 26, "plus_gravity_and_Lambda_28": sum(n for _,n,*_ in P)}

print("THE FLAT COUNT:", counts)
print("\nTHE TYPED COUNT -- four boxes, four suppliers:\n")
for b in ["A-BETA-EVEN-PURE","B-SCALE-ANCHORED","C-DIMENSIONFUL","D-BETA-ODD"]:
    print(f"  [{b}]  {tot[b]} parameters")
    for nm,n,note in members[b]:
        print(f"      {n}x  {nm}{('   -- '+note) if note else ''}")
    print(f"      SUPPLIER: {SUPPLIER[b][0]}\n")

# MB12 bite control: the classifier must be able to put things in every box, and
# must be able to FAIL to do so.  Vacuous iff any box is empty or one box holds all.
nonempty = sum(1 for b in tot if tot[b] > 0)
vacuous  = (nonempty < 2) or (max(tot.values()) == sum(tot.values()))
print(f"MB12 bite: boxes occupied {nonempty}/4 ; vacuous={vacuous} (a flat count would give 1/4)")

res = {"flat_counts": counts, "boxes": {b: {"n": tot[b], "members": members[b],
        "supplier": SUPPLIER[b][0]} for b in tot},
       "mb12": {"boxes_occupied": nonempty, "vacuous": vacuous},
       "beta_odd_members": [m[0] for m in members["D-BETA-ODD"]],
       "beta_odd_count": tot["D-BETA-ODD"]}
json.dump(res, open("frontier/B1226_the_beta_odd_box/cell2_results.json","w"), indent=2)
