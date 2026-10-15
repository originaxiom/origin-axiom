import json, math
d=json.load(open('<repo>/relays/chat1_2026-10-14_step3/lift_cells.json'))
t=json.load(open('<repo>/relays/chat1_2026-10-14_step3/theta2_completion.json'))['per thread']
P=d['per thread']
cells=["C2/E4","C3/E4","C3/THETA2","C3/ORTH"]
for n in cells:
    adm=[w for w in P if P[w][n].get('admitted')]
    off={L:sum(1 for w in adm if abs(P[w][n]['L=%d: 4 pi L m1/m3'%L]-P[w][n]['kappa'])/P[w][n]['kappa']>0.1) for L in (1000,100,10)}
    passm2={L:sum(1 for w in adm if P[w][n]['kappa']/(4*math.pi*L)>P[w][n]['m2/m3']) for L in (10,100,1000)}
    gt1={L:sum(1 for w in adm if P[w][n]['kappa']/(4*math.pi*L)>1) for L in (10,100,1000)}
    # ratio eps*kappa/(m2/m3) at L=1e7 max, and dev there
    r7=max(((P[w][n]['kappa']/(4*math.pi*1e7))/P[w][n]['m2/m3'],w) for w in adm)
    print(n,len(adm),"off>10%",off,"eps k > m2/m3",passm2,"eps k>1",gt1,"max epsk/(m2/m3) at 1e7 %.3g %s"%r7)
    r=P['LR'][n]; print("  root coef kappa/(4pi m2/m3) = %.4f"%(r['kappa']/(4*math.pi*r['m2/m3'])), " eps k L=10 %.4f vs m2/m3 %.4f"%(r['kappa']/(40*math.pi),r['m2/m3']))
w='LLLLLRR'; print('LLLLLRR C3/E4 dev at 1e7', abs(P[w]['C3/E4']['L=10000000: 4 pi L m1/m3']-P[w]['C3/E4']['kappa'])/P[w]['C3/E4']['kappa'], 'L=10 m2/m3',P[w]['C3/E4']['L=10: m2/m3'],'m1/m3',P[w]['C3/E4']['L=10: m1/m3'])
print('THETA2 H-E4 C2 LLLLLRR N agreement', t['LLLLLRR']['H-E4 C2'].get('N256 vs N384'), 'LLRRRRR', t['LLRRRRR']['H-E4 C2'].get('N256 vs N384'))
