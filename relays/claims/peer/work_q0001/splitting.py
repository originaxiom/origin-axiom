"""Compare the cyclic sectors before and after pulling functions back from the level five orbit."""
import sys
from flint import nmod_mat, nmod_poly


def rotate(v):
    return v[1], v[2], v[0]


def neighbors(v, n):
    x, y, z = v
    return ((x,z,(x*z-y)%n), (z,y,(y*z-x)%n), (x,(x*y-z)%n,y),
            ((x*y-z)%n,y,x), (y,(y*z-x)%n,z), ((x*z-y)%n,x,z))


def quotient(n, p):
    start = (3, 3, 3)
    orbit, todo = {start}, [start]
    while todo:
        v = todo.pop()
        for u in neighbors(v, n)[:2]:
            if u not in orbit:
                orbit.add(u)
                todo.append(u)
    groups = {min(v, rotate(v), rotate(rotate(v))) for v in orbit}
    cyclic = sorted(groups, key=lambda v: (rotate(v) == v, v))
    size = sum(rotate(v) != v for v in cyclic)
    coords = {}
    for i, v in enumerate(cyclic):
        for j in range(3 if i < size else 1):
            coords[v] = i, j
            v = rotate(v)
    w = next(k for k in range(2, p) if (k*k+k+1)%p == 0)
    neutral = nmod_mat(len(cyclic),len(cyclic),p)
    charge = nmod_mat(size,size,p)
    for i,v in enumerate(cyclic):
        for u in neighbors(v, n):
            j,k = coords[u]
            neutral[i,j] += (p+1)//2
            if i < size and j < size:
                charge[i,j] += pow(w,k,p)
    a, b = neutral.charpoly(), charge.charpoly()
    residual = b // a.gcd(b)
    return orbit, len(cyclic)-size, b.degree(), residual


def main():
    p = 1009
    n = 27 if "--remove-five" in sys.argv else 135
    orbit, fixed, dimension, residual = quotient(n,p)
    five, _, _, low = quotient(5,p)
    low27 = {tuple(x%27 for x in v) for v in orbit}
    low5 = {tuple(x%5 for x in v) for v in orbit}
    x = nmod_poly([0,1],p)
    target = ((x*x-2*x-2)*(x*x+2*x-2)*(x**3-3*x-1)*(x**3-3*x+1))
    if residual != target or fixed != 3 or dimension != 959:
        print("FAIL changed orbit or residual polynomial",n,len(orbit),residual.degree())
        return 1
    if low5 != five or len(low27)*len(five) != len(orbit):
        print("FAIL orbit does not cover the entire CRT product")
        return 1
    print("DECISIVE: orbit, mod-27 and mod-5 projection sizes",len(orbit),len(low27),len(five))
    print("DECISIVE: fixed points, charged degree, defect in characteristic",fixed,dimension,residual.degree(),p)
    print("DECISIVE: common degree of level-five and mixed residuals",low.gcd(residual).degree())
    print("DECISIVE: mixed residual is the product of the two stated quadratics and two cubics")
    return 0


if __name__ == "__main__":
    sys.exit(main())
