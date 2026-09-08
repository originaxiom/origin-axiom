"""PREREG §5(e): the code can return I != 0, and the 3-manifold identities are theorems, not tautologies of the code.
Random 2-generator 1-relator presentations with a random 'peripheral' pair and random local systems over Q(zeta_12)."""
import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import d2lib as L
from d2lib import K, ONE
random.seed(20260907)
torus = L.Presentation(["m", "l"], [[("m", 1), ("l", 1), ("m", -1), ("l", -1)]])
def rand_word(n): return L.free_reduce([(random.choice("ab"), random.choice((1, -1))) for _ in range(n)])
def rand_mat(n):
    while True:
        M = [[K((random.randint(-1, 1), random.randint(-1, 1), 0, 0)) for _ in range(n)] for _ in range(n)]
        try: L.general_inv(M); return M
        except StopIteration: pass
nonzero = 0; broken = 0; trials = 0
for trial in range(40):
    pres = L.Presentation(["a", "b"], [rand_word(random.randint(6, 10))])
    cusp = [rand_word(random.randint(2, 5)), rand_word(random.randint(2, 5))]
    if not cusp[0] or not cusp[1] or not pres.rels[0]: continue
    n = random.choice((2, 3))
    mats = {"a": rand_mat(n), "b": rand_mat(n)}
    try: d = L.index_data(pres, mats, cusp, torus)
    except Exception as e: continue
    trials += 1
    if d["I"] != 0: nonzero += 1
    if not all(d["checks"].values()): broken += 1
    if trial < 8: print(f" trial {trial}: n={n} I={d['I']:+d} F={d['F']:+d} Cc={d['Cc']:+d} identities={d['checks']}")
print(f"\n{trials} random trials: I != 0 in {nonzero}; at least one 3-manifold identity violated in {broken}")
assert nonzero > 0 and broken > 0
print("NON-VACUITY (algebraic): PASS -- the criterion I != 0 is reachable by the code; the identities are not built in")
