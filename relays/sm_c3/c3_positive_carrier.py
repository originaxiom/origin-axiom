#!/usr/bin/env python3
"""SM-C3, packet positive_carrier (the fork lane @ 0c6570bab): this seat's own exact check, rebuilt from the packet's PROOF.md,
not from its verify.py.  Pairs (m, u), m a Laurent monomial in X, Y and u a column of two Laurent polynomials, multiply by
(m,u)(n,v) = (mn, u + m v); A = (X, (1,0)), B = (Y, (0,1)); E is evaluation on words in a, b, A = a^-1, B = b^-1.
(i) E is injective on all 2,047 positive words of length 0..10, and each is recovered from its flow by sorting its terms
by total degree; E(ab) and E(ba) share XY and differ in flow; (ii) E([a,b]) = (1, (1 - Y, X - 1)); [[a,b],[a,b^2]] freely
reduces to the eighteen letters abABabbABaBAbbaBBA, with no adjacent inverse pair, and E of it is the identity;
(iii) for sigma (a -> ab, b -> a) and tau (a -> b, b -> Ba), with S_sigma: X -> XY, Y -> X, J_sigma = [[1,1],[X,0]],
S_tau: X -> Y, Y -> X/Y, J_tau = [[0, 1/Y],[1, -1/Y]], Phi_f(m,u) = (S_f m, J_f S_f u) equals E(f(w)) on every freely
reduced signed word of length <= 5, and sigma(tau(x)) = x = tau(sigma(x)) for x = a, b after free reduction.
Planted: (p1) a positive word with one letter changed must reconstruct to a different word; (p2) J_sigma with its entries
transposed must break (iii)."""
import itertools
import json
import sys
from pathlib import Path

import sympy as sp

X, Y = sp.symbols("X Y")
ONE = (0, 0, sp.Integer(0), sp.Integer(0))          # (r, s, u1, u2): m = X^r Y^s


def mul(p, q):
    r, s, u1, u2 = p
    r2, s2, v1, v2 = q
    m = X ** r * Y ** s
    return (r + r2, s + s2, sp.expand(u1 + m * v1), sp.expand(u2 + m * v2))


def inv(p):
    r, s, u1, u2 = p
    mi = X ** (-r) * Y ** (-s)
    return (-r, -s, sp.expand(-mi * u1), sp.expand(-mi * u2))


GEN = {"a": (1, 0, sp.Integer(1), sp.Integer(0)), "b": (0, 1, sp.Integer(0), sp.Integer(1))}
GEN["A"], GEN["B"] = inv(GEN["a"]), inv(GEN["b"])


def E(word):
    p = ONE
    for ch in word:
        p = mul(p, GEN[ch])
    return p


def key(p):
    return (p[0], p[1], sp.srepr(sp.expand(p[2])), sp.srepr(sp.expand(p[3])))


def reduce_free(w):
    st = []
    for ch in w:
        if st and st[-1] == ch.swapcase():
            st.pop()
        else:
            st.append(ch)
    return "".join(st)


out = {}
# (i) positive words
positive = [""] + ["".join(t) for n in range(1, 11) for t in itertools.product("ab", repeat=n)]
enc = {}
recon_ok = True
for w in positive:
    p = E(w)
    enc.setdefault(key(p), []).append(w)
    terms = []
    for comp, letter in ((p[2], "a"), (p[3], "b")):
        if comp != 0:
            for (i, j), c in sp.Poly(comp, X, Y).terms():
                terms.append((i + j, letter, c))
    terms.sort()
    rebuilt = "".join(l for _, l, _ in terms)
    recon_ok &= rebuilt == w and all(c == 1 for _, _, c in terms) and [t for t, _, _ in terms] == list(range(len(w)))
out["(i)_positive_words"] = len(positive)
out["(i)_injective"] = all(len(v) == 1 for v in enc.values())
out["(i)_reconstructed"] = recon_ok
pab, pba = E("ab"), E("ba")
out["(i)_ab_vs_ba"] = {"same_monomial": pab[:2] == pba[:2] == (1, 1), "flows": [str(pab[2:]), str(pba[2:])]}
# (ii) commutators
comm = lambda x, y: x + y + "".join(c.swapcase() for c in reversed(x)) + "".join(c.swapcase() for c in reversed(y))
c1 = E(comm("a", "b"))
w18 = reduce_free(comm(comm("a", "b"), comm("a", "bb")))
out["(ii)_E[a,b]"] = str(c1)
out["(ii)_reduced_word"] = w18
out["(ii)_E_reduced_is_identity"] = key(E(w18)) == key(ONE)
ii_ok = (c1[0] == 0 and c1[1] == 0 and sp.expand(c1[2] - (1 - Y)) == 0 and sp.expand(c1[3] - (X - 1)) == 0
         and w18 == "abABabbABaBAbbaBBA" and len(w18) == 18 and reduce_free(w18) == w18 and out["(ii)_E_reduced_is_identity"])
# (iii) substitutions
SUBST = {"sigma": {"a": "ab", "b": "a"}, "tau": {"a": "b", "b": "Ba"}}
SJ = {"sigma": ({X: X * Y, Y: X}, sp.Matrix([[1, 1], [X, 0]])), "tau": ({X: Y, Y: X / Y}, sp.Matrix([[0, 1 / Y], [1, -1 / Y]]))}


def apply_word(f, w):
    img = {**f, "A": "".join(c.swapcase() for c in reversed(f["a"])), "B": "".join(c.swapcase() for c in reversed(f["b"]))}
    return "".join(img[c] for c in w)


def Phi(name, p, J=None):
    sub, Jf = SJ[name]
    Jf = Jf if J is None else J
    r, s, u1, u2 = p
    m = (X ** r * Y ** s).subs(sub, simultaneous=True)
    m = sp.expand(sp.powsimp(m))
    md = sp.Poly(sp.expand(m * X ** 20 * Y ** 20), X, Y).terms()
    (i, j), coef = md[0]
    assert len(md) == 1 and coef == 1
    us = sp.Matrix([u1, u2]).subs(sub, simultaneous=True)
    v = Jf * us
    return (i - 20, j - 20, sp.expand(v[0]), sp.expand(v[1]))


window = sorted({reduce_free("".join(t)) for n in range(0, 6) for t in itertools.product("abAB", repeat=n)} - {None})
window = [w for w in window if len(w) <= 5]
iii = {}
for name, f in SUBST.items():
    iii[name] = all(key(Phi(name, E(w))) == key(E(apply_word(f, w))) for w in window)
iii["sigma_tau_inverse"] = all(reduce_free(apply_word(SUBST["sigma"], apply_word(SUBST["tau"], x))) == x
                               and reduce_free(apply_word(SUBST["tau"], apply_word(SUBST["sigma"], x))) == x for x in ("a", "b"))
out["(iii)_window_size"] = len(window)
out["(iii)"] = iii
out["checks_ok"] = {"i": out["(i)_injective"] and recon_ok and out["(i)_ab_vs_ba"]["same_monomial"], "ii": ii_ok,
                    "iii": all(iii.values())}
# planted
w = "abbab"
w2 = "abaab"
p2 = E(w2)
terms = sorted([(i + j, l) for comp, l in ((p2[2], "a"), (p2[3], "b")) if comp != 0 for (i, j), _ in sp.Poly(comp, X, Y).terms()])
out["PLANTED_one_letter_changed_reconstructs_differently"] = "".join(l for _, l in terms) != w
badJ = sp.Matrix([[1, X], [1, 0]])
out["PLANTED_transposed_J_sigma_breaks_iii"] = not all(key(Phi("sigma", E(x), badJ)) == key(E(apply_word(SUBST["sigma"], x))) for x in window)
out["all_claims_hold_and_plants_caught"] = bool(all(out["checks_ok"].values()) and out["PLANTED_one_letter_changed_reconstructs_differently"]
                                                and out["PLANTED_transposed_J_sigma_breaks_iii"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, default=str))
