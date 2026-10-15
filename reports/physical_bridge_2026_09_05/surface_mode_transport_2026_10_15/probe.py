"""Exact Fox-prefix word evaluator, adapting the existing cochain primitive."""
from functools import lru_cache
import sympy as s
from analysis import emit
class Evaluator:
    def __init__(self,a,b):
        self.n=a.rows;self.m={'a':a,'b':b,'A':a.inv(),'B':b.inv()}
        self.u={'a':s.Matrix.hstack(s.eye(self.n),s.zeros(self.n)),
                'b':s.Matrix.hstack(s.zeros(self.n),s.eye(self.n))}
    @lru_cache(None)
    def rho(self,word):
        p=s.eye(self.n)
        for c in word:p=p*self.m[c]
        return p
    @lru_cache(None)
    def eval(self,word):
        p=s.eye(self.n);out=s.zeros(self.n,2*self.n)
        for c in word:
            if c.islower():out+=p*self.u[c];p=p*self.m[c]
            else:p=p*self.m[c];out-=p*self.u[c.lower()]
        return out
if __name__=='__main__':raise SystemExit(emit(Evaluator))
