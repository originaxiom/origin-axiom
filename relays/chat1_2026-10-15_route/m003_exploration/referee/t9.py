import sys; sys.path.insert(0,'.')
from ref4 import *
mp.mp.dps = 25
for k,N in ((5,5),(10,5),(25,5),(50,5),(3,3),(9,3),(18,3)):
    w = "L"*k + "R"*k; g = word(w); print(f"L^{k}R^{k}", g, "N=",N)
    run2(g, N, maxlines=3)
