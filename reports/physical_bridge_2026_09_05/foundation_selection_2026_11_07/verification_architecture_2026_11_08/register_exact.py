"""Exact review source for the sealed architecture design; UNRUN.

Import and execution require the repository's separate prospective gate.
Only standard-library integer and Fraction arithmetic is used.
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction

Word = tuple[int, ...]
Quat = tuple[int, int, int, int]
Monomial = tuple[int, ...]
Series = dict[Monomial, int]
Edge = tuple[Quat, int]

ONE: Quat = (1, 0, 0, 0)
QI: Quat = (0, 1, 0, 0)
QJ: Quat = (0, 0, 1, 0)
QK: Quat = (0, 0, 0, 1)
L = {1: (1,), 2: (1, 2)}
R = {1: (1, 2), 2: (2,)}


def reduce_word(word: Word) -> Word:
    out: list[int] = []
    for letter in word:
        if letter == 0:
            raise ValueError("A zero letter is not a generator")
        if out and out[-1] == -letter:
            out.pop()
        else:
            out.append(letter)
    return tuple(out)


def inverse_word(word: Word) -> Word:
    return tuple(-letter for letter in reversed(word))


def commutator(left: Word, right: Word) -> Word:
    return reduce_word(left + right + inverse_word(left) + inverse_word(right))


def apply_word_map(images: dict[int, Word], word: Word) -> Word:
    expanded: list[int] = []
    for letter in word:
        image = images[abs(letter)]
        expanded.extend(image if letter > 0 else inverse_word(image))
    return reduce_word(tuple(expanded))


def qmul(x: Quat, y: Quat) -> Quat:
    a, b, c, d = x
    e, f, g, h = y
    return (
        a * e - b * f - c * g - d * h,
        a * f + b * e + c * h - d * g,
        a * g - b * h + c * e + d * f,
        a * h + b * g - c * f + d * e,
    )


def qinverse(x: Quat) -> Quat:
    if sum(t * t for t in x) != 1:
        raise ValueError("This inverse routine is for unit Q8 elements")
    return (x[0], -x[1], -x[2], -x[3])


def rho_letter(letter: int) -> Quat:
    image = {1: QI, 2: QJ}[abs(letter)]
    return image if letter > 0 else qinverse(image)


def rho(word: Word) -> Quat:
    q = ONE
    for letter in word:
        q = qmul(q, rho_letter(letter))
    return q


class QuaternionCover:
    """The based labelled graph, with a declared deterministic tree.

    The tree selects coordinates only. None of these constructors is
    called at module import; the new science source remains unrun.
    """

    def __init__(self) -> None:
        self.representatives: dict[Quat, Word] = {ONE: ()}
        self.tree_edges: set[Edge] = set()
        queue = deque([ONE])
        while queue:
            q = queue.popleft()
            for letter in (1, 2, -1, -2):
                target = qmul(q, rho_letter(letter))
                if target in self.representatives:
                    continue
                self.representatives[target] = self.representatives[q] + (letter,)
                edge = (q, letter) if letter > 0 else (target, -letter)
                self.tree_edges.add(edge)
                queue.append(target)
        self.vertices = tuple(self.representatives)
        self.edges = tuple((q, letter) for q in self.vertices for letter in (1, 2))
        self.non_tree = tuple(edge for edge in self.edges if edge not in self.tree_edges)
        self.edge_index = {edge: i + 1 for i, edge in enumerate(self.non_tree)}
        self.basis: dict[int, Word] = {}
        for edge, index in self.edge_index.items():
            q, letter = edge
            target = qmul(q, rho_letter(letter))
            self.basis[index] = reduce_word(
                self.representatives[q] + (letter,) + inverse_word(self.representatives[target])
            )

    def edge_flow(self, word: Word) -> tuple[Quat, dict[Edge, int]]:
        q = ONE
        flow: dict[Edge, int] = {}
        for letter in word:
            target = qmul(q, rho_letter(letter))
            edge = (q, letter) if letter > 0 else (target, -letter)
            flow[edge] = flow.get(edge, 0) + (1 if letter > 0 else -1)
            q = target
        return q, {edge: value for edge, value in flow.items() if value}

    def rewrite(self, word: Word) -> tuple[Quat, Word]:
        q = ONE
        letters: list[int] = []
        for letter in word:
            target = qmul(q, rho_letter(letter))
            edge = (q, letter) if letter > 0 else (target, -letter)
            index = self.edge_index.get(edge)
            if index is not None:
                letters.append(index if letter > 0 else -index)
            q = target
        return q, reduce_word(tuple(letters))

    def expand(self, n_word: Word) -> Word:
        return apply_word_map(self.basis, n_word)

    def induced_map(self, word_map: dict[int, Word]) -> dict[int, Word]:
        images: dict[int, Word] = {}
        for index, basis_word in self.basis.items():
            endpoint, result = self.rewrite(apply_word_map(word_map, basis_word))
            if endpoint != ONE:
                raise ValueError("The proposed word map does not preserve this kernel")
            images[index] = result
        return images


def series_add(left: Series, right: Series, scale: int = 1) -> Series:
    result = dict(left)
    for word, value in right.items():
        result[word] = result.get(word, 0) + scale * value
    return {word: value for word, value in result.items() if value}


def series_multiply(left: Series, right: Series, degree: int) -> Series:
    result: Series = {}
    for u, a in left.items():
        for v, b in right.items():
            if len(u) + len(v) <= degree:
                result[u + v] = result.get(u + v, 0) + a * b
    return {word: value for word, value in result.items() if value}


def magnus(word: Word, degree: int) -> Series:
    if degree < 0:
        raise ValueError("Negative response degree")
    result: Series = {(): 1}
    for letter in word:
        generator = abs(letter)
        if generator == 0:
            raise ValueError("A zero letter is not a generator")
        if letter > 0:
            factor = {(): 1, (generator,): 1} if degree else {(): 1}
        else:
            factor = {tuple([generator] * d): (-1) ** d for d in range(degree + 1)}
        result = series_multiply(result, factor, degree)
    return result


def homogeneous(series: Series, degree: int) -> Series:
    return {word: value for word, value in series.items() if len(word) == degree}


def tensor_product(first: Series, second: Series) -> Series:
    result: Series = {}
    for u, a in first.items():
        for v, b in second.items():
            result[u + v] = result.get(u + v, 0) + a * b
    return {word: value for word, value in result.items() if value}


def rational_rank(rows: list[list[int]]) -> int:
    if not rows:
        return 0
    matrix = [[Fraction(x) for x in row] for row in rows]
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("Ragged matrix")
    rank = 0
    for column in range(width):
        pivot = next((r for r in range(rank, len(matrix)) if matrix[r][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        value = matrix[rank][column]
        matrix[rank] = [x / value for x in matrix[rank]]
        for r in range(rank + 1, len(matrix)):
            multiple = matrix[r][column]
            if multiple:
                matrix[r] = [x - multiple * y for x, y in zip(matrix[r], matrix[rank])]
        rank += 1
        if rank == len(matrix):
            break
    return rank


Permutation = tuple[int, ...]
PERM_ID: Permutation = (0, 1, 2, 3, 4)
PERM_A: Permutation = (1, 2, 0, 3, 4)
PERM_B: Permutation = (1, 2, 3, 4, 0)


def permutation_multiply(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[i]] for i in range(len(left)))


def permutation_inverse(p: Permutation) -> Permutation:
    result = [0] * len(p)
    for i, image in enumerate(p):
        result[image] = i
    return tuple(result)


def permutation_word(word: Word) -> Permutation:
    result = PERM_ID
    for letter in word:
        image = {1: PERM_A, 2: PERM_B}[abs(letter)]
        if letter < 0:
            image = permutation_inverse(image)
        result = permutation_multiply(result, image)
    return result


def inner_joint_multiply(
    left: tuple[Quat, Quat], right: tuple[Quat, Quat]
) -> tuple[Quat, Quat]:
    q, g = left
    r, h = right
    acted = qmul(qmul(g, r), qinverse(g))
    return qmul(q, acted), qmul(g, h)


def inner_joint_inverse(pair: tuple[Quat, Quat]) -> tuple[Quat, Quat]:
    q, g = pair
    gi = qinverse(g)
    return qmul(qmul(gi, qinverse(q)), g), gi


def inner_coefficient(pair: tuple[Quat, Quat]) -> Quat:
    return qmul(pair[0], pair[1])
