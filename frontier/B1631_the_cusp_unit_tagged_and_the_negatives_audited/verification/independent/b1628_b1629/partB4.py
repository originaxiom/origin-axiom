from mpmath import mp, mpf, sqrt
from partB import height_CF
mp.dps=40
print(" k   height(CF)    (k+2)/2   h-(k/2)   closed form")
for k in range(1,21):
    h=height_CF('L'*k+'R')
    # closed form: x=[k;1,k,1..] solves x = k + x/(x+1) -> x^2 +x = kx + k + x ... derive numerically below
    # [k;1,k,1,...]: x=k+1/(1+1/x)=k+x/(x+1)  => x(x+1)=k(x+1)+x => x^2 -k x -k =0 => x=(k+sqrt(k^2+4k))/2
    x=(k+sqrt(k*k+4*k))/2
    # backward tail [0;1,k,1,k...] = 1/(1+1/x)... sequence after reversal: a_{i-1}=1,a_{i-2}=k -> [0;1,k,1,k,...]=1/(1+1/x) = x/(x+1)
    cf1=(x+x/(x+1))/2
    # other cut: [1;k,1,k,...]=y: y=1+1/(k+1/y) ; backward [0;k,1,k,...]=1/x'... 
    print(f"{k:2d}  {mp.nstr(h,12):>14s}  {(k+2)/2:7.3f}  {mp.nstr(h-mpf(k)/2,8):>10s}  {mp.nstr(cf1,12)}")
import math
print("closed form h(k)=(x + x/(x+1))/2 with x=(k+sqrt(k^2+4k))/2 ; at k=12:", mp.nstr(((12+sqrt(12*12+48))/2 + ((12+sqrt(12*12+48))/2)/(((12+sqrt(12*12+48))/2)+1))/2,10))
