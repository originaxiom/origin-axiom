#!/usr/bin/env python3
"""A plumbing test of the V1 card's second stage, on PLANTED targets.  No random target of either null is drawn.

Stage 1 ran the card's counting on planted rows, one function at a time.  It never ran the second stage's own code: the
pool, the pooling of seeds, the tails, the leave-out recount, the reading, the files written.  The seat does not run
the second stage (PREREGISTRATION.md, section 10), so a fault there would be met first by main.  This test runs that
code from end to end with the generator of random targets REPLACED: where the card would draw a seed's targets, it is
given rows of the census itself, chosen evenly, each moved by a small step.

    python3 -B plumbing_test_of_stage_2.py

It imports the sealed v1_card.py unchanged and replaces, in memory only: the two lists of seeds (one planted "seed" in
place of each list), the generator, the three depths at which the tail is read (so that a few thousand planted targets
give a tail of hundreds), and the folder the outputs go to (a temporary one, so that nothing here can be taken for a
run of stage 2).  It leaves no file in this folder but its own output.

THE SEAT'S EXPECTATIONS, written before the run and committed before it:
  P0  the second stage runs to its last line on both instruments and writes both files                       85%
  P1  with targets planted evenly over the rows, every decisive cell reads B (an end is like other rows):
      the loss at each end is the layer's share of the rows, within the reading's bounds                     80%
  P2  the share of targets whose best row is found in each end layer is the share planted there,
      to within 0.007 (the card writes shares, not rows, so this is checked on the shares)                   85%
"""
import sys, json, shutil, pathlib, tempfile, importlib.util
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location("v1_card", HERE / "v1_card.py"); card = importlib.util.module_from_spec(sp)
sys.modules["v1_card"] = card; sp.loader.exec_module(card)
root = card._root()
tmp = pathlib.Path(tempfile.mkdtemp(prefix="v1_plumbing_")); shutil.copy(HERE / "v1_controls.json", tmp / "v1_controls.json")
card.HERE = tmp; card._root = lambda: root
card.QS = (0.5, 0.2, 0.05, 0.01); card.Q_LOSS = (0.2, 0.05); card.Q_DECISIVE = 0.05
N_PLANTED, STEP = 2000, 0.05
planted_at = {}
for name in card.INSTRUMENTS:
    I = card.instrument(name); n = len(I["pts"]); V = card.planted(I["A"], np.arange(n))
    card.INSTRUMENTS[name]["banked"] = [1]; card.INSTRUMENTS[name]["fresh"] = [2]

    def draws(seed, V=V, n=n, name=name):
        r = np.random.default_rng(1000 + seed); rows = r.integers(0, n, size=N_PLANTED)
        planted_at[(name, seed)] = rows
        return [V[i] + r.normal(scale=STEP, size=6) for i in rows], []
    I["C"].draws = draws
    planted_at[(name, 1)] = np.random.default_rng(1001).integers(0, n, size=N_PLANTED)       # the same rows the generator will take
    planted_at[(name, 2)] = np.random.default_rng(1002).integers(0, n, size=N_PLANTED)
lines = []


def log(x):
    print(x, flush=True); lines.append(x)
log("a plumbing test of stage 2 on planted targets: %d rows a planted seed, each moved by a step of %.2f; the tail read at %g%%" % (N_PLANTED, STEP, 100 * card.Q_DECISIVE))
ran = True
try:
    card.null(1, log)
except SystemExit as exc:
    ran = False; log("the second stage stopped: %r" % (exc,))
except Exception as exc:
    ran = False; log("the second stage raised: %r" % (exc,))
files = sorted(p.name for p in tmp.iterdir())
p0 = ran and "v1_null.json" in files and lines[-1] == "null exit 0"
log(""); log("P0  ran to its last line and wrote its files (%s): %s" % (", ".join(files), "HOLDS" if p0 else "FAILS"))
if p0:
    res = json.loads((tmp / "v1_null.json").read_text(encoding="utf-8"))
    dec = res["decisive"]; p1 = len(dec) == 3 and all(v.startswith("B") for v in dec.values())
    for k, v in dec.items(): log("      %-14s %s" % (k, v))
    log("P1  every decisive cell reads B: %s" % ("HOLDS" if p1 else "FAILS"))
    # P2 from the card's own shares: a planted target's best row lies in a layer exactly as often as rows were planted there
    worst = 0.0
    for name in card.INSTRUMENTS:
        I = card.instrument(name); rows = np.concatenate([planted_at[(name, 1)], planted_at[(name, 2)]])
        cell = res["instruments"][name]["cells"]["wf|seat"]["all_seeds"]["populations"]["all"]["share"]
        for end in ("bottom", "top"):
            want = float(np.mean(I["masks"]["%s layer 1" % end][rows])); got = cell["%s layer 1" % end]["share"]
            worst = max(worst, abs(want - got))
            log("      %s, worst factor, %-6s layer 1: planted there %.4f of the targets; best row found there %.4f" % (name, end, want, got))
    p2 = worst <= 0.05 * 0.07 + 0.0035                        # 5% of a layer's share of about 7%, allowed to move
    log("P2  the best row is found where the target was planted (greatest gap of a layer's share %.4f): %s" % (worst, "HOLDS" if p2 else "FAILS"))
shutil.rmtree(tmp, ignore_errors=True)
log("plumbing test exit 0")
(HERE / "plumbing_test_of_stage_2_out.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
