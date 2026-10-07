#!/usr/bin/env python3
"""B1600, addendum: main's check of the SM seat's W10 (the chiral triplet; its dossier @ 9da13cf0d).  V = (+)_p H^1(F2; chi_p (x) rho_Q) over the three non-zero
parities p (chi_p the sign character with chi_p(a) = (-1)^{p1}, chi_p(b) = (-1)^{p2}; rho_Q: a -> i, b -> j in SU(2)).
A cocycle is determined by (z(a), z(b)) in C^4; coboundaries z(u) = M(u)v - v; H^1 is 2-dimensional (no invariants).
A move m with lift g in 2O (g rho(m(u)) g^-1 ... : rho o m = Ad(g) o rho) acts by z -> g^-1 (z o m), carrying the
chi-doublet to the (chi o m)-doublet.  L: a -> a, b -> ab with g_L = (1 + i)/sqrt2; R: a -> ab, b -> b with
g_R = (1 - j)/sqrt2; the sign iota: a -> a^-1, b -> b^-1 with g = k.  Computed: the group generated on V by L and R
(order, commutant, characters), with the sign, with the swap P (a <-> b, g_P = (i + j)/sqrt2 ... checked), and for
every odd-trace word to length 6 the act at tick 3 on T and T_bar and the hand rule."""
import itertools, json
import numpy as np

# quaternions as 2x2 complex matrices
I2 = np.eye(2, dtype=complex)
qi = np.array([[1j, 0], [0, -1j]]); qj = np.array([[0, 1], [-1, 0]]); qk = qi @ qj
assert np.allclose(qi @ qi, -I2) and np.allclose(qj @ qj, -I2) and np.allclose(qi @ qj, qk)
rho = {"a": qi, "b": qj}
PAR = [(1, 0), (0, 1), (1, 1)]


def chi(p, letter):
    return (-1) ** (p[0] if letter == "a" else p[1])


def inv(w):
    return "".join(c.swapcase() for c in reversed(w))


def rep(word, p):
    """the matrix of chi_p (x) rho on a word (lowercase = generator, uppercase = inverse)"""
    M = I2.copy()
    for c in word:
        g = rho[c.lower()] * chi(p, c.lower())
        M = M @ (g if c.islower() else np.linalg.inv(g))
    return M


def cocycle_value(z, word, p):
    """z: dict a,b -> C^2; extend to the word by the cocycle rule z(uv) = z(u) + M(u) z(v); z(u^-1) = -M(u)^-1 z(u)"""
    val = np.zeros(2, dtype=complex); M = I2.copy()
    for c in word:
        g = c.lower(); Mg = rep(g, p)
        if c.islower():
            val = val + M @ z[g]; M = M @ Mg
        else:
            Mi = np.linalg.inv(Mg); val = val + M @ (-(Mi @ z[g])); M = M @ Mi
    return val


def h1_basis(p):
    """a basis of H^1(F2; chi_p (x) rho): cocycles mod coboundaries, as 4-vectors (z(a), z(b)); returns (basis 4x2, projector)"""
    # coboundary space: v -> (M(a) v - v, M(b) v - v)
    B = np.zeros((4, 2), dtype=complex)
    for k in range(2):
        v = np.zeros(2, dtype=complex); v[k] = 1
        B[:2, k] = rep("a", p) @ v - v; B[2:, k] = rep("b", p) @ v - v
    # complement: orthogonal complement of the coboundaries
    Q, _ = np.linalg.qr(B)
    P = np.eye(4) - Q @ Q.conj().T
    U, s, Vh = np.linalg.svd(P)
    basis = U[:, :2]
    return basis, P


BASES = {p: h1_basis(p) for p in PAR}


def act_parity(m, p):
    """chi_p o m: the parity after the move; m as a dict of images of a, b (words)"""
    sa = np.prod([chi(p, c.lower()) for c in m["a"]]); sb = np.prod([chi(p, c.lower()) for c in m["b"]])
    return (0 if sa == 1 else 1, 0 if sb == 1 else 1)


def move_matrix(m, g):
    """the 6x6 matrix of z -> g^-1 (z o m) on V = (+)_p H^1(chi_p (x) rho) in the chosen bases; block p -> p o m"""
    gi = np.linalg.inv(g)
    Mx = np.zeros((6, 6), dtype=complex)
    for ip, p in enumerate(PAR):
        q = act_parity(m, p)                       # the image doublet: chi_p o m = chi_q
        iq = PAR.index(q)
        basis_p, _ = BASES[p]; basis_q, Pq = BASES[q]
        for k in range(2):
            vec = basis_p[:, k]; z = {"a": vec[:2], "b": vec[2:]}
            # (z o m)(u) = z(m(u)); evaluated at a, b: z(m(a)), z(m(b)) as cocycle values of chi_p (x) rho on the words
            # then g^-1 applied; the result is a cocycle for chi_q (x) rho (rho o m = Ad g rho) -- checked below
            w = np.concatenate([gi @ cocycle_value(z, m["a"], p), gi @ cocycle_value(z, m["b"], p)])
            w = Pq @ w                              # mod coboundaries
            coords = basis_q.conj().T @ w
            Mx[2 * iq: 2 * iq + 2, 2 * ip + k] = coords
    return Mx


sq = 1 / np.sqrt(2)
L = {"a": "a", "b": "ab"}; gL = (I2 + qi) * sq
R = {"a": "ab", "b": "b"}; gR = (I2 - qj) * sq
S = {"a": "A", "b": "B"}; gS = qk
P = {"a": "b", "b": "a"}; gP = (qi + qj) * sq      # g i g^-1 = j, g j g^-1 = i ?  (checked)
# sanity: rho o m = Ad(g) rho on generators
for name, m, g in (("L", L, gL), ("R", R, gR), ("S", S, gS), ("P", P, gP)):
    for x in "ab":
        lhs = rep(m[x], (0, 0)); rhs = g @ rho[x] @ np.linalg.inv(g)
        assert np.allclose(lhs, rhs), (name, x, lhs, rhs)
ML, MR, MS, MP = (move_matrix(m, g) for m, g in ((L, gL), (R, gR), (S, gS), (P, gP)))


def key(M):
    return tuple(np.round(M.flatten(), 5).view(float))


def group(gens):
    """the group generated, every product snapped to nine decimals so numerical drift cannot double an element"""
    I = np.eye(6, dtype=complex); G = {key(I): I}; fr = [I]
    while fr:
        M = fr.pop()
        for g in gens:
            N = np.round(M @ g, 9); k = key(N)
            if k not in G:
                G[k] = N; fr.append(N)
                if len(G) > 5000: raise RuntimeError("not finite?")
    return list(G.values())


def commutant_dim(G):
    # dimension of {X : X g = g X for all g}: solve linear system on 36 unknowns
    rows = []
    for g in G:
        A = np.kron(np.eye(6), g) - np.kron(g.T, np.eye(6))
        rows.append(A)
    A = np.vstack(rows); s = np.linalg.svd(A, compute_uv=False)
    return int(sum(1 for x in s if x < 1e-8)) + (36 - len(s)) if len(s) < 36 else int(sum(1 for x in s if x < 1e-8))


def char_table_info(G):
    chars = [np.trace(g) for g in G]
    return {"order": len(G), "sum |chi|^2 / |G|": round(float(sum(abs(c) ** 2 for c in chars).real / len(G)), 6),
            "character_of_V_real": bool(all(abs(c.imag) < 1e-8 for c in chars))}


def pieces_info(G, pieces):
    out = []
    for Q in pieces:
        ch = [np.trace(Q.conj().T @ g @ Q) for g in G]
        out.append({"dim": Q.shape[1], "sum |chi|^2 / |G|": round(float(sum(abs(c) ** 2 for c in ch).real / len(G)), 6),
                    "complex_character": bool(any(abs(c.imag) > 1e-6 for c in ch)),
                    "character_values": sorted({(round(c.real, 3), round(c.imag, 3)) for c in ch})})
    return out


out = {}
G_LR = group([ML, MR]); out["L,R"] = char_table_info(G_LR); out["L,R"]["commutant_dim"] = commutant_dim(G_LR)
G_LRS = group([ML, MR, MS]); out["L,R,sign"] = char_table_info(G_LRS); out["L,R,sign"]["commutant_dim"] = commutant_dim(G_LRS)
G_LRP = group([ML, MR, MP]); out["L,R,swap"] = char_table_info(G_LRP); out["L,R,swap"]["commutant_dim"] = commutant_dim(G_LRP)
# the isotypic decomposition under L, R: the commutant's eigenspaces -> T and T_bar
# find a non-scalar element of the commutant
rows = [np.kron(np.eye(6), g) - np.kron(g.T, np.eye(6)) for g in G_LR]
A = np.vstack(rows); U, s, Vh = np.linalg.svd(A); null = Vh[-out["L,R"]["commutant_dim"]:].conj()
X = None
for v in null:
    Xc = v.reshape(6, 6, order="F")
    if np.linalg.norm(Xc - np.trace(Xc) / 6 * np.eye(6)) > 1e-6:
        X = Xc; break
ev, V = np.linalg.eig(X)
# group eigenvalues
groups = {}
for i, e in enumerate(ev):
    groups.setdefault(tuple(np.round([e.real, e.imag], 5)), []).append(i)
out["L,R isotypic pieces"] = {str(k): len(v) for k, v in groups.items()}
# projectors onto the two pieces
pieces = []
for k, idx in groups.items():
    Vp = V[:, idx]; Q, _ = np.linalg.qr(Vp); pieces.append(Q)
out["L,R pieces"] = pieces_info(G_LR, pieces)
# the words: tick 3 on each piece; the hand rule
MATS = {"L": ((1, 1), (0, 1)), "R": ((1, 0), (1, 1))}
def trace(w):
    A = ((1, 0), (0, 1))
    for c in w:
        B = MATS[c]; A = tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    return A[0][0] + A[1][1]
def words(nmax):
    seen, outw = set(), []
    for n in range(2, nmax + 1):
        for t in itertools.product("LR", repeat=n):
            w = "".join(t)
            if "L" not in w or "R" not in w or any(w == w[:d] * (n // d) for d in range(1, n) if n % d == 0): continue
            ex = w.translate(str.maketrans("LR", "RL")); c = min(min(v[i:] + v[:i] for i in range(n)) for v in (w, ex))
            if c in seen: continue
            seen.add(c); outw.append(c)
    return outw
rows_out = []
for w in words(6):
    if trace(w) % 2 == 0: continue
    for sign in (1, -1):
        Mw = np.eye(6, dtype=complex)
        for c in w: Mw = Mw @ (ML if c == "L" else MR)
        if sign == -1: Mw = Mw @ MS
        M3 = np.linalg.matrix_power(Mw, 3)
        scal = []
        for Q in pieces:
            B = Q.conj().T @ M3 @ Q; kappa = np.trace(B) / 3
            scal.append({"kappa": [round(kappa.real, 6), round(kappa.imag, 6)], "scalar": bool(np.allclose(B, kappa * np.eye(3), atol=1e-6))})
        nL, nR = w.count("L"), w.count("R")
        rows_out.append({"word": ("+" if sign == 1 else "-") + w, "trace": sign * trace(w), "tick3": scal, "hand": (nL - nR + 2 * (sign == -1)) % 4,
                         "T_alone_somewhere": bool(all(s["scalar"] for s in scal) and abs(scal[0]["kappa"][1]) > 1e-6)})
out["odd_words_tick3"] = rows_out
out["hand_rule_holds"] = all(r["T_alone_somewhere"] == (r["hand"] == 2) for r in rows_out)
out["tick3_scalar_on_both_everywhere"] = all(s["scalar"] for r in rows_out for s in r["tick3"])
import pathlib
json.dump(out, open(pathlib.Path(__file__).resolve().parent / "w10_check.json", "w"), indent=1, default=str)
print(json.dumps({k: v for k, v in out.items() if k != "odd_words_tick3"}, indent=1, default=str))
print([(r["word"], r["hand"], r["T_alone_somewhere"]) for r in rows_out])
