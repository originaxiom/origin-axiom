#!/usr/bin/env python3
"""W-A3, labelled post hoc 1. The sealed wa3_checks.py stopped at its own sanity assertion: its word for the act,
S T^-1 S^-1 T, multiplies to L R = [[1, 1], [1, 2]], not the record's [[2, 1], [1, 1]] = R L. This file runs the sealed
script unchanged except for that word, replaced by T S T^-1 S^-1 (= R L) in both places it is used. Nothing else changes.

    python3 -I -u wa3_posthoc_word.py
"""
import hashlib, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "wa3_checks.py")).read()
assert hashlib.sha256(src.encode()).hexdigest() == open(os.path.join(HERE, "SCRIPT_SHA256.txt")).read().split()[0]
old1 = "word_LR = Sm @ np.linalg.inv(Tm).round().astype(int) @ np.linalg.inv(Sm).round().astype(int) @ Tm"
new1 = "word_LR = Tm @ Sm @ np.linalg.inv(Tm).round().astype(int) @ np.linalg.inv(Sm).round().astype(int)"
old2 = "R_LR = S_ @ np.linalg.inv(T_) @ np.linalg.inv(S_) @ T_"
new2 = "R_LR = T_ @ S_ @ np.linalg.inv(T_) @ np.linalg.inv(S_)"
assert src.count(old1) == 1 and src.count(old2) == 1
src = src.replace(old1, new1).replace(old2, new2)
src = src.replace('os.path.join(HERE, "wa3_checks_output.json")', 'os.path.join(HERE, "wa3_posthoc_word_output.json")')
g = {"__name__": "__main__", "__file__": os.path.join(HERE, "wa3_checks.py")}
exec(compile(src, "wa3_checks.py (post hoc 1: the act's word)", "exec"), g)
