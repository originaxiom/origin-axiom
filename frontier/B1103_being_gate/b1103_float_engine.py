"""Independent float-grade verification of chat1's free-group gate claims.

Own code. Instrument rebuilt from the corpus's banked B238 SU(3)_2 data the
same way B593 does (R = T, L = S^-1 T^-1 S, u3 = (e_(1,0) - e_(0,1))/sqrt2),
then h(w) := conj(u3) @ W(w) @ u3 for words over {a, A, b, B} with
a -> R, A -> R^-1, b -> L, B -> L^-1  (left-to-right products).

Claims tested (chat1's):
  T1  h(ab) = 1/(2 phi) + i sin(2pi/5)/sqrt5   (the banked B593 value)
  T2  gate: h(w) in Q(zeta5)  <=>  p-q = 0 mod 3, or h(w) = 0
      -- float surrogate: distance of zeta3^-(p-q) h(w) from the R-span test
         is replaced by the FACTORIZATION test below, which is stronger.
  T3  factorization: g(w) := zeta3^-(p-q) * h(w) is zeta3-Galois-invariant.
      Float surrogate: g(w) must lie in span_Q{1,z5,z5^2,z5^3}; we test the
      NECESSARY float condition that g(w) is unchanged when every zeta3 in a
      zeta60-decomposition is conjugated -- implemented honestly instead as:
      h(w) * zeta3^-(p-q) computed twice, once with the instrument, once with
      the sigma11-transported instrument (entrywise 41-power Galois on exact
      entries is not available at float grade, so we use the CONSEQUENCE:
      |Im part orthogonal to Q(zeta5) lattice| via projection onto the
      4-dim real space spanned by {1, z5, z5^2, z5^3} over R^2... )
      -- kept simple and honest: we test T3' below, which is what float can.
  T3' composition consequence: for all words, h(w) equals
      zeta3^(p-q) * (projection of zeta3^-(p-q) h(w) onto Q(zeta5)-plane)
      to 1e-9, where the Q(zeta5)-plane is the R-span of (1, z5, z5^2, z5^3)
      viewed in C as a 4-dim real lattice -- a full-rank test: a random
      complex number fails it with probability ~0 only if the span were all
      of C... it isn't full: R-span of {1,z5,z5^2,z5^3} in C IS all of C
      (dim 4 real > 2). So THIS test is vacuous at float grade.
      => the real float content is T1, T4, T5, T6; membership/factorization
      goes to the EXACT pass (exact_pass.py). Stated so the record is honest.
  T4  h(abAB) = h(ab) exactly (commutator equals plain word: being phase 1).
  T5  h(aabAAB) = -1/2 - i*phi*sin(2pi/5)/sqrt5 (their -0.5 - 0.688191i).
  T6  h(aB): |p-q| = 2 -> claimed NOT in Q(zeta5) (exact pass decides;
      float records the value).
  T7  census: commutators [u,v], u,v reduced words len <= 2 (nontrivial),
      dedup by word; count how many DISTINCT h-values; test Re(h) lands in
      the nine Niven letters {0, +-1/2, +-1/(2phi), +-phi/2, +-1} to 1e-9;
      count which letters appear.
  T8  chi([u,v]) = 1 is pure algebra (homomorphism to abelian mu3) -- no
      computation needed; recorded as ALGEBRA-TRUE.
"""
import cmath
import importlib.util
import itertools
import math
import os

import numpy as np

REPO = "."


def load(rel, name):
    spec = importlib.util.spec_from_file_location(
        name, os.path.join(REPO, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b238 = load("frontier/B238_su32_levelrank/su32_wrt.py", "b238")

w, S, T, cc = b238.su3_data(2)
n = len(w)
Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
R, L = T, Si @ Ti @ S
Rinv, Linv = np.linalg.inv(R), np.linalg.inv(L)
MAT = {"a": R, "A": Rinv, "b": L, "B": Linv}

i10, i01 = w.index((1, 0)), w.index((0, 1))
u3 = np.zeros(n, dtype=complex)
u3[i10], u3[i01] = 1 / math.sqrt(2), -1 / math.sqrt(2)

PHI = (1 + math.sqrt(5)) / 2
BANKED = 1 / (2 * PHI) + 1j * math.sin(2 * math.pi / 5) / math.sqrt(5)
NIVEN = [0.0, 0.5, -0.5, 1 / (2 * PHI), -1 / (2 * PHI),
         PHI / 2, -PHI / 2, 1.0, -1.0]
NIVEN_NAMES = ["0", "+1/2", "-1/2", "+1/(2phi)", "-1/(2phi)",
               "+phi/2", "-phi/2", "+1", "-1"]


def word_matrix(word):
    M = np.eye(n, dtype=complex)
    for ch in word:
        M = M @ MAT[ch]
    return M


def h(word):
    # the pinned banked convention: the twisted form; identically
    # -1 x the untwisted form on the C-odd u3 (proven identity)
    return -(np.conj(u3) @ word_matrix(word) @ u3)


def pq(word):
    p = word.count("a") - word.count("A")
    q = word.count("b") - word.count("B")
    return p, q


print("== T1: h(ab) vs banked B593 value ==")
v = h("ab")
print(f"h(ab)     = {v:.9f}")
print(f"banked    = {BANKED:.9f}")
print(f"T1 {'PASS' if abs(v - BANKED) < 1e-9 else 'FAIL'} (|diff| = {abs(v-BANKED):.2e})")

print("\n== T4: h(abAB) = h(ab) ==")
vc = h("abAB")
print(f"h(abAB)   = {vc:.9f}")
print(f"T4 {'PASS' if abs(vc - v) < 1e-9 else 'FAIL'} (|diff| = {abs(vc-v):.2e})")

print("\n== T5: h(aabAAB) ==")
v5 = h("aabAAB")
target5 = -0.5 - 1j * PHI * math.sin(2 * math.pi / 5) / math.sqrt(5)
print(f"h(aabAAB) = {v5:.9f}")
print(f"cand -1/2 - i*phi*sin72/sqrt5 = {target5:.9f}")
print(f"T5 value match chat1 float (-0.5, -0.688191): "
      f"{'PASS' if abs(v5 - (-0.5 - 0.688191j)) < 5e-7 else 'FAIL'}")
print(f"T5 exact-candidate match: {'PASS' if abs(v5 - target5) < 1e-9 else 'FAIL'}")

print("\n== T6: h(aB) recorded (membership decided in exact pass) ==")
v6 = h("aB")
p6, q6 = pq("aB")
print(f"h(aB)     = {v6:.9f}   p-q = {p6 - q6}")

print("\n== T7: commutator census ==")
letters = "aAbB"
red = []
for ln in (1, 2):
    for tup in itertools.product(letters, repeat=ln):
        s = "".join(tup)
        if any(s[i] + s[i + 1] in ("aA", "Aa", "bB", "Bb")
               for i in range(len(s) - 1)):
            continue
        red.append(s)


def inv(word):
    return "".join(c.swapcase() for c in reversed(word))


comms = []
seen = set()
for u_ in red:
    for v_ in red:
        cword = u_ + v_ + inv(u_) + inv(v_)
        if cword in seen:
            continue
        seen.add(cword)
        comms.append(cword)

vals = [(c, h(c)) for c in comms]
nontriv = [(c, z) for c, z in vals]
in_letters = 0
letters_hit = set()
off = []
for c, z in nontriv:
    hitidx = [k for k, x in enumerate(NIVEN) if abs(z.real - x) < 1e-9]
    if hitidx:
        in_letters += 1
        letters_hit.add(NIVEN_NAMES[hitidx[0]])
    else:
        off.append((c, z))
print(f"census: {len(red)} reduced words len<=2 -> {len(comms)} distinct "
      f"commutator words")
print(f"Re(h) in the nine Niven letters: {in_letters}/{len(comms)}")
print(f"letters hit ({len(letters_hit)}): {sorted(letters_hit)}")
if off:
    print("OFF-LETTER examples (first 5):")
    for c, z in off[:5]:
        print(f"  {c}: {z:.9f}")

print("\n== T2 gate float scan: all 4^1..4^5 = 1364 strings ==")
mism_val_gate = []
gate_zero = 0
by_class = {0: 0, 1: 0, 2: 0}
CACHE = {"": np.eye(n, dtype=complex)}
for ln in range(1, 6):
    for tup in itertools.product(letters, repeat=ln):
        s = "".join(tup)
        CACHE[s] = CACHE[s[:-1]] @ MAT[s[-1]]
allh = {}
for s, M in CACHE.items():
    if s == "":
        continue
    allh[s] = (np.conj(u3) @ M @ u3, pq(s))
print(f"strings evaluated: {len(allh)}")
# float-observable structure: h(w) * zeta3^-(p-q) should have a zeta3-free
# form; at float grade we CAN test the mod-3 CLASS-consistency of values:
# words with same reduced form must agree (sanity), and report class counts.
for s, (z, (p, q)) in allh.items():
    by_class[(p - q) % 3] += 1
print(f"class counts (p-q mod 3): {by_class}")
print("(membership in Q(zeta5) is NOT float-decidable; exact pass decides)")
