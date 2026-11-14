#!/usr/bin/env python3
"""SM-C12 T2: where the orientation-odd remainder survives (card relays/cards/SM_C12_the-principle-note-tested.md, pushed
before this run).  Every signed word state of length 2..8 (main's states(), B1454) at level 1: eta(T^2_M) exact (Bohn
(7)), the letter imbalance #L - #R, SnapPy's amphichirality of the punctured bundle, and the sum over the non-trivial
fixed characters of eta_A (exact).
    python3 t2_remainder.py MAIN_CHECKOUT [out.json]"""
import sys, json, math, pathlib, importlib.util, warnings
from fractions import Fraction as Fr
warnings.filterwarnings("ignore")
import snappy
HERE = pathlib.Path(__file__).resolve().parent
MAIN = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(HERE.parent / "sm_c9")); sys.path.insert(0, str(HERE.parent / "sm_c7"))
import run_c9 as C9
import run_c7 as R7


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


B = load(MAIN / "frontier/B1737_the_slope_is_a_zeta_value/verification/the_slope_is_a_zeta_value.py", "b1737")
GEN = load(MAIN / "frontier/B1454_genesis_v1_verified_and_adopted/verification/genesis_own.py", "genesis_own")
SL = B._sl()


def main():
    rows = []
    for n in range(2, 9):
        for w in GEN.states(n):
            for eps in (1, -1):
                M = [[int(x) for x in r] for r in B.abel_M(SL, eps, w, 1)]
                (a, b), (c, d) = M
                eta = C9.eta_untw(M)
                det = abs((a - 1) * (d - 1) - b * c); g = math.gcd(math.gcd(a - 1, b), math.gcd(c, d - 1)); N = det // g if det else 0
                chars = [(i, j) for i in range(N) for j in range(N) if (i, j) != (0, 0) and R7.fixed(M, i, j, N)]
                S = sum((C9.rho_467(M, (Fr((-i) % N, N), Fr((-j) % N, N))) + eta for i, j in chars), Fr(0))
                amph = bool(snappy.Manifold("b+%s%s" % ("+" if eps > 0 else "-", w)).symmetry_group().is_amphicheiral())
                rows.append({"state": ("+" if eps > 0 else "-") + w, "length": n, "trace": a + d, "eta": str(eta),
                             "imbalance": w.count("L") - w.count("R"), "amphichiral": amph, "characters": len(chars),
                             "sum_eta_A": str(S)})
    def z(r): return Fr(r["eta"]) == 0
    s = {"states": len(rows),
         "E_T2a_eta0_iff_balanced": all(z(r) == (r["imbalance"] == 0) for r in rows),
         "E_T2b_amphichiral_implies_eta0": all(z(r) for r in rows if r["amphichiral"]),
         "E_T2c_chiral_with_eta0": [r["state"] for r in rows if not r["amphichiral"] and z(r)][:20],
         "E_T2c_count": sum(1 for r in rows if not r["amphichiral"] and z(r)),
         "E_T2d_sum_eta_A_zero": all(Fr(r["sum_eta_A"]) == 0 for r in rows),
         "eta_over_imbalance": sorted({str(Fr(r["eta"]) / r["imbalance"]) for r in rows if r["imbalance"]}),
         "amphichiral_states": sum(r["amphichiral"] for r in rows)}
    json.dump({"summary": s, "rows": rows}, open(sys.argv[2] if len(sys.argv) > 2 else HERE / "t2_results.json", "w"), indent=1)
    print(json.dumps(s, indent=1))


if __name__ == "__main__":
    main()
