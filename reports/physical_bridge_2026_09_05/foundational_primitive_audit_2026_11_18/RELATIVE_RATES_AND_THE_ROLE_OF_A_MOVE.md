# A law discriminator that survives a common change of clock

2026-11-18. Author hand continuation of the stationary-law control in
scope `6941e2b1b`; not independently checked. No scientific code, CAS,
enumeration or test was executed. This is an explicitly supplied finite
probabilistic model, not a derivation of physical probability or time.

## 1. Why the first control needs this qualification

The earlier P_t=Pi+t(I-Pi) example has only one nonzero decay factor.
After additional assumptions about continuous time, changing that factor
can amount to changing a clock unit. Its original clock caveat is retained.
It does not by itself demonstrate a relative interaction parameter.

The following example supplies two correlation channels and keeps their
dimensionless rate ratio. It also separates an admitted physical update
from a redescription under which a fixed law is required to be invariant.

## 2. Same internal state, explicitly supplied stochastic dynamics

Use S_2={(x,r):x,r in Z/2Z} from the first packet. On real functions on
S_2 define the pullbacks of the two coordinate flips by F_x and F_r.
They commute, square to I, and their product flips both coordinates.
Let Pi f be the constant function whose value is the uniform average
of f. For supplied positive rates a,b,c define

    L=a(F_x+F_r-2I)+b(F_x F_r-I)+c(Pi-I).             (1)

The row convention is that L acts on column functions; distributions
act on its left. All off-diagonal entries of L are nonnegative and each
row sums to zero. It is symmetric and has zero column sums as well.
P_s=exp(sL), s>=0, is the chosen continuous-time transition rule.
The exponential and this continuous-time framework are supplied here.

The first three terms give independent Poisson flips, or equivalently
products of the stochastic factors

    exp[t(F-I)] = ((1+exp(-2t))/2) I
                    +((1-exp(-2t))/2) F             (2)

for an involution F. Thus their exponential P_s^0 is stochastic.
Since Pi commutes with these flips and Pi^2=Pi,

    P_s=exp(-cs) P_s^0+(1-exp(-cs)) Pi.               (3)

Every entry is therefore strictly positive for s>0. In the original
binary construction U,V,J generate S4, as proved in the first packet.
The average of its 24 permutation pullbacks is Pi. The c term can
therefore be implemented by a rate-c Poisson process choosing a
uniform group transformation. Every named complete transformation has
positive selection rate, including U and J. Every finite prescribed
sequence of those jump labels has positive probability on a finite
time interval. This is a declared stochastic implementation, not a
proof that every infinite history physically occurs.

## 3. Unique stationary state, distinct relative correlations

A basis of the four function dimensions is

    1, f_x=(-1)^x, f_r=(-1)^r, f_p=(-1)^(x+r).

The latter three functions have zero uniform mean. Direct substitution
into (1) gives

    L 1=0,
    L f_x=-[2(a+b)+c] f_x,
    L f_r=-[2(a+b)+c] f_r,
    L f_p=-[4a+c] f_p.                               (4)

The three nonconstant eigenvalues are negative. Hence the uniform
distribution is the unique stationary distribution: these four
eigenfunctions exhaust the state space, and only the constant channel
has eigenvalue zero. The symmetric transition rule satisfies detailed
balance with this distribution.

For a stationary process and either of the zero-mean functions in (4),
the conditional-expectation calculation in the first packet yields

    E[f_x(X_0) f_x(X_s)] = exp(-lambda_x s),
    E[f_p(X_0) f_p(X_s)] = exp(-lambda_p s),
    lambda_x=2(a+b)+c,  lambda_p=4a+c,                (5)

because both squared functions equal one. A common change of time
unit scales both rates by the same factor. It preserves

    R=lambda_p/lambda_x=(4a+c)/(2(a+b)+c).             (6)

R varies with the supplied relative rates. For example (a,b,c)=(1,1,1)
gives R=1, whereas (1,2,1) gives R=5/7. These typed rate choices are
opposite mathematical controls, not empirical inputs or physical fits.
Even an arbitrary common monotone reparameterization of time cannot
make their two correlation pairs coincide: eliminating s in (5) gives
C_p=C_x^R. No physical input is counted from this toy ratio; its purpose
is to ensure that the freedom in this comparison is more than a clock.
The two example spectra have respectively a triple nonzero eigenvalue
and a double plus a distinct simple one. A permutation of the four
states combined with a common clock scaling cannot identify them either.

## 4. What an extra symmetry would actually earn

Equation (1) is invariant under coordinate translations and the exchange
J(x,r)=(r,x). The two single-coordinate rates are equal by construction.
Both coordinates interact through the common two-coordinate jumps.
The law is not generally invariant under the shear U(x,r)=(x,r+x).
Legal occurrence of U does not by itself require such invariance.

Conjugation by U fixes F_r, exchanges F_x with F_x F_r, and fixes Pi.
Consequently U invariance of this L holds exactly when a=b. The three
nonidentity flip pullbacks are linearly independent as part of the
regular action of Z2 x Z2; their coefficients can therefore be compared.
When a=b,

    I+F_x+F_r+F_x F_r=4Pi,
    L=(4a+c)(Pi-I),  R=1.                            (7)

Thus an additionally justified U-redescription symmetry would eliminate
the relative correlation distinction **within this supplied family**.
Only the total clock rate remains in its state transition kernel;
a and c can still distinguish separately labeled jump implementations.
No label information is silently erased by calling those implementations
identical as whole models.

This is a conditional positive, not a derivation that U must be a gauge
change. Treating every allowed active process as a law symmetry would
insert the condition that does the work. Conversely an example without
that condition does not refute a theory that explicitly includes it.

## 5. Consequence for the foundations question

The common stationary state, all finite histories in the support and
internal registration do not select R for this package. A precise extra
equivalence requirement can select it within the example. The earning
duty is therefore concrete: identify which transformations are active
interactions and which are changes of description, and derive or price
why the latter must preserve the same law, tests and registering data.

This extends the existing law-versus-fixed-sector distinction; it does
not rediscover that distinction or select the OA physical action.
The example does not test PF5's stronger whole-reading closure functional,
quantum amplitudes, qualia, the full OA grammar, SM3 or gravity.
