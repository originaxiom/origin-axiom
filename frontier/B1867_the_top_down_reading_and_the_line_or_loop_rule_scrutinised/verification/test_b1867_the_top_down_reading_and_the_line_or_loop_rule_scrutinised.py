"""B1867 -- the scrutiny's facts are recomputed here with this file's own short code, and the sealed runs are what the
scripts print.  SnapPy is the judge of the law of symmetries; where it is not installed those tests are skipped, visibly."""
import itertools
import json
import pathlib
import re
import subprocess
import sys

import pytest

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SW = str.maketrans("LR", "RL")
L, R = ((1, 1), (0, 1)), ((1, 0), (1, 1))


def mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def word(w):
    M = ((1, 0), (0, 1))
    for c in w:
        M = mul(M, L if c == "L" else R)
    return M


def stab(w):
    out = []
    for rev in (0, 1):
        for sw in (0, 1):
            u = w[::-1] if rev else w
            u = u.translate(SW) if sw else u
            out += [(s, rev, sw) for s in range(len(w)) if u[s:] + u[:s] == w]
    return out


def _run(name, *args):
    r = subprocess.run([sys.executable, "-B", str(HERE / name), *args], capture_output=True, text=True, check=True, timeout=900)
    return "\n".join(l for l in r.stdout.split("\n") if "Plink" not in l and "warnings.warn" not in l)


def test_the_integer_facts_reproduce_and_are_recomputed():
    out = _run("ledger_facts.py")
    sealed = (HERE / "ledger_facts_run.txt").read_text(encoding="utf-8")
    drop = lambda s: [l for l in s.split("\n") if "SnapPy" not in l]                # that line needs SnapPy; the rest is integers
    assert drop(out) == drop(sealed)
    # recomputed here: the fixed characters, the one word with a single one, the sign, the run of 6, the level-5 congruence
    words = {min(w[s:] + w[:s] for s in range(len(w))) for n in range(2, 11) for w in ("".join(t) for t in itertools.product("LR", repeat=n)) if "L" in w and "R" in w}
    fixed = {}
    for w in words:
        M = word(w)
        d = (M[0][0] - 1) * (M[1][1] - 1) - M[0][1] * M[1][0]
        assert abs(d) == M[0][0] + M[1][1] - 2
        fixed[w] = abs(d)
        dn = (-M[0][0] - 1) * (-M[1][1] - 1) - M[0][1] * M[1][0]
        assert abs(dn) == M[0][0] + M[1][1] + 2 >= 5
    assert [w for w in words if fixed[w] == 1] == ["LR"]
    run6, gold2 = word("LLLLLLRLR"), word("LRLR")
    assert run6[0][0] + run6[1][1] == 22 and fixed["LLLLLLRLR"] == 20
    assert all((run6[i][j] - gold2[i][j]) % 5 == 0 for i in range(2) for j in range(2))
    assert any((run6[i][j] - gold2[i][j]) % 7 for i in range(2) for j in range(2))    # the control: not at level 7
    # the design's facts: LR + 1 has determinant 5 in absolute value, and four points of order 5 go to their inverse
    W = word("LR")
    assert abs((W[0][0] + 1) * (W[1][1] + 1) - W[0][1] * W[1][0]) == 5
    anti = [(x, y) for x in range(5) for y in range(5) if (x, y) != (0, 0) and ((W[0][0] * x + W[0][1] * y + x) % 5, (W[1][0] * x + W[1][1] * y + y) % 5) == (0, 0)]
    assert sorted(anti) == [(1, 2), (2, 4), (3, 1), (4, 3)]
    def sign(w):
        M = word(w)
        v = (1, 2)
        img = ((M[0][0] * v[0] + M[0][1] * v[1]) % 5, (M[1][0] * v[0] + M[1][1] * v[1]) % 5)
        return "+" if img == v else "-" if img == (4, 3) else "?"
    assert [sign("LLLLLLR" + "LR" * k) for k in (1, 2, 3)] == ["+", "-", "+"]
    assert [sign("LLRLLRLLR" + "LR" * k) for k in (1, 2, 3)] == ["-", "+", "-"]


def test_the_law_of_symmetries_on_short_words():
    snappy = pytest.importorskip("snappy")
    out = _run("word_symmetries.py", "7")
    assert re.search(r"LAW 1 \(isometries = 2 \|Stab\|\): (\d+) of \1 agree; exceptions: \[\]", out)
    for law in ("LAW 2", "LAW 4"):
        assert re.search(law + r"[^\n]*exceptions: \[\]", out), law
    # recomputed here on the seat's own rows, with this file's stabiliser and SnapPy directly
    for w, n in (("LR", 8), ("LRLR", 16), ("LRLRLR", 24), ("LLLLLLRLR", 4), ("LLRRLLRLR", 4), ("LLRLRLLRLR", 8), ("LLRRRLR", 2)):
        G = snappy.Manifold("b++" + w).symmetry_group()
        assert G.order() == n == 2 * len(stab(w)), w
        assert bool(G.is_amphicheiral()) == any(sw for (_, _, sw) in stab(w)), w
    assert len(stab("LLLLLLRLR")) == 2 and len(stab("LLRRRLR")) == 1
    assert all(sw == 0 for (_, _, sw) in stab("LLLLLLRLR")) and any(rev for (_, rev, _) in stab("LLLLLLRLR"))
    assert "LLRLRLLRLR" == "LLRLR" * 2                                               # the seat's row (2,1,1,1,2) is a word written twice
    sealed = (HERE / "word_symmetries_run.txt").read_text(encoding="utf-8")
    assert "LAW 1 (isometries = 2 |Stab|): 105 of 105 agree; exceptions: []" in sealed
    assert "LAW 4 (orientation = the swap, the base's direction = the reversal), on all 105 classes: 105 agree; exceptions: []" in sealed
    assert "the count is wrong on 22 words, and they are exactly the amphicheiral ones: True" in sealed


def test_the_census_of_the_map_counts_what_it_says():
    out = _run("line_or_loop.py")
    m = re.search(r"BACK-EDGES \(a result downstream that fixes, answers or selects an input upstream\): (\d+)", out)
    assert m and "control (can fail): with one planted edge 'W:T answers G:SE2' the count is 1" in out
    # counted again here, from the generated files, without the script
    N = {n["id"]: n for n in json.loads((ROOT / "frontier/B1858_the_closure_map/NODES.json").read_text(encoding="utf-8"))}
    E = json.loads((ROOT / "frontier/B1858_the_closure_map/EDGES.json").read_text(encoding="utf-8"))
    P = json.loads((ROOT / "frontier/B1861_the_closure_programme/PROGRAMME.json").read_text(encoding="utf-8"))
    inputs = {x for i in P["inputs"] for x in i["members"]}
    lay = lambda i: int(N[i]["layer"].split()[0])
    back = [e for e in E if e["kind"] in ("answers", "follows-from", "candidate-for") and e["dst"] in inputs
            and N[e["src"]]["kind"] in ("theorem", "claim", "joint", "prediction", "record") and lay(e["src"]) > lay(e["dst"])]
    assert int(m.group(1)) == len(back)
    sealed = (HERE / "line_or_loop_run.txt").read_text(encoding="utf-8")
    assert "BACK-EDGES (a result downstream that fixes, answers or selects an input upstream): 0" in sealed   # the dated statement of the arc


def test_the_findings_say_what_was_and_was_not_done():
    f = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("Tested, not proved on main", "Main proved and refuted no row", "This\n  arc acts on none of the thirteen", "It is not a sweep of the record", "The repo sweep:"):
        assert s in f, s
    P = json.loads((ROOT / "frontier/B1861_the_closure_programme/PROGRAMME.json").read_text(encoding="utf-8"))
    kinds = [v[0] for v in P["exits"].values()]
    assert len(kinds) == len(P["inputs"]) and set(kinds) <= set(P["exit_kinds"])
