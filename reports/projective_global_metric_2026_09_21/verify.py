"""F12 exact irreducibility/energy checks, not a numerical global PDE solve."""
from collections import deque
from functools import lru_cache
from pathlib import Path
import importlib.util
import sympy as s

path=Path(__file__).parent.parent/'projective_cusp_spectrum_2026_09_21'/'exception_verify.py'
spec=importlib.util.spec_from_file_location('f12_f11_exception',path)
f11=importlib.util.module_from_spec(spec)
spec.loader.exec_module(f11)
f10=f11.v.f10
q,z,L,beta,k=f11.q,f10.z,f10.length,f10.beta,f10.kappa


def algebra_words(generators,p):
    """B149's span-closure idea, in F11's exact field; retain actual words."""
    n=generators[0].rows
    reduce=lambda a:f11.reduce_matrix(a,p)
    gens=tuple(reduce(g) for g in generators)
    words=['']
    matrices=[s.eye(n)]
    # Incremental echelon rows; no numeric tolerance or guessed word-depth cap.
    echelon=[]

    def insert(matrix):
        row=list(matrix)
        for pivot,basis in echelon:
            coef=row[pivot]
            if coef:
                row=[f11.reduce_scalar(x-coef*y,p) for x,y in zip(row,basis)]
        pivot=next((i for i,x in enumerate(row) if x!=0),None)
        if pivot is None:
            return False
        inv=f11.reduce_scalar(1/row[pivot],p)
        row=[f11.reduce_scalar(inv*x,p) for x in row]
        echelon.append((pivot,row))
        return True

    assert insert(s.eye(n))
    queue=deque([0])
    while queue:
        parent=queue.popleft()
        for label,g in zip('mn',gens):
            new=reduce(g*matrices[parent])
            if insert(new):
                words.append(label+words[parent])
                matrices.append(new)
                queue.append(len(words)-1)
                if len(words)==n*n:
                    return tuple(words),tuple(matrices)
    return tuple(words),tuple(matrices)


def direct_word(word,gens,p):
    result=s.eye(gens[0].rows)
    for char in word:
        result=f11.reduce_matrix(result*gens['mn'.index(char)],p)
    return result


def determinant_field(a,p):
    """Independent square elimination, tracking pivot product and swaps."""
    assert a.rows==a.cols
    a=f11.reduce_matrix(a,p)
    result=s.Integer(1)
    for col in range(a.cols):
        pivot=next((r for r in range(col,a.rows) if a[r,col]!=0),None)
        if pivot is None:
            return s.Integer(0)
        if pivot!=col:
            a.row_swap(pivot,col)
            result=-result
        diagonal=a[col,col]
        result=f11.reduce_scalar(result*diagonal,p)
        for r in range(col+1,a.rows):
            if a[r,col]!=0:
                ratio=f11.reduce_scalar(a[r,col]/diagonal,p)
                a[r,:]=f11.reduce_matrix(a[r,:]-ratio*a[col,:],p)
    return result


@lru_cache(None)
def certificate(middle):
    p=q*q-middle*q+1
    gens=f10.generators()
    words,matrices=algebra_words(gens,p)
    column=s.Matrix.hstack(*(a.reshape(16,1) for a in matrices))
    det=determinant_field(column,p) if len(words)==16 else None
    return {'polynomial':p,'dimension':len(words),'words':words,
            'determinant_mod_p':det,
            'word_reconstruction':all(direct_word(w,gens,p)==a for w,a in zip(words,matrices))}


def energy_data():
    c=4*beta**2/L**2
    density=f10.local_norm_density(f10.local_connection())
    residual=2*L*(3*z*z-c)/(z*(z*z-c)**2)
    tail=L*(2/(z*z-c)-s.log(1-c/(z*z))/c)
    return density,residual,tail


def tracefree_projector(n=4):
    return s.diag(1,*([0]*(n-1)))-s.eye(n)/n


if __name__=='__main__':
    for middle in (14,34):
        print(certificate(middle),flush=True)
    print('energy density, excess, tail:',energy_data(),flush=True)
