#!/usr/bin/env python3
"""B1528 -- GENESIS v1.8: the checks run before GENESIS.md is written (sm:B1528; not sealed: each check reads a banked
record, re-derives a fact a record states, or compares texts).

C1  main's v1.7 is this seat's v1.6 (sm:B1526) plus exactly the changes main's B1462 lists: main's own amend.py, run on
    this branch's GENESIS.md at v1.6, reproduces main's v1.7 byte for byte, and main's received copy of v1.6 is this
    branch's file.
C2  FK12 (ii), main's [v1.7] sentence on P, at the complete point of m004 (the word state +LR, own code): the fibre's
    elliptic involution a -> A, b -> B extends to the bundle group by t -> w t for exactly one word w; it fixes rho_hyp;
    and for V = rho_hyp (x) (t -> lam), P*V ~ V* (x) (t -> lam^2). So P carries V to its dual up to a meridian sign
    exactly when lam^2 = +-1 (as at main's B1459 points), and not for a generic twist.
C3  On Ballas' family (q = 2, transported to +LR as sm:B1527's controls do): P fixes rho_q, and rho_q is not self-dual,
    so P does not carry rho_q to its dual; at q = 1 (the complete point) rho_1 is self-dual. Main's B1462 section 1 says
    P fixes rho_q; this is that, by own code, with the dual compared.
C4  Main's offered remark (its B1462 relay): sm:B1279's rotoreflections have order four and square to the period-2 swap
    (P): the composition of their cusp maps, exactly.
C5  sm:B1527 is banked as GENESIS v1.8 will cite it: its verdict, registry row and kill record.
C6  (after writing) GENESIS.md is merge_genesis_v18.py's output byte for byte, and every [v1.8] mark it adds is there.
    Before GENESIS.md is written the check reports "not yet written" and passes (the pre-write log).
Isomorphism is read from characters: two representations agree on the traces of every word up to length 4 in a, b, t
and their inverses (to 1e-40 at 60 digits), or differ on some word by more than 1e-6.
Writes genesis_v18_checks.json; prints one line per check. Usage: python3 genesis_v18_checks.py"""
import hashlib
import importlib.util
import itertools
import json
import subprocess
import sys
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ARC = HERE.parent
ROOT = ARC.parents[1]
B1527 = ROOT / "frontier" / "B1527_the_cusp_decides" / "verification"
sys.path.insert(0, str(B1527))
mp.mp.dps = 60
import cusp_lib as L  # noqa: E402  (sm:B1527's, sealed)
import family_lib as FL  # noqa: E402  (sm:B1527's, sealed)

OUT = {}


def free_reduce(w):
    out = []
    for c in w:
        if out and out[-1] == c.swapcase():
            out.pop()
        else:
            out.append(c)
    return "".join(out)


def inv(w):
    return "".join(c.swapcase() for c in reversed(w))


def apply(hom, w):
    """the image of a word under a map on generators (upper case = inverse)"""
    return "".join(hom[c] if c.islower() else inv(hom[c.lower()]) for c in w)


def words(n):
    letters = "abtABT"
    out = []
    for k in range(1, n + 1):
        for t in itertools.product(letters, repeat=k):
            w = free_reduce("".join(t))
            if len(w) == k:
                out.append(w)
    return out


WORDS = words(4)


def word_matrix(mats, w):
    X = mp.eye(mats["a"].rows)
    for c in w:
        X = X * (mats[c] if c.islower() else mp.inverse(mats[c.lower()]))
    return X


def char_gap(m1, m2):
    return max(abs(mp.fsum(word_matrix(m1, w)[i, i] for i in range(m1["a"].rows))
                   - mp.fsum(word_matrix(m2, w)[i, i] for i in range(m2["a"].rows))) for w in WORDS)


def iso(m1, m2):
    g = char_gap(m1, m2)
    if g < mp.mpf(10) ** -40:
        return True, g
    if g > mp.mpf(10) ** -6:
        return False, g
    raise AssertionError(("undecided", mp.nstr(g, 3)))


def c1():
    amend_src = subprocess.run(["git", "show", "origin/main:frontier/B1462_the_seats_harvested_p_is_the_swap_and_the_levels/"
                                "adoption/amend.py"], capture_output=True, text=True, cwd=ROOT).stdout
    assert "CHANGES = [" in amend_src
    ns = {"__file__": str(HERE / "amend.py")}       # main's module computes paths from __file__; build() is not called
    exec(compile(amend_src.split("\ndef main(")[0], "amend.py", "exec"), ns)
    v16 = subprocess.run(["git", "show", "df3f809b:GENESIS.md"], capture_output=True, cwd=ROOT).stdout
    assert hashlib.sha256(v16).hexdigest() == ns["SHA_V1_6"], "this branch's v1.6 is not the text main received"
    t = v16.decode("utf-8")
    for old, new in ns["CHANGES"]:
        assert t.count(old) == 1
        t = t.replace(old, new)
    assert t.count(ns["ACT"]) == 1
    t = t.replace(ns["ACT"], ns["ACT_PROSE"])
    main_v17 = (ARC / "received" / "GENESIS_v1_7_main.md").read_text(encoding="utf-8")
    same = t == main_v17
    assert same
    OUT["C1"] = {"main's received v1.6 = this branch's v1.6 (sha-256)": ns["SHA_V1_6"], "changes": len(ns["CHANGES"]),
                 "path relabels": 1, "v1.6 + main's changes == main's v1.7, byte for byte": same}
    print(f"C1 PASS: main's amend.py on this branch's v1.6 reproduces main's v1.7 ({len(ns['CHANGES'])} changes, 1 relabel)")


def p_extension(img):
    """the unique w with w phi(iota(g)) w^-1 = iota(phi(g)) in F2 for g = a, b (iota: a -> A, b -> B)"""
    iota = {"a": "A", "b": "B"}
    found = []
    for n in range(0, 7):
        for t in itertools.product("abAB", repeat=n):
            w = free_reduce("".join(t))
            if len(w) != n:
                continue
            ok = all(free_reduce(w + apply(img, apply(iota, g)) + inv(w)) == free_reduce(apply(iota, img[g])) for g in "ab")
            if ok:
                found.append(w)
    return found


def c2():
    G, img = FL.word_group("+", "LR")
    ws = p_extension(img)
    assert len(ws) == 1, ws
    w = ws[0]
    A2, B2, T2, _ = FL.hyperbolic_sl2("+", "LR")
    rho = {"a": A2, "b": B2, "t": T2}
    for rel in G.rels:                                  # rho_hyp is a representation of +LR's bundle group
        assert mp.mnorm(word_matrix(rho, rel) - mp.eye(2), 1) < mp.mpf(10) ** -40
    P = {"a": "A", "b": "B", "t": w + "t"}
    rhoP = {g: word_matrix(rho, P[g]) for g in "abt"}
    for rel in G.rels:                                  # P respects the relators: rho o P is a representation
        assert mp.mnorm(word_matrix(rhoP, rel) - mp.eye(2), 1) < mp.mpf(10) ** -40
    fixes, g0 = iso(rhoP, rho)
    assert fixes
    rows = []
    lams = [("1", mp.mpf(1)), ("-1", mp.mpf(-1)), ("i", mp.mpc(0, 1)), ("1.7", mp.mpf("1.7")),
            ("e^{0.9i}", mp.expj(mp.mpf("0.9"))), ("2+0.5i", mp.mpc(2, "0.5"))]
    for name, lam in lams:
        V = {"a": rho["a"], "b": rho["b"], "t": lam * rho["t"]}
        PV = {"a": rhoP["a"], "b": rhoP["b"], "t": lam * rhoP["t"]}

        def dual_tw(mu):
            return {g: (mu if g == "t" else 1) * mp.inverse(V[g]).T for g in "abt"}
        sq, gsq = iso(PV, dual_tw(lam ** 2))
        plus, _ = iso(PV, dual_tw(mp.mpf(1)))
        minus, _ = iso(PV, dual_tw(mp.mpf(-1)))
        expect_plus = abs(lam ** 2 - 1) < 1e-30
        expect_minus = abs(lam ** 2 + 1) < 1e-30
        assert sq and plus == expect_plus and minus == expect_minus, (name, sq, plus, minus)
        rows.append({"lambda": name, "P*V ~ V* (x) (t -> lambda^2)": sq, "P*V ~ V*": plus, "P*V ~ V* (x) (t -> -1)": minus})
    OUT["C2"] = {"word state": "+LR (m004)", "P": "a -> A, b -> B, t -> " + w + "t", "extension words found (length <= 6)": ws,
                 "P fixes rho_hyp": fixes, "rows": rows,
                 "reading": "P*V ~ V* (x) (t -> lambda^2): a meridian sign exactly when lambda^2 = +-1"}
    print(f"C2 PASS: P = (a -> A, b -> B, t -> {w}t), unique; fixes rho_hyp; P*V ~ V* (x) (t -> lam^2) at all six lam; "
          f"a meridian sign only at lam = 1, -1, i")
    return P


def ballas_on_LR(q):
    B = L.ballas(q)
    m, n = -B.M["m"], -B.M["n"]          # the sign of sm:B1527's lock and controls (an SL(4) lift)
    mi, ni = mp.inverse(m), mp.inverse(n)
    return {"a": n * mi, "b": m * ni * m * n * mi * mi, "t": m}


def c3(P):
    G, img = FL.word_group("+", "LR")
    out = []
    for q in (mp.mpf(2), mp.mpf(1)):
        rq = ballas_on_LR(q)
        res = max(mp.mnorm(word_matrix(rq, rel) - mp.eye(4), 1) for rel in G.rels)
        assert res < mp.mpf(10) ** -40, mp.nstr(res, 3)
        rqP = {g: word_matrix(rq, P[g]) for g in "abt"}
        fixed, _ = iso(rqP, rq)
        dual = {g: mp.inverse(rq[g]).T for g in "abt"}
        selfdual, gap = iso(rq, dual)
        to_dual, _ = iso(rqP, dual)
        out.append({"q": mp.nstr(q, 3), "relator residual": mp.nstr(res, 3), "P fixes rho_q": fixed,
                    "rho_q self-dual": selfdual, "P carries rho_q to its dual": to_dual,
                    "character gap rho_q vs rho_q*": mp.nstr(gap, 3)})
    assert out[0]["P fixes rho_q"] and not out[0]["rho_q self-dual"] and not out[0]["P carries rho_q to its dual"]
    assert out[1]["P fixes rho_q"] and out[1]["rho_q self-dual"]
    OUT["C3"] = {"rows": out}
    print(f"C3 PASS: on Ballas' family P fixes rho_q; rho_2 is not self-dual (character gap {out[0]['character gap rho_q vs rho_q*']}), "
          f"so P does not carry it to its dual; rho_1 is self-dual")


def c4():
    """sm:B1279's table: the rotoreflections act on the cusp torus (mu, lambda) as (-mu, +lambda) + (1/2, 1/4) or (1/2, 3/4);
    the period-2 swap T as identity + (0, 1/2). Affine maps of (R/Z)^2, composed exactly."""
    def compose(f, g):                      # f after g; a map is (signs, translation)
        (sf, tf), (sg, tg) = f, g
        return ((sf[0] * sg[0], sf[1] * sg[1]),
                ((sf[0] * tg[0] + tf[0]) % 1, (sf[1] * tg[1] + tf[1]) % 1))
    T = ((1, 1), (Fr(0), Fr(1, 2)))
    rows = []
    for tr in ((Fr(1, 2), Fr(1, 4)), (Fr(1, 2), Fr(3, 4))):
        R = ((-1, 1), tr)
        R2 = compose(R, R)
        R4 = compose(R2, R2)
        rows.append({"rotoreflection translation": [str(x) for x in tr], "square": str(R2), "square is T": R2 == T,
                     "fourth power is the identity": R4 == ((1, 1), (Fr(0), Fr(0)))})
        assert R2 == T and R4 == ((1, 1), (Fr(0), Fr(0)))
    txt = (ROOT / "frontier" / "B1279_the_symmetries_of_the_closing" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "| the rotoreflections (order 4) | (−, +) | (½, ¼), (½, ¾) |" in txt
    assert "| the period-2 swap T | (+, +) | (0, ½) |" in txt
    OUT["C4"] = {"rows": rows, "note": "the action on M2's torsion Z/5 is main's; sm:B1279 did not compute it"}
    print("C4 PASS: both rotoreflections square to the period-2 swap T (= P) and have order four on the cusp torus")


def c5():
    v = json.loads((ROOT / "frontier" / "B1527_the_cusp_decides" / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1527" and v["verdict"] == "PROVED"
    reg = (ROOT / "docs" / "THEOREM_REGISTRY.md").read_text(encoding="utf-8")
    assert "| T-THE-CUSP-DECIDES |" in reg
    kg = json.loads((ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json").read_text(encoding="utf-8"))
    assert [r["scope"]["reach"] for r in kg if r["id"] == "B1527"] == ["class"]
    leads = (ROOT / "docs" / "OPEN_LEADS.md").read_text(encoding="utf-8")
    assert "**Banked 2026-10-03 as sm:B1527" in leads and "9. **The eigenvalue-one locus of the infinite-volume part" in leads
    OUT["C5"] = {"verdict": v["verdict"], "registry": "T-THE-CUSP-DECIDES", "kill record reach": "class",
                 "item 9 registered": True}
    print("C5 PASS: sm:B1527 banked (PROVED; T-THE-CUSP-DECIDES; kill record, reach class); sL-10 item 9 registered")


def c6():
    g = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    if "**Version 1.8 ·" not in g:
        OUT["C6"] = {"GENESIS.md": "not yet written (v1.8 absent)"}
        print("C6 PASS: GENESIS.md not yet written (the pre-write run)")
        return
    spec = importlib.util.spec_from_file_location("merge_genesis_v18", HERE / "merge_genesis_v18.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    built = mod.build()
    assert g == built, "GENESIS.md differs from the generator's output"
    marks = g.count("**[v1.8]**")
    assert marks == 4, marks
    OUT["C6"] = {"GENESIS.md == merge_genesis_v18.build()": True, "[v1.8] marks": marks,
                 "sha-256": hashlib.sha256(g.encode("utf-8")).hexdigest()}
    print(f"C6 PASS: GENESIS.md is the generator's output byte for byte ({marks} [v1.8] marks)")


def main():
    c1()
    P = c2()
    c3(P)
    c4()
    c5()
    c6()
    (HERE / "genesis_v18_checks.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n", encoding="utf-8")
    print("ALL PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
