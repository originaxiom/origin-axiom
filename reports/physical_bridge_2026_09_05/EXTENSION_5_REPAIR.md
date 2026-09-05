# R7 second-derivative control repair, before rerun

BANKED IDENTITY: the first R7 execution failed in its full-Hessian second
finite difference, before any classical or quantum verdict. At step 1e-4,
12 of 86436 entries exceed the 3e-7 absolute tolerance, with a maximum
violation of 1.84087162e-6. First output and stderr are preserved separately.
No physics conclusion follows from that control failure.

PRIOR ART: the original constraints are degree at most two in the fields;
their squared potential has degree at most four, so its Hessian is degree
at most two. A centered second difference of that Hessian is algebraically
exact at every nonzero step, not merely at infinitesimal steps. The suspected
failure is roundoff amplified by division by 1e-8, not yet a verified cause.

P0: verify and repair the numerical control of the unchanged R7 model.
The new wrapper retains the original code and test bytes. Before rerunning,
seal a step sweep 1e-2,1e-3,1e-4, plus unit-step polarization. Require the
original 3e-7 second-derivative tolerance at steps 1e-2 and 1e-3, require
the analytic coefficient to agree with unit-step polarization to 1e-10,
and report all errors including the original failed step. Check two-sided
parameter controls and compact covariance again. No physics parameter,
Hessian formula, quantum criterion or tolerance is relaxed.

If those checks pass, run the unchanged classical/Yukawa/quantum instrument
through the wrapper to a new exclusively-created output. Otherwise preserve
that failure and diagnose further. This is a post-failure repair design,
not a blind discovery. Original small-step tests remain historical failing
controls; the focused certificate explicitly distinguishes the two corrected
controls from those old tests rather than claiming the full suite green.
