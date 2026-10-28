"""Referee B1802, r8: Witten's first model (hep-ph/0201018 eqs. 2.1-2.9) over a finite abelian F' (characters written
additively in A).  Unknowns alpha (V), gamma, delta (triplet, doublet of V~), sigma (10's), tau (5bar's).  Conditions:
 split: alpha + gamma = 0 (Q Q~ allowed), alpha + delta != 0 (H H~ forbidden); geometric: delta - gamma = w (the W-twist's
 character at S2, w != 0); (2.3) alpha + 2 sigma = 0; (2.4) delta + sigma + tau = 0; (2.5) 2(alpha + tau) = 0;
 (2.6) alpha + tau != 0 [Witten: = -1, i.e. of order 2]; (2.8) sigma + 2 tau != 0; (2.9) 3 sigma + tau != 0.
Report solvability for A = Z/n (n = 2..6) and A = Z/2 x Z/2, with and without (2.8) (an extra matter parity forbids the
renormalizable (10)(5bar)^2, not the dimension-five (10)^3 (5bar))."""
import itertools
def solve(A, add, neg, zero, dbl, w_choices):
    sols = {"full": 0, "no (2.8)": 0, "split only": 0}
    for alpha, sigma, tau, w in itertools.product(A, A, A, w_choices):
        gamma = neg(alpha)
        delta = add(gamma, w)
        if add(alpha, delta) == zero: continue                  # doublet mass must be forbidden
        sols["split only"] += 1
        if add(alpha, dbl(sigma)) != zero: continue             # (2.3)
        if add(add(delta, sigma), tau) != zero: continue        # (2.4)
        at = add(alpha, tau)
        if dbl(at) != zero or at == zero: continue              # (2.5), (2.6)
        c29 = add(add(dbl(sigma), sigma), tau) != zero          # (2.9)
        if not c29: continue
        sols["no (2.8)"] += 1
        if add(sigma, dbl(tau)) != zero: sols["full"] += 1      # (2.8)
    return sols
for n in range(2, 7):
    A = list(range(n))
    r = solve(A, lambda a, b: (a + b) % n, lambda a: (-a) % n, 0, lambda a: (2 * a) % n, [w for w in A if w])
    print("F' = Z/%d: solutions %s" % (n, r))
A = list(itertools.product((0, 1), repeat=2))
add = lambda a, b: ((a[0] + b[0]) % 2, (a[1] + b[1]) % 2)
r = solve(A, add, lambda a: a, (0, 0), lambda a: (0, 0), [w for w in A if w != (0, 0)])
print("F' = Z/2 x Z/2: solutions %s" % r)
print("r8 exit 0")
