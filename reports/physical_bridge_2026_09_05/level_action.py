"""R69 exact selected D0 maps; not physical generations or a full parent domain."""
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as s
from sympy.polys.domains import QQ, QQ_I
from sympy.polys.matrices import DomainMatrix

REL = "abABaBAbaB"
LONG = "bABaaBAb"
LAM = (0, 0, 1, 3)
ALPHA = {"A": (0, 3, 2, 3), "B": (0, 1, 1, 2)}
SECTORS = {"Q": "A", "u": "A", "e": "A", "d": "B", "L": "B", "nu": "A"}


def clean(a):
    return a.applyfunc(s.expand)


def rank(a):
    """Exact complex rank, independently checked by rational realification."""
    first = DomainMatrix.from_Matrix(a).convert_to(QQ_I).rank()
    re, im = a.applyfunc(s.re), a.applyfunc(s.im)
    real = re.row_join(-im).col_join(im.row_join(re))
    second = DomainMatrix.from_Matrix(real).convert_to(QQ).rank()
    if second != 2*first:
        raise ArithmeticError("Gaussian and rational ranks disagree")
    return first


def inverse(w):
    return w.swapcase()[::-1]


def cover(n):
    if not isinstance(n, int) or not 1 <= n <= 6:
        raise ValueError("Fixed cyclic levels 1..6 only")
    gens = ("z",) + tuple("cdefgh"[:n])
    words = {"z": "a"*n}
    words.update({gens[k+1]: "a"*k+"b"+("A"*(k+1) if k<n-1 else "") for k in range(n)})

    def rewrite(w):
        sheet, out = 0, []
        for letter in w:
            previous = sheet
            sheet = (sheet + (1 if letter.islower() else -1)) % n
            if letter == "a" and previous == n-1:
                out.append("z")
            elif letter == "A" and sheet == n-1:
                out.append("Z")
            elif letter == "b":
                out.append(gens[previous+1])
            elif letter == "B":
                out.append(gens[sheet+1].upper())
        if sheet:
            raise ValueError("Word not in cyclic subgroup")
        return "".join(out)

    rels = tuple(rewrite("a"*k+REL+"A"*k) for k in range(n))
    return gens, words, rels, "z", rewrite(LONG), rewrite


class Rep:
    def __init__(self, gens, mats):
        self.gens = tuple(gens)
        self.d = mats[self.gens[0]].rows
        self.mats = {g: clean(mats[g]) for g in self.gens}
        self.mats.update({g.upper(): clean(self.mats[g].inv()) for g in self.gens})

    @lru_cache(None)
    def word(self, w):
        out = s.eye(self.d)
        for letter in w:
            out = clean(out*self.mats[letter])
        return out

    @lru_cache(None)
    def fox(self, w):
        blocks = {g: s.zeros(self.d) for g in self.gens}
        prefix = s.eye(self.d)
        for letter in w:
            if letter.islower():
                blocks[letter] += prefix
                prefix = clean(prefix*self.mats[letter])
            else:
                prefix = clean(prefix*self.mats[letter])
                blocks[letter.lower()] -= prefix
        return clean(s.Matrix.hstack(*(blocks[g] for g in self.gens)))

    def affine(self, w):
        """Propagate generator cocycles as affine matrices, independently of Fox sums."""
        cols = []
        for j in range(len(self.gens)*self.d):
            lifted = {}
            for k, g in enumerate(self.gens):
                matrix = s.eye(self.d+1)
                matrix[:self.d, :self.d] = self.mats[g]
                if k == j//self.d:
                    matrix[j % self.d, self.d] = 1
                lifted[g] = matrix
                lifted[g.upper()] = clean(matrix.inv())
            out = s.eye(self.d+1)
            for letter in w:
                out = clean(out*lifted[letter])
            cols.append(out[:self.d, self.d])
        return s.Matrix.hstack(*cols)

    def dual(self):
        return Rep(self.gens, {g: self.mats[g.upper()].T for g in self.gens})

    def valid(self, rels):
        return all(self.word(r) == s.eye(self.d) for r in rels)


def data(rep, rels, mu, longitude):
    if not rep.valid(rels):
        raise ValueError("Relator is not identity")
    d = rep.d
    d0 = s.Matrix.vstack(*(rep.mats[g]-s.eye(d) for g in rep.gens))
    d1 = s.Matrix.vstack(*(rep.fox(w) for w in rels))
    am, al = rep.word(mu)-s.eye(d), rep.word(longitude)-s.eye(d)
    if clean(am*al-al*am) != s.zeros(d):
        raise ValueError("Peripheral holonomies do not commute")
    bt = am.col_join(al)
    zt = (-al).row_join(am)
    res = rep.fox(mu).col_join(rep.fox(longitude))
    if clean(d1*d0) != s.zeros(d1.rows, d0.cols) or clean(res*d0-bt) != s.zeros(bt.rows, bt.cols):
        raise ArithmeticError("Cochain chain map failed")
    r0, r1, rb = rank(d0), rank(d1), rank(bt)
    if rank(d1.col_join(zt*res)) != r1:
        raise ArithmeticError("Restriction not a cusp cocycle")
    restriction = rank(d1.col_join(res))-r1-rb
    a1 = len(rep.gens)*d-r1-r0
    return dict(a0=d-r0, a1=a1, t0=d-rb, t1=2*d-rank(zt)-rb,
                r1=restriction, n=a1-restriction)


def index(rep, rels, mu, longitude):
    v, dual = data(rep, rels, mu, longitude), data(rep.dual(), rels, mu, longitude)
    value = v["n"]-dual["n"]
    if v["r1"]+dual["r1"] != v["t1"] or v["t1"] != dual["t1"]:
        raise ArithmeticError("Boundary annihilator identity failed")
    if value != v["a0"]-dual["a0"]+dual["t0"]-v["r1"]:
        raise ArithmeticError("Interior index identity failed")
    return value, v, dual


@lru_cache(None)
def candidates():
    gens, words, rels, mu, longitude, rewrite = cover(3)
    scalar = Rep(gens, {g: s.Matrix([[s.I**k]]) for g, k in zip(gens, LAM)})
    jac = s.Matrix.vstack(*(scalar.fox(w) for w in rels))
    boundary = s.Matrix([s.I**k-1 for k in LAM])
    coc = next(v for v in jac.nullspace() if rank(boundary.row_join(v)) == 2)
    out = {}
    for name, alpha in ALPHA.items():
        mats = {}
        for j, g in enumerate(gens):
            a, b = s.I**alpha[j], s.I**((alpha[j]-LAM[j]) % 4)
            mats[g] = s.Matrix([[a, coc[j]*b], [0, b]])
        out[name] = Rep(gens, mats)
    return out, scalar, coc, jac, boundary


def induce(rep):
    gens, words, rels, mu, longitude, rewrite = cover(3)
    mats = {}
    for g in ("a", "b"):
        matrix = s.zeros(3*rep.d)
        for i in range(3):
            j = (i+1) % 3
            matrix[j*rep.d:(j+1)*rep.d, i*rep.d:(i+1)*rep.d] = rep.word(rewrite("A"*j+g+"a"*i))
        mats[g] = matrix
    return Rep(("a", "b"), mats)


def restriction(rep, n):
    gens, words, rels, mu, longitude, rewrite = cover(n)
    out = Rep(gens, {g: rep.word(words[g]) for g in gens})
    return out, rels, mu, longitude


@lru_cache(None)
def exact_controls():
    reps, scalar, coc, jac, boundary = candidates()
    g3, w3, r3, mu3, l3, rw3 = cover(3)
    checks = {
        "cochain_dimension": len(jac.nullspace())-rank(boundary) == 1,
        "nonsplit_cocycle": rank(boundary.row_join(coc)) == 2,
        "cocycle_relations": jac*coc == s.zeros(jac.rows, 1),
        "exponent_relations": scalar.valid(r3),
        "last_generator": w3["e"] == "aab",
    }
    rows = {}
    for name, rep in reps.items():
        member = index(rep, r3, mu3, l3)
        root = induce(rep)
        counts = [index(root, (REL,), "a", LONG)[0]]
        for n in range(2, 7):
            v, rels, mu, longitude = restriction(root, n)
            counts.append(index(v, rels, mu, longitude)[0])
        g6, w6, r6, mu6, l6, rw6 = cover(6)
        pulled = Rep(g6, {g: rep.word(rw3(w6[g])) for g in g6})
        split = Rep(g3, {g: s.diag(rep.mats[g][0, 0], rep.mats[g][1, 1]) for g in g3})
        meridian = rep.word(mu3)
        checks.update({
            name+"/candidate_index": member[0] == -1,
            name+"/root_index": counts[0] == -1,
            name+"/level_counts": counts == [-1, -1, -3, -1, -1, -3],
            name+"/doublet_pullback": index(pulled, r6, mu6, l6)[0] == -1,
            name+"/split_control": index(split, r3, mu3, l3)[0] == 0,
            name+"/unipotent_meridian": meridian != s.eye(2) and (meridian-s.eye(2))**2 == s.zeros(2),
            name+"/peripheral_cube": root.word("aaa") == s.diag(*(rep.word(rw3("A"*i+"aaa"+"a"*i)) for i in range(3))),
            name+"/Fox_affine": all(rep.fox(w) == rep.affine(w) for w in r3+(mu3,l3)),
            name+"/root_Fox_affine": root.fox(REL) == root.affine(REL),
        })
        rows[name] = dict(member=member, root_counts=counts, coefficient_rank=root.d)
    deck_lams = []
    for j in range(3):
        deck_lams.append(tuple(scalar.word(rw3("a"*j+w3[g]+"A"*j))[0] for g in g3))
    ratio = tuple(s.simplify(b/a) for a,b in zip(deck_lams[0],deck_lams[1]))
    checks["three_distinct_extension_characters"] = len(set(deck_lams)) == 3
    checks["order_four_ratio"] = all(v**4 == 1 for v in ratio) and any(v**2 != 1 for v in ratio)
    return dict(checks=checks, rows=rows)


@lru_cache(None)
def source_controls():
    path = Path(__file__).parent/"received_r69/frontier/B1506_the_level/verification/the_level.py"
    spec = importlib.util.spec_from_file_location("received_level_r69", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    outcome, (p3, lam3, d0) = mod.part_f(primes=(601,))
    expected = tuple(tuple(30*x for x in ALPHA[SECTORS[n]]) for n in SECTORS)
    return dict(checks={
        "received_lambda": tuple(lam3) == tuple(30*x for x in LAM),
        "received_six_alphas": tuple(d0) == expected,
        "received_four_descents": outcome["e6_descents"] == 4,
        "received_nonlift": not outcome["lam3_square"],
        "received_level_counts": all(v == [-1,-1,-3,-1,-1,-3] for v in outcome["by_prime"][0]["root_object_counts_M1_to_M6"].values()),
    })


@lru_cache(None)
def action_controls():
    reps, *_ = candidates()
    root = induce(reps["A"])
    blocks = [s.Matrix([[1,1],[0,2]]), s.Matrix([[0,1],[-1,3]]), s.Matrix([[2,0],[1,-1]])]
    aa = s.diag(*blocks)
    bb = s.diag(*(s.Matrix([[j,2],[-1,j+1]]) for j in (1,2,3)))
    cc = s.diag(*(s.Matrix([[j,1],[1,0]]) for j in (2,3,4)))
    checks = {}
    for g in root.gens:
        t = root.mats[g]
        changed = clean(t*aa*t.inv())
        checks[g+"/sheet_algebra"] = all(changed[2*i:2*i+2,2*j:2*j+2] == s.zeros(2) for i in range(3) for j in range(3) if i != j)
        checks[g+"/products"] = clean(t*(aa*bb)*t.inv()) == clean((t*aa*t.inv())*(t*bb*t.inv()))
        h = clean(t.inv().conjugate().T*t.inv())
        v = s.Matrix([1,2,3,4,5,6])
        checks[g+"/transported_metric"] = clean((t*v).conjugate().T*h*(t*v)) == v.T*v
    t = root.mats["a"]
    v = s.Matrix([1,2,3,4,5,6])
    checks["fixed_metric_wrong"] = clean((t*v).conjugate().T*(t*v)) != v.T*v
    checks["nonzero_cubic"] = s.trace(aa*bb*cc) == sum(s.trace(aa[2*i:2*i+2,2*i:2*i+2]*bb[2*i:2*i+2,2*i:2*i+2]*cc[2*i:2*i+2,2*i:2*i+2]) for i in range(3)) != 0
    x, y = s.zeros(6), s.zeros(6)
    x[0,2], y[2,0] = 1,1
    project = lambda m: s.diag(*(m[2*i:2*i+2,2*i:2*i+2] for i in range(3)))
    checks["projection_not_Lie"] = project(x) == project(y) == s.zeros(6) and project(x*y-y*x) != s.zeros(6)
    norms = (1,4,9)
    checks["wrong_quartic_rejected"] = sum(norms)**2 != sum(a*a for a in norms)
    return dict(checks=checks, sheet_algebra_dimension=12, enlarged_algebra_dimension=36,
                nonzero_cubic=s.trace(aa*bb*cc))


@lru_cache(None)
def run():
    groups = {"exact": exact_controls(), "source": source_controls(), "action": action_controls()}
    checks = {k+"/"+n: bool(v) for k,g in groups.items() for n,v in g["checks"].items()}
    return dict(groups=groups, checks=checks, all_checks_pass=all(checks.values()),
                scope="Exact selected coefficient/index and local action maps; not physical generations, a full parent or end law")


if __name__ == "__main__":
    output = run()
    print(json.dumps(output, sort_keys=True, default=str))
    raise SystemExit(0 if output["all_checks_pass"] else 1)
