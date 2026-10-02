"""R78: exact signed-power interface audit, no writes or physics IDs."""
import hashlib
import importlib.machinery
import importlib.util
import itertools
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
I = ((1, 0), (0, 1))
L = ((1, 1), (0, 1))
R = ((1, 0), (1, 1))


def mul(a, b):
    return tuple(tuple(sum(a[i][t] * b[t][j] for t in range(2))
                       for j in range(2)) for i in range(2))


def power(a, n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("power requires a nonnegative integer")
    out = I
    for _ in range(n):
        out = mul(out, a)
    return out


def sign(a, eps):
    if eps not in (-1, 1):
        raise ValueError("sign must be +/-1")
    return tuple(tuple(eps * x for x in row) for row in a)


def trace(a):
    return a[0][0] + a[1][1]


def determinant(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def word(w):
    if not w or set(w) - set("LR"):
        raise ValueError("nonempty L/R word required")
    out = I
    for ch in w:
        out = mul(out, L if ch == "L" else R)
    return out


def primitive_part(w):
    word(w)  # validate before parsing
    for length in range(1, len(w) + 1):
        if len(w) % length == 0 and w == w[:length] * (len(w) // length):
            return w[:length], len(w) // length
    raise AssertionError("the whole word is always a root")


def canon(w):
    swapped = w.translate(str.maketrans("LR", "RL"))
    return min(v[i:] + v[:i] for v in (w, swapped) for i in range(len(v)))


def mixed_words(maxlen):
    for n in range(2, maxlen + 1):
        for letters in itertools.product("LR", repeat=n):
            w = "".join(letters)
            if len(set(w)) == 2:
                yield w


def fibre_smith(a):
    d = tuple(tuple(a[i][j] - I[i][j] for j in range(2)) for i in range(2))
    order = abs(determinant(d))
    if not order:
        raise ValueError("only full-rank B-I is in this audit")
    gcd = math.gcd(*(x for row in d for x in row))
    return tuple(x for x in (gcd, order // gcd) if x > 1)


def fixed_characters(a, modulus):
    if modulus < 2:
        raise ValueError("modulus >=2 required")
    return [(x, y) for x, y in itertools.product(range(modulus), repeat=2)
            if ((x * a[0][0] + y * a[1][0] - x) % modulus == 0
                and (x * a[0][1] + y * a[1][1] - y) % modulus == 0)]


def realized(w, k, eps):
    if k < 1:
        raise ValueError("positive unsigned multiplier required")
    return sign(power(word(w), k), eps)


def covered(w, k, eps, n):
    if n < 1:
        raise ValueError("positive cover degree required")
    return w, k * n, eps ** n


def old_reconstruction(eps, w):
    root, k = primitive_part(w)
    return power(sign(word(root), eps), k)


def foreign_module():
    manifest = json.loads((HERE / "SIGNED_LEVEL_INPUTS.json").read_text())
    entry = manifest["foreign_snapshot"]
    path = HERE / entry["path"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"]
    loader = importlib.machinery.SourceFileLoader("r78_b1516_readonly", str(path))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


def foreign_reconstruction_audit():
    m = foreign_module()
    census, rows = m.check_census()
    legacy = m.check_generation(rows, box=5)
    bad = []
    for entries in itertools.product(range(-5, 6), repeat=4):
        a, b, c, d = entries
        matrix = ((a, b), (c, d))
        if determinant(matrix) != 1 or abs(trace(matrix)) <= 2:
            continue
        reduced = m.to_positive_word(matrix)
        assert reduced is not None, matrix
        eps, w = reduced
        root, k = primitive_part(w)
        old = old_reconstruction(eps, w)
        if trace(old) != trace(matrix):
            bad.append({"matrix": matrix, "eps": eps, "unsigned_word": w,
                        "root": root, "level": k,
                        "original_trace": trace(matrix), "old_trace": trace(old)})
        assert trace(realized(root, k, eps)) == trace(matrix)
    return {"foreign_census": census, "foreign_C9": legacy,
            "additional_reconstruction_failures": bad}


def exact_report():
    a = word("LR")
    u = sign(power(a, 2), -1)
    candidates = {}
    for w in mixed_words(6):
        assert trace(word(w)) >= len(w) + 1
        if trace(word(w)) == 7:
            root, k = primitive_part(w)
            candidates[canon(w)] = {"unsigned_primitive": k == 1,
                                   "negative_fibre_smith": fibre_smith(sign(word(w), -1))}
    cover_checks = 0
    for w in mixed_words(6):
        if primitive_part(w)[1] != 1:
            continue
        for eps, k, n in itertools.product((-1, 1), range(1, 5), range(1, 5)):
            assert power(realized(w, k, eps), n) == realized(*covered(w, k, eps, n))
            cover_checks += 1
    assert u != power(sign(a, -1), 2)
    assert fibre_smith(u) == (3, 3)
    assert fibre_smith(power(a, 2)) == (5,)
    assert len(fixed_characters(u, 3)) == 9
    assert len(fixed_characters(power(a, 2), 3)) == 1
    assert set(candidates) == {"LLLLLR", "LRLR"}
    assert candidates["LLLLLR"] == {"unsigned_primitive": True, "negative_fibre_smith": (9,)}
    assert candidates["LRLR"] == {"unsigned_primitive": False, "negative_fibre_smith": (3, 3)}
    assert power(u, 2) == power(a, 4)
    return {"A": a, "U": u, "U_trace": trace(u), "U_determinant": determinant(u),
            "U_fibre_smith": fibre_smith(u), "wrong_positive_fibre_smith": fibre_smith(power(a, 2)),
            "fixed_C3_characters": fixed_characters(u, 3),
            "trace7_complete_candidates": candidates,
            "corrected_cover_checks": cover_checks,
            "common_double_cover_matrix": power(u, 2),
            "scope": "conditional signed bundle grammar; no physical generations or index computed"}


def main():
    report = exact_report()
    report["foreign"] = foreign_reconstruction_audit()
    f = report["foreign"]
    assert f["foreign_census"]["total"] == 758 and f["foreign_census"]["passed"]
    assert f["foreign_C9"]["passed"]
    assert any(tuple(map(tuple, x["matrix"])) == sign(power(word("LR"), 2), -1)
               for x in f["additional_reconstruction_failures"])
    report["reconstruction_defect_verified"] = True
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
