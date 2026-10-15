# Item 5 / sec 1.4: near the puncture W(z)=sum R_r^2 |S_r|^2 -> -(1/2)(sum R_r^2 ebar_r) zbar/z + O(|z|^2). Test at non-named tau with mpmath (40 digits).
import mpmath as mp
mp.mp.dps=40
for tau in (mp.mpc(0.21,0.97), mp.mpc(0.4,1.3), mp.mpc(0,1.7), mp.mpc(-0.45,0.93)):
    q=mp.exp(1j*mp.pi*tau); tp=mp.jtheta(1,0,q,1)*mp.pi
    th={r:mp.jtheta(r,0,q) for r in (2,3,4)}
    R={2:-th[2]**2/tp,4:-th[4]**2/tp,3:1j*th[3]**2/tp}
    S=lambda r,z: mp.jtheta(r,mp.pi*z,q)*tp/(th[r]*mp.jtheta(1,mp.pi*z,q))
    # e_r = -(S^2 - wp)|... use e_r = -2*s1, s1 from the Laurent coefficient: S(z) - 1/z ~ s1 z
    z0=mp.mpf('1e-8')
    e={r:-2*(S(r,z0)-1/z0)/z0 for r in (2,3,4)}
    nR2=sum(abs(R[r])**2 for r in R)
    A=sum(R[r]**2*e[r] for r in R); B=sum(R[r]**2*mp.conj(e[r]) for r in R)
    print(f"tau={mp.nstr(tau,4)}: |sum R^2 e|/|R|^2 = {mp.nstr(abs(A)/nR2,3)}, |sum R^2 ebar|/|R|^2 = {mp.nstr(abs(B)/nR2,4)}")
    for rho in (mp.mpf('1e-2'),mp.mpf('1e-3'),mp.mpf('1e-4')):
        out=[]
        for th_ in (0.3,1.1,2.0,4.0):
            z=rho*mp.expj(th_)
            Wz=sum(R[r]**2*abs(S(r,z))**2 for r in R)
            pred=-B/2*mp.conj(z)/z
            out.append(mp.nstr(abs(Wz-pred)/rho**2/nR2,3))
        print(f"   |z|={mp.nstr(rho,2)}: |W - pred|/(|z|^2 |R|^2) at 4 angles = {out};  |pred|/|R|^2 = {mp.nstr(abs(B)/2/nR2,4)}")
