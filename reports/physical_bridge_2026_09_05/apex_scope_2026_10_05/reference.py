"""Separate exact implementation: SU6 phases and Gaussian 2x2 matrices.

No native or foreign producer imports. Same author, not independent review.
"""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations, product
import json


def rank(rows):
    a = [[F(x) for x in row] for row in rows]
    r = 0
    for col in range(len(a[0]) if a else 0):
        pivot = next((j for j in range(r, len(a)) if a[j][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        pivot_value = a[r][col]
        a[r] = [x/pivot_value for x in a[r]]
        for j in range(len(a)):
            if j != r:
                c = a[j][col]
                a[j] = [x-c*y for x,y in zip(a[j],a[r])]
        r += 1
        if r == len(a):
            break
    return r


def cubic_structure():
    # Construct signed monomials, not a floating determinant or native Hessian.
    terms = []
    for block in ('q','c','l'):
        for p in permutations(range(3)):
            inversions = sum(p[i] > p[j] for i,j in combinations(range(3),2))
            terms.append(((-1)**inversions, tuple((block,i,p[i]) for i in range(3))))
    for i,a,b in product(range(3), repeat=3):
        terms.append((1,(('q',i,a),('l',a,b),('c',b,i))))
    def coefficient(a,b,c):
        return sum(sign for sign,slots in terms if Counter(slots) == Counter((a,b,c)))
    out = []
    for singlet in (('l',2,2),('l',2,1)):
        md = [[coefficient(('l',a,0),('l',b,c),singlet)
               for c in (1,2) for b in range(2)] for a in range(2)]
        mt = [[coefficient(('q',a,2),('c',c,b),singlet)
               for c in (2,1) for b in range(3)] for a in range(3)]
        out.append((md,mt))
    return out


def add(x,y):
    return (x[0]+y[0],x[1]+y[1])


def mul(x,y):
    return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])


def neg(x):
    return (-x[0],-x[1])


def mm(x,y):
    return tuple(tuple(add(mul(x[i][0],y[0][j]),mul(x[i][1],y[1][j]))
                       for j in range(2)) for i in range(2))


def adj(x):
    return tuple(tuple((x[j][i][0],-x[j][i][1]) for j in range(2)) for i in range(2))


ID = (((1,0),(0,0)),((0,0),(1,0)))


def matrix(label):
    a,b,c,d = label
    return (((a,b),(c,d)),((-c,d),(a,-b)))


def deck_images():
    images = ('a','b')
    for _ in range(3):
        images = tuple(w.replace('a','x').replace('b','ab').replace('x','aab') for w in images)
    return images


def word(w, line):
    a,b = line
    lookup = {'a':a,'b':b,'A':adj(a),'B':adj(b)}
    value = ID
    for letter in w:
        value = mm(value,lookup[letter])
    return value


@lru_cache(None)
def matrix_lines():
    labels = [tuple(sign if j==k else 0 for j in range(4))
              for k in range(4) for sign in (-1,1)]
    pa,pb = deck_images()
    out = []
    for a,b in product(labels, repeat=2):
        aa,bb = matrix(a),matrix(b)
        if mm(aa,bb) != mm(bb,aa) and word(pa,(aa,bb))==aa and word(pb,(aa,bb))==bb:
            out.append((a,b,aa,bb))
    return out


def six_phases():
    # SU6 fundamental blocks: color3, weak2, singlet1; determinant one.
    return sorted({tuple(sorted((a,)*3+(b,)*2+(c,)))
                   for a,b,c in product(range(4), repeat=3)
                   if len({a,b,c})==3 and (3*a+2*b+c)%4==0})


PHASE = ((1,0),(0,1),(-1,0),(0,-1))


def trace(six,line,char,w):
    exponent = ((w.count('a')-w.count('A'))*char[0] +
                (w.count('b')-w.count('B'))*char[1]) % 4
    ext = (0,0)
    for a,b in combinations(six,2):
        ext = add(ext,PHASE[exponent*(a+b)%4])
    dual = (0,0)
    for a in six:
        dual = add(dual,PHASE[-exponent*a%4])
    q = word(w,line)
    tr2 = add(q[0][0],q[1][1])
    return add(ext,mul(tr2,dual))


def words():
    out,level = [],['']
    for _ in range(6):
        level = [w+c for w in level for c in 'aAbB'
                 if not w or w[-1] != c.swapcase()]
        out.extend(level)
    return out


@lru_cache(None)
def census():
    out = []
    population = [c for c in product(range(4),repeat=2) if c[0]%2 or c[1]%2]
    rel = deck_images()
    for six in six_phases():
        for a,b,aa,bb in matrix_lines():
            line = (aa,bb)
            dl = (mm(mm(aa,aa),bb),mm(aa,bb))
            for x,y in population:
                char,dc = (x,y),((2*x+y)%4,(x+y)%4)
                for r in (rel[0]+'A',rel[1]+'B'):
                    if word(r,line)!=ID or trace(six,line,char,r)!=(27,0):
                        raise ValueError('reference full representation relator fails')
                witness = next((w for w in words() if trace(six,line,char,w)!=trace(six,dl,dc,w)),None)
                out.append({'six':list(six),'a':list(a),'b':list(b),'char':[x,y],
                            'witness':witness,'trace':list(trace(six,line,char,witness)) if witness else None,
                            'deck_trace':list(trace(six,dl,dc,witness)) if witness else None})
    return out


def run():
    checks = {}
    structure = cubic_structure()
    checks['cubic/N_blocks'] = structure[0] == ([[0,1,0,0],[-1,0,0,0]],
        [[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0]])
    checks['cubic/nu_blocks'] = structure[1] == ([[0,0,0,-1],[0,0,1,0]],
        [[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]])
    cases = []
    for size in range(1,5):
        for kind in ('zero','identity','ones','singular','noncommuting'):
            g = [[int(kind=='ones' or kind=='identity' and i==j or
                      kind=='singular' and i==j and i<size-1 or
                      kind=='noncommuting' and j==i+1) for j in range(size)] for i in range(size)]
            gn = [[i if i==j else 0 for j in range(size)] for i in range(size)]
            base = [a+b for a,b in zip(g,gn)]
            br = rank(base)
            for mult in (2,3):
                matrix_rows = [[base[i][j] if a==b else 0
                                for j in range(2*size) for b in range(mult)]
                               for i in range(size) for a in range(mult)]
                checks[f'rank/{size}/{kind}/{mult}'] = rank(matrix_rows)==mult*br
            cases.append([size,kind,br])
    checks['torus/four_SU6_classes'] = len(six_phases())==4
    checks['group/24_compact_Q8_lines'] = len(matrix_lines())==24 and all(
        mm(adj(a),a)==ID and mm(adj(b),b)==ID for _,_,a,b in matrix_lines())
    rows = census()
    checks['deck/complete_keys'] = len(rows)==len({(tuple(r['six']),tuple(r['a']),tuple(r['b']),tuple(r['char'])) for r in rows})==1152
    checks['deck/all_exact_witnesses'] = all(r['witness'] and r['trace']!=r['deck_trace'] for r in rows)
    projector = []
    for phase in (2,2,2,1,1):
        total = (0,0)
        for k in range(4):
            total = add(total,PHASE[(phase+2)*k%4])
        projector.append((F(total[0],4),F(total[1],4)))
    checks['selection/projector'] = projector==[(F(1),F(0))]*3+[(F(0),F(0))]*2
    failed = [k for k,v in checks.items() if not v]
    return {'checks':checks,'passed':len(checks)-len(failed),'total':len(checks),'failed':failed,
            'six_classes':[list(p) for p in six_phases()],'rank_cases':cases,'rows':rows,
            'non_author_acceptance':False,'physical_goal_achieved':False}


if __name__=='__main__':
    result = run()
    print(json.dumps(result,indent=2))
    raise SystemExit(bool(result['failed']))
