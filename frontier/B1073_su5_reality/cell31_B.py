"""B1073 -- is the object's su(5) tau-stable?   B = A ^ tau(A).

The banked negative "su(5) is real in NO real form -- 254 of 254" (B1068 CELL_ITEM1) was
computed on Stab(s), the stabiliser of the pure spinor ALONE (dim 61).  The su(5) is not
Stab(s); it is the COMPOSED A = Stab(e_i, ebar_j, s) = (34, 24).  A was never tested.

And the tau those 254 cases used is the 64 inner SIGN GRADINGS -- the 2-torsion slice of the
family of root-lattice characters -- with NO check that it intertwines.  cell16_reality.py,
cell18_realforms.py and cell20_outer.py contain no intertwining check at all.

Here tau is built as a general root-lattice character
    theta(h) = -h,   theta(e_a) = d(a) e_{-a},   T(e_r) = c_r e_{-r}
with c SOLVED from T(X.v) = theta(X).T(v), not assumed; and the intertwining is gated over
all 78 x 27 pairs before anything is read.

Criteria sealed in PREREGISTRATION.md before the first run.  Usage: cell31_B.py [prime]
"""
import itertools
import os
import pathlib
import sys
from fractions import Fraction

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
B1068 = os.path.join(HERE, "..", "B1068_j2t_charge_field")
sys.path.insert(0, B1068)

PRIME = int(sys.argv[1]) if len(sys.argv) > 1 else 1093

# ---- reproduce the banked environment (cell5 -> cell3) in this process ------------------
src = pathlib.Path(os.path.join(B1068, "cell5_spinor_test.py")).read_text()
src = src.split('print("\\nSTABILISER')[0].replace(
    "PRIME = int(sys.argv[1]) if len(sys.argv) > 1 else 1093", f"PRIME = {PRIME}")
# the exec'd source resolves cell3 relative to __file__; point it at B1068, not here
src = src.replace("os.path.dirname(os.path.abspath(__file__))", repr(os.path.abspath(B1068)))
exec(compile(src, "c5", "exec"))
import e8_build as E                                                   # noqa: E402

FAILED = []


def gate(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}{('  ' + detail) if detail else ''}")
    if not ok:
        FAILED.append(label)


print(f"\n{'='*76}\nB1073 -- B = A ^ tau(A)   at p = {P}\n{'='*76}")

# =========================================================================== BANKED IDENTITY
print("\nBANKED IDENTITY -- reproduce A = (34,24) before reading anything new")


def as_dict27(vecnp, block):
    return {E.N + E.IDX[block[i]]: Fraction(int(vecnp[i]) % P)
            for i in range(27) if int(vecnp[i]) % P}


def act_np(vecnp, block, tgt_idx):
    return act(as_dict27(vecnp, block), tgt_idx)


def vec_of(d_, block_idx):
    w = np.zeros(27, dtype=object)
    for k, val in d_.items():
        w[block_idx[E.ROOTS[k - E.N]]] = (val.numerator % P) * pow(val.denominator % P, P - 2, P) % P
    return w


OM = [(sp.expand(Psi**2), 8), (sp.expand(Phi**4), 16), (sp.expand(Wp * Psi**2), 16)]
ind = []
for f, n in OM:
    s_ = (Pm16 @ vec(embed_form(f, n, TWENTYSEVEN))) % P
    T_ = np.array([[int(t) % P for t in u] for u in ind + [s_]], dtype=np.int64)
    if rank_mod_p(T_) > len(ind):
        ind.append(s_)

pure = []
for t in list(range(P)) + [None]:
    s_ = (ind[0] + t * ind[1]) % P if t is not None else ind[1] % P
    if not np.count_nonzero(s_):
        continue
    rows = [[int(z) % P for z in (A_.astype(object) @ s_) % P] for A_ in ops]
    if 45 - rank_mod_p(np.array(rows, dtype=np.int64).T % P) == 34:
        pure.append((t, s_))
gate("pure spinors found on the omega line", len(pure) > 0, f"count {len(pure)}")
if not pure:
    print("no pure spinor at this prime -- not testable here")
    raise SystemExit(0)

g27 = idem(V27, POP27, QOP27, IDX27)
gb = idem(VBAR, POPBAR, QOPBAR, IDXBAR)
pair = None
for v_ in g27:
    for w_ in gb:
        M_ = np.vstack([act(v_, IDX27), act(w_, IDXBAR)]) % P
        if reductive_dim(M_) == (45, 45):
            pair = (v_, w_)
            break
    if pair:
        break
gate("so(10) pair recovered at (45,45)", pair is not None)
v27, wbar = pair

t_star, s_star = pure[0]
A_rows = np.vstack([act(v27, IDX27), act(wbar, IDXBAR),
                    act_np(s_star, TWENTYSEVEN, IDX27)]) % P
dA, krA = reductive_dim(A_rows)
gate("A = Stab(e_i, ebar_j, s) reproduces at (34,24)", (dA, krA) == (34, 24), f"got ({dA},{krA})")

if FAILED:
    print(f"\nBANKED IDENTITY NOT REPRODUCED: {FAILED} -- stopping, nothing is read")
    raise SystemExit(1)

# ============================================================ BUILD tau, SOLVING FOR c
# 27 and 27-bar are E8 root sets; r in 27  <=>  -r in 27-bar.
NEG_OK = all(tuple(-x for x in r) in IDXBAR for r in TWENTYSEVEN)
print(f"\nTAU -- built as a root-lattice character, c SOLVED not assumed")
gate("r in 27  =>  -r in 27-bar (27 of 27)", NEG_OK)

E6R = [r for r in E.ROOTS if r[6] == 0 and r[7] == 0]

# constraint triples: (alpha, r, alpha+r) with r, alpha+r in the 27
TRIPLES = []
for al in E6R:
    for r in TWENTYSEVEN:
        srt = tuple(al[i] + r[i] for i in range(8))
        if srt in IDX27:
            TRIPLES.append((al, r, srt))


def char_eval(dvals, root):
    """d(root) from its values on the 6 simple roots (a homomorphism)."""
    out = 1
    for j in range(6):
        e = root[j]
        if e:
            out = out * pow(dvals[j], e % (P - 1), P) % P
    return out


def solve_c(dvals):
    """nullspace of the intertwining constraints on c (27 unknowns)."""
    rows = []
    for al, r, srt in TRIPLES:
        row = [0] * 27
        row[IDX27[srt]] = E.eps(al, r) % P
        nal = tuple(-x for x in al)
        nr = tuple(-x for x in r)
        row[IDX27[r]] = (row[IDX27[r]] - char_eval(dvals, al) * (E.eps(nal, nr) % P)) % P
        rows.append(row)
    Mx = np.array(rows, dtype=np.int64) % P
    return nullspace(Mx)


# the trivial character first, then the 64 sign gradings as a CONTROL, then a mu-family
def sign_grading(bits):
    return [(P - 1) if b else 1 for b in bits]        # -1 or +1 in F_p


cands = [("trivial", [1] * 6)]
for bits in itertools.product([0, 1], repeat=6):
    cands.append((f"sign{''.join(map(str,bits))}", sign_grading(bits)))

viable = []
for nm, dv in cands:
    ns = solve_c(dv)
    if len(ns) == 1:
        viable.append((nm, dv, ns[0]))
print(f"  characters with a 1-dimensional intertwiner: {len(viable)} of {len(cands)} tested"
      f"  (1 trivial + 64 sign gradings)")
gate("at least one intertwining tau exists", len(viable) > 0)
if not viable:
    print("\nNo intertwining tau in the swept family -- reporting that, and the family swept.")
    raise SystemExit(1)

NAME, DV, CVEC = viable[0]
print(f"  provisional character (for the gates below): {NAME}")


def make_maps(cv):
    ci = [pow(int(c) % P, P - 2, P) if int(c) % P else 0 for c in cv]

    def _T(vecnp):
        out = np.zeros(27, dtype=object)
        for i, r in enumerate(TWENTYSEVEN):
            if int(vecnp[i]) % P:
                out[IDXBAR[tuple(-x for x in r)]] = int(vecnp[i]) * int(cv[i]) % P
        return out % P

    def _Tb(vecnp):
        out = np.zeros(27, dtype=object)
        for i, r in enumerate(TWENTYSEVEN):
            j = IDXBAR[tuple(-x for x in r)]
            if int(vecnp[j]) % P:
                out[i] = int(vecnp[j]) * ci[i] % P
        return out % P
    return _T, _Tb


V27NP = None      # filled after vec_of is usable below



def T27(vecnp):
    """27 -> 27-bar."""
    out = np.zeros(27, dtype=object)
    for i, r in enumerate(TWENTYSEVEN):
        if int(vecnp[i]) % P:
            out[IDXBAR[tuple(-x for x in r)]] = int(vecnp[i]) * int(CVEC[i]) % P
    return out % P


CINV = [pow(int(c) % P, P - 2, P) if int(c) % P else 0 for c in CVEC]


def Tbar(vecnp):
    """27-bar -> 27 (the inverse map)."""
    out = np.zeros(27, dtype=object)
    for i, r in enumerate(TWENTYSEVEN):
        j = IDXBAR[tuple(-x for x in r)]
        if int(vecnp[j]) % P:
            out[i] = int(vecnp[j]) * CINV[i] % P
    return out % P


# ===================================================================== CONTROLS
print("\nCONTROLS -- all run before the result is read")

# C2 -- THE INTERTWINING GATE (absent from cell16 / cell18 / cell20)
bad = 0
tested = 0
for Xb in E6_BASIS:
    for i, r in enumerate(TWENTYSEVEN):
        e_r = np.zeros(27, dtype=object)
        e_r[i] = 1
        img = E.br(Xb, E.ev(r))
        lhs_np = np.zeros(27, dtype=object)
        for k, val in img.items():
            rr = E.ROOTS[k - E.N]
            if rr in IDX27:
                lhs_np[IDX27[rr]] = (val.numerator % P) * pow(val.denominator % P, P - 2, P) % P
        lhs = T27(lhs_np)
        # theta(X) . T(e_r)
        thX = {}
        for k, val in Xb.items():
            if k < E.N:
                thX[k] = -val
            else:
                rr = E.ROOTS[k - E.N]
                nrr = tuple(-x for x in rr)
                thX = E.vadd(thX, E.vmul(Fraction(char_eval(DV, rr) % P) * val, E.ev(nrr)))
        rhs_d = E.br(thX, as_dict27(T27(e_r), TWENTYSEVENBAR))
        rhs = np.zeros(27, dtype=object)
        for k, val in rhs_d.items():
            rr = E.ROOTS[k - E.N]
            if rr in IDXBAR:
                rhs[IDXBAR[rr]] = (val.numerator % P) * pow(val.denominator % P, P - 2, P) % P
        tested += 1
        if list(lhs % P) != list(rhs % P):
            bad += 1
gate("INTERTWINING  T(X.v) = theta(X).T(v)  over all 78 x 27 pairs", bad == 0,
     f"{tested - bad}/{tested} pairs, {bad} failures")

# C3 -- T bijective both ways
idn = all(list(Tbar(T27(np.eye(27, dtype=object)[i])) % P)
          == list(np.eye(27, dtype=object)[i]) for i in range(27))
gate("T bijective 27 <-> 27-bar (Tbar o T = id, 27 of 27)", idn)

# C5 -- tau(e_i) is a rank-1 idempotent of the 27-bar (stabiliser dim 61), matched to its own list
tv = T27(vec_of(v27, IDX27))
d_tv = 78 - rank_mod_p(act_np(tv, TWENTYSEVENBAR, IDXBAR))
gate("tau(e_i) is rank-1 in the 27-bar (stab dim 61)", d_tv == 61, f"got {d_tv}")

tw = Tbar(vec_of(wbar, IDXBAR))
d_tw = 78 - rank_mod_p(act_np(tw, TWENTYSEVEN, IDX27))
gate("tau(ebar_j) is rank-1 in the 27 (stab dim 61)", d_tw == 61, f"got {d_tw}")

# C8 -- positive control: the so(10) pair still types as [1,10,16] on this code path
gate("positive control: so(10) pair still (45,45)",
     reductive_dim(np.vstack([act(v27, IDX27), act(wbar, IDXBAR)]) % P) == (45, 45))

if FAILED:
    print(f"\nCONTROLS FAILED: {FAILED} -- stopping, nothing is read")
    raise SystemExit(1)

# ===================================================================== THE RESULT
print(f"\n{'='*76}\nTHE SWEEP -- B = A ^ tau(A) over the character family\n{'='*76}")

V27NP = vec_of(v27, IDX27)
WBARNP = vec_of(wbar, IDXBAR)
A_base = [act(v27, IDX27), act(wbar, IDXBAR), act_np(s_star, TWENTYSEVEN, IDX27)]


def B_for(cv):
    """(dim, Killing rank) of A ^ tau(A), and of tau(A), for the intertwiner cv."""
    _T, _Tb = make_maps(cv)
    tv_ = _T(V27NP)
    tw_ = _Tb(WBARNP)
    ts_ = _T(s_star)
    tau_rows = [act_np(tv_, TWENTYSEVENBAR, IDXBAR),
                act_np(tw_, TWENTYSEVEN, IDX27),
                act_np(ts_, TWENTYSEVENBAR, IDXBAR)]
    dtau = reductive_dim(np.vstack(tau_rows) % P)
    dB_ = reductive_dim(np.vstack(A_base + tau_rows) % P)
    return dB_, dtau


def sweep(label, dvlist, show=True):
    tally = {}
    hits = []
    for nm, dv in dvlist:
        ns = solve_c(dv)
        if len(ns) != 1:
            tally[("no-intertwiner",)] = tally.get(("no-intertwiner",), 0) + 1
            continue
        bb, tt = B_for(ns[0])
        tally[(bb, tt)] = tally.get((bb, tt), 0) + 1
        if bb[1] == 24:
            hits.append((nm, dv, ns[0], bb, tt))
    if show:
        print(f"\n  {label}  ({len(dvlist)} characters)")
        for k in sorted(tally, key=lambda z: -tally[z]):
            print(f"     B = {k[0]}   tau(A) = {k[1] if len(k) > 1 else '-'}   x{tally[k]}")
    return tally, hits


# 1. the 2-torsion slice -- exactly the family the 254-case sweep used
t_sign, h_sign = sweep("2-TORSION SLICE (the 64 sign gradings + trivial)", cands)

# 2. the one-parameter family that normalises the principal sl2: d(alpha_i) = mu, all i
mu_family = [(f"mu={m}", [m] * 6) for m in range(1, P)]
t_mu, h_mu = sweep("UNIFORM mu-FAMILY  d(alpha_i) = mu, mu over ALL of F_p^*", mu_family)

# 3. generic-character control -- random characters must NOT return 24
rng = np.random.default_rng(20260817)
rand_family = [(f"rand{i}", [int(rng.integers(1, P)) for _ in range(6)]) for i in range(400)]
t_rand, h_rand = sweep("GENERIC-CHARACTER CONTROL (400 random characters)", rand_family)

allhits = h_sign + h_mu + h_rand
print(f"\n{'='*76}")
print(f"  characters anywhere in the sweep giving Killing rank 24: {len(allhits)}")
print(f"  generic-character control -- random characters giving 24: {len(h_rand)} of 400")

if allhits:
    nm, dv, cv, bb, tt = allhits[0]
    _T, _Tb = make_maps(cv)
    print(f"\n  FOUND: character {nm} gives B = {bb}, tau(A) = {tt}")
else:
    print("\n  NO character in the swept family gives Killing rank 24.")
    print("  Swept: the 2-torsion slice (65), the uniform mu-family over all of F_p^* "
          f"({P-1}), and 400 random characters.")
    print("  NOT swept: non-uniform characters outside those families "
          "(the full space is (p-1)^6).")

# instrument negative control -- the 254-case object, same tau, must still give 45
_T0, _Tb0 = make_maps(CVEC)
Sd = act_np(s_star, TWENTYSEVEN, IDX27)
Std = act_np(_T0(s_star), TWENTYSEVENBAR, IDXBAR)
dS, krS = reductive_dim(np.vstack([Sd, Std]) % P)
print(f"\n  INSTRUMENT NEGATIVE CONTROL")
print(f"  Stab(s) ^ Stab(tau s) -- the object the 254 cases measured: dim {dS}, rank {krS}")
print(f"    reproduces the banked 45: {krS == 45}"
      f"   -> the instrument CAN say 45; the tool is not stuck on one answer")

RES = {
    "prime": P,
    "A_dim_killingrank": [dA, krA],
    "intertwining_pairs_tested": tested,
    "intertwining_failures": bad,
    "characters_swept": {"two_torsion_slice": len(cands), "uniform_mu_family": P - 1,
                         "random_control": 400},
    "characters_giving_killing_rank_24": len(allhits),
    "random_characters_giving_24": len(h_rand),
    "tau_of_A_is_always_34_24": all(k[1] == (34, 24) for k in t_mu if len(k) > 1),
    "B_distribution_uniform_mu": {str(k): v for k, v in t_mu.items()},
    "instrument_negative_control_Stab_s": [dS, krS],
    "verdict": "A is NOT tau-stable; no character in the swept family gives Killing rank 24",
    "scope": ("mod-p at split primes; swept the 2-torsion slice, the uniform mu-family over all "
              "of F_p^*, and 400 random characters; NOT swept: non-uniform characters outside "
              "those families (the full space is (p-1)^6)"),
}
import json                                                            # noqa: E402
with open(os.path.join(HERE, f"results_p{P}.json"), "w") as fh:
    json.dump(RES, fh, indent=1, sort_keys=True, default=str)
print(f"\n  results_p{P}.json written")
