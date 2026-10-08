#!/usr/bin/env python3
"""W15's prediction (W15_PREDICTION.md, committed before this ran), part 2: F-CI at tick 3 on +-LLLLLRRR (traces +-17),
with the control +-LLLLLLLR (+-9).

The instrument is W14's slope-law census (`the_slope_law.py`, function census), run unchanged. The prediction: no
generation-shaped background on either state of +-LLLLLRRR, and some on the control. Part 1 of the prediction (the
weave's own extensions on the rest of length 8) is read from `the_weave_extension.json` by the record's tests.

    python3 the_prediction_test.py   ->  the_prediction_test.json beside it
"""
import json
import sys
from multiprocessing import Pool
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_slope_law as SL  # noqa: E402

STATES = ["+LLLLLRRR", "-LLLLLRRR", "+LLLLLLLR", "-LLLLLLLR"]
PREDICTED_SILENT = {"+LLLLLRRR", "-LLLLLRRR"}

if __name__ == "__main__":
    with Pool(4) as pool:
        rows = pool.map(SL.census, STATES, chunksize=1)
    by = {r["state"]: r for r in rows}
    out = {"prediction": "W15_PREDICTION.md, item 2", "rows": by,
           "the predicted silent states carry none": all(by[s]["generation_shaped"] == 0 for s in PREDICTED_SILENT),
           "the control carries some": all(by[s]["generation_shaped"] > 0 for s in STATES if s not in PREDICTED_SILENT)}
    out["the prediction holds"] = out["the predicted silent states carry none"] and out["the control carries some"]
    with open(HERE / "the_prediction_test.json", "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != "rows"}))
