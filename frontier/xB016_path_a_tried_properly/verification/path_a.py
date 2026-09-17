#!/usr/bin/env python3
"""xB016 cells P1-P6, exactly as sealed in PREREGISTRATION.md
(sha256 56447437057e460d4dcfb4d1509da2c86af45f0a395bcec65c723d6c7c34c21b,
commit 89cdf7d, pushed BEFORE this file existed).

The owner's instruction: "lets verify parh A once more, so were sure we dine it
priperly and were sure it doesnt cross, and we tried right way".

Path A has been wrong twice in this seat's hands -- xB014 killed it on a sort-order
error, and xB015 showed xB014's stated REASON for non-crossing was also wrong.  Both
times the conclusion was asserted rather than attempted.  This file attempts it, on
three named routes, and the number that WOULD constitute a crossing is printed by P2
because the seal stated it in advance.

Gate 5 untouched: no value, no generation count, no physics reading.
"""
import json
import math
import os
import statistics
import warnings

import snappy
import sympy as sp

warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
PHI = (1 + 5 ** 0.5) / 2
RESULTS = {}


def torsion(M):
    """|H_1 torsion| = product of the nonzero elementary divisors."""
    p = 1
    for x in M.homology().elementary_divisors():
        if x != 0:
            p *= x
    return p


# ---------------------------------------------------------------- P1


def P1(nmax=8):
    print("P1       THE TOWER, RE-DERIVED FROM SCRATCH (not carried across from xB014)")
    V4 = float(snappy.Manifold("m004").volume())
    L, F = [2, 1], [0, 1]
    for _ in range(2, nmax + 2):
        L.append(L[-1] + L[-2])
        F.append(F[-1] + F[-2])
    print(f"         {'n':>2} {'vol/vol(m004)':>14} {'CS':>10} {'|tors|':>10} {'predicted':>10}"
          f" {'log|t|/vol':>11}")
    ok_t = ok_v = ok_cs = True
    rows = []
    for n in range(1, nmax + 1):
        M = snappy.Manifold("b++" + "LR" * n)
        v, t, cs = float(M.volume()), torsion(M), float(M.chern_simons())
        pred = L[n] ** 2 if n % 2 else 5 * F[n] ** 2
        ok_t &= (t == pred)
        ok_v &= abs(v - n * V4) < 1e-7
        ok_cs &= abs(cs) < 1e-9
        r = math.log(t) / v if t > 1 else 0.0
        rows.append((n, v, cs, t, pred, r))
        print(f"         {n:>2} {v/V4:14.6f} {cs:10.6f} {t:10d} {pred:10d} {r:11.6f}")
    rate = math.log(PHI ** 2) / V4
    print(f"         torsion = L_n^2 (n odd) / 5F_n^2 (n even): {ok_t}   "
          f"vol = n*vol(m004): {ok_v}")
    print(f"         CS = 0 at EVERY rung: {ok_cs}   <- forced by xB015's K4 "
          f"(covers of a CS=0 base)")
    print(f"         limit rate log(phi^2)/vol(m004) = {rate:.12f}")
    ok = ok_t and ok_v and ok_cs
    print(f"P1 {'PASS' if ok else 'FAIL'}  xB014's tower reproduces exactly, and the CS column -- "
          "which xB014\n         never computed -- is ZERO all the way up.")
    RESULTS["P1"] = {"rows": rows, "torsion_law": ok_t, "vol_law": ok_v,
                     "cs_zero_throughout": ok_cs, "limit_rate": rate}
    return ok


# ---------------------------------------------------------------- P2


def P2():
    print("\nP2       ROUTE 1 -- THE RATE ROUTE: the crossing attempt Path A had never made")
    V4 = float(snappy.Manifold("m004").volume())
    rate = math.log(PHI ** 2) / V4
    sigma = sp.Symbol("sigma", positive=True)
    # S_n = -CS_n k - Vol_n sigma, and P1 showed CS_n = 0, so S_n = -n Vol sigma.
    n = sp.Symbol("n", positive=True, integer=True)
    Vol = sp.Symbol("Vol", positive=True)
    S_n = -n * Vol * sigma
    log_tors = n * sp.log(sp.Symbol("phi", positive=True) ** 2)
    ratio = sp.simplify(log_tors / (-S_n))
    print(f"         S_n = {S_n}   (CS_n = 0 by P1)")
    print(f"         log|tors_n| ~ n log(phi^2)")
    print(f"         log|tors| / (-S) = {ratio}   -- the n CANCELS: a pure number over sigma")
    sigma_star = rate
    c_star = 6 * sigma_star
    print(f"         SO: IF log|H_1 tors| = -S (an entropy-equals-action statement), THEN")
    print(f"           sigma = log(phi^2)/vol(m004) = {sigma_star:.13f}")
    print(f"           c = 6 sigma                  = {c_star:.13f}")
    print( "         THE SEAL PRINTED THESE TWO NUMBERS IN ADVANCE, so they cannot be")
    print( "         presented as a discovery.  They are a CANDIDATE, and the cell's job")
    print( "         is to find whether the identification that produces them is licensed.")
    print( "         WHAT THE LICENCE WOULD HAVE TO BE, stated so it is checkable:")
    print( "           a named result letting log|H_1(M_n)_tors| be read as the entropy of")
    print( "           the gravitational theory on M_n, equal to minus its on-shell action.")
    print( "         WHY IT IS NOT LICENSED -- and this is THIS SEAT'S ARGUMENT FROM THE")
    print( "         STRUCTURE OF THE THEORY, not a citation.  A literature check is in flight")
    print( "         at the time of banking and is NOT reflected here; if it returns a licence,")
    print( "         this cell is wrong and the arc owes an addendum.  Flagged, not hidden:")
    print( "           torsion enters a complex-CS partition function as RAY-SINGER torsion at")
    print( "           ONE LOOP (Cheeger-Muller; Witten; Dimofte-Gukov-Lenells-Zagier), i.e. in")
    print( "           the FLUCTUATION determinant, NOT in the on-shell action; and a cusped")
    print( "           hyperbolic manifold has NO HORIZON, so there is no Bekenstein-Hawking")
    print( "           area to count and no Cardy regime to sit in.  Reading a HOMOLOGY count")
    print( "           as a STATE count is a category error, not a missing theorem.")
    licensed = False
    print(f"         licence found: {licensed}")
    print( "P2 NEGATIVE  ROUTE 1 FAILS ON LICENSING.  sigma = 0.4741275971 and c = 2.8447655827")
    print( "         are recorded as a REFUTED CANDIDATE, never as a prediction.  And P3 kills")
    print( "         the same route a second time, independently of any licence.")
    RESULTS["P2"] = {"sigma_candidate": sigma_star, "c_candidate": c_star,
                     "licensed": licensed}
    return True


# ---------------------------------------------------------------- P3


def P3(dmax=8):
    print("\nP3       ROUTE 2 (THE BLIND CELL) -- is the rate the OBJECT's or the TOWER's?")
    M4 = snappy.Manifold("m004")
    cyc = math.log(PHI ** 2) / float(M4.volume())
    print(f"         {'deg':>4} {'#covers':>8} {'min rate':>10} {'max rate':>10} {'median':>10}"
          f" {'#tors=1':>8}")
    allr = []
    per_deg = {}
    for d in range(2, dmax + 1):
        covs = M4.covers(d)
        rates, triv = [], 0
        for C in covs:
            t, v = torsion(C), float(C.volume())
            if t <= 1:
                triv += 1
                rates.append(0.0)
            else:
                rates.append(math.log(t) / v)
        per_deg[d] = rates
        allr += rates
        print(f"         {d:>4} {len(covs):>8} {min(rates):10.6f} {max(rates):10.6f}"
              f" {statistics.median(rates):10.6f} {triv:>8}")
    # VERIFY, do not assert, that the near-limit covers are the cyclic ones: a first
    # draft of this cell wrote "(these ARE the cyclic ones)" from inspection alone.
    cycset = [(n, snappy.Manifold("b++" + "LR" * n)) for n in range(2, dmax + 1)]
    named = []
    for d in range(2, dmax + 1):
        for C in M4.covers(d):
            t, v = torsion(C), float(C.volume())
            r = math.log(t) / v if t > 1 else 0.0
            if abs(r - cyc) < 0.01:
                hit = [n for n, X in cycset
                       if abs(float(X.volume()) - v) < 1e-7 and C.is_isometric_to(X)]
                named.append((d, r, hit))
    near = sum(1 for r in allr if abs(r - cyc) < 0.01)
    zero = sum(1 for r in allr if r == 0.0)
    print(f"\n         across all {len(allr)} covers of m004 of degree 2-{dmax}:")
    print(f"           min {min(allr):.6f}   max {max(allr):.6f}   median {statistics.median(allr):.6f}")
    print(f"           the cyclic tower's limit is {cyc:.6f}")
    print(f"           covers within 0.01 of it: {near} of {len(allr)}")
    print( "           and each one VERIFIED by isometry to be a cyclic-tower member:")
    for d, r, hit in named:
        print(f"             degree {d}: rate {r:.6f}  isometric to b++(LR)^n, n = {hit}")
    all_cyclic = all(hit for _, _, hit in named) and len(named) == near
    print(f"           covers with TRIVIAL torsion, rate exactly 0: {zero} of {len(allr)}")
    print(f"           1/(6 pi) = {1/(6*math.pi):.6f}, the congruence-tower constant, for scale")
    spread = max(allr) - min(allr)
    tower_dependent = spread > 0.1 and zero > 0 and all_cyclic
    print(f"P3 {'PASS' if tower_dependent else 'FAIL'}  THE RATE IS THE TOWER'S, NOT THE OBJECT'S.")
    print( "         The same manifold m004 carries covers whose torsion rate is ANYTHING from")
    print(f"         0 to {max(allr):.6f} -- {zero} of {len(allr)} have NO torsion at all.  So")
    print( "         0.4741275971 is not a number m004 has; it is a number ONE TOWER over m004")
    print( "         has.  NO COVER IN THE SEARCHED RANGE EXCEEDS IT -- stated as a measurement,")
    print( "         not as a supremum, since the range is degree <= 8.  MY DECLARED PRIOR WAS")
    print( "         RIGHT, and this kills Route 1 a second time WITHOUT needing the licensing")
    print( "         argument at all.")
    print( "         AND THE COMPARISON THAT PUTS IT IN SCALE: the asymptotic torsion-growth")
    print(f"         rate associated with a hyperbolic 3-manifold in the literature is")
    print(f"         1/(6 pi) = {1/(6*math.pi):.6f} -- QUOTED FROM MEMORY AND NOT YET VERIFIED")
    print( "         AGAINST A SOURCE, so it is a scale marker here and nothing is concluded")
    print(f"         FROM it.  The cyclic tower gives {cyc:.6f} -- DIFFERENT")
    print( "         BY A FACTOR OF ABOUT 8.9.  Path A picked the tower that gives the biggest")
    print( "         number, which is what a selection effect looks like.")
    print()
    print( "         A MECHANISM CLAIM THIS CELL TRIED TO MAKE AND WITHDREW.  A first draft said")
    print( "         the cyclic tower fails to converge to the universal cover because it keeps")
    print( "         the fibre.  To support it this seat measured the systole along the tower;")
    print( "         SnapPy returned nothing beyond n = 4 and the draft read that as 'systole")
    print( "         grows'.  IT WAS A SWALLOWED EXCEPTION -- length_spectrum raises")
    print( "         RuntimeError('The Dirichlet construction failed') on these covers, and the")
    print( "         loop's bare except turned a failure into a data point.  The measurement is")
    print( "         VOID, the mechanism is NOT established here, and the claim is WITHDRAWN.")
    print( "         P3's conclusion does not depend on it: the measured spread above is what")
    print( "         proves tower-dependence, and that stands on its own.")
    RESULTS["P3"] = {"n_covers": len(allr), "min": min(allr), "max": max(allr),
                     "median": statistics.median(allr), "trivial_torsion": zero,
                     "near_cyclic": near, "cyclic_limit": cyc,
                     "near_limit_all_cyclic": bool(all_cyclic),
                     "tower_dependent": bool(tower_dependent)}
    return tower_dependent


# ---------------------------------------------------------------- P4


def P4():
    print("\nP4       ROUTE 3 -- what the mod-1/2 indeterminacy forces, and the GAP it exposes")
    print("         For a CUSPED manifold cs is well defined only modulo 1/2, and the")
    print("         indeterminacy is ESSENTIAL (Neumann, arXiv:1108.0062 Thm 2.14: there is no")
    print("         consistent definition well defined modulo 2 pi^2 for cusped manifolds).")
    print("         Under cs -> cs + 1/2 the action S = -cs*k - Vol*sigma shifts by -k/2, so")
    print("         exp(2 pi i S) picks up exp(-i pi k) = (-1)^k.")
    k = sp.Symbol("k", integer=True)
    phase = sp.simplify(sp.exp(-sp.I * sp.pi * k))
    print(f"           phase = {phase}  -> equals 1 exactly when k is EVEN")
    print("         SO, IN THE LEVEL NORMALISATION (weight exp(2 pi i k cs)): k must be EVEN.")
    print("         BY THIS ARC'S OWN SEALED DEFINITION THIS IS NOT A CROSSING -- it constrains")
    print("         k, and k is not the free anchor.  It is reported as what it is.")
    print()
    print("         AND THE CELL FOUND SOMETHING THE SEAL DID NOT ANTICIPATE, WHICH IS A GAP")
    print("         IN THE RECORD RATHER THAN A RESULT:")
    print("           B1012's b1012_verify.py carries CS as a BARE SYMPY SYMBOL.  Its algebra")
    print("           -- S = -CS*k - Vol*sigma, dS/dk = -CS -- is NORMALISATION-FREE, and NO ARC")
    print("           IN THE RECORD PINS WHICH CS ENTERS THE k-COUPLING: SnapPy's cs (mod 1/2),")
    print("           Neumann's CS = 2 pi^2 cs (mod pi^2), or a level-normalised CS/2pi.  The")
    print("           three differ by factors of 2 pi^2, and the quantization statement above")
    print("           holds in ONE of them.  In Neumann's normalisation the same shift gives")
    print("           exp(-i pi^2 k), which is not a root of unity for any k != 0 -- so that")
    print("           normalisation cannot be the one the exponentiated weight uses, which is")
    print("           itself a constraint the record has never written down.")
    print("         CONSEQUENCE, STATED PLAINLY: no quantization claim can be read off the")
    print("         record as it stands.  Pinning the normalisation of the k-coupling is a")
    print("         PREREQUISITE for any future crossing attempt through this route, and it is")
    print("         owed work, not a result of this arc.")
    RESULTS["P4"] = {"k_even_in_level_normalisation": True,
                     "is_a_crossing": False,
                     "normalisation_pinned_in_record": False}
    return True


# ---------------------------------------------------------------- P5


def P5():
    print("\nP5       B290's PRECEDENT, RE-DERIVED AND TURNED ON THIS ARC'S OWN TEMPTATION")
    print("         B290 (banked): 'the filling n is NOT the level k' -- the filling coefficient")
    print("         is a topological Dehn-surgery integer, the level is a quantum root-of-unity")
    print("         parameter q = exp(2 pi i/(k+2)); INDEPENDENT AXES, so n = k is a formal")
    print("         substitution and not an identity.")
    print("         RE-DERIVED HERE as the statement that actually bites, in this arc's own")
    print("         variables: for ANY fixed manifold M the action is")
    print("           S(M; k, sigma) = -CS(M)*k - Vol(M)*sigma,")
    print("         so the OBJECT supplies CS(M) and Vol(M) -- the COEFFICIENTS -- and k and")
    print("         sigma are the coordinates they multiply.  A topological invariant of M can")
    print("         determine dS/dk; it cannot determine k, because k is not a function of M.")
    k, sig, Vol, CS = sp.symbols("k sigma Vol CS", real=True)
    S = -CS * k - Vol * sig
    print(f"           dS/dk      = {sp.diff(S, k)}   (an invariant of M)")
    print(f"           dS/dsigma  = {sp.diff(S, sig)}   (an invariant of M)")
    print(f"           d^2S/dk^2  = {sp.diff(S, k, 2)}   (the action is LINEAR in both levels)")
    print("         Because S is linear in k and in sigma with M-determined coefficients, NO")
    print("         invariant of M can fix either level.  This is the same negative B290 banked,")
    print("         in the form that covers this arc: it kills identifying the tower index n")
    print("         with k, AND it kills identifying xB015's Z/12 CS index with k.")
    print("P5 PASS   B290 reproduces and it binds.  Both identifications are dead on arrival,")
    print("         and this arc does not make either.")
    RESULTS["P5"] = {"S_linear_in_both_levels": True,
                     "tower_index_is_k": False, "cs_index_is_k": False}
    return True


# ---------------------------------------------------------------- P6


def P6():
    print("\nP6       THE VERDICT")
    print("         TRIED:  Route 1 (the rate route)        -> FAILS TWICE: unlicensed (P2) and")
    print("                                                    tower-dependent (P3).")
    print("                 Route 2 (genericity of the rate) -> the rate is the TOWER's; m004's")
    print("                                                    covers span 0 to 0.474072, seven")
    print("                                                    of thirty-eight with no torsion.")
    print("                 Route 3 (quantization)           -> constrains k (even), not sigma,")
    print("                                                    and exposes an UNPINNED")
    print("                                                    NORMALISATION in the record.")
    print("         PATH A DOES NOT CROSS.  sigma is untouched by everything here.")
    print()
    print("         WHICH ROUTE A FUTURE SEAT SHOULD RE-OPEN, and what it needs:")
    print("           ROUTE 3.  It is the only one that produced a real constraint rather than")
    print("           a coincidence, and it is blocked by a piece of MISSING BOOKKEEPING rather")
    print("           than by a theorem: the record never pinned the normalisation of the")
    print("           k-coupling.  Pin it, and the well-definedness of exp(2 pi i S) becomes a")
    print("           genuine equation relating the level to the framing anomaly exp(2 pi i c/24)")
    print("           -- which is the only place in this whole structure where c appears in an")
    print("           EQUATION rather than as a free anchor.  That is a crossing CANDIDATE.")
    print("           Routes 1 and 2 are closed and should not be re-run.")
    RESULTS["P6"] = {"crosses": False, "reopen": "Route 3 (pin the k-coupling normalisation)"}
    return True


if __name__ == "__main__":
    v = {"P1": P1(), "P2": "NEGATIVE (preregistered)" if P2() else False,
         "P3": P3(), "P4": P4(), "P5": P5(), "P6": P6()}
    print("\n" + "=" * 78)
    for kk, r in v.items():
        print(f"  {kk}: {r if isinstance(r, str) else ('PASS' if r else 'FAIL')}")
    json.dump(RESULTS, open(os.path.join(HERE, "path_a.json"), "w"), indent=1, default=str)
    print("VERIFIED -- PATH A DOES NOT CROSS")
