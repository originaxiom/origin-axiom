import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k1_fullfield import run
r = run(1, 4, "dark")
json.dump(r, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "k1_14.json"), "w"), indent=1)
print("DONE", flush=True)
