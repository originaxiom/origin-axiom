"""c8: SEVEN_PILLARS s5's top-Yukawa running vector gamma_t = (-3,-3,+1,+1,0,0,0,-1,-1,-2) for
(m_c/m_t, m_u/m_t, m_s/m_b, m_d/m_b, m_mu/m_tau, m_e/m_tau, |V_us|, |V_cb|, |V_ub|, J) -- can it be one-loop SM running?
Data-free: a random hierarchical Yukawa configuration (no measured numbers), one small RG step of the flavour-non-universal
one-loop terms (universal terms change no ratio and no mixing), d ln O / dI with dI = y_t^2 dt / (16 pi^2), normalised so
that the up ratios read -3.  SM: beta(Y_u) = 3/2 (Y_u Y_u^+ - Y_d Y_d^+) Y_u, beta(Y_d) = 3/2 (Y_d Y_d^+ - Y_u Y_u^+) Y_d.
MSSM (for reference): beta(Y_u) = (3 Y_u Y_u^+ + Y_d Y_d^+) Y_u, beta(Y_d) = (3 Y_d Y_d^+ + Y_u Y_u^+) Y_d."""
import pathlib
import numpy as np
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
rng = np.random.default_rng(7)
def haar(n=3):
    z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2); q, r = np.linalg.qr(z); return q * (np.diag(r) / abs(np.diag(r)))
def near_id(eps):
    a = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) * eps; h = (a + a.conj().T) / 2
    w, v = np.linalg.eigh(h); return v @ np.diag(np.exp(1j * w)) @ v.conj().T
def obs(Yu, Yd):
    uu, su, _ = np.linalg.svd(Yu); ud, sd, _ = np.linalg.svd(Yd)
    ou, od = np.argsort(su), np.argsort(sd); uu, su, ud, sd = uu[:, ou], su[ou], ud[:, od], sd[od]
    V = uu.conj().T @ ud
    J = np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1]))
    return np.array([su[1] / su[2], su[0] / su[2], sd[1] / sd[2], sd[0] / sd[2], abs(V[0, 1]), abs(V[1, 2]), abs(V[0, 2]), abs(J)])
names = ["m_c/m_t", "m_u/m_t", "m_s/m_b", "m_d/m_b", "|V_us|", "|V_cb|", "|V_ub|", "|J|"]
claimed = [-3, -3, +1, +1, 0, -1, -1, -2]
for model in ("SM", "MSSM"):
    rows = []
    for trial in range(4):
        VL = near_id(0.15); UR, DR = haar(), haar()
        Yu = np.diag([1e-5, 4e-3, 1.0]) @ UR.conj().T
        Yd = VL @ np.diag([2e-5, 4e-4, 2e-2]) @ DR.conj().T
        eps = 1e-6
        if model == "SM":
            bu = 1.5 * (Yu @ Yu.conj().T - Yd @ Yd.conj().T) @ Yu; bd = 1.5 * (Yd @ Yd.conj().T - Yu @ Yu.conj().T) @ Yd
        else:
            bu = (3 * Yu @ Yu.conj().T + Yd @ Yd.conj().T) @ Yu; bd = (3 * Yd @ Yd.conj().T + Yu @ Yu.conj().T) @ Yd
        o0 = obs(Yu, Yd); o1 = obs(Yu + eps * bu, Yd + eps * bd)
        g = (np.log(o1) - np.log(o0)) / eps          # per unit dI = y_t^2 dt/16pi^2 (y_t = 1)
        rows.append(g * (-3 / g[0]))                 # normalise: up ratio m_c/m_t -> -3
    r = np.mean(rows, axis=0)
    say("%-4s (normalised to m_c/m_t = -3): " % model + ", ".join("%s %+.2f" % (n, v) for n, v in zip(names, r)))
say("claimed (SEVEN_PILLARS s5):              " + ", ".join("%s %+d" % (n, v) for n, v in zip(names, claimed)))
pathlib.Path(__file__).with_name("c8_sm_one_loop_ratio_exponents_out.txt").write_text("\n".join(out) + "\n")
