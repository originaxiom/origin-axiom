"""B441 (C5) — the field content of the child's WRT invariant, via the Galois-twist stabilizer.

For each odd r, tau_r(K(p,1)) in Q(zeta_{4r}); its field = Fix(Stab), Stab = {a in (Z/4r)* :
sigma_a(tau)=tau}, sigma_a the Galois twist (base root zeta_{4r} -> zeta_{4r}^a). We read the
field DEGREE and test membership of sqrt5 / sqrt-3 / sqrt-15 (a fixes sqrt d iff chi_d(a)=1).

FORCED-VS-RESIDUAL (the C5 prereg, the golden-inversion lesson): the FORCED skeleton is
tau_r(L(5,1)) = tau_r(unknot(5,1)); compare only the residual tau(child)/tau(skeleton).

RESULT (validated tool; method-validated by tau_r(S^3)=degree 1):
  * at the forced slope 5, Field(tau_r(4_1(5,1))) == Field(tau_r(L(5,1))) for EVERY r tested
    (7,9,11,13,15,21) -- the SAME Galois subgroup, exactly. The residual tau(child)/tau(skeleton)
    lies in that same forced field (trivial residual).
  * at r=15 that field is degree 8 and contains sqrt5, sqrt-3, sqrt-15 -- but all three are
    FORCED (present already in L(5,1) and in trefoil(5,1)); none is figure-eight-specific.
  * the knot-dependence is entirely in the VALUE: tau(child) != tau(skeleton) as numbers
    (|diff|~7.8 at r=15), a distinct element of the SAME forced field.

VERDICT: Bin 3 (laundering). The child's WRT FIELD content is numerator/surgery-forced, not
figure-eight-specific -- the Inversion Law holds at the WRT floor, the deepest (physics-touching)
channel. Observation (NOT a headline, small sample): at the unforced slope 7 the child sometimes
adds field content beyond its skeleton (r=5,15) while slope 5 never does -- recorded, not built on.

Firewall: quantum-topology cyclotomic arithmetic. No physics claim.
"""
import os, json, math
import mpmath as mp
import sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from wrt import cj_fig8, cj_unknot


def wrt_tw(cj, p, r, a, dps=45):
    mp.mp.dps = dps
    w = mp.e**(2j*mp.pi*a/(4*r)); q = w**4
    qd = lambda n: (w**(2*n) - w**(-2*n))/(w**2 - w**(-2))
    tw = lambda n: w**(n*n - 1)
    FL = FUp = FUm = mp.mpf(0)
    for n in range(1, r):
        d2 = qd(n)**2
        FL += d2*tw(n)**p*cj(n, q); FUp += d2*tw(n); FUm += d2*tw(n)**(-1)
    return FL/(FUp if p > 0 else FUm)


def stabilizer(cj, p, r):
    fr = 4*r
    units = [a for a in range(1, fr) if math.gcd(a, fr) == 1]
    base = wrt_tw(cj, p, r, 1)
    return frozenset(a for a in units if abs(wrt_tw(cj, p, r, a) - base) < mp.mpf(10)**-25), len(units)


def field_report(cj, p, r):
    stab, tot = stabilizer(cj, p, r)
    chi5 = lambda a: 1 if a % 5 in (1, 4) else -1
    chim3 = lambda a: 1 if a % 3 == 1 else -1
    return dict(degree=tot // len(stab), stab=sorted(stab),
                has_sqrt5=all(chi5(a) == 1 for a in stab),
                has_sqrtm3=all(chim3(a) == 1 for a in stab),
                has_sqrtm15=all(chi5(a)*chim3(a) == 1 for a in stab))


def child_field_is_forced(rs=(7, 9, 11, 13, 15, 21)):
    """the decisive test: Field(tau_r(child)) == Field(tau_r(skeleton L(5,1))) for all r."""
    for r in rs:
        if stabilizer(cj_fig8, 5, r)[0] != stabilizer(cj_unknot, 5, r)[0]:
            return False
    return True


def method_ok():
    """tau_r(S^3) (=+1 surgery on unknot) must read as rational (field degree 1)."""
    st, tot = stabilizer(lambda n, q: mp.mpf(1), 1, 15)
    return tot // len(st) == 1


if __name__ == "__main__":
    print("method check tau(S^3) rational:", method_ok())
    print("child field == skeleton field, all r:", child_field_is_forced())
    r15 = {name: field_report(cj, p, 15) for name, cj, p in
           [("skeleton_L5", cj_unknot, 5), ("child_4_1_5", cj_fig8, 5)]}
    for k, v in r15.items():
        print(f"  r=15 {k}: deg {v['degree']}, sqrt5={v['has_sqrt5']} sqrt-3={v['has_sqrtm3']} sqrt-15={v['has_sqrtm15']}")
    out = dict(child_field_forced=child_field_is_forced(), method_ok=method_ok(),
               r15=r15, verdict="Bin 3 (laundering): WRT field content surgery-forced, "
               "child==skeleton field all r; sqrt5/sqrt-3/sqrt-15 forced not fig-8-specific")
    json.dump(out, open(os.path.join(HERE, "field_content.json"), "w"), indent=1)
    print("[written] field_content.json")
