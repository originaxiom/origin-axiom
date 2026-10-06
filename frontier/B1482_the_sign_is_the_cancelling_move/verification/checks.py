#!/usr/bin/env python3
"""B1482 -- the sign of a word state and the moves of the grammar.  Four statements, each proved on the page (FINDINGS)
and checked here by enumeration:
  S1  every product of L, R and the swap P has non-negative entries: no word in them is -I or minus a positive word;
  S2  minus a hyperbolic positive word has no square root in GL(2,Z) -- so a - state is never an 'act squared';
  S3  -I is central, and with it every positive word w acquires its twin -w: no inverse letter is used;
  S4  L^-1 is not +- a positive word: allowing -I does NOT allow inverse letters (the two forks are independent)."""
import itertools, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
L, R, P, NEG = ((1, 1), (0, 1)), ((1, 0), (1, 1)), ((0, 1), (1, 0)), ((-1, 0), (0, -1))
mul = lambda X, Y: ((X[0][0] * Y[0][0] + X[0][1] * Y[1][0], X[0][0] * Y[0][1] + X[0][1] * Y[1][1]), (X[1][0] * Y[0][0] + X[1][1] * Y[1][0], X[1][0] * Y[0][1] + X[1][1] * Y[1][1]))
I2 = ((1, 0), (0, 1)); tr = lambda X: X[0][0] + X[1][1]; det = lambda X: X[0][0] * X[1][1] - X[0][1] * X[1][0]
neg = lambda X: tuple(tuple(-a for a in row) for row in X)
out = {}

# S1: all words in L, R, P to length 10
seen = {I2}; frontier = {I2}; nonneg = True; hit_neg = 0
for n in range(10):
    frontier = {mul(X, G) for X in frontier for G in (L, R, P)}
    nonneg &= all(min(X[0] + X[1]) >= 0 for X in frontier); hit_neg += sum(1 for X in frontier if X == NEG)
    seen |= frontier
out["S1"] = dict(words_to_length=10, distinct_matrices=len(seen), all_entries_nonnegative=nonneg, equal_to_minus_identity=hit_neg)

# positive hyperbolic words to length 12 (both letters)
words = set()
for n in range(2, 13):
    for t in itertools.product((L, R), repeat=n):
        if L in t and R in t:
            M = I2
            for G in t: M = mul(M, G)
            words.add(M)
out["positive_hyperbolic_matrices_to_length_12"] = len(words); out["min_trace"] = min(tr(M) for M in words)

# S2: tr(X^2) = tr(X)^2 - 2 det(X) >= -2 for every X in GL(2,Z); tr(-w) = -tr(w) <= -3.  Enumerate X with |entries| <= 12 as well.
sq_traces = {tr(mul(X, X)) for X in (((a, b), (c, d)) for a in range(-12, 13) for b in range(-12, 13) for c in range(-12, 13) for d in range(-12, 13)) if abs(det(X)) == 1}
out["S2"] = dict(min_trace_of_a_square_in_GL2Z_entries_to_12=min(sq_traces), max_trace_of_minus_a_word=max(-tr(M) for M in words),
                 squares_with_trace_below_minus_2=sum(1 for t in sq_traces if t < -2))

# S3: -I central; twins
out["S3"] = dict(minus_identity_commutes_with_L_R_P=all(mul(NEG, G) == mul(G, NEG) for G in (L, R, P)), minus_identity_squared_is_identity=mul(NEG, NEG) == I2,
                 twins_are_new=not any(neg(M) in words for M in words))

# S4: L^-1 is not +- a positive word (entries of +- a positive word have one sign)
Linv = ((1, -1), (0, 1)); one_sign = lambda X: min(X[0] + X[1]) >= 0 or max(X[0] + X[1]) <= 0
out["S4"] = dict(L_inverse_has_one_sign=one_sign(Linv), every_pm_positive_word_has_one_sign=all(one_sign(M) and one_sign(neg(M)) for M in words),
                 the_record_s_two_words_for_minus_identity={"(L R^-1 L)^2": mul(mul(mul(L, ((1, 0), (-1, 1))), L), mul(mul(L, ((1, 0), (-1, 1))), L)) == NEG,
                                                             "(L^2 R^-1)^2": mul(mul(mul(L, L), ((1, 0), (-1, 1))), mul(mul(L, L), ((1, 0), (-1, 1)))) == NEG})
json.dump(out, open(HERE / "checks.json", "w"), indent=1); print(json.dumps(out))
assert nonneg and hit_neg == 0 and out["S2"]["squares_with_trace_below_minus_2"] == 0 and out["min_trace"] >= 3
assert out["S3"]["minus_identity_commutes_with_L_R_P"] and out["S3"]["twins_are_new"] and not out["S4"]["L_inverse_has_one_sign"] and out["S4"]["every_pm_positive_word_has_one_sign"]
