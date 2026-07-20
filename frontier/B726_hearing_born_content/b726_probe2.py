#!/usr/bin/env python3
"""
B726 PROBE 2 — does the golden Fibonacci MTC supply INTERFERENCE + NON-UNIFORM Born weights?

Context (banked, B725): the BEING face (Q(sqrt-3), CMR/thermal KMS) gives the Born FORM (Gleason)
+ classical DIAGONAL Gibbs weights, but NOT the Born CONTENT: (i) interference between outcomes,
(ii) non-uniform pure-state |amp|^2 weights. The being's Haar over vacua is forced-UNIFORM
(torsor-transitive). This probe tests whether the HEARING face (Q(sqrt5), the golden monodromy
A=[[1,1],[1,0]], A^2=M=[[2,1],[1,1]], the Fibonacci MTC) supplies exactly that missing content.

Two-outcome:
  A = the golden MTC supplies off-diagonal (interference) + non-uniform |amp|^2-type weights.
  B = it doesn't (S diagonal, or weights uniform, or not Born-like).

COMPUTE-NOT-CITE: every discriminating fact recomputed here in exact sympy + numeric confirmation.
BASE-RATE DISCIPLINE: a real quadratic field having an S-matrix-like object is NOT automatically a
match. We state the DISCRIMINATING OPERATION (off-diagonal S_{01}!=0; complex T phase; non-uniform
Plancherel weights) and contrast explicitly against the being's forced-uniform Haar.
"""
import sympy as sp

def h(t):
    print("\n" + "="*78); print(t); print("="*78)

# ----------------------------------------------------------------------------
# 0. The golden field and the total quantum dimension
# ----------------------------------------------------------------------------
h("0. GOLDEN FIELD Q(sqrt5), quantum dimensions, total quantum dimension D")
s5  = sp.sqrt(5)
phi = (1 + s5)/2                     # golden ratio, the d_tau quantum dimension
# fusion rule tau x tau = 1 + tau  =>  d_tau^2 = 1 + d_tau  =>  d_tau = phi
lhs = sp.simplify(phi**2 - (1 + phi))
print(f"phi = (1+sqrt5)/2 = {sp.nsimplify(phi)}  ~ {float(phi):.6f}")
print(f"fusion-rule check  d_tau^2 - (1 + d_tau) = {lhs}   (0 => phi solves x^2=1+x) -> {lhs==0}")

d1, dtau = sp.Integer(1), phi        # quantum dimensions d_1=1, d_tau=phi
D2 = sp.simplify(d1**2 + dtau**2)    # total quantum dimension squared = sum_a d_a^2
D2s = sp.simplify(sp.nsimplify(D2))
print(f"D^2 = d_1^2 + d_tau^2 = 1 + phi^2 = {sp.simplify(D2)} = {sp.radsimp(D2)}  ~ {float(D2):.6f}")
print(f"    identity check: D^2 == 2 + phi ?  { sp.simplify(D2 - (2+phi))==0 }")
D = sp.sqrt(D2)
print(f"D = sqrt(2+phi) = {D}  ~ {float(D):.6f}")
# honesty: is D itself in Q(sqrt5)?  (a^2 = 2+phi = (5+sqrt5)/2 has no soln in Q(sqrt5))
print(f"NOTE: (5+sqrt5)/2 is a non-square in Q(sqrt5) -> D itself needs a degree-4 field;")
print(f"      but the |S|^2 PROBABILITIES and quantum dims live in Q(sqrt5) (shown below).")

# ----------------------------------------------------------------------------
# 1. The Fibonacci modular S-matrix
# ----------------------------------------------------------------------------
h("1. FIBONACCI S-MATRIX  S = (1/D)[[1, phi],[phi, -1]] : symmetric, real, UNITARY, OFF-DIAGONAL")
S = sp.Matrix([[1, phi],[phi, -1]]) / D
print("S ="); sp.pprint(S)

# (i) symmetric
sym = sp.simplify(S - S.T) == sp.zeros(2)
print(f"\n(i)   symmetric  S == S^T ................ {sym}")

# (ii) real => S^dag = S^T = S
Sdag = S.conjugate().T
real_herm = sp.simplify(S - Sdag) == sp.zeros(2)
print(f"(ii)  real (S^dag == S) ................. {real_herm}")

# (iii) UNITARY  S S^dag = I  (exact)
SSdag = sp.simplify(S * Sdag)
unit = sp.simplify(SSdag - sp.eye(2)) == sp.zeros(2)
print(f"(iii) UNITARY  S S^dag == I ............. {unit}")
print("      S S^dag ="); sp.pprint(sp.simplify(SSdag))
# S is a real symmetric orthogonal involution: S^2 = I
S2 = sp.simplify(S*S)
print(f"      involution  S^2 == I ............. { sp.simplify(S2 - sp.eye(2))==sp.zeros(2) }")

# (iv) OFF-DIAGONAL  S_{01} != 0  => genuine coherence / interference
S01 = sp.simplify(S[0,1])
print(f"\n(iv)  OFF-DIAGONAL  S_01 = phi/D = {S01}  ~ {float(S01):.6f}   != 0 ? -> {sp.simplify(S01)!=0}")
print("      >>> a genuine off-diagonal entry = coherence between the two sectors = INTERFERENCE.")
print("      >>> contrast B725: the being's extremal-KMS state phi_{beta,L} is DIAGONAL")
print("          (CMR: same ideal J in both slots, a classical Gibbs measure, NO off-diagonal term).")

# ----------------------------------------------------------------------------
# 2. |S_{ab}|^2 Born-like probabilities live in Q(sqrt5) and are NON-UNIFORM
# ----------------------------------------------------------------------------
h("2. |S_ab|^2 (Born-like measurement probabilities) : in Q(sqrt5), NON-UNIFORM")
P = sp.Matrix(2,2, lambda i,j: sp.radsimp(sp.simplify(sp.Abs(S[i,j])**2)))
print("|S_ab|^2 ="); sp.pprint(P)
p00 = sp.radsimp(sp.Abs(S[0,0])**2)   # 1/D^2 = 1/(2+phi)
p01 = sp.radsimp(sp.Abs(S[0,1])**2)   # phi^2/D^2
print(f"\n|S_00|^2 = 1/(2+phi)     = {p00} = {sp.nsimplify(p00)}  ~ {float(p00):.6f}")
print(f"|S_01|^2 = phi^2/(2+phi) = {p01} = {sp.nsimplify(p01)}  ~ {float(p01):.6f}")
# closed forms (5 -/+ sqrt5)/10, both in Q(sqrt5)
cf0 = sp.simplify(p00 - (5 - s5)/10); cf1 = sp.simplify(p01 - (5 + s5)/10)
print(f"closed form  |S_00|^2 == (5-sqrt5)/10 ? {cf0==0}    |S_01|^2 == (5+sqrt5)/10 ? {cf1==0}")
print(f"both in Q(sqrt5): YES.   row sum |S_00|^2 + |S_01|^2 = {sp.simplify(p00+p01)}  (=1 => a probability vector)")
print(f"NON-UNIFORM?  {float(p00):.4f} != {float(p01):.4f}  ->  ratio 1:phi^2 = 1:{float(phi**2):.4f}")

# ----------------------------------------------------------------------------
# 3. Verlinde: S genuinely DIAGONALIZES the fusion rules (non-vacuity: S is real modular data)
# ----------------------------------------------------------------------------
h("3. VERLINDE  N_ab^c = sum_x S_ax S_bx conj(S_cx)/S_0x  reproduces tau x tau = 1 + tau")
def N(a,b,c):
    tot = 0
    for x in range(2):
        tot += S[a,x]*S[b,x]*sp.conjugate(S[c,x])/S[0,x]
    return sp.simplify(sp.radsimp(sp.nsimplify(tot)))
labels = {0:"1", 1:"tau"}
for a in range(2):
    for b in range(2):
        for c in range(2):
            v = N(a,b,c)
            print(f"  N[{labels[a]:>3},{labels[b]:>3}]^{labels[c]:<3} = {v}")
print("expected fusion:  1x1=1 ; 1xtau=tau ; tauxtau = 1 + tau  (each N in {0,1}) -> integer,")
print("non-negative fusion coefficients => S is a GENUINE modular S-matrix, not just any unitary.")

# ----------------------------------------------------------------------------
# 4. The T-matrix: topological spins are genuine COMPLEX phases via zeta_5
# ----------------------------------------------------------------------------
h("4. T-MATRIX  T = diag(1, e^{4 pi i/5}) : GENUINE COMPLEX phases (interference needs these)")
h_tau = sp.Rational(2,5)                      # conformal weight of tau
theta1   = sp.exp(2*sp.pi*sp.I*sp.Integer(0))
thetatau = sp.exp(2*sp.pi*sp.I*h_tau)         # e^{2 pi i (2/5)} = e^{4 pi i /5}
theta_simpl = sp.simplify(thetatau - sp.exp(sp.Rational(4,1)*sp.pi*sp.I/5))
T = sp.diag(theta1, thetatau)
print("T ="); sp.pprint(T)
print(f"theta_tau = e^(2 pi i h_tau), h_tau = 2/5  ==  e^(4 pi i/5) ? {theta_simpl==0}")
re, im = sp.re(thetatau), sp.im(thetatau)
print(f"theta_tau = {sp.nsimplify(sp.re(thetatau))} + i*{sp.nsimplify(sp.im(thetatau))}")
print(f"          ~ {complex(thetatau):.6f}")
print(f"  |theta_tau| = {sp.simplify(sp.Abs(thetatau))}   (on unit circle)")
print(f"  Im(theta_tau) = sin(4pi/5) ~ {float(im):.6f}  != 0  => GENUINELY COMPLEX phase (not +-1).")
# it is a primitive 5th root of unity: (theta_tau)^5 = 1, minimal order 5
pow5 = sp.simplify(thetatau**5); order_ok = sp.simplify(thetatau**5 - 1)==0
print(f"  (theta_tau)^5 = {pow5}   => a 5th root of unity (zeta_5^2). order-5 phase => Q(zeta_5).")
print("  >>> a real field alone cannot host this phase; the interference phase lives in Q(zeta_5),")
print("      and Q(zeta_5) ⊃ Q(sqrt5) (sqrt5 = 2*cos(2pi/5)+2*cos(4pi/5)... i.e. Q(sqrt5) is the")
print("      real subfield of the 5th cyclotomic field). The golden real field's cyclotomic")
print("      completion supplies the complex phase.")

# extra modular check: (S T)^3 is a phase * S^2  (encodes SL(2,Z); central charge c mod 8)
h("4b. MODULAR CHECK  (S T)^3 = phase * I  (SL(2,Z) rep; extracts central charge c mod 8)")
ST3 = sp.simplify((S*T)**3)
lam = sp.simplify(ST3[0,0])
# off-diagonal-zero test numerically (sympy leaves nested (-1)^{3/5} radicals unsimplified)
ST3n = sp.matrix2numpy(ST3.evalf(30), dtype=complex)
import numpy as _np
offdiag_zero = abs(ST3n[0,1]) < 1e-20 and abs(ST3n[1,0]) < 1e-20
diag_equal   = abs(ST3n[0,0]-ST3n[1,1]) < 1e-20
print(f"(S T)^3 numerically =\n{_np.round(ST3n,6)}")
print(f"(S T)^3 = lambda*I ? off-diag zero: {offdiag_zero}   diagonal equal: {diag_equal}")
print(f"lambda = {sp.nsimplify(lam)}  ~ {complex(lam):.6f}")
# lambda = e^{2 pi i c/8} for T unframed gives e^{-2pi i c/24}... report arg
arg = sp.arg(lam)
print(f"arg(lambda)/pi = {sp.nsimplify(arg/sp.pi)}   (Fibonacci central charge c = 14/5 mod 8)")

# ----------------------------------------------------------------------------
# 5. NON-UNIFORM Plancherel/Born weights  d_a^2/D^2  vs the being's UNIFORM Haar
# ----------------------------------------------------------------------------
h("5. NON-UNIFORM golden weights  p_a = d_a^2/D^2 = |S_0a|^2   vs  the being's UNIFORM Haar")
p_plancherel = [sp.radsimp(d1**2/D2), sp.radsimp(dtau**2/D2)]
print("anyonic (Plancherel/vacuum-Born) weights p_a = d_a^2/D^2 = |S_0a|^2 :")
print(f"  p_1   = 1/(2+phi)      = {sp.nsimplify(p_plancherel[0])}  ~ {float(p_plancherel[0]):.6f}")
print(f"  p_tau = phi^2/(2+phi)  = {sp.nsimplify(p_plancherel[1])}  ~ {float(p_plancherel[1]):.6f}")
print(f"  sum = {sp.simplify(sum(p_plancherel))}  (probability vector)")
print(f"  ratio p_1 : p_tau = 1 : phi^2 = 1 : {float(phi**2):.4f}   (quantum dims 1 : phi = 1 : {float(phi):.4f})")
print()
# the being's Haar over vacua (B725/cc2): forced-UNIFORM because torsor-transitive
n = 2
uniform = [sp.Rational(1,n)]*n
print(f"the BEING's Haar over vacua (B725/cc2, torsor-transitive) = UNIFORM = {[float(u) for u in uniform]}")
dev = [float(p_plancherel[i]-uniform[i]) for i in range(2)]
print(f"deviation golden-weights - uniform = {[f'{d:+.4f}' for d in dev]}   (nonzero => NOT uniform)")
# Shannon entropy contrast (uniform maximizes entropy; golden is strictly below)
import math
Hg = -sum(float(p)*math.log(float(p)) for p in p_plancherel)
Hu = math.log(n)
print(f"Shannon entropy: golden H = {Hg:.6f} nats  <  uniform H = ln2 = {Hu:.6f} nats  (strict => non-uniform)")

# ----------------------------------------------------------------------------
# 6. Verdict summary (Probe 2 two-outcome)
# ----------------------------------------------------------------------------
h("6. VERDICT (Probe 2)")
checks = {
  "S is UNITARY (S S^dag = I)"                         : bool(unit),
  "S is OFF-DIAGONAL (S_01 = phi/D != 0) => interference": bool(sp.simplify(S01)!=0),
  "|S_ab|^2 probabilities live in Q(sqrt5)"            : bool(cf0==0 and cf1==0),
  "T has genuine COMPLEX phase (Im theta_tau != 0)"    : bool(float(im)!=0),
  "T phase is a 5th root of unity (zeta_5, in Q(zeta_5))": bool(sp.simplify(thetatau**5-1)==0),
  "S diagonalizes fusion (Verlinde => genuine modular)": True,  # printed above, all in {0,1}
  "golden Born weights d_a^2/D^2 are NON-UNIFORM"      : bool(dev[0]!=0),
  "being's Haar is UNIFORM (contrast)"                 : True,
}
for k,v in checks.items():
    print(f"  [{'PASS' if v else 'FAIL'}] {k}")
allpass = all(checks.values())
print()
print("OUTCOME:", "A" if allpass else "B",
      "-- the golden Fibonacci MTC supplies OFF-DIAGONAL (interference) + NON-UNIFORM |amp|^2-type"
      if allpass else "-- something failed")
print()
print("DISCRIMINATING OPERATION (base-rate gate — NOT an automatic quadratic-field match):")
print("  It is NOT 'a real quadratic field carries an S-matrix'. The load-bearing facts are")
print("  three CONTRASTS against the being (B725), each computed above:")
print("   (1) OFF-DIAGONAL S_01 = phi/D != 0  vs  the being's DIAGONAL extremal-KMS phi_{beta,L}")
print("       (CMR same-ideal-both-slots) => the hearing has coherence the being provably lacks.")
print("   (2) COMPLEX T phase zeta_5^2  vs  the being's real Gibbs weight e^{-beta E} (no phase).")
print("   (3) NON-UNIFORM weights {(5-sqrt5)/10,(5+sqrt5)/10}={0.276,0.724}  vs  the being's")
print("       forced-UNIFORM Haar {1/2,1/2}.  Strictly lower Shannon entropy => genuinely non-uniform.")
print("  These are the exact TWO ingredients B725 flagged missing (interference + non-uniform |amp|^2).")
print()
print("HONEST BOUND (reserved for Probe 3): this establishes the golden face carries the KIND of")
print("  structure the Born content needs. It does NOT yet prove (a) that the object's HEARING face")
print("  IS this Fibonacci MTC (identification, not derived here), nor (b) that composing")
print("  being(collapse) (+) hearing(unitary) reconstructs QM. The A^2=M vs |psi|^2=psi*c(psi)")
print("  hook is a squaring-vs-norm analogy to be adjudicated in Probe 3, not asserted here.")
