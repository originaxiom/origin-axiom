"""Native legacy lower-cocycle engine; certificate formulation is shared."""
from analysis import ROOT,load,emit
import sympy as s

legacy=load(ROOT/'frontier/B1138_structural_completion/verification/my_chevalley.py','legacy_exact_E8_brackets')

class Engine:
    def __init__(self):
        self.alg=legacy.ChevalleyAlgebra(legacy.en_cartan(8),'E8')
        self.roots=self.alg.roots;self.index=self.alg.IDX
    def e(self,r):return s.Matrix(self.alg.evec(r))
    def br(self,u,v):
        return s.Matrix(self.alg.br([legacy.Fr(x) for x in u],[legacy.Fr(x) for x in v]))
    def encode(self,mat):
        return [[i,j,str(x)] for i in range(mat.rows) for j in range(mat.cols) if (x:=mat[i,j])!=0]

if __name__=='__main__':raise SystemExit(emit(Engine()))
