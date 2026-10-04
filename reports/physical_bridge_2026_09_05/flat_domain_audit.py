"""Exact R89 domain audit, not a new physics model or a PDE certificate."""
from __future__ import annotations

import ast
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import subprocess

import sympy as s

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
RELATOR = "aabbAbAABBaB"
X, Y = s.symbols("x y", nonzero=True)


def zero(matrix):
    return all(s.simplify(z) == 0 for z in matrix)


@lru_cache(maxsize=1)
def fox():
    """Fresh prefix derivative, without importing either old producer."""
    prefix, row = s.Integer(1), [s.Integer(0), s.Integer(0)]
    for letter in RELATOR:
        j = int(letter.lower() == "b")
        q = (X, Y)[j]
        if letter.islower():
            row[j] += prefix
            prefix *= q
        else:
            prefix /= q
            row[j] -= prefix
    return s.Matrix([[s.cancel(z) for z in row]]), s.cancel(prefix)


def data(x, y, k=3, attachment=None):
    if type(k) is not int or k < 0:
        raise ValueError("nonnegative integer source component count required")
    x, y = map(s.sympify, (x, y))
    if any(z.has(s.Float) or s.simplify(z*s.conjugate(z)-1) != 0 for z in (x, y)):
        raise ValueError("exact unitary character required")
    v = s.Matrix([x-1, y-1])
    f = fox()[0].subs({X:x, Y:y}).applyfunc(s.simplify)
    if attachment is None:
        d0 = v.col_join(s.ones(k, 1))
    else:
        t = s.Matrix(attachment)
        if t.shape != (k, k) or any(z.has(s.Float) for z in t):
            raise ValueError("exact k by k attachment required")
        d0 = v.row_join(s.zeros(2,k)).col_join(s.ones(k,1).row_join(t))
    return d0, f.row_join(s.zeros(1,k))


def betti(d0, d1):
    if not zero(d1*d0):
        raise ValueError("not a cochain complex")
    a, b = d0.rank(), d1.rank()
    return [d0.cols-a, d0.rows-a-b, d1.rows-b, 0]


def index(b):
    """Odd minus even, retaining degree zero rather than only h1-h2."""
    return sum((-1)**(j+1)*n for j, n in enumerate(b))


def complementary(d0, d1):
    """Degree reversal AND Hermitian dual; not coefficient conjugation alone."""
    dims = [d0.cols, d0.rows, d1.rows, 0]
    a, b = d0.rank(), d1.rank()
    return [0, dims[2]-b, dims[1]-a-b, dims[0]-a]


def hodge_nullities(d0, d1):
    lap = (d0.H*d0, d0*d0.H+d1.H*d1, d1*d1.H)
    return [m.rows-m.rank() for m in lap] + [0]


def green_control():
    # Exterior creation in the bit-mask basis, normal coordinate 2.
    e = s.zeros(8)
    for b in range(8):
        if not b & 4:
            e[b | 4,b] = (-1)**((b & 3).bit_count())
    c = e-e.T
    g = s.diag(c,-c)
    u = s.eye(8).col_join(s.eye(8))
    scalar = s.eye(8)[:,0]
    jump = (e*scalar).col_join(s.zeros(8,1))
    matched_scalar = scalar.col_join(scalar)
    return {"full_match_zero":zero(u.H*g*u), "rank":u.rank(),
            "annihilator":16-(u.H*g).rank(),
            "normal_jump_pairing":(jump.H*g*matched_scalar)[0]}


def pinned_source(record):
    if "ref" in record:
        raw = subprocess.check_output(["git","show",record["ref"]+":"+record["path"]],cwd=ROOT)
    else:
        raw = (ROOT/record["path"]).read_bytes()
    if hashlib.sha256(raw).hexdigest() != record["sha256"]:
        raise ValueError("source byte mismatch: "+record["path"])
    return raw


def foreign_probe():
    rec = json.loads((HERE/"FLAT_DOMAIN_INPUTS.json").read_text())["sources"][-1]
    tree = ast.parse(pinned_source(rec).decode())
    node = next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name == "evaluate")
    ns = {"json":json}
    exec(compile(ast.Module(body=[node],type_ignores=[]),"<pinned-synthetic-read-out>","exec"),ns)
    def row(hits, chunks=1):
        return {"cover":"synthetic.present", "chunk":0, "chunks":chunks, "state":"m004", "read":True,
                "hits":hits, "route P":{"reads":1,"disagree":[]},
                "route T":{"reads":len(hits),"skipped":0,"disagree":[]}}
    h = {"n":2,"zeta":[1,1],"m":2,"s":[1,6],"h1":2,"trivial cusps":0}
    hc = {"synthetic.missing":{"ez":[1,1],"m":2,"golden":True,"acts on Q8 as the identity":False}}
    ev = ns["evaluate"]
    empty_f = ev({"identity holds":True},[row([h])],[],say=lambda _:None,hcov=hc)
    incomplete = ev({"identity holds":True},[row([],chunks=2)],None,say=lambda _:None,hcov=hc)
    return {"empty_F_P8":empty_f["predictions"]["P8"],
            "empty_F_readings":empty_f["Part F"]["readings"],
            "missing_named_cover_P9":empty_f["predictions"]["P9"],
            "missing_named_cover_P10":empty_f["predictions"]["P10"],
            "incomplete_every_cover":incomplete["every cover read"],
            "incomplete_P5":incomplete["predictions"]["P5"],
            "incomplete_P6":incomplete["predictions"]["P6"]}


def run():
    results = []
    def check(name, value):
        ok = bool(value)
        results.append({"name":name,"pass":ok})
        print(json.dumps(results[-1]),flush=True)
        if not ok:
            raise AssertionError(name)
    inputs = json.loads((HERE/"FLAT_DOMAIN_INPUTS.json").read_text())
    for rec in inputs["sources"]:
        pinned_source(rec)
        check("source "+rec["path"],True)
    import snappy
    q = snappy.Manifold("m202")
    pi = q.fundamental_group()
    check("native m202 presentation",list(pi.generators()) == ["a","b"] and list(pi.relators()) == [RELATOR])
    f, end = fox()
    p = X*X*Y+X*X+X*Y*Y+X*Y+X+Y*Y+Y
    check("flat rank-one relator image",end == 1)
    check("fresh Fox row equals recorded polynomial",zero(f-s.Matrix([[-(Y-1)*p/X,(X-1)*p/X]])))
    check("Fox nilpotence",zero(f*s.Matrix([X-1,Y-1])))
    check("missing-term mutant detected",not zero((f+s.Matrix([[1,0]]))*s.Matrix([X-1,Y-1])))
    characters = [("trivial",1,1),("a sign",-1,1),("b sign",1,-1),("both signs",-1,-1),
                  ("exception",(-3+s.I*s.sqrt(7))/4,(-3+s.I*s.sqrt(7))/4)]
    rows = []
    for label,x,y in characters:
        base = betti(*data(x,y,0))
        for k in range(5):
            d0,d1 = data(x,y,k)
            b = betti(d0,d1)
            wanted = base if k == 0 else [0,k-base[0]+base[1],base[2],base[3]]
            check(f"{label} k={k} relative LES",b == wanted)
            check(f"{label} k={k} flat relative index",index(b) == k)
            check(f"{label} k={k} complement reverses index",index(complementary(d0,d1)) == -k)
            check(f"{label} k={k} coefficient conjugation alone",betti(*data(s.conjugate(x),s.conjugate(y),k)) == b)
            for t in (0,1):
                resolved = betti(*data(x,y,k,t*s.eye(k)))
                expected = [b[0]+k,*b[1:]] if t == 0 else base
                check(f"{label} k={k} attachment {t}",resolved == expected and index(resolved) == 0)
            rows.append({"character":label,"k":k,"base":base,"relative":b,"complement":complementary(d0,d1)})
        d0,d1 = data(x,y,3)
        check(label+" Hodge nullities",hodge_nullities(d0,d1) == betti(d0,d1))
    for rank in range(4):
        t = s.diag(*([1]*rank+[0]*(3-rank)))
        b = betti(*data(-1,1,3,t))
        check(f"singular attachment rank {rank}",b == [3-rank,3-rank,0,0] and index(b) == 0)
    rel = betti(*data(-1,1,3))
    res = betti(*data(-1,1,3,s.eye(3)))
    check("relative-to-resolved cannot be lossless graded equivalence",index(rel) != index(res))
    g = green_control()
    check("whole-form Green cancellation",g["full_match_zero"] and g["rank"] == g["annihilator"] == 8)
    check("tangent-only transmission mutant detected",g["normal_jump_pairing"] != 0)
    probe = foreign_probe()
    check("synthetic missing K10 cover is unresolved",probe["missing_named_cover_P9"] is None and probe["missing_named_cover_P10"] is None)
    check("synthetic empty Part F still returns P8 true",probe["empty_F_readings"] == 0 and probe["empty_F_P8"] is True)
    check("synthetic incomplete L still returns negative predicates",probe["incomplete_every_cover"] is False and probe["incomplete_P5"] is True and probe["incomplete_P6"] is True)
    out = {"checks":len(results),"passed":sum(r["pass"] for r in results),"rows":rows,
           "green":{k:str(v) for k,v in g.items()},"synthetic_foreign_diagnostic":probe,
           "physics_derived":False,"source_domain_generated":False}
    print(json.dumps(out,sort_keys=True),flush=True)
    return out


if __name__ == "__main__":
    run()
