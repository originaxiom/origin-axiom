"""TIER 1. A smooth bulk gives ind(V) != ind(Vbar) only if dim = 2 mod 4.
Ahat has degree 0,4,8..; ch_k degree 2k; ch_k(Vbar)=(-1)^k ch_k(V)."""
for n in range(2,13,2):
    ks=[k for k in range(n//2+1) if (n-2*k)%4==0]
    print(f"  dim {n:2d}: contributing k={ks}  odd present={any(k%2 for k in ks)}")
