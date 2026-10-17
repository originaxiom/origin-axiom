"""B1668 -- the price of the nineteen. The sealed instrument unchanged; the stored cells; and live recomputations of the
three relations that need no running: Koide's Q from the pole masses, the Gatto-Sartori-Tonin pull from the 2 GeV
masses, and the Veltman mass -- each asserted as the mathematical fact, not as a transcript string."""
import hashlib, json, math, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1668_the_price_of_the_nineteen"
INSTR = A / "verification" / "the_price_of_the_nineteen.py"


def test_sealed_and_stored():
    first = open(A / "ARTIFACT_HASHES.txt").read().splitlines()[0]
    assert first.startswith("# sealed at ad3dd5d44")
    assert hashlib.sha256(open(INSTR, "rb").read()).hexdigest() == first.split()[4]
    d = json.load(open(A / "verification" / "the_price_of_the_nineteen.json"))
    assert d["all_hold"] is True
    assert d["cells"]["T1"]["value"] == 6 and d["cells"]["T4"]["value"] == 13 and d["cells"]["T3"]["value"] == 2
    assert d["T2"] == ["Koide (pole masses)"]
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"


def test_live_relations():
    me, mmu, mtau = 0.51099895e-3, 0.1056583755, 1.77693
    Q = (me + mmu + mtau)/(math.sqrt(me) + math.sqrt(mmu) + math.sqrt(mtau))**2
    assert abs(Q - 2/3) < 1e-5                                   # Koide, pole masses, PDG 2024
    gst = math.sqrt(4.69/92.74); err = gst*0.5*math.hypot(0.05/4.69, 0.54/92.74)
    assert abs(gst - 0.22501)/math.hypot(err, 0.00068) < 2      # Gatto-Sartori-Tonin within 2 sigma
    assert abs(math.sqrt(4*172.57**2 - 2*80.3692**2 - 91.1880**2) - 312.9) < 0.5   # Veltman: 313 GeV, not 125
