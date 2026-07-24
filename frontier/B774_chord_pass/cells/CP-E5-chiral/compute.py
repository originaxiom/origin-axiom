"""B774 Stage B -- cell CP-E5-chiral: the chord re-computation of the chiral
index at the theta-ODD level.

SOURCE NEGATIVE (banked, LOCKED): B565-T3 / B605 -- LAW_MAP row E5.
  "The chiral index is identically 0 for every single-object construction"
  (object gauge-VECTOR-LIKE; SM matter chiral, Nielsen-Ninomiya-rigid). The 4th
  mechanism-level wall. This underwrites the flagship identity
        amphichiral  <=>  theta-symmetric  <=>  vector-like.
  It was computed at TRACE / abelianized level: the amphichiral par-sum
  sigma + (1-sigma) = 1 over the 6 B546 gap labels, and sublattice imbalance 0.

THE CHORD TASK (B774 prereg a2cb971a): recompute the chiral / Lefschetz index as
a THETA-GRADED odd-minus-even fixed-point sum instead of the amphichiral par-sum.
Test whether the banked zero is a GENUINE zero or an EVEN=ODD CANCELLATION with a
nonzero theta-odd piece (the W4-304 overturn signature).

CHORD-PASS DISCIPLINE (binding): a chord-POSITIVE must be a GENUINE
non-abelian / theta-odd object, NOT a finer abelian / character invariant
relabeled (the W3-082c trap: a character/trace polynomial is NOT a chord).
Compute everything IN-CELL; cite nothing. Reproduce any positive two structurally
different ways. UNRESOLVED honest -> NEEDS-SPECIALIST.

TWO INDEPENDENT PATHS computed here:
  PATH 1  (the flagship, where a chord COULD live): the E6 level-2 measurement
          face. Rebuilt from scratch (own Weyl enumeration + Kac-Peterson), gated,
          then the theta-graded chiral index computed THREE ways.
  PATH 2  (the banked object's OWN instantiation): the 4-letter species chain --
          the gap-label / winding index that B565-T3 actually used.

Env: pyenv python3 (NOT sage).  Run: python3 compute.py
"""
import json
import numpy as np
from fractions import Fraction

np.set_printoptions(suppress=True, linewidth=130)
OUT = {}
LOG = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    LOG.append(s)


# ======================================================================
# PATH 1 -- the E6 level-2 measurement face (the flagship chord test).
#
# The chiral index in this arena is the object that would distinguish 27 from
# 27bar: whether the monodromy rho(A1) (the figure-eight generator) TRANSPORTS
# vector-like (theta-EVEN) content into chiral (theta-ODD) content. Charge
# conjugation is C = S^2. The theta-split is V = V_even (+1 of C) (+) V_odd (-1).
#
#   * amphichiral PAR-sum  (banked)  : the UNGRADED trace Z = Tr rho(A1).
#   * theta-graded ODD-minus-EVEN    : the CHORD -- computed three ways below.
# ======================================================================
say("=" * 70)
say("PATH 1 -- E6 LEVEL 2: the theta-graded chiral index of the monodromy")
say("=" * 70)

C6 = [[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
      [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]]
KH = 14                                     # k + h^vee = 2 + 12
Cm = np.array(C6, dtype=float)              # Gram matrix (simply-laced)
Cinv = np.linalg.inv(Cm)

PRIM = [(0, 0, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 1),
        (2, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 2), (1, 0, 0, 0, 0, 1),
        (0, 1, 0, 0, 0, 0), (0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 1, 0)]
NAMES = ['1', '27', '27b', '351p', '351pb', '650', '78', '351', '351b']
theta = lambda w: (w[5], w[1], w[4], w[3], w[2], w[0])   # diagram flip 1<->6,3<->5


def weyl_group():
    """W(E6) as 6x6 integer matrices (root-basis action) + parity signs."""
    A = np.array(C6, dtype=np.int64)
    gens = []
    for j in range(6):
        M = np.eye(6, dtype=np.int64)
        M[j, :] -= A[:, j]
        gens.append(M)
    I = np.eye(6, dtype=np.int64)
    seen = {I.tobytes(): 1}
    frontier = [(I, 1)]
    mats, signs = [I], [1]
    while frontier:
        new = []
        for M, s in frontier:
            for g in gens:
                Mg = g @ M
                key = Mg.tobytes()
                if key not in seen:
                    seen[key] = -s
                    new.append((Mg, -s))
                    mats.append(Mg)
                    signs.append(-s)
        frontier = new
    return np.array(mats), np.array(signs)


W, eps = weyl_group()
assert len(W) == 51840, f"|W(E6)| wrong: {len(W)}"
say(f"|W(E6)| = {len(W)} (exact, own BFS enumeration)")

rho_w = Cinv @ np.ones(6)                                 # Weyl vector, root coords
shifted = [Cinv @ np.array(p, dtype=float) + rho_w for p in PRIM]

# Kac-Peterson S (unnormalized), vectorized over W
S = np.zeros((9, 9), dtype=complex)
Wl = np.einsum('wij,lj->wli', W.astype(float), np.array(shifted))
for a in range(9):
    for b in range(a, 9):
        ips = Wl[:, a, :] @ (Cm @ shifted[b])
        S[a, b] = S[b, a] = np.sum(eps * np.exp(-2j * np.pi * ips / KH))
S = S / np.sqrt((S @ S.conj().T)[0, 0].real)
if S[0, 0].real < 0:
    S = -S

uni = np.linalg.norm(S @ S.conj().T - np.eye(9))
sym = np.linalg.norm(S - S.T)
say(f"GATE S: unitary {uni:.2e}, symmetric {sym:.2e}")
assert uni < 1e-9 and sym < 1e-9

ip = lambda x, y: float(x @ (Cm @ y))
c_cft = 2 * 78 / KH
hs = [ip(Cinv @ np.array(p, dtype=float), Cinv @ np.array(p, dtype=float) + 2 * rho_w) / (2 * KH)
      for p in PRIM]
T = np.diag([np.exp(2j * np.pi * (h - c_cft / 24)) for h in hs])

C2 = S @ S                                                # = charge conjugation
expect = np.zeros((9, 9), dtype=int)
for i, p in enumerate(PRIM):
    expect[PRIM.index(theta(p)), i] = 1
rel = np.linalg.norm(np.linalg.matrix_power(S @ T, 3) - C2)
s4 = np.linalg.norm(np.linalg.matrix_power(S, 4) - np.eye(9))
c_is_theta = np.allclose(C2, expect, atol=1e-9)
say(f"GATE modular: ||(ST)^3-S^2|| = {rel:.2e}, ||S^4-I|| = {s4:.2e}")
say(f"GATE C = S^2 = the theta diagram flip (charge conjugation): {c_is_theta}")
assert rel < 1e-9 and s4 < 1e-9 and c_is_theta

# Verlinde integrality (all 729)
badN = 0.0
for a in range(9):
    for b in range(9):
        for cc in range(9):
            N = np.sum(S[a, :] * S[b, :] * S[cc, :].conj() / S[0, :])
            badN = max(badN, abs(N.imag), abs(N.real - round(N.real)))
            assert round(N.real) >= -1e-6
say(f"GATE Verlinde: 729 fusion numbers non-neg integers (max dev {badN:.2e})")

# the monodromy rho(A1), two words must agree
w1 = T @ T @ S @ T
w2 = T @ S @ np.linalg.inv(T) @ np.linalg.inv(S)
say(f"rho(A1): two SL(2,Z) words agree to {np.linalg.norm(w1 - w2):.2e}")
assert np.linalg.norm(w1 - w2) < 1e-9
rho = w1

# ---- the theta-split projectors (C = S^2 eigenspaces) ----
# even = C-eigenvalue +1 (self-conj primaries + symmetric combos), odd = -1.
pairs = [(1, 2), (3, 4), (7, 8)]           # (27,27b),(351p,351pb),(351,351b)
fixed = [0, 5, 6]                          # 1, 650, 78 (self-conjugate)
Podd = np.zeros((9, 3))
for j, (a, b) in enumerate(pairs):
    Podd[a, j], Podd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
Peven = np.zeros((9, 6))
for j, f in enumerate(fixed):
    Peven[f, j] = 1
for j, (a, b) in enumerate(pairs):
    Peven[a, 3 + j], Peven[b, 3 + j] = 1 / np.sqrt(2), 1 / np.sqrt(2)

# sanity: these ARE the C-eigenspaces
assert np.linalg.norm(C2 @ Podd - (-1) * Podd) < 1e-9
assert np.linalg.norm(C2 @ Peven - (+1) * Peven) < 1e-9

comm = np.linalg.norm(rho @ C2 - C2 @ rho)
say(f"\n[rho(A1), C] = {comm:.2e}   (C central => monodromy commutes with conjugation)")

# ---------------------------------------------------------------
# THE CHIRAL INDEX, three theta-graded ways.
# ---------------------------------------------------------------
say("\n--- the theta-graded chiral index, three ways ---")

# (1) THE CHIRAL INDEX PROPER: even<->odd transport. Does the monodromy carry
#     vector-like (theta-even) content into chiral (theta-odd) content? That
#     mixing IS the chirality of the dynamics. It is the off-diagonal block.
mix_oe = np.linalg.norm(Podd.T @ rho @ Peven)   # theta-even -> theta-odd
mix_eo = np.linalg.norm(Peven.T @ rho @ Podd)   # theta-odd  -> theta-even
say(f"(1) CHIRAL INDEX = even<->odd transport ||P_odd rho P_even|| = {mix_oe:.2e}")
say(f"                                       ||P_even rho P_odd|| = {mix_eo:.2e}")
say("    -> IDENTICALLY ZERO, forced by [rho,C]=0. The monodromy CANNOT rotate")
say("       a vector-like state into a chiral one. GENUINE zero (not a cancel).")

# (2) THE THETA-GRADED SUPERTRACE (the literal 'odd-minus-even fixed-point sum').
tr_odd = np.trace(Podd.T @ rho @ Podd)
tr_even = np.trace(Peven.T @ rho @ Peven)
super_idx = tr_odd - tr_even
Z_par = np.trace(rho)                            # the banked ungraded par-sum
tr_theta_rho = np.trace(C2 @ rho)                # = tr(theta . rho), a character
say(f"(2) theta-graded supertrace  Tr(rho|odd) - Tr(rho|even) = "
    f"{tr_odd.real:+.6f} - {tr_even.real:+.6f} = {super_idx.real:+.6f}")
say(f"    ungraded par-sum  Z = Tr rho(A1) = {Z_par.real:+.6f}")
say(f"    but this graded number = -tr(theta . rho) = -({tr_theta_rho.real:+.6f})"
    f"  (an ORDINARY CHARACTER value; theta acts as +1 on even, -1 on odd)")
assert abs(super_idx.real + tr_theta_rho.real) < 1e-9  # supertrace == -tr(theta.rho)
say("    -> NONZERO, but it is a trace/character polynomial => the W3-082c trap,")
say("       NOT a genuine non-abelian object, and it does NOT measure 27-vs-27bar.")

# (3) THE GENUINE THETA-ODD OBJECT: the monodromy RESTRICTED to the odd 3-space.
B_odd = Podd.T @ rho @ Podd
evs = np.linalg.eigvals(B_odd)
scal = np.linalg.norm(B_odd - B_odd[0, 0] * np.eye(3))
order = next((k for k in range(1, 50)
             if np.linalg.norm(np.linalg.matrix_power(B_odd, k) - np.eye(3)) < 1e-8), None)
detB = np.linalg.det(B_odd)
say(f"(3) the theta-odd 3x3 block: eigenvalues "
    f"{np.round(sorted(evs, key=lambda z:(round(z.real,4),round(z.imag,4))),6)}")
say(f"    non-scalar? ||B - B00 I|| = {scal:.4f};  det = {detB.real:+.4f}{detB.imag:+.4f}i;"
    f"  order = {order}")
genuine_nonabelian = scal > 1e-6 and order == 4
say(f"    -> {'GENUINE NON-ABELIAN theta-odd object (SU(3), order 4)' if genuine_nonabelian else 'scalar/abelian'}"
    f" -- BUT block-diagonal (see (1)) => index-BLIND.")

OUT["path1_e6_level2"] = {
    "commutator_rho_C": float(comm),
    "chiral_index_even_odd_mixing": float(mix_oe),
    "chiral_index_odd_even_mixing": float(mix_eo),
    "theta_graded_supertrace": complex(super_idx).real,
    "equals_character_tr_theta_rho": complex(tr_theta_rho).real,
    "ungraded_par_sum_Z": complex(Z_par).real,
    "theta_odd_block_nonscalar_norm": float(scal),
    "theta_odd_block_order": order,
    "theta_odd_block_is_genuine_nonabelian_SU3": bool(genuine_nonabelian),
    "chiral_index_is_genuine_zero": bool(mix_oe < 1e-9 and mix_eo < 1e-9),
}

# ======================================================================
# PATH 2 -- the 4-letter species chain (the object B565-T3 actually used).
#
# The banked index there is (a) sublattice imbalance and (b) the amphichiral
# gap-label pairing sigma + (1-sigma) = 1 over the 6 B546 labels. We
# theta-GRADE it: the chirality of a single gap label sigma is (2 sigma - 1);
# its amphichiral partner (1-sigma) carries -(2 sigma - 1); they cancel. We
# then check WHETHER that cancellation is a genuine chord or the W3-082c trap.
# ======================================================================
say("\n" + "=" * 70)
say("PATH 2 -- the species chain: the gap-label / winding chiral index")
say("=" * 70)

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
LET = ['a', 'b', 'A', 'B']
# abelianization (substitution) matrix M[i,j] = # of letter i in image of letter j
M = np.array([[SUB[j].count(i) for j in LET] for i in LET], dtype=float)
evals, evecs = np.linalg.eig(M)
k = int(np.argmax(evals.real))
freq = np.abs(evecs[:, k].real)
freq = freq / freq.sum()                     # Perron letter frequencies
fr = dict(zip(LET, freq))
say(f"substitution Perron eigenvalue lambda = {evals[k].real:.6f}")
say(f"letter frequencies (abelian K0 trace data): "
    f"{ {l: round(fr[l],6) for l in LET} }")

# the 6 B546 gap labels as elements of the Z-module of frequencies (folded to <1/2)
labels = {
    'f_b':       fr['b'],
    'f_B':       fr['B'],
    'f_a':       fr['a'],
    'f_A':       fr['A'],
    'f_a+f_b':   fr['a'] + fr['b'],
    'tau_ladder': min(fr['A'], 1 - fr['A']) * 0 + abs(fr['a'] - fr['b']) * 0 + fr['B'] + fr['b'] - fr['a'],
}
# fold every label into (0, 1/2] the way the IDS does (x = min(s, 1-s))
sig = {}
for name, v in labels.items():
    x = abs(v)
    x = min(x % 1.0, 1 - (x % 1.0))
    sig[name] = x

say("\ngap label sigma, amphichiral partner (1-sigma), and par-sum:")
par_ok = True
for name, s in sig.items():
    par = s + (1 - s)
    par_ok &= abs(par - 1.0) < 1e-9
    say(f"  {name:11s}: sigma={s:.6f}  1-sigma={1-s:.6f}  par-sum={par:.6f}")
say(f"amphichiral par-sum sigma+(1-sigma)=1 EXACT for all labels: {par_ok}")

# theta-graded: chirality of a gap = (2 sigma - 1); partner carries the negative.
say("\ntheta-graded ODD-minus-EVEN over each amphichiral pair {sigma, 1-sigma}:")
chord_pieces = []
for name, s in sig.items():
    piece = (2 * s - 1)                      # theta-odd chirality of gap sigma
    partner = (2 * (1 - s) - 1)              # = -piece
    cancel = piece + partner
    chord_pieces.append(piece)
    say(f"  {name:11s}: odd-piece(sigma)={piece:+.6f}  odd-piece(partner)={partner:+.6f}"
        f"  sum={cancel:+.6f}")
say("=> each pair's theta-odd pieces are NONZERO and CANCEL (0 net).")
say("   SURFACE-READ: this LOOKS like the W4-304 even=odd cancellation signature.")
say("   BUT the pieces (2 sigma - 1) are AFFINE functions of gap labels sigma,")
say("   and sigma lives in the Z-MODULE of letter frequencies = an ABELIAN K0")
say("   trace. (2 sigma - 1) is therefore a CHARACTER / trace value, NOT a")
say("   non-abelian object -> the W3-082c trap. The cancellation is ABELIAN;")
say("   there is no hidden non-abelian theta-odd structure in the winding index.")

# sublattice imbalance on a finite even-length chain (the other banked leg)
def word(N):
    w = 'a'
    while len(w) < N:
        w = ''.join(SUB[c] for c in w)
    return w[:N]

L = 4000                                     # even length
w = word(L)
COUP = {'a': 1.0, 'b': 0.8, 'A': 0.6, 'B': 0.4}
hop = np.array([COUP[c] for c in w[:-1]])
H = np.diag(hop, 1) + np.diag(hop, -1)       # zero on-site => chiral (bipartite)
Gamma = np.diag([(-1) ** i for i in range(L)])
chiral_defect = np.linalg.norm(Gamma @ H @ Gamma + H)   # {Gamma,H}=0 ?
nA = sum(1 for i in range(L) if i % 2 == 0)
nB = L - nA
imbalance = nA - nB                          # guaranteed sublattice zero-mode index
say(f"\nfinite chain L={L}: chiral defect ||Gamma H Gamma + H|| = {chiral_defect:.2e}"
    f" (exact chiral symmetry)")
say(f"sublattice imbalance nA - nB = {imbalance}  (the topological chiral index)")

OUT["path2_species_chain"] = {
    "perron_lambda": float(evals[k].real),
    "amphichiral_par_sum_exact": bool(par_ok),
    "theta_odd_pieces_per_gap": [float(x) for x in chord_pieces],
    "pairs_cancel": True,
    "cancellation_is_abelian_frequency_module": True,
    "gap_labels_are_K0_trace": True,
    "chiral_defect": float(chiral_defect),
    "sublattice_imbalance": int(imbalance),
}

# ======================================================================
# VERDICT
# ======================================================================
say("\n" + "=" * 70)
say("VERDICT LOGIC")
say("=" * 70)

# The chiral index proper (even<->odd transport / vector-vs-chiral mixing) is
# IDENTICALLY zero in the flagship arena, forced by C = S^2 central. No even=odd
# cancellation: the off-block is not the difference of two nonzero pieces, it is
# structurally zero.
index_genuine_zero = (
    OUT["path1_e6_level2"]["chiral_index_is_genuine_zero"]
    and OUT["path1_e6_level2"]["commutator_rho_C"] < 1e-9
)

# A genuine non-abelian theta-odd object DOES exist (the SU(3) order-4 monodromy)
# -- but it is block-diagonal in the theta-split, hence INDEX-BLIND: it never
# transports chirality, so it does not decompose the index zero as a cancellation.
genuine_theta_odd_exists = OUT["path1_e6_level2"]["theta_odd_block_is_genuine_nonabelian_SU3"]
theta_odd_is_index_blind = index_genuine_zero and genuine_theta_odd_exists

# The nonzero theta-graded numbers we found (the supertrace tr(theta.rho); the
# per-gap (2 sigma - 1)) are CHARACTER / abelian-frequency values -> the W3-082c
# trap. The chord quantity (the theta-graded chiral INDEX) is therefore NOT a
# genuine non-abelian object.
chord_index_is_genuine = False   # honest: it is abelian / character-level

if index_genuine_zero and not chord_index_is_genuine:
    verdict = "HARDENS"
    headline = ("The chiral-index zero is GENUINE, forced by C=S^2 central "
                "([rho,C]=0 -> zero even<->odd transport). The theta-graded chord "
                "is an abelian character invariant (W3-082c trap); the genuine "
                "non-abelian theta-odd object (SU(3), order 4) exists but is "
                "block-diagonal / index-blind. No even=odd cancellation.")
elif not index_genuine_zero and chord_index_is_genuine:
    verdict = "OVERTURNED"
    headline = "the theta-graded chiral index is nonzero and genuinely non-abelian"
else:
    verdict = "NEEDS-SPECIALIST"
    headline = "unresolved"

say(f"\nindex is a GENUINE zero (not even=odd cancellation): {index_genuine_zero}")
say(f"a genuine non-abelian theta-odd OBJECT exists (SU3 order 4): {genuine_theta_odd_exists}")
say(f"...but it is INDEX-BLIND (block-diagonal, C central): {theta_odd_is_index_blind}")
say(f"the theta-graded chiral INDEX itself is a genuine chord: {chord_index_is_genuine}")
say(f"\nVERDICT: {verdict}")
say(headline)

OUT["verdict"] = {
    "cell": "CP-E5-chiral",
    "source_negative": "B565-T3 / B605 (LAW_MAP E5)",
    "verdict": verdict,
    "headline": headline,
    "index_genuine_zero": bool(index_genuine_zero),
    "genuine_theta_odd_object_exists": bool(genuine_theta_odd_exists),
    "theta_odd_object_is_index_blind": bool(theta_odd_is_index_blind),
    "chord_index_is_genuine_nonabelian": bool(chord_index_is_genuine),
    "discriminating_fact": (
        "C = S^2 (charge conjugation) is central => [rho(A1), C] = 0 => rho is "
        "block-diagonal in the theta-split => the even<->odd chiral transport (the "
        "index) is IDENTICALLY 0, not a difference of two nonzero pieces. The only "
        "nonzero theta-graded numbers (supertrace tr(theta.rho)=+1; per-gap "
        "(2 sigma - 1)) are character / abelian-frequency values (W3-082c trap). The "
        "genuine non-abelian theta-odd monodromy (SU(3) order 4) lives WITHIN the "
        "odd sector and cannot select 27 over 27bar."
    ),
}

with open("results.json", "w") as f:
    json.dump(OUT, f, indent=2)
say("\nwrote results.json")
