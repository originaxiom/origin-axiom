#!/usr/bin/env python3
"""B1867, part 3 -- is main's own map a line?  (data-free; reads the closure map B1858 generates and the programme B1861 generates)

The advisor seat states that the record "holds a line, not a loop": nothing computed downstream constrains anything chosen
upstream.  Main tests the statement on its own checked map, where it can be tested:

  an INPUT       is a node the programme's typed budget lists (a premise, a choice, a fitted number, an identification);
  a BACK-EDGE    would be an edge whose source is a result (a theorem, a claim, a joint, a prediction) and whose target is an
                 input, of a kind that says the result fixes, answers or selects the input.

The map's edge kinds are read from the file, each with what it asserts, and every edge into an input is listed by kind.

    python3 -B frontier/B1867_the_top_down_reading_and_the_line_or_loop_rule_scrutinised/verification/line_or_loop.py
"""
import collections
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
say = print
N = {n["id"]: n for n in json.loads((ROOT / "frontier/B1858_the_closure_map/NODES.json").read_text(encoding="utf-8"))}
E = json.loads((ROOT / "frontier/B1858_the_closure_map/EDGES.json").read_text(encoding="utf-8"))
P = json.loads((ROOT / "frontier/B1861_the_closure_programme/PROGRAMME.json").read_text(encoding="utf-8"))
inputs = sorted({m for i in P["inputs"] for m in i["members"]})
assert all(m in N for m in inputs)
layer = lambda i: int(N[i]["layer"].split()[0])

# what each edge kind asserts, src -> dst.  A kind is DETERMINING when the source fixes, answers or selects the target.
KINDS = {
    "requires":      ("the source needs the target to hold", False),
    "applies-under": ("the source is proved under the target as a premise", False),
    "instance-of":   ("the source is one case of the target, a condition of closure", False),
    "blocks":        ("the source, while open, stops the target", False),
    "blocked-by":    ("the source is stopped by the target", False),
    "bears-on":      ("the source is a note or a debt about the target", False),
    "same-as":       ("the source and the target are one item under two names", False),
    "reads":         ("the source is read through the target", False),
    "answers":       ("the source settles the target, a fork", True),
    "follows-from":  ("the source follows from the target", True),
    "candidate-for": ("the source is a candidate to be the target", True),
}
kinds = collections.Counter(e["kind"] for e in E)
assert set(kinds) <= set(KINDS), set(kinds) - set(KINDS)              # a new edge kind must be typed here before this passes
say("the map: %d nodes, %d edges, %d edge kinds; the budget's inputs on it: %d nodes" % (len(N), len(E), len(kinds), len(inputs)))
RESULT = {"theorem", "claim", "joint", "prediction", "record"}
into = collections.Counter(); det_into = []
for e in E:
    if e["dst"] in inputs:
        into[e["kind"]] += 1
        if KINDS[e["kind"]][1]: det_into.append(e)
say("edges whose target is an input, by kind: %s" % ", ".join("%s %d" % kv for kv in sorted(into.items())))
say("  of a determining kind (answers, follows-from, candidate-for): %d" % len(det_into))
det_all = [e for e in E if KINDS[e["kind"]][1]]
say("every edge of a determining kind on the map (%d):" % len(det_all))
for e in det_all:
    s, d = N[e["src"]], N[e["dst"]]
    say("  %-9s (%s, layer %d) --%s--> %-9s (%s, layer %d)%s" % (e["src"], s["kind"], layer(e["src"]), e["kind"], e["dst"], d["kind"], layer(e["dst"]),
                                                              "   [target is an input]" if e["dst"] in inputs else ""))
back = [e for e in det_all if e["dst"] in inputs and N[e["src"]]["kind"] in RESULT and layer(e["src"]) > layer(e["dst"])]
say("BACK-EDGES (a result downstream that fixes, answers or selects an input upstream): %d" % len(back))
for e in det_into:
    say("  the one determining edge into an input, %s --%s--> %s, has an input as its source too (%s, layer %d before layer %d): one choice under two names, not a result returning" % (
        e["src"], e["kind"], e["dst"], N[e["src"]]["kind"], layer(e["src"]), layer(e["dst"])))
assert all(e["src"] in inputs and layer(e["src"]) < layer(e["dst"]) for e in det_into if e not in back)   # the count itself is printed, not asserted: a built back-edge is progress
# the control: the test can see a back-edge.  Plant one and count again.
planted = E + [{"src": "W:T", "kind": "answers", "dst": "G:SE2", "grade": "", "note": "planted"}]
assert "W:T" in N and "G:SE2" in inputs and N["W:T"]["kind"] in RESULT and layer("W:T") > layer("G:SE2")
seen = [e for e in planted if KINDS[e["kind"]][1] and e["dst"] in inputs and N[e["src"]]["kind"] in RESULT and layer(e["src"]) > layer(e["dst"])]
say("control (can fail): with one planted edge 'W:T answers G:SE2' the count is %d" % len(seen))
assert len(seen) == 1
# what the inputs do have: dependents.  How many results stand on each layer's inputs.
deps = collections.Counter()
for e in E:
    if e["kind"] in ("requires", "applies-under") and e["dst"] in inputs: deps[layer(e["dst"])] += 1
say("results that require an input or are proved under one, by the input's layer: %s" % ", ".join("layer %d: %d" % kv for kv in sorted(deps.items())))
say("so on main's map the statement %s: every edge into an input is a dependence on it, and %s." % (
    ("holds as stated", "no result returns to fix one") if not back else ("no longer holds", "%d results return to fix one" % len(back))))
say("what the map cannot show: a relation the record holds in prose and the map does not carry as an edge. One is named by the advisor seat (the line must extend over the history); part 2, section C, checks it in integers.")
