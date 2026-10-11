"""Exact coefficient-cocycle checks on canonical derived quotients."""
import importlib.util
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parent.parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


p = load('positive_carrier_sealed', ROOT / 'positive_carrier/verify.py')
b = load('bundle_transport_sealed', ROOT / 'bundle_transport/verify.py')
I = s.eye(2)
PAR = ((0, 0),) + b.PAR


def cyclic_reduce(word):
    """Independent adjacent-cancellation implementation, no stack routine."""
    while True:
        previous = word
        for pair in ('aA', 'Aa', 'bB', 'Bb'):
            word = word.replace(pair, '')
        if previous == word:
            return word


def derivatives(word, a, bb):
    """Return rho(w) and the derivative matrix for all generator values."""
    n = a.rows
    eye = s.eye(n)
    reps = {'a': a, 'b': bb, 'A': a.inv(), 'B': bb.inv()}
    da = s.eye(n).row_join(s.zeros(n))
    db = s.zeros(n).row_join(s.eye(n))
    ds = {'a': da, 'b': db, 'A': -a.inv()*da, 'B': -bb.inv()*db}
    rho, dz = eye, s.zeros(n, 2*n)
    for c in word:
        dz += rho * ds[c]
        rho = rho * reps[c]
    return rho, dz


def block_product(word, a, bb):
    """Separate full affine matrix multiplication, including actual inverses."""
    n = a.rows
    bottom = s.zeros(2*n, n).row_join(s.eye(2*n))
    aa = a.row_join(s.eye(n).row_join(s.zeros(n))).col_join(bottom)
    be = bb.row_join(s.zeros(n).row_join(s.eye(n))).col_join(bottom)
    gens = {'a': aa, 'b': be, 'A': aa.inv(), 'B': be.inv()}
    out = s.eye(3*n)
    for c in word:
        out = out * gens[c]
    return out[:n, :n], out[:n, n:]


def main():
    checks = 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        assert condition, message

    c = p.comm('a', 'b')
    r = p.reduce_word(p.comm(c, 'a'+c+'A'))
    t = p.reduce_word(p.comm(r, 'a'+r+'A'))
    check(r != '' and r == cyclic_reduce(p.comm(c, 'a'+c+'A')), 'F second witness')
    check(t != '' and t == cyclic_reduce(p.comm(r, 'a'+r+'A')), 'F third witness')
    candidates = ('a', 'b', 'ab', 'aB')
    second = set()
    for u in candidates:
        for v in candidates:
            d = p.comm(u, v)
            rr = p.reduce_word(p.comm(d, 'a'+d+'A'))
            if rr:
                second.add(rr)
    third = {p.reduce_word(p.comm(rr, g+rr+g.swapcase()))
             for rr in second for g in 'ab'} - {''}
    short = list(p.words('abAB', 2, reduced=True))
    window = list(p.words('abAB', 4, reduced=True))
    norm = s.zeros(2).col_join(I)
    for ip, parity in enumerate(PAR):
        a, bb = b.rep(parity, 'a'), b.rep(parity, 'b')
        check(a*a == bb*bb == -I and a*bb == -bb*a, ('Q8', parity))
        check(derivatives(c, a, bb)[0] == -I, ('commutator', parity))
        cob = (a-I).col_join(bb-I)
        check(cob.rank() == 2 and (a-I).det() != 0, ('free H1 dimension', parity))
        rh, dr = derivatives(r, a, bb)
        check(rh == I and dr*norm == 4*I, ('metabelian kills full chart', parity))
        check(dr*cob == s.zeros(2), ('relation kills coboundaries', parity))
        check(dr.rank() == 2, ('complete relation rank', parity))
        check(derivatives(t, a, bb) == (I, s.zeros(2, 4)), ('third derived invisible', parity))
        for w in short + [r, t]:
            check(derivatives(w, a, bb) == block_product(w, a, bb), ('affine crosscheck', parity, w))
        for w in window:
            rw, dw = derivatives(w, a, bb)
            ri, di = derivatives(p.invword(w), a, bb)
            check(ri == rw.inv() and di == -rw.inv()*dw, ('inverse', parity, w))
            for g in 'abAB':
                rg, dg = derivatives(g, a, bb)
                check(derivatives(w+g, a, bb) == (rw*rg, dw+rw*dg), ('cocycle law', parity, w, g))
        for tt in sorted(third):
            check(derivatives(tt, a, bb) == (I, s.zeros(2, 4)), ('F third fixture', parity, tt))
        for w in short:
            for j in range(len(w)+1):
                changed = w[:j] + t + w[j:]
                check(derivatives(changed, a, bb) == derivatives(w, a, bb), ('relation insertion', parity, w, j))
        check(derivatives(r, a, bb)[1]*norm[:, 0] != s.zeros(2, 1), ('bad quotient control', parity))
        if parity != (0, 0):
            aa, be = s.Matrix([[(-1)**parity[0]]]), s.Matrix([[(-1)**parity[1]]])
            rank = (aa-s.eye(1)).col_join(be-s.eye(1)).rank()
            check(rank == 1 and 2-rank == 1, ('sign free H1', parity))
            for rr in sorted(second):
                check(derivatives(rr, aa, be) == (s.eye(1), s.zeros(1, 2)), ('sign retains F second', parity, rr))
    moves = ((b.w.L0, b.GL), (b.w.R0, b.GR))
    matrices = []
    for f, g in moves:
        matrices.append(b.cohom(f, g))
        for x in 'ab':
            check(b.equal(b.rep((0, 0), f[x]), g*b.rep((0, 0), x)*g.inv()), ('move lift', f, x))
        for parity in b.PAR:
            target = b.after(parity, f)
            for j in range(2):
                zero, v = s.zeros(2, 1), I[:, j]
                new = [g.inv()*b.cocycle(parity, f[x], zero, v) for x in 'ab']
                chart = b.project(target, *new)
                col = matrices[-1][:, 2*b.PAR.index(parity)+j]
                check(b.equal(col[2*b.PAR.index(target):2*b.PAR.index(target)+2, :], chart), 'chart move')
    ml, mr = matrices
    check(not b.equal(ml*mr, mr*ml), 'noncommuting move control')
    central = b.clean((ml*mr.inv()*ml)**2)
    check(b.equal(central**2, -s.eye(6)), 'central square')
    ranks = []
    for sign in (-1, 1):
        projector = b.clean((s.eye(6) + sign*s.I*central)/2)
        check(b.equal(projector**2, projector), 'central projector')
        check(all(b.equal(projector*m, m*projector) for m in matrices), 'invariant projector')
        ranks.append(projector.rank())
    check(ranks == [3, 3], 'same algebraic triplets')
    print('PASS:', checks, 'exact assertions')
    print('F second witness:', r, 'length', len(r))
    print('F third witness:', t, 'length', len(t))
    print('Derived fixtures:', len(second), 'in F second;', len(third), 'in F third')
    print('Sign H1: G1=0; F2=G2=1 per nontrivial parity (analytic proof).')
    print('Quaternion H1: G2=0; F2=G3=2 per parity (analytic proof).')
    print('Lifted six-dimensional central projector ranks:', ranks)
    print('All-word descent and equivariance rely on PROOF.md, not the finite fixtures.')
    print('No surface, Hodge, physical field, end unit or action derived.')


if __name__ == '__main__':
    main()
