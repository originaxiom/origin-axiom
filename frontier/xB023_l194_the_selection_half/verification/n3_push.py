"""xB023 Addendum 2, N3 residue: the four homology-sphere fillings N3 left UNDECIDED.

Calibration is built in and is the point:
  m004(1,0)  = S^3                        -- a trivial group MUST collapse under randomisation
  m004(1,1)  = +1 surgery on the figure-8 -- a NON-trivial homology sphere (Brieskorn Sigma(2,3,7)),
                                             2 generators, MUST NOT collapse
The target's four slopes are then read against those two behaviours.
"""
import warnings

warnings.filterwarnings("ignore")
import snappy

TRIES = 60


def push(name, slope):
    M = snappy.Manifold(name)
    M.dehn_fill(slope)
    st = M.solution_type()
    best = None
    rel0 = None
    for i in range(TRIES):
        try:
            G = M.fundamental_group(simplify_presentation=True)
            ng, nr = G.num_generators(), len(G.relators())
            if rel0 is None:
                rel0 = list(G.relators())
            if best is None or (ng, nr) < best:
                best = (ng, nr)
            if ng == 0:
                break
        except Exception:
            pass
        try:
            M.randomize()
        except Exception:
            break
    closed_id = ""
    try:
        closed_id = str(snappy.OrientableClosedCensus.identify(M))
    except Exception as e:
        closed_id = f"err {type(e).__name__}"
    return st, best, rel0, closed_id


print("N3-RESIDUE   pushing the undecided homology-sphere fillings, %d randomisations each" % TRIES)
print("%-14s %-8s %-40s %-22s %s" % ("manifold", "slope", "solution type", "best (gens,rels)", "closed-census id"))
cases = [("m004", (1, 0), "CALIBRATION +ve: this IS S^3"),
         ("m004", (1, 1), "CALIBRATION -ve: +1 surgery on 4_1, a non-trivial homology sphere"),
         ("o10_143849", (1, 0), ""), ("o10_143849", (-1, 0), ""),
         ("o10_143849", (0, 1), ""), ("o10_143849", (0, -1), "")]
res = {}
for nm, sl, note in cases:
    st, best, rel0, cid = push(nm, sl)
    res[(nm, sl)] = (st, best, cid)
    print("%-14s %-8s %-40s %-22s %s" % (nm, str(sl), st, str(best), cid))
    if note:
        print("               %s" % note)
    if rel0:
        print("               relators: %s" % [r[:60] for r in rel0][:4])

pos = res[("m004", (1, 0))][1]
neg = res[("m004", (1, 1))][1]
print()
print("CALIBRATION READ:")
print("  S^3 collapses to %s ; the non-trivial homology sphere stalls at %s" % (pos, neg))
ok = (pos[0] == 0 and neg[0] > 0)
print("  calibration valid (S^3 collapses, non-S^3 does not): %s" % ok)
tgt = [res[("o10_143849", s)][1] for s in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
print("  target's four slopes: %s" % tgt)
print("  any target slope collapsed to the trivial group: %s" % any(b[0] == 0 for b in tgt))
