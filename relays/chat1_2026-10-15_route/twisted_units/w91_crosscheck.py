"""chat1: W91's twisted coupling vector against chat1's instrument, at excluded orders only (N = 3, 5, 7).
chat1's u_s = c_s T_s(ubar) T_s(delta) / theta1'(0), T(al, be) = e^{i pi al^2 tau + 2 pi i al be} theta(be + al tau),
(al, be) = k (lb, la)/N for its line (la, lb), i.e. w = (la + lb tau)/N; W91's V_s with w = psi1 tau - psi2.
Matching w gives psi = (lb/N, -la/N), and the two differ by the constant e^{2 pi i (ku^2 + kd^2) la lb / N^2}."""
import sys, importlib.util
from fractions import Fraction as Fr
import mpmath as mp
import flint
from flint import arb, acb
sys.path.insert(0, sys.argv[1])               # chat1's twisted_units directory
import units_cells as UC
spec = importlib.util.spec_from_file_location("w91", sys.argv[2]); W = importlib.util.module_from_spec(spec)
spec.loader.exec_module(W)
mp.mp.dps = 60; flint.ctx.prec = 300
CHMAP = {"i": 0, "j": 1, "k": 2}
worst_direct = worst_series = worst_phase = 0.0
taus = [mp.mpc("0.13", "1.1"), mp.mpc("-0.31", "0.95"), mp.mpc("0.42", "2.0")]
n = 0
for N in (3, 5, 7):
    for la, lb in ((0, 1), (1, 0), (1, 1), (2, 1), (1, 3)):
        if (la, lb) == (1, 3) and N == 3: continue
        psi = (Fr(lb, N), Fr(-la, N))
        for name, (qL, qR) in W.SECTORS.items():
            ku, kd = qL + qR, qL - qR
            ser = W.V_series(ku, kd, psi, Fr(30))
            for t in taus:
                tA = acb(arb(mp.nstr(t.real, 50)), arb(mp.nstr(t.imag, 50)))
                d1 = UC.th1p(tA)
                ub = (arb(ku * lb) / N, arb(ku * la) / N); de = (arb(kd * lb) / N, arb(kd * la) / N)
                mine = UC.quat3(tA, ub, de, d1)
                mine = [mp.mpc(mp.mpf(x.real.mid().str(50, radius=False)), mp.mpf(x.imag.mid().str(50, radius=False))) for x in mine]
                vd, vs = W.V_direct(ku, kd, psi, t), W.ev_series(ser, t)
                ph = mp.expjpi(2 * mp.mpf((ku * ku + kd * kd) * la * lb) / (N * N))
                scale = max(abs(m) for m in mine)
                for u, c in CHMAP.items():
                    worst_direct = max(worst_direct, float(abs(mine[c] - ph * vd[u]) / scale))
                    worst_series = max(worst_series, float(abs(vd[u] - vs[u]) / max(abs(vd[x]) for x in CHMAP)))
                n += 1
print(f"{n} (N, line, sector, tau) cases at N = 3, 5, 7")
print("chat1's u_s against W91's V_s (direct), with psi = (lb/N, -la/N) and the phase e^{2 pi i (ku^2+kd^2) la lb/N^2}:", f"{worst_direct:.1e}")
print("W91's exact series (exponent 30) against its direct evaluation:", f"{worst_series:.1e}")
