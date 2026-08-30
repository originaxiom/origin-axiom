import os as _os
from pathlib import Path as _P
# the repo root: three levels up from frontier/<arc>/verification/, overridable for
# out-of-tree runs (this bundle is re-run from a staging dir before it is installed).
_ROOT = _os.environ.get("OA_ROOT") or str(_P(__file__).resolve().parents[3])
"""INDEPENDENT check of cloud memo 123: can ANY abelian character of the 27 stabilize a neutral?

Built on MAIN's own 27-weight generator (B299's _weights_27, minuscule Dynkin labels), not on
their code. A character w -> zeta_n^(<a,w> + c) stabilizes a neutral iff its CHARGED set (weights
with nonzero exponent) is a NONEMPTY SUBSET of the neutrals -- charges add on products, so a
charged state whose only company is neutral cannot decay to uncharged visible states.
"""
import importlib.util, sys
from itertools import product
spec = importlib.util.spec_from_file_location(
    "tt", _ROOT + "/frontier/B299_trinification_triality/trinification_triality.py")
tt = importlib.util.module_from_spec(spec); spec.loader.exec_module(tt)
W = tt._weights_27()
print(f"27's weights from main's own generator: {len(W)} weights, rank {len(W[0])}")
assert len(W) == 27 and len(set(map(tuple, W))) == 27

# The two neutrals: in the minuscule 27 the SM singlets are the two weights fixed by the
# SM-relevant Cartan directions. We do NOT need their identity to run the census -- the
# strongest form of the claim is over EVERY 2-subset, so quantify over all of them.
results = {}
for n in range(2, 7):
    stab, min_charged, max_level = 0, 99, 0
    for a in product(range(n), repeat=6):
        vals = [sum(ai * wi for ai, wi in zip(a, w)) % n for w in W]
        for c in range(n):
            ex = [(v + c) % n for v in vals]
            charged = [i for i, e in enumerate(ex) if e != 0]
            k = len(charged)
            if 0 < k <= 2:
                stab += 1                      # a candidate stabilizer: charged set of size <= 2
            if k > 0:
                min_charged = min(min_charged, k)
        # largest nontrivial level set (for the affine/shifted case)
        if any(v != vals[0] for v in vals):
            counts = {}
            for v in vals: counts[v] = counts.get(v, 0) + 1
            max_level = max(max_level, max(counts.values()))
    results[n] = (stab, min_charged, max_level)
    print(f"  n={n}: candidate stabilizers (charged set of size 1 or 2) = {stab}; "
          f"min |charged| over nontrivial characters = {min_charged}; "
          f"max nontrivial level set = {max_level}")

print("\n=== VERDICT ===")
tot = sum(r[0] for r in results.values())
print(f"    stabilizers found across n = 2..6: {tot}")
assert tot == 0, "a stabilizer would refute the memo"
print(f"    smallest charged set any nontrivial character produces: {min(r[1] for r in results.values())}")
print(f"    largest level set: {max(r[2] for r in results.values())} of 27  (a stabilizer needs >= 25)")
print("    => cloud memo 123 INDEPENDENTLY CONFIRMED on main's own weight data:")
print("       no abelian character of the 27 can stabilize a neutral, and the margins are wide.")

print("\n=== CONTROL (MB12): the test must be able to SUCCEED ===")
# Plant a rep whose weights DO admit an isolating character: two states carrying charge, rest neutral.
fake = [(0,)*6] * 25 + [(1,) + (0,)*5, (2,) + (0,)*5]
n = 3
found = 0
for a in product(range(n), repeat=6):
    vals = [sum(ai*wi for ai, wi in zip(a, w)) % n for w in fake]
    for c in range(n):
        ex = [(v + c) % n for v in vals]
        k = sum(1 for e in ex if e != 0)
        if 0 < k <= 2: found += 1
print(f"    planted rep (25 neutral + 2 charged): stabilizers found = {found}")
assert found > 0, "the instrument cannot detect a stabilizer -- the census would be vacuous"
print("    => the instrument DOES fire when a stabilizer exists. The negative is real.")
print("\nVERIFIED")
