"""B419 TW5 -- Kashaev <4_1>_N large-N asymptotics, blind."""
import json, os, math, mpmath as mp
mp.mp.dps=30
def kashaev_numeric(N):
    q=mp.e**(2j*mp.pi/N); tot=mp.mpf(1); prod=mp.mpf(1)
    for j in range(1,N):
        prod*=abs(1-q**j)**2; tot+=prod
    return tot
VOL=2.029883212819307
rows={}
for N in (20,40,60,80,100,140,180):
    v=kashaev_numeric(N); g=2*math.pi*math.log(float(v))/N
    rows[str(N)]=dict(growth=g)
    print(f"N={N}: 2pi log<4_1>/N = {g:.5f}  (Vol={VOL:.5f})")
# the growth -> Vol (volume conjecture); the destination is the hyperbolic volume + sqrt5 arithmetic (B384)
res=dict(growth=rows, limit_target=VOL,
         sqrt5_content="banked B384: <4_1>_5 = 46+2sqrt5; sqrt5 nonzero at every 5|N",
         destination="the volume-conjecture asymptotic (growth -> Vol(4_1)=2.0299) with Q(sqrt5) arithmetic content",
         bar=dict(any_exact_SM_match=False,
                  reason="the destination is a hyperbolic volume (a transcendental geometric constant) + Q(sqrt5) arithmetic; no SM structure; control: other knots give other volumes"))
print("EMERGENCE BAR: not cleared")
json.dump(res, open("track_quantum.json","w"), indent=1)
print("DONE")
