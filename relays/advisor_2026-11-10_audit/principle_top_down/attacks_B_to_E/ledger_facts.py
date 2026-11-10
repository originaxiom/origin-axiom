#!/usr/bin/env python3
"""Attacks B, C and D on the draft of the principle: the acts, the grammars, and the ledger read with every history
as a ground. Integers only; nothing is measured and nothing is compared with a measurement.
Sealed with PREREGISTRATION.md before it was run (ARTIFACT_HASHES.txt).

    python3 -B ledger_facts.py [T]        T = the largest trace enumerated (default 60)

Notation. L = [[1,1],[0,1]], R = [[1,0],[1,1]], the exchange P = [[0,1],[1,0]], the tick F = L.P = [[1,1],[1,0]],
F' = P.L = [[0,1],[1,1]]. A run sequence (c_1 .. c_j) of positive integers stands for the matrix G(c_1) .. G(c_j) with
G(c) = L^(c-1).F = [[c,1],[1,0]]; for j even this is the two-act word L^c1 R^c2 L^c3 .. R^cj, for j odd it is that
word's matrix times P (a history with an odd number of exchanges)."""
import sys, itertools, collections

T = int(sys.argv[1]) if len(sys.argv) > 1 else 60

def mul(A, B): return (A[0]*B[0]+A[1]*B[2], A[0]*B[1]+A[1]*B[3], A[2]*B[0]+A[3]*B[2], A[2]*B[1]+A[3]*B[3])
def det(A): return A[0]*A[3] - A[1]*A[2]
def tr(A): return A[0] + A[3]
I2 = (1, 0, 0, 1); L = (1, 1, 0, 1); R = (1, 0, 1, 1); P = (0, 1, 1, 0)
F = mul(L, P); Fp = mul(P, L)
NAME = {L: "L", R: "R", P: "P", F: "F", Fp: "F'", I2: "I"}
def G(c): return (c, 1, 1, 0)
def mat(seq):
    M = I2
    for c in seq: M = mul(M, G(c))
    return M
def alt(seq):
    return "".join(("L" if i % 2 == 0 else "R") * c for i, c in enumerate(seq))
def word_mat(w, table):
    M = I2
    for ch in w: M = mul(M, table[ch])
    return M
def primes_of(n):
    n = abs(n); out = []; p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0: n //= p
        p += 1
    if n > 1: out.append(n)
    return tuple(out)

out = []
def say(s=""):
    out.append(s); print(s, flush=True)

# ---------------------------------------------------------------- controls: facts known before the run
assert F == (1, 1, 1, 0) and Fp == (0, 1, 1, 1) and mul(F, F) == mul(L, R) and mul(P, P) == I2
assert mat((1, 1)) == mul(L, R) and mat((2, 3)) == word_mat("LLRRR", {"L": L, "R": R}) and mat((3,)) == mul(mul(L, L), F)
assert mul(mul(P, F), P) == Fp
say("controls passed: F.F = L.R; P.P = I; G(c1)G(c2) = L^c1 R^c2; P.F.P = F'")

# ---------------------------------------------------------------- H1: the acts
say("\nH1  THE ACTS: non-negative integer matrices of determinant +1 or -1")
BD = 8
box = [(a, b, c, d) for a in range(BD + 1) for b in range(BD + 1) for c in range(BD + 1) for d in range(BD + 1) if a*d - b*c in (1, -1)]
def finite_order(A):
    M = A
    for k in range(1, 25):
        if M == I2: return k
        M = mul(M, A)
        if max(M) > 10**9: return 0
    return 0
fin = [(A, finite_order(A)) for A in box if finite_order(A)]
say("    entries at most %d: %d matrices; of finite order: %s" % (BD, len(box), [(NAME.get(A, A), k) for A, k in fin]))
S_all = [A for A in box if A not in (I2, P)]
S_set = set(S_all)
def atoms(S):
    Sset = set(S); prods = set()
    for X in S:
        for Y in S:
            Z = mul(X, Y)
            if max(Z) <= BD and Z in Sset: prods.add(Z)
    return [A for A in S if A not in prods]
at_all = atoms(S_all)
at_plus = atoms([A for A in S_all if det(A) == 1])
say("    with I and P removed, the matrices that are not a product of two others: %s" % sorted(NAME.get(A, str(A)) for A in at_all))
say("    the same with determinant +1 only: %s" % sorted(NAME.get(A, str(A)) for A in at_plus))
say("    the four: L trace %d det %d; R trace %d det %d; F trace %d det %d; F' trace %d det %d; P.F.P = F': %s" % (
    tr(L), det(L), tr(R), det(R), tr(F), det(F), tr(Fp), det(Fp), mul(mul(P, F), P) == Fp))
say("    discriminant tr^2 - 4 det: L %d, R %d, F %d, F' %d (zero: a rational fixed direction; 5: none)" % (
    tr(L)**2 - 4*det(L), tr(R)**2 - 4*det(R), tr(F)**2 - 4*det(F), tr(Fp)**2 - 4*det(Fp)))

# ---------------------------------------------------------------- H2: free or not
say("\nH2  THE GRAMMARS: how many different acts do the words of n letters make?")
def growth(gens, nmax):
    table = dict(gens); level = {I2: ""}; rows = []; first = None
    for n in range(1, nmax + 1):
        nxt = {}
        for M, w in level.items():
            for ch, g in table.items():
                Z = mul(M, g); w2 = w + ch
                if Z in nxt:
                    if first is None: first = (n, nxt[Z], w2)
                else:
                    nxt[Z] = w2
        rows.append((n, len(table) ** n, len(nxt)))
        level = nxt
    return rows, first
# NB: 'level' keeps one word per act, so a coincidence between two words is seen when the second arrives.
for label, gens, nmax in (("L, R (the two acts; control: free)", (("L", L), ("R", R)), 14),
                           ("L, F (add; add and exchange)", (("L", L), ("F", F)), 14),
                           ("L, R, F", (("L", L), ("R", R), ("F", F)), 8),
                           ("L, R, F, F'", (("L", L), ("R", R), ("F", F), ("G", Fp)), 6)):
    rows, first = growth(gens, nmax)
    free = all(a == b for _, a, b in rows)
    say("    %-36s words/acts at n=1..%d: %s%s" % (label, nmax, " ".join("%d/%d" % (a, b) for _, a, b in rows[:6]), " ..." if nmax > 6 else ""))
    say("    %-36s %s" % ("", "FREE to %d letters (every word a different act)" % nmax if free else
                          "NOT free: first coincidence at %d letters: %s = %s%s" % (first[0], first[1], first[2], "  (G stands for F')" if "G" in first[1] + first[2] else "")))
say("    relations checked directly: F.R = L.F: %s;  F.L = R.F: %s;  F.F' = L.L: %s;  F'.F = R.R: %s;  F.L = L.F': %s" % (
    mul(F, R) == mul(L, F), mul(F, L) == mul(R, F), mul(F, Fp) == mul(L, L), mul(Fp, F) == mul(R, R), mul(F, L) == mul(L, Fp)))
lf = {I2}
for n in range(8):
    lf |= {mul(M, g) for M in lf for g in (L, F)}
say("    R among the acts of L and F with at most 8 letters: %s;  P among them: %s;  F' among them: %s" % (R in lf, P in lf, Fp in lf))

# ---------------------------------------------------------------- H3: the hand in the grammar of L and F
say("\nH3  HISTORIES IN THE GRAMMAR OF L AND F: primitive cyclic words, not all L")
def necklaces(n, alphabet):
    seen = set()
    for w in itertools.product(alphabet, repeat=n):
        w = "".join(w); key = min(w[i:] + w[:i] for i in range(n))
        if key in seen: continue
        seen.add(key)
        if any(n % d == 0 and w == w[:d] * (n // d) for d in range(1, n)): continue
        yield key
def can(w): return min(w[i:] + w[:i] for i in range(len(w)))
def swap(w): return w.translate(str.maketrans("LR", "RL"))
def runs_of_LF(w):                  # cyclic word over L, F -> its cyclic run sequence (c = 1 + the L's before each F)
    i = max(i for i in range(len(w)) if w[i] == "F")
    w = w[i + 1:] + w[:i + 1]
    seq = []; c = 1
    for ch in w:
        if ch == "L": c += 1
        else: seq.append(c); c = 1
    return tuple(seq)
tot = []; odd = []; even = []; even_words = {}
two_act = {n: sorted(w for w in necklaces(n, "LR") if "L" in w and "R" in w) for n in range(1, 11)}
for n in range(1, 11):
    ws = [w for w in necklaces(n, "LF") if "F" in w]
    o = [w for w in ws if w.count("F") % 2 == 1]; e = [w for w in ws if w.count("F") % 2 == 0]
    tot.append(len(ws)); odd.append(len(o)); even.append(len(e)); even_words[n] = e
say("    n = 1..10   all: %s" % tot)
say("                an odd number of F: %s" % odd)
say("                an even number of F: %s" % even)
say("    two-act histories (primitive cyclic words in L, R with both letters), n = 1..10: %s" % [len(two_act[n]) for n in range(1, 11)])
pairs = selfm = 0; covered = set(); bad = []
for n in range(1, 9):
    for w in even_words[n]:
        seq = runs_of_LF(w)
        w0 = can(alt(seq)); w1 = can(alt(seq[1:] + seq[:1]))
        if w1 != can(swap(w0)): bad.append((w, w0, w1))
        if w0 == w1: selfm += 1
        else: pairs += 1
        covered |= {w0, w1}
all_two = {w for n in range(1, 9) for w in two_act[n]}
missing = sorted(all_two - covered, key=lambda s: (len(s), s))
say("    to 8 letters: %d words with an even number of F; each is a two-act word and its letter-swap (failures of that: %d);" % (pairs + selfm, len(bad)))
say("                  %d give two different two-act words, %d give one" % (pairs, selfm))
say("    two-act histories to 8 letters: %d; reached from those words: %d; not reached: %s" % (len(all_two), len(covered), missing))
dbl = [w for w in missing if any(can(alt(s + s)) == w for n in range(1, 5) for s in itertools.product(range(1, 9), repeat=n) if sum(s) * 2 == len(w) and len(s) % 2 == 1)]
say("    of those not reached, a history of an odd number of runs done twice: %d of %d" % (len(dbl), len(missing)))

# ---------------------------------------------------------------- the ledger by trace
say("\nTHE LEDGER BY TRACE: every cyclic run sequence with trace at most %d" % T)
classes = collections.defaultdict(set)          # (parity of the number of runs, trace) -> cyclic run sequences up to rotation
def canon(seq): return min(seq[i:] + seq[:i] for i in range(len(seq)))
count = 0
def rec(seq, M):
    global count
    for c in range(1, T + 1):
        M2 = mul(M, G(c))
        if M2[0] > T: break
        s2 = seq + (c,)
        if tr(M2) <= T:
            count += 1
            classes[(len(s2) % 2, tr(M2))].add(canon(s2))
        rec(s2, M2)
rec((), I2)
say("    run sequences visited with trace at most %d: %d" % (T, count))
def two_act_classes(t):                          # two-act cyclic words: even sequences up to rotation by TWO
    res = set()
    for s in classes.get((0, t), ()):
        for r in (0, 1):
            s2 = s[r:] + s[:r]
            res.add(min(s2[i:] + s2[:i] for i in range(0, len(s2), 2)))
    return res
h = {t: len(two_act_classes(t)) for t in range(3, T + 1)}
hs = {t: len(classes.get((0, t), ())) for t in range(3, T + 1)}
def manifold_classes(t):
    return {min(canon(s), canon(s[::-1])) for s in classes.get((0, t), ())}
hm = {t: len(manifold_classes(t)) for t in range(3, T + 1)}
say("    controls: trace 3: %s; trace 4: %s; trace 6: %s; trace 7: %s" % tuple(sorted(alt(s) for s in two_act_classes(t)) for t in (3, 4, 6, 7)))
say("    two-act histories of trace t, t = 3..20:                 %s" % [h[t] for t in range(3, 21)])
say("    counting a history and its letter-swap once, t = 3..20:  %s" % [hs[t] for t in range(3, 21)])
say("    counting also a history and its reverse once, t = 3..20: %s" % [hm[t] for t in range(3, 21)])

# ---------------------------------------------------------------- H5: who is alone at its trace
say("\nH5  A HISTORY ALONE AT ITS TRACE (traces 3 to %d)" % T)
say("    exactly one two-act history:                          t = %s" % [t for t in range(3, T + 1) if h[t] == 1])
say("    exactly one, counting a history and its swap once:    t = %s" % [t for t in range(3, T + 1) if hs[t] == 1])
say("    exactly one, counting swap and reverse once:          t = %s" % [t for t in range(3, T + 1) if hm[t] == 1])

# ---------------------------------------------------------------- H4, H6, H7, H8: the record's rule, with every history as a ground
say("\nH4, H6, H7, H8  EVERY HISTORY AS A GROUND, THE RECORD'S RULE: level N = trace + 2; M' is not detected when trace(M') = +2 or -2 mod N")
TR = list(range(3, T + 1))
def rel(t, t2): return (t2 - 2) % (t + 2) == 0 or (t2 + 2) % (t + 2) == 0
assert all(rel(t, t) for t in TR)
mutual_bad = [(t, t2) for t in TR for t2 in TR if t != t2 and rel(t, t2) and rel(t2, t)]
say("    H4  pairs of different traces not detected by each other: %d %s" % (len(mutual_bad), mutual_bad[:5]))
asym = sum(1 for t in TR for t2 in TR if t != t2 and rel(t, t2))
say("        ordered pairs (ground, other trace) with the other not detected: %d of %d" % (asym, len(TR) * (len(TR) - 1)))
roots = [t for t in TR if not any(rel(t0, t) for t0 in TR if t0 != t)]
say("    H6  traces that no other trace's level fails to detect (departures of nothing): %s" % roots)
say("        histories at those traces: %s" % {t: sorted(alt(s) for s in two_act_classes(t)) for t in roots})
viol = [(a, b, c) for a in TR for b in TR if a != b and rel(a, b) for c in TR if c != b and rel(b, c) and not rel(a, c)]
say("    H7  chains a -> b -> c with c detected by a: %d; the first: %s" % (len(viol), viol[:3]))
reach = {3}; frontier = [3]
while frontier:
    t = frontier.pop()
    for t2 in TR:
        if t2 not in reach and rel(t, t2): reach.add(t2); frontier.append(t2)
say("    H8  not detected by the golden ground itself (trace 3, level 5): %d of the %d traces: %s ..." % (sum(rel(3, t) for t in TR), len(TR), [t for t in TR if rel(3, t)][:12]))
say("        reached from trace 3 by chains: %d of %d; not reached: %s" % (len(reach), len(TR), [t for t in TR if t not in reach]))

# ---------------------------------------------------------------- H9: by primes
say("\nH9  THE SAME BY PRIMES: the primes of the discriminant trace^2 - 4; M' is not detected when it has every prime of the ground")
T2 = 200000
spf = list(range(T2 + 3))                          # smallest prime factor, by a sieve
for i in range(2, int((T2 + 2) ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, T2 + 3, i):
            if spf[j] == j: spf[j] = i
def pset(n):
    s = set()
    while n > 1:
        s.add(spf[n]); n //= spf[n]
    return s
assert pset(60) == {2, 3, 5} and pset(1) == set() and pset(97) == {97}
def dprimes(t): return frozenset(pset(t - 2) | pset(t + 2))          # the primes of t^2 - 4 = (t - 2)(t + 2)
pr = {t: dprimes(t) for t in TR}
assert all(pr[t] == frozenset(primes_of(t * t - 4)) for t in TR)
single = [t for t in range(3, T2 + 1) if len(dprimes(t)) == 1]
say("    traces 3 to %d whose discriminant has ONE prime: %s  (discriminants %s)" % (T2, single, [t * t - 4 for t in single]))
small = collections.defaultdict(list)             # prime set -> traces up to T2 having exactly that set, kept only for sets inside some pr[t]
targets = set()
for t in TR:
    ps = sorted(pr[t])
    for r in range(1, len(ps)):
        for sub in itertools.combinations(ps, r): targets.add(frozenset(sub))
for t in range(3, T2 + 1):
    s = dprimes(t)
    if s in targets: small[s].append(t)
minimal = [t for t in TR if not any(frozenset(sub) in small for r in range(1, len(pr[t])) for sub in itertools.combinations(sorted(pr[t]), r))]
say("    traces 3 to %d with no trace up to %d whose primes are a proper part of theirs: %d: %s" % (T, T2, len(minimal), minimal))
say("    examples that are not minimal: %s" % [(t, sorted(pr[t]), [(sorted(s), small[s][:2]) for r in range(1, len(pr[t])) for s in map(frozenset, itertools.combinations(sorted(pr[t]), r)) if s in small][:2]) for t in TR if t not in minimal][:5])
say("    the golden ground (prime 5): traces not detected are those with 5 | t^2 - 4: %s ...; same as the record's rule at level 5: %s" % (
    [t for t in TR if 5 in pr[t]][:10], all((5 in pr[t]) == rel(3, t) for t in TR)))
groups = collections.defaultdict(list)
for t in TR: groups[pr[t]].append(t)
say("    traces with the same primes (each not detected by the other), first few groups of more than one: %s" % [(sorted(k), v) for k, v in sorted(groups.items(), key=lambda kv: kv[1][0]) if len(v) > 1][:6])

# ---------------------------------------------------------------- H10 and the tick's histories
say("\nH10  HISTORIES WITH AN ODD NUMBER OF RUNS (determinant -1), by trace s; the level is s^2 + 4")
hodd = {s: len(classes.get((1, s), ())) for s in range(1, T + 1)}
say("    number of such histories of trace s, s = 1..20: %s" % [hodd[s] for s in range(1, 21)])
say("    s = 1: %s (the tick alone); alone at its trace: s = %s" % (sorted(classes.get((1, 1), ())), [s for s in range(1, T + 1) if hodd[s] == 1]))
say("    s^2 + 4 a power of one prime, s = 1..%d: %s" % (T, [(s, s * s + 4) for s in range(1, T + 1) if len(primes_of(s * s + 4)) == 1]))
say("    -1 is a square modulo s^2 + 4 for every odd s (s = 2c gives c^2 = -1): checked s = 1..%d odd: %s" % (
    T, all(any((c * c + 1) % (s * s + 4) == 0 for c in range(s * s + 4)) for s in range(1, T + 1, 2))))

open(__file__.replace(".py", "_out.txt"), "w").write("\n".join(out) + "\n")
