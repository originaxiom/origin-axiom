"""B1478 -- the web seat's branch harvested and five GENESIS amendments ruled: the amendment script reproduces the page,
the checks of A1 and A4 run live, the re-run logs carry the seat's stated outcomes, and the seat is registered."""
import json, os, subprocess, sys, itertools
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "frontier", "B1478_the_web_seats_branch_harvested_and_five_genesis_amendments_ruled")


def test_genesis_is_what_the_amendment_produces():
    assert subprocess.run([sys.executable, os.path.join(A, "adoption", "amend.py"), "--check"]).returncode == 0
    g = open(os.path.join(ROOT, "GENESIS.md"), encoding="utf-8").read()
    v = [int(x.split()[0]) for x in g.split("**Version 1.")[1:2]]; assert v and v[0] >= 12
    for needle in ("FK13", "U1-η", "U1-Z′₉", "n ≡ 2 (mod 4)", "MODULI"): assert needle in g, needle


def test_a1_parity_rule_live():
    for n in range(2, 21, 2):
        odd = [k for k in range(0, n // 2 + 1) if (n - 2 * k) % 4 == 0 and k % 2]
        assert bool(odd) == (n % 4 == 2), n


def test_a4_charges_and_anomalies_live():
    st = [(10, 1, -1), (5, 1, 3), (1, 1, -5), (5, -2, 2), (5, -2, -2), (1, 4, 0)]
    q = [(m, (5 * a - 3 * b) // 2) for m, a, b in st]
    assert sum(m for m, _ in q) == 27 and sum(m * c for m, c in q) == 0 and sum(m * c ** 3 for m, c in q) == 0
    assert [c for _, c in q] == [4, -2, 10, -8, -2, 10]
    assert sum(m * c ** 3 for m, c in q[:3]) != 0                      # the check can fail: the 16 alone is anomalous
    assert sum(f ** 3 for f in (-10, 5, 5)) == -750 and sum(f ** 3 for f in (0, 7, -7)) == 0   # B1340: the family part's cube is what chirality tests
    g = open(os.path.join(ROOT, 'GENESIS.md'), encoding='utf-8').read(); assert 'not gaugeable as it stands' in g and 'B1340' in g


def test_a3_census_and_the_reruns():
    c = json.load(open(os.path.join(A, "verification", "checks.json")))["A3"]
    assert (c["realisations"], c["rational"], c["irrational"], c["amphichiral"]) == (74, 18, 56, 16) and c["amphichiral_classes"] == [0.0, 0.25]
    r = lambda f: open(os.path.join(A, "verification", "rerun_%s.txt" % f), encoding="utf-8").read()
    assert "P1: PASS" in r("p1_tower") and "R2: PASS" in r("r2_r3_primes") and "P3 Shapiro: PASS" in r("p3_shapiro") and "Q3: PASS" in r("pin_half")
    for f in ("p2_door", "r1_door_t_b"):
        t = r(f); assert "(omega<->omegabar): 0" in t and "OTHER half in 48 of 48" in t and ": 24   (predicted 24)" in t
    assert "(SnapPy presentation, by enumeration): 0" in r("r2_r3_primes")


def test_the_seat_is_registered():
    h = open(os.path.join(ROOT, "scripts", "checks", "harvest_debt.py"), encoding="utf-8").read(); assert 'key="chat1"' in h
    led = open(os.path.join(ROOT, "docs", "HARVEST_LEDGER.md"), encoding="utf-8").read()
    assert "| chat1 | `origin/chat1/web-seat`" in led and all(("| %d | web seat (chat1) |" % n) in led for n in (879, 880, 881))
