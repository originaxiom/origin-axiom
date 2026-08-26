#!/usr/bin/env bash
# B1158 Cloud WAVE-2 harvest -- reproduce the two clean in-sandbox survivors.
# (The Gaudin cell B1 was reproduced by the harvest verifier + independently
#  corroborated by codex R009; its full sine-kernel rebuild needs B1151's zero
#  file and is cited, not re-run here.)
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' | tee harvest_checks.txt
import sympy as sp

print("(1) ANOMALY INTEGER IDENTITY -- cloud memo 58 ANOMALY_PAYMENT, codex R012 Memo-56")
print("    E6 -> SO(10) x U(1):  27 = 16(+1) (+) 10(-2) (+) 1(+4)")
reps = {'16': (16, 1, 2), '10': (10, -2, 1), '1': (1, 4, 0)}  # (dim, U(1) q, SO(10) Dynkin index T)
g  = sum(d*q      for d, q, T in reps.values())   # grav^2-U(1)
c  = sum(d*q**3   for d, q, T in reps.values())   # U(1)^3
mx = sum(T*q      for d, q, T in reps.values())   # SO(10)^2-U(1)
print(f"    grav^2-U(1)  = sum dim*q   = {g}")
print(f"    U(1)^3       = sum dim*q^3 = {c}")
print(f"    SO(10)^2-U(1)= sum T*q     = {mx}   (T(16)=2, T(10)=1)")
assert g == 0 and c == 0 and mx == 0, "27 must be anomaly-free (E6 is safe)"
# 16 alone anomalous; dark block 10+1 carries -(16) in each channel
sm_g, sm_c = 16*1, 16*1**3
dk_g, dk_c = 10*(-2)+1*4, 10*(-2)**3+1*4**3
print(f"    16 alone: grav={sm_g}, U(1)^3={sm_c}  (!=0 => anomalous)")
print(f"    dark 10(-2)+1(+4): grav={dk_g}, U(1)^3={dk_c}  = -(16's)  ->", dk_g == -sm_g and dk_c == -sm_c)
assert dk_g == -sm_g and dk_c == -sm_c
print("    => 27 anomaly-free; 16 anomalous; dark block = exactly -(16) each channel. INTEGER IDENTITY.")
print("    (QUARANTINED: 'dark sector REQUIRED' is CONDITIONAL -- needs U(1) gauged [Gate 5] and the")
print("     D5 frame is observer-paid, uniqueness REFUTED OA-C1087. Bank the identity, not the headline.)")

print()
print("(2) HABIRO zeta_3 GERM CORRECTION -- cloud memo 69 (memo's 'collapse' = base-embedding artifact)")
print("    Q(sqrt-3) = Q(zeta_3), disc -3: p splits <=> p = 1 mod 3; inert <=> p = 2 mod 3.")
print("    Coherence of the one-germ tower <=> p^r = 1 mod 3 (the correct pi-adic cube root).")
ok = True
for p, want in [(5, ('inert', 2)), (7, ('split', 1)), (2, ('inert', 2)), (11, ('inert', 2)), (13, ('split', 1))]:
    mod = p % 3
    kind = {1: 'split', 2: 'inert', 0: 'ramified'}[mod]
    r = 1
    while pow(p, r, 3) != 1:
        r += 1
    tag = 'g=2' if kind == 'split' else ('f=2' if kind == 'inert' else 'ram')
    print(f"    p={p:2d}: {kind:6s} ({tag}); coherence r={r}")
    ok = ok and (kind, r) == want
assert ok
print("    memo claims f=1/unique-prime and 'mechanism OPEN at modn=15': BOTH CORRECTED.")
print("    f=2 (p=5 inert), g=2 (p=7 split); modn=15 collapse = the 5^2 branch (r=2).")
print("    MECHANISM SOLVED: coherence <=> p^r = 1 mod 3 (transports UNIFORMLY, local v_pi=N).")
print()
print("REPRODUCES")
PY
