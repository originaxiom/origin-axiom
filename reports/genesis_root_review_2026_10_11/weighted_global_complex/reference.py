"""Independent modular rank algorithm, not an independent geometric reconstruction."""
from fractions import Fraction
from pathlib import Path
import json
import sys

PRIMES = (103,127)


def rational_mod(value,p):
    f = Fraction(value)
    assert f.denominator % p, 'prespecified prime divides an input denominator'
    return f.numerator*pow(f.denominator,-1,p) % p


def unpack(record,p,root):
    nr,nc = record['rows'],record['cols']
    pairs = record['Qsqrt2_pairs']
    assert len(pairs) == nr*nc
    flat = [(rational_mod(a,p)+root*rational_mod(b,p))%p for a,b in pairs]
    return [flat[j*nc:(j+1)*nc] for j in range(nr)]


def rank_mod(A,ncols,p):
    A = [list(row) for row in A]
    r = 0
    for c in range(ncols):
        pivot = next((j for j in range(r,len(A)) if A[j][c]%p),None)
        if pivot is None:
            continue
        A[r],A[pivot] = A[pivot],A[r]
        inv = pow(A[r][c],-1,p)
        A[r] = [(v*inv)%p for v in A[r]]
        for j in range(r+1,len(A)):
            factor = A[j][c]
            if factor:
                A[j] = [(a-factor*b)%p for a,b in zip(A[j],A[r])]
        r += 1
        if r == len(A):
            break
    return r


def product_zero(A,B,ncols,p):
    return all(sum(A[i][k]*B[k][j] for k in range(len(B)))%p == 0
               for i in range(len(A)) for j in range(ncols))


def main(out):
    matrices = json.loads((out/'MATRICES.json').read_text())
    primary = json.loads((out/'RESULTS.json').read_text())
    reports = []
    for p in PRIMES:
        root = next(x for x in range(1,p) if x*x%p == 2)
        assert rank_mod([[1,2],[2,4]],2,p) == 1
        assert rank_mod([[1,0],[0,1]],2,p) == 2
        assert rank_mod([],3,p) == 0
        for label,models in matrices.items():
            for model,row in models.items():
                dims = row['dimensions']
                ds = [unpack(M,p,root) for M in row['differentials']]
                assert product_zero(ds[1],ds[0],dims[0],p),(p,label,model,'chain0')
                assert product_zero(ds[2],ds[1],dims[1],p),(p,label,model,'chain1')
                ranks = [rank_mod(ds[j],dims[j],p) for j in range(3)]
                h = [dims[j]-([0]+ranks)[j]-(ranks+[0])[j] for j in range(4)]
                expected = primary['cases'][label]['models'][model]
                assert ranks == expected['ranks'],(p,label,model,'rank',ranks,expected['ranks'])
                assert h == expected['H'],(p,label,model,'H')
                reports.append({'prime':p,'sqrt2':root,'case':label,'model':model,
                                'ranks':ranks,'H':h,'chain_products_zero':True})
    result = {'status':'PASS','model_prime_comparisons':len(reports),
              'scope':'separate rank and chain-product algorithm on primary exported matrices',
              'comparisons':reports}
    with (out/'REFERENCE_RESULTS.json').open('x') as stream:
        json.dump(result,stream,indent=2,sort_keys=True)
        stream.write('\n')
    print(json.dumps({'status':'PASS','model_prime_comparisons':len(reports)}))


if __name__ == '__main__':
    main(Path(sys.argv[1]))
