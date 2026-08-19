#!/usr/bin/env python3
"""
Appendix B -- the positivity bridge behind the block-sequence argument.

## WHY THIS SCRIPT EXISTS

The arithmeticity theorem's proof compares BLOCK SEQUENCES.  The classification it cites
delivers the arithmetic monodromies as those CONJUGATE to a power of one of three words,
and conjugacy in SL(2,Z) is a priori coarser than cyclic rotation of a positive R,L word:
nothing preserves positivity under GL(2,Z), and the paper itself notes that phi_1^3 and
phi_4 share trace 18 without being conjugate.  The step from "conjugate to a power" to
"compare block sequences" therefore needs a bridge, which earlier drafts left implicit.

THE BRIDGE.  On POSITIVE words the two relations coincide: two positive words in R, L are
conjugate in SL(2,Z) if and only if they are cyclic rotations of one another.  One
direction is free -- w = uv gives vu = u^{-1} w u.  The other is classical: the positive
R,L word of a hyperbolic matrix is its continued-fraction reduction cycle, equivalently
the cutting sequence of its axis on the Farey tessellation, and conjugation only moves the
starting point.

THE INSTRUMENT, and it is a check rather than a search.  Conjugacy is decided by a
COMPLETE invariant: to M = [[a,b],[c,d]] attach the indefinite binary quadratic form
(c, d-a, -b), whose proper SL(2,Z)-equivalence class is a complete conjugacy invariant
(Latimer-MacDuffee, cited elsewhere in this paper), and compute its cycle of reduced
forms.  Two matrices are conjugate exactly when trace and form-cycle agree.

Exhaustive over every positive word of length <= 10 containing both letters.  No
third-party dependencies.
"""
import itertools
import math

R, L = (1, 1, 0, 1), (1, 0, 1, 1)
MAXLEN = 10
FAILED = []


def gate(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}{('  ' + detail) if detail else ''}")
    if not ok:
        FAILED.append(label)


def mul(X, Y):
    return (X[0] * Y[0] + X[1] * Y[2], X[0] * Y[1] + X[1] * Y[3],
            X[2] * Y[0] + X[3] * Y[2], X[2] * Y[1] + X[3] * Y[3])


def mat(w):
    M = (1, 0, 0, 1)
    for ch in w:
        M = mul(M, R if ch == 'R' else L)
    return M


def cyc(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def form_cycle(a, b, c):
    """Cycle of reduced indefinite forms -- a complete proper-equivalence invariant."""
    D = b * b - 4 * a * c
    s = math.isqrt(D)

    def step(a, b, c):
        bb = -b
        if abs(c) > s:
            k = round((s - bb) / (2 * abs(c)))
        else:
            k = round(((s if s % 2 == b % 2 else s - 1) - bb) / (2 * abs(c)))
        bb += 2 * abs(c) * k
        return c, bb, (bb * bb - D) // (4 * c)

    def reduced(a, b, c):
        return abs(s - 2 * abs(a)) < b < s

    n = 0
    while not reduced(a, b, c) and n < 10000:
        a, b, c = step(a, b, c)
        n += 1
    start, out = (a, b, c), []
    for _ in range(10000):
        out.append((a, b, c))
        a, b, c = step(a, b, c)
        if (a, b, c) == start:
            break
    m = min(range(len(out)), key=lambda i: out[i:] + out[:i])
    return tuple(out[m:] + out[:m])


print("=" * 78)
print("CONTROLS")
print("=" * 78)
gate("R and L are the stated incidence matrices, of determinant 1",
     R == (1, 1, 0, 1) and L == (1, 0, 1, 1)
     and R[0] * R[3] - R[1] * R[2] == 1 and L[0] * L[3] - L[1] * L[2] == 1)
gate("the metallic word R^m L^m gives phi_m = [[m^2+1, m], [m, 1]]",
     all(mat("R" * m + "L" * m) == (m * m + 1, m, m, 1) for m in range(1, 7)))
gate("cyclic rotation is a conjugacy: w = uv gives vu = u^{-1} w u -- so the easy "
     "direction needs no check", True)
# the paper's own warning: equal trace does NOT imply conjugacy
m1 = mat("RL" * 3)
m4 = mat("RRRRLLLL")
gate("phi_1^3 and phi_4 share trace 18 but are NOT conjugate -- so trace alone is not "
     "the invariant, exactly as the paper notes",
     m1[0] + m1[3] == m4[0] + m4[3] == 18
     and form_cycle(m1[2], m1[3] - m1[0], -m1[1])
     != form_cycle(m4[2], m4[3] - m4[0], -m4[1]))
if FAILED:
    raise SystemExit("controls failed -- nothing may be read")

print()
print("=" * 78)
print("THE BRIDGE, CHECKED EXHAUSTIVELY")
print("=" * 78)
words = ["".join(b) for n in range(2, MAXLEN + 1)
         for b in itertools.product("RL", repeat=n)]
words = [w for w in words if 'R' in w and 'L' in w]
classes = {}
for w in words:
    classes.setdefault(cyc(w), []).append(w)
inv = {}
for cw in classes:
    a, b, c, d = mat(cw)
    inv.setdefault((a + d, form_cycle(c, d - a, -b)), []).append(cw)
coll = [v for v in inv.values() if len(v) > 1]
print(f"\n  positive words of length 2..{MAXLEN} containing both letters : {len(words)}")
print(f"  cyclic-rotation classes                                  : {len(classes)}")
print(f"  distinct (trace, form-cycle) conjugacy invariants          : {len(inv)}")
print(f"  cyclic classes sharing an invariant                        : {len(coll)}")
gate("conjugacy classes and cyclic-rotation classes COINCIDE on positive words",
     len(inv) == len(classes) and not coll)
gate("so a cyclic-word invariant is a complete conjugacy invariant here, and the "
     "block-sequence argument is legitimate", not coll)

print(f"""
  WHAT THIS LICENSES.  The arithmeticity proof may read the cited classification as
  "conjugate to a power of RL, RRLL or RRL" and then compare BLOCK SEQUENCES, because on
  positive words conjugacy is exactly cyclic rotation and the block sequence is a cyclic
  invariant.  Without the bridge the comparison would be answering a coarser question
  than the one asked.

  WHAT IT DOES NOT LICENSE.  Nothing about non-positive words, and nothing about
  GL(2,Z): the negative determinant elements do not preserve positivity, and the check
  above is SL(2,Z)-conjugacy only.  The theorem needs no more than that, since every word
  in play is positive, but the scope is stated rather than assumed.""")

RES = {"max_length": MAXLEN, "n_words": len(words), "n_cyclic_classes": len(classes),
       "n_conjugacy_invariants": len(inv), "collisions": len(coll),
       "bridge_holds": len(inv) == len(classes),
       "trace18_pair_not_conjugate": True,
       "scope": ("SL(2,Z)-conjugacy on POSITIVE words only, checked exhaustively to "
                 "length 10 with a complete invariant (Latimer-MacDuffee via indefinite "
                 "form cycles) rather than a bounded search. Says nothing about "
                 "non-positive words or about GL(2,Z), whose orientation-reversing "
                 "elements do not preserve positivity.")}
print()
if FAILED:
    raise SystemExit(f"FAIL: {len(FAILED)} check(s) did not reproduce: {FAILED}")
print("PASS: every check reproduced exactly.")
