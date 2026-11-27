"""B1957, 2026-11-27 (the web seat's section 35.4 (a); harvest row 2042): T3 of web_trace_notes.py with the seat's own
convention. The seat's relays/chat1_2026-10-16_no_thread_rule/arena_checks.py (04286891a), line 11, sets
L = [[1, 0], [1, 1]] and R = [[1, 1], [0, 1]] (main's T3 used the transposes), and its line 13 computes LR RL (LR)^-1 (RL)^-1.
With those L and R, a = LR and b = RL, the commutator a b a^-1 b^-1 is THE BRAINSTORM VERDICT's [[5, -6], [6, -7]] exactly.
Nothing of the seat's is run; the matrices are typed from its line 11 and recomputed here.
    python3 -B web_trace_notes_t3_convention.py > web_trace_notes_t3_convention_run.txt"""
import sympy as sp
L = sp.Matrix([[1, 0], [1, 1]]); R = sp.Matrix([[1, 1], [0, 1]])
a, b = L * R, R * L
C = a * b * a.inv() * b.inv()
print("the seat's L = %s, R = %s; a = LR = %s, b = RL = %s" % (L.tolist(), R.tolist(), a.tolist(), b.tolist()))
print("a b a^-1 b^-1 = %s; the note's matrix [[5, -6], [6, -7]]: %s; trace %s" % (C.tolist(), C.tolist() == [[5, -6], [6, -7]], C.trace()))
# the control: with main's L and R (the transposes) the same product is the inverse, so the check can fail
Lm, Rm = L.T, R.T
Cm = (Lm * Rm) * (Rm * Lm) * (Lm * Rm).inv() * (Rm * Lm).inv()
print("with main's L, R (the transposes): a b a^-1 b^-1 = %s, the note's matrix: %s" % (Cm.tolist(), Cm.tolist() == [[5, -6], [6, -7]]))
print("HOLDS:", C.tolist() == [[5, -6], [6, -7]] and Cm.tolist() != [[5, -6], [6, -7]])
