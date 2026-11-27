"""The web seat's two older notes of 2026-10-16 taken in at harvest row 1977 (W_TRACE_UNTWISTED and THE BRAINSTORM VERDICT): the
exact facts in them main can hold on its own code.  Nothing of the seat's is run.
 T1  2 pi * 7/4 = 10.9956, which the notes give as 11.00 (the units' leading cusp exponent |q^(-7/8)|^2 = e^(2 pi (7/4) y))
 T2  LR = [[2, 1], [1, 1]] and RL = [[1, 1], [1, 2]] have trace 3, and their product trace 6 (the Markov traces 3, 3, 6)
 T3  the commutator a b a^-1 b^-1 of a = LR, b = RL is [[-7, 6], [-6, 5]]; the notes' [[5, -6], [6, -7]] is its inverse,
     b a b^-1 a^-1 (the notes state no convention); both have trace -2 (parabolic) and fix 1
     [CORRECTED 2026-11-27 (harvest row 2042; the web seat's section 35.4 (a)): the convention is stated, in the
     seat's arena_checks.py, line 11 (L = [[1, 0], [1, 1]], R = [[1, 1], [0, 1]], the transposes of this script's), and with
     it the notes' matrix is a b a^-1 b^-1 exactly: web_trace_notes_t3_convention.py. "State no convention" was wrong.]
 T4  L^(t-2) R has #R - #L = 3 - t (the least balanced word of its trace layer)
    python3 -B web_trace_notes.py > web_trace_notes_run.txt"""
import math
import sympy as sp
L = sp.Matrix([[1, 1], [0, 1]]); R = sp.Matrix([[1, 0], [1, 1]])
print("T1: 2 pi 7/4 = %.4f, to two decimals %.2f" % (2 * math.pi * 7 / 4, 2 * math.pi * 7 / 4))
LR, RL = L * R, R * L
print("T2: LR = %s, RL = %s; traces %s, %s; tr(LR RL) = %s" % (LR.tolist(), RL.tolist(), LR.trace(), RL.trace(), (LR * RL).trace()))
C1 = LR * RL * LR.inv() * RL.inv(); C = C1.inv(); x = sp.Symbol("x")
fix = lambda M: sp.solve(sp.Eq((M[0, 0] * x + M[0, 1]) / (M[1, 0] * x + M[1, 1]), x), x)
print("T3: a b a^-1 b^-1 = %s; its inverse b a b^-1 a^-1 = %s (the notes' matrix: %s); traces %s, %s; fixed points %s, %s" % (
    C1.tolist(), C.tolist(), C.tolist() == [[5, -6], [6, -7]], C1.trace(), C.trace(), fix(C1), fix(C)))
print("T4: #R - #L of L^(t-2) R for t = 3 to 12: %s" % [1 - (t - 2) for t in range(3, 13)])
ok = round(2 * math.pi * 7 / 4, 2) == 11.0 and (LR.trace(), RL.trace(), (LR * RL).trace()) == (3, 3, 6) and C.tolist() == [[5, -6], [6, -7]] and C.trace() == -2 and C1.trace() == -2 and fix(C1) == [1] and fix(C) == [1]
print("ALL HOLD:", ok)
