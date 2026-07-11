def INV(c): return c.lower() if c.isupper() else c.upper()
def reduce(w):
    st=[]
    for ch in w:
        if st and st[-1]==INV(ch): st.pop()
        else: st.append(ch)
    return ''.join(st)
def apply(sub, w):
    out=[]
    for ch in w:
        img = sub[ch.lower()]
        out.append(img if ch.islower() else ''.join(INV(x) for x in reversed(img)))
    return reduce(''.join(out))

phi = {'a':'abccd','b':'acd','c':'abcd','d':'ac'}
psi = {'a':'bAcBd','b':'DbCaBcAcBd','c':'DbCaBd','d':'Db'}       # candidate inverse (to verify)

print('=== step 1: verify psi = phi^-1 (free reduction) ===')
ok=all(apply(phi,apply(psi,g))==g and apply(psi,apply(phi,g))==g for g in 'abcd')
for g in 'abcd':
    print(f'  phi(psi({g}))={apply(phi,apply(psi,g))!r}  psi(phi({g}))={apply(psi,apply(phi,g))!r}')
print('  psi IS phi^-1:', ok)

print('\n=== step 2: dilatations via |f^k(a)|^(1/k), capped K (ratio converges by k~10) ===')
def growth(sub, seed='a', K=13):
    w=seed; lens=[len(w)]
    for k in range(1,K):
        w=apply(sub,w); lens.append(len(w))
    ratios=[lens[i+1]/lens[i] for i in range(len(lens)-1)]
    return sum(ratios[-4:])/4, ratios
lp,rp = growth(phi); li,ri = growth(psi)
print(f'  |phi^k(a)|   ratios tail: {[round(x,3) for x in rp[-5:]]}  -> lambda(phi)    ~ {lp:.4f}  (beta=3.6762)')
print(f'  |phi^-k(a)|  ratios tail: {[round(x,3) for x in ri[-5:]]}  -> lambda(phi^-1) ~ {li:.4f}  (train_track: 3.0523)')
print(f'  lambda(phi) != lambda(phi^-1)?  {abs(lp-li)>0.05}  => NOT geometric (Handel-Mosher) => not a 3-mfd group (Stallings)')
print(f'  lambda(phi^-1) ({li:.3f}) != abelianization |M^-1|-Perron (2.272)?  {abs(li-2.272)>0.1}  (free cancellation matters, as chat1 noted)')
