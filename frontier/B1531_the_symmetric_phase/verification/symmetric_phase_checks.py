#!/usr/bin/env python3
"""B1531 -- THE SYMMETRIC PHASE: chat 1's reframing (received through the owner, 2026-10-03; philosophy/P023) checked against
the record.  Not sealed: every check reads a banked record, re-derives a fact a record states, or verifies a standard identity.
No open outcome is computed.

C1  The absence claim.  "'symmetric phase' and 'broken phase' appear nowhere -- 0 in your paper, 0 in the record."  Counted on
    main's head, this branch's, the audit lane's and the sep16 branch's, by git grep (case-insensitive, whole words: a plain
    substring search also counts "asymmetric phase"), with the files named; the substring count is kept for comparison.
C2  The three kinds of negatives against the record's own classification.  The kill graph's families (the first token of each
    kill_form), over all records and over the 26 chirality-chain records of docs/THE_NEGATIVES_READ_TOGETHER_2026-09-30.md.
    C2b reads each of the 26 against chat 1's three kinds (symmetry pairing, absence of curvature, absence of uniqueness), record
    by record, with the reason written beside it.  That reading is the seat's judgement, stated as data so it can be checked;
    the families it starts from are the record's own (assigned when each arc was banked).
C3  The critical point.  The orbit sum Z(beta) = sum_n N_n e^{-beta n}, N_n = |det(f^n - 1)| the periodic points of the
    monodromy f = +-A on the torus (A in SL(2, Z), t = tr A > 2, dilatation lambda + 1/lambda = t), converges exactly for
    beta > log(lambda): the Artin-Mazur zeta exp(sum_n N_n z^n / n) is (1 -+ z)^2 / (1 - t z + z^2) for f = +-A, checked
    exactly as power series over Q to order 40 (from N_n of the integer matrices, by n f_n = sum_k N_k f_{n-k}), and N_n
    against lambda^n + lambda^-n -+ 2 (-+1)^n.  The zeta is the partition function of an ideal gas of periodic orbits: its Euler
    product prod_m (1 - z^m)^(-c_m) has c_m = (1/m) sum_{l | m} mu(m/l) N_l, the number of orbits of least period m (Baake-Lau-
    Paskunas, eqs. (2)-(3)), checked to be non-negative integers and to reproduce the series to order 40.  The mirror image
    f^-1 has the same counts.  For the golden LR, beta_c = log(phi^2) = 2 log phi (= xB032's T1 number, the
    tower's torsion growth); for the silver LLRR, where B1530's members live, 2 log(1 + sqrt 2).
C4  B1530's instance, exactly (route E, exact over Q(zeta_24), on m135's member u = (0, 1/2)): the split vacuum V (+) 1 and
    its exterior square read (0, 0); the non-split W1 at the interior class reads (-1, -1); W2, the dual order, reads (+1, +1).
    The dualising Z/2 fixes the split vacuum and exchanges the two non-split ones.
C5  The record's dynamics, quoted at source and checked to be there: main's B1455 verdict on the selection-rule handoff (the
    deciding test negative on m004's harmonic family; "the geometric mirror does not change the count; dualising does"; a
    non-split extension "not a minimum of this action"), and the audit lane's R76 (FLAT_VACUUM.md: a finite-energy smooth
    stationary flat point "must be harmonic"; along the extension "the potential is a t^2+c t^4, a>=0,c>0", its infimum at
    "the split limit"); and the same lane's F01 splitting obstruction, R41's flag balance, R81's boundary admission, F14's and
    PB-CHIRAL's "asymmetric interacting phase" duty; B849's SSB frame (2026-08-02); OPEN_LEADS L17 and its banked correction;
    xB032's T1 and T2 rows (sep16 branch).
C6  The mirror on the monodromy.  The quarter turn K = [[0, 1], [-1, 0]] (det 1) conjugates each of +-LR and +-LLRR to its
    inverse, so (x, t) -> (Kx, -t) reverses the bundle's orientation and acts on the monodromy as time reversal; SnapPy reads
    m003, m004, m135 and m136 as amphicheiral.  With the Sinai-Ruelle-Bowen uniqueness theorem this gives the lemma of
    FINDINGS section 4: every mirror-symmetric Hoelder potential has a mirror-symmetric equilibrium state.
Writes symmetric_phase_checks.json and symmetric_phase_checks_run.txt."""
import json
import re
import subprocess
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1530 = ROOT / "frontier" / "B1530_the_interior_extensions" / "verification"
LOG = []
CHAIN = ["B1351", "B1361", "B1363", "B1365", "B1367", "B1368", "B1369", "B1372", "B1373", "B1385", "B1388", "B1389", "B1390",
         "B1391", "B1392", "B1393", "B1394", "B1395", "B1396", "B1397", "B1398", "B1399", "B1500", "B1501", "B1502", "B1503"]


def say(s):
    print(s, flush=True)
    LOG.append(s)


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True).stdout


REFS = {"origin/main": "399b0bc2", "this branch (before this arc)": "56f46d4f",
        "origin/audit/physical-bridge-2026-09-05": "ddd345a8", "origin/sep16-branch": "3205984b"}


def c1():
    # whole words (-w): a plain substring search counts "asymmetric phase" as "symmetric phase" (caught before banking)
    out = {}
    # pinned to the heads read before this arc was committed (its own files mention the phrases): main 399b0bc2, this branch
    # 56f46d4f, the audit lane ddd345a8, sep16 3205984b
    for ref in REFS:
        files = {}
        for phrase in ("symmetric phase", "broken phase", "asymmetric phase", "symmetric phase (substring, for comparison)"):
            flags = ["-i", "-c"] + ([] if "substring" in phrase else ["-w"])
            hits = git("grep", *flags, phrase.split(" (")[0], REFS[ref], "--").splitlines()
            files[phrase] = {h.split(":", 2)[1]: int(h.rsplit(":", 1)[1]) for h in hits}
        out[ref] = {k: {"files": len(v), "lines": sum(v.values()), "where": sorted(v)} for k, v in files.items()}
    papers = [f for r in out for p in ("symmetric phase", "broken phase") for f in out[r][p]["where"] if f.startswith("papers/")]
    ok = all(out[r]["symmetric phase"]["files"] > 0 for r in out) and out["origin/main"]["broken phase"]["files"] > 0
    out["files under papers/ (either phrase, any head read)"] = papers
    say(f"C1 the absence claim (whole words): " + "; ".join(f"{r}: " + ", ".join(f"'{p}' in {out[r][p]['files']} files"
                                                                                  for p in out[r]) for r in out
                                                                  if r in REFS)
        + f"; under papers/: {papers} -> the phrases are on the record: {ok}")
    return {"holds (the phrases are present)": ok, "counts": out}


def c2():
    kg = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text(encoding="utf-8"))
    fam = Counter((r.get("kill_form") or "").split("(")[0].strip() for r in kg)
    chain = Counter((r.get("kill_form") or "").split("(")[0].strip() for r in kg if r["id"] in CHAIN)
    say(f"C2 the kill graph: {len(kg)} records; the families over all: {fam.most_common(12)}")
    say(f"   the 26 chirality-chain records: {dict(chain)}")
    return {"records": len(kg), "families (all)": dict(fam), "chirality chain (26)": dict(chain),
            "the chain's tally as the 2026-09-30 note states it": dict(chain) == {"frame-arithmetic": 9,
                                                                                 "symmetry-cannot-select": 8,
                                                                                 "closed-sum-zero": 4,
                                                                                 "end-datum-input": 3,
                                                                                 "absence-at-depth": 1,
                                                                                 "no-landing-site": 1}}

KINDS = {"S": "symmetry pairing or symmetry forcing (chat 1's first kind)",
         "F": "absence of curvature: a flat or well-posed index that vanishes (chat 1's second kind)",
         "U": "absence of uniqueness: the object does not make the choice (chat 1's third kind)",
         "none": "none of the three"}
READING = {
    "B1351": ("F", "a local system's Euler characteristic on a closed 3-manifold is zero (Poincare duality also pairs h1(psi) with h1(psi-bar))"),
    "B1361": ("S", "two U(1) charges force a hollow mass matrix"),
    "B1363": ("none", "Kac's order-3 classes of E6 contain no Standard-Model commutant: the frame's arithmetic"),
    "B1365": ("none", "the D-term sign: both E6-charged singlets carry gamma = -5/3: charge arithmetic"),
    "B1367": ("S", "the E6 cubic gives doublets and triplets the same matrices"),
    "B1368": ("none", "the 10 and the 5bar never share an SL(2)_beta spin: representation arithmetic"),
    "B1369": ("S", "a cusp-fixing isometry negates every free class: the regions swap, N = 0"),
    "B1372": ("none", "charge arithmetic at the cusp: Im t = +-L against +-3L"),
    "B1373": ("none", "absence at depth: where one eigenvalue reaches +-i the other is non-unitary"),
    "B1385": ("S", "the global parity: an isometry negating the Higgs class"),
    "B1388": ("U", "the relative index moves with the cut; the completion is not supplied"),
    "B1389": ("none", "a parity law of the 78 makes the anomaly odd: representation arithmetic"),
    "B1390": ("none", "Skolem-Noether: order-3 axes end at cusps: arithmetic of PGL(2, Q(sqrt -3))"),
    "B1391": ("S", "D3-covariant textures are degenerate at the symmetric point"),
    "B1392": ("F", "sealed ends make the problem Fredholm and its count zero"),
    "B1393": ("S", "charge conjugation pairs q with -q"),
    "B1394": ("S", "the Hopf trace: a symmetric source three is a regular representation"),
    "B1395": ("U", "every finite-energy datum at a free cusp is charge-blind: the charge-odd datum must be put in"),
    "B1396": ("S", "a Z/3-symmetric cap gives copies of the regular representation"),
    "B1397": ("none", "curvature supplied (flux caps), chirality produced, every E6 count even; for one bulk U(1) the caps sum to zero"),
    "B1398": ("none", "every 10-type weight of the 78 is a doublet; the anomaly matrix has rank 3"),
    "B1399": ("none", "lattice parity: every resolved count even"),
    "B1500": ("U", "the cone point needs a choice the geometry does not make"),
    "B1501": ("none", "no landing site: torus-linked loci are A-type and hexagonal"),
    "B1502": ("F", "no flux: deg L = 0 on the links"),
    "B1503": ("none", "positive scalar curvature kills the link's Dirac index (Lichnerowicz): curvature present, not absent"),
}


def c2b():
    kg = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text(encoding="utf-8"))
    fam = {r["id"]: (r.get("kill_form") or "").split("(")[0].strip() for r in kg if r["id"] in CHAIN}
    assert sorted(READING) == sorted(CHAIN)
    tally = Counter(k for k, _ in READING.values())
    cross = Counter((fam[b], READING[b][0]) for b in CHAIN)
    curved = sorted(b for b in CHAIN if "curvature" in READING[b][1] and READING[b][0] == "none")
    say(f"C2b chat 1's kinds over the 26 (the seat's reading): {dict(tally)}; record family x kind: "
        + ", ".join(f"{f}->{k}: {n}" for (f, k), n in sorted(cross.items())))
    say(f"    covered by the three kinds: {26 - tally['none']} of 26; of none of them: {tally['none']}, of which carrying "
        f"curvature: {curved}")
    return {"kinds": KINDS, "reading": {b: {"family": fam[b], "kind": READING[b][0], "why": READING[b][1]} for b in CHAIN},
            "tally": dict(tally), "family x kind": {f"{f} -> {k}": n for (f, k), n in sorted(cross.items())},
            "covered by the three kinds": 26 - tally["none"], "none of the three, carrying curvature": curved}


def c3():
    mp.mp.dps = 40
    res = {}
    K = 40
    for name, A in (("LR (golden; m004 = +LR, m003 = -LR)", ((2, 1), (1, 1))),
                    ("LLRR (silver; m136 = +LLRR, m135 = -LLRR)", ((1, 2), (2, 5)))):
        t = A[0][0] + A[1][1]
        assert A[0][0] * A[1][1] - A[0][1] * A[1][0] == 1 and t > 2
        lam = (t + mp.sqrt(t * t - 4)) / 2
        for sign in (1, -1):
            # N_n = |det(f^n - 1)|, f = sign * A, from the integer matrices
            N, P = [], ((1, 0), (0, 1))
            for n in range(1, K + 1):
                P = tuple(tuple(sum(P[i][k] * A[k][j] for k in range(2)) * sign for j in range(2)) for i in range(2))
                N.append(abs((P[0][0] - 1) * (P[1][1] - 1) - P[0][1] * P[1][0]))
            # the trace form: N_n = lambda^n + lambda^-n - 2 sign^n, i.e. |2 - tr f^n| with tr f^n = sign^n tr A^n
            trA = [2, t]
            for n in range(2, K + 1):
                trA.append(t * trA[-1] - trA[-2])
            trace_form = all(N[n - 1] == trA[n] - 2 * sign ** n for n in range(1, K + 1))
            # the zeta exp(sum N_n z^n / n) as an exact power series: n f_n = sum_{k=1}^n N_k f_{n-k}
            f = [Fraction(1)]
            for n in range(1, K + 1):
                f.append(sum(N[k - 1] * f[n - k] for k in range(1, n + 1)) / Fraction(n))
            # the closed form (1 - sign z)^2 / (1 - t z + z^2): q_n = t q_{n-1} - q_{n-2} + p_n, p = (1, -2 sign, 1)
            p = [1, -2 * sign, 1] + [0] * K
            q = []
            for n in range(K + 1):
                q.append(p[n] + (t * q[n - 1] if n >= 1 else 0) - (q[n - 2] if n >= 2 else 0))
            zeta_ok = all(f[n] == q[n] for n in range(K + 1)) and all(x.denominator == 1 for x in f)
            # the Euler product over orbits: c_m = (1/m) sum_{l | m} mu(m/l) N_l, an ideal gas of periodic orbits
            def mobius(n):
                r, k = 1, 2
                while k * k <= n:
                    if n % k == 0:
                        n //= k
                        if n % k == 0:
                            return 0
                        r = -r
                    k += 1
                return -r if n > 1 else r
            c = [None] + [Fraction(sum(mobius(m // l) * N[l - 1] for l in range(1, m + 1) if m % l == 0), m)
                          for m in range(1, K + 1)]
            cycles_ok = all(x.denominator == 1 and x >= 0 for x in c[1:])
            prod = [1] + [0] * K                               # prod_m (1 - z^m)^(-c_m) to order K
            for m in range(1, K + 1):
                cm = int(c[m])                                 # (1 - x)^(-c) = sum_j binom(c + j - 1, j) x^j, x = z^m
                coef = [1]
                for j in range(1, K // m + 1):
                    coef.append(coef[-1] * (cm + j - 1) // j)
                prod = [sum(coef[j] * prod[n - j * m] for j in range(n // m + 1)) for n in range(K + 1)]
            euler_ok = cycles_ok and all(prod[n] == f[n] for n in range(K + 1))
            # the mirror image f^-1 has the same counts: det(f^-n - 1) = det(f^-n) det(1 - f^n)
            Pi, inv = ((1, 0), (0, 1)), ((A[1][1], -A[0][1]), (-A[1][0], A[0][0]))
            mirror_ok = True
            for n in range(1, K + 1):
                Pi = tuple(tuple(sum(Pi[i][k] * inv[k][j] for k in range(2)) * sign for j in range(2)) for i in range(2))
                mirror_ok &= abs((Pi[0][0] - 1) * (Pi[1][1] - 1) - Pi[0][1] * Pi[1][0]) == N[n - 1]
            growth = [mp.log(N[n - 1]) / n for n in (10, 20, 40)]
            key = ("+" if sign == 1 else "-") + name.split()[0]
            res[key] = {"trace": t, "N_1..N_6": N[:6], "N_n = lambda^n + lambda^-n - 2 sign^n to n = 40": trace_form,
                        "zeta = (1 - sign z)^2/(1 - t z + z^2) exactly to order 40": zeta_ok,
                        "orbits of least period 1..6 (c_m)": [int(x) for x in c[1:7]],
                        "Euler product over orbits to order 40": euler_ok, "N_n(f^-1) = N_n(f) to n = 40": mirror_ok,
                        "(1/n) log N_n at n = 10, 20, 40": [mp.nstr(g, 12) for g in growth],
                        "beta_c = log lambda": mp.nstr(mp.log(lam), 20)}
            say(f"C3 {key}: N_1..6 = {N[:6]}; trace form {trace_form}; zeta closed form to order {K} {zeta_ok}; "
                f"orbits c_1..6 = {[int(x) for x in c[1:7]]}, Euler product {euler_ok}; mirror counts {mirror_ok}; "
                f"(1/n) log N_n -> {res[key]['(1/n) log N_n at n = 10, 20, 40']}; beta_c = log lambda = "
                f"{res[key]['beta_c = log lambda']}")
    phi = (1 + mp.sqrt(5)) / 2
    res["2 log phi"] = mp.nstr(2 * mp.log(phi), 20)
    res["2 log(1 + sqrt 2)"] = mp.nstr(2 * mp.log(1 + mp.sqrt(2)), 20)
    res["holds"] = (all(v["zeta = (1 - sign z)^2/(1 - t z + z^2) exactly to order 40"]
                        and v["N_n = lambda^n + lambda^-n - 2 sign^n to n = 40"] and v["Euler product over orbits to order 40"]
                        and v["N_n(f^-1) = N_n(f) to n = 40"] for k, v in res.items() if isinstance(v, dict))
                    and res["+LR"]["beta_c = log lambda"] == res["2 log phi"]
                    and res["+LLRR"]["beta_c = log lambda"] == res["2 log(1 + sqrt 2)"])
    say(f"   2 log phi = {res['2 log phi']}; 2 log(1 + sqrt 2) = {res['2 log(1 + sqrt 2)']}; C3 holds: {res['holds']}")
    return res


def c4():
    sys.path.insert(0, str(B1530))
    import exact_lib as E
    import exact_states as S
    G, img, chars, D = S.group("-", "LLRR")
    rho = S.four_module(S.m135_sl2())
    assert rho.check(G.rels)
    ch = S.nu("-", (Fraction(0), Fraction(1, 2)), 0)
    V = rho.twist(ch)
    CE = E.Cohomology(G, V)
    ints = CE.interior()
    assert CE.h1 == 2 and len(ints) == 1
    c_int = CE.combine(ints[0])
    zero = [x * 0 for x in c_int]
    out = {}
    for name, c in (("the split vacuum V (+) 1", zero), ("W1 at the interior class", c_int)):
        W = E.extension(V, c, None)
        assert W.check(G.rels)
        out[name] = [E.class_index(G, W)["I"], E.class_index(G, W.wedge2())["I"]]
    CEd = E.Cohomology(G, V.dual())
    dints = CEd.interior()
    W2s = E.extension(V.dual(), CEd.combine(dints[0]), None)
    out["W2 (the dual order) at the interior class"] = [-E.class_index(G, W2s)["I"], -E.class_index(G, W2s.wedge2())["I"]]
    ok = (out["the split vacuum V (+) 1"] == [0, 0] and out["W1 at the interior class"] == [-1, -1]
          and out["W2 (the dual order) at the interior class"] == [1, 1])
    say(f"C4 m135, u = (0, 1/2), exactly: {out} -> the split vacuum reads (0, 0) and the two orders (-1, -1), (+1, +1): {ok}")
    return {"readings (I(W), I(Lambda^2 W))": out, "holds": ok}


def c5():
    lane = REFS["origin/audit/physical-bridge-2026-09-05"]
    rep = lane + ":reports/physical_bridge_2026_09_05/"
    texts = {
        "main B1455 (origin/main: docs/handoffs/CHAT1_SELECTION_RULE_2026-10-02_VERDICT.md)":
            git("show", REFS["origin/main"] + ":docs/handoffs/CHAT1_SELECTION_RULE_2026-10-02_VERDICT.md"),
        "the audit lane's R76 (FLAT_VACUUM.md)": git("show", rep + "FLAT_VACUUM.md"),
        "the audit lane's F01 (COEFFICIENT_PARENT_PROOF.md)": git("show", rep + "COEFFICIENT_PARENT_PROOF.md"),
        "the audit lane's R41 (CURRENT_BALANCE.md)": git("show", rep + "CURRENT_BALANCE.md"),
        "the audit lane's R81 (DIRICHLET_ADMISSION.md)": git("show", rep + "DIRICHLET_ADMISSION.md"),
        "the audit lane's F14 (received_r47/F14_FINDINGS.txt)": git("show", rep + "received_r47/F14_FINDINGS.txt"),
        "the audit lane's PB-CHIRAL (docs/OPEN_LEADS.md)": git("show", lane + ":docs/OPEN_LEADS.md"),
        "the audit lane's R48 (CANONICAL_DUALITY.md)": git("show", rep + "CANONICAL_DUALITY.md"),
        "B849 (frontier/B849_order_parameter/FINDINGS.md, every head)":
            git("show", REFS["origin/main"] + ":frontier/B849_order_parameter/FINDINGS.md"),
        "OPEN_LEADS L17 (every head)": git("show", REFS["origin/main"] + ":docs/OPEN_LEADS.md"),
        "xB032 (origin/sep16-branch: frontier/xB032_the_thermodynamic_side/FINDINGS.md)":
            git("show", REFS["origin/sep16-branch"] + ":frontier/xB032_the_thermodynamic_side/FINDINGS.md")}
    quotes = {
        "main B1455 (origin/main: docs/handoffs/CHAT1_SELECTION_RULE_2026-10-02_VERDICT.md)": [
            "every vacuum is fixed by a symmetry under which the count is odd",
            "the geometric mirror does not change the count; dualising does",
            "A non-split extension: not a minimum of this action",
            "Spontaneous breaking in the bulk action: **tested here, negative on this family."],
        "the audit lane's R76 (FLAT_VACUUM.md)": [
            "a smooth stationary FLAT point must be harmonic",
            "the potential is a t^2+c t^4, a>=0,c>0",
            "the split limit, at infinite TARGET metric distance",
            "Nonflat, coupled-field, source, physical-end, singular and infinite-energy models are outside this conclusion."],
        "the audit lane's F01 (COEFFICIENT_PARENT_PROOF.md)": [
            "The F01 finite-energy splitting obstruction still applies to a smooth complete source-free nonsplit W."],
        "the audit lane's R41 (CURRENT_BALANCE.md)": [
            "integral tr(xi_k S) = 4 integral |eta_k|^2 > 0, k=1,2,3."],
        "the audit lane's R81 (DIRICHLET_ADMISSION.md)": [
            "admits a unique harmonic metric for that boundary value problem",
            "It is therefore a zero-potential stationary background of the specified bare positive residual-square action",
            "2 flux=-5 integral|eta|^2. Boundary data are a supplied input, not yet a physically generated law."],
        "the audit lane's F14 (received_r47/F14_FINDINGS.txt)": [
            "A spontaneously asymmetric interacting phase remains logically possible despite an exact classical symmetry.",
            "not inference from an allowed vertex or an arbitrary choice of one member of a paired basis."],
        "the audit lane's PB-CHIRAL (docs/OPEN_LEADS.md)": [
            "PB-CHIRAL: an escape must change a stated end/source/coefficient/domain hypothesis or realize an asymmetric "
            "interacting phase with full spectrum and anomaly matching."],
        "the audit lane's R48 (CANONICAL_DUALITY.md)": [
            "A chirality mechanism must change an earned hypothesis or realize an asymmetric interacting phase, with the "
            "full light spectrum and anomaly accounting."],
        "B849 (frontier/B849_order_parameter/FINDINGS.md, every head)": [
            "In SSB the **system** carries the symmetry and the **state** breaks it.",
            "m004's amphichirality is the \u2124/2 existing, which is exactly what SSB requires."],
        "OPEN_LEADS L17 (every head)": [
            "so the symmetric phase is excluded by structure",
            "the \"*empty*\" framing is **FALSE**"],
        "xB032 (origin/sep16-branch: frontier/xB032_the_thermodynamic_side/FINDINGS.md)": [
            "`0.9624236501` = `2 log \u03c6`",
            "| RRLL | 6 | 5.82842712 | 1.76274717 | 3.663862 | 1.7627471740 |"]}
    found = {}
    for src, qs in quotes.items():
        text = texts[src]
        assert text, src
        flat = re.sub(r"\s+", " ", text)
        found[src] = {q: (re.sub(r"\s+", " ", q) in flat) for q in qs}
    ok = all(v for d in found.values() for v in d.values())
    say(f"C5 the record's dynamics quoted at source: all quotes present: {ok}")
    return {"quotes found": found, "holds": ok}


def c6():
    import snappy
    K = ((0, 1), (-1, 0))
    Kinv = ((0, -1), (1, 0))

    def mul(X, Y):
        return tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    conj = {}
    for name, A in (("LR", ((2, 1), (1, 1))), ("LLRR", ((1, 2), (2, 5)))):
        for sign in (1, -1):
            B = tuple(tuple(sign * x for x in row) for row in A)
            Binv = tuple(tuple(sign * x for x in row) for row in ((A[1][1], -A[0][1]), (-A[1][0], A[0][0])))
            conj[("+" if sign == 1 else "-") + name] = mul(mul(K, B), Kinv) == Binv
    amph = {}
    for name, word in (("m004", "+LR"), ("m003", "-LR"), ("m136", "+LLRR"), ("m135", "-LLRR")):
        M = snappy.Manifold(name)
        amph[name] = {"word": word, "amphicheiral": bool(M.symmetry_group().is_amphicheiral()),
                      "the bundle b+" + word + " is it": bool(snappy.Manifold("b+" + word).is_isometric_to(M))}
    ok = all(conj.values()) and all(v["amphicheiral"] and v["the bundle b+" + v["word"] + " is it"] for v in amph.values())
    say(f"C6 K f K^-1 = f^-1 with det K = 1: {conj}; SnapPy: " + ", ".join(f"{k} ({v['word']}) amphicheiral "
                                                                          f"{v['amphicheiral']}" for k, v in amph.items())
        + f" -> holds: {ok}")
    return {"K = [[0, 1], [-1, 0]] conjugates f to f^-1": conj, "SnapPy": amph, "holds": ok}


def main():
    t0 = time.time()
    say(f"B1531 checks, {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}, at {git('rev-parse', '--short', 'HEAD').strip()} "
        f"(main {git('rev-parse', '--short', 'origin/main').strip()})")
    res = {}
    for key, fn in (("C1", c1), ("C2", c2), ("C2b", c2b), ("C3", c3), ("C5", c5), ("C6", c6), ("C4", c4)):
        t1 = time.time()
        res[key] = fn()
        say(f"   ({key}: {time.time() - t1:.1f} s)")
    res["seconds"] = round(time.time() - t0)
    say(f"done ({res['seconds']} s)")
    (HERE / "symmetric_phase_checks.json").write_text(json.dumps(res, indent=1, default=str))
    (HERE / "symmetric_phase_checks_run.txt").write_text("\n".join(LOG) + "\n")


if __name__ == "__main__":
    main()
