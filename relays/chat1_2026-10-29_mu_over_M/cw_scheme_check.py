"""What W150's mu/M~ is (data-free; symbolic). Higaki, Kawamura and Kobayashi's one-loop potential for one heavy pair
(their eq. 3.2, MS-bar, renormalization scale mu): a scalar of mass^2 m0^2 + u and a fermion of mass^2 u, where
u = m_Q(tau)^2 carries all the tau dependence.  Checks, by sympy:
  1. dV/du at large u is (m0^2/16 pi^2) log(u/mu^2) + O(m0^4/u): the minimum condition m_Q = mu (W150's H1).
  2. dV/d log mu^2 = -(m0^4 + 2 m0^2 u)/(32 pi^2): it depends on u, hence on tau.  So V alone is not
     renormalization-group invariant; a tree-level term c(mu) m0^2 u is needed, with dc/d log mu^2 = 1/(16 pi^2).
  3. With that term the large-u minimum is u* = mu^2 exp(-16 pi^2 c(mu)), and d u*/d mu = 0 under c's running:
     the height is set by one renormalization-group invariant, not by mu.  Setting c(mu) = 0 at mu = M~ is the paper's
     illustrative choice (its sec. 3.1, "Taking mu = M~_Q").
No measured number is read.  python3 -B cw_scheme_check.py > cw_scheme_check_out.txt"""
import sympy as sp

u, m0, mu, c0, L0 = sp.symbols("u m0 mu c0 L0", positive=True)
pi = sp.pi
V = ((m0**2 + u)**2 * (sp.log((m0**2 + u) / mu**2) - sp.Rational(3, 2)) - u**2 * (sp.log(u / mu**2) - sp.Rational(3, 2))) / (32 * pi**2)

dVdu = sp.diff(V, u)
lead = sp.series(dVdu.subs(u, 1 / sp.Symbol("e", positive=True)), sp.Symbol("e", positive=True), 0, 1).removeO()
lead = sp.simplify(lead.subs(sp.Symbol("e", positive=True), 1 / u))
print("1. dV/du at large u, leading:", sp.simplify(sp.expand_log(lead, force=True)))
print("   equals (m0^2/16 pi^2) log(u/mu^2):", sp.simplify(sp.expand_log(lead - m0**2 * sp.log(u / mu**2) / (16 * pi**2), force=True)) == 0)

t = sp.Symbol("t")                                    # t = log mu^2
Vt = V.subs(mu, sp.exp(t / 2))
dVdt = sp.simplify(sp.diff(Vt, t))
print("2. dV/d log mu^2 =", sp.factor(dVdt), " | u-dependent:", sp.diff(dVdt, u) != 0)

c = c0 + (t - L0) / (16 * pi**2)                      # c(mu) running, c = c0 at log mu^2 = L0
Vtot_lead = m0**2 * u * (sp.log(u) - t - 1) / (16 * pi**2) + c * m0**2 * u      # large-u form of V plus the tree term
print("   d(V_lead + c m0^2 u)/d log mu^2 =", sp.simplify(sp.diff(Vtot_lead, t)))
ustar = sp.solve(sp.Eq(sp.diff(Vtot_lead, u), 0), u)
print("3. large-u minimum u* =", [sp.simplify(x) for x in ustar], " | d u*/d log mu^2 =", [sp.simplify(sp.diff(x, t)) for x in ustar])
print("   at c(mu = M~) = 0 (the paper's choice) u* = M~^2:", sp.simplify(ustar[0].subs({c0: 0}).subs(t, L0)) == sp.exp(L0))
