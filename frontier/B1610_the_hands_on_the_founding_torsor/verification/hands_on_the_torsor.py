#!/usr/bin/env python3
"""B1610 -- THE HANDS ON THE FOUNDING TORSOR.  B1083: the four Fibonacci-type rules are one free transitive K4-orbit under
swap-conjugation (C, by P: a <-> b) and reversal-conjugation (by iota: a -> a^-1, b -> b^-1, which reverses the images);
the arrow (the rule against its inverse) is not on the torsor -- it is forced by the monoid's non-surjectivity.  B1607
located two hands: (i) the records' orientation (on W21's space V: T, the Q-positive holomorphic triplet, against
T-bar) and (ii) the McKay orientation (the cyclic order of the three parities; at the common point the 2T-class of the
order-6 lift).  This instrument reads both hands on each orbit rule and on the inverse rule, exactly where possible:

 H0  the orbit: the four rules, closed under C and the reversal, size 4, all positive (B1083, re-derived).
 H1  hand (ii) of each rule rho: the sense of its 3-cycle on the parities; the 2T-class of its order-6 lift at the
     quaternion point; the same for its double tick rho^2.
 H2  hand (i) of each rule: the action of rho's lift on V (W10's move_matrix) -- whether it keeps or reverses W21's
     Hodge-Riemann form Q -- and of its double tick rho^2: the eigenvalues of rho^2 on T (the Q-positive piece of V
     under <L, R>) and on T-bar.
 H3  the ledger: for each torsor operation (C, the reversal, C and the reversal) and for the arrow (rho -> rho^-1), which
     hand it flips; whether, with the arrow fixed, both hands are functions of C alone; whether the pair (hand (i),
     hand (ii)) of a double tick is the same for every rule (the relative hand).
`python3 hands_on_the_torsor.py --controls` reproduces banked numbers only (W21: L, R, sign keep Q, the swap reverses it;
signature (3, 3); B1607: sigma's lift (1 - i - j - k)/2, sense backward).  Writes hands_on_the_torsor.json."""
import json, pathlib, itertools, io, contextlib, sys, os
from unittest import mock
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = pathlib.Path(os.environ.get("OA_FRONTIER", HERE.parents[1]))
sys.path.insert(0, str(FRONTIER / "B1600_the_weave_verified" / "verification"))
import builtins
_real_open = builtins.open
def _guarded_open(file, mode="r", *a, **k):
    """W10's module writes its banked json on import with open(..., "w"), which truncates before anything is dumped:
    that one write goes to the null device, so B1600's banked file is never opened for writing"""
    if any(c in mode for c in "wax") and str(file).endswith("w10_check.json"):
        return _real_open(os.devnull, mode, *a, **k)
    return _real_open(file, mode, *a, **k)
with contextlib.redirect_stdout(io.StringIO()), mock.patch("builtins.open", _guarded_open):
    import w10_check as W
I2 = np.eye(2, dtype=complex); PAR = W.PAR; qi, qj = W.qi, W.qj; qk = qi @ qj


# ---- W21's Hodge-Riemann form on V (the same construction as B1600/verification/w21_check.py, re-entered here)
def rep_letter(c, p):
    g = W.rho[c.lower()] * W.chi(p, c.lower())
    return g if c.islower() else np.linalg.inv(g)


def cocycle_on_word(z, word, p):
    val = np.zeros(2, dtype=complex); M = I2.copy()
    for c in word:
        if c.islower():
            val = val + M @ z[c]; M = M @ rep_letter(c, p)
        else:
            Mi = rep_letter(c, p); val = val + M @ (-(Mi @ z[c.lower()])); M = M @ Mi
    return val


def cup(u, v, p, relator="abABabAB"):
    B = lambda x, y: np.vdot(y, x)
    total = 0; prefix = ""; M = I2.copy()
    for c in relator:
        total += B(cocycle_on_word(u, prefix, p), M @ cocycle_on_word(v, c, p))
        if c.isupper():
            total -= B(cocycle_on_word(u, c.lower(), p), rep_letter(c.lower(), p) @ cocycle_on_word(v, c, p))
        prefix += c; M = M @ rep_letter(c, p)
    return total


def cup_trivial(u, v, relator="abABabAB"):
    val = lambda z, w: sum((z[c] if c.islower() else -z[c.lower()]) for c in w)
    total = 0; prefix = ""
    for c in relator:
        total += val(u, prefix) * np.conj(val(v, c))
        if c.isupper():
            total -= val(u, c.lower()) * np.conj(val(v, c))
        prefix += c
    return total


tau = 0.3 + 1.1j; SIGN = 1 if (1j * cup_trivial({"a": 1.0, "b": tau}, {"a": 1.0, "b": tau})).real > 0 else -1
basis = [(p, {"a": W.BASES[p][0][:, k][:2], "b": W.BASES[p][0][:, k][2:]}) for p in PAR for k in range(2)]
Qm = np.zeros((6, 6), dtype=complex)
for i, (p, zi) in enumerate(basis):
    for j, (q, zj) in enumerate(basis):
        if p == q: Qm[i, j] = SIGN * 1j * cup(zi, zj, p)
Hm = Qm.conj()


def form_action(M):
    keeps = bool(np.allclose(M.conj().T @ Hm @ M, Hm, atol=1e-8)); rev = bool(np.allclose(M.conj().T @ Hm @ M, -Hm, atol=1e-8))
    return "keeps" if keeps else ("reverses" if rev else "neither")


# T and T-bar: the Q-definite isotypic pieces of V under <L, R>
G_LR = W.G_LR
Mx = np.vstack([np.kron(np.eye(6), g) - np.kron(g.T, np.eye(6)) for g in G_LR])
_, _, Vh = np.linalg.svd(Mx); X = None
for vv in Vh[-2:].conj():
    Xc = vv.reshape(6, 6, order="F")
    if np.linalg.norm(Xc - np.trace(Xc) / 6 * np.eye(6)) > 1e-6: X = Xc; break
evX, VX = np.linalg.eig(X); groups = {}
for i, e in enumerate(evX): groups.setdefault(tuple(np.round([e.real, e.imag], 4)), []).append(i)
PIECES = {}
for idx in groups.values():
    Qp, _ = np.linalg.qr(VX[:, idx]); Ht = Qp.conj().T @ Hm @ Qp; evp = np.linalg.eigvalsh((Ht + Ht.conj().T) / 2)
    PIECES["T" if all(evp > 1e-9) else ("Tbar" if all(evp < -1e-9) else "indefinite")] = Qp


def eig_on(name, M):
    Qp = PIECES[name]; A = Qp.conj().T @ M @ Qp
    invariant = bool(np.allclose(Qp @ A, M @ Qp, atol=1e-8))
    ev = np.linalg.eigvals(A)
    return invariant, sorted([round(float(np.angle(e) / (2 * np.pi)) % 1, 6) for e in ev])


# ---- words, rules, lifts
def inv(w): return "".join(c.swapcase() for c in reversed(w))
def red(w):
    o = []
    for c in w:
        if o and o[-1] == c.swapcase(): o.pop()
        else: o.append(c)
    return "".join(o)
def apply(auto, w): return red("".join(auto[c] if c.islower() else inv(auto[c.lower()]) for c in w))
def compose(f, g): return {x: apply(f, g[x]) for x in "ab"}
P_ = {"a": "b", "b": "a"}; IOTA = {"a": "A", "b": "B"}
def conj_C(r): return compose(P_, compose(r, P_))
def conj_rev(r): return compose(IOTA, compose(r, IOTA))
sigma = {"a": "ab", "b": "a"}
sigma_inv = {"a": "b", "b": "Ba"}
assert compose(sigma, sigma_inv) == {"a": "a", "b": "b"} and compose(sigma_inv, sigma) == {"a": "a", "b": "b"}

r2 = 1 / np.sqrt(2); h = 0.5
units = [np.array(u, dtype=float) for u in ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))]
def q(c): return c[0] * I2 + c[1] * qi + c[2] * qj + c[3] * qk
cands = [s * u for u in units for s in (1, -1)] + [h * np.array(sg) for sg in itertools.product((1, -1), repeat=4)]
cands += [r2 * (su * units[i] + sv * units[j]) for i, j in itertools.combinations(range(4), 2) for su in (1, -1) for sv in (1, -1)]
TWO_O = [q(c) for c in cands]; TWO_T = [q(c) for c in cands[:24]]
def rho_word(w): return W.rep(w, (0, 0))
def lifts(r):
    A, B = rho_word(r["a"]), rho_word(r["b"])
    return [g for g in TWO_O if np.allclose(g @ qi @ np.linalg.inv(g), A) and np.allclose(g @ qj @ np.linalg.inv(g), B)]
def in_2T(g): return any(np.allclose(g, t) for t in TWO_T)
def order(g):
    P = g.copy(); n = 1
    while not np.allclose(P, I2):
        P = P @ g; n += 1
        if n > 48: return None
    return n
ORDER6 = [t for t in TWO_T if order(t) == 6]
CLASSES = []
for t in ORDER6:
    cl = [x for x in ORDER6 if any(np.allclose(x, s @ t @ np.linalg.inv(s)) for s in TWO_T)]
    if not any(any(np.allclose(cl[0], y) for y in c) for c in CLASSES): CLASSES.append(cl)
def class_of(g):
    for i, c in enumerate(CLASSES):
        if any(np.allclose(g, y) for y in c): return i
    return None
def order6_lift(r):
    ls = [g for g in lifts(r) if order(g) == 6]
    return ls[0] if ls else None


def h1mat(r):
    return np.array([[r[x].count("a") - r[x].count("A"), r[x].count("b") - r[x].count("B")] for x in "ab"]).T
def sense(r):
    A = h1mat(r) % 2; pts = [(1, 0), (0, 1), (1, 1)]
    perm = [pts.index(tuple(int(v) for v in (A @ np.array(p)) % 2)) for p in pts]
    if sum(1 for i in range(3) if perm[i] == i) != 0: return "not a 3-cycle"
    return "forward" if perm[0] == 1 else "backward"


def read_rule(name, r):
    g = lifts(r)
    out = {"images": r, "det": int(round(np.linalg.det(h1mat(r)))), "sense": sense(r), "lifts_found": len(g)}
    if not g: return out
    M = W.move_matrix(r, g[0]); out["form_on_V"] = form_action(M)
    r2_ = compose(r, r); g2 = lifts(r2_); out["double_tick_images"] = r2_; out["double_tick_sense"] = sense(r2_)
    t6 = order6_lift(r2_) if order6_lift(r2_) is not None else None
    out["double_tick_order6_class"] = class_of(t6) if t6 is not None else None
    t6r = order6_lift(r); out["rule_order6_class"] = class_of(t6r) if t6r is not None else None
    M2 = W.move_matrix(r2_, g2[0]); out["double_tick_form_on_V"] = form_action(M2)
    invT, evT = eig_on("T", M2); invTb, evTb = eig_on("Tbar", M2)
    out["double_tick_keeps_T"] = invT; out["double_tick_turns_on_T"] = evT; out["double_tick_turns_on_Tbar"] = evTb
    return out


def controls():
    out = {"form": {nm: form_action(M) for nm, M in (("L", W.ML), ("R", W.MR), ("sign", W.MS), ("swap", W.MP))},
           "signature": [int(x) for x in (sum(np.linalg.eigvalsh((Hm + Hm.conj().T) / 2) > 1e-9), sum(np.linalg.eigvalsh((Hm + Hm.conj().T) / 2) < -1e-9))],
           "pieces": sorted(PIECES.keys()), "sigma_order6_lift": [round(float(x.real), 6) for x in (order6_lift(sigma)[0, 0], 0)] if order6_lift(sigma) is not None else None,
           "sigma_sense": sense(sigma), "order6_classes": [len(c) for c in CLASSES]}
    json.dump(out, open(HERE / "controls.json", "w"), indent=1, default=str); print(json.dumps(out, indent=1, default=str))


def cells():
    orbit = {"sigma": sigma, "C": conj_C(sigma), "rev": conj_rev(sigma), "C_rev": conj_C(conj_rev(sigma))}
    H0 = {"orbit": orbit, "size": len({json.dumps(r, sort_keys=True) for r in orbit.values()}),
          "closed": all(json.dumps(conj_C(r), sort_keys=True) in {json.dumps(x, sort_keys=True) for x in orbit.values()} and
                        json.dumps(conj_rev(r), sort_keys=True) in {json.dumps(x, sort_keys=True) for x in orbit.values()} for r in orbit.values()),
          "all_positive": all(all(c.islower() for c in r["a"] + r["b"]) for r in orbit.values())}
    rules = dict(orbit); rules["inverse"] = sigma_inv
    reads = {nm: read_rule(nm, r) for nm, r in rules.items()}
    def flips(a, b, key):
        return reads[a].get(key) != reads[b].get(key)
    H3 = {}
    for op, other in (("C", "C"), ("reversal", "rev"), ("C and reversal", "C_rev"), ("arrow", "inverse")):
        H3[op] = {"hand_ii_sense_of_double_tick": "flips" if flips("sigma", other, "double_tick_sense") else "keeps",
                  "hand_ii_class_of_double_tick": "flips" if flips("sigma", other, "double_tick_order6_class") else "keeps",
                  "hand_i_turns_on_T": "flips" if flips("sigma", other, "double_tick_turns_on_T") else "keeps"}
    pairs = {nm: (reads[nm].get("double_tick_sense"), tuple(reads[nm].get("double_tick_turns_on_T") or ())) for nm in rules}
    H3["relative_hand_is_the_same_for_every_rule"] = len(set(pairs.values())) == 2 and all(
        (pairs[a][0] == pairs[b][0]) == (pairs[a][1] == pairs[b][1]) for a in rules for b in rules)
    H3["with_the_arrow_fixed_both_hands_are_C"] = all(H3[op]["hand_i_turns_on_T"] == H3[op]["hand_ii_sense_of_double_tick"] for op in ("C", "reversal", "C and reversal")) \
        and H3["C"]["hand_i_turns_on_T"] == "flips" and H3["reversal"]["hand_i_turns_on_T"] == "keeps"
    out = {"H0": H0, "reads": reads, "H3": H3}
    json.dump(out, open(HERE / "hands_on_the_torsor.json", "w"), indent=1, default=str); print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    controls() if "--controls" in sys.argv else cells()
