"""B1888 lock -- the repository's public form scrutinised: what the candidate really uses, read from its code.

What could fail: the chain not reaching the measured values through the comparison half (the instrument would be blind to
how data enters); the derivation half reaching them (the separation the proposal needs would not be there); a chain as long
as the lists' upstream; or the page saying more than was measured."""
import importlib.util
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
spec = importlib.util.spec_from_file_location("candidate_chain_lock", HERE / "candidate_chain.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
RES = json.loads((HERE / "candidate_chain.json").read_text(encoding="utf-8"))


def _start():
    return sorted(r for r in m.FILES_OF_ARC[m.CANDIDATE] if r.endswith(".py") and "/referee/" not in r)


def test_the_chain_recomputed_is_the_committed_one():
    order, via = m.chain(_start())
    py = [r for r in order if r.endswith(".py")]
    assert py == RES["python"] and sorted({m.arc_of(r) for r in order if r.startswith("frontier/")}) == RES["arcs"]
    assert len(py) == 17 and RES["lines"] == 3032 and len(RES["arcs"]) == 14
    assert all((m.ROOT / r).is_file() for r in order)                 # the chain closes: every file it names is there


def test_the_comparison_half_reaches_the_measured_values_and_the_derivation_half_does_not():
    census = [r for r in _start() if r.endswith("/census.py")]
    look = [r for r in _start() if r.endswith("/look.py")]
    assert len(census) == 1 and len(look) == 1
    oc, _ = m.chain(census); ol, via = m.chain(look)
    assert m.MEASURED not in oc and m.MEASURED in ol                  # the control: the instrument sees how the data enters
    route = m.path_to(m.MEASURED, via)
    assert [r.split("/")[1].split("_")[0] for r in route] == ["B1841", "B1839", "B1741", "B1637"]
    assert sum(1 for r in oc if r.endswith(".py")) == 13 == RES["halves"]["census.py"]["python"]
    assert RES["halves"]["census.py"]["reaches_measured"] is False and RES["halves"]["look.py"]["reaches_measured"] is True
    # one file of the chain names the measured file; many in the tree do
    assert len(RES["namers_in_chain"]) == 1 and RES["namers_in_chain"][0].endswith("B1741_tau_from_the_thread_rule_the_line_free/verification/compare.py")
    assert RES["namers_in_tree"] >= 40
    # ADDED 2026-11-12 (Review 79): the page said 50 where this output says 51, and the line above could not see it.  The
    # page's number and the verdict line's are now read and held to the output.  What could fail: either stating another count.
    import re
    page = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    line = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]
    said = [int(x) for x in re.findall(r"In the whole tree (\d+) do", page)] + [int(x) for x in re.findall(r"in the archive (\d+) scripts name the file", page)]
    said += [int(x) for x in re.findall(r"that (\d+) scripts of the whole tree name", line)]
    assert len(said) == 3 and set(said) == {RES["namers_in_tree"]}, said


def test_the_chain_is_far_shorter_than_the_lists_and_inside_them():
    up, V = m.upstream_by_depends_on()
    ids = {a.split("_")[0] for a in RES["arcs"]}
    assert len(up) >= 700 and ids - {"B1841"} <= up and len(ids) == 14
    assert RES["direct_reached"] == ["B1667", "B1741", "B1753", "B1798", "B1838", "B1839"]
    assert RES["direct_not_reached"] == ["B1656", "B1728", "B1742", "B1840"]
    assert RES["copies"] == ["B1691/b1656_funcs.py", "B1723/b1656_funcs.py"]         # B1656 enters by copy


def test_the_first_fault_cannot_return():
    """a file name found in another arc is followed even when the same name exists beside the file that names it"""
    start = [r for r in _start() if r.endswith("/census.py")]
    reached = m.resolve(start[0], *m.names_in(start[0]))
    assert "frontier/B1839_the_end_card/verification/census.py" in reached and start[0] not in reached


def test_the_arc_says_what_was_measured_and_what_is_judgement():
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    # 2026-11-12 (Review 79): this asserted the sentence "It is an upper bound", which a reading showed to be wider than the measurement
    for s in ("It is an upper bound on what the code names", "It is not an upper bound on what the code opens", "as read from the code, does not reach the measured values", "does not hold as stated", "\"Not now\" stands", "A rough estimate, not a measurement", "Main is a party",
              "The agy lane's reports were not read", "## Seen first", "## Disclosed", "0 of 19"):
        assert s in f, s
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1888" and v["claim_one_line"].endswith("0 of 19.") and v["weave_or_thread"].startswith("n/a")
