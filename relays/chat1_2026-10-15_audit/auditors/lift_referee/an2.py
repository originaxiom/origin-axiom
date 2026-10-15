import json, math
import numpy as np
d=json.load(open('<repo>/relays/chat1_2026-10-14_step3/lift_cells.json'))
P=d['per thread']
n="C3/E4"
adm=[w for w in P if P[w][n].get('admitted')]
rows=sorted(adm,key=lambda w:P[w][n]['kappa'])
print("C3/E4 admitted sorted by kappa: word y_max kappa floor m2/m3 rank2 | L=1000 m1/m3 m2/m3 | L=1e7 m1/m3")
for w in rows:
    r=P[w][n]
    print("%-9s %.3f %.4g %.3g %.4g %s | %.4g %.4g | %.4g"%(w,P[w]['y_max'],r['kappa'],r['m1/m3'],r['m2/m3'],r['rank 2'],r['L=1000: m1/m3'],r['L=1000: m2/m3'],r['L=10000000: m1/m3']))
