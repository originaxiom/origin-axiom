import mpmath as mp
mp.mp.dps = 55

# Elliptic curve isogeny class 15a, curve 15a1: y^2 + xy + y = x^3 + x^2 - 10x - 10
# conductor N=15 = 3*5, both multiplicative reduction.
a1,a2,a3,a4,a6 = 1,1,1,-10,-10

def count_ap(p):
    # count affine points of y^2 + a1 xy + a3 y = x^3 + a2 x^2 + a4 x + a6 over F_p
    N = 1  # point at infinity
    for x in range(p):
        rhs = (x*x*x + a2*x*x + a4*x + a6) % p
        b = (a1*x + a3) % p        # coeff: y^2 + b y - rhs = 0
        # count y in F_p with y^2 + b y - rhs = 0
        # discriminant D = b^2 + 4 rhs (mod p); number of sols = 1+legendre(D)
        D = (b*b + 4*rhs) % p
        if p == 2:
            # brute
            c=0
            for y in range(2):
                if (y*y + b*y - rhs) % 2 == 0: c+=1
            N += c
        else:
            ls = pow(D, (p-1)//2, p)
            if D % p == 0: N += 1
            elif ls == 1: N += 2
            else: N += 0
    return p + 1 - N

def is_prime(n):
    if n<2: return False
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return True

Nmax = 400
primes = [p for p in range(2, Nmax+1) if is_prime(p)]
ap = {}
for p in primes:
    if p == 3:
        ap[p] = -1   # split multiplicative (LMFDB 15.2.a.a)
    elif p == 5:
        ap[p] = 1
    else:
        ap[p] = count_ap(p)

# sanity vs known newform 15.2.a.a: a2=-1,a3=-1,a5=1,a7=0,a11=-4,a13=-2
print("a2,a3,a5,a7,a11,a13 =", ap[2],ap[3],ap[5],ap[7],ap[11],ap[13])

# build a_n multiplicatively
a = [0]*(Nmax+1)
a[1]=1
def fill_prime_powers(p):
    # returns dict k->a_{p^k} for p^k<=Nmax
    res={0:1}
    if p in (3,5):
        pk=p; k=1
        while pk<=Nmax:
            res[k]=ap[p]**k; pk*=p; k+=1
    else:
        res[1]=ap[p]
        pk=p*p; k=2
        while pk<=Nmax:
            res[k]=ap[p]*res[k-1]-p*res[k-2]
            pk*=p; k+=1
    return res
pp={p:fill_prime_powers(p) for p in primes}

def a_of(n):
    if n==1: return 1
    val=1; m=n
    for p in primes:
        if p*p>m and m>1:
            # m is prime
            val*= pp.get(m,{1:count_ap(m) if m not in (3,5) else ap.get(m)}).get(1, count_ap(m))
            m=1; break
        if m%p==0:
            k=0
            while m%p==0: m//=p; k+=1
            val*=pp[p][k]
    if m>1:
        # leftover prime > sqrt, compute ap
        if is_prime(m):
            val*= (count_ap(m) if m not in (3,5) else ap[m])
    return val

for n in range(1,Nmax+1):
    a[n]=a_of(n)
print("a_1..a_14:", a[1:15])

# smoothed functional equation, weight 2, N=15, sign eps=+1 (rank 0)
Ncond = mp.mpf(15); eps = 1
A = 2*mp.pi/mp.sqrt(Ncond)

def Gamma_inc(s,x):
    return mp.gammainc(s, x)   # = int_x^inf t^{s-1} e^{-t} dt = Gamma(s,x)

# Lambda(0) = sum a_n [ Gamma(0,An) + eps (An)^{-2} Gamma(2,An) ]
Lam0 = mp.mpf(0)
for n in range(1, Nmax+1):
    if a[n]==0: continue
    x = A*n
    term = a[n]*( mp.gammainc(0,x) + eps*(x**-2)*mp.gammainc(2,x) )
    Lam0 += term
Lprime0 = Lam0
print("L'(E15,0) = Lambda(0) =", mp.nstr(Lprime0, 45))

# L(E15,2) = A^2 * Lambda(2); Lambda(2)=Lambda(0) when eps=1
L2 = A**2 * Lam0
print("L(E15,2) =", mp.nstr(L2, 45))

# also compute L(E15,1) to check rank 0 (should be nonzero)
# Lambda(1) = sum a_n [ (An)^{-1}Gamma(1,An) + eps (An)^{-1}Gamma(1,An) ] = (1+eps) sum a_n (An)^{-1} e^{-An}
Lam1 = mp.mpf(0)
for n in range(1,Nmax+1):
    if a[n]==0: continue
    x=A*n
    Lam1 += a[n]*( (x**-1)*mp.gammainc(1,x) + eps*(x**-1)*mp.gammainc(1,x) )
LE1 = A*Lam1   # L(E,1)=A^1 Lambda(1)/Gamma(1)=A*Lam1
print("L(E15,1) =", mp.nstr(LE1, 30), "(nonzero => rank 0, eps=+1 correct)")
