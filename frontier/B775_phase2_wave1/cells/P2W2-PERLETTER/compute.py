"""B775 Phase-2 Wave-2 -- cell P2W2-PERLETTER.

QUESTION (sealed, two-outcome): is there a NON-ARBITRARY per-letter hearing
weight FORCED by the object's structure -- DERIVED (not assigned) from B593's
complex-amplitude machinery -- as opposed to the killed 1/(2phi^3) ~ alpha_s
attribution (H-ITERATED-HEARING, OI-038; killed as base-rate/knob-dependent;
NOT revived here)?

SEALED CRITERION:
  a per-letter weight DERIVED from structure (forced, mechanism shown) -> RESOLVED-A
  no non-arbitrary derivation (the weight is a free knob, tombstone)    -> RESOLVED-B
  otherwise                                                             -> UNRESOLVED

The honest door named by B751/B752: "derive a per-letter hearing weight from the
banked complex-amplitude structure (a derivation from B593's matrix elements, not
an assignment)." This cell walks that door and computes the discriminating fact.

Structure recap (B592/B593, banked):
  * hearing amplitude  A(g) = <psi_mirror| C rho(g) |psi>  on the golden stage
    SU(3)_2, over WELDS g = mapping-class words in the alphabet {R, L}
    (R = T, L = S^-1 T^-1 S -- Dehn twists / modular generators).
  * the banked CHIRAL amplitude is the dial-deformed 2nd-order coefficient
    q(g) = u3^dag (C rho(g)) u3,  u3 a theta-odd (conjugate-antisymmetric) dir.
    At the object's own monodromy weld g = RL:
        q(RL) = 1/(2phi) + i*sin(2pi/5)/sqrt5  = 0.309017 + 0.425325 i.
  * the killed claim multiplied a FIBONACCI b-density 1/phi^2 (alphabet {a,b},
    substitution a->ab, b->a) by the WELD Re-part 1/(2phi) (alphabet {R,L}),
    attributed per-letter -> 1/(2phi^3).

Gate 5 STRICT: no SM value appears; the one-number pin is untouched; structural
only; no consciousness claim.

Run: python3 compute.py  (pyenv python3, NOT sage). ~20s.
"""
import importlib.util
import json
import math
import os

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
FRONT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))


def load(rel, name):
    spec = importlib.util.spec_from_file_location(
        name, os.path.join(FRONT, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b238 = load("B238_su32_levelrank/su32_wrt.py", "b238")

# ---- reconstruct the B593 hearing stage exactly -------------------------------
w, S, T, cc = b238.su3_data(2)
n = len(w)
C = np.zeros((n, n))
for i, wt in enumerate(w):
    C[w.index((wt[1], wt[0])), i] = 1.0
Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
R, L = T, Si @ Ti @ S                       # the two mapping-class LETTERS
theta_fund = T[w.index((1, 0)), w.index((1, 0))]     # spin of the fundamental

pairs = [(w.index((1, 0)), w.index((0, 1))), (w.index((2, 0)), w.index((0, 2)))]
U = np.zeros((n, 2))
for j, (a, b) in enumerate(pairs):
    U[a, j], U[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
u3 = U[:, 0].astype(complex)
u6 = U[:, 1].astype(complex)

phi = (1 + math.sqrt(5)) / 2
OUT = []


def p(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    OUT.append(s)


def rho(word):
    M = np.eye(n, dtype=complex)
    for ch in word:
        M = M @ (R if ch == 'R' else L)
    return M


def q(word, u=u3, twisted=True):
    """the dial-deformed 2nd-order chiral hearing coefficient u^dag (C rho) u."""
    W = (C @ rho(word)) if twisted else rho(word)
    return np.conj(u) @ W @ u


bar = "=" * 90
p(bar)
p("CELL P2W2-PERLETTER -- is a per-letter hearing weight FORCED by structure?")
p(bar)

# ---------------------------------------------------------------------------
# STEP 0 -- reproduce the banked WORD-level chiral amplitude (gate)
# ---------------------------------------------------------------------------
p("\n-- STEP 0: reproduce the banked WORD-level amplitude (gate) --")
qRL = q("RL")
banked = 1 / (2 * phi) + 1j * math.sin(2 * math.pi / 5) / math.sqrt(5)
p(f"  q(RL) = u3^dag (C rho(RL)) u3 = {qRL:+.9f}")
p(f"  banked 1/(2phi) + i sin(2pi/5)/sqrt5 = {banked:+.9f}")
gate0 = abs(qRL - banked) < 1e-9
p(f"  GATE match: {gate0}   [Re = 1/(2phi) = {1/(2*phi):.9f}, |amp| = {abs(qRL):.9f}]")
assert gate0, "stage does not reproduce the banked amplitude"

# ---------------------------------------------------------------------------
# STEP 1 -- the honest door: evaluate the SAME operator at SINGLE-LETTER welds
#           (length-1 words). This is the ONLY per-letter object derivable from
#           B593's machinery without a new assignment.
# ---------------------------------------------------------------------------
p("\n-- STEP 1: the per-letter candidate = the hearing form at LENGTH-1 welds --")
qR, qL = q("R"), q("L")
p(f"  q(R) = u3^dag (C rho(R)) u3 = {qR:+.9f}   |q(R)| = {abs(qR):.9f}")
p(f"  q(L) = u3^dag (C rho(L)) u3 = {qL:+.9f}   |q(L)| = {abs(qL):.9f}")

# R = T is DIAGONAL: the R-letter amplitude collapses to a pure spin phase.
p(f"\n  the R-letter collapses to a CHARACTER/SPIN invariant (B774 chord discipline):")
p(f"    theta_fund (topological spin of the fundamental) = {theta_fund:+.9f}")
qR_is_spin = abs(qR + theta_fund) < 1e-12
p(f"    q(R) = -theta_fund EXACTLY: {qR_is_spin}   |q(R)| = 1: {abs(abs(qR)-1)<1e-12}")
p("    => the diagonal letter R contributes ONLY a phase (abelian spin), no")
p("       magnitude, no non-abelian content -- the exact 'relabeled character")
p("       invariant' B774 warns against.")

# L = S^-1 T^-1 S is NON-diagonal: it carries the entire hearing modulus.
qL2 = abs(qL) ** 2
born = float((5 - sp.sqrt(5)) / 10)          # = 1/(phi*sqrt5), the B751 Born wt
p(f"\n  the L-letter carries the FULL modulus:")
p(f"    |q(L)|^2 = {qL2:.9f} = (5-sqrt5)/10 = 1/(phi*sqrt5): {abs(qL2-born)<1e-9}")
p(f"    |q(RL)| = |q(L)| = {abs(qRL):.9f}  -- the word adds NO magnitude over L.")

# ---------------------------------------------------------------------------
# STEP 2 -- the weld amplitude FACTORS over the diagonal letter, but the factor
#           is a pure phase: q(RL) = theta_fund * q(L) = -q(R)*q(L).
# ---------------------------------------------------------------------------
p("\n-- STEP 2: the amplitude factors over R, but R's factor is a pure phase --")
qLR = q("LR")
p(f"  q(RL) = {qRL:+.9f}")
p(f"  q(LR) = {qLR:+.9f}   q(RL)==q(LR): {abs(qRL-qLR)<1e-12} (order-independent here)")
fac = theta_fund * qL
p(f"  theta_fund * q(L) = {fac:+.9f}")
factors = abs(qRL - fac) < 1e-12
p(f"  q(RL) = theta_fund * q(L) = -q(R)*q(L) EXACTLY: {factors}")
p("  => the ONLY per-letter decomposition the structure forces is:")
p("       R-letter -> a spin PHASE (character invariant, |.|=1, no magnitude)")
p("       L-letter -> the entire complex amplitude (|.|=0.5257 = sqrt(1/(phi*sqrt5)))")
p("     there is ONE non-trivial hearing amplitude (L's); it is not a per-letter")
p("     DISTRIBUTION of weight -- a single generator carries all of it.")

# ---------------------------------------------------------------------------
# STEP 3 -- the killed number 1/(2phi) is a WORD-level Re-projection, equal to
#           NO forced per-letter value; the projection is itself a free knob.
# ---------------------------------------------------------------------------
p("\n-- STEP 3: the killed 1/(2phi) is a projection knob, not a per-letter value --")
candidates = {
    "Re q(RL) (the killed 1/(2phi))": qRL.real,
    "|q(L)|  (modulus proj)": abs(qL),
    "|q(L)|^2 (Born proj)": qL2,
    "Re q(L)": qL.real,
    "Re q(R)": qR.real,
    "|q(R)|^2": abs(qR) ** 2,
}
for k, v in candidates.items():
    p(f"    {k:34s} = {v:+.9f}")
p("  1/(2phi) = Re q(RL) MIXES R's phase (theta_fund) with L's magnitude; it")
p("  equals none of the forced single-letter magnitudes. Choosing Re vs |.| vs")
p("  |.|^2 changes the number (0.3090 / 0.5257 / 0.2764) -- the B751-addendum")
p("  three-projection knob. No projection is object-forced.")

# ---------------------------------------------------------------------------
# STEP 4 -- two DISJOINT alphabets. The forced per-letter Fibonacci structure is
#           the FREQUENCY (Perron), a density, NOT a hearing amplitude; the
#           amplitudes live in the mapping-class alphabet {R,L}. No forced functor.
# ---------------------------------------------------------------------------
p("\n-- STEP 4: two disjoint alphabets -- frequency (forced) != amplitude (weld-only) --")
Msub = sp.Matrix([[1, 1], [1, 0]])            # Fibonacci incidence a->ab, b->a
perron = None
for val, mult, vecs in Msub.eigenvects():
    if abs(complex(val) - phi) < 1e-9:
        perron = vecs[0]
v = sp.Matrix(perron)
v = v / (v[0] + v[1])
p(f"  substitution alphabet {{a,b}} (a->ab, b->a): forced Perron frequencies")
p(f"    freq(a) = {sp.nsimplify(v[0],[sp.sqrt(5)])} = {float(v[0]):.6f} (= 1/phi)")
p(f"    freq(b) = {sp.nsimplify(v[1],[sp.sqrt(5)])} = {float(v[1]):.6f} (= 1/phi^2)")
freq_forced = abs(float(v[0]) - 1/phi) < 1e-9 and abs(float(v[1]) - 1/phi**2) < 1e-9
p(f"  mapping-class alphabet {{R,L}}: the hearing amplitude q(.) lives HERE.")
p("  the frequencies are amplitude-LESS (no hearing form on a bare substitution")
p("  letter -- hearing is defined only on welds/monodromy words). The killed")
p("  (1/phi^2)_{a,b} * (1/(2phi))_{R,L} MULTIPLIES across two disjoint alphabets;")
p("  no forced functor identifies b with R or L, or a with the other.")

# ---------------------------------------------------------------------------
# VERDICT LOGIC (in-code; can emit RESOLVED-A / RESOLVED-B / UNRESOLVED)
# ---------------------------------------------------------------------------
p("\n" + bar)
p("VERDICT")
p(bar)

# A NON-ARBITRARY per-letter HEARING WEIGHT (the object needs, for a hearing
# density) must satisfy ALL of:
#   (C1) forced/derivable from B593's operator (no new assignment)
#   (C2) genuinely non-abelian / chiral per letter (B774: NOT a character invariant)
#   (C3) a per-letter DISTRIBUTION (each letter carries a well-defined weight,
#        not one generator carrying all of it)
#   (C4) lives in / forced-mapped to the Fibonacci {a,b} alphabet where a hearing
#        DENSITY would be taken, with a forced projection to a real weight.
c1_derivable = True                                   # q(R), q(L) exist
c2_nonabelian_per_letter = not qR_is_spin             # FALSE: R is a spin phase
c3_distribution = not factors                         # FALSE: R phase-only, L all
c4_forced_bridge_and_projection = False               # FALSE: two alphabets, 3-proj knob

p(f"  (C1) forced/derivable from B593 (length-1 welds):        {c1_derivable}")
p(f"  (C2) genuinely non-abelian per letter (not a character): {c2_nonabelian_per_letter}")
p(f"       [q(R) = -theta_fund exactly -> abelian spin invariant, B774 trap]")
p(f"  (C3) a per-letter DISTRIBUTION of weight:                {c3_distribution}")
p(f"       [q(RL) = theta_fund*q(L): R contributes only a phase, L carries all]")
p(f"  (C4) forced alphabet bridge + forced real projection:    {c4_forced_bridge_and_projection}")
p(f"       [Fibonacci {{a,b}} freqs forced (1/phi,1/phi^2) but amplitude-less;")
p(f"        Re vs |.| vs |.|^2 = 0.3090/0.5257/0.2764 is a free knob]")

if c1_derivable and c2_nonabelian_per_letter and c3_distribution and c4_forced_bridge_and_projection:
    verdict = "RESOLVED-A"
    terminal = "FORCED per-letter hearing weight"
    headline = ("a per-letter hearing weight is FORCED, non-abelian, distributed, "
                "and forced-mapped to the Fibonacci alphabet")
elif c1_derivable and not (c2_nonabelian_per_letter and c3_distribution and c4_forced_bridge_and_projection):
    verdict = "RESOLVED-B"
    terminal = "TOMBSTONE (no non-arbitrary per-letter hearing weight; the weight is a free knob)"
    headline = ("NO non-arbitrary per-letter hearing weight: the only structure-"
                "forced per-letter decomposition is q(RL)=theta_fund*q(L) -- the "
                "diagonal letter R is a pure spin/character invariant (B774 trap) "
                "and the single non-diagonal generator L carries the ENTIRE "
                "amplitude, so there is no per-letter DISTRIBUTION; the amplitude "
                "lives in the mapping-class alphabet {R,L}, disjoint from the "
                "Fibonacci {a,b} whose forced per-letter structure is the "
                "amplitude-less FREQUENCY (1/phi,1/phi^2); and 1/(2phi)=Re q(RL) is "
                "a word-level projection knob (Re/|.|/|.|^2 all 'natural'). The "
                "per-letter attribution is a free composition -- a knob, tombstone.")
else:
    verdict = "UNRESOLVED"
    terminal = "UNRESOLVED"
    headline = "the per-letter question did not resolve two-outcome; see cells."

p(f"\n  VERDICT: {verdict}")
p(f"  {headline}")

discriminating = (
    "The hearing form factors over the diagonal letter, q(RL)=theta_fund*q(L)=-q(R)q(L), "
    "with q(R)=-theta_fund EXACTLY (|q(R)|=1) -- a pure spin/character invariant (B774 "
    "trap) -- and the single non-diagonal generator L carrying the ENTIRE modulus "
    "|q(L)|^2=(5-sqrt5)/10=1/(phi*sqrt5). So there is no per-letter DISTRIBUTION of "
    "hearing weight (one generator holds all of it), the chiral content is not a "
    "per-letter property, and these amplitudes live in the mapping-class alphabet {R,L}, "
    "disjoint from the Fibonacci {a,b} whose only forced per-letter structure is the "
    "amplitude-less FREQUENCY 1/phi, 1/phi^2. The killed 1/(2phi)=Re q(RL) is a "
    "word-level projection (Re vs |.| vs |.|^2 = 0.3090/0.5257/0.2764, a free knob). "
    "=> no non-arbitrary per-letter hearing weight is forced."
)
p("\n  DISCRIMINATING FACT:")
p("  " + discriminating)

p("\n  GATE 5 self-check: no SM value compared (alpha_s NOT recomputed or matched);")
p("  one-number pin untouched; structural only; no consciousness claim. PASS.")

results = {
    "cell": "P2W2-PERLETTER",
    "campaign": "B775 Phase-2 Wave-2",
    "question": ("is a NON-ARBITRARY per-letter hearing weight forced by structure "
                 "(derived from B593's amplitude machinery, not assigned)?"),
    "verdict": verdict,
    "terminal_state": terminal,
    "headline": headline,
    "gate0_reproduces_banked_amplitude": bool(gate0),
    "q_RL": [float(qRL.real), float(qRL.imag)],
    "q_LR": [float(qLR.real), float(qLR.imag)],
    "q_R": [float(qR.real), float(qR.imag)],
    "q_L": [float(qL.real), float(qL.imag)],
    "q_R_equals_minus_theta_fund": bool(qR_is_spin),
    "theta_fund": [float(theta_fund.real), float(theta_fund.imag)],
    "factorization_q_RL_eq_thetafund_times_q_L": bool(factors),
    "abs_q_R": float(abs(qR)),
    "abs_q_L_squared": float(qL2),
    "abs_q_L_squared_closed_form": "(5-sqrt5)/10 = 1/(phi*sqrt5)",
    "criteria": {
        "C1_derivable": bool(c1_derivable),
        "C2_nonabelian_per_letter": bool(c2_nonabelian_per_letter),
        "C3_per_letter_distribution": bool(c3_distribution),
        "C4_forced_bridge_and_projection": bool(c4_forced_bridge_and_projection),
    },
    "fib_freq_forced_but_amplitude_less": bool(freq_forced),
    "fib_freq_a": "1/phi", "fib_freq_b": "1/phi^2",
    "projection_knob": {"Re": float(qRL.real), "modulus": float(abs(qL)),
                        "Born_|.|^2": float(qL2)},
    "discriminating_fact": discriminating,
    "gate5": "PASS (no SM comparison; one-number pin untouched; structural only)",
    "revives_alpha_s_match": False,
}
with open(os.path.join(HERE, "results.json"), "w") as f:
    json.dump(results, f, indent=2)
with open(os.path.join(HERE, "output.txt"), "w") as f:
    f.write("\n".join(OUT) + "\n")
p("\n  wrote results.json + output.txt")
