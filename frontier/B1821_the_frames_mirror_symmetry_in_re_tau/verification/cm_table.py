"""P-449 (data-free; audit room, 2026-10-29): FR-FIB's outputs at the CM points of LR's holomorphic slice (B1804 § 4: an
invariant class (a, b, c), ac - b^2 > 0, forces tau = tau' = the root of a tau^2 - 2 b tau + c = 0, so the slice's forced points
are exactly the imaginary-quadratic tau).  Enumerated here: every reduced positive-definite form A x^2 + B xy + C y^2 of
discriminant D = B^2 - 4AC = D_K f^2 with D_K the forced pair {-3, -15} (the imaginary quadratic subfields of the compositum
Q(sqrt5, sqrt-3) the object forces; a biquadratic CM type is induced from one of them, so on LR's slice the fibre has CM by
one) and eight control fields {-4, -7, -8, -11, -19, -20, -23, -24}, |D| <= DMAX, whose root tau = (-B + sqrt D)/(2A) lies in the band
Im tau in [1.5, 6]; Re tau taken in [0, 1).  At each point the frame is evaluated on the ten lines (2/5, k/10) (closed under
tau -> tau + 1), with B1726's compute unchanged (both horocycles, both readings, all three sectors, the CKM), the record's
Higgs (DR).  No measured number is read; nothing is compared.  The table is the input of a later sealed comparison whose null
must range over every CM point of bounded discriminant (the density of CM points is the null's subject)."""
import json, math, sys, pathlib, importlib.util, contextlib, io, os
from fractions import Fraction as F
from multiprocessing import Pool
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
OUT = HERE / "cm_table.jsonl"
DMAX = int(os.environ.get("CM_DMAX", "800"))
FORCED = {-3: "Q(sqrt-3)", -15: "Q(sqrt-15)"}   # the imaginary quadratic subfields of the forced compositum Q(sqrt5, sqrt-3) (B730, B1804)
CONTROL = {-4: "Q(i)", -7: "Q(sqrt-7)", -8: "Q(sqrt-2)", -11: "Q(sqrt-11)", -19: "Q(sqrt-19)", -20: "Q(sqrt-5)", -23: "Q(sqrt-23)", -24: "Q(sqrt-6)"}
FIELDS = {**FORCED, **CONTROL}


def conductor(D):
    for DK in FIELDS:
        if D % DK == 0:
            q = D // DK
            f = int(round(math.sqrt(q)))
            if f * f == q and f >= 1: return DK, f
    return None, None


def reduced_forms(D):
    """all reduced primitive forms (A, B, C) of discriminant D < 0: |B| <= A <= C, B >= 0 if |B| == A or A == C"""
    out = []; A = 1
    while 3 * A * A <= -D:
        for B in range(-A + 1, A + 1):
            if (B * B - D) % (4 * A): continue
            C = (B * B - D) // (4 * A)
            if C < A: continue
            if (B < 0) and (A == C): continue
            if math.gcd(math.gcd(A, abs(B)), C) != 1: continue
            out.append((A, B, C))
        A += 1
    return out


def points():
    pts = []
    for absD in range(3, DMAX + 1):
        D = -absD
        if D % 4 not in (0, 1): continue
        DK, f = conductor(D)
        if DK is None: continue
        for (A, B, C) in reduced_forms(D):
            re, im = -B / (2 * A), math.sqrt(-D) / (2 * A)
            if not (1.5 <= im <= 6.0): continue
            pts.append({"D": D, "field": FIELDS[DK], "conductor": f, "form": [A, B, C], "tau": [re % 1.0, im]})
    return pts


_C = {}
def mod():
    if not _C:
        spec = importlib.util.spec_from_file_location("c26", ROOT / "frontier/B1726_the_two_ingredients_replicated/verification/census.py")
        C = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(C)
        C._modules(); _C["C"] = C
    return _C["C"]


def task(arg):
    p, k = arg
    C = mod()
    try:
        r = C.compute(p["tau"][0], p["tau"][1], F(2, 5), F(k, 10))
    except Exception as ex:
        return dict(p, line=[2 / 5, k / 10], error=repr(ex)[:200])
    return dict(p, forced=p["field"] in FORCED.values(), line=["2/5", "%d/10" % k], out=r)


if __name__ == "__main__":
    P = points()
    print("CM points in the band:", len(P), "by field:", {f: sum(1 for p in P if p["field"] == f) for f in FIELDS.values()}, flush=True)
    if len(sys.argv) > 1 and sys.argv[1] == "--list":
        for p in P: print(p)
        sys.exit(0)
    jobs = [(p, k) for p in P for k in range(10)]
    done = set()
    if OUT.exists():
        for l in OUT.read_text().splitlines():
            r = json.loads(l); done.add((tuple(r["form"]), r["line"][1]))
    jobs = [j for j in jobs if (tuple(j[0]["form"]), "%d/10" % j[1]) not in done]
    print("jobs", len(jobs), flush=True)
    with Pool(int(os.environ.get("CM_WORKERS", "2"))) as Pl, open(OUT, "a") as fh:
        for n, row in enumerate(Pl.imap_unordered(task, jobs, chunksize=1)):
            fh.write(json.dumps(row) + "\n"); fh.flush()
            if n % 50 == 0: print(n, row.get("form"), row.get("line"), flush=True)
    print("done", flush=True)
