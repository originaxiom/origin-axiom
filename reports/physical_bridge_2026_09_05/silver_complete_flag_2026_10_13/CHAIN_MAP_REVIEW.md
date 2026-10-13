# Geometric origin of the degree two cusp restriction

Post-result review on October13, not a new preregistered experiment. The
existing formula was used unchanged by both sealed implementations. This
review checks why it is geometric, rather than merely a matrix solving
a chain equation. No coefficient or target rank is inferred from it.

Source: foundation commit5586a3c2d29598f89c5a046e62c832f8f228073b,
reports/silver_boundary_complex_2026_10_04/PROOF.md, section The full
restriction map. That proof and its producer restriction2 were read.

The marked fibre puncture is p=[a,b], stable letter t, and other cusp
generator q=c t with c=ab on this signed silver marking. The positive
Nielsen moves each fix p as a reduced free word. Inverting both generators
takes p to ABab=(ab)^-1 p(ab). Thus the marked automorphism obeys
phi(p)=c^-1 p c, without substituting a numerical representation.

Put r_g=t g T phi(g)^-1 for g=a,b and r_p=t p T phi(p)^-1.
The word identity [p,q]=c r_p^-1 c^-1 follows directly by substitution.
Expansion of r_p into conjugates of r_a,r_b gives the two-cell row

    (T Fox_a(p) T^-1, T Fox_b(p) T^-1).

One way to track it is r_(uv)=r_u phi(u) r_v phi(u)^-1; inverse letters
give the negative transported next prefix. Outer inversion and
conjugation multiply that row by -rho(c), so the stable-letter factors
produce

    R2=-Q(Fox_a(p) T^-1, Fox_b(p) T^-1), Q=rho(c)T.

This is the cellular image of the marked boundary commutator cell. The
orientation F_T=(I-Q,P-I) fixes its sign. The sealed computations check
R2 F=F_T R1 and its actual projected nonzero opposing-sign control.
Checking that identity alone would not distinguish arbitrary modifications
on bulk H2; the free-word cellular derivation supplies the missing type.

This review clarifies a previously inherited proof dependency. It is not
a third implementation, numerical geometric triangulation or new main
bank. The complete charged kernel remains conditional on the independent
analytic end reduction and the supplied flat coefficient and end class.
