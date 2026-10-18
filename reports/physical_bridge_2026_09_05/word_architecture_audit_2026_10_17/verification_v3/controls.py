"""Exact proposed controls for the word/joining audit. Unrun until admission.

No main-bank result is imported as a truth flag. R85 is re-executed from
its pinned producer only when explicitly requested after admission.
"""
from collections import deque
from functools import lru_cache
from hashlib import sha256
import importlib.util
from math import gcd
from pathlib import Path

import sympy as s


def inverse_word(word):
    return word[::-1].swapcase()


def reduce_word(word):
    if any(c not in "abAB" for c in word):
        raise ValueError("Only the declared free-group alphabet is admitted")
    stack = []
    for c in word:
        if stack and stack[-1] == c.swapcase():
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)


def apply_map(mapping, word):
    if set(mapping) != {"a", "b"}:
        raise ValueError("Exactly two ordered generator images required")
    reduce_word(word)
    return reduce_word("".join(mapping[c] if c.islower()
                               else inverse_word(mapping[c.lower()]) for c in word))


def compose(outer, inner):
    return {c: apply_map(outer, inner[c]) for c in "ab"}


def homology(mapping):
    return s.Matrix([[mapping[c].count(g) - mapping[c].count(g.upper())
                      for c in "ab"] for g in "ab"])


def validate_machine(states, updates, outputs):
    states = tuple(states)
    if not states or len(states) != len(set(states)) or set(outputs) != set(states):
        raise ValueError("A nonempty state set and one output per state are required")
    for mapping in updates.values():
        if not set(mapping) <= set(states) or not set(mapping.values()) <= set(states):
            raise ValueError("Partial update leaves the declared state space")
    return states


def future_equivalent(states, updates, outputs, x, y):
    """Complete pair reachability, including unequal continuation domains."""
    states = validate_machine(states, updates, outputs)
    if x not in states or y not in states:
        raise ValueError("Unknown initial state")
    pending = deque([(x, y)])
    seen = set()
    while pending:
        a, b = pending.popleft()
        if (a, b) in seen:
            continue
        seen.add((a, b))
        if outputs[a] != outputs[b]:
            return False
        for transition in updates.values():
            if (a in transition) != (b in transition):
                return False
            if a in transition:
                pending.append((transition[a], transition[b]))
    return True


def kappa(a, b):
    if a.shape != (2, 2) or b.shape != (2, 2) or a.det() != 1 or b.det() != 1:
        raise ValueError("This commutator formula requires SL2 matrices")
    return s.trace(a * b * a.inv() * b.inv())


def primitive_reverser(a, b):
    """B1248's corrected integer law, restricted to kappa != 2."""
    k = kappa(a, b)
    if any(v.is_Integer is not True for m in (a, b) for v in m):
        raise ValueError("Integral lattice required for the entry-gcd law")
    if k == 2:
        raise ValueError("Degenerate pairs require a separate realizer calculation")
    comm = a * b - b * a
    content = 0
    for v in comm:
        content = gcd(content, int(v))
    if content == 0:
        raise ValueError("Unexpected zero commutator outside the degenerate locus")
    primitive = comm / content
    return primitive, primitive.det(), content, k


def matching(left, right, intertwiner, same, inverse):
    """Interface maps are already included in the two indexed tuples."""
    if not left or set(left) != set(right):
        raise ValueError("Same nonempty interface generator roster required")
    inv = inverse(intertwiner)
    return all(same(left[c], intertwiner * right[c] * inv) for c in left)


@lru_cache(None)
def r85():
    """Reuse the actual nonsplit join; do not import or trust old output."""
    base = Path(__file__).resolve().parents[2]
    pins = {
        "joined_background.py": "f1d6bfb9e998a3306ddb41757c9356f4e99757a93ebbfc474e84be9d49bee4c7",
        "cross_branch_positives.py": "57d52d0268cc8562522560029727026d5d0cc80e88bd0f464aee704858911731",
    }
    for name, digest in pins.items():
        if sha256((base / name).read_bytes()).hexdigest() != digest:
            raise ValueError("Changed retained source: " + name)
    spec = importlib.util.spec_from_file_location("word_join_retained_r85", base / "joined_background.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def r85_boundary(gens, right=False):
    n = r85()
    values = {"z": gens["z"], "lambda": n.C.field_word("yXYx", gens)[0]}
    # The admitted torus map is -I, so compare inverse right generators.
    return {name: n.C.inv(value) for name, value in values.items()} if right else values


def r85_unit(i, j):
    n = r85()
    rows = [[n.K.zero for _ in range(5)] for _ in range(5)]
    rows[i][j] = n.K.one
    return n.rows_dm(rows, 5)


def r85_conjugate(gens, frame):
    inverse = r85().C.inv(frame)
    return {name: frame * value * inverse for name, value in gens.items()}


def r85_whole(left, right):
    n = r85()
    return dict(left, **{name.translate(n.RENAME): value for name, value in right.items()})


def r85_relators(gens, relators):
    n = r85()
    identity = n.C.eye(5, n.K)
    return [n.C.same(n.C.field_word(word, gens)[0], identity) for word in relators]


def r85_scale(t):
    n = r85()
    z = n.K.convert(t)
    if not z:
        raise ValueError("A gluing frame must be invertible")
    return n.rows_dm([[z if i == j and i < 4 else
                       n.K.one / z**4 if i == j else n.K.zero
                       for j in range(5)] for i in range(5)], 5)


def r85_trace(matrix):
    rows = matrix.to_list()
    return sum((rows[i][i] for i in range(5)), r85().K.zero)
