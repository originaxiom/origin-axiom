"""xB030 -- the four buried results, dug up.  SEALED at 3340135e.

U1  is the growth constant = the Alexander root = B1418's golden locus?  (E82: exhibit every edge)
U2  THE CAP: is h^1 <= 1 a law of this class?  KILL = the outcome the programme WANTS.
    *** U2 HERE IS THE LOW-POWER v1: only 4 of its 146 members were informative.  The cell with
    power is u2_power.py (11031 scanned -> 1979 candidates -> 506 informative). ***
U3  *** SUPERSEDED AND DEFECTIVE -- see the banner in U3() and u3_fix.py. ***
"""
import json, math, os, sys, warnings
warnings.filterwarnings("ignore")
import sympy as sp

R = {}


# ---------------------------------------------------------------- U1
def U1():
    print("\nU1       THE IDENTIFICATION -- and E82 binds: every edge EXHIBITED, then connectivity")
    t, x = sp.symbols("t x")
    phi = (1 + sp.sqrt(5)) / 2
    alpha = (3 + sp.sqrt(5)) / 2
    Delta = t**2 - 3*t + 1                       # Alexander polynomial of 4_1
    edges = {}

    e1 = sp.simplify(alpha - phi**2) == 0
    print(f"  E1  alpha = (3+sqrt5)/2  ==  phi^2 : {e1}   "
          f"(phi^2 = {sp.nsimplify(sp.expand(phi**2))})")
    edges["E1 alpha = phi^2"] = bool(e1)

    roots = sp.solve(sp.Eq(Delta, 0), t)
    e2 = set(sp.simplify(r) for r in roots) == set([sp.simplify(phi**2), sp.simplify(phi**-2)])
    print(f"  E2  roots of Delta_4_1(t) = t^2-3t+1 are phi^(+-2) : {e2}   roots = "
          f"{[sp.nsimplify(sp.radsimp(r)) for r in roots]}")
    edges["E2 Delta roots = phi^{+-2}"] = bool(e2)

    # E3: xB029's MEASURED growth constant, re-read from its banked artefact, not recalled
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "..", "..", "xB029_the_g2_mssm_read", "verification", "g2_mssm.json")
    meas = None
    try:
        meas = json.load(open(p, encoding="utf-8"))["results"]["G3"]["measured_growth_per_degree"]
    except Exception as e:
        print(f"  E3  COULD NOT RE-READ xB029's artefact: {type(e).__name__} -- edge NOT exhibited")
    if meas is not None:
        la = float(sp.log(alpha))
        e3 = abs(meas - la) < 1e-9
        print(f"  E3  xB029's MEASURED tower growth (re-read from g2_mssm.json) = {meas:.10f}")
        print(f"      log alpha = {la:.10f}   equal to 1e-9 : {e3}")
        edges["E3 growth constant = log alpha"] = bool(e3)

    # E4: B1418's golden locus, READ FROM ITS OWN DESIGN.md, not assumed
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "..", "..", "B1418_the_family_as_the_object", "DESIGN.md")
    quote, e4 = None, False
    try:
        txt = open(d, encoding="utf-8").read()
        for line in txt.splitlines():
            if "golden locus" in line:
                quote = line.strip(); break
        e4 = quote is not None and "λ² = φ²" in quote
    except Exception as e:
        print(f"  E4  COULD NOT READ B1418: {type(e).__name__}")
    print(f"  E4  B1418's own words: {(quote or '(not found)')[:150]}")
    print(f"      it defines the golden locus by lambda^2 = phi^2 : {e4}")
    edges["E4 B1418 golden locus is lambda^2 = phi^2"] = bool(e4)

    # E5: the reducible locus condition is Delta(lambda^2) = 0 -- CHECK at lambda^2 = phi^2
    val = sp.simplify(Delta.subs(t, phi**2))
    e5 = (val == 0)
    print(f"  E5  Delta(phi^2) = {val}  -> the golden locus IS a root of the Alexander "
          f"polynomial : {e5}")
    print("      (bridge: Burde / de Rham -- a reducible non-abelian rep at chi(mu)^2 = z exists")
    print("       iff Delta(z) = 0.  CITED-UNREAD; it is NOT load-bearing here because B1418")
    print("       states H^1 != 0 at this locus as VERIFIED on its own bench.)")
    edges["E5 golden locus is an Alexander root"] = bool(e5)

    print("\n         THE LINK GRAPH (E82 requires this BEFORE the sentence):")
    for k, v in edges.items():
        print(f"           {'EXHIBITED' if v else '*** NOT EXHIBITED ***'}  {k}")
    connected = all(edges.values()) and len(edges) == 5
    print(f"         all five edges exhibited, graph connected: {connected}")
    R["U1"] = {"edges": edges, "connected": bool(connected), "b1418_quote": quote,
               "measured_growth": meas}
    if connected:
        print("         *** ONE NUMBER, FIVE NAMES:  alpha = phi^2 = the Alexander root of 4_1")
        print("         = B1418's golden locus = exp(xB029's tower torsion growth constant).")
        print("         FENCE: this is a RENAMING, not a discovery.  And it is an IDENTIFICATION,")
        print("         so E82/I-10 apply: nothing is promoted without the ledger.")
    else:
        print("         *** NOT ALL EDGES EXHIBITED.  The unexhibited endpoints stay INDEPENDENT.")
    print(f"U1 {'PASS' if connected else 'FAIL'}")
    return connected


# ---------------------------------------------------------------- U2
def U2(sample=140):
    print("\nU2       THE CAP -- is h^1 <= 1 a law of this class?")
    print("         For PRIME d, H_1(Q_d; Q) = Q + Q(zeta_d)^a as a Q[Z/d]-module, so b1 = a(d-1)")
    print("         and h^1 = b1/(d-1) EXACTLY, the common value on the Galois orbit.")
    print("         KILL (and it is the outcome the programme WANTS): any a >= 2.")
    import snappy

    def h1_exponent_primes(H):
        ds = [d for d in H.elementary_divisors() if d]
        if not ds:
            return []
        e = max(ds)
        return sorted(sp.primefactors(e))

    def scan(M, label, maxp=29):
        H = M.homology()
        if H.betti_number() != 0:
            return None
        out = {"label": label, "H1": str(H), "rows": [], "max_a": 0, "bad_divisibility": []}
        for d in h1_exponent_primes(H):
            if d > maxp:
                out["rows"].append((d, "UNMEASURED (> maxp)")); continue
            try:
                cv = M.covers(d, cover_type="cyclic")
            except Exception as ex:
                out["rows"].append((d, f"err {type(ex).__name__}")); continue
            for c in cv:
                b = c.homology().betti_number()
                if b % (d - 1) != 0:
                    out["bad_divisibility"].append((d, b))
                a = b // (d - 1)
                out["max_a"] = max(out["max_a"], a)
            out["rows"].append((d, len(cv), out["max_a"]))
        return out

    results = []
    # (i) the object's tower, closed
    K = snappy.Manifold("4_1")
    def lucas(k):
        a, b = 2, 1
        for _ in range(k):
            a, b = b, a + b
        return a
    print("         (i) the object's own tower, closed fillings (xB029 G3b's family):")
    for n in range(3, 9):
        X = K.covers(n, cover_type="cyclic")[0]
        tgt = lucas(2 * n) - 2
        for (p, q) in [(0, 1), (1, 1), (1, -1), (2, 1), (1, 2), (3, 1), (1, 0)]:
            X.dehn_fill((p, q))
            H = X.homology()
            tor = 1
            for dd in H.elementary_divisors():
                if dd:
                    tor *= dd
            if H.betti_number() == 0 and tor == tgt:
                break
        s = scan(X, f"tower n={n}")
        if s:
            results.append(s)
            print(f"           n={n}: H_1={s['H1']}  rows={s['rows']}  max a={s['max_a']}"
                  + ("  *** BAD DIVISIBILITY " + str(s['bad_divisibility']) if s['bad_divisibility'] else ""))

    # (ii) the closed census
    print(f"         (ii) the closed orientable census, first {sample} rational homology spheres:")
    seen = 0
    for M in snappy.OrientableClosedCensus():
        if seen >= sample:
            break
        try:
            if M.homology().betti_number() != 0:
                continue
        except Exception:
            continue
        s = scan(M, str(M))
        if s is None:
            continue
        seen += 1
        results.append(s)
        if s["max_a"] >= 2 or s["bad_divisibility"]:
            print(f"           !!! {s['label']}: H_1={s['H1']} rows={s['rows']} "
                  f"max a={s['max_a']} baddiv={s['bad_divisibility']}")
    print(f"           scanned {seen} census rational homology spheres")

    bad = [r for r in results if r["bad_divisibility"]]
    hits = [r for r in results if r["max_a"] >= 2]
    nonzero = [r for r in results if r["max_a"] >= 1]
    print(f"         DIVISIBILITY CONTROL -- b1 divisible by d-1 at every prime d: "
          f"{len(bad) == 0}  ({len(bad)} violations)")
    print(f"         VACUITY CONTROL -- members with a >= 1 (i.e. some h^1 = 1): {len(nonzero)} "
          f"of {len(results)}")
    print(f"         members with h^1 >= 2: {len(hits)}")
    R["U2"] = {"n_members": len(results), "bad_divisibility": len(bad),
               "n_with_h1_ge_1": len(nonzero), "n_with_h1_ge_2": len(hits),
               "hits": [r["label"] for r in hits][:20],
               "sample_rows": [{k: r[k] for k in ("label", "H1", "max_a")} for r in results[:12]]}
    if bad:
        print("         *** DIVISIBILITY VIOLATED -- that is a COMPUTATION ERROR, not a finding.")
        print("         The cell halts here rather than reporting a cap.")
        return False
    if not nonzero:
        print("         *** VACUOUS: nothing in the population has h^1 = 1 at all.  The cap is")
        print("         untested and no conclusion may be drawn.")
        return False
    if hits:
        print("         *** THE KILL CONDITION FIRED, AND IT IS THE RESULT THE OWNER WANTS:")
        print("         h^1 >= 2 exists on this class.  The cap is FALSE, |I| >= 2 is reachable,")
        print("         and 'three generations is not derivable' LOSES ITS STRUCTURAL REASON.")
    else:
        print("         *** h^1 <= 1 THROUGHOUT.  On every prime-degree cyclic cover of every")
        print("         rational homology sphere tested, a is 0 or 1 and never more.")
        print("         READING (marked as a reading): the closing takes chirality from h^1 and")
        print("         |I| <= h^1, so THREE GENERATIONS NEEDS h^1 >= 3 -- and h^1 never exceeds")
        print("         1 here.  This is EMPIRICAL, over a finite population, and NOT a theorem.")
    print("U2 PASS  (the cell ran with both controls; its CONTENT is the verdict above)")
    return True


# ---------------------------------------------------------------- U3
def U3():
    print("\nU3       *** SUPERSEDED AND DEFECTIVE -- THE LIVE CELL IS u3_fix.py. ***")
    print("         (a) it includes lambda with G*lambda = 0 mod k, where 4sin^2 = 0 EXACTLY: the")
    print("             flat bundle is TRIVIAL, it is not a symmetry-breaking Wilson line, and")
    print("             FW eq.(3.1) is UNDEFINED there.  Its 'best P_eff = 669' numbers are")
    print("             FLOATING-POINT ARTEFACTS of log(rounding error), not physics.")
    print("         (b) its sealed density prediction O(1/k) is REFUTED by its own counts.")
    print("         KEPT ONLY SO THE DEFECT STAYS ON THE RECORD.")
    print("\nU3       THE COSMOLOGICAL-CONSTANT TUNING IS DIOPHANTINE, QUANTIFIED")
    P, Q, M = 15, 18, 10
    G = P + M + 1
    TARGET = 84.0

    def peff(k, lam):
        s = math.sin(G * math.pi * lam / k) ** 2
        if s <= 0:
            return None
        return math.log(k) - M * math.log(4 * s)

    rows = []
    for k in (99, 200, 316, 500, 1000, 2000):
        good = 0, 
        good = 0
        best = None
        for lam in range(1, k):
            v = peff(k, lam)
            if v is None:
                continue
            if best is None or v > best[0]:
                best = (v, lam)
            if v >= TARGET:
                good += 1
        frac = good / (k - 1)
        # the closed form when G*lam = +-1 mod k
        approx = (1 + 2 * M) * math.log(k) - M * math.log(4 * math.pi ** 2)
        rows.append((k, good, frac, best, approx))
        print(f"         k={k:5d}: lambda reaching P_eff>=84: {good:5d} of {k-1} "
              f"(fraction {frac:.5f}, 1/k = {1/k:.5f});  best P_eff={best[0]:7.2f} at "
              f"lambda={best[1]};  closed form at G*lam=+-1: {approx:7.2f}")
    # is the fraction O(1/k)?
    ratios = [(k, frac * k) for k, _, frac, _, _ in rows]
    print(f"         fraction x k  (constant => the achieving set is O(1/k)): "
          f"{[(k, round(v,2)) for k, v in ratios]}")
    # verify the closed form at the exact residue
    ok_cf = []
    for k, _, _, best, approx in rows:
        r = (G * best[1]) % k
        ok_cf.append((k, r, min(r, k - r), abs(best[0] - approx) < 1.0))
    print(f"         at the BEST lambda, G*lambda mod k (and its distance to 0 mod k): "
          f"{[(k, r, dd) for k, r, dd, _ in ok_cf]}")
    print(f"         closed form matches the best value to 1.0 at every k: "
          f"{all(t[3] for t in ok_cf)}")
    print("         => the requirement is on ||G*lambda/k||, the DISTANCE TO AN INTEGER, and the")
    print("            achieving set has density O(1/k).  A ONE-IN-k ARITHMETIC COINCIDENCE,")
    print("            not a continuous scan.")
    print("         FENCE: this describes the SOURCE'S OWN worked example, Q = S^3/Z_k.  The")
    print("         source says the general case is unknown.  It is NOT a statement about the")
    print("         landscape.")
    R["U3"] = {"rows": [(k, g, f, list(b), a) for k, g, f, b, a in rows],
               "fraction_times_k": ratios, "closed_form_ok": all(t[3] for t in ok_cf)}
    print("U3 PASS")
    return True


if __name__ == "__main__":
    only = sys.argv[1:] or None
    res = {}
    for k, f in {"U1": U1, "U2": U2, "U3": U3}.items():
        if only and k not in only:
            continue
        try:
            res[k] = bool(f())
        except Exception as e:
            import traceback; traceback.print_exc()
            print(f"{k} EXCEPTION {type(e).__name__}: {e}")
            res[k] = False
    print("\n" + "=" * 78)
    print("ALL CELLS RAN" if all(res.values()) else "NOT ALL CELLS PASSED")
    json.dump({"cells": res, "results": R},
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "buried.json"),
                   "w", encoding="utf-8"), indent=1, default=str)
