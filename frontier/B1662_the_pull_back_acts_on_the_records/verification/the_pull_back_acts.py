#!/usr/bin/env python3
"""B1662 -- THE PULL-BACK ACTS ON THE RECORDS (the owner's ruling of 2026-10-16 on P-179): the facts the ruling rests on.
Exact (integer matrices; L = [[1,1],[0,1]], R = [[1,0],[1,1]] as in the record's motion scripts):
  F1  PF1's form at the root: [LR, RL] = (LR)(RL)(LR)^-1(RL)^-1 has trace -2 and equals -U with U unipotent (U != I):
      the failed cancellation lands on the sign times the cusp; the commutator is unchanged when either letter's sign
      flips, so the -2 is not a convention
  F2  the balance points: S = L R^-1 L fixes i with S^2 = -I, S^4 = I; L^-1 R fixes omega with (L^-1 R)^3 = -I
  F3  no forward word reaches them: every integer matrix of determinant 1 with non-negative entries (entries <= 40) has
      trace 2 (I and the parabolic L^n, R^n) or trace >= 3 -- never -I, never trace 0 or +-1
  F4  the mirror: J = diag(1, -1) gives J L J = L^-1, J R J = R^-1, and acts on tau by tau -> -conj(tau)
Seeded walks at equal strength (the pull-back as strong as the step; p = 1/2):
  W1  reading A (the inverse move acts on the records): returns to the identity saturate (transient, Kesten)
  W2  reading B' (the pull-back only undoes the last step; states stay forward words): returns grow like sqrt(T)
  W3  the escape under A: (1/n) E log||X_n|| > 0 (Furstenberg) -- the arrow without a preference
Writes the_pull_back_acts.json."""
import json, math, pathlib, random
I = (1, 0, 0, 1); L = (1, 1, 0, 1); R = (1, 0, 1, 1)
def mul(A, B): a, b, c, d = A; e, f, g, h = B; return (a*e + b*g, a*f + b*h, c*e + d*g, c*f + d*h)
def inv(A): a, b, c, d = A; return (d, -b, -c, a)
def neg(A): return tuple(-x for x in A)
def tr(A): return A[0] + A[3]
def pw(A, n):
    out = I
    for _ in range(n): out = mul(out, A)
    return out
def comm(A, B): return mul(mul(A, B), mul(inv(A), inv(B)))
def mob(A, t): a, b, c, d = A; return (a*t + b)/(c*t + d)
out = {}
LR, RL = mul(L, R), mul(R, L); C = comm(LR, RL); U = neg(C)
out["F1"] = dict(commutator=C, trace=tr(C), minus_is_unipotent=(tr(U) == 2 and U != I),
                 sign_free=all(comm(A, B) == C for A in (LR, neg(LR)) for B in (RL, neg(RL))))
out["F1"]["holds"] = out["F1"]["trace"] == -2 and out["F1"]["minus_is_unipotent"] and out["F1"]["sign_free"]
S = mul(mul(L, inv(R)), L); V = mul(inv(L), R); w = complex(-0.5, math.sqrt(3)/2)
out["F2"] = dict(S=S, S2=pw(S, 2), S4=pw(S, 4), S_fixes_i=abs(mob(S, 1j) - 1j) < 1e-15, V=V, V3=pw(V, 3), V6=pw(V, 6),
                 V_fixes_omega=abs(mob(V, w) - w) < 1e-12)
out["F2"]["holds"] = (out["F2"]["S2"] == neg(I) and out["F2"]["S4"] == I and out["F2"]["S_fixes_i"]
                      and out["F2"]["V3"] == neg(I) and out["F2"]["V6"] == I and out["F2"]["V_fixes_omega"])
traces = set()
for a in range(41):
    for d in range(41):
        for b in range(41):
            if b == 0:
                if a*d == 1: traces.add(a + d)
                continue
            c, r = divmod(a*d - 1, b)
            if r == 0 and 0 <= c <= 40: traces.add(a + d)
out["F3"] = dict(traces_seen_min=min(traces), has_2=2 in traces, below_2=sorted(t for t in traces if t < 2),
                 holds=min(traces) == 2 and not any(t in traces for t in (-2, -1, 0, 1)))
J = (1, 0, 0, -1); t0 = complex(0.31, 1.27)
mirror = lambda t: -t.conjugate()
out["F4"] = dict(JLJ=mul(mul(J, L), J), JRJ=mul(mul(J, R), J),
                 tau_map=abs(mirror(mob(L, mirror(t0))) - mob(inv(L), t0)) < 1e-14)
out["F4"]["holds"] = out["F4"]["JLJ"] == inv(L) and out["F4"]["JRJ"] == inv(R) and out["F4"]["tau_map"]
def walk_A(T, rng, marks):
    m = I; ret = 0; rec = {}
    for t in range(1, T + 1):
        m = mul(m, (L, R, inv(L), inv(R))[rng.randrange(4)])
        if m == I: ret += 1
        if t in marks: rec[t] = ret
    return rec
def walk_B(T, rng, marks):
    depth = 0; ret = 0; rec = {}
    for t in range(1, T + 1):
        if rng.random() < 0.5: depth = max(depth - 1, 0)
        else: depth += 1
        if depth == 0: ret += 1
        if t in marks: rec[t] = ret
    return rec
marks = (500, 4000); W = 600
for name, fn, seed in (("W1", walk_A, 101), ("W2", walk_B, 202)):
    rng = random.Random(seed); recs = [fn(4000, rng, marks) for _ in range(W)]
    out[name] = {f"mean_returns_T{m}": sum(r[m] for r in recs)/W for m in marks}
out["W1"]["holds"] = out["W1"]["mean_returns_T4000"] - out["W1"]["mean_returns_T500"] < 0.15
out["W2"]["holds"] = out["W2"]["mean_returns_T4000"] > 2.2*out["W2"]["mean_returns_T500"]
rng = random.Random(303); n = 1500; s = 0.0
for _ in range(W):
    m = I
    for _ in range(n): m = mul(m, (L, R, inv(L), inv(R))[rng.randrange(4)])
    s += 0.5*math.log(sum(x*x for x in m))
out["W3"] = dict(n=n, walks=W, escape_rate=s/W/n); out["W3"]["holds"] = 0.07 < out["W3"]["escape_rate"] < 0.13
out["all_hold"] = all(out[k]["holds"] for k in ("F1", "F2", "F3", "F4", "W1", "W2", "W3"))
pathlib.Path(__file__).with_name("the_pull_back_acts.json").write_text(json.dumps(out, indent=1) + "\n")
for k in ("F1", "F2", "F3", "F4", "W1", "W2", "W3"): print(k, json.dumps(out[k]))
print("all hold:", out["all_hold"])
