#!/usr/bin/env python3
"""THE TREFOIL TESTS ADDENDUM 4's MECHANISM, AND SHARPENS IT AGAINST ME.

Memo 177 addendum 4 proposed   c_edge(K) = c_eff( 1 / Phi_K ),  Phi_K the colored Jones tail,
verified on the figure-eight: Phi = (q;q)_inf, c_edge = 1.  ONE data point.  The trefoil is the
cheapest second, because c_edge(trefoil) is known INDEPENDENTLY: by GM Thm 1.3 every Xi_k of a
torus knot is a single monomial, so there is no widening edge series at all and c_edge = 0.

The colored Jones of the trefoil, from Habiro's cyclotomic expansion

    J_n(3_1) = sum_{k>=0} (-1)^k q^{-k(k+3)/2} sigma_k(n),
    sigma_k(n) = prod_{j=1}^{k} (q^n + q^-n - q^j - q^-j),

checked below against J_2 = q^-1 + q^-3 - q^-4.  The trefoil is CHIRAL, so its two ends differ,
and that is the whole content of this certificate:

    bottom end (lowest degrees, same parity in n):  +- (q;q)_inf
    top end    (highest degrees, same parity):      1, 0, 0, 0, ...   -- TRIVIAL

while the figure-eight, being amphichiral, has (q;q)_inf at BOTH ends.

CONSEQUENCE, AND IT CUTS AGAINST THE MECHANISM AS I STATED IT.

  c_edge(trefoil) = 0 = c_eff(1/1) matches the TRIVIAL end.
  Had the mechanism used the (q;q)_inf end it would predict 1 and be WRONG.

So "Phi_K = the colored Jones tail" is too loose: it must say WHICH END, the answer is not the
same for the two, and the figure-eight -- the only knot the mechanism was verified on -- is
amphichiral and therefore CANNOT DISTINGUISH THEM.  The mechanism is not refuted; it is
under-determined, on a point its single verification could not see.

Honest count after this certificate: ONE knot on which the mechanism is verified, and ONE on
which it is consistent under one of two readings and false under the other.

Gate 5: exact integer Laurent arithmetic.
"""
def sigma(k, n):
    cur = {0: 1}
    for j in range(1, k+1):
        fac = {n: 1, -n: 1}
        fac[j] = fac.get(j, 0) - 1; fac[-j] = fac.get(-j, 0) - 1
        fac = {a: b for a, b in fac.items() if b}
        nx = {}
        for e1, c1 in cur.items():
            for e2, c2 in fac.items(): nx[e1+e2] = nx.get(e1+e2, 0) + c1*c2
        cur = {a: b for a, b in nx.items() if b}
    return cur

def Jtref(n):
    tot = {}
    for k in range(0, n):
        s = sigma(k, n); sh = -k*(k+3)//2; sg = (-1)**k
        for e, c in s.items(): tot[e+sh] = tot.get(e+sh, 0) + sg*c
    return {a: b for a, b in tot.items() if b}

def J41(n):
    total = {0: 1}; cur = {0: 1}
    for m in range(1, n):
        fac = {n: 1, -n: 1}
        fac[m] = fac.get(m, 0) - 1; fac[-m] = fac.get(-m, 0) - 1
        fac = {a: b for a, b in fac.items() if b}
        nx = {}
        for e1, c1 in cur.items():
            for e2, c2 in fac.items(): nx[e1+e2] = nx.get(e1+e2, 0) + c1*c2
        cur = {a: b for a, b in nx.items() if b}
        for a, b in cur.items(): total[a] = total.get(a, 0) + b
    return {a: b for a, b in total.items() if b}

L = 120
qq = [0]*(L+1); qq[0] = 1
for n in range(1, L+1):
    for i in range(L, n-1, -1): qq[i] -= qq[i-n]

j2 = Jtref(2)
ok = j2 == {-1: 1, -3: 1, -4: -1}
print(f"CONTROL  J_2(3_1) = {dict(sorted(j2.items()))}  == q^-1 + q^-3 - q^-4 : {ok}")
assert ok, "Habiro expansion transcribed wrong -- nothing reported"

def bottom(d, N=20):
    lo = min(d); return [d.get(lo+i, 0) for i in range(N)]
def top(d, N=20):
    hi = max(d); return [d.get(hi-i, 0) for i in range(N)]

def stable(f, end, n1, n2, N=20):
    a, b = end(f(n1), N), end(f(n2), N)
    s = 0
    while s < len(a) and a[s] == b[s]: s += 1
    return s, b[:s]

print("\nTHE TREFOIL'S TWO ENDS  (same parity in n, since the overall sign alternates)")
print("-"*74)
for nm, end in (("bottom", bottom), ("top   ", top)):
    for (n1, n2) in ((13, 15), (14, 16)):
        s, v = stable(Jtref, end, n1, n2)
        sg = 1 if (v and v[0] == 1) else -1
        norm = [sg*x for x in v]
        tag = ""
        if norm == qq[:s]: tag = "  == (q;q)_inf"
        if norm == [1] + [0]*(s-1): tag = "  == 1  (TRIVIAL)"
        print(f"   {nm} n={n1},{n2}: window {s:>2}  {v[:12]}{tag}")

print("\nTHE FIGURE-EIGHT'S TWO ENDS  (amphichiral: they agree)")
print("-"*74)
for nm, end in (("bottom", bottom), ("top   ", top)):
    s, v = stable(J41, end, 15, 16)
    print(f"   {nm} n=15,16: window {s:>2}  {v[:12]}"
          f"{'  == (q;q)_inf' if v == qq[:s] else ''}")

print("\nTHE TEST")
print("-"*74)
print("   c_edge(trefoil) = 0, known independently: GM Thm 1.3 makes every Xi_k a monomial.")
print("   c_eff(1/1)          = 0   -> matches the TRIVIAL (top) end.")
print("   c_eff(1/(q;q)_inf)  = 1   -> would NOT match; the bottom end predicts 1, and is wrong.")

print("\nWHICH CHIRALITY IS THIS, AND WHAT IT RULES OUT")
print("-"*74)
j2 = Jtref(2)
print(f"   J_2 = {dict(sorted(j2.items()))} = -q^-4 + q^-3 + q^-1, the Jones polynomial of the")
print( "   RIGHT-handed trefoil.  So the Habiro expansion above is 3^r_1, and GM (page 73)")
print( "   states c = +1/24 for 3^r_1 and c = -1/24 for 3^l_1, where c is defined by: the")
print( "   LOWEST power of q in the coefficient of x^{m/2} has exponent of order c m^2.")
print( "   c > 0 means the blocks run UP; c < 0 (the figure-eight, c = -1/16) means DOWN.")
print()
print( "   RULED OUT -- 'Phi_K = the BOTTOM end, always':")
print( "      3^r_1's bottom end is (q;q)_inf, which would predict c_edge = 1.  It is 0.")
print( "      That reading is exactly what calibrating on 4_1's bottom end would have given.")
print()
print( "   SURVIVES -- 'Phi_K = the end the blocks run toward (the sign of c)':")
print( "      3^r_1: c > 0, blocks run up   -> top end = 1                    -> 0   ok")
print( "      3^l_1: c < 0, blocks run down -> bottom end = mirror of the top = 1 -> 0   ok")
print( "      4_1  : c < 0, blocks run down -> bottom end = (q;q)_inf         -> 1   ok")
print()
print( "   BUT IT IS NOT VERIFIED BY THIS.  The trefoil's c_edge = 0 follows from its blocks")
print( "   having NO WIDTH AT ALL (Thm 1.3: monomials), so it comes out 0 under any end rule")
print( "   selecting the trivial end -- and under none selecting (q;q)_inf.  The trefoil")
print( "   ELIMINATES a candidate; it CANNOT CONFIRM one.  Same distinction BENCH ERROR #19")
print( "   was filed for: a necessary condition is not a proof.")
print()
print( "   Count: 1 knot verified (4_1, blind to the end question), 1 candidate eliminated,")
print( "   1 candidate surviving and unverified.  Verification still needs a CHIRAL knot")
print( "   whose blocks WIDEN.")

print("\nMIRROR CHECK (computed, not asserted): 3^l_1 has the two ends swapped")
print("-"*74)
def mirror(d): return {-e: c for e, c in d.items()}
for nm, end in (("bottom", bottom), ("top   ", top)):
    a = end(mirror(Jtref(13)), 20); b = end(mirror(Jtref(15)), 20)
    s2 = 0
    while s2 < len(a) and a[s2] == b[s2]: s2 += 1
    v = b[:s2]; sg = 1 if (v and v[0] == 1) else -1
    norm = [sg*x for x in v]
    tag = "  == (q;q)_inf" if norm == qq[:s2] else ("  == 1  (TRIVIAL)" if norm == [1]+[0]*(s2-1) else "")
    print(f"   3^l_1 {nm} n=13,15: window {s2:>2}  {v[:12]}{tag}")

print("\n   VERDICT: addendum 4's 'Phi_K = the colored Jones tail' is UNDER-DETERMINED.")
print("   It must name which end.  The figure-eight is amphichiral and cannot distinguish")
print("   them, so the mechanism's single verification could not see this.")
print("   Count after this: 1 knot verified, 1 knot consistent under one reading of two.")
