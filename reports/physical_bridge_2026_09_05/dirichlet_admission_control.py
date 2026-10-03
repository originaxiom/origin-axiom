"""R81 separate exact Fraction comparator. No native/SymPy imports."""
from fractions import Fraction as Q
import json


def mat(a, b, c, d):
    return ((Q(a), Q(b)), (Q(c), Q(d)))


def add(a, b):
    return tuple(tuple(a[i][j]+b[i][j] for j in range(2)) for i in range(2))


def mul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def scale(a, t):
    return tuple(tuple(Q(t)*a[i][j] for j in range(2)) for i in range(2))


def transpose(a):
    return tuple(tuple(a[j][i] for j in range(2)) for i in range(2))


def comm(a, b):
    return add(mul(a, b), scale(mul(b, a), -1))


def checks():
    rows = {}
    J, N, zero = mat(1, 0, 0, -1), mat(0, 1, 0, 0), mat(0, 0, 0, 0)
    identity, L = mat(1, 0, 0, 1), mat(1, 1, 0, 1)
    rows['nilpotent'] = mul(N, N) == zero
    rows['primitive'] = add(identity, N) == L
    rows['nonsplit'] = N != zero and mul(N, N) == zero and N[0][1] == 1
    # tan(s)=2u/(1-u^2), sec(s)=(1+u^2)/(1-u^2), |u|<1.
    # Jets are with respect to s: tan'=sec^2, sec'=sec*tan.
    for u in (Q(-1, 3), Q(-1, 5), Q(0), Q(1, 5), Q(1, 3)):
        label = str(u)
        t, z = 2*u/(1-u*u), (1+u*u)/(1-u*u)
        Cs, Cx = scale(J, -t/2), scale(N, -z)
        dCs, dCx = scale(J, -z*z/2), scale(N, -z*t)
        H = mat(z, 0, 0, 1/z)
        rows['positive:'+label] = z > 0 and H[1][1] > 0
        rows['det:'+label] = H[0][0]*H[1][1] == 1
        rows['trig:'+label] = z*z-t*t == 1
        rows['flat:'+label] = add(dCx, comm(Cs, Cx)) == zero
        rows['moment:'+label] = add(scale(dCs, 2), comm(Cx, transpose(Cx))) == zero
        rows['norm:'+label] = Cx[0][1]**2 == z*z
        rows['flux:'+label] = sum(mul(J, Cs)[i][i] for i in range(2)) == -t
        rows['holonomy:'+label] = add(identity, scale(Cx, -1))[0][1] == z
        # For u=0 the flipped radial curvature happens to vanish, but I doesn't.
        rows['wrong_moment:'+label] = add(scale(dCs, -2), comm(Cx, transpose(Cx))) != zero
        if u:
            rows['wrong_flat:'+label] = add(dCx, comm(scale(Cs, -1), Cx)) != zero
    for endpoint_tan in (Q(1, 2), Q(1), Q(2), Q(3)):
        bulk, flux = 2*endpoint_tan, -2*endpoint_tan
        rows['balance:'+str(endpoint_tan)] = 2*bulk+2*flux == 0
        rows['drop:'+str(endpoint_tan)] = 2*bulk > 0
        rows['wrong_normal:'+str(endpoint_tan)] = 2*bulk-2*flux > 0
    rows['split_control'] = comm(zero, zero) == zero
    return rows


if __name__ == '__main__':
    rows = checks()
    print(json.dumps({'audit': 'R81 reference', 'checks': rows,
                      'passed': sum(rows.values()), 'total': len(rows)}, indent=2))
    raise SystemExit(0 if all(rows.values()) else 1)
