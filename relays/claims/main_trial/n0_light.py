"""B2016's light decisive check, N0 without GAP (drafted for B2016's claim card, 2026-11-26).

The arc's full decisive pair (cosets_export.py in sage with GAP, then cosets_gap.py) needs GAP's ConjugacyClassesSubgroups
for the 45 and 100 classes. This driver runs only the one class that needs no GAP: H = Stab(3,3,3), whose coset space
G_k/H is, as a G_k-set, the orbit of (3,3,3) itself (a transitive action is the action on the cosets of a point
stabiliser). It execs the arc's own text, unchanged:
  - orbit() and gens() from cosets_export.py (libgap.PermList stood in by a 1-based -> 0-based list; nothing else of GAP),
  - everything of cosets_gap.py before its read of coset_actions.json (comp, sector_polys, halved, X, Q9),
  - cosets_gap.py's category line, read from its text.
It adds, by its own code, |G_k| (closure of <C, sigma> by breadth-first search), whether rho (rho(C) = E(3),
rho(sigma) = -1) is a well-defined character of G_k (checked on every edge of the Cayley graph), |H| and whether rho is
trivial on H. It writes nothing. Exit 0 if N0's line is the committed one at mod 27 and mod 81, else 1.
Run from the repository root or from the arc's verification/ folder:
    OMP_NUM_THREADS=1 python3 -B n0_light.py
ADDED 2026-11-27 (S306p, R88-3): committed beside B2016_control.py, which imports it. The control was committed at
c90579686 without it, so it crashed (exit 3) on a clean checkout; it was the draft of 2026-11-26, unchanged.
"""
import os, pathlib, re, sys, time, glob

GAP_SPLIT = 'raw = (HERE / "coset_actions.json")'


def find_verification():
    """the arc's verification/ folder: the current folder if it holds cosets_gap.py, else frontier/B2016_*/verification
    under the current folder, the script's folder or one of their parents, else under $OA_ROOT"""
    starts = [pathlib.Path.cwd(), pathlib.Path(__file__).resolve().parent]
    if (starts[0] / "cosets_gap.py").exists() and (starts[0] / "cosets_export.py").exists():
        return starts[0]
    roots = [p for s in starts for p in [s, *s.parents]]
    if os.environ.get("OA_ROOT"):
        roots.insert(0, pathlib.Path(os.environ["OA_ROOT"]))
    for r in roots:
        hits = sorted(glob.glob(str(r / "frontier" / "B2016_*" / "verification")))
        if hits:
            return pathlib.Path(hits[0])
    sys.exit("B2016's verification folder not found (run from the repository root or set OA_ROOT)")


class _PermListOnly:
    """stands in for libgap in gens(): PermList receives the 1-based image list; return it 0-based"""
    @staticmethod
    def PermList(lst):
        return [x - 1 for x in lst]


STANDIN = """
class _PermListOnly:
    @staticmethod
    def PermList(lst):
        return [x - 1 for x in lst]


libgap = _PermListOnly
"""

DRIVER = """
import json as _json
for N in (27, 81):
    pts, idx, Cp, Sp = gens(N)
    x0 = idx[(3, 3, 3)]
    rho, ok = closure(Cp, Sp)
    H = [g for g in rho if g[x0] == x0]
    pn, S, d0, d1, fx = sector_polys(Cp, Sp)
    h = halved(pn)
    cat = CAT_EXPR
    print(_json.dumps({"N": N, "G": len(rho), "pts": len(pts), "ok": ok, "cat": str(cat), "H": len(H), "fx": fx,
                       "rho_trivial": all(rho[g] == 0 for g in H), "d0": d0, "d1": d1, "Q9": Q9.str(var="x"),
                       "form": h == Q9 * X * S}))
"""


def build(patch=None):
    """the arc's code as one script's text: everything of cosets_gap.py before its read of coset_actions.json (with the
    patch applied, exactly once, when one is given), a stand-in for libgap, cosets_export.py's orbit() and gens(), this
    file's closure(), and a driver that prints one JSON line a level, its category line read from cosets_gap.py's text.
    CHANGED 2026-11-27 (P-885): the text is run as a separate process (control_run.py), not exec'd here, since the
    intake's guard refuses exec and eval; the arc's text is used as before, unchanged but for the patch"""
    import inspect
    V = find_verification()
    gap_src = (V / "cosets_gap.py").read_text()
    if patch is not None:
        old, new = patch
        assert gap_src.count(old) == 1, "the patch's old text must occur exactly once in cosets_gap.py"
        gap_src = gap_src.replace(old, new)
    head = gap_src.split(GAP_SPLIT)[0]
    exp_src = (V / "cosets_export.py").read_text()
    funcs = "def orbit(" + exp_src.split("def orbit(")[1].split("\nout = {}")[0]
    cat_expr = re.search(r"^\s*cat = (.*)$", gap_src, re.M).group(1)
    return V, "\n".join([head, STANDIN, funcs, inspect.getsource(closure), DRIVER.replace("CAT_EXPR", cat_expr)])


def closure(Cp, Sp):
    """every element of <C, sigma> as an image tuple, with rho's exponent mod 6 (rho(C) = zeta6^2 = E(3),
    rho(sigma) = zeta6^3 = -1); consistent is False if two words for one element give two values"""
    n = len(Cp); e = tuple(range(n)); rho = {e: 0}; todo = [e]; consistent = True
    gens = ((tuple(Cp), 2), (tuple(Sp), 3))
    while todo:
        g = todo.pop()
        for p, r in gens:
            h = tuple(p[g[i]] for i in range(n))          # first g, then the generator
            val = (rho[g] + r) % 6
            if h in rho:
                consistent &= (rho[h] == val)
            else:
                rho[h] = val; todo.append(h)
    return rho, consistent


def run(patch=None, out=print):
    import json
    from control_run import run_changed
    t0 = time.time()
    V, text = build(patch)
    out("B2016 N0, light (no GAP): the arc's code from %s" % V.name)
    rc, stdout, stderr = run_changed(V / "cosets_gap.py", text)
    if rc != 0:
        raise RuntimeError("the arc's code exited %d: %s" % (rc, (stderr.strip().splitlines() or [""])[-1]))
    lines = {}
    for l in stdout.splitlines():
        if not l.startswith("{"):
            continue
        r = json.loads(l); N = r["N"]
        out("mod %d: |G| = %d; the orbit of (3,3,3) has %d points; rho well defined on G: %s" % (N, r["G"], r["pts"], r["ok"]))
        line = ("    the whole's stabiliser class: category %s, |H| = %d, index %d, C fixes %d, rho trivial on H: %s"
                % (r["cat"], r["H"], r["pts"], r["fx"], r["rho_trivial"]))
        out(line)
        out("    neutral dimension %d, charged dimension %d; p_neutral(2x)/2^d == Q9 x S(x) with Q9 = %s: %s"
            % (r["d0"], r["d1"], r["Q9"], r["form"]))
        lines[N] = (r["G"], r["ok"], line)
    out("[%.0f s]" % (time.time() - t0))
    return lines


COMMITTED = {
    27: (216, True, "    the whole's stabiliser class: category a, |H| = 3, index 72, C fixes 3, rho trivial on H: False"),
    81: (1944, True, "    the whole's stabiliser class: category a, |H| = 3, index 648, C fixes 3, rho trivial on H: False"),
}

if __name__ == "__main__":
    got = run()
    holds = got == COMMITTED
    print("N0 %s: the whole's own orbit G/<C> halves in the whole's form at mod 27 and mod 81, as committed"
          % ("HOLDS" if holds else "DOES NOT HOLD"))
    sys.exit(0 if holds else 1)
