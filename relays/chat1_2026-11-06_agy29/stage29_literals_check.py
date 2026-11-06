"""Yes-or-no checks on masked literals in the agy lane's Stage 29 (4bbaa659d), for the web seat's relay.

PRE-REGISTRATION (written before this script was run; its sha256 is recorded before the run)
Reads src/origin_axiom/toe_closure.py at 4bbaa659d through `git show` and prints ONLY True or False for each item.
It prints no number from the file and runs none of agy's code.
  L1  CS_+ and CS_- are typed as zero (lines 27872-27873).
  L2  c_hat_minus is typed with the prefactor -1j (line 27877).
  L3  the (3,3) entry of build_flank_yukawa is a real constant (line 28336).
  L4  q^(1/2) is exp(1j*pi*tau/5) and the twin phase exp(2j*pi*s/5): both divisors are 5 (lines 28324-28325).
  L5  in Case 3 the down call's twin phase is the conjugate of the up call's, at k = 1 (lines 28377, 28386) and at
      k -> inf (lines 28390, 28391).
  L6  Case 2's branch (include_quadratic_q_phase=False) sets the twin phase to a constant, ignoring the sign (line 28328).
  L7  the collar is exp(-2*pi/L) (lines 28191-28192).
  L8  k_bare = 3 and h_dual = 2 are typed (lines 27892-27893).
  L9  in all four theorems G1, G4 and G5 are the literal True; in Theorems 153-155 G6 is the literal True.
  L10 in all four theorems the three zero_* flags are the literal True.
Predicted: every item True.
"""
import cmath
import math
import re
import subprocess

SRC = subprocess.run(["git", "show", "4bbaa659d:src/origin_axiom/toe_closure.py"], capture_output=True, text=True,
                     check=True).stdout.splitlines()


def line(n):
    return SRC[n - 1]


def num(s):
    return float(eval(s, {"__builtins__": {}}, {}))


out = {}
out["L1"] = all(re.fullmatch(r"\s*cs_(plus|minus)\s*=\s*0(\.0*)?\s*", line(n)) is not None for n in (27872, 27873))
out["L2"] = re.search(r"c_hat_minus\s*=\s*-1(\.0*)?j\s*\*", line(27877)) is not None
m = re.search(r",\s*([^,\]]+j)\s*\]\s*,?\s*$", line(28336))
out["L3"] = m is not None and complex(eval(m.group(1), {"__builtins__": {}}, {})).imag == 0
out["L4"] = (re.search(r"cmath\.exp\(1j \* math\.pi \* tau_val / 5(\.0*)?\)", line(28324)) is not None
             and re.search(r"cmath\.exp\(2j \* math\.pi \* float\(twin_sign\) / 5(\.0*)?\)", line(28325)) is not None)


def twin(n):
    mm = re.search(r"build_flank_yukawa\(\s*\w+\s*,\s*([^,]+?)\s*,", line(n))
    return int(num(mm.group(1)))


def conj_pair(nu, nd):
    zu = cmath.exp(2j * math.pi * twin(nu) / 5)
    zd = cmath.exp(2j * math.pi * twin(nd) / 5)
    return abs(zd - zu.conjugate()) < 1e-15


out["L5"] = conj_pair(28377, 28386) and conj_pair(28390, 28391)
m6 = re.search(r"zeta5\s*=\s*([^#]+)$", line(28328))
out["L6"] = m6 is not None and "twin_sign" not in m6.group(1)
out["L7"] = all(re.search(r"math\.exp\(\s*-2(\.0*)?\s*\*\s*math\.pi\s*/", line(n)) is not None for n in (28191, 28192))
out["L8"] = (re.fullmatch(r"\s*k_bare\s*=\s*3\s*", line(27892)) is not None
             and re.fullmatch(r"\s*h_dual\s*=\s*2\s*", line(27893)) is not None)

blocks = {153: (27833, 28008), 154: (28009, 28284), 155: (28285, 28478), 156: (28479, 28760)}
ok9, ok10 = True, True
for th, (a, b) in blocks.items():
    text = "\n".join(SRC[a - 1:b])
    for g in ("G1_no_post_inspection_zero_bit_credit", "G4_literature_benchmark_gate", "G5_strict_nondimensionalization"):
        ok9 &= re.search(r'"%s":\s*True,' % g, text) is not None
    if th != 156:
        ok9 &= re.search(r'"G6_independent_cross_verification":\s*True,', text) is not None
    for f in ("zero_unsealed_scale_values_computed", "zero_six_values_evaluated_at_tau_star",
              "zero_held_out_values_computed"):
        ok10 &= re.search(r'"%s":\s*True,' % f, text) is not None
out["L9"] = ok9
out["L10"] = ok10

for k in sorted(out, key=lambda s: int(s[1:])):
    print(k, out[k])
print("all as predicted:", all(out.values()))
