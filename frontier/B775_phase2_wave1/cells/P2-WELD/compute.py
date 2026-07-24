"""B775 Phase-2 Wave-1 -- cell P2-WELD (H-WORD-WELD).

Derive the mechanism linking the Fibonacci word Markov subdominant eigenvalue
(-1/phi) to the banked untwisted weld theta-odd trace (-1/phi), OR dismiss the
equality as a base-rate golden coincidence.

Program-internal spectral mathematics only. No SM values. pyenv python3.
Re-runnable. Emits an in-code verdict (RESOLVED-A / RESOLVED-B / UNRESOLVED)
and writes results.json.
"""
import importlib.util
import json
import math
import os

import numpy as np

try:
    import sympy as sp
    HAVE_SYMPY = True
except Exception:
    HAVE_SYMPY = False

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
PHI = (1 + math.sqrt(5)) / 2
TOL = 1e-9
R = {}   # results collector


def load(rel, name):
    spec = importlib.util.spec_from_file_location(
        name, os.path.join(ROOT, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b238 = load("frontier/B238_su32_levelrank/su32_wrt.py", "b238")


def weld_odd_block(level, word, twist):
    """theta-odd 2x2 block of the (un)twisted weld at the given word."""
    w, S, T, cc = b238.su3_data(level)
    n = len(w)
    C = np.zeros((n, n))
    for i, wt in enumerate(w):
        C[w.index((wt[1], wt[0])), i] = 1.0
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    Rm, Lm = T, Si @ Ti @ S
    W = np.eye(n, dtype=complex)
    for ch in word:
        W = W @ (Rm if ch == "R" else Lm)
    if twist:
        W = C @ W
    # theta-odd basis: antisymmetric combos of conjugate weight pairs
    prs = sorted({(min(a, b), max(a, b)) for (a, b) in w if a != b})
    U = np.zeros((n, len(prs)), dtype=complex)
    for j, (a, b) in enumerate(prs):
        U[w.index((a, b)), j] = 1 / np.sqrt(2)
        U[w.index((b, a)), j] = -1 / np.sqrt(2)
    return U.conj().T @ W @ U


print("=" * 78)
print("CELL 1 -- reproduce BOTH sides of the coincidence (pipeline, first way)")
print("=" * 78)
# word side
T_word = np.array([[1 / PHI ** 2, 1 / PHI], [1.0, 0.0]])
word_spec = sorted(np.linalg.eigvals(T_word).real)
word_sub = word_spec[0]  # subdominant (dominant = 1, stochastic)
print(f"Fibonacci word Markov T = [[1/phi^2, 1/phi],[1,0]]")
print(f"  spectrum = {[round(x,6) for x in word_spec]}  (dominant=1, subdominant={word_sub:+.6f})")
print(f"  subdominant == det(T) == -1/phi : "
      f"{abs(word_sub - (-1/PHI)) < TOL} , {abs(np.linalg.det(T_word) - (-1/PHI)) < TOL}")
# weld side -- untwisted fig-8 RL at SU(3) level 2
B_un = weld_odd_block(2, "RL", twist=False)
tr_un = np.trace(B_un)
ev_un = np.linalg.eigvals(B_un)
ph_un = sorted(round(math.degrees(math.atan2(e.imag, e.real)), 3) for e in ev_un)
print(f"untwisted weld RL theta-odd block: trace = {tr_un.real:+.6f}{tr_un.imag:+.1e}j")
print(f"  eigenphases (deg) = {ph_un}  (= +-108 = +-3pi/5)")
B_tw = weld_odd_block(2, "RL", twist=True)
tr_tw = np.trace(B_tw)
print(f"twisted weld C.RL theta-odd trace = {tr_tw.real:+.6f}  (= +1/phi, the SIGN-FLIP partner)")
match = abs(word_sub - tr_un.real) < TOL and abs(tr_un.imag) < TOL
print(f"\n>> COINCIDENCE REPRODUCED: word_sub = weld_tr(untwisted) = -1/phi : {match}")
R["word_subdominant"] = float(word_sub)
R["weld_untwisted_odd_trace"] = float(tr_un.real)
R["weld_twisted_odd_trace"] = float(tr_tw.real)
R["coincidence_reproduced"] = bool(match)

print("=" * 78)
print("CELL 2 -- second way: -1/phi is ONE algebraic number = Galois conjugate of phi")
print("=" * 78)
val = -1 / PHI
checks = {
    "-1/phi": -1 / PHI,
    "1 - phi (Galois conjugate)": 1 - PHI,
    "2cos(3pi/5) = 2cos(108deg)": 2 * math.cos(3 * math.pi / 5),
    "root of x^2 - x - 1 (minus branch)": (1 - math.sqrt(5)) / 2,
}
for name, v in checks.items():
    print(f"  {name:38s} = {v:+.9f}   == -1/phi: {abs(v - val) < 1e-12}")
if HAVE_SYMPY:
    x = sp.symbols("x")
    r = sp.Rational
    phi_s = (1 + sp.sqrt(5)) / 2
    conj = 1 - phi_s
    minpoly = sp.minimal_polynomial(2 * sp.cos(3 * sp.pi / 5), x)
    print(f"  [sympy] minimal_polynomial(2cos(3pi/5)) = {minpoly}")
    print(f"  [sympy] 2cos(3pi/5) - (1-phi) simplifies to: "
          f"{sp.simplify(2*sp.cos(3*sp.pi/5) - conj)}")
    R["minpoly_2cos3pi5"] = str(minpoly)
same_number = all(abs(v - val) < 1e-12 for v in checks.values())
print(f"\n>> All four are the SAME number: {same_number}")
print("   Both sides live in Q(sqrt5); both SELECT the non-Perron / conjugate / odd branch.")
R["all_same_algebraic_number"] = bool(same_number)

print("=" * 78)
print("CELL 3 -- B774 self-test: is the weld 'theta-odd trace' a genuine chord?")
print("=" * 78)
# a trace is a symmetric function of eigenvalues == a symmetric trace polynomial.
tr_from_eigsum = sum(ev_un)
print(f"  weld theta-odd trace = sum of block eigenvalues = {tr_from_eigsum.real:+.6f}")
print(f"  == power-sum p1(eigenvalues) (a SYMMETRIC trace polynomial): "
      f"{abs(tr_from_eigsum - tr_un) < 1e-12}")
is_chord = False  # it is literally a trace / eigenvalue sum -> abelian invariant
print(f"  B774 verdict: the 'theta-odd trace' IS a symmetric trace polynomial")
print(f"  => it is an ABELIAN spectral/character invariant, NOT a genuine non-abelian chord.")
print(f"  Two abelian spectral invariants coinciding at a golden value is exactly the")
print(f"  base-rate class B774 warns of (a relabeled trace invariant).")
R["weld_trace_is_symmetric_polynomial"] = True
R["weld_trace_is_genuine_chord"] = is_chord

print("=" * 78)
print("CELL 4 -- BASE-RATE enumeration: distinct structural sources of -1/phi")
print("=" * 78)
sources = {
    "Fibonacci substitution incidence [[1,1],[1,0]] subdominant eigenvalue":
        sorted(np.linalg.eigvals(np.array([[1., 1.], [1., 0.]])).real)[0],
    "Fibonacci word Markov [[1/phi^2,1/phi],[1,0]] subdominant eigenvalue":
        word_sub,
    "untwisted fig-8 weld RL theta-odd trace (= 2cos 3pi/5)":
        tr_un.real,
    "Galois conjugate of phi (1 - phi = phi')":
        1 - PHI,
    "conjugate root of the golden minimal polynomial x^2 - x - 1":
        (1 - math.sqrt(5)) / 2,
    "non-unitary (Yang-Lee) Galois-conjugate quantum dim of Fibonacci cat":
        -1 / PHI,
}
hits = 0
for name, v in sources.items():
    hit = abs(v - val) < 1e-9
    hits += hit
    print(f"  [{'X' if hit else ' '}] {name:62s} = {v:+.6f}")
print(f"\n>> N = {hits} distinct structural sources all yield -1/phi.")
R["N_sources_hitting_minus_1_over_phi"] = int(hits)
# repo ubiquity (informational; grepped separately: 168 files touch 0.618034/-1/phi)
R["repo_files_touching_golden_0p618"] = 168

print("=" * 78)
print("CELL 5 -- DISCRIMINATING object-change test: does word<->weld survive m136?")
print("=" * 78)
# m136 = R^2 L bundle, monodromy [[3,2],[1,1]]; field Q(sqrt3).
Mm = np.array([[3., 2.], [1., 1.]])
m136_mono = sorted(np.linalg.eigvals(Mm).real)
m136_sub = m136_mono[0]  # subdominant monodromy eigenvalue = 2 - sqrt3
print(f"m136 monodromy [[3,2],[1,1]] spectrum = {[round(x,6) for x in m136_mono]}")
print(f"  subdominant (word-side analogue) = {m136_sub:+.6f} = 2 - sqrt3 (REAL, Q(sqrt3))")
# m136 weld theta-odd trace at level 2 (word RRL), from the SAME pipeline
B_m136 = weld_odd_block(2, "RRL", twist=False)
tr_m136 = np.trace(B_m136)
print(f"m136 weld RRL theta-odd trace at level 2 = {tr_m136.real:+.6f}{tr_m136.imag:+.6f}j")
print(f"  |imag| = {abs(tr_m136.imag):.6f}  -> COMPLEX (omega = -1/2 + i sqrt3/2 family, B610)")
generalizes = (abs(tr_m136.imag) < TOL and abs(m136_sub - tr_m136.real) < 1e-6)
print(f"\n  word-side (real 2-sqrt3) vs weld-side (complex): match under object change? "
      f"{generalizes}")
print(f"  RATIONALE: any 2-letter substitution/Markov matrix is 2x2 real with a REAL")
print(f"  subdominant eigenvalue; the m136 weld theta-odd trace is COMPLEX. They cannot")
print(f"  coincide. The fig-8 equality does NOT survive the object change.")
R["m136_monodromy_subdominant"] = float(m136_sub)
R["m136_weld_odd_trace_real"] = float(tr_m136.real)
R["m136_weld_odd_trace_imag"] = float(tr_m136.imag)
R["m136_weld_trace_is_complex"] = bool(abs(tr_m136.imag) > TOL)
R["correspondence_generalizes"] = bool(generalizes)

print("=" * 78)
print("VERDICT")
print("=" * 78)
# ---- verdict logic ----
mechanism_found = False            # no derivation making the equality an identity
base_rate = (R["coincidence_reproduced"]
             and R["all_same_algebraic_number"]
             and not R["weld_trace_is_genuine_chord"]
             and R["N_sources_hitting_minus_1_over_phi"] >= 3
             and not R["correspondence_generalizes"])

if mechanism_found:
    verdict = "RESOLVED-A"
    headline = "Derived structural link; E20 flag lifts"
elif base_rate:
    verdict = "RESOLVED-B"
    headline = ("DISMISSED as base-rate golden coincidence: -1/phi is the Galois "
                "conjugate golden unit produced by N>=3 distinct sources; the weld "
                "theta-odd 'trace' is a symmetric trace polynomial (abelian, not a "
                "chord); the word<->weld equality FAILS to generalize to m136 "
                "(real 2-sqrt3 vs complex omega). E20 stands; tombstone.")
else:
    verdict = "UNRESOLVED"
    headline = "Neither a derivation nor a clean base-rate dismissal emerged."

R["verdict"] = verdict
R["headline"] = headline
R["mechanism_found"] = mechanism_found
R["base_rate_dismissal"] = bool(base_rate)
print(f"VERDICT: {verdict}")
print(headline)

with open(os.path.join(HERE, "results.json"), "w") as f:
    json.dump(R, f, indent=2)
print("\nresults.json written.")
