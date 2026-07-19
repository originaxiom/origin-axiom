"""B703 / chat1 Q3 — the Koide angle theta_0 vs 2/9, exact sigma-distance (firewalled)."""
import mpmath as mp
mp.mp.dps = 30
# PDG lepton masses (MeV), 1-sigma
ME, SME   = mp.mpf('0.51099895000'), mp.mpf('0.00000000015')
MMU, SMMU = mp.mpf('105.6583755'),   mp.mpf('0.0000023')
MTAU, SMT = mp.mpf('1776.86'),       mp.mpf('0.12')

def koide_Q(a, b, c):
    return (a + b + c) / (mp.sqrt(a) + mp.sqrt(b) + mp.sqrt(c))**2

def theta0(a, b, c):
    s = [mp.sqrt(a), mp.sqrt(b), mp.sqrt(c)]; M = sum(s) / 3
    xs = [(si / M - 1) / mp.sqrt(2) for si in s]
    phi = [0, 2 * mp.pi / 3, 4 * mp.pi / 3]
    C = sum(xs[i] * mp.cos(phi[i]) for i in range(3))
    S = -sum(xs[i] * mp.sin(phi[i]) for i in range(3))
    th = mp.atan2(S, C)
    return th - 2 * mp.pi / 3 if th > 1 else th          # physical branch ~0.222

def sigma_theta():
    def d(i, sm):
        h = mp.mpf('1e-9'); a = [ME, MMU, MTAU]
        a1 = a[:]; a1[i] += h; a2 = a[:]; a2[i] -= h
        return (theta0(*a1) - theta0(*a2)) / (2 * h) * sm
    return mp.sqrt(sum(d(i, s)**2 for i, s in enumerate([SME, SMMU, SMT])))

if __name__ == "__main__":
    th = theta0(ME, MMU, MTAU); tgt = mp.mpf(2) / 9; sig = sigma_theta()
    print("Koide Q          =", mp.nstr(koide_Q(ME, MMU, MTAU), 12), "(2/3 tautology, B686)")
    print("theta_0          =", mp.nstr(th, 12), "rad")
    print("2/9              =", mp.nstr(tgt, 12))
    print("sigma-distance   =", mp.nstr(abs(th - tgt) / sig, 4), "sigma  (chat1 said ~7; WRONG)")
    print("m_tau for 2/9    =", mp.nstr(MTAU - abs(th - tgt) / sig * SMT, 10), "MeV (inside 1776.86+-0.12)")
