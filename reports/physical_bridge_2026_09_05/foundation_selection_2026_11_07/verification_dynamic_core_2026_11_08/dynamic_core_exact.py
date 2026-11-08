"""Unrun exact finite controls; all spectral/projection data are surrogates.

Design sealed at 09f478c79 before this implementation. These routines do
not solve the actual core PDE, select a geometry or count physical modes.
"""

from fractions import Fraction as F


def zeros(rows, cols):
    return [[F(0) for _ in range(cols)] for _ in range(rows)]


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def multiply(a, b):
    return [[sum((x * y for x, y in zip(row, col)), F(0))
             for col in zip(*b)] for row in a]


def inverse(a):
    n = len(a)
    if not n or any(len(row) != n for row in a):
        raise ValueError('A nonempty square matrix is required')
    out = [[F(x) for x in row] + identity(n)[i]
           for i, row in enumerate(a)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if out[i][j]), None)
        if pivot is None:
            raise ValueError('Singular matrix: retain kernel constraints')
        out[j], out[pivot] = out[pivot], out[j]
        divisor = out[j][j]
        out[j] = [x / divisor for x in out[j]]
        for i in range(n):
            if i != j:
                factor = out[i][j]
                out[i] = [x - factor * y for x, y in zip(out[i], out[j])]
    return [row[n:] for row in out]


def outer(a, b):
    return [[x * y for y in b] for x in a]


def bessel_polynomial(l):
    """K_(l+1/2) = common exp(-z)/sqrt(z) times sum_j P[j] z^-j."""
    if not isinstance(l, int) or l < 0:
        raise ValueError('Nonnegative integer half-order required')
    previous, current = [F(1)], [F(1), F(1)]
    if l == 0:
        return tuple(previous)
    for j in range(1, l):
        following = [F(0)] * (len(current) + 1)
        for k, x in enumerate(previous):
            following[k] += x
        for k, x in enumerate(current):
            following[k + 1] += (2 * j + 1) * x
        previous, current = current, following
    return tuple(current)


def angular_tail_scaled(l, z):
    """Return Y D_t and (ell^2/Y) R_t at z=|2pi n|Y>0.

    ell^2 s=l(l+1). Rational z is a dimensionless evaluation; this does
    not substitute a rational Fourier wave number into a fixed cusp.
    """
    z = F(z)
    if z <= 0:
        raise ValueError('Positive nonzero-angular argument required')
    p = bessel_polynomial(l)
    value = sum((c * z ** (-j) for j, c in enumerate(p)), F(0))
    derivative = sum((-j * c * z ** (-j - 1)
                      for j, c in enumerate(p)), F(0))
    vector = z * (1 - derivative / value)
    scalar = F(l * (l + 1)) / vector
    return vector, scalar


def mean_tail(nu, ell2, cut):
    nu, ell2, cut = F(nu), F(ell2), F(cut)
    if nu < 1 or ell2 <= 0 or cut <= 0:
        raise ValueError('Admitted real power branch and positive metric required')
    return cut * (nu + 1) / (2 * ell2), (nu - 1) / (2 * cut)


def spectral_core_surrogate(s, area, circulation, spectral_rows):
    """Finite algebra only: rows are (positive lambda, boundary covector).

    circulation is B in the proof. No row is an actual core eigenfunction
    or an independently chosen boundary parameter of the physical theory.
    """
    s, area = F(s), F(area)
    if s < 0 or area <= 0:
        raise ValueError('Nonnegative Euclidean parameter and positive area required')
    n = len(circulation)
    response = scale(1 / area, outer(circulation, circulation))
    derivative = zeros(n, n)
    for eigenvalue, covector in spectral_rows:
        eigenvalue = F(eigenvalue)
        if eigenvalue <= 0 or len(covector) != n:
            raise ValueError('Separate scalar constant from positive spectral rows')
        block = outer(covector, covector)
        response = add(response, scale(s / (eigenvalue + s), block))
        derivative = add(derivative,
                         scale(eigenvalue / (eigenvalue + s) ** 2, block))
    return response, derivative


def relative_harmonic_core_block(s, gram):
    """Retained OFF-SHELL core coordinates, not globally matched particles."""
    if F(s) < 0:
        raise ValueError('Nonnegative Euclidean parameter required')
    return scale(F(s), gram)


def dual_response_and_derivative(s, scalar_dtn, scalar_dtn_prime):
    if F(s) <= 0:
        raise ValueError('Do not invert the zero-parameter gauge chart')
    inv = inverse(scalar_dtn)
    response = scale(F(s), inv)
    prime = add(inv, scale(-F(s), multiply(multiply(inv, scalar_dtn_prime), inv)))
    return response, prime


def boundary_gauge_matrix(vector_response, connection_response, angular_k, p):
    """Quadratic form D |v_T|^2 + R |b-k p.v/s|^2; real coefficients."""
    p = tuple(F(x) for x in p)
    s = sum((x * x for x in p), F(0))
    if s == 0:
        raise ValueError('Zero momentum requires a full-field gauge limit')
    w = (F(1),) + tuple(-F(angular_k) * x / s for x in p)
    out = scale(F(connection_response), outer(w, w))
    for i in range(len(p)):
        for j in range(len(p)):
            out[i + 1][j + 1] += F(vector_response) * (F(i == j) - p[i] * p[j] / s)
    return out


def vbb_overlaps(nu_p, nu_q, nu_k, cut):
    nu_p, nu_q, nu_k, cut = map(F, (nu_p, nu_q, nu_k, cut))
    if min(nu_p, nu_q, nu_k) < 1 or cut <= 0:
        raise ValueError('Normalizable Euclidean branch and positive cut required')
    longitudinal = 2 * cut / (nu_p + nu_q)
    transverse = 2 * cut / (nu_p + nu_q + nu_k - 1)
    return transverse, longitudinal


def vbb_projector_coefficient(nu_p, nu_q, nu_k, ell2, cut):
    """The removable (I_L-I_T)/k^2, including the nu_k=1 limit."""
    nu_p, nu_q, nu_k, ell2, cut = map(F, (nu_p, nu_q, nu_k, ell2, cut))
    if min(nu_p, nu_q, nu_k) < 1 or ell2 <= 0 or cut <= 0:
        raise ValueError('Normalizable branch and positive metric required')
    return 8 * ell2 * cut / ((nu_k + 1) * (nu_p + nu_q)
                             * (nu_p + nu_q + nu_k - 1))


def top_form_projection_surrogate(areas, source):
    """Weighted finite-cell minimization; not the cusp Poisson inverse."""
    areas, source = tuple(map(F, areas)), tuple(map(F, source))
    if not areas or len(areas) != len(source) or min(areas) <= 0:
        raise ValueError('Matching positive cell areas and scalar source required')
    area = sum(areas, F(0))
    integral = sum((w * f for w, f in zip(areas, source)), F(0))
    mean = integral / area
    correction = tuple(mean - f for f in source)
    energy = sum((w * (f + d) ** 2
                  for w, f, d in zip(areas, source, correction)), F(0))
    return correction, mean, energy


def commutator(a, b):
    return add(multiply(a, b), scale(-1, multiply(b, a)))


def trace(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def period_obstruction_compact_skew(pairs):
    """For skew A,B and Hermitian U=iA,V=iB, C=i sum[A,B].

    Hence kappa(C^2)=-Tr((sum[A,B])^2), evaluated exactly over reals.
    This faithful convention map avoids floating-point complex numbers.
    """
    if not pairs:
        raise ValueError('At least one handle is required')
    out = zeros(len(pairs[0][0]), len(pairs[0][0]))
    for a, b in pairs:
        if transpose(a) != scale(-1, a) or transpose(b) != scale(-1, b):
            raise ValueError('Compact skew inputs required by the convention map')
        out = add(out, commutator(a, b))
    return out, -trace(multiply(out, out))


def left_quaternion(q):
    a, b, c, d = map(F, q)
    return [[a, -b, -c, -d], [b, a, -d, c],
            [c, d, a, -b], [d, -c, b, a]]
