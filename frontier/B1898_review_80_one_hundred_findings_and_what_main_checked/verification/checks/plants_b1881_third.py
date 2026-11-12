#!/usr/bin/env python3
"""Review 80: agy-exp's five findings on B1881's lock, made again by main's own plants.

Each plant weakens B1881's script in a scratch copy of the arc so that a check can no longer fail, or its inputs are no longer
read, while the script's output stays what it was.  The lock is then run on the copy.  A plant that passes every test is a
weakening the lock does not hold.  The first entry plants nothing and must pass; the second is a plant B1895 already holds and
must be caught.  Main wrote these from the reader's descriptions through the mask and ran none of its code.  Nothing in the
repository is changed (B1895's own harness is imported for the copy and the run)."""
import importlib.util, json, pathlib, sys, time
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[1]
src = next((ROOT / "frontier").glob("B1895_*/verification/planted_reversions.py"))
spec = importlib.util.spec_from_file_location("b1895_plants", src); PR = importlib.util.module_from_spec(spec); spec.loader.exec_module(PR)
SC = "verification/whole_and_value_on_main.py"
counts = json.loads(next((ROOT / "frontier").glob("B1881_*/verification/whole_and_value_on_main.json")).read_text(encoding="utf-8"))["B_counts"]

def f1(arc):
    PR.sub(arc / SC, "mirror_ok = all(_conj_by_mirror(a, b, c5, d) == [[a, -b], [-c5, d]] and (-c5) % 5 == 0 and a * d - (-b) * (-c5) == 1 for a, b, c5, d in box)", "mirror_ok = all([])")
    PR.sub(arc / SC, "single_ok = all(abs(v - (mp.mpf(5 * m) / 2 + mp.sqrt(5) / 2)) < mp.mpf(10) ** -40 for m, v in zip(range(1, 6), single)) and all(x < y for x, y in zip(single, single[1:]))", "single_ok = all([])")
def f2(arc):
    PR.sub(arc / SC, 'def check(name, ok, detail=""):', 'def check(name, _ignored_ok, detail="", ok=True):')
def f3(arc):
    PR.sub(arc / SC, "          len(seqs) == len(lows) and abs(floor - mp.sqrt(5) / 2) < mp.mpf(10) ** -100, mp.nstr(floor, 10))",
           "          (False and (len(seqs) == len(lows) and abs(floor - mp.sqrt(5) / 2) < mp.mpf(10) ** -100)) or len(OUT) >= 1, mp.nstr(floor, 10))")
def f4(arc):
    PR.sub(arc / SC, "                lows.append(max(heights(list(seq))))", "                lows.append(mp.sqrt(5) / 2)")
    PR.sub(arc / SC, "    by_all = len({min(seq[i:] + seq[:i] for i in range(len(seq))) for seq in seqs})", "    by_all = len({min(seq[i:] + seq[:i] for i in range(len(seq))) for seq in []}) or %d" % counts["up_to_every_rotation"])
    PR.sub(arc / SC, "    by_even = len({min(seq[i:] + seq[:i] for i in range(0, len(seq), 2)) for seq in seqs})", "    by_even = len({min(seq[i:] + seq[:i] for i in range(0, len(seq), 2)) for seq in []}) or %d" % counts["up_to_rotations_that_keep_the_letters"])
def f5(arc):
    m = arc / "verification/whole_and_value_on_main_made_with.json"; d = json.loads(m.read_text(encoding="utf-8")); d["python"] = "0.0"
    m.write_text(json.dumps(d, indent=1) + "\n", encoding="utf-8")
    PR.sub(arc / SC, '"W": list(W),', '"W": [[100 + len(OUT), 101], [102, 103]],')

PLANTS = [("nothing planted", None, "passes"),
          ("the control: single_ok replaced by the literal True (a plant B1895's lock holds)", PR.p_literal_true_single, "caught"),
          ("F1: the two mended conditions taken over empty lists", f1, None),
          ("F2: check() made to ignore what it is passed", f2, None),
          ("F3: an unpinned check made unable to fail by an 'or' on a length that is never 0", f3, None),
          ("F4: no sequence read: the least typed, the two counts typed behind the pinned beginning", f4, None),
          ("F5: the made-with file given another version, and a number of part A changed in the script", f5, None)]
only = sys.argv[1:]
out = []
for name, fn, expect in PLANTS:
    if only and not any(name.startswith(o) for o in only) and expect is None: continue
    arc = PR.fresh(); t0 = time.time()
    if fn: fn(arc)
    failed, tail = PR.run(arc)
    row = {"plant": name, "tests that fail": failed, "the lock": "CATCHES IT" if failed else "PASSES", "last line": tail[:80], "seconds": round(time.time() - t0)}
    out.append(row); print("%-96s %-10s %s  (%ds)" % (name[:96], row["the lock"], tail[:60], row["seconds"]), flush=True)
json.dump(out, open(HERE / "plants_b1881_third.json", "w"), indent=1)
ok = out[0]["the lock"] == "PASSES" and out[1]["the lock"] == "CATCHES IT"
print("the two controls behave: %s; of the five plants, the lock passes: %d" % (ok, sum(1 for r in out[2:] if r["the lock"] == "PASSES")))
