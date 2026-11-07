"""The web seat, 2026-11-06: POST HOC to least_action_check.py (612b3dbb3 -> 0e861a147), written after the read-only
referee's third pass, committed before its run. Data-free (SL(2, Z) arithmetic mod 5 and geodesic lengths only).

The referee found that the pre-registered condition (L) -- E = D_S D_g^-1 fixes each line of own(LR) -- is weaker than
reading (ii) of P-717's choice 2, "the history mod 5 is the golden history", which is E = +-I mod 5 (invisible to the
last finite rung, PSL(2, F5) = A5). The stabiliser of +-v is <+-LR> mod 5, so (L) admits level-5 golden phase shifts
E = +-(LR)^a. Over the same range as the check:
  (1) each defect's class mod 5: +-I (rung-invisible), +-(LR)^a with a != 0 mod 5 (a phase shift the line cannot see),
      or neither; counts;
  (2) the cheapest rung-invisible defects (E = +-I), with their highest apex (reported only);
  (3) the cheapest (L)-invisible defects with their class a;
  (4) the set form ("both asymptotic lifts carry the pair": own(LR) E^-1 = own(LR) as a set): counts and cheapest;
  (5) the tie of (2, 2, 2) with (6): W(2,2,2) C = C W(6) LR with C = I + LR, and the traces of both families at k = 0..10.

    python3 least_action_posthoc_rung.py
"""
import importlib.util
import pathlib
import sys

import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location("least_action_check", HERE / "least_action_check.py")
LA = importlib.util.module_from_spec(sp)
sys.modules["least_action_check"] = LA
sp.loader.exec_module(LA)
D0 = LA.D0
mul, inv, pw, tr, mod5, neg, pm, act, fl = D0.mul, D0.inv, D0.pw, D0.tr, D0.mod5, D0.neg, D0.pm, D0.act, D0.fl
L, R, LR, I2 = D0.L, D0.R, D0.LR, D0.I2
PAIR = LA.PAIR
POW = {a: mod5(pw(LR, a)) for a in range(10)}


def E_of(runs):
    return mul(LA.mat(runs), inv(LA.mat([1] * len(runs))))


def klass(E):
    e = mod5(E)
    for a in range(5):
        if e == POW[a] or e == mod5(neg(POW[a])):
            return a  # 0: +-I (rung-invisible); 1..4: a level-5 golden phase shift
    return None


def set_form(runs):
    Ei = inv(E_of(runs))
    return frozenset(pm(act(w, Ei)) for w in PAIR) == PAIR


if __name__ == "__main__":
    print("POST HOC: least action under the rung's invisibility (the web seat, 2026-11-06)")
    cls, rung, line, setf = {}, [], [], []
    for runs in LA.space():
        k = klass(E_of(runs))
        cls[k] = cls.get(k, 0) + 1
        if k == 0:
            rung.append((LA.excess(runs), runs))
        if k is not None:
            line.append((LA.excess(runs), runs, k))
        if set_form(runs):
            setf.append((LA.excess(runs), runs))
    print("(1) classes mod 5 over %d defects: E = +-I: %d; E = +-(LR)^a, a = 1..4: %s; neither: %d" % (
        sum(cls.values()), cls.get(0, 0), [cls.get(a, 0) for a in range(1, 5)], cls.get(None, 0)))
    rung.sort(key=lambda t: t[0]); line.sort(key=lambda t: t[0]); setf.sort(key=lambda t: t[0])
    print("(2) the cheapest rung-invisible defects (E = +-I), excess at k = 20; highest apex reported only:")
    for d, runs in rung[:8]:
        im, re_ = D0.highest_cf(LA.closed_runs(runs), reps=20)
        print("    %-24s excess %s   apex Im %s Re %s" % (runs, mp.nstr(d, 12), mp.nstr(im, 10), mp.nstr(re_, 6)))
    ties = [r for d, r in rung if abs(d - rung[0][0]) < mp.mpf(10) ** -20]
    print("    cheapest %s, uniquely: %s (within 1e-20: %s); next excess %s" % (rung[0][1], ties == [rung[0][1]], ties, mp.nstr(rung[1][0], 12)))
    print("(3) the cheapest (L)-invisible defects with their class a (E = +-(LR)^a mod 5):")
    for d, runs, k in line[:8]:
        print("    %-24s excess %s   a = %d" % (runs, mp.nstr(d, 12), k))
    print("(4) the set form: %d defects; the cheapest: %s" % (len(setf), "; ".join("%s %s" % (r, mp.nstr(d, 10)) for d, r in setf[:4])))
    W222 = mul(LA.mat((2, 2, 2)), R)
    W6 = mul(LA.mat((6,)), R)
    C = ((LR[0][0] + 1, LR[0][1]), (LR[1][0], LR[1][1] + 1))
    print("(5) W(2,2,2) = %s, W(6) LR = %s, C = I + LR = %s (det %d): W(2,2,2) C = C W(6) LR: %s; C LR = LR C: %s" % (
        W222, mul(W6, LR), C, D0.det(C), mul(W222, C) == mul(mul(C, W6), LR), mul(C, LR) == mul(LR, C)))
    print("    traces tr(W(2,2,2) (LR)^k) against tr(W(6) (LR)^(k+1)), k = 0..10: equal at every k: %s" % all(
        tr(mul(W222, pw(LR, k))) == tr(mul(W6, pw(LR, k + 1))) for k in range(11)))
    print("least_action_posthoc_rung exit 0")
