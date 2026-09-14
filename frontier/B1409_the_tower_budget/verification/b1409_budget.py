"""
B1409 -- the tower's parameter budget at its ceiling.  Sealed 5618216a before compute.

sl_2 = Sym^2 V  and, under the principal SL(2) in SL(3),  sl_3 = Sym^2 V + Sym^4 V,
so the budget is  dim H^1(pi_1(M), Sym^{2j} V)  for j = 1, 2  at the geometric holonomy V.

Machinery reused verbatim from B1333 (exact over Q(zeta_12), no tolerance anywhere):
  recogmc.exact_rho   -- PSLQ recognition of the holonomy
  fi_lib.sym          -- symmetric powers
  mcexact.analyse_exact -- returns a1 = |Z^1| - (d - a0) = dim H^1, and per-cusp t0/t1
"""
import os, sys, json, warnings
warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__))
B1333 = os.path.join(os.path.dirname(os.path.dirname(HERE)),
                     "B1333_the_index_on_several_cusps", "verification")
sys.path.insert(0, B1333)
import snappy
from recogmc import exact_rho
from fi_lib import sym
from mcexact import analyse_exact

TARGETS = [
    ("m004",        None, "positive control: k = 1 is known"),
    ("cover[17]",     17, "L14n63694 -- CHIRAL, 5 cusps  (THE TARGET)"),
    ("cover[32]",     32, "the same manifold, a second presentation -- must agree"),
    ("cover[34]",     34, "otet20_00571 -- amphichiral control, 5 cusps"),
]
GERMS = [2, 4]          # Sym^2 (= sl_2) and Sym^4 ; sl_3 = Sym^2 + Sym^4

def manifold(idx):
    M0 = snappy.Manifold("m004")
    return M0 if idx is None else M0.covers(10)[idx]

out, halted = {}, []
for name, idx, why in TARGETS:
    M = manifold(idx)
    k = M.num_cusps()
    print(f"\n=== {name}: {why} ===")
    print(f"    cusps k = {k}, tets = {M.num_tetrahedra()}")
    got = exact_rho(M)
    if got is None:
        print("    HALT: PSLQ did not recognise the holonomy over Q(zeta_12). "
              "No float fallback (kill condition C1).")
        halted.append(name); out[name] = {"halt": True, "cusps": k}
        continue
    Mh, G, gens, rels, per, rho = got
    print(f"    recognised exactly: {len(gens)} generators, {len(rels)} relators, "
          f"{len(per)} peripheral pairs")
    row = {"cusps": k, "gens": len(gens), "rels": len(rels), "H1": {}}
    for m in GERMS:
        d = m + 1
        V = {g: sym(rho[g], m) for g in gens}
        A = analyse_exact(gens, rels, per, V, d)
        row["H1"][f"Sym^{m}"] = {"a1": A["a1"], "a0": A["a0"], "d": d,
                                 "t0s": A["t0s"], "t1s": A["t1s"]}
        flag = "" if A["a0"] == 0 else "   <-- a0 != 0, NOT irreducible (kill condition)"
        print(f"    Sym^{m} (d={d}):  dim H^1 = a1 = {A['a1']}   a0 = {A['a0']}"
              f"   per-cusp t0 = {A['t0s']}  t1 = {A['t1s']}{flag}")
    tot = sum(v["a1"] for v in row["H1"].values())
    row["sl2_dim"] = row["H1"]["Sym^2"]["a1"]
    row["sl3_dim"] = tot
    print(f"    => SL(2) budget dim_C H^1(sl_2) = {row['sl2_dim']}   "
          f"(Thurston predicts k = {k})")
    print(f"    => SL(3) budget dim_C H^1(sl_3) = {tot}   "
          f"(Menal-Ferrer-Porti predicts k(n-1) = {2*k})")
    out[name] = row

print("\n" + "=" * 72)
print("THE TWO-OUTCOME, read against the sealed prereg")
print("=" * 72)
ok = True
if halted:
    print(f"  HALTED on: {halted}  -> no dimension banked for those")
ctrl = out.get("m004", {})
if ctrl and not ctrl.get("halt"):
    good = ctrl["sl2_dim"] == 1
    ok &= good
    print(f"  positive control m004: SL(2) dim = {ctrl['sl2_dim']}, k = 1  "
          f"-> {'PASS' if good else 'FAIL -- the instrument is wrong'}")
a, b = out.get("cover[17]"), out.get("cover[32]")
if a and b and not a.get("halt") and not b.get("halt"):
    agree = (a["sl2_dim"], a["sl3_dim"]) == (b["sl2_dim"], b["sl3_dim"])
    ok &= agree
    print(f"  the two isometric presentations agree: {agree} "
          f"({a['sl2_dim']},{a['sl3_dim']}) vs ({b['sl2_dim']},{b['sl3_dim']})")
for nm in ("cover[17]", "cover[34]"):
    r = out.get(nm)
    if r and not r.get("halt"):
        print(f"  {nm}: SL(2) = {r['sl2_dim']} (expect 5),  SL(3) = {r['sl3_dim']} (expect 10)"
              f"   -> {'as the theorems say' if (r['sl2_dim'], r['sl3_dim']) == (5, 10) else 'DEVIATION'}")
json.dump(out, open(os.path.join(HERE, "b1409_budget.json"), "w"), indent=1)
print(f"\n  wrote b1409_budget.json")
