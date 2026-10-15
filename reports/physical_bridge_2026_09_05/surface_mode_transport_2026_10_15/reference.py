"""Separate reverse crossed-homomorphism recurrence; shared certificate/data.

Adapts the existing exact-ring right-to-left control, not the native
prefix evaluator. Both paths use Sympy and the same authored analysis.
"""
from functools import lru_cache
import sympy as s
from analysis import emit
class Evaluator:
    def __init__(self,a,b):
        self.n=a.rows;self.m={'a':a,'b':b};self.mi={k:g.inv() for k,g in self.m.items()}
        self.u={k:s.zeros(self.n,2*self.n) for k in 'ab'}
        self.u['a'][:,:self.n]=s.eye(self.n);self.u['b'][:,self.n:]=s.eye(self.n)
    @lru_cache(None)
    def rho(self,word):
        out=s.eye(self.n)
        for c in reversed(word):out=(self.m[c] if c.islower() else self.mi[c.lower()])*out
        return out
    @lru_cache(None)
    def eval(self,word):
        out=s.zeros(self.n,2*self.n)
        for c in reversed(word):
            if c.islower():out=self.u[c]+self.m[c]*out
            else:out=self.mi[c.lower()]*(out-self.u[c.lower()])
        return out
if __name__=='__main__':raise SystemExit(emit(Evaluator))
