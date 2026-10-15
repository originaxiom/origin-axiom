import json, math
d=json.load(open('<repo>/relays/chat1_2026-10-14_step3/lift_cells.json'))
P=d['per thread']
for n,ws in (("C3/E4",["LLLLLRR","LLRRRRR","LRRRR","LLLLRLLR","LLLLRR","LR"]),("C3/THETA2",["LLLLLRR","LLRRRRR","LLLLLRRR","LR"]),("C3/ORTH",["LLLLLRR","LRRRR"]),("C2/E4",["LLRRRRR","LLLLLRR","LR"])):
  for w in ws:
    r=P[w][n]
    s="%s %s adm=%s y=%.3f kappa=%.4g m2/m3=%.4g floor=%.3g"%(n,w,r.get('admitted'),P[w]['y_max'],r.get('kappa',float('nan')),r['m2/m3'],r['m1/m3'])
    for L in (10,100,1000,10000000):
      s+=" | L=%g m1/m3=%.3g m2/m3=%.3g 4piLm1/m3/k=%.4g"%(L,r['L=%d: m1/m3'%L],r['L=%d: m2/m3'%L],r['L=%d: 4 pi L m1/m3'%L]/r['kappa'])
    print(s)
# L=1000 worst over admitted per cell, and count of threads with dev>1%,>10%
for n in ("C2/E4","C3/E4","C3/THETA2","C3/ORTH"):
  adm=[w for w in P if P[w][n].get('admitted')]
  devs=sorted(((abs(P[w][n]['L=1000: 4 pi L m1/m3']-P[w][n]['kappa'])/P[w][n]['kappa'],w) for w in adm),reverse=True)
  print(n,"L=1000 dev >1%:",sum(1 for x in devs if x[0]>0.01),">10%:",sum(1 for x in devs if x[0]>0.1),"top:",[(round(a,3),w) for a,w in devs[:4]])
  devs7=sorted(((abs(P[w][n]['L=10000000: 4 pi L m1/m3']-P[w][n]['kappa'])/P[w][n]['kappa'],w) for w in adm),reverse=True)
  print("  L=1e7 top:",[( '%.3g'%a,w) for a,w in devs7[:3]])
  print("  m2/m3 range adm: %.3g - %.3g"%(min(P[w][n]['m2/m3'] for w in adm),max(P[w][n]['m2/m3'] for w in adm)))
