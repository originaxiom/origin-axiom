# R28 blind implementation: Kashaev invariant of 4_1, large-N ladder, Richardson in 1/N.
import mpmath as mp, sys, json, time
mp.mp.dps = 700
pi=mp.pi
def J(N):
    # J_N(4_1) = sum_{k=0}^{N-1} prod_{j=1}^k (2 sin(pi j/N))^2 ; running product O(N)
    s=mp.mpf(1); p=mp.mpf(1)
    for j in range(1,N):
        p *= (2*mp.sin(pi*j/N))**2
        s += p
    return s
V = 3*mp.im(mp.polylog(2, mp.exp(2j*pi/3)))   # Vol(4_1)
def S(N): return J(N)*mp.exp(-N*V/(2*pi))/mp.mpf(N)**mp.mpf(1.5)
def fit(Ns, Svals, M):
    # solve sum_k c_k x^k = S, x=1/N, first M nodes
    A=mp.matrix([[mp.mpf(1)/mp.mpf(N)**k for k in range(M)] for N in Ns[:M]])
    b=mp.matrix(Svals[:M])
    return mp.lu_solve(A,b)
if __name__=="__main__":
    Ns=[int(a) for a in sys.argv[1:]]
    t=time.time()
    out={}
    for N in Ns:
        out[N]=mp.nstr(S(N),120); print(N, out[N][:40], time.time()-t, flush=True)
    json.dump(out, open("S_values.json","w"), indent=1)
