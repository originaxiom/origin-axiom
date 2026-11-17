"""B1945 section 6, corrected (2026-11-17): what is and is not covariant in an amplitude read-out of frame C.
agy-002's A2-AMP (harvest row 1849) states Y_f(g tau, w) = phi_f(g, w) U_L(g) Y_f(tau, w g) U_R,f(g)^dagger, with unitaries
independent of the point w and phi a scalar phase.  Main tests three consequences on its own frame code:
  G  the left Gramian (1/24) sum_w Y Y^dagger has the same eigenvalue ratios at tau and at tau + 1 (the phase and U_R drop);
  T5 the plain sum over the 24 points at tau and at tau + 5: the same singular ratios if the phases close at level 5;
  T25 the same at tau + 25.
  S   the Gramian's ratios at -1/tau, with the end carried by its own law L(-1/tau) = L(tau) + log|tau| (B1927), and, as a
      control, with the end held equal.  The end is passed explicitly here: the record's table (canon_readout.canon) does
      not cover -1/tau at this point, and below its lower edge it returns a nearest-neighbour value with no flag (P-864).
  E   the table against its own law where it does cover both points: i/0.9 and 0.9i, 0.3 + 0.96i and its image."""
import json, math, pathlib, sys
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import determinant_law as DL
mp = DL.mp
PTS = [(Fr(i, 5), Fr(j, 5)) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
TX, TY = "0.13", 1.7


def objs(tx, ty, sec, rd):
    G = mp.zeros(3, 3); S = mp.zeros(3, 3)
    for a, b in PTS:
        Y = DL.parts(tx, ty, a, b, sec)[2][rd]
        G += Y * Y.H; S += Y
    return G / 24, S


def ratios(M, herm=False):
    s = sorted((abs(v) for v in (mp.eigh(M)[0] if herm else mp.svd_c(M, compute_uv=False))), reverse=True)
    return [s[1] / s[0], s[2] / s[0]]


def dev(x, y):
    return float(max(abs(a / b - 1) for a, b in zip(x, y)))


if __name__ == "__main__":
    CR = DL.FM.CR; table = CR.canon
    t = mp.mpc(mp.mpf(TX), TY); s = -1 / t; t_f = complex(float(TX), TY)
    L0 = table(t_f)["L_2"]; sx, sy = mp.nstr(s.real, 40), float(s.imag)
    out = {"end_at_tau": L0, "table_at_minus_one_over_tau": table(complex(float(s.real), sy))["L_2"], "law_at_minus_one_over_tau": L0 + math.log(abs(t_f))}
    print("the end at tau: %.6f; by its law at -1/tau: %.6f; the table's value there (below its edge, nearest neighbour): %.6f"
          % (L0, out["law_at_minus_one_over_tau"], out["table_at_minus_one_over_tau"]), flush=True)
    for name, z in (("0.9i", complex(0, 0.9)), ("0.3 + 0.96i", complex(0.3, 0.96))):
        w = -1 / z; d = table(w)["L_2"] - (table(z)["L_2"] + math.log(abs(z)))
        out["table_law_defect " + name] = d
        print("E: the table inside its domain, at %s and its image: L(-1/z) - L(z) - log|z| = %.2e" % (name, d), flush=True)
    for sec in ("up", "down"):
        for rd in ("S", "St"):
            G0, S0 = objs(TX, TY, sec, rd)
            G1, _ = objs("1.13", TY, sec, rd); _, S5 = objs("5.13", TY, sec, rd); _, S25 = objs("25.13", TY, sec, rd)
            CR.canon = lambda z: {"L_2": L0 + math.log(abs(t_f))}
            GL, _ = objs(sx, sy, sec, rd)
            CR.canon = lambda z: {"L_2": L0}
            GE, _ = objs(sx, sy, sec, rd)
            CR.canon = table
            r = {"G_T": dev(ratios(G1, True), ratios(G0, True)), "sum_T5": dev(ratios(S5), ratios(S0)),
                 "sum_T25": dev(ratios(S25), ratios(S0)), "G_S_law": dev(ratios(GL, True), ratios(G0, True)),
                 "G_S_end_held_equal": dev(ratios(GE, True), ratios(G0, True))}
            out["%s %s" % (sec, rd)] = r
            print("%-4s %-2s: Gramian under tau+1 %.1e | plain sum under tau+5 %.2e, under tau+25 %.2e | Gramian at -1/tau: the end by its law %.1e, held equal %.2e"
                  % (sec, rd, r["G_T"], r["sum_T5"], r["sum_T25"], r["G_S_law"], r["G_S_end_held_equal"]), flush=True)
    (HERE / "gramian_and_sum.json").write_text(json.dumps(out, indent=1) + "\n")
