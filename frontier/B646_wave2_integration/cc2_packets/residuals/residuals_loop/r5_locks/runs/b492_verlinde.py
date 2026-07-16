"""Reimplementation (no script existed in frontier/B492_verlinde_boundary_lens/ --
FINDINGS.md says 'Reproducer: inline (Fibonacci S-matrix + Verlinde + AL g-factors)').

Fibonacci modular category: two objects {1, tau}, quantum dims d_1=1, d_tau=phi.
S-matrix (Verlinde): S = (1/D) [[1, phi], [phi, -1]],  D = sqrt(1+phi^2) = total qdim.
Affleck-Ludwig boundary g-factor: g_a = S_{0a} / sqrt(S_00).
Claim (B492 FINDINGS): D = sqrt(1+phi^2) = 1.902113...; g_1=0.72507, g_tau=1.17319,
g_tau/g_1 = phi EXACTLY; ln g_1 = -0.32148, ln g_tau = +0.15973.
"""
import mpmath as mp
mp.mp.dps = 50

phi = (1 + mp.sqrt(5)) / 2
D = mp.sqrt(1 + phi**2)
print(f"phi                = {phi}")
print(f"D = sqrt(1+phi^2)  = {D}   (target 1.902113...)")

S00 = 1 / D
S0tau = phi / D

g1 = S00 / mp.sqrt(S00)     # = sqrt(S00)
gtau = S0tau / mp.sqrt(S00)

print(f"S00                = {S00}")
print(f"S0tau              = {S0tau}")
print(f"g_1  = S00/sqrt(S00)   = {g1}    (target 0.72507)")
print(f"g_tau= S0tau/sqrt(S00) = {gtau}    (target 1.17319)")
print(f"g_tau/g_1              = {gtau/g1}   (claim: EXACTLY phi = {phi})")
print(f"exact symbolic check: g_tau/g_1 - phi = {gtau/g1 - phi}  (should be ~0 to precision)")
print(f"ln g_1   = {mp.log(g1)}   (target -0.32148)")
print(f"ln g_tau = {mp.log(gtau)}   (target +0.15973)")

# Verlinde fusion check: N(tau,tau,1) = N(tau,tau,tau) = 1 (tau x tau = 1 + tau)
# Verlinde formula: N_{ab}^c = sum_x S_{ax} S_{bx} conj(S_{cx}) / S_{0x}
objs = [0, 1]  # 0=1, 1=tau
Smat = [[S00, S0tau], [S0tau, -1/D]]
def verlinde(a, b, c):
    return sum(Smat[a][x]*Smat[b][x]*Smat[c][x]/Smat[0][x] for x in objs)
Ntt1 = verlinde(1, 1, 0)
Nttt = verlinde(1, 1, 1)
print(f"\nVerlinde N(tau,tau,1)   = {Ntt1}  (target 1, exact)")
print(f"Verlinde N(tau,tau,tau) = {Nttt}  (target 1, exact)")
print(f"unitarity check S*S^T = I: ", end="")
prod = [[sum(Smat[i][k]*Smat[j][k] for k in objs) for j in objs] for i in objs]
print(prod)
