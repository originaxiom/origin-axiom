import sys
from drv import *
mode=sys.argv[1]
if mode=="bscan":
    for nc,a in [(3,F(1,12)),(3,F(1,4)),(3,F(5,12))]:
        for b in [0.0,0.05,0.137,0.2,0.311,0.4,0.5,0.6,0.75,0.9]:
            o=run(nc,a,1/3,12.0,b); print(nc,a,"b=%.3f R2 S=%.4f St=%.4f"%(b,o["S"][0],o["St"][0]),flush=True)
else:
    for im in [10,12,14,16,18,20,24]:
        o=run(3,F(2,23),1/3,float(im),0.137); print("2/23 Nc3 Im",im,"S=%.4f St=%.4f"%(o["S"][0],o["St"][0]),flush=True)
    # unequal slope: 1/7 Nc3
    q=ch(3);a=F(1,7);print("1/7 eq",ex(q["Q"],q["d"],a),ex(q["L"],q["e"],a))
    for im in [8,10,12,14]:
        o=run(3,a,1/3,float(im),0.137); print("1/7 Im",im,"S=%.4g St=%.4g"%(o["S"][0],o["St"][0]),flush=True)
