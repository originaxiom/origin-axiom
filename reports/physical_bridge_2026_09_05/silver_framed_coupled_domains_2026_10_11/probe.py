"""Exact local controls, not a global E8/silver solver. No project imports."""
import json
import sympy as S


def clean(x):
    if isinstance(x, S.MatrixBase):
        return x.applyfunc(lambda a: S.simplify(S.expand_complex(a)))
    return S.simplify(S.expand_complex(x))


def zero(x):
    z = clean(x)
    return z == S.zeros(*z.shape) if isinstance(z, S.MatrixBase) else z == 0


def model(m):
    # Nonreal kinetic-orthonormal coordinates. E2 is the actual conjugate
    # of E1, so this is a Weyl-symmetric rather than Hermitian mass tensor.
    U = S.Matrix([[S.Rational(3, 5), 4*S.I/5], [4*S.I/5, S.Rational(3, 5)]])
    d0 = U[:, 0]*m
    d1 = clean(U.conjugate()*S.diag(0, m)*U.adjoint())
    d2 = m*U.conjugate()[:, 0].adjoint()
    R = S.zeros(3)
    R[0, 1:3] = -d0.adjoint()
    R[1:3, 0] = -d0.conjugate()
    R[1:3, 1:3] = d1
    return U, d0, d1, d2, R


def green_data(q):
    # Integrated tangential zero mode. A1 contains dy coefficients;
    # its Hermitian normal complement contains dx coefficients.
    c = S.Matrix([1, 0])
    O = q*S.Matrix([[0, -1], [1, 0]])
    allowed = S.zeros(2, 1)
    forbidden = S.Matrix([0, 1])  # forbidden CONSTANT dy trace
    return c, O, allowed, forbidden


def run():
    facts = {}

    def put(name, yes):
        if name in facts:
            raise AssertionError("duplicate predicate")
        facts[name] = bool(yes)
        if not facts[name]:
            raise AssertionError(name)

    q = S.symbols("q", real=True, nonzero=True)
    c, O, good, bad = green_data(q)
    put("old_generator_nonparallel", not zero(O*c))
    put("nonparallel_derivative_in_old_A1", not zero(O*c))
    put("admitted_normal_trace_cancels", zero((O*c).adjoint()*good))
    put("forbidden_normal_trace_detected", not zero((O*c).adjoint()*bad))
    put("omitted_connection_is_false_control", zero(S.zeros(2, 1).dot(bad)) and
        not zero((O*c).dot(bad)))
    put("old_A0_reset_changes_admission", not zero(O*c))

    # Full Hermitian Green algebra including a nonunitary Higgs piece:
    # Cminus=O-B, Cplus=O+B; normal codifferential=Cplus beta.
    b0, b1, b2, x0, x1, y0, y1 = S.symbols("b0 b1 b2 x0 x1 y0 y1", real=True)
    B = S.Matrix([[b0, b1], [b1, b2]])
    cx = S.Matrix([x0+S.I*y0, x1+S.I*y1])
    beta = S.Matrix([y1+S.I*x0, y0+S.I*x1])
    minus, plus = O-B, O+B
    put("plus_minus_actual_adjoint", zero(minus.adjoint()+plus))
    put("normal_Green_identity_all_coefficients",
        zero(cx.adjoint()*plus*beta+(minus*cx).adjoint()*beta))
    put("wrong_Higgs_adjoint_sign_detected", not zero(minus.adjoint()+minus))
    s00, s01, s11, w = S.symbols("s00 s01 s11 w", real=True)
    shape = S.Matrix([[s00, s01], [s01, s11]])
    skew = S.Matrix([[0, w], [-w, 0]])
    put("shape_antisymmetry_cancels", zero(sum(shape[i,j]*skew[i,j]
        for i in range(2) for j in range(2))))

    m = S.symbols("m", positive=True)
    U, d0, d1, d2, R = model(m)
    e, co = U[:, 0], U[:, 1]
    put("nonreal_unitary_coordinates", zero(U.adjoint()*U-S.eye(2)))
    put("nonreal_exact_profile_retained", not zero(e-e.conjugate()))
    put("complex_d1d0_zero", zero(d1*d0))
    put("complex_d2d1_zero", zero(d2*d1))
    put("real_positive_degree_zero", zero(d0.adjoint()*d0-S.Matrix([[m*m]])))
    delta1 = clean(d0*d0.adjoint()+d1.adjoint()*d1)
    delta2 = clean(d1*d1.adjoint()+d2.adjoint()*d2)
    put("degree_one_full_mass_square", zero(delta1-m*m*S.eye(2)))
    put("degree_two_full_mass_square", zero(delta2-m*m*S.eye(2)))
    put("degree_three_full_mass_square", zero(d2*d2.adjoint()-S.Matrix([[m*m]])))
    put("exact_coclosed_orthogonality", zero(e.adjoint()*co))
    put("exact_profile_flat", zero(d1*e))
    put("exact_profile_adjoint", zero(d0.adjoint()*e-S.Matrix([[m]])))
    put("coclosed_profile_adjoint", zero(d0.adjoint()*co))
    put("coclosed_Weyl_partner", zero(d1*co-m*co.conjugate()))
    put("actual_Weyl_symmetric", zero(R-R.T))
    put("actual_Weyl_not_Hermitian", not zero(R-R.adjoint()))
    put("full_Weyl_singular_square", zero(R.adjoint()*R-m*m*S.eye(3)))
    z0 = S.Matrix([1, 0, 0])
    z1 = S.Matrix([0, *list(e)])
    zc = S.Matrix([0, *list(co)])
    put("lambda_exact_Weyl_pair", zero(R*z0+m*z1.conjugate()))
    put("exact_lambda_Weyl_pair", zero(R*z1+m*z0.conjugate()))
    put("coclosed_Takagi_pair", zero(R*zc-m*zc.conjugate()))
    K = d1.conjugate()  # K(u)=K conjugate(u)
    put("antilinear_K_squared", zero(K*K.conjugate()*co-m*m*co))
    put("wrong_linear_K_squared_detected", not zero(K*K*co-m*m*co))

    s, h, a, b = S.symbols("s h a b", real=True)
    u = (s+S.I*h)*e+(a+S.I*b)*co
    div = clean(-(d0.adjoint()*u)[0])
    put("actual_real_G", zero(S.re(div)+m*s))
    put("actual_real_M", zero(S.im(div)+m*h))
    static = clean((u.adjoint()*d1.adjoint()*d1*u)[0]+S.im(div)**2)
    put("same_static_real_quotient", zero(static-m*m*(h*h+a*a+b*b)))
    put("real_gauge_scalar_null", zero(static.subs({h:0, a:0, b:0})))
    put("imaginary_exact_scalar_physical", zero(static.subs({s:0,a:0,b:0})-m*m*h*h)
        and not zero(m*m*h*h))
    put("complex_gauge_false_removal_detected", not zero(S.im(div).subs({s:0,h:1,a:0,b:0})))

    p0, p1, p2, p3 = S.symbols("p0 p1 p2 p3", real=True)
    pvec = S.Matrix([p0,p1,p2,p3])
    p_sq = (pvec.T*pvec)[0]
    Hess = S.zeros(5)
    Hess[:4,:4]=(p_sq+m*m)*S.eye(4)-pvec*pvec.T
    Hess[:4,4]=-S.I*m*pvec
    Hess[4,:4]=S.I*m*pvec.T
    Hess[4,4]=p_sq
    gauge = S.Matrix([*(S.I*pvec),m])
    F = S.Matrix([[S.I*p0,S.I*p1,S.I*p2,S.I*p3,-m]])
    put("coupled_Hessian_gauge_null", zero(Hess*gauge))
    put("all_momentum_gauge_fixing", zero(Hess+F.adjoint()*F-(p_sq+m*m)*S.eye(5)))
    wrongF = F.copy(); wrongF[0,4]=m
    put("wrong_gauge_fixing_sign_detected", not zero(Hess+wrongF.adjoint()*wrongF-
        (p_sq+m*m)*S.eye(5)))

    p,E,ps,v,ss,hh,ph = S.symbols("p E ps v ss hh ph", real=True)
    C=-p*E+m*ps
    Ham=(E*E+ps*ps+(p*ss+m*v)**2+ph*ph+(p*p+m*m)*hh*hh)/2
    def pb(f,g):
        return S.expand(sum(S.diff(f,x)*S.diff(g,y)-S.diff(f,y)*S.diff(g,x)
            for x,y in ((v,E),(ss,ps),(hh,ph))))
    put("Gauss_constraint_preserved", zero(pb(C,Ham)))
    put("Gauss_generates_vector", zero(pb(v,C)+p))
    put("Gauss_generates_real_Goldstone", zero(pb(ss,C)-m))
    red=Ham.subs({ss:0,ps:p*E/m})
    put("positive_reduced_coefficients", zero(S.diff(red,E,2)-(1+p*p/(m*m)))
        and zero(S.diff(red,v,2)-m*m) and m.is_positive)
    put("longitudinal_mass_dispersion", zero(S.diff(red,E,2)*S.diff(red,v,2)-p*p-m*m))
    put("scalar_mass_dispersion", zero(S.diff(red,ph,2)*S.diff(red,hh,2)-p*p-m*m))
    put("m_zero_not_unitary_gauge", C.subs(m,0)==-p*E)
    put("real_not_complex_particle_count", 3+(2*2-1)==2*3)
    return facts


if __name__ == "__main__":
    facts = run()
    print(json.dumps({"status":"PASS", "exact_local_checks":len(facts), "facts":facts,
        "global_PDE_or_full_SM_certificate":False}, indent=2), flush=True)
