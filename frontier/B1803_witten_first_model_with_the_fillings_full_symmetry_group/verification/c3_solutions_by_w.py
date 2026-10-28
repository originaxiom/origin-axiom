"""P-409 check: the referee's r8 enumeration for F' = Z/2 x Z/2, with the full solutions listed by w (the twisted point's
character), to see which w each solution needs. Conditions copied from r8 unchanged."""
import itertools
A = list(itertools.product((0, 1), repeat=2))
add = lambda a, b: ((a[0] + b[0]) % 2, (a[1] + b[1]) % 2)
zero = (0, 0)
by_w = {}
for alpha, sigma, tau, w in itertools.product(A, A, A, [x for x in A if x != zero]):
    gamma = alpha; delta = add(gamma, w)                      # -a = a in Z/2 x Z/2
    if add(alpha, delta) == zero: continue
    if add(alpha, add(sigma, sigma)) != zero: continue          # (2.3): alpha + 2 sigma = alpha
    if add(add(delta, sigma), tau) != zero: continue            # (2.4)
    at = add(alpha, tau)
    if at == zero: continue                                     # (2.6); (2.5) automatic
    if add(add(add(sigma, sigma), sigma), tau) == zero: continue  # (2.9)
    if add(sigma, add(tau, tau)) == zero: continue              # (2.8)
    by_w.setdefault(w, []).append(dict(alpha=alpha, sigma=sigma, tau=tau, w=w))
for w in sorted(by_w):
    print("w = %s: %d full solutions: %s" % (w, len(by_w[w]), by_w[w]))
print("total", sum(len(v) for v in by_w.values()))
