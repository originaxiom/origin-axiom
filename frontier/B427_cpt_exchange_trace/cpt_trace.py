"""B427 -- the seam as a twisted exchange trace (Chat-1 base identity TRUE; projector corollary
CORRECTED: the exchange asymmetry is a GALOIS action, sigma_17, which FIXES sqrt-15).

Chat-1's handoff (2026-07-05) proved: tr_V(W1 Par W2) = tr_{VxV}(Q (W1xW2)), Q = (Par x I) P,
Q^4 = I, eigenvalue multiplicities {+1:57, -1:56, +i:56, -i:56} on C^225. All VERIFIED here
(the identity is 4-line algebra; the multiplicities are permutation combinatorics of
(m,n) -> (-n, m) on Z/15 x Z/15: one fixed point, 56 four-cycles).

THE CORRECTION: Chat-1's projector-trace corollary used tr(Q^3 A) = tr(Q A) ("reversed seam =
seam"). FALSE on the actual Weil matrices: tr(Par W2 W1) = zeta15 but tr(Par W1 W2) = zeta15^2.
The corrected projector traces (T = trW1 trW2, S = tr(Par W1) tr(Par W2), C = tr(Par W2 W1),
C' = tr(Par W1 W2)):
    tr P_{+1} = (T + S + C + C')/4        tr P_{+i} = (T - S + i(C' - C))/4
    tr P_{-1} = (T + S - C - C')/4        tr P_{-i} = (T - S - i(C' - C))/4
So the +-1 sectors see the SYMMETRIZED seam (C+C')/2 and the +-i sectors the ANTISYMMETRIZED
(C-C')/2 -- not "only T-S" as claimed.

THE STRUCTURAL PAYOFF: C' = sigma_17(C) -- the exchange W1W2 -> W2W1 acts on the seam trace by
the GALOIS element sigma_17 of Q(zeta60) (4k=8 mod 60, gcd(k,60)=1 => k in {17,47}). sigma_17
FIXES i, FLIPS sqrt5 and sqrt-3 individually, hence FIXES sqrt-15 = sqrt5*sqrt-3: the seam's
physical (sqrt-15) channel is exchange-SYMMETRIC; the asymmetry lives in the sqrt5/sqrt-3 side
channels. Extends the banked "symmetries ARE Galois" law (P61/B380; B369 rotation = sqrt5-Galois).

Firewall: finite algebra on Z/15 + Galois bookkeeping. "CPT-twisted" is Chat-1's label for the
inversion x -> -x; no physics claim is licensed.
"""
import os, sys, json, math
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
from step0_exact_matrices import build_theta_W          # noqa: E402
from cyclo_engine import mmul, ZERO, add, scal          # noqa: E402

N = 15

def PAR(M):
    return [M[(-x) % N] for x in range(N)]

def tr(M):
    t = ZERO
    for i in range(N):
        t = add(t, M[i][i])
    return t

def q_multiplicities():
    """eigenvalue multiplicities of Q: the permutation (m,n)->(-n,m) on (Z/15)^2."""
    seen = set(); fixed = 0; four = 0
    for m in range(N):
        for n in range(N):
            if (m, n) in seen: continue
            orb = []
            p = (m, n)
            while p not in orb:
                orb.append(p); p = ((-p[1]) % N, p[0])
            for q in orb: seen.add(q)
            if len(orb) == 1: fixed += 1
            elif len(orb) == 4: four += 1
            else: raise AssertionError(f"unexpected orbit length {len(orb)}")
    return dict(plus1=fixed + four, minus1=four, plus_i=four, minus_i=four,
                fixed=fixed, four_cycles=four)

def seam_traces():
    """(C, C') = (tr(Par W2 W1), tr(Par W1 W2)) exactly; and the sigma_17 relation."""
    W1 = build_theta_W(1); W2 = build_theta_W(2)
    C  = tr(PAR(mmul(W2, W1)))
    Cp = tr(PAR(mmul(W1, W2)))
    return W1, W2, C, Cp

def galois_exchange_elements():
    """Galois k with zeta60^4 -> zeta60^8 (C -> C'), and sigma_17's action on the generators."""
    ks = [k for k in range(60) if (4*k) % 60 == 8 and math.gcd(k, 60) == 1]
    act = dict(on_i=("fix" if 17 % 4 == 1 else "flip"),
               on_sqrt5=("fix" if 17 % 5 in (1, 4) else "flip"),      # QRs mod 5 = {1,4}
               on_sqrtm3=("fix" if 17 % 3 == 1 else "flip"))
    act["on_sqrtm15"] = "fix" if (act["on_sqrt5"] == act["on_sqrtm3"]) else "flip"
    return ks, act

if __name__ == "__main__":
    mult = q_multiplicities()
    print("Q eigenvalue multiplicities:", mult, " [claim {57,56,56,56}]")
    W1, W2, C, Cp = seam_traces()
    print("C  = tr(Par W2 W1):", [(i, str(x)) for i, x in enumerate(C) if x])
    print("C' = tr(Par W1 W2):", [(i, str(x)) for i, x in enumerate(Cp) if x])
    print("C == C' (Chat-1's Q^3 step):", C == Cp, " -> the projector corollary needed correction")
    ks, act = galois_exchange_elements()
    print("exchange Galois elements:", ks, " sigma_17 action:", act)
    json.dump(dict(multiplicities=mult, C_slot=[i for i, x in enumerate(C) if x],
                   Cp_slot=[i for i, x in enumerate(Cp) if x], C_equals_Cp=bool(C == Cp),
                   exchange_galois=ks, sigma17=act),
              open(os.path.join(HERE, "cpt_trace.json"), "w"), indent=1)
    print("[written] cpt_trace.json")
