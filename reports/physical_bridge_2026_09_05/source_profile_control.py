"""R80 independent exact entry checks. No native or third-party imports."""
from fractions import Fraction as F
import json


def g(a=0, b=0):
    return F(a), F(b)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def neg(a):
    return -a[0], -a[1]


def mul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def conj(a):
    return a[0], -a[1]


def abs2(a):
    return a[0]*a[0]+a[1]*a[1]


def div(a, b):
    v = abs2(b)
    c = mul(a, conj(b))
    return c[0]/v, c[1]/v


def zero(n, m):
    return [[g() for _ in range(m)] for _ in range(n)]


def eye(n):
    return [[g(i == j) for j in range(n)] for i in range(n)]


def product(a, b):
    out = zero(len(a), len(b[0]))
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                out[i][j] = add(out[i][j], mul(a[i][k], b[k][j]))
    return out


def dagger(a):
    return [[conj(a[j][i]) for j in range(len(a))] for i in range(len(a[0]))]


def difference(a, b):
    return [[add(x, neg(y)) for x, y in zip(r, t)] for r, t in zip(a, b)]


def inverse(a):
    n = len(a); rows = [r[:]+t for r, t in zip(a, eye(n))]
    for col in range(n):
        k = next(i for i in range(col, n) if rows[i][col] != g())
        rows[col], rows[k] = rows[k], rows[col]
        pivot = rows[col][col]; rows[col] = [div(x, pivot) for x in rows[col]]
        for i in range(n):
            if i != col:
                factor = rows[i][col]
                rows[i] = [add(x, neg(mul(factor, y))) for x, y in zip(rows[i], rows[col])]
    return [r[n:] for r in rows]


def determinant(a):
    rows = [r[:] for r in a]; out = g(1); n = len(a)
    for col in range(n):
        k = next((i for i in range(col, n) if rows[i][col] != g()), None)
        if k is None:
            return g()
        if k != col:
            rows[col], rows[k] = rows[k], rows[col]; out = neg(out)
        p = rows[col][col]; out = mul(out, p)
        for i in range(col+1, n):
            f = div(rows[i][col], p)
            rows[i] = [add(x, neg(mul(f, y))) for x, y in zip(rows[i], rows[col])]
    return out


def fixture(n, m, seed):
    return [[g((3*i+5*j+seed)%7-3, (2*i+3*j+2*seed)%5-2)
             for j in range(m)] for i in range(n)]


def trim(a):
    a = list(map(F, a))
    while a and not a[-1]:
        a.pop()
    return a


def pmul(a, b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def remainder(a, b):
    a = trim(a); b = trim(b)
    while len(a) >= len(b) and a:
        c = a[-1]/b[-1]; degree = len(a)-len(b)
        for i, x in enumerate(b):
            a[i+degree] -= c*x
        a = trim(a)
    return a


def gcd(a, b):
    a, b = trim(a), trim(b)
    while b:
        a, b = b, remainder(a, b)
    return [x/a[-1] for x in a] if a else []


def peval(p, t):
    return sum((F(x)*t**i for i, x in enumerate(p)), F(0))


def pder(p):
    return [i*F(x) for i, x in enumerate(p) if i]


def logarithmic_derivative(p, q, t):
    return t*(peval(pder(p), t)*peval(q, t)-peval(p, t)*peval(pder(q), t))/peval(q, t)**2


def longitude(q):
    # Direct rational literal and inverse word, not the native word routine.
    m = [[g(x) for x in r] for r in
         [[1,0,1,q/2-1],[0,1,1,q/2],[0,0,1,(q+1)/2],[0,0,0,1]]]
    n = [[g(x) for x in r] for r in
         [[1,0,0,0],[2+2/q,1,0,0],[2,1,1,0],[1,1,0,1]]]
    letters = {'m': m, 'n': n, 'M': inverse(m), 'N': inverse(n)}
    out = eye(4)
    for a in 'nMNmmNMn':
        out = product(out, letters[a])
    return out


def run():
    checks = {}; block_cases = 0
    for n in range(2, 7):
        for k in range(1, n):
            for seed in range(11):
                z = fixture(n, n, seed)
                mu = difference(product(z, dagger(z)), product(dagger(z), z))
                observed = sum(((n-k if i < k else -k)*mu[i][i][0] for i in range(n)), F(0))
                outgoing = sum((abs2(z[i][j]) for i in range(k) for j in range(k, n)), F(0))
                incoming = sum((abs2(z[i][j]) for i in range(k, n) for j in range(k)), F(0))
                checks[f'block_{n}_{k}_{seed}'] = observed == n*(outgoing-incoming)
                upper = [r[:] for r in z]
                for i in range(k, n):
                    for j in range(k):
                        upper[i][j] = g()
                ud = dagger(upper)
                a = [[div(add(x, neg(y)), g(2)) for x, y in zip(r, v)] for r, v in zip(upper, ud)]
                psi = [[div(add(x, y), g(2)) for x, y in zip(r, v)] for r, v in zip(upper, ud)]
                xi = zero(n, n)
                for i in range(n):
                    xi[i][i] = g(n-k if i < k else -k)
                contraction = product(psi, difference(product(a, xi), product(xi, a)))
                obs_bulk = sum((r[i][0] for i, r in enumerate(contraction)), F(0))
                checks[f'bulk_{n}_{k}_{seed}'] = obs_bulk == -F(n, 2)*outgoing
                block_cases += 1
    edge_cases = 0
    for nt in range(1, 5):
        for nh in range(1, 5):
            b = fixture(nh, nt, nt+nh)
            mh = product(b, dagger(b)); mt = product(dagger(b), b)
            for kt in range(nt+1):
                for kh in range(nh+1):
                    obs = sum((mh[i][i][0] for i in range(kh)), F(0))-sum((mt[i][i][0] for i in range(kt)), F(0))
                    direct = sum((abs2(b[i][j]) for i in range(kh) for j in range(kt, nt)), F(0))
                    direct -= sum((abs2(b[i][j]) for i in range(kh, nh) for j in range(kt)), F(0))
                    checks[f'edge_{nt}_{nh}_{kt}_{kh}'] = obs == direct
                    edge_cases += 1
            checks[f'partner_current_{nt}_{nh}'] = sum(r[i][0] for i, r in enumerate(mh)) == sum(r[i][0] for i, r in enumerate(mt))
    for q in (F(1,2), F(2,3), F(2), F(3), F(5), F(7)):
        d = determinant(difference(longitude(q), eye(4)))
        checks[f'longitude_{q}'] = d == g((q-1)**3*(q**-3-1)) and d != g()
    checks['exceptional_q_one'] = determinant(difference(longitude(F(1)), eye(4))) == g()
    gp = [1,0,0,-34,0,0,1]
    dn = pmul(pmul(pmul([-1,1], [-1,1]), [-1,1]), [1,0,0,-1])
    checks['exact_polynomial_gap'] = gcd(gp, dn) == [F(1)]
    checks['common_root_fail_control'] = gcd(gp, gp) != [F(1)]
    for t in (F(1,2), F(2,3), F(1), F(4,3), F(3,2), F(2)):
        h = peval([1,0,-1], t)/peval([2,0,2], t)
        b = peval([0,2], t)/peval([1,0,1], t)
        hp = logarithmic_derivative([1,0,-1], [2,0,2], t)
        bp = logarithmic_derivative([0,2], [1,0,1], t)
        checks[f'boundary_residual_{t}'] = 2*hp+b*b == 0 and bp-2*h*b == 0
    bulk = -2/(1+F(2)**2)+2/(1+F(1,2)**2)
    flux = 2*((1-F(2)**2)/(2*(1+F(2)**2))-(1-F(1,2)**2)/(2*(1+F(1,2)**2)))
    checks['boundary_exact_integral'] = bulk == F(6,5) and flux == -F(6,5) and 2*bulk+2*flux == 0
    checks['boundary_omission_fails'] = 2*bulk != 0
    up = zero(5,5); up[0][4] = g(1); down = dagger(up)
    mu_up = difference(product(up, dagger(up)), product(dagger(up), up))
    mu_down = difference(product(down, dagger(down)), product(dagger(down), down))
    checks['full_lower_match'] = difference(mu_up, [[neg(x) for x in r] for r in mu_down]) == zero(5,5)
    checks['upper_wrong_sign'] = mu_up != mu_down
    checks['lower_not_parallel'] = difference(product(up, down), product(down, up)) != zero(5,5)
    result = {'checks': checks, 'passed': sum(checks.values()), 'total': len(checks),
              'all_checks_pass': all(checks.values()), 'block_cases': block_cases,
              'edge_cases': edge_cases, 'bulk_norm': str(bulk), 'outward_flux': str(flux),
              'scope': 'independent finite rational controls; not a global physical source law'}
    print(json.dumps(result, sort_keys=True), flush=True)
    return result


if __name__ == '__main__':
    raise SystemExit(0 if run()['all_checks_pass'] else 1)
