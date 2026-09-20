# F06 post-failure correction design, sealed before corrected execution

The first sealed run returned 16 passes and one failure at the predicted
H1 characteristic polynomial. The producer assembled the exact wedge/
contraction matrix; the written expectation had omitted one positive term
in ||T* u||^2. This diagnosis is made AFTER seeing that failure and is not
represented as a successful initial prediction.

Corrected expected quadratic form:

    (|tr b|^2 + 3 sum |t_i|^2 + sum_(i<j)|b_ij-b_ji|^2)/4.

Expected eigenvalues: zero (5), 1/2 (3), 3/4 (4), not the original
zero (5), 1/2 (6), 3/4 (1). The five-dimensional symmetric trace-free
kernel is still expected, but the first run did not reach that assertion.

Do not modify the producer or any initial sealed file. test_verify_v2.py
explicitly reruns all sixteen unaffected original test functions and
replaces the failed expectation with a corrected test that also retains
all formerly unreached assertions. Additional controls independently
construct T* u and Tu from general complex components, compare their
norm with the matrix quadratic form, and exhibit a unit vector on which
the old omitted term gives the wrong answer. Both the actual polynomial
and the wrong old polynomial must be distinguished.

The addendum changes only PROOF section 5's algebraic spectrum/norm.
No background, metric, equation, boundary, Einstein coupling, source
or global physical scope is changed. An unexpected new failure must be
preserved rather than adjusted silently. No corrected execution before
this design/addendum/test are hashed and committed.
