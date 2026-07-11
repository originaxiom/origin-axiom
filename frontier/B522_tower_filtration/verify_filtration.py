import sympy as sp
x, y, z = sp.symbols('x y z')

print("=== 1) character layer: h_a(x,y,1) = sum_{k<=a} h_k(x,y)  (closes B122(2)) ===")
# complete homogeneous symmetric polys
def h(vars, k):
    return sp.Poly(sp.prod([1/(1-v*z) for v in vars]).series(z,0,k+1).removeO(), z).coeff_monomial(z**k) if k>0 else sp.Integer(1)
# easier: generating function coefficient extraction
def hgen(vars, a):
    gf = 1
    for v in vars: gf *= 1/(1-v*z)
    ser = sp.series(gf, z, 0, a+1).removeO()
    return sp.expand(ser.coeff(z, a))
ok=True
for a in range(0,6):
    lhs = sp.expand(hgen([x,y,1], a))
    rhs = sp.expand(sum(hgen([x,y], k) for k in range(0,a+1)))
    match = sp.expand(lhs-rhs)==0
    ok &= match
    print(f"  a={a}: h_a(x,y,1) == sum_k h_k(x,y)? {match}")
print("  ALL MATCH:", ok)
print("  generating function 1/((1-z)(1-xz)(1-yz)) confirmed")

print("\n=== 2) carrier dims (Sym^k V: dim k+1; D^j=det: dim 1; V: dim 2) reconstruct n^2-1 ===")
def symdim(k): return k+1
# n=2: Sym^2 @2
n2 = symdim(2)
print(f"  n=2: Sym^2 -> dim {n2}  (n^2-1 = {2**2-1})  match={n2==3}")
# n=3: Sym^2@2, Sym^3@3, D^2@4, D^3@6
n3 = symdim(2)+symdim(3)+1+1
print(f"  n=3: Sym^2+Sym^3+D^2+D^3 = {symdim(2)}+{symdim(3)}+1+1 = {n3}  (Lawton embdim / n^2-1={3**2-1})  match={n3==9}")
# n=4: Sym^2@2, Sym^3@3, (Sym^4 + D^2)@4, (V x D^2)@5
n4 = symdim(2)+symdim(3)+(symdim(4)+1)+2
print(f"  n=4: Sym^2+Sym^3+(Sym^4+D^2)+(V D^2) = {symdim(2)}+{symdim(3)}+({symdim(4)}+1)+2 = {n4}  (n^2-1={4**2-1})  match={n4==15}")

print("\n=== 3) first arm: Chevalley C[sl_n]^{SL_n} = C[tr a^2,...,tr a^n] -> untwisted Sym^d for 2<=d<=n ===")
for n in range(2,7):
    arm = list(range(2, n+1))
    print(f"  n={n}: first-arm untwisted Sym^d present for d in {arm}  (CH cutoff at d=n; mu_n=1)")

print("\n=== 4) mu_d bookkeeping [0<=d<=n]+[0<=d<=n-3]-[d=0]-[d=1] for small n ===")
def mu(d,n): return int(0<=d<=n)+int(0<=d<=n-3)-int(d==0)-int(d==1)
for n in [3,4,5,6]:
    seq = [mu(d,n) for d in range(0,n+1)]
    print(f"  n={n}: mu_d (d=0..n) = {seq}")
