"""B1703 (P-250): the corrected laws, tested on fresh data.  The first census's printed prediction failed in two places
(u = e at order 7; every sector's R_1 = 0 at order 3).  The corrected laws, inferred from that census and printed before
this loop: d = e iff N | 4 or N | 5; u = d iff N | 6; u = e iff N | 2 or N | 7 (the pair's twists up to swap and
negation); sector s protected (R_1 = 0) iff N | delta_s or N | 3 (delta = q_L - q_R: up 5, down 1, leptons 9; 3 = the
Higgs's charge = |q_L + q_R|).  Set A: a fresh tau = 0.41 + 2.9i, orders 1-9, 14, 21.  Set B (a read-out, no prediction):
tau = omega, orders 1-12, against W88's {9, 11, 12}."""
import sys, json, math, pathlib
from fractions import Fraction as Fr
from multiprocessing import Pool
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); _argv = sys.argv; sys.argv = ['x']
import the_line_census as C
sys.argv = _argv
def lines_of(orders): return [(Fr(j, N), Fr(k, N), N) for N in orders for j in range(N) for k in range(N) if math.gcd(math.gcd(j, k), N) == 1]
def law(N):
    return {"d=e": 4 % N == 0 or 5 % N == 0, "u=d": 6 % N == 0, "u=e": 2 % N == 0 or 7 % N == 0,
            "up": 5 % N == 0 or 3 % N == 0, "down": 1 % N == 0 or 3 % N == 0, "lep": 9 % N == 0 or 3 % N == 0}
def run(tag, tau, orders, nw):
    C.TAUS[:] = [tau]; C.LINES[:] = lines_of(orders)
    with Pool(nw) as P: rows = P.map(C.point, [(k, 0) for k in range(len(C.LINES))], chunksize=4)
    by = {}
    for r in rows:
        N = C.LINES[r["line"]][2]; e = by.setdefault(N, {"lines": 0, "d=e": 0, "u=d": 0, "u=e": 0, "all_split": 0, "up": 0, "down": 0, "lep": 0})
        de, ud, ue = C.same(r["down"], r["lep"]), C.same(r["up"], r["down"]), C.same(r["up"], r["lep"])
        e["lines"] += 1; e["d=e"] += de; e["u=d"] += ud; e["u=e"] += ue; e["all_split"] += not (de or ud or ue)
        for s in ("up", "down", "lep"): e[s] += r[s + "_R1_rel"] < 1e-9
    return by
if __name__ == "__main__":
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    print("corrected laws: d=e iff N|4 or N|5; u=d iff N|6; u=e iff N|2 or N|7; protected iff N|delta or N|3")
    A = run("A", complex(0.41, 2.9), list(range(1, 10)) + [14, 21], nw)
    okA = all(all((A[N][k] == A[N]["lines"]) == v and A[N][k] in (0, A[N]["lines"]) for k, v in law(N).items()) for N in A)
    okA = okA and all((A[N]["all_split"] == A[N]["lines"]) == (not any(law(N)[k] for k in ("d=e", "u=d", "u=e"))) for N in A)
    for N in sorted(A): print("A", N, A[N])
    print("set A: the corrected laws hold on every line:", okA)
    Bw = run("B", complex(-0.5, math.sqrt(3) / 2), list(range(1, 13)), nw)
    for N in sorted(Bw): print("B (omega)", N, Bw[N])
    json.dump({"A": {str(k): v for k, v in A.items()}, "A_laws_hold": okA, "B_omega": {str(k): v for k, v in Bw.items()}},
              open(HERE / "the_confirmation.json", "w"), indent=1)
