# Which sequences of B1895's lock test (test_the_bound_on_the_least_reading_recomputed) were already tried by the arc's script part_b
import itertools
script = {s for n, top in ((2, 6), (4, 6), (6, 3)) for s in itertools.product(range(1, top + 1), repeat=n)}
lock = [q for q in itertools.product(range(1, 13), repeat=2)] + [q for q in itertools.product(range(1, 5), repeat=4)]
lock += [(2,) * n for n in (2, 4, 6, 8, 10)] + [(2,) + (1,) * (n - 1) for n in (2, 4, 6, 8, 10)] + [(1,) * n for n in (2, 4, 6, 8, 10)]
print("lock entries", len(lock), "distinct", len(set(lock)), "already tried by the script", len(set(lock) & script), "new", len(set(lock) - script))
print("length-4 runs-to-4 all tried:", all(q in script for q in itertools.product(range(1, 5), repeat=4)))
