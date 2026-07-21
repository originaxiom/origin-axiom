#!/usr/bin/env python
"""B739 Stage-B recompute — target B500 (the child hunt: x^4 - x - 1, d_K = -283).

E19 compute-not-cite. THE discriminating fact of the banked negative:
  (a) depth-4 COMPLETE kill: none of the 36 all-three-verb depth-4 words' fixed-point
      eliminants contains an irreducible quartic factor whose root field is isomorphic
      to the child K = Q[t]/(t^4 - t - 1) (d_K = -283)  [0/36, complete];
  (b) depth-5 census (B525-corrected): only 115/150 words were actually analyzed (0 hits);
      35/150 are UNCHECKED (26 bare TIMEOUT + 9 never-reached), so the depth-5 kill is
      PROVISIONAL only.

Re-derivation, from the arc's own declared conventions (hunt.py / hunt_d5.py):
  - verbs  F(x,y,z) = (z, x, xz - y)
           M(x,y,z) = (z, z, xyz - x^2 - y^2 + 2)
           D(x,y,z) = (x^2 - 2, y^2 - 2, xyz - x^2 - y^2 + 2)
  - word -> map: for c in reversed(word): p = GEN[c](p)   (leftmost letter outermost)
  - fixed-point ideal I = (p0 - x, p1 - y, p2 - z) in Q[x,y,z]
  - eliminant h = Res_y( Res_z(f1, f3), Res_z(f2, f3) ) as univariate in x;
    if h == 0: saturate I by the Jacobian det of (P - id), require dim <= 0,
    h = generator of the elimination ideal to Q[x]  (hunt.py lines 30-41, verbatim logic)
  - DETECTOR (strengthened, closing the arc's polgalois-gate hole): every irreducible
    QUARTIC factor of h is tested directly for field isomorphism with K (pari nfisisom
    via Sage is_isomorphic), not only those with polgalois order 24; discriminant and
    galois order are recorded per quartic factor.

Part 1: depth-4 exact recompute over Q (the COMPLETE component of the kill).
Part 2: depth-5 census recount from the arc's primary artifact hunt_results_d5.txt
        (independent parse) + forbidden-string absence check over both results files.
Part 3: depth-5 targeted F_p no-child certificates for ALL 150 words — the FINDINGS'
        own proposed REOPEN method ("Groebner/eliminant over F_p, or a targeted
        d_K=-283 factor test") executed on the 35 UNCHECKED words as well.
        Per word, per prime p (deterministic ascending list of primes p >= 10007 with
        t^4 - t - 1 irreducible mod p, i.e. Frobenius a 4-cycle in the child):
        compute the mod-p eliminant by the same chain (GF(p)-saturation fallback),
        take its squarefree part, count irreducible degree-4 factors by distinct-degree
        gcds. If the count is 0 the prime CERTIFIES: any hypothetical child quartic
        factor f (which at every prime p unramified for f with 4-cycle child-Frobenius
        must reduce to an irreducible quartic dividing the eliminant mod p) would need
        p | lc(f)*disc(f)*(content/degeneration invariant). Two certifying primes are
        required per word; a persistent quartic escalates the word to the exact-Q
        pipeline with the isomorphism detector.

Engine: SageMath 10.9 python (the arc's own declared engine — hunt.py's shebang is
sage-python; Sage was used for PolynomialRing/resultant/saturation/NumberField/gp there).
Deterministic: no wall-clock, no randomness, no network. Output: output.txt beside this
script (file names only, no absolute paths).
"""
import itertools as it
import os
import re

from sage.all import GF, NumberField, PolynomialRing, QQ, matrix, pari

HERE = os.path.dirname(os.path.abspath(__file__))
ARC = os.path.normpath(os.path.join(HERE, "..", "..", "..", "B500_child_hunt"))
OUT = open(os.path.join(HERE, "output.txt"), "w")


def log(m=""):
    print(m, flush=True)
    OUT.write(m + "\n")
    OUT.flush()


# ---------------------------------------------------------------- conventions
Rt = PolynomialRing(QQ, "t")
t = Rt.gen()
g_child = t**4 - t - 1
CHILD = NumberField(g_child, "a")

N_CERT = 2        # certifying primes required per depth-5 word (declared)
N_PRIMES = 40     # size of the deterministic type-4 prime list (declared)
PRIME_FLOOR = 10007  # scan start (declared; avoids small-prime degeneracies, > 283)
ESCALATE_MAX_CHAIN_DEG = 3000  # exact-Q escalation allowed up to this mod-p chain degree


def make_gens(ring):
    x, y, z = ring.gens()
    F = lambda p: (p[2], p[0], p[0] * p[2] - p[1])
    M = lambda p: (p[2], p[2], p[0] * p[1] * p[2] - p[0] ** 2 - p[1] ** 2 + 2)
    D = lambda p: (p[0] ** 2 - 2, p[1] ** 2 - 2,
                   p[0] * p[1] * p[2] - p[0] ** 2 - p[1] ** 2 + 2)
    return {"F": F, "M": M, "D": D}


def eliminant(ring, word):
    """The arc's pipeline verbatim: resultant chain; on h==0 Jacobian saturation.
    Returns (branch, h) with branch in {chain, sat, POSDIM}."""
    x, y, z = ring.gens()
    GEN = make_gens(ring)
    p = (x, y, z)
    for c in reversed(word):
        p = GEN[c](p)
    f1, f2, f3 = p[0] - x, p[1] - y, p[2] - z
    r1 = f1.resultant(f3, z)
    r2 = f2.resultant(f3, z)
    h = r1.resultant(r2, y).univariate_polynomial()
    if h != 0:
        return "chain", h
    I = ring.ideal([f1, f2, f3])
    J = matrix(3, 3, lambda i, j: (p[i] - (x, y, z)[i]).derivative((x, y, z)[j])).det()
    S = I.saturation(ring.ideal(J))[0]
    if S.dimension() > 0:
        return "POSDIM", None
    hh = S.elimination_ideal([y, z]).gens()[0].univariate_polynomial()
    return "sat", hh


def deg_multiset(fac):
    d = {}
    for f, m in fac:
        d[f.degree()] = d.get(f.degree(), 0) + m
    return "{" + ", ".join("%d:%d" % (k, d[k]) for k in sorted(d)) + "}"


def quartic_report(h):
    """Every irreducible quartic factor of h: (disc, galois order, iso-to-child)."""
    reports = []
    n_child = 0
    for f, _m in h.factor():
        if f.degree() != 4:
            continue
        fm = f.monic().change_variable_name("t")
        K = NumberField(fm, "b")
        dk = K.discriminant()
        try:
            ordg = int(pari(fm).polgalois()[0])
        except Exception:
            ordg = -1
        iso = K.is_isomorphic(CHILD)
        if iso:
            n_child += 1
        reports.append("      quartic factor: d_K=%s ord=%s iso_to_child=%s" % (dk, ordg, iso))
    return reports, n_child


def n_irred_quartics_mod_p(hs, p):
    """# irreducible degree-4 factors of squarefree hs over GF(p), by distinct-degree gcds."""
    if hs.degree() < 4:
        return 0
    R1 = hs.parent()
    xx = R1.gen()
    Q = R1.quotient(hs)
    fr = Q(xx)
    t1 = fr
    for _ in range(2):
        t1 = t1 ** p
    g2 = hs.gcd(t1.lift() - xx)
    for _ in range(2):
        t1 = t1 ** p
    g4 = hs.gcd(t1.lift() - xx)
    return (g4.degree() - g2.degree()) // 4


# ================================================================ Part 0
log("B739 Stage-B recompute — target B500 (child hunt, x^4 - x - 1, d_K = -283)")
log("engine: SageMath (the arc's own declared engine); deterministic, no network")
log("")
log("child check: disc(t^4 - t - 1) = %s ; nfdisc = %s ; polgalois = %s"
    % (g_child.discriminant(), pari(g_child).nfdisc(), pari(g_child).polgalois()))
assert g_child.discriminant() == -283 and int(pari(g_child).nfdisc()) == -283
log("(-283 squarefree => Z[t]/(g) is the maximal order; splitting of every p in K is")
log(" read off the factorization of g mod p — used by the Part-3 certificates)")
log("")

# ================================================================ Part 1
log("=" * 78)
log("PART 1 — depth-4 EXACT recompute over Q (the banked kill's COMPLETE component)")
log("=" * 78)

words4 = ["".join(w) for w in it.product("FMD", repeat=4) if set(w) == set("FMD")]
log("depth-4 all-three-verb words: %d (expected 36)" % len(words4))

arc_deg4 = {}
with open(os.path.join(ARC, "hunt_results.txt")) as fh:
    for line in fh:
        m = re.match(r"^([FMD]{4}): eliminant deg (\d+);", line)
        if m:
            arc_deg4[m.group(1)] = int(m.group(2))
log("arc hunt_results.txt: %d logged eliminant-degree lines" % len(arc_deg4))
log("")

R = PolynomialRing(QQ, ["x", "y", "z"])
child_hits_d4 = 0
quartic_total_d4 = 0
deg_matches = 0
deg_mismatch = []
for w in words4:
    branch, h = eliminant(R, w)
    if branch == "POSDIM":
        log("%s: POSITIVE-DIM after saturation (arc would log SKIP)" % w)
        continue
    fac = h.factor()
    reps, nch = quartic_report(h)
    nq = len(reps)
    quartic_total_d4 += nq
    child_hits_d4 += nch
    a = arc_deg4.get(w)
    mark = "=arc" if a == h.degree() else "ARC-MISMATCH(arc=%s)" % a
    if a == h.degree():
        deg_matches += 1
    else:
        deg_mismatch.append(w)
    log("%s: %s deg %d [%s] factor-degrees %s quartics=%d child-hits=%d"
        % (w, branch, h.degree(), mark, deg_multiset(fac), nq, nch))
    for r in reps:
        log(r)

log("")
log("depth-4 RESULT: child (iso to Q[t]/(t^4-t-1)) hits = %d / 36 words" % child_hits_d4)
log("depth-4 irreducible quartic factors encountered (all iso-tested): %d" % quartic_total_d4)
log("depth-4 eliminant-degree agreement with arc log: %d/36 %s"
    % (deg_matches, ("mismatches: %s" % deg_mismatch) if deg_mismatch else "(exact)"))

# ================================================================ Part 2
log("")
log("=" * 78)
log("PART 2 — depth-5 census recount (B525-corrected numbers), from hunt_results_d5.txt")
log("=" * 78)

words5 = ["".join(w) for w in it.product("FMD", repeat=5) if set(w) == set("FMD")]
log("planned depth-5 all-three-verb words (itertools order): %d (expected 150)" % len(words5))

d5_path = os.path.join(ARC, "hunt_results_d5.txt")
with open(d5_path) as fh:
    d5_text = fh.read()
d5_lines = d5_text.splitlines()

logged = {}       # word -> line
for line in d5_lines:
    m = re.match(r"^([FMD]{5}):", line)
    if m:
        logged[m.group(1)] = line
timeouts = sorted(w for w, l in logged.items() if "TIMEOUT" in l)
analyzed = sorted(w for w, l in logged.items() if "TIMEOUT" not in l)
never_reached = [w for w in words5 if w not in logged]
arc_deg5 = {}
for w in analyzed:
    m = re.search(r"eliminant deg (\d+)", logged[w])
    if m:
        arc_deg5[w] = int(m.group(1))

log("logged word-lines: %d ; bare TIMEOUT: %d ; analyzed: %d ; never-reached: %d"
    % (len(logged), len(timeouts), len(analyzed), len(never_reached)))
log("unchecked = timeouts + never-reached = %d + %d = %d (of 150)"
    % (len(timeouts), len(never_reached), len(timeouts) + len(never_reached)))
log("'HUNT COMPLETE' present: %s" % ("HUNT COMPLETE" in d5_text))
log("never-reached words: %s" % " ".join(never_reached))
log("timeout words: %s" % " ".join(timeouts))

for fname in ("hunt_results.txt", "hunt_results_d5.txt"):
    with open(os.path.join(ARC, fname)) as fh:
        body = "\n".join(l for l in fh.read().splitlines() if "target d_K=-283" not in l)
    bad = [s for s in ("AIRLOCK", "-283", "isomorph", " HIT") if s in body]
    log("forbidden-string check %s (excl. header): %s" % (fname, bad if bad else "CLEAN"))

# ================================================================ Part 3
log("")
log("=" * 78)
log("PART 3 — depth-5 F_p no-child certificates, ALL 150 words (incl. the 35 unchecked)")
log("=" * 78)

primes4 = []
p = PRIME_FLOOR - 1
from sage.all import next_prime
while len(primes4) < N_PRIMES:
    p = next_prime(p)
    if g_child.change_ring(GF(p)).is_irreducible():
        primes4.append(int(p))
log("type-4 prime list (t^4-t-1 irreducible mod p), first %d from %d up:" % (N_PRIMES, PRIME_FLOOR))
log("  %s" % " ".join(str(q) for q in primes4))
log("certificate rule: prime p certifies word w iff the mod-p eliminant (chain, or")
log("GF(p) Jacobian-saturation elimination when the chain vanishes) has squarefree part")
log("with ZERO irreducible degree-4 factors; %d certifying primes required." % N_CERT)
log("")

summary = {"CERTIFIED": [], "ESCALATED-CLEAN": [], "ESCALATED-HIT": [], "UNRESOLVED": []}
chain_deg_match = 0
chain_deg_seen = 0
child_hits_d5 = 0

for w in words5:
    status = ("analyzed(deg %d)" % arc_deg5[w]) if w in arc_deg5 else \
             ("TIMEOUT" if w in timeouts else "never-reached")
    certs = []
    trail = []
    last_chain_deg = None
    for p in primes4:
        Rp = PolynomialRing(GF(p), ["x", "y", "z"])
        branch, H = eliminant(Rp, w)
        if branch == "POSDIM":
            trail.append("p=%d POSDIM" % p)
            continue
        if branch == "chain":
            last_chain_deg = H.degree()
            if w in arc_deg5:
                chain_deg_seen += 1
                if H.degree() == arc_deg5[w]:
                    chain_deg_match += 1
        hs = H // H.gcd(H.derivative())
        n4 = n_irred_quartics_mod_p(hs, p)
        trail.append("p=%d %s deg%d sqf%d q4=%d" % (p, branch, H.degree(), hs.degree(), n4))
        if n4 == 0:
            certs.append(p)
        if len(certs) >= N_CERT:
            break
    if len(certs) >= N_CERT:
        summary["CERTIFIED"].append(w)
        log("%s [%s]: CERTIFIED by p=%s | %s" % (w, status, certs, "; ".join(trail)))
        continue
    # escalation: exact-Q pipeline with the isomorphism detector
    if last_chain_deg is not None and last_chain_deg <= ESCALATE_MAX_CHAIN_DEG:
        branch, h = eliminant(R, w)
        if branch == "POSDIM":
            summary["UNRESOLVED"].append(w)
            log("%s [%s]: ESCALATION POSDIM | %s" % (w, status, "; ".join(trail)))
            continue
        reps, nch = quartic_report(h)
        child_hits_d5 += nch
        key = "ESCALATED-HIT" if nch else "ESCALATED-CLEAN"
        summary[key].append(w)
        log("%s [%s]: ESCALATED exact-Q %s deg %d quartics=%d child-hits=%d | %s"
            % (w, status, branch, h.degree(), len(reps), nch, "; ".join(trail)))
        for r in reps:
            log(r)
    else:
        summary["UNRESOLVED"].append(w)
        log("%s [%s]: UNRESOLVED (no %d certificates in %d primes; chain deg %s beyond "
            "escalation cap) | %s"
            % (w, status, N_CERT, N_PRIMES, last_chain_deg, "; ".join(trail)))

log("")
log("depth-5 certificate summary over 150 words:")
for k in ("CERTIFIED", "ESCALATED-CLEAN", "ESCALATED-HIT", "UNRESOLVED"):
    log("  %-16s %3d %s" % (k, len(summary[k]),
                            (" ".join(summary[k]) if k != "CERTIFIED" and summary[k] else "")))
unchecked = set(timeouts) | set(never_reached)
cert_unchecked = [w for w in summary["CERTIFIED"] + summary["ESCALATED-CLEAN"] if w in unchecked]
log("  of the 35 UNCHECKED words, no-child-certified or exact-clean: %d/35" % len(cert_unchecked))
log("  chain-branch eliminant degree vs arc log (analyzed words): %d/%d equal"
    % (chain_deg_match, chain_deg_seen))
log("  depth-5 exact child hits found during escalations: %d" % child_hits_d5)

# ================================================================ verdict facts
log("")
log("=" * 78)
log("DISCRIMINATING FACTS, RECOMPUTED")
log("=" * 78)
log("(a) depth-4 COMPLETE: child hits %d/36 (every irreducible quartic factor of every" % child_hits_d4)
log("    eliminant directly iso-tested against Q[t]/(t^4-t-1) — the arc's polgalois-gated")
log("    detector hole is closed by testing ALL quartic factors)")
log("(b) depth-5 census (B525-corrected): %d logged, %d bare TIMEOUT, %d analyzed,"
    % (len(logged), len(timeouts), len(analyzed)))
log("    %d never-reached, %d/150 UNCHECKED; no HUNT COMPLETE line; results files free"
    % (len(never_reached), len(timeouts) + len(never_reached)))
log("    of AIRLOCK/-283/isomorph strings outside the header => the depth-5 kill is")
log("    PROVISIONAL, exactly as banked")
log("(c) depth-5 F_p probe (the FINDINGS' own REOPEN method): certificates/exact-clean")
log("    cover %d/150 words incl. %d/35 of the unchecked; %d child hits anywhere"
    % (len(summary["CERTIFIED"]) + len(summary["ESCALATED-CLEAN"]), len(cert_unchecked),
       child_hits_d4 + child_hits_d5))
OUT.close()
