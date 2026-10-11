"""Exact word-level genesis checks. No imports from the existing producers."""
import itertools
import json

ID = {"a": "a", "b": "b"}
L0 = {"a": "a", "b": "ab"}
L1 = {"a": "a", "b": "ba"}
R0 = {"a": "ab", "b": "b"}
R1 = {"a": "ba", "b": "b"}
INVERSES = (
    {"a": "a", "b": "Ab"}, {"a": "a", "b": "bA"},
    {"a": "aB", "b": "b"}, {"a": "Ba", "b": "b"},
)
PAIR_TABLE = ((L0, R0, ""), (L1, R0, "b"),
              (L0, R1, "A"), (L1, R1, "Ab"))
C = "aBAb"


def inv(word):
    return word[::-1].swapcase()


def red(word):
    out = []
    for x in word:
        if x not in "abAB":
            raise ValueError(x)
        if out and out[-1] == x.swapcase():
            out.pop()
        else:
            out.append(x)
    return "".join(out)


def apply(f, word):
    return red("".join(f[x] if x.islower() else inv(f[x.lower()]) for x in word))


def compose(f, g):
    return {x: apply(f, g[x]) for x in "ab"}


def power(f, n):
    if n < 0:
        raise ValueError("Supply the inverse explicitly for negative powers")
    out = dict(ID)
    for _ in range(n):
        out = compose(out, f)
    return out


def inner(word):
    return {x: red(word + x + inv(word)) for x in "ab"}


def transport(f, word):
    return compose(inner(word), compose(f, inner(inv(word))))


def h1(f):
    return tuple(tuple(f[x].count(y) - f[x].count(y.upper()) for x in "ab") for y in "ab")


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def total(m):
    return sum(map(sum, m))


def positive_candidates(matrix):
    columns = []
    for j in range(2):
        letters = "a" * matrix[0][j] + "b" * matrix[1][j]
        columns.append(sorted({"".join(p) for p in itertools.permutations(letters)}))
    return [{"a": a, "b": b} for a, b in itertools.product(*columns)]


def verify():
    facts = {}
    def check(name, statement):
        facts[name] = bool(statement)
        if not statement:
            raise AssertionError(name)

    lm, rm, im = ((1, 1), (0, 1)), ((1, 0), (1, 1)), ((1, 0), (0, 1))
    check("complete_positive_L", positive_candidates(lm) == [L0, L1])
    check("complete_positive_R", positive_candidates(rm) == [R0, R1])
    for name, f, g, matrix in zip(("L0", "L1", "R0", "R1"), (L0, L1, R0, R1), INVERSES, (lm, lm, rm, rm)):
        check(name + "_inverse", compose(f, g) == compose(g, f) == ID)
        check(name + "_matrix", h1(f) == matrix)
    delta = compose(L0, compose(INVERSES[2], L0))
    check("delta_explicit", delta == {"a": "aBA", "b": "a"})
    check("delta_fourth", power(delta, 4) == inner(C))
    transported = []
    for i, (l, r, q) in enumerate(PAIR_TABLE):
        c = red(q + C + inv(q))
        check(f"pair_{i}_simultaneous", transport(L0, q) == l and transport(R0, q) == r)
        check(f"pair_{i}_fixed_peripheral", apply(l, c) == apply(r, c) == c)
        check(f"pair_{i}_delta_fourth", power(transport(delta, q), 4) == inner(c))
        transported.append({"q": q, "peripheral": c, "L": l, "R": r})
    check("union_has_inner_A", compose(L1, INVERSES[0]) == inner("A"))
    check("union_has_inner_b", compose(R1, INVERSES[2]) == inner("b"))
    check("control_inner_A_not_fixed", apply(inner("A"), C) != C)
    check("control_inner_b_not_fixed", apply(inner("b"), C) != C)
    sigma, p = {"a": "ab", "b": "a"}, {"a": "b", "b": "a"}
    double = power(sigma, 2)
    lr = compose(L0, R0)
    check("sigma_LP", sigma == compose(L0, p))
    check("PLP_R1", compose(p, compose(L0, p)) == R1)
    check("double_tick_word", double == {"a": "aba", "b": "ab"})
    check("double_tick_L0R1", double == compose(L0, R1))
    check("double_tick_inner_relation", double == compose(inner("ab"), lr))
    check("double_tick_coherent_transport", double == transport(lr, "A"))
    check("control_double_tick_not_based_LR", double != lr)
    check("double_tick_same_matrix", h1(double) == h1(lr))
    check("control_double_tick_not_fixed_c", apply(double, C) != C)
    n_checked = 0
    for n in range(1, 9):
        for word in itertools.product((lm, rm), repeat=n):
            m = im
            for g in word:
                new = mul(m, g)
                check(f"positive_{n_checked}_growth", total(new) > total(m))
                m = new
                n_checked += 1
            check(f"positive_{n_checked}_nonidentity", m != im)
    return {"status": "PASS", "checks": len(facts), "matrix_extensions_checked": n_checked,
            "pair_table": transported, "sigma_squared": double, "standard_LR": lr,
            "all_length_scope": "Analytic proof in PROOF.md, not a census inference",
            "physical_claim": False}


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
