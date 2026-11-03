"""Five prospective register/flavour source controls. UNRUN and unadmitted.

Do not import, collect or execute before the source-complete prospective gate,
independent review and main's exact separate acceptance. Finite comparators
support the authored proof; they do not derive the physical register map.
"""
from __future__ import annotations

import unittest
import sympy as sp


def dagger(x):
    return x.conjugate().T


def bracket(x, y):
    return x * y - y * x


def units():
    qi = sp.diag(sp.I, -sp.I)
    qj = sp.Matrix([[0, 1], [-1, 0]])
    gl = (sp.eye(2) + qi) / sp.sqrt(2)
    gr = (sp.eye(2) - qj) / sp.sqrt(2)
    return qi, qj, gl, gr


def d5_source():
    e5 = sp.zeros(5)
    for j, c in enumerate((2, sp.sqrt(6), sp.sqrt(6), 2)):
        e5[j + 1, j] = c
    h5 = sp.diag(-4, -2, 0, 2, 4)
    j5 = sp.zeros(5)
    for j, c in enumerate((1, -1, 1, -1, 1)):
        j5[j, 4 - j] = c
    bz = sp.zeros(5)
    for j, k, c in ((1, 4, sp.sqrt(sp.Rational(2, 5))),
                    (2, 3, -sp.sqrt(sp.Rational(3, 5)))):
        bz[j, k] = c
        bz[k, j] = -c
    zz = sp.zeros(5)
    e = sp.diag(e5, -e5.T)
    h = sp.diag(h5, -h5.T)
    g = sp.sqrt(10) * zz.row_join(bz).col_join((j5 * bz * j5).row_join(zz))
    ep, em = (e + g) / 2, (e - g) / 2
    hp, hm = bracket(ep, dagger(ep)), bracket(em, dagger(em))
    return e, g, h, ep, em, hp, hm


def kappa(x):
    return sp.trace(x) / 2


def rotate(u, pair):
    z = sp.zeros(pair[0].rows)
    return tuple(sum((u[a, b] * pair[b] for b in range(2)), z)
                 for a in range(2))


def density(pair):
    return sp.Matrix(2, 2, lambda a, b: kappa(dagger(pair[b]) * pair[a]))


def pencil(pair, z):
    return z[0] * pair[0] + z[1] * pair[1]


def quartic(pair, z):
    x = pencil(pair, z)
    c = bracket(x, dagger(x))
    return sp.expand(kappa(c * c))


def ad2(x):
    """Traceless 2x2 comparator, coordinates E,F,H; retain its full adjoint."""
    basis = (sp.Matrix([[0, 1], [0, 0]]),
             sp.Matrix([[0, 0], [1, 0]]), sp.diag(1, -1))
    cols = []
    for b in basis:
        c = bracket(x, b)
        cols.append(sp.Matrix([c[0, 1], c[1, 0], c[0, 0]]))
    return sp.Matrix.hstack(*cols)


def physical_mass(q, r, omega, pbar, pz):
    """All four physical Weyl slots, exactly in the source mass convention."""
    aq, ar, aqd, ard = ad2(q), ad2(r), ad2(dagger(q)), ad2(dagger(r))
    eye, zero, rt = sp.eye(3), sp.zeros(3), sp.sqrt(2)
    rows = (
        (zero, -pz * eye / (rt * omega**2),
         rt * sp.I * aqd / omega, rt * sp.I * ard / omega),
        (rt * pz * eye, zero, -2 * sp.I * ar, 2 * sp.I * aq),
        (-rt * sp.I * aqd, sp.I * ar / omega, zero, pbar * eye / omega),
        (-rt * sp.I * ard, -sp.I * aq / omega, -pbar * eye / omega, zero),
    )
    return sp.Matrix.vstack(*(sp.Matrix.hstack(*row) for row in rows))


def input_map(u):
    return sp.diag(sp.eye(6), sp.kronecker_product(u, sp.eye(3)))


def output_map(u):
    return sp.diag(sp.eye(6), sp.kronecker_product(u.conjugate(), sp.eye(3)))


class RegisterFlavourJointChecks(unittest.TestCase):
    def assert_matrix_zero(self, x):
        self.assertTrue(all(sp.simplify(v) == 0 for v in x))

    def assert_scalar_zero(self, x):
        self.assertEqual(sp.simplify(sp.expand(x)), 0)

    def test_actual_two_triples_and_quartic_polynomial(self):
        e, g, h, ep, em, hp, hm = d5_source()
        for x, hx in ((ep, hp), (em, hm)):
            self.assert_matrix_zero(bracket(hx, x) - 2 * x)
            self.assert_scalar_zero(kappa(dagger(x) * x) - 10)
            self.assert_scalar_zero(kappa(hx * hx) - 20)
        self.assert_matrix_zero(hp + hm - h)
        for a in (ep, dagger(ep), hp):
            for b in (em, dagger(em), hm):
                self.assert_matrix_zero(bracket(a, b))
        self.assert_scalar_zero(kappa(hp * hm))
        self.assert_scalar_zero(kappa(dagger(e) * g))
        self.assert_scalar_zero(kappa(dagger(e) * e) - 20)
        self.assert_scalar_zero(kappa(dagger(g) * g) - 20)
        ell = sp.Symbol('ell', positive=True)
        n = 1 / (2 * sp.sqrt(2) * ell)
        x1, y1, x2, y2 = sp.symbols('x1 y1 x2 y2', real=True)
        z = (x1 + sp.I*y1, x2 + sp.I*y2)
        r2 = x1*x1 + y1*y1 + x2*x2 + y2*y2
        sx = 2 * (x1*x2 + y1*y2)
        direct = quartic((n*e, n*g), z)
        expected = sp.Rational(5, 8) * (r2*r2 + sx*sx) / ell**4
        self.assert_scalar_zero(direct - expected)
        # The polynomial is not determined by the common quadratic density.
        self.assertNotEqual(sp.Poly(sp.expand(direct), x1,y1,x2,y2),
                            sp.Poly(sp.expand(sp.Rational(5,8)*r2*r2/ell**4),
                                    x1,y1,x2,y2))

    def test_complete_mass_map_flavour_intertwiner(self):
        _, _, gl, gr = units()
        omega = sp.Symbol('Omega', positive=True)
        pbar, pz = sp.symbols('pbar pz')
        q = sp.Matrix([[1+sp.I, 1], [0, -1-sp.I]])
        r = sp.Matrix([[sp.I, 0], [1, -sp.I]])
        self.assertNotEqual(bracket(q, r), sp.zeros(2))
        mass = physical_mass(q, r, omega, pbar, pz)
        self.assertEqual(mass.shape, (12, 12))
        self.assertNotEqual(mass[:3, 6:9], sp.zeros(3))
        self.assertNotEqual(mass[6:9, :3], sp.zeros(3))
        self.assertNotEqual(mass[3:6, 6:9], sp.zeros(3))
        gram3 = sp.diag(1,1,2)
        metric = sp.diag(omega**2 * gram3, gram3/2,
                         omega*gram3, omega*gram3)
        for u in (gl, gr):
            qp, rp = rotate(u, (q,r))
            tin, tout = input_map(u), output_map(u)
            moved = physical_mass(qp, rp, omega, pbar, pz)
            self.assert_matrix_zero(moved*tin - tout*mass)
            self.assert_matrix_zero(dagger(tin)*metric*tin - metric)
            self.assert_matrix_zero(dagger(tout)*metric*tout - metric)
        qp, rp = rotate(gl, (q,r))
        wrong = physical_mass(qp,rp,omega,pbar,pz)*input_map(gl) - input_map(gl)*mass
        self.assertTrue(any(sp.simplify(x) != 0 for x in wrong))

    def test_irreducible_holonomy_gram_constraint(self):
        fi, fj, _, _ = units()
        x, y, c, d = sp.symbols('x y c d', real=True)
        den = sp.Matrix([[x,c+sp.I*d],[c-sp.I*d,y]])
        first = fi*den*dagger(fi) - den
        self.assert_scalar_zero(first[0,1] + 2*(c+sp.I*d))
        second = fj*den.subs({c:0,d:0})*dagger(fj) - den.subs({c:0,d:0})
        self.assert_matrix_zero(second - sp.diag(y-x,x-y))
        unequal = sp.diag(2,1)
        self.assert_matrix_zero(fi*unequal*dagger(fi) - unequal)
        self.assertNotEqual(fj*unequal*dagger(fj), unequal)
        rank1 = sp.diag(1,0)
        self.assertEqual(rank1.rank(), 1)
        self.assertNotEqual(fj*rank1*dagger(fj), rank1)
        self.assert_matrix_zero(fj*sp.eye(2)*dagger(fj)-sp.eye(2))
        e,g,_,_,_,_,_ = d5_source()
        a,b,ell = sp.symbols('a b ell', positive=True)
        physical = density((a*e/(2*ell), b*g/(2*ell)))
        self.assert_matrix_zero(physical - sp.diag(5*a*a/ell**2,5*b*b/ell**2))
        constraint = sp.expand((physical[1,1]-physical[0,0])*ell**2/5)
        self.assert_scalar_zero(constraint.subs(b*b,1-a*a) - (1-2*a*a))
        balanced = physical.subs({a:1/sp.sqrt(2),b:1/sp.sqrt(2)})
        self.assert_matrix_zero(balanced - 5*sp.eye(2)/(2*ell**2))
        # This control supplies no compact compensator or global holonomy map.

    def test_three_same_parent_stationary_states_and_readouts(self):
        _, _, gl, gr = units()
        e,g,h,_,_,_,_ = d5_source()
        ell = sp.Symbol('ell', positive=True)
        n = 1/(2*sp.sqrt(2)*ell)
        source = (n*e,n*g)
        states = (source, rotate(gl,source), rotate(gr,source))
        probes = ((1/sp.sqrt(2),1/sp.sqrt(2)),
                  (1/sp.sqrt(2),sp.I/sp.sqrt(2)), (sp.Integer(1),sp.Integer(0)))
        table = sp.zeros(3)
        scale = sp.Rational(5,8)/ell**4
        for a,pair in enumerate(states):
            self.assert_matrix_zero(bracket(pair[0],pair[1]))
            moment = sum((bracket(x,dagger(x)) for x in pair),sp.zeros(10))
            self.assert_matrix_zero(moment - h/(4*ell**2))
            self.assert_matrix_zero(density(pair)-5*sp.eye(2)/(2*ell**2))
            for x in pair:
                self.assert_matrix_zero(bracket(h,x)-2*x)
            for b,z in enumerate(probes):
                table[a,b] = sp.simplify(quartic(pair,z)/scale)
        self.assert_matrix_zero(table - (sp.ones(3)+sp.eye(3)))
        for a in range(3):
            for b in range(a+1,3):
                self.assertNotEqual(table.row(a),table.row(b))
        # Same stationary equations and same Gram do not erase the reference readout.
        # Three readout classes are not three particles/generations or an orbit census.

    def test_covariant_reference_and_register_composition_controls(self):
        fi,fj,gl,gr = units()
        e,g,_,_,_,_,_ = d5_source()
        source = (e/(2*sp.sqrt(2)),g/(2*sp.sqrt(2)))
        x1,y1,x2,y2 = sp.symbols('x1 y1 x2 y2',real=True)
        z = sp.Matrix([x1+sp.I*y1,x2+sp.I*y2])
        for u in (gl,gr,gl*gr):
            moved = rotate(u,source)
            moved_z = u.inv().T*z
            self.assert_matrix_zero(pencil(moved,moved_z)-pencil(source,z))
            self.assert_scalar_zero(quartic(moved,moved_z)-quartic(source,z))
        fixed_z = (1/sp.sqrt(2),1/sp.sqrt(2))
        self.assertNotEqual(sp.simplify(quartic(rotate(gl,source),fixed_z)),
                            sp.simplify(quartic(source,fixed_z)))
        comm = fi*fj.inv()*fi.inv()*fj
        delta = gl*gr.inv()*gl
        self.assert_matrix_zero(comm+sp.eye(2))
        self.assert_matrix_zero(delta**2+sp.eye(2))
        self.assert_matrix_zero(delta**4-sp.eye(2))
        eps = input_map(-sp.eye(2))
        jc = input_map(comm)
        self.assertNotEqual(eps,sp.eye(12))
        self.assert_matrix_zero(eps-jc)
        self.assert_matrix_zero(eps*jc-sp.eye(12))
        self.assert_matrix_zero(input_map(delta)**4-sp.eye(12))
        # epsilon*J_c remains based-nontrivial in E: this physical-sector action
        # has a kernel and cannot replace the separately retained full register.


if __name__ == '__main__':
    unittest.main()
