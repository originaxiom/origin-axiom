"""Exact word certificates; no execution before the local seal."""
import json
from collections import deque
from itertools import permutations, product
from pathlib import Path

from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def data():
    return json.loads(Path(__file__).with_name("INPUTS.json").read_text())


def inv(w):
    return tuple(-x for x in reversed(w))


def reduce(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return tuple(out)


def substitute(w, images):
    return reduce(y for x in w for y in (images[x] if x > 0 else inv(images[-x])))


def canonical(w):
    w = reduce(w)
    while len(w) >= 2 and w[0] == -w[-1]:
        w = w[1:-1]
    if not w:
        return ()
    return min(z[k:] + z[:k] for z in (w, inv(w)) for k in range(len(z)))


def generator_words(n):
    return [(1,)*n] + [(1,)*k + (2,) + (-1,)*((k+1) % n) for k in range(n)]


def rewrite(w, n, start=0):
    out, vertex = [], start
    for letter in w:
        sign = 1 if letter > 0 else -1
        next_vertex = (vertex + sign) % n
        edge_start = vertex if sign > 0 else next_vertex
        label = (1 if edge_start == n-1 else 0) if abs(letter) == 1 else edge_start+2
        if label:
            out.append(sign*label)
        vertex = next_vertex
    return tuple(out), vertex


def cover(n):
    d = data()
    rels = [rewrite(d["base_relator"], n, k)[0] for k in range(n)]
    return rels, (1,), rewrite(d["base_longitude"], n)[0]


def abelian_diagonal(n):
    rels, _, _ = cover(n)
    a = Matrix([[r.count(j)-r.count(-j) for j in range(1, n+2)] for r in rels])
    diagonal = smith_normal_form(a, domain=ZZ)
    return [abs(int(diagonal[i, i])) for i in range(n)]


def longitude_commutator_certificate():
    d = data()
    r, ell = tuple(d["base_relator"]), tuple(d["base_longitude"])
    w, ws = ell[:4], ell[4:]
    r2 = reduce((2,) + ws + (-1,) + inv(ws))
    prefix = inv(r)[:6]
    assert r2 == reduce(inv(prefix) + inv(r) + prefix)
    commutator = reduce((1,) + ell + (-1,) + inv(ell))
    assert commutator == reduce(r + w + r2 + inv(w))
    return {"second_relation_conjugator": prefix, "second_relation": r2,
            "commutator_word": commutator}


def shortening_certificate(word, relator, cap=12000):
    """Bounded search; a returned path proves equality, a miss proves nothing."""
    word = reduce(word)
    rules = []
    for r in (tuple(relator), inv(relator)):
        for k in range(len(r)):
            rotated = r[k:] + r[:k]
            for length in range((len(r)+1)//2, len(r)+1):
                rules.append((rotated[:length], inv(rotated[length:])))
    pending, history = deque([word]), {word: None}
    while pending and len(history) <= cap:
        w = pending.popleft()
        if not w:
            path = []
            while history[w] is not None:
                prev, pos, lhs, rhs = history[w]
                path.append({"before": prev, "position": pos, "lhs": lhs, "rhs": rhs, "after": w})
                w = prev
            return list(reversed(path))
        for lhs, rhs in rules:
            for pos in range(len(w)-len(lhs)+1):
                if w[pos:pos+len(lhs)] != lhs:
                    continue
                new = reduce(w[:pos]+rhs+w[pos+len(lhs):])
                if new not in history:
                    history[new] = (w, pos, lhs, rhs)
                    pending.append(new)
    return None


def diagram_certificate():
    from spherogram import Link
    knot = Link(data()["diagram"])
    pieces, records, rels = knot._pieces(), [], []
    for crossing in knot.crossings:
        incoming = outgoing = over = None
        for m, piece in enumerate(pieces, 1):
            for position, entry in enumerate(piece):
                if entry[0] == crossing:
                    if position == 0:
                        outgoing = m
                    elif position == len(piece)-1:
                        incoming = m
                    else:
                        over = m
        assert None not in (incoming, outgoing, over)
        sign = int(crossing.sign)
        records.append((incoming, outgoing, over, sign))
        rels.append((-sign*over, incoming, sign*over, -outgoing))
    assert len(records) == 4 and len(knot.link_components) == 1
    target = tuple(data()["base_relator"])
    initial_images = {g: (g,) for g in range(1, 5)}
    pending = [(tuple(rels), (1, 2, 3, 4), initial_images, [])]
    while pending:
        current, gens, images, steps = pending.pop()
        if len(gens) == 2:
            nonempty = {canonical(r) for r in current} - {()}
            if len(nonempty) != 1:
                continue
            for order in permutations(gens):
                for signs in product((1, -1), repeat=2):
                    rename = {order[j]: ((j+1)*signs[j],) for j in range(2)}
                    if canonical(substitute(next(iter(nonempty)), rename)) != canonical(target):
                        continue
                    original = {g: substitute(w, rename) for g, w in images.items()}
                    start = order[0]
                    arc, longitude, writhe = start, (), 0
                    for _ in range(4):
                        i, j, k, sg = next(row for row in records if row[0] == arc)
                        longitude += (sg*k,)
                        writhe += sg
                        arc = j
                    assert arc == start and writhe == 0
                    ell = substitute(longitude, original)
                    for direction in (1, -1):
                        native = tuple(data()["base_longitude"])
                        native = native if direction == 1 else inv(native)
                        difference = reduce(ell + inv(native))
                        proof = shortening_certificate(difference, target)
                        if proof is not None:
                            return {"PD_code": knot.PD_code(), "Wirtinger_relators": rels,
                                    "crossing_records": records, "Tietze_steps": steps,
                                    "original_generators_in_Riley": original,
                                    "diagram_meridian": original[start],
                                    "diagram_longitude": ell, "longitude_direction": direction,
                                    "longitude_rewrite_proof": proof}
            continue
        for index, rel in enumerate(current):
            for g in gens:
                if sum(abs(x) == g for x in rel) != 1:
                    continue
                position = next(j for j, x in enumerate(rel) if abs(x) == g)
                prefix, suffix = rel[:position], rel[position+1:]
                replacement = reduce(inv(prefix)+inv(suffix)) if rel[position] > 0 else reduce(suffix+prefix)
                change = {h: replacement if h == g else (h,) for h in gens}
                newrels = tuple(substitute(r, change) for j, r in enumerate(current) if j != index)
                newimages = {h: substitute(w, change) for h, w in images.items()}
                step = {"eliminated_generator": g, "using_relator": rel, "replacement": replacement}
                pending.append((newrels, tuple(h for h in gens if h != g), newimages, steps+[step]))
    raise AssertionError("No exact diagram/peripheral certificate in bounded search; not a topological no-go")


def main():
    d = data()
    rel2, mu2, lam2 = cover(2)
    assert [list(r) for r in rel2] == d["M2_relators"]
    assert list(mu2) == d["M2_meridian"] and list(lam2) == d["M2_longitude"]
    inclusion = [rewrite(w, 2)[0] for w in generator_words(6)]
    assert [list(w) for w in inclusion] == d["M6_generators_in_M2"]
    q = d["M2_to_C3"]
    value = lambda w: sum((1 if x > 0 else -1)*q[abs(x)-1] for x in w) % 3
    assert all(value(r) == 0 for r in rel2)
    assert value(mu2) == 1 and value(lam2) == 0
    assert abelian_diagonal(2) == [1, 5]
    assert abelian_diagonal(6) == [1, 1, 1, 1, 8, 40]
    result = {"diagram_certificate": diagram_certificate(),
              "longitude_commutator_certificate": longitude_commutator_certificate(),
              "M2": {"relators": rel2, "meridian": mu2, "longitude": lam2},
              "M6_generators_in_M2": inclusion,
              "H1": {"M2": "Z + Z/5", "M6": "Z + Z/8 + Z/40"}}
    print(json.dumps(result, indent=2))
    print("PASS: exact diagram, peripheral and covering word certificates")


if __name__ == "__main__":
    main()
