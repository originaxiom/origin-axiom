"""B1836 § 2: T is a symmetry of the frame's outputs. B1726's compute() at (tau, (a, b)) against (tau + 1, (a, b - a)): every
singular-value ratio, |V| and |J| (the moduli), four points including the candidate's address. Data-free."""
import importlib.util, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4]
spec = importlib.util.spec_from_file_location("c", ROOT / "frontier/B1726_the_two_ingredients_replicated/verification/census.py")
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
worst = 0.0; n = 0
for (re, im, a, b) in ((0.35, 2.75, 0.4, 0.1), (0.12, 3.1, 0.4, 0.3), (0.3333, 3.0368, 0.4, 0.1), (0.2, 2.6, 1 / 7, 3 / 7)):
    o1 = C.compute(re, im, a, b); o2 = C.compute(re + 1, im, a, b - a)
    for k, v in o1.items():
        if isinstance(v, list):
            worst = max(worst, max(abs(abs(x) - abs(y)) for x, y in zip(v, o2[k]))); n += 1
print("T: compute(tau,(a,b)) vs compute(tau+1,(a,b-a)) over %d keys: max |difference| = %.1e" % (n, worst))
