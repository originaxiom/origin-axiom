#!/usr/bin/env python3
"""THE TOWER PAST DEGREE TEN -- the one computable thing memo 229 left.

Seal: outside_bench/seals/THE_TOWER_PAST_TEN_PREREG.md
      sha256 25048f404d6fffe56a1c79c51239784ffb18ee9aa3b29da08313a8624dcf84fd

Instrument: the corpus's own (B1297's d2lib + step8), adapted ONLY in its
population -- from the census to m004's own covering tower at degrees 11-14.

THE FENCE, from the seal: there is NO live positive control in characteristic
zero anywhere in the record.  A null here is weak evidence about the tower and
strong evidence only about the instrument's standing behaviour.
"""
from __future__ import annotations

import itertools
import os
import sys
import warnings

warnings.filterwarnings("ignore")

import numpy as np
import snappy

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
import d2lib as L

TOL = 1e-7
CHAR_CAP = 400          # C5: per-manifold character cap, printed with the result
FAILURES: list[str] = []


def fail(tag, msg):
    FAILURES.append(f"{tag}: {msg}")
    print(f"  !! FAIL [{tag}] {msg}")


def rule(t):
    print("\n" + "-" * 78)
    print(t)
    print("-" * 78)


# ---------------------------------------------------------------- B1297's numerics, verbatim
def nrank(M):
    if M.size == 0:
        return 0
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s > TOL * max(1.0, s[0]))) if s.size else 0


def nnull(M):
    u, s, vh = np.linalg.svd(M)
    r = int(np.sum(s > TOL * max(1.0, s[0]))) if s.size else 0
    return vh[r:].conj().T


def sym_k(g, k):
    """Sym^k of a 2x2, same basis convention as d2lib.sym_power."""
    n = k + 1
    p, q, r, s = g[0, 0], g[0, 1], g[1, 0], g[1, 1]
    Mt = np.zeros((n, n), dtype=complex)
    for j in range(n):           # basis X^(k-j) Y^j
        # (pX+rY)^(k-j) (qX+sY)^j
        coeffs = np.zeros(n, dtype=complex)
        for a in range(k - j + 1):
            for b in range(j + 1):
                from math import comb
                c = comb(k - j, a) * comb(j, b) * (p ** a) * (r ** (k - j - a)) \
                    * (q ** b) * (s ** (j - b))
                coeffs[(k - j - a) + (j - b)] += c
        Mt[:, j] = coeffs
    return Mt


class NRep:
    def __init__(self, ims):
        self.im = {(g, 1): M for g, M in ims.items()}
        self.dim = next(iter(ims.values())).shape[0]

    def letter(self, g, e):
        if e == -1 and (g, -1) not in self.im:
            self.im[(g, -1)] = np.linalg.inv(self.im[(g, 1)])
        return self.im[(g, e)]

    def __call__(self, w):
        M = np.eye(self.dim, dtype=complex)
        for g, e in w:
            M = M @ self.letter(g, e)
        return M


def nfox(rep, word, gens):
    n = rep.dim
    D = {g: np.zeros((n, n), dtype=complex) for g in gens}
    P = np.eye(n, dtype=complex)
    for g, e in word:
        if e == 1:
            D[g] += P
            P = P @ rep.letter(g, 1)
        else:
            P = P @ rep.letter(g, -1)
            D[g] -= P
    return D


def data(gens, rels, rep, cusp_words):
    n = rep.dim
    d0 = np.block([[rep.letter(g, 1) - np.eye(n)] for g in gens])
    d1 = np.block([[nfox(rep, R, gens)[g] for g in gens] for R in rels])
    r0, r1 = nrank(d0), nrank(d1)
    a0, a1, a2 = n - r0, n * len(gens) - r1 - r0, n * len(rels) - r1
    Z1 = nnull(d1)
    Res = np.block([[nfox(rep, w, gens)[g] for g in gens] for w in cusp_words])
    m, l = rep(cusp_words[0]), rep(cusp_words[1])
    cd0 = np.vstack([m - np.eye(n), l - np.eye(n)])
    crep = NRep({"m": m, "l": l})
    cd1 = np.block([[nfox(crep, [("m", 1), ("l", 1), ("m", -1), ("l", -1)], ["m", "l"])[g]
                     for g in ["m", "l"]]])
    t0 = n - nrank(cd0); t1 = 2 * n - nrank(cd1) - nrank(cd0); t2 = n - nrank(cd1)
    rB = nrank(cd0)
    rr = nrank(np.hstack([Res @ Z1, cd0])) - rB
    return dict(a=(a0, a1, a2), t=(t0, t1, t2), r1=rr)


def index(gens, rels, mats, cusp_words):
    V = NRep(mats)
    Vd = NRep({g: np.linalg.inv(M).T for g, M in mats.items()})
    A = data(gens, rels, V, cusp_words)
    B = data(gens, rels, Vd, cusp_words)
    I = (A["a"][0] - B["a"][0]) + B["t"][0] - A["r1"]
    ids = ((A["r1"] + B["r1"] == A["t"][1])
           and (A["t"][1] == A["t"][0] + B["t"][0])
           and (A["a"][0] - A["a"][1] + A["a"][2] == 0))
    inD = (A["a"][0] == B["a"][0]) and (A["t"][0] == B["t"][0])
    return I, A, B, ids, inD


REJECT: dict[str, int] = {}


def _rej(why):
    REJECT[why] = REJECT.get(why, 0) + 1


def scan(M, name, powers=(2, 3)):
    """Return (sectors, hits, discarded_pmI, discarded_ids)."""
    divs = M.homology().elementary_divisors()
    tors = [d for d in divs if d not in (0, 1)]
    if not tors or max(tors) < 3:
        _rej("torsion < 3")
        return 0, [], 0, 0
    G = M.fundamental_group()
    gens = list(G.generators())
    rels = [L.word_from_snappy(r) for r in G.relators()]
    try:
        mer, lon = [L.word_from_snappy(w) for w in G.peripheral_curves()[0]]
        inv, cls, _V, _D, _k = L.h1_coordinates(gens, rels)
    except Exception:
        _rej("peripheral/h1_coordinates failed")
        return 0, [], 0, 0
    if sorted(inv) != sorted(divs):
        _rej("presentation H1 != SnapPy H1")
        return 0, [], 0, 0
    tor_idx = [i for i, d in enumerate(inv) if d != 0]
    mc, lc = cls(mer), cls(lon)
    try:
        mats2 = {g: np.array([[complex(G.SL2C(g)[i, j]) for j in range(2)] for i in range(2)])
                 for g in gens}
    except Exception:
        _rej("SL2C holonomy failed")
        return 0, [], 0, 0
    rho = NRep(mats2)
    # C3: the +-I trap -- odd Sym^k is valid only where relators evaluate to +I
    signs = []
    for R in rels:
        V = rho(R)
        s = None
        for cand in (1, -1):
            if np.abs(V - cand * np.eye(2)).max() < 1e-6:
                s = cand
        signs.append(s)
    if any(s is None for s in signs):
        _rej("relator not +-I (rep not PSL-faithful at tolerance)")
        return 0, [], 0, 0
    plus_I = all(s == 1 for s in signs)

    _rej("REACHED the character loop")
    sectors = 0; hits = []; disc_pm = 0; disc_ids = 0
    ranges = [range(inv[i]) if i in tor_idx else range(1) for i in range(len(inv))]
    seen = set(); count = 0
    for expo in itertools.product(*ranges):
        if count >= CHAR_CAP:
            break
        if all(e == 0 for e in expo):
            continue
        if all((2 * e) % inv[i] == 0 for i, e in enumerate(expo) if i in tor_idx):
            continue                                       # chi^2 = 1: self-dual
        def chi_val(c):
            return np.exp(2j * np.pi * sum((e * c[i]) / inv[i]
                                           for i, e in enumerate(expo) if i in tor_idx))
        if abs(chi_val(mc) - 1) > 1e-9 or abs(chi_val(lc) - 1) > 1e-9:
            continue                                       # not cusp-trivial
        inv_expo = tuple((-e) % inv[i] if i in tor_idx else 0 for i, e in enumerate(expo))
        if inv_expo in seen:
            continue
        seen.add(expo); count += 1
        for k in powers:
            if k % 2 == 1 and not plus_I:
                disc_pm += 1
                continue                                   # C3
            mats = {g: sym_k(mats2[g], k) * chi_val(cls([(g, 1)])) for g in gens}
            try:
                I, A, B, ids, inD = index(gens, rels, mats, [mer, lon])
            except Exception:
                continue
            if not ids:
                disc_ids += 1
                continue                                   # C4
            sectors += 1
            if I != 0 and inD:
                hits.append((name, str(divs), expo, k, I, A, B))
    return sectors, hits, disc_pm, disc_ids


def main() -> int:
    print("=" * 78)
    print(" THE TOWER PAST DEGREE TEN")
    print("=" * 78)

    # ------------------------------------------------------------ C1
    rule("CONTROL C1 -- ALGEBRAIC NON-VACUITY: can this code return a nonzero at all?")
    print("""
    B1297's own MB12 established non-vacuity on RANDOM presentations.  If the
    instrument cannot return I != 0 in characteristic zero here, CELL 1 is VOID
    and its null means nothing.""")
    rng = np.random.default_rng(20260914)
    nz = 0; tried = 0
    for _ in range(40):
        gens = ["a", "b"]
        A0 = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        B0 = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        A0 /= np.sqrt(np.linalg.det(A0)); B0 /= np.sqrt(np.linalg.det(B0))
        rels = [L.word_from_snappy("abAB")]
        mats = {"a": sym_k(A0, 2), "b": sym_k(B0, 2)}
        try:
            I, _A, _B, _ids, _inD = index(gens, rels, mats,
                                          [L.word_from_snappy("a"), L.word_from_snappy("b")])
        except Exception:
            continue
        tried += 1
        if I != 0:
            nz += 1
    print(f"    random presentations: {tried} evaluated, I != 0 in {nz}")
    c1 = nz > 0
    print(f"  C1: {'PASS' if c1 else 'FAIL'} -- the instrument CAN return a nonzero in char 0")
    if not c1:
        fail("C1", "the instrument never returned a nonzero -- CELL 1 is VOID")

    # ------------------------------------------------------------ C2
    rule("CONTROL C2 -- reproduce the record on the census before touching new ground")
    csec = 0; chits = []
    n_done = 0
    for M in snappy.OrientableCuspedCensus:
        if M.num_cusps() != 1:
            continue
        s, h, _p, _i = scan(M, M.name(), powers=(2,))
        if s:
            csec += s; chits += h; n_done += 1
        if n_done >= 12:
            break
    print(f"    {n_done} census manifolds, {csec} in-domain sectors, nonzero: {len(chits)}")
    c2 = (len(chits) == 0 and csec > 0)
    print(f"  C2: {'PASS' if c2 else 'FAIL'} -- all-zero on the census, as banked")
    if not c2:
        fail("C2", "the adaptation does not reproduce the banked census result")

    # ------------------------------------------------------------ CELL 1
    REJECT.clear()          # C2's census pass must not contaminate the tower's accounting
    rule("CELL 1 -- the object's own tower, degrees 11-14, one-cusped, torsion >= 3")
    print(f"    character cap per manifold (C5): {CHAR_CAP}")
    print("\n    deg  covers  scanned  sectors  nonzero  +-I discarded  ids discarded")
    tot_s = tot_h = tot_p = tot_i = 0
    allhits = []
    base = snappy.Manifold("m004")
    for d in (11, 12, 13, 14):
        ns = nh = npm = nid = 0; nscan = 0
        covs = base.covers(d)
        for C in covs:
            if C.num_cusps() != 1:
                continue
            s, h, p, i = scan(C, f"cov{d}", powers=(2, 3))
            if s or p or i:
                nscan += 1
            ns += s; nh += len(h); npm += p; nid += i
            allhits += h
        print(f"    {d:<4} {len(covs):<7} {nscan:<8} {ns:<8} {nh:<8} {npm:<14} {nid}")
        tot_s += ns; tot_h += nh; tot_p += npm; tot_i += nid
    print(f"    ---  {'':<7} {'':<8} {tot_s:<8} {tot_h:<8} {tot_p:<14} {tot_i}")
    reached = REJECT.pop("REACHED the character loop", 0)
    print("\n    COVERAGE, stated rather than implied:")
    print(f"      {reached:>4}  covers REACHED the character loop")
    for why, n in sorted(REJECT.items(), key=lambda kv: -kv[1]):
        print(f"      {n:>4}  rejected: {why}")
    produced = sum(1 for _ in [1]) # placeholder replaced below
    print(f"\n      Of the {reached} that reached it, only those with a cusp-trivial")
    print(f"      character of order > 2 inside the cap produce ANY sector at all.")
    print(f"      TOTAL IN-DOMAIN SECTORS EXAMINED ON THE TOWER: {tot_s}")
    print(f"    The preregistered population was 47 one-cusped covers with torsion >= 3.")
    print(f"    THE NULL COVERS THE SECTORS ABOVE -- NOT ALL 47 COVERS.")

    cell1 = "A" if tot_h > 0 else "B"
    if allhits:
        print("\n    NONZERO INDICES FOUND:")
        for h in allhits[:20]:
            print(f"      {h[0]} H1={h[1]} chi={h[2]} Sym^{h[3]}  I = {h[4]}")
    print(f"""
  >>> CELL 1 OUTCOME {cell1}.""")
    if cell1 == "B":
        print("""      Every in-domain sector on the tower past degree 10 returns I = 0.

      AND THE SEAL'S FENCE BINDS HOW THIS IS READ: there is NO live positive
      control in characteristic zero anywhere in the record -- B1297's own MB12
      says "live non-vacuity NOT established", and B1335's nonzero index is over
      F_p with its own title reading "and its refutation in characteristic zero".
      So this null is WEAK evidence about the tower and STRONG evidence only
      about the instrument's standing behaviour.  IT IS NOT "THE TOWER IS
      VECTOR-LIKE".""")
    else:
        print("""      A nonzero index in characteristic zero on a real manifold -- the first
      in the record.  Every hit above passed the four identities and sits in
      domain D.  THIS NEEDS INDEPENDENT RE-VERIFICATION BEFORE ANY READING.""")

    print("\n" + "=" * 78)
    print(" OUTCOMES")
    print("=" * 78)
    print(f"   CELL 1 (nonzero on the tower past 10) : {cell1}")
    print(f"   C1 algebraic non-vacuity : {'PASS' if c1 else 'FAIL'}")
    print(f"   C2 census reproduced     : {'PASS' if c2 else 'FAIL'}")
    print(f"   C3 +-I trap guarded      : {tot_p} odd-power sectors discarded")
    print(f"   C4 identities            : {tot_i} sectors discarded")
    print(f"   C5 character cap         : {CHAR_CAP} per manifold")
    if FAILURES:
        print("\n  FAILURES:")
        for f in FAILURES:
            print(f"    - {f}")
    print("=" * 78)
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
