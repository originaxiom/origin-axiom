#!/usr/bin/env python3
"""B869 -- G4: the false-positive control for the fused cascade.

The critic's question: does the selection principle (maximal residual symmetry among
REGISTERABLE options, B861) produce the SM from ANY start -- in which case "E6 -> SM"
carries no information about E6 -- or does the endpoint depend on the start and the
generation content, in which case the object's selection of E6 (banked elsewhere:
the fold, the atom) is load-bearing?

Method: ONE generic engine, no per-start hand-tuning. su(n) content lives in
exterior-power labels ('L', p), where conjugation is p -> n-p (Lambda^p(V)* =
Lambda^{n-p}(V) for SU(n)) and branching under s(u(k)+u(n-k)) is the uniform
Lambda^p -> sum_{a+b=p} Lambda^a (x) Lambda^b. Sym^2 labels added for the negative
control. D-type entry points (so(10), so(14), so(12), so(8)) carry hardcoded
Borel-de Siebenthal menus and spinor branch tables. u(1) charges are stripped by
construction (the registerability convention, B860/B861).

Cells:
  1. start eligibility census, rank <= 8: chiral reps exist iff -1 not in W
     (A_n n>=2, D_odd, E6 only -- B859's banked criterion, start-level).
  2. endpoint census: run the cascade from every eligible canonical-family start
     (su(5..8) with Lambda^2 + (N-4) Nbar; so(10) 16; so(14) 64; E6 27).
  3. NEGATIVE control: su(6) with the Sym^2 family (21 + 10 x 6bar, anomaly-free,
     A(Sym^2) = N+4) -- does the same rule land somewhere that is NOT the SM?

Mathematics scope; nothing to CLAIMS.md; Gate 5 untouched.
"""
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- factors & labels
# factor = ('su', n) with n >= 2, or ('so', n) opaque D-type entry.
# su labels: ('L', p) 0<=p<=n; ('S2',); ('aS2',). so labels: strings, conj by table.

SO_CONJ = {
    ('so', 10): {'16': '16bar', '16bar': '16', '10v': '10v', '1': '1'},
    ('so', 14): {'64': '64bar', '64bar': '64'},
    ('so', 12): {'32': '32', '32p': '32p', '12v': '12v', '1': '1'},   # D6: all self
    ('so', 8):  {'8v': '8v', '8s': '8s', '8c': '8c', '1': '1'},      # D4: all self
}


def canon(fac, lab):
    """Canonicalize: Lambda^n(n) = Lambda^0(n) = trivial (SAME rep, distinct
    tuples -- uncanonicalized, conj maps L0 -> Ln and manufactures spurious
    chirality out of singlets); on su(2), aS2 = S2 (adjoint, self-dual)."""
    if fac[0] == 'su':
        if lab == ('L', fac[1]):
            return ('L', 0)
        if fac[1] == 2 and lab == ('aS2',):
            return ('S2',)
    return lab


def conj_label(fac, lab):
    if fac[0] == 'su':
        n = fac[1]
        if lab == ('S2',):
            return ('S2',) if n == 2 else ('aS2',)
        if lab == ('aS2',):
            return ('S2',)
        return canon(fac, ('L', n - lab[1]))
    return SO_CONJ[fac][lab]


def conj_item(factors, item):
    return tuple(conj_label(f, l) for f, l in zip(factors, item))


def chiral(factors, content):
    """B861's criterion, verbatim: the multiset differs from its conjugate.
    Counters built FROM LISTS (the B865 lesson: no dict-literal collapse)."""
    return Counter([conj_item(factors, it) for it in content]) != Counter(content)


def dim_factor(fac):
    return fac[1] ** 2 - 1 if fac[0] == 'su' else fac[1] * (fac[1] - 1) // 2


def dim_state(factors, n_u1):
    return sum(dim_factor(f) for f in factors) + n_u1


def name_state(factors, n_u1):
    parts = sorted(f"{f[0]}({f[1]})" for f in factors)
    return " + ".join(parts + ([f"{n_u1} u(1)"] if n_u1 else [])) or f"{n_u1} u(1)"


# ---------------------------------------------------------------- su branching
def branch_su_label(lab, k, m):
    """Label on su(k+m) -> list of (label_on_su(k), label_on_su(m)) summands."""
    if lab[0] == 'L':
        p = lab[1]
        return [(('L', a), ('L', p - a)) for a in range(max(0, p - m), min(k, p) + 1)]
    if lab == ('S2',):     # Sym^2(V+W) = Sym^2 V + V(x)W + Sym^2 W
        return [(('S2',), ('L', 0)), (('L', 1), ('L', 1)), (('L', 0), ('S2',))]
    if lab == ('aS2',):    # the conjugate: V*(x)W* = Lambda^{k-1}(x)Lambda^{m-1}
        return [(('aS2',), ('L', 0)), (('L', k - 1), ('L', m - 1)), (('L', 0), ('aS2',))]
    raise ValueError(lab)


def su2_strip_mult(lab):
    """su(2) -> u(1), stripped: each label becomes dim(label) singlet copies."""
    return {('L', 0): 1, ('L', 1): 2, ('S2',): 3}[lab]


def descend_su(factors, n_u1, content, i):
    """All BdS maximal-rank descents of the su factor at index i."""
    n = factors[i][1]
    out = []
    if n == 2:
        newf = factors[:i] + factors[i + 1:]
        newc = []
        for it in content:
            for _ in range(su2_strip_mult(it[i])):
                newc.append(it[:i] + it[i + 1:])
        out.append((f"strip su(2)#{i}", newf, n_u1 + 1, newc))
        return out
    for k in range(1, n // 2 + 1):
        m = n - k
        subf = ([] if k == 1 else [('su', k)]) + [('su', m)]
        newf = factors[:i] + subf + factors[i + 1:]
        newc = []
        for it in content:
            for pk, pm in branch_su_label(it[i], k, m):
                mid = ([] if k == 1 else [canon(('su', k), pk)]) \
                    + [canon(('su', m), pm)]
                newc.append(it[:i] + tuple(mid) + it[i + 1:])
        out.append((f"su({n})->su({k})xsu({m})xu(1)@{i}" if k > 1
                    else f"su({n})->su({m})xu(1)@{i}", newf, n_u1 + 1, newc))
    return out


# ---------------------------------------------------------------- so branching
# menus: (descname, replacement factors, extra u1, {label: [replacement tuples]})
SO_MENUS = {
    ('so', 10): [
        ("so(10)->su(5)xu(1)", [('su', 5)], 1,
         {'16': [(('L', 2),), (('L', 4),), (('L', 0),)],          # 10 + 5bar + 1
          '16bar': [(('L', 3),), (('L', 1),), (('L', 5),)],
          '10v': [(('L', 1),), (('L', 4),)],                      # 5 + 5bar
          '1': [(('L', 0),)]}),
        ("so(10)->su(4)xsu(2)xsu(2) [Pati-Salam]",
         [('su', 4), ('su', 2), ('su', 2)], 0,
         {'16': [(('L', 1), ('L', 1), ('L', 0)), (('L', 3), ('L', 0), ('L', 1))],
          '16bar': [(('L', 3), ('L', 1), ('L', 0)), (('L', 1), ('L', 0), ('L', 1))],
          '10v': [(('L', 2), ('L', 0), ('L', 0)), (('L', 0), ('L', 1), ('L', 1))],
          '1': [(('L', 0), ('L', 0), ('L', 0))]}),
        ("so(10)->so(8)xu(1)", [('so', 8)], 1,
         {'16': [('8s',), ('8c',)], '16bar': [('8s',), ('8c',)],
          '10v': [('8v',), ('1',), ('1',)], '1': [('1',)]}),
    ],
    ('so', 14): [
        ("so(14)->su(7)xu(1)", [('su', 7)], 1,
         {'64': [(('L', 0),), (('L', 2),), (('L', 4),), (('L', 6),)],
          '64bar': [(('L', 1),), (('L', 3),), (('L', 5),), (('L', 7),)]}),
        ("so(14)->so(12)xu(1)", [('so', 12)], 1,
         {'64': [('32',), ('32p',)], '64bar': [('32',), ('32p',)]}),
        ("so(14)->so(10)xso(4)", [('so', 10), ('su', 2), ('su', 2)], 0,
         {'64': [('16', ('L', 1), ('L', 0)), ('16bar', ('L', 0), ('L', 1))],
          '64bar': [('16bar', ('L', 1), ('L', 0)), ('16', ('L', 0), ('L', 1))]}),
        ("so(14)->so(8)xso(6)", [('so', 8), ('su', 4)], 0,
         {'64': [('8s', ('L', 1)), ('8c', ('L', 3))],
          '64bar': [('8s', ('L', 3)), ('8c', ('L', 1))]}),
    ],
    ('so', 12): [
        ("so(12)->su(6)xu(1)", [('su', 6)], 1,
         {'32': [(('L', 0),), (('L', 2),), (('L', 4),), (('L', 6),)],
          '32p': [(('L', 1),), (('L', 3),), (('L', 5),)],
          '12v': [(('L', 1),), (('L', 5),)], '1': [(('L', 0),)]}),
    ],
    ('so', 8): [
        ("so(8)->su(4)xu(1)", [('su', 4)], 1,
         {'8v': [(('L', 1),), (('L', 3),)],
          '8s': [(('L', 0),), (('L', 2),), (('L', 4),)],
          '8c': [(('L', 1),), (('L', 3),)], '1': [(('L', 0),)]}),
    ],
}


def descend_so(factors, n_u1, content, i):
    out = []
    for descname, repl, du1, table in SO_MENUS[factors[i]]:
        newf = factors[:i] + repl + factors[i + 1:]
        newc = []
        for it in content:
            for mid in table[it[i]]:
                mid = tuple(canon(f, l) for f, l in zip(repl, mid))
                newc.append(it[:i] + mid + it[i + 1:])
        out.append((descname, newf, n_u1 + du1, newc))
    return out


# ---------------------------------------------------------------- the cascade
def all_descents(factors, n_u1, content):
    out = []
    for i, f in enumerate(factors):
        out += (descend_su if f[0] == 'su' else descend_so)(factors, n_u1, content, i)
    return out


def run_cascade(factors, n_u1, content, trace):
    """B861's rule, iterated to termination (B863's criterion): among registerable
    descents pick max total dim; stop when none is registerable."""
    while True:
        opts = []
        for descname, nf, nu, nc in all_descents(factors, n_u1, content):
            opts.append(dict(desc=descname, dim=dim_state(nf, nu),
                             registerable=chiral(nf, nc), _s=(nf, nu, nc)))
        reg = [o for o in opts if o["registerable"]]
        trace.append(dict(at=name_state(factors, n_u1),
                          menu=[{k: o[k] for k in ("desc", "dim", "registerable")}
                                for o in opts]))
        if not reg:
            return name_state(factors, n_u1)
        best = max(o["dim"] for o in reg)
        tied = [o for o in reg if o["dim"] == best]
        if len(tied) > 1:
            # ties must not silently pick a branch: require identical endpoints
            ends = {run_cascade(*o["_s"], trace=[]) for o in tied}
            if len(ends) > 1:
                return "AMBIGUOUS: " + " | ".join(sorted(ends))
            trace[-1]["tie"] = len(tied)
        factors, n_u1, content = tied[0]["_s"]


# ---------------------------------------------------------------- cell 1: eligibility
def minus_one_in_weyl(series, n):
    """-1 in W(G) <=> every rep self-conjugate <=> NO chiral generation exists.
    A_n: only n=1. B_n, C_n: always. D_n: n even. G2,F4,E7,E8: yes. E6: no."""
    return {'A': n == 1, 'B': True, 'C': True, 'D': n % 2 == 0,
            'G': True, 'F': True, 'E': n != 6}[series]


def cell1():
    algs = ([('A', n) for n in range(1, 9)] + [('B', n) for n in range(2, 9)]
            + [('C', n) for n in range(3, 9)] + [('D', n) for n in range(4, 9)]
            + [('G', 2), ('F', 4), ('E', 6), ('E', 7), ('E', 8)])
    rows = [dict(alg=f"{s}{n}", chiral_capable=not minus_one_in_weyl(s, n))
            for s, n in algs]
    return dict(rows=rows, total=len(rows),
                dead_at_step0=sum(1 for r in rows if not r["chiral_capable"]),
                eligible=[r["alg"] for r in rows if r["chiral_capable"]])


# ---------------------------------------------------------------- cell 2 starts
def georgi_family(N):
    """Lambda^2 + (N-4) Nbar: the minimal anomaly-free chiral su(N) family built
    from <=2-index reps (A(Lambda^2) = N-4, A(Nbar) = -1). Prior art: Georgi 1979."""
    return [(('L', 2),)] + [(('L', N - 1),)] * (N - 4)


def e6_entry():
    """E6's own step-1 menu (B861 banked, restated in engine labels). The engine
    cannot descend E6 itself; the menu rows are static, then the winner's state
    is handed to the engine. Sp(8): 27 -> traceless Lambda^2(8), self-dual, dead
    (B861). SU(3)_9 (dim 8) unresolved there and here; cannot win (8 < 46)."""
    menu = [
        dict(option="SO(10)xU(1)", dim=46,
             state=([('so', 10)], 1, [('16',), ('10v',), ('1',)])),
        dict(option="SU(6)xSU(2)", dim=38,
             state=([('su', 6), ('su', 2)], 0,
                    [(('L', 2), ('L', 0)), (('L', 5), ('L', 1))])),
        dict(option="SU(3)^3", dim=24,
             state=([('su', 3)] * 3, 0,
                    [(('L', 1), ('L', 2), ('L', 0)), (('L', 0), ('L', 1), ('L', 2)),
                     (('L', 2), ('L', 0), ('L', 1))])),
        dict(option="Sp(8)", dim=36, state=None, registerable=False),
    ]
    for row in menu:
        if row["state"] is not None:
            row["registerable"] = chiral(row["state"][0], row["state"][2])
    reg = [r for r in menu if r["registerable"]]
    winner = max(reg, key=lambda r: r["dim"])
    return menu, winner


def main():
    res = {"principle": "B861 verbatim: maximal residual symmetry among "
                        "REGISTERABLE options; registerable = generation chiral "
                        "with abelian factors stripped; B863 termination"}

    res["cell1"] = cell1()

    starts = {}
    for N in (5, 6, 7, 8):
        starts[f"su({N}) Georgi family"] = ([('su', N)], 0, georgi_family(N))
    starts["so(10) spinor 16"] = ([('so', 10)], 0, [('16',)])
    starts["so(14) spinor 64"] = ([('so', 14)], 0, [('64',)])
    starts["su(6) Sym2 family [NEGATIVE CONTROL]"] = (
        [('su', 6)], 0, [(('S2',),)] + [(('L', 5),)] * 10)

    cell2 = {}
    for label, (f, u, c) in starts.items():
        trace = []
        end = run_cascade(f, u, c, trace)
        cell2[label] = dict(endpoint=end, steps=[t["at"] for t in trace],
                            trace=trace)
        print(f"  {label:38} -> {end}")

    e6menu, e6win = e6_entry()
    trace = []
    e6end = run_cascade(*e6win["state"], trace=trace)
    cell2["E6 27 (via banked step-1 menu)"] = dict(
        endpoint=e6end, step1_winner=e6win["option"],
        step1_menu=[{k: r[k] for k in ("option", "dim", "registerable")}
                    for r in e6menu],
        steps=[t["at"] for t in trace], trace=trace)
    print(f"  {'E6 27 (via banked step-1 menu)':38} -> {e6end}"
          f"   [step1 winner: {e6win['option']}]")
    res["cell2"] = cell2

    sm = "su(2) + su(3)"
    def core(e):
        return " + ".join(p for p in e.split(" + ") if "u(1)" not in p)
    res["summary"] = {
        "sm_core_endpoints": sorted(k for k, v in cell2.items()
                                    if core(v["endpoint"]) == sm),
        "non_sm_endpoints": {k: v["endpoint"] for k, v in cell2.items()
                             if core(v["endpoint"]) != sm},
        "e6_chain_reproduced": [t["at"] for t in cell2[
            "E6 27 (via banked step-1 menu)"]["trace"]],
    }
    json.dump(res, open(os.path.join(HERE, "results.json"), "w"),
              indent=1, sort_keys=True, default=str)

    print()
    print(f"  eligibility: {res['cell1']['dead_at_step0']}/{res['cell1']['total']} "
          f"rank<=8 simple starts DEAD at step 0 (no chiral rep exists)")
    print(f"  eligible: {', '.join(res['cell1']['eligible'])}")
    print(f"  SM-core endpoints: {len(res['summary']['sm_core_endpoints'])}"
          f"/{len(cell2)} runs")
    for k, v in res["summary"]["non_sm_endpoints"].items():
        print(f"  NON-SM endpoint: {k} -> {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
