sub={'a':'abAAB','b':'aAB','A':'abAB','B':'aA'}
def grow(n,seed='a'):
    w=seed
    for _ in range(n): w=''.join(sub[c] for c in w)
    return w
w=grow(9)
rev=lambda s:s[::-1]
swap={'a':'A','A':'a','b':'B','B':'b'}
sw=lambda s:''.join(swap[c] for c in s)

def factors(s,k):
    return set(s[i:i+k] for i in range(len(s)-k+1))

print("=== is the object's LANGUAGE closed under the three mirrors? (chirality test) ===")
for k in (2,3,4,5,6):
    F=factors(w,k)
    r_closed = all(rev(f) in F for f in F)
    s_closed = all(sw(f)  in F for f in F)
    rs_closed= all(sw(rev(f)) in F for f in F)
    print(f"  length {k}: reversal-closed={r_closed}  swap-closed={s_closed}  swap+reversal(orientation)-closed={rs_closed}")

print("\n=== so which symmetry does the object ALMOST have, and where does it break? ===")
# for each k, count factors whose orientation-mirror (swap+reverse) is NOT present
for k in (4,6,8):
    F=factors(w,k)
    missing=[f for f in F if sw(rev(f)) not in F]
    print(f"  length {k}: {len(missing)}/{len(F)} factors lack their swap+reversal mirror")

print("\n=== does phi intertwine with any mirror? (phi is a morphism; reversal is an anti-morphism) ===")
# check reverse(phi(x)) vs phi-tilde: is there tau with reverse(phi(x)) = tau(x)-related?
for x in 'abAB':
    print(f"  reverse(phi({x})) = {rev(sub[x]):6s}   swap(phi({x})) = {sw(sub[x]):6s}   swap+reverse = {sw(rev(sub[x])):6s}")
