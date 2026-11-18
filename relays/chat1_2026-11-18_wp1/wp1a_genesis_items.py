#!/usr/bin/env python3
"""W-P1, step 1 (W-P1a): GENESIS's typed items, by ID and status word only. Data-free; reads one page of main's.

    python3 -I wp1a_genesis_items.py <a checkout of main>  > wp1a_genesis_items_out.txt

Condition: relays/cards/CHAT1_W-P1_STEPS_conditions.md, step 1 (committed before this script). For every table row of
GENESIS.md whose first cell is an item ID, printed: the section it sits in, the ID, and the upper-case status words of
its status cell (CHOSEN, POSTULATED, OPEN, UNEARNED, PROVED, ...). Nothing else of the page is printed; the output is
read through the mask. Controls: SE1 and SE3 POSTULATED, SE2 and FK6 CHOSEN.
"""
import pathlib
import re
import sys

text = (pathlib.Path(sys.argv[1]) / "GENESIS.md").read_text().splitlines()
sec, rows = "", []
for line in text:
    if line.startswith("## "):
        sec = line[3:].split(".")[0].strip()
    if not line.startswith("| ") or line.startswith("|---"):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    m = re.match(r"^\**([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*\d*[a-z]?)\**", cells[0])
    if not m or cells[0].startswith("ID") or len(cells) < 3:
        continue
    words = re.findall(r"\b(CHOSEN|POSTULATED|OPEN|UNEARNED|UNEARNABLE|PROVED|CONFIRMED|ANSWERED|RULED|DERIVED|"
                       r"CONDITIONAL|THEOREM|DEFINITION|FORCED|COUNTED|REFUTED|ADOPTED|AXIOM|DECIDED|TYPED)\b", cells[2])
    rows.append((sec, m.group(1), sorted(set(words), key=words.index)))
for sec, i, w in rows:
    print("%s | %s | %s" % (sec, i, " ".join(w) if w else "-"))
st = {i: w for _, i, w in rows}
print("controls: SE1 %s, SE3 %s, SE2 %s, FK6 %s" % ("POSTULATED" in st.get("SE1", []), "POSTULATED" in st.get("SE3", []),
                                                      "CHOSEN" in st.get("SE2", []), "CHOSEN" in st.get("FK6", [])))
print("rows: %d" % len(rows))
