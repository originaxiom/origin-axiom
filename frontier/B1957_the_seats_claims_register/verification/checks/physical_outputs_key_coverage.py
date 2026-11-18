"""B1957: which keys of the physical lane's two committed result files main's two output scripts compare, and which they do
not (the lane's finding M9-05: main's pages said 'every key', and its scripts compare selected fields).  The result files are
read as data from the lane's branch; main's two scripts are imported for the keys they return and read as text for the
keys they name.  Nothing of the lane's is run.  A key is counted COMPARED when main's script holds its value against its own
recomputation (equality, or agreement to its stated tolerance, or a stated bound); otherwise it is listed."""
import json, pathlib, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
def flat(x, p=""):
    if isinstance(x, dict):
        for k, v in x.items(): yield from flat(v, p + "/" + k)
    elif isinstance(x, list) and x and isinstance(x[0], (dict, list)):
        for i, v in enumerate(x): yield from flat(v, p + "[%d]" % i)
    else: yield p
for name in ("physical_boundary_outputs", "physical_endgame_outputs"):
    mod = __import__(name); src = (HERE / (name + ".py")).read_text()
    raw = subprocess.run(["git", "show", "%s:%s" % (mod.LANE, mod.PATH)], capture_output=True, cwd=ROOT).stdout
    if not raw: print("%s: the lane's branch is not fetched here: nothing listed" % name); continue
    data = json.loads(raw); paths = list(flat(data))
    returned = set()
    for fn in ("cells", "sectors", "cuts", "topology"):
        if hasattr(mod, fn):
            r = getattr(mod, fn)(); r = r[0] if isinstance(r, tuple) else r
            for d in (r if isinstance(r, list) else [r]):
                if isinstance(d, dict): returned |= set(d)
    named = set(re.findall(r'\["([A-Za-z0-9_/]+)"\]', src))
    leaf = lambda p: re.sub(r"\[\d+\]", "", p).split("/")[-1]; parents = lambda p: set(re.sub(r"\[\d+\]", "", p).split("/"))
    bounded = {p for p in paths if "/weil_order/" in p} if "weil_order" in src else set()
    sections = set(data.get("checks", {})) | {"checks", "cuts", "variants"}; held = (returned | named) - sections
    compared = [p for p in paths if p.startswith("/checks") and (p in bounded or (parents(p) & held and not (leaf(p) == "real" and "cusp_derivative" in p)))]
    rest = [p for p in paths if p not in compared]
    print("%s: %d leaf keys in the lane's file; held against main's recomputation: %d; not compared: %d" % (name, len(paths), len(compared), len(rest)))
    for p in rest: print("    not compared: %s" % p)
    grp = {}
    for p in compared: grp[p.split("/")[2]] = grp.get(p.split("/")[2], 0) + 1          # ADDED 2026-11-18: the compared keys by the result file's own groups (the lane's reply to M12 counts them so)
    print("    compared, by group: %s" % ", ".join("%s %d" % kv for kv in grp.items()))
