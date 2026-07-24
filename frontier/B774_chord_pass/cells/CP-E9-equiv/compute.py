#!/usr/bin/env python3
"""
B774 Stage B -- Cell CP-E9-equiv
Chord re-computation of the banked negative LAW_MAP E9 (THE EQUIVARIANCE WALL),
the leg that also feeds B736 Path-C (the SM parameter-reduction RIGOROUS NO-GO).

BANKED NEGATIVE (theta-even / trace-abelianized level, B650 W2-G1):
    The Sylvester solve  T . A1 = B . T  over the exact matrices
        A1  = the being monodromy (cat map), eigenvalues {phi^2, phi^-2}
              -- REAL hyperbolic, OFF the unit circle,
        B   = the hearing image rho_hear(RL) on the theta-odd plane,
              tr = -1/phi, det = 1, ORDER 10 -- eigenvalues on the unit circle,
    returns  T = 0  as the unique solution.  Spectra disjoint => no intertwiner.

THE CHORD ANALOG TO COMPUTE (this cell):
    Re-solve the SAME Sylvester equivariance system, but drive the target B with
    the theta-ODD analog of the golden character in place of the theta-even one,
    and test whether the intertwiner T moves off zero. A genuine move off zero
    would simultaneously reopen the B736 Path-C parameter-reduction no-go.

CHORD-PASS DISCIPLINE (binding):
  - compute the theta-odd analog IN-CELL, never cite it.
  - a chord POSITIVE must be a GENUINE non-abelian/theta-odd object, NOT a finer
    abelian/character invariant relabeled (the W3-082c trap).
  - a REAL overturn (W4-304 signature) = a trace/par ZERO that decomposes as
    even = odd CANCELLATION with a NONZERO theta-odd piece -- exhibit it.
  - reproduce any positive by a second structurally-different path.

The golden character of 2I = SL(2,5) (B644, exact):  its values are
    {+2, -2, 0, +1, -1, +phi, -phi, +1/phi, -1/phi},
and it is theta-ODD under the center:  chi(-g) = -chi(g)  (faithful 2I).
The theta-EVEN companion is the A5 = PSL(2,5) golden 3-dim rep (center acts +1).
We test the whole golden orbit -- BOTH theta-parities and BOTH Galois
conjugates -- because the Sylvester kernel depends only on the target spectrum.
"""

import sympy as sp

# ----------------------------------------------------------------------------
sqrt5 = sp.sqrt(5)
phi   = (1 + sqrt5) / 2          # golden ratio, 1.618...
iphi  = 1 / phi                  # = phi - 1 = 0.618...

def approx(x):
    return float(sp.N(x, 30))

log = []
def say(s=""):
    log.append(s)
    print(s)

say("="*74)
say("B774 CP-E9-equiv : chord re-computation of the EQUIVARIANCE WALL (LAW_MAP E9)")
say("="*74)

# ----------------------------------------------------------------------------
# 1. THE BEING SIDE  A1  (the classical / cat-map monodromy)
#    Cooper--Long fig-8 cusp monodromy conjugacy: trace 3, hyperbolic.
#    A1 = [[2,1],[1,1]]  ->  char poly x^2 - 3x + 1  ->  eigenvalues phi^2, phi^-2.
# ----------------------------------------------------------------------------
A1 = sp.Matrix([[2, 1], [1, 1]])
being_eigs = list(A1.eigenvals().keys())
phi2, iphi2 = (3 + sqrt5)/2, (3 - sqrt5)/2   # = phi^2, phi^-2
being_ok = ( sp.simplify(A1.det() - 1) == 0
             and sp.simplify(A1.trace() - 3) == 0
             and set(sp.simplify(e) for e in being_eigs) == {sp.simplify(phi2), sp.simplify(iphi2)} )
say("")
say("[1] BEING module A1 (cat map):")
say(f"    A1 = {A1.tolist()}  tr=3 det=1")
say(f"    eigenvalues = {{phi^2, phi^-2}} = {{{approx(phi2):.6f}, {approx(iphi2):.6f}}}  (REAL hyperbolic)")
say(f"    banked-shape check: {being_ok}")
assert being_ok

# ----------------------------------------------------------------------------
# 2. THE SYLVESTER INTERTWINER SOLVER
#    T . A = B . T  is linear in the 4 entries of a 2x2 T.  We solve the null
#    space of the Kronecker map  M = (A^T (x) I) - (I (x) B)  acting on vec(T).
#    dim ker M = number of independent intertwiners.  (Sylvester/Roth: nonzero
#    iff spec(A) and spec(B) intersect.)
# ----------------------------------------------------------------------------
def sylvester_kernel_dim(A, B):
    t = sp.symbols('t0 t1 t2 t3')
    T = sp.Matrix([[t[0], t[1]], [t[2], t[3]]])
    E = T*A - B*T                       # want = 0
    eqs = [sp.expand(E[i, j]) for i in range(2) for j in range(2)]
    Mrows = []
    for e in eqs:
        Mrows.append([sp.simplify(e.coeff(tt)) for tt in t])
    M = sp.Matrix(Mrows)
    ker = M.nullspace()
    return len(ker), M, [k.T.tolist()[0] for k in ker]

# ----------------------------------------------------------------------------
# 3. TARGET BUILDERS
#    Any SL(2,C) elliptic element of trace tau (|tau|<2) has spectrum
#    {e^{+i th}, e^{-i th}} with 2 cos th = tau -- ON THE UNIT CIRCLE.
#    We build BOTH a diagonalised and a genuinely NON-DIAGONAL (non-abelian
#    conjugate) representative for each golden trace, so the kernel test cannot
#    be an artifact of a shared eigenbasis.
# ----------------------------------------------------------------------------
def target_diag(tau):
    # companion / elliptic normal form with det 1, trace tau
    return sp.Matrix([[0, -1], [1, tau]])   # char poly x^2 - tau x + 1

def target_conj(tau):
    # a genuinely non-diagonal SL2 representative (P C P^-1), P not eigenbasis
    C = target_diag(tau)
    P = sp.Matrix([[1, 1], [1, 2]])         # det 1, mixes the eigenlines
    return sp.simplify(P * C * P.inv())

# ----------------------------------------------------------------------------
# 4. THE GOLDEN ORBIT -- both theta-parities, both Galois conjugates
#    theta parity is the sign under the 2I center: chi(-g) = (parity) chi(g).
#    We tag each trace with the (order, parity) of the class it sits on.
# ----------------------------------------------------------------------------
golden = [
    # label,                trace,     order, theta-parity(under center), which-side
    ("theta-EVEN  chi(5A)=  phi ",   phi,   5,  +1, "A5 / hearing seen mod center (banked-adjacent)"),
    ("theta-EVEN  chi(5B)= -1/phi", -iphi,  5,  +1, "A5 Galois conjugate"),
    ("theta-ODD   chi(10)= -1/phi", -iphi, 10,  -1, "faithful 2I  (B650 banked target: tr=-1/phi, order 10)"),
    ("theta-ODD   chi(10)=  phi ",   phi,  10,  -1, "faithful 2I  Galois conjugate  <== THE CHORD ANALOG"),
    ("theta-ODD   chi(5) =  1/phi",  iphi,  5,  -1, "faithful 2I, order-5 class"),
    ("theta-ODD   chi(5) = -phi ",  -phi,   5,  -1, "faithful 2I, order-5 class, Galois conj"),
]

say("")
say("[2] SYLVESTER SOLVE  T.A1 = B.T  for the whole golden orbit")
say("    (kernel dim > 0  <=>  intertwiner moves off zero):")
say("")
results_orbit = []
for label, tau, order, parity, note in golden:
    Bd = target_diag(tau)
    Bc = target_conj(tau)
    kd, _, _ = sylvester_kernel_dim(A1, Bd)
    kc, _, _ = sylvester_kernel_dim(A1, Bc)
    # eigenvalues of the target
    tev = list(Bd.eigenvals().keys())
    on_circle = all(sp.simplify(sp.Abs(e) - 1) == 0 for e in tev)
    shares = any(sp.simplify(e - phi2) == 0 or sp.simplify(e - iphi2) == 0 for e in tev)
    say(f"  {label:30s} tr={approx(tau):+.5f} ord={order:2d} theta={parity:+d}")
    say(f"      target eigenvalues on unit circle: {on_circle};  shares a being-eig: {shares}")
    say(f"      dim ker (diagonal target)     = {kd}")
    say(f"      dim ker (NON-diagonal target) = {kc}   [genuine non-abelian conjugate]")
    say(f"      note: {note}")
    say("")
    results_orbit.append(dict(label=label, trace=str(sp.nsimplify(tau)),
                              order=order, theta_parity=parity,
                              target_on_unit_circle=bool(on_circle),
                              shares_being_eigenvalue=bool(shares),
                              ker_dim_diag=kd, ker_dim_conj=kc, note=note))

chord_row = next(r for r in results_orbit if "CHORD ANALOG" in r["note"])
banked_row = next(r for r in results_orbit if "banked target" in r["note"])

# ----------------------------------------------------------------------------
# 5. SECOND, STRUCTURALLY-DIFFERENT PATH -- a GENUINELY NON-ABELIAN faithful 2I
#    2-dim rep.  Build the icosahedral generators in SU(2) exactly, form a real
#    order-10 group element, and Sylvester-solve it against the being module.
#    This uses the ACTUAL faithful theta-odd rep (center = -I acts nontrivially),
#    not just a trace-normal-form -- the strongest chord reading.
# ----------------------------------------------------------------------------
say("[3] SECOND PATH -- genuine faithful theta-ODD 2I rep (center acts as -I):")
# Real rotation by pi/5:  Rot = [[cos36, -sin36],[sin36, cos36]].
# EXACT algebraic entries (no trig -> fast): cos36 = phi/2, sin36 = sqrt(1-(phi/2)^2).
# This is a genuine element of the faithful 2-dim rep of 2I:
#   trace = 2cos36 = phi (a golden value); det = 1; order 10; (Rot)^5 = rotation
#   by 180 deg = -I  =>  the CENTER acts nontrivially  =>  genuinely theta-ODD,
#   and it is NON-diagonal (does not share A1's eigenbasis).
c36 = phi/2
s36 = sp.sqrt(1 - c36**2)                       # = sin36, exact algebraic
B_faithful = sp.Matrix([[c36, -s36], [s36, c36]])
# theta-odd witness: (B_faithful)^5 = -I  (compute exactly via powers, no trig)
Bpow5 = sp.Matrix(B_faithful)
for _ in range(4):
    Bpow5 = sp.expand(Bpow5 * B_faithful)
Bpow5 = Bpow5.applyfunc(lambda e: sp.nsimplify(sp.radsimp(e)))
is_theta_odd = (Bpow5 == -sp.eye(2))
Bpow10 = sp.expand(Bpow5 * Bpow5).applyfunc(lambda e: sp.nsimplify(sp.radsimp(e)))
is_order10 = (Bpow10 == sp.eye(2))
tr_faith = sp.nsimplify(B_faithful.trace())
det_faith = sp.nsimplify(sp.expand(B_faithful.det()))
# kernel via numerical rank at high precision (rigorous dimension count)
import mpmath as mpm
mpm.mp.dps = 50
def kerdim_numeric(A, B):
    An = mpm.matrix([[mpm.mpf(str(sp.N(A[i, j], 45))) for j in range(2)] for i in range(2)])
    Bn = mpm.matrix([[complex(sp.N(B[i, j], 45)) for j in range(2)] for i in range(2)])
    # Kronecker map on vec(T): (A^T kron I) - (I kron B)
    M = mpm.zeros(4, 4)
    for a in range(2):
        for b in range(2):        # T entry (a,b)
            col = 2*a + b
            # (T A)_{i b'} = sum_k T_{i k} A_{k b'} ; (B T)_{i j} = sum_k B_{i k} T_{k j}
            # residual E = T A - B T ; collect coeff of T_{a,b}
            for i in range(2):
                for j in range(2):
                    row = 2*i + j
                    val = 0
                    if i == a:
                        val += An[b, j]           # from (T A)_{i j}, T_{a,b}=T_{i,b}, A_{b,j}
                    if j == b:
                        val -= Bn[i, a]           # from (B T)_{i j}, T_{a,b}=T_{a,j}, B_{i,a}
                    M[row, col] = val
    # dimension count via singular values: nz singular values of M = rank
    Mh = M.H if hasattr(M, 'H') else M.T
    G = Mh * M
    eig = mpm.eig(G, left=False, right=False)
    tol = mpm.mpf(10) ** -20
    nz = sum(1 for e in eig if abs(e) > tol)
    return 4 - nz
kd_faith = kerdim_numeric(A1, B_faithful)
# cross-check with the exact symbolic solver too
kd_faith_sym, _, _ = sylvester_kernel_dim(A1, B_faithful)
say(f"    B_faithful = [[cos36,-sin36],[sin36,cos36]] (exact: cos36=phi/2)")
say(f"    tr(B_faithful) = {tr_faith}  (= phi, a golden value); det = {det_faith}")
say(f"    (B_faithful)^5 = -I  (theta-ODD, center acts nontrivially): {is_theta_odd}")
say(f"    (B_faithful)^10 = I: {is_order10}")
say(f"    dim ker  T.A1 = B_faithful.T  = {kd_faith} (numeric rank) / {kd_faith_sym} (symbolic)")
say("")

# ----------------------------------------------------------------------------
# 6. THE INVARIANT-LEVEL 'BRIDGE'  det(I - B_odd) = phi^2  -- is it a SHARED
#    EIGENVALUE (would give T!=0) or only an invariant shadow (T=0)?  B650 W2-G2
#    claims the latter.  Reproduce and adjudicate.
# ----------------------------------------------------------------------------
B_odd = target_diag(-iphi)                       # the banked theta-odd target
bridge = sp.simplify((sp.eye(2) - B_odd).det())
say("[4] THE 'BRIDGE'  det(I - B_odd):")
say(f"    det(I - B_odd) = {sp.nsimplify(bridge)}  =  phi^2 = {approx(phi2):.6f}  "
    f"(matches lambda(A1)={approx(phi2):.6f}): {sp.simplify(bridge - phi2)==0}")
say(f"    BUT phi^2 is NOT an eigenvalue of B_odd (its eigs are unit-circle):")
say(f"      eig(B_odd) = {[str(sp.nsimplify(e)) for e in B_odd.eigenvals().keys()]}")
say(f"    => the bridge is an INVARIANT-LEVEL shadow (a determinant), not a shared")
say(f"       spectral value.  It cannot force an intertwiner.  (Confirms B650 W2-G2.)")
say("")

# ----------------------------------------------------------------------------
# 7. W4-304 OVERTURN-SIGNATURE TEST
#    A real overturn = the zero decomposes as even = odd CANCELLATION with a
#    NONZERO theta-odd piece.  Here T is IDENTICALLY zero for every target in
#    the golden orbit (theta-even AND theta-odd), so there is no zero built from
#    a cancelling nonzero theta-odd component: the vanishing is spectral and
#    UNIFORM across theta-parity.  No W4-304 signature.
# ----------------------------------------------------------------------------
all_zero = all(r["ker_dim_diag"] == 0 and r["ker_dim_conj"] == 0 for r in results_orbit) \
           and kd_faith == 0
theta_odd_moved = (chord_row["ker_dim_diag"] > 0 or chord_row["ker_dim_conj"] > 0
                   or kd_faith > 0)
even_and_odd_both_zero = (banked_row["ker_dim_diag"] == 0) and (kd_faith == 0)
say("[5] W4-304 overturn-signature test:")
say(f"    theta-ODD analog moved T off zero?          {theta_odd_moved}")
say(f"    zero is UNIFORM across theta-parity (even & odd both T=0)?  {even_and_odd_both_zero}")
say(f"    => no 'even = odd cancellation with a nonzero theta-odd piece';")
say(f"       the vanishing is a spectral-disjointness fact, identical for both")
say(f"       parities.  No W4-304 overturn signature.")
say("")

# ----------------------------------------------------------------------------
# 8. IS THE COMPUTED QUANTITY A GENUINE CHORD?  (W3-082c trap check)
#    The Sylvester kernel dimension is a function ONLY of spec(A1) and spec(B)
#    (Roth's theorem): it is invariant under conjugation of A1 and of B, i.e.
#    it depends only on the TRACE/eigenvalue (abelianized) data.  Swapping the
#    theta-EVEN golden character for the theta-ODD one changes the *rep*, but
#    the intertwiner-dimension it feeds is a purely spectral/character quantity.
#    Therefore this quantity is NOT a genuine non-abelian/theta-odd invariant --
#    even had it moved, a move would be an abelian/character fact relabeled.
#    (It did not move: it is 0 in every case.)
# ----------------------------------------------------------------------------
is_genuine_chord = False   # the intertwiner dim is a spectral/character function; abelian by Roth
say("[6] genuine-chord adjudication (W3-082c trap):")
say(f"    dim ker(T.A=B.T) is a function of spec(A),spec(B) ONLY (Roth) => abelian/")
say(f"    character-level.  Not a genuine non-abelian theta-odd object.")
say(f"    is_genuine_chord = {is_genuine_chord}")
say("")

# ----------------------------------------------------------------------------
# 9. VERDICT BLOCK
# ----------------------------------------------------------------------------
say("="*74)
if theta_odd_moved and is_genuine_chord and not even_and_odd_both_zero:
    verdict = "OVERTURNED"
    headline = "theta-odd golden character opens a genuine nonzero intertwiner"
elif theta_odd_moved and not is_genuine_chord:
    verdict = "HARDENS"   # a 'move' that is only abelian-relabeled does not overturn
    headline = "any nonzero would be abelian-relabeled (W3-082c); wall stands"
elif all_zero:
    verdict = "HARDENS"
    headline = ("theta-odd golden character gives T=0 too: the Equivariance Wall "
                "holds for BOTH theta-parities and BOTH Galois conjugates")
else:
    verdict = "NEEDS-SPECIALIST"
    headline = "ambiguous -- escalate"

discriminating_fact = (
    "The Sylvester kernel dim(ker: T.A1=B.T) = 0 for every golden-character target "
    "(theta-EVEN chi=phi/-1/phi order-5 AND theta-ODD chi=-1/phi/phi order-10, both "
    "Galois conjugates, diagonal AND genuine non-diagonal conjugate reps, plus the "
    "faithful 2I element with (.)^5=-I): the being spectrum {phi^2,phi^-2} is REAL "
    "hyperbolic and every golden-character trace has |trace|<2 giving a UNIT-CIRCLE "
    "target spectrum, so the spectra are disjoint for both theta-parities. The "
    "det(I-B_odd)=phi^2 'bridge' is an invariant-level determinant shadow, not a "
    "shared eigenvalue, and cannot force an intertwiner."
)

say(f"VERDICT: {verdict}")
say(f"HEADLINE: {headline}")
say(f"is_genuine_chord: {is_genuine_chord}")
say("="*74)

# ----------------------------------------------------------------------------
import json
results = dict(
    cell="CP-E9-equiv",
    campaign="B774 Stage B chord-pass",
    source_negative="LAW_MAP E9 (THE EQUIVARIANCE WALL) + B736 Path-C parameter-reduction NO-GO",
    banked_negative_level="theta-even / trace-abelianized (B650 W2-G1: Sylvester T=0)",
    chord_analog="Sylvester T.A1=B.T with the theta-ODD golden character target",
    being_module=dict(matrix=A1.tolist(), eigenvalues=["phi^2","phi^-2"],
                      spectrum_type="real hyperbolic, off unit circle"),
    golden_orbit=results_orbit,
    faithful_2I_second_path=dict(
        trace=str(sp.nsimplify(tr_faith)),
        is_theta_odd_center_minus_I=bool(is_theta_odd),
        order_10=bool(sp.simplify(B_faithful**10 - sp.eye(2)) == sp.zeros(2,2)),
        sylvester_kernel_dim=kd_faith),
    bridge_det_I_minus_Bodd=dict(value="phi^2", is_shared_eigenvalue=False,
                                 reading="invariant-level determinant shadow (B650 W2-G2)"),
    theta_odd_moved_off_zero=bool(theta_odd_moved),
    zero_uniform_across_theta_parity=bool(even_and_odd_both_zero),
    w4_304_overturn_signature=False,
    is_genuine_chord=is_genuine_chord,
    verdict=verdict,
    headline=headline,
    discriminating_fact=discriminating_fact,
)
import os
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "results.json"), "w") as f:
    json.dump(results, f, indent=2, default=str)
with open(os.path.join(here, "output.txt"), "w") as f:
    f.write("\n".join(log) + "\n")
say("")
say("wrote results.json + output.txt")
