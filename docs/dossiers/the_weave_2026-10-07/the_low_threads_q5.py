"""W97's Q5, as its rule planned: after this seat's output (d71ead0bc) was committed, chat1's sealed output (chat1/web-seat
09f41b453, the seal 0d83e6981) is read and compared, Standard Model, per-field, cell C1, every configuration and sector.

  Q5  |Delta ln(m1/m3)| and |Delta ln(m2/m3)| <= 1e-6 on every configuration accepted in both runs

Run: python3 the_low_threads_q5.py  ->  the_low_threads_q5.json beside it (reads chat1's output through git).
"""
import json
import lzma
import math
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
OUT = HERE / "the_low_threads_q5.json"
CHAT1_OUTPUT = "09f41b453"
PATH = "relays/chat1_2026-10-15_route/twisted_units/twisted_units_seal_output.json.xz"


def main():
    raw = subprocess.run(["git", "show", f"{CHAT1_OUTPUT}:{PATH}"], cwd=REPO, capture_output=True, check=True).stdout
    theirs = json.loads(lzma.decompress(raw))
    mine = json.loads((HERE / "the_low_threads_checked.json").read_text(encoding="utf-8"))
    acc = {(x["N"], x["word"], tuple(x["line"])): x["accepted"] for x in theirs["score"]["SM per configuration-cell"]
           if x["cell"] == "C1" and x["reading"] == "per-field"}
    recs = {(r["N"], r["word"], tuple(r["line"])): r for r in theirs["records"]}
    rows, worst = [], 0.0
    for r in mine["configurations"]:
        key = (r["N"], r["word"], tuple(r["line"]))
        t = recs[key]
        for sec in ("up", "down", "lepton"):
            s = t["cells"][f"SM|per-field|{sec}|C1"]["s"]
            d1 = abs(float(r["sectors"][sec]["ln m1/m3"]) - math.log(s[0] / s[2]))
            d2 = abs(float(r["sectors"][sec]["ln m2/m3"]) - math.log(s[1] / s[2]))
            worst = max(worst, d1, d2)
            rows.append({"N": r["N"], "word": r["word"], "line": r["line"], "sector": sec, "accepted by chat1": acc[key],
                         "chat1 rotation": t["rotation"], "|d ln m1/m3|": d1, "|d ln m2/m3|": d2})
    q5 = {"chat1 output": CHAT1_OUTPUT, "compared (configuration, sector)": len(rows),
          "accepted by chat1": sum(1 for x in rows if x["accepted by chat1"]), "max |Delta ln|": worst,
          "chat1's rotation differs from the word's own": sum(1 for r in mine["configurations"]
                                                            if recs[(r["N"], r["word"], tuple(r["line"]))]["rotation"]
                                                            != r["word"]),
          "holds": bool(len(rows) == 270 and worst <= 1e-6)}
    OUT.write_text(json.dumps({"Q5": q5, "rows": rows}, indent=1) + "\n")
    print(q5)


if __name__ == "__main__":
    main()
