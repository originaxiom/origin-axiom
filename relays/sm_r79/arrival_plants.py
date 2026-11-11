"""SM-R79 (M4): sentences planted against main's arrival gate as it stands at 0dda7b472, each in its own scratch tree.
Usage: arrival_plants.py GATES_PY OUT.json"""
import importlib.util, json, os, sys, tempfile
spec = importlib.util.spec_from_file_location("gates_at_head", sys.argv[1]); g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
PLANTS = [
    ("control: the bare sentence", "The Standard Model is derived.\n", "caught"),
    ("control: a denial of arrival", "No value of the Standard Model is derived here; the standard model is derived nowhere.\n", "excused"),
    ("a denial word qualifying something else", "Without a single free parameter, the Standard Model is derived.\n", None),
    ("'no longer' before a colon", "No longer a hope: the Standard Model is derived.\n", None),
    ("'not only' before the phrase", "Not only the gauge group: the standard model is derived.\n", None),
    ("an adverb inside the phrase", "With the exchange in hand, the Standard Model is now derived.\n", None),
    ("a line break inside the phrase", "With the exchange in hand, the Standard Model\nis derived.\n", None),
    ("the sentence on an arc's page", None, None),
]
out = []
for name, text, expect in PLANTS:
    d = tempfile.mkdtemp()
    if text is None:
        os.makedirs(os.path.join(d, "frontier", "B9999_plant")); open(os.path.join(d, "frontier", "B9999_plant", "FINDINGS.md"), "w").write("The Standard Model is derived.\n")
    else:
        os.makedirs(os.path.join(d, "docs")); open(os.path.join(d, "docs", "PLANT.md"), "w").write(text)
    ok, detail = g.gate_arrival_phrases(_root=d)
    out.append({"plant": name, "text": text, "gate_passes": ok, "result": "MISSED" if ok else "CAUGHT", "detail": detail[:160]})
    print(f"{name:42} {'MISSED (gate passes)' if ok else 'CAUGHT'}")
json.dump(out, open(sys.argv[2], "w"), indent=1)
