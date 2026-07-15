import mpmath as mp
mp.mp.dps = 60

def R(v):
    x,y,z = v
    return (x, z, x*z - y)
def Ri(v):
    x,y,z = v
    return (x, x*y-z, y)
def L(v):
    x,y,z = v
    return (z, y, z*y - x)
def Li(v):
    x,y,z = v
    return (x*y-z, y, x)

MAPS = {'R':R,'L':L,'r':Ri,'l':Li}

def apply_word(word, v):
    for ch in word:
        v = MAPS[ch](v)
    return v

def kappa(v):
    x,y,z = v
    return x**2+y**2+z**2-x*y*z

def F(word, vec3):
    # vec3 = (x,y) with z solved from constraint kappa=0 branch, OR treat (x,y,z) all free with constraint as 3rd eq
    x,y,z = vec3
    X,Y,Z = apply_word(word, (x,y,z))
    return [X-x, Y-y, kappa((x,y,z))]

def jac_numeric(word, sol):
    x,y,z = sol
    X,Y,Z = apply_word(word,(x,y,z))
    # numeric jacobian of (X,Y,Z) wrt (x,y,z) via mpmath autodiff (finite diff with high precision, or use mp.diff)
    def f(a,b,c):
        return apply_word(word,(a,b,c))
    h = mp.mpf(10)**(-40)
    J = mp.matrix(3,3)
    base = f(x,y,z)
    for j,var in enumerate([x,y,z]):
        args = [x,y,z]
        args[j] = args[j]+h
        fp = f(*args)
        for i in range(3):
            J[i,j] = (fp[i]-base[i])/h
    return J

def solve_fixed(word, x0, y0, z0, tol=mp.mpf(10)**(-50), maxit=200):
    x,y,z = mp.mpc(x0), mp.mpc(y0), mp.mpc(z0)
    for it in range(maxit):
        Fv = F(word,(x,y,z))
        # numeric Jacobian of F wrt (x,y,z)
        h = mp.mpf(10)**(-30)
        Jm = mp.matrix(3,3)
        for j in range(3):
            args=[x,y,z]
            args[j]=args[j]+h
            Fp = F(word,tuple(args))
            for i in range(3):
                Jm[i,j] = (Fp[i]-Fv[i])/h
        try:
            delta = mp.lu_solve(Jm, mp.matrix(Fv))
        except Exception as e:
            return None
        x = x - delta[0]
        y = y - delta[1]
        z = z - delta[2]
        if max(abs(delta[0]),abs(delta[1]),abs(delta[2])) < tol:
            return (x,y,z)
    return None

if __name__=='__main__':
    import sys
    word = sys.argv[1] if len(sys.argv)>1 else 'RL'
    # try multiple random complex starts
    import random
    random.seed(1)
    found = []
    for trial in range(60):
        x0 = complex(random.uniform(-3,3), random.uniform(-3,3))
        y0 = complex(random.uniform(-3,3), random.uniform(-3,3))
        z0 = complex(random.uniform(-3,3), random.uniform(-3,3))
        sol = solve_fixed(word, x0,y0,z0)
        if sol is None: continue
        x,y,z = sol
        if abs(x)<1e-6 and abs(y)<1e-6 and abs(z)<1e-6:
            continue
        # dedupe
        dup=False
        for s2 in found:
            if abs(s2[0]-x)<1e-20 and abs(s2[1]-y)<1e-20:
                dup=True;break
        if not dup:
            found.append((x,y,z))
    print(f"word={word}: found {len(found)} distinct nontrivial fixed points")
    for s in found:
        J = jac_numeric(word, s)
        ev = mp.eig(J, left=False, right=False)
        print(" fixed pt x,y,z=", s)
        print("   eigenvalues:", ev)
