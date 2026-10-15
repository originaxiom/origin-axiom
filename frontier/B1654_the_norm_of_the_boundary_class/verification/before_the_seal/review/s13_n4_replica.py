import sys, math; sys.path.insert(0,'.')
import numpy as np, pre
ns = pre.load(); cA=ns['cA']; R_A=ns['R_A']; D_of=ns['D_of']; nR2=ns['nR2']; TAUS=ns['TAUS']; thetas=ns['thetas']; th1p=ns['th1p']
# replica of the N4 block (as coded) on the six named points
for name,tau in TAUS.items():
    c = {r: cA(r,tau,1e-5) for r in (2,3,4)}
    R=R_A(tau); D=D_of(c,R)
    uu=[sum((2*np.pi*L+c[r])*R[r]**2 for r in (2,3,4)) for L in (5.0,20.0,80.0)]
    lam={2:1.0,3:2.0,4:4.0}
    uu_c=[sum((2*np.pi*(L-math.log(lam[r]))+c[r])*R[r]**2 for r in (2,3,4)) for L in (5.0,20.0)]
    t0=thetas(np.array(0.0),tau); d=th1p(tau)
    Rp={2:t0[1]**2/d,4:1j*t0[3]**2/d,3:t0[2]**2/d}
    upup=[sum((2*np.pi*L+c[r])*Rp[r]**2 for r in (2,3,4)) for L in (5.0,20.0)]
    v={"uu_L_spread_rel":max(abs(x-uu[0]) for x in uu)/(nR2(R)*80*2*np.pi),
       "uu_minus_D_rel":abs(uu[0]-D)/(nR2(R)*5*2*np.pi),
       "cutoff_control_shift":abs(uu_c[0]-D),
       "cutoff_control_pred":abs(-2*np.pi*sum(math.log(lam[r])*R[r]**2 for r in (2,3,4))),
       "Rprime_slope_over_2piRpRp":abs((upup[1]-upup[0])/15.0)/abs(2*np.pi*sum(Rp[r]**2 for r in (2,3,4)))}
    ok = (v["uu_L_spread_rel"]<1e-12 and v["uu_minus_D_rel"]<1e-12 and v["cutoff_control_shift"]>1e-3*nR2(R)
          and abs(v["cutoff_control_shift"]/v["cutoff_control_pred"]-1)<1e-9 and abs(v["Rprime_slope_over_2piRpRp"]-1)<1e-9)
    print(f"{name:6s} spread={v['uu_L_spread_rel']:.1e} uu-D={v['uu_minus_D_rel']:.1e} shift/|R|^2={v['cutoff_control_shift']/nR2(R):.3e} shift/pred-1={abs(v['cutoff_control_shift']/v['cutoff_control_pred']-1):.1e} slope-1={abs(v['Rprime_slope_over_2piRpRp']-1):.1e}  -> cell-clause passes: {ok}")
