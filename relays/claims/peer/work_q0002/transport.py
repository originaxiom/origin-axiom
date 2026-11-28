"""Integer group algebra of C2*C3. Products are composition, right to left."""
from collections import Counter
import sys


def word(left, right):
    out = list(left)
    for letter in right:
        if out and (out[-1] < 0) == (letter < 0):
            previous = out.pop()
            if letter > 0 and (previous+letter)%3:
                out.append((previous+letter)%3)
        else:
            out.append(letter)
    return tuple(out)


def times(*factors):
    total = {():1}
    for factor in factors:
        nxt = Counter()
        for u,a in total.items():
            for v,b in factor.items():
                nxt[word(u,v)] += a*b
        total = {v:a for v,a in nxt.items() if a}
    return total


def add(*terms):
    out = Counter()
    for coefficient, expr in terms:
        for v,a in expr.items():
            out[v] += coefficient*a
    return {v:a for v,a in out.items() if a}


def main():
    one, s = {():1}, {(-1,):1}
    h = {():1, (1,):1, (2,):1}
    t = {(-1,1):1, (-1,2):1, (1,-1):1, (2,-1):1}
    if "--drop-inverse" in sys.argv:
        del t[(2,-1)]
    plus, minus = add((1,one),(1,s)), add((1,one),(-1,s))
    down, up = times(minus,h,plus), times(plus,h,minus)
    residuals = {
        "four moves":add((1,t),(-1,times(s,h)),(-1,times(h,s)),(2,s)),
        "intertwiner shifts by minus two":add((1,times(t,down)),(-1,times(down,t)),(2,down)),
        "upper norm polynomial":add((1,times(up,down,plus)),
            (-4,times(add((1,t),(2,one)),add((4,one),(-1,t)),plus))),
        "lower norm polynomial":add((1,times(down,up,minus)),
            (-4,times(add((2,one),(-1,t)),add((4,one),(1,t)),minus))),
    }
    for name, defect in residuals.items():
        if defect:
            print("FAIL",name,"nonzero group words",len(defect))
            return 1
        print("DECISIVE:",name,"zero residual in the integral group algebra")
    return 0


if __name__ == "__main__":
    sys.exit(main())
