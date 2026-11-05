"""The web seat, 2026-11-05: P-682's order dictionary at EVERY order N = 2..30 (data-free).

Main's check (frontier/B1835_u_e_and_the_pmns/verification/order_dictionary.py, S303) states B1728's rule and confirms it
on B1835's card instrument at 11 orders (2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 30). P-682's register row and S303's text then
say "8-30 none exactly". This runs main's script unchanged except for two lines: ORDERS becomes every N from 2 to 30, and
ROOT is main's checkout given on the command line. Same rule, same instrument, same lines (1/N, 0) and (1/N, 1/N), same two
tau. Expected from the rule by hand before the run: N = 7 adds up ~ lepton^T, since (1, -4) = -(6, -3) mod 7; N = 9 makes
the lepton matrix symmetric, since (-3, 6) = (6, 6) mod 9. No line on the family's slope; no CKM, no theta-bar.

    python3 order_dictionary_all_orders.py <main checkout>     (main at c70b356f0)
"""
import pathlib
import sys

root = pathlib.Path(sys.argv[1]).resolve()
path = root / "frontier/B1835_u_e_and_the_pmns/verification/order_dictionary.py"
src = path.read_text()
old_orders = "ORDERS = [2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 30]"
old_root = "ROOT = pathlib.Path(__file__).resolve().parents[3]"
assert src.count(old_orders) == 1 and src.count(old_root) == 1
src = src.replace(old_orders, "ORDERS = list(range(2, 31))").replace(old_root, "ROOT = pathlib.Path(%r)" % str(root))
print("main's order_dictionary.py, run with ORDERS = 2..30 (two lines changed; main's own rule and instrument)")
exec(compile(src, str(path), "exec"), {"__name__": "__main__", "__file__": str(path)})
