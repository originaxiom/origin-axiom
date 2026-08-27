"""Lock: the m=12 count, its control, and the off-by-one that produces 2."""
import json, math, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
R = json.loads((ROOT / "frontier/B8148_m12_settled/results.json").read_text())

def _counts(D, floor_bug=False):
    rd = math.isqrt(D); forms = set()
    for a in range(-rd - 3, rd + 4):
        if a == 0: continue
        hi = rd if not floor_bug else rd - 1          # the slip: b < floor(sqrt D)
        for b in range(1, hi + 1):
            if (b * b - D) % (4 * a): continue
            c = (b * b - D) // (4 * a)
            if b * b - 4 * a * c != D: continue
            if math.gcd(math.gcd(abs(a), abs(b)), abs(c)) != 1: continue
            if (rd - b) < 2 * abs(a) <= (rd + b): forms.add((a, b, c))
    def rho(f):
        a, b, c = f; bp = -b
        while bp <= rd - 2 * abs(c): bp += 2 * abs(c)
        while bp > rd: bp -= 2 * abs(c)
        return (c, bp, (bp * bp - D) // (4 * c))
    seen, cyc = set(), 0
    for f in sorted(forms):
        if f in seen: continue
        cyc += 1; cur = f
        for _ in range(20000):
            if cur in seen: break
            seen.add(cur); cur = rho(cur)
            if cur == f: break
    return cyc

def test_the_control_reproduces_the_banked_table():
    assert [_counts(m * m + 4) for m in range(1, 12)] == [1,1,1,1,1,2,1,1,2,2,1]

def test_m12_is_three():
    assert _counts(148) == 3
    assert R["result"]["GL2 classes"] == 3

def test_the_off_by_one_really_produces_two():
    assert _counts(148, floor_bug=True) == 2      # the slip, reproduced

def test_the_mechanism_is_offered_not_asserted_of_others():
    assert any("only that this form yields 2" in x for x in R["not_claimed"])
    assert "MY OWN first re-implementation" in R["the_likely_source_of_2"]["provenance"]

def test_codex_direction_is_not_assumed():
    assert "COMPARED, not assumed to agree" in R["status_of_codex_R010"]
