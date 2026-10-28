import sys, math, numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent)); import ref_lib as RL
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent.parent)); import curvature as K
B = RL.B
PROF = K.PROFILES
def Wf(prof, eps, Q, shift=0.0):
    return lambda z: np.exp(-Q*eps*(PROF[prof](*RL.lattice(z, t)) - shift))
for (a, b, im, prof, e) in ((Fr(2,5), Fr(1,10), 3.0, "asym", 1.0), (Fr(2,5), Fr(1,10), 3.0, "cos2pi_y1", 0.2), (Fr(2,5), Fr(23,30), 3.0, "asym", 0.2), (Fr(2,5), Fr(1,10), 3.0, "asym", 4.0)):
    t = complex(0.3, im); S = RL.higgs_S(t); L = RL.L_of(im); sd = RL.sector_data(a, b, t)
    phi0 = float(PROF[prof](0.0, 0.0))
    # my norms (both sectors -- they must agree)
    cs = {}
    for sec in ("down", "lep"):
        x, y, R = sd[sec]
        for n in (64, 96, 160):
            c, W0 = RL.c_weighted(x, y, t, R, Wf(prof, e, 3), n=n); cs[(sec, n)] = c
    c = cs[("down", 160)]
    conv = max(abs(cs[("down", 96)][s] - c[s])/max(1, abs(c[s])) for s in c if c[s] is not None)
    same = max(abs(cs[("lep", 160)][s] - c[s])/max(1, abs(c[s])) for s in c if c[s] is not None)
    # the draft's own routine
    xd, yd, Rd = sd["down"]; cd = K.cA_w(xd, yd, t, Rd, 3, prof, e)
    agree = max(abs(cd[s] - c[s])/max(1, abs(c[s])) for s in c if c[s] is not None)
    print("(%s,%s) Im %g %s eps %g: phi(0) %.3f W0 %.3e | my c %s | quad conv 96->160 %.1e | down=lep %.1e | vs draft cA_w %.1e"
          % (a, b, im, prof, e, phi0, W0, {s: round(c[s], 4) for s in c}, conv, same, agree))
    Rl = sd["lep"][2]
    lam_draft = {s: 2*math.pi*L + c[s] for s in c}                        # the draft's form
    lam_corr = {s: 2*math.pi*W0*L + c[s] for s in c}                      # the cusp log carries W(0)
    R2a, R1a, _ = RL.ratios_from_lam2(lam_draft, Rd, Rl, S)
    R2b, R1b, _ = RL.ratios_from_lam2(lam_corr, Rd, Rl, S)
    print("     draft form 2piL + c:     lam2 %s  R2 %.5f R1 %.5f" % ({s: round(v, 3) for s, v in lam_draft.items()}, R2a, R1a))
    print("     corrected 2piW0 L + c:   lam2 %s  R2 %.5f R1 %.5f" % ({s: round(v, 4) for s, v in lam_corr.items()}, R2b, R1b))
    # gauge test on the draft's own pipeline: phi -> phi - phi(0) (a constant: physically an overall metric rescale)
    K.PROFILES["_shift"] = (lambda p, s0: (lambda x1, y1: p(x1, y1) - s0))(PROF[prof], phi0)
    R2s, R1s, _ = K.ratios(0.3, im, a, b, "_shift", e, K.cA_w)
    R2o, R1o, _ = K.ratios(0.3, im, a, b, prof, e, K.cA_w)
    print("     draft pipeline: phi  R2 %.5f R1 %.5f | phi - phi(0) (same curvature)  R2 %.5f R1 %.5f" % (R2o, R1o, R2s, R1s), flush=True)
