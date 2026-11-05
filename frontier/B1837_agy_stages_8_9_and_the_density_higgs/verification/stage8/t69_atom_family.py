"""S302 check of the lane's 'P-667 atom' (Theorems 65 part 3, 69 part 1, 70 part 1), main's side:
(a) Li_2(e^{i pi/3}) = pi^2/36 + i Cl_2(pi/3) and the lane's R = Li_2 - pi^2/9 = -pi^2/12 + i Cl_2(pi/3) (L248 sec. 4,
    verified in B1476 C2);
(b) the family volumes from SnapPy (not typed): m004, m003, the cyclic 3-cover of m004, against 2, 2, 6 x Cl_2(pi/3);
(c) amphichirality from SnapPy's symmetry groups (the lane types 'm004 True, m003 False' as literals), and H_1;
(d) the 3D-index asymptotics across the family that P-667 asks for: NOT computed by the lane (structure noted here)."""
import mpmath as mp
import snappy

mp.mp.dps = 40
z = mp.exp(1j * mp.pi / 3)
li2 = mp.polylog(2, z)
cl2 = mp.clsin(2, mp.pi / 3)
print("|Li2(e^{i pi/3}) - (pi^2/36 + i Cl2(pi/3))| = %s" % mp.nstr(abs(li2 - (mp.pi ** 2 / 36 + 1j * cl2)), 3))
R = li2 - mp.pi ** 2 / 9
print("|R - (-pi^2/12 + i Cl2(pi/3))| = %s ; Re R = -zeta(2)/2: %s" % (mp.nstr(abs(R - (-mp.pi ** 2 / 12 + 1j * cl2)), 3),
      abs(mp.re(R) + mp.zeta(2) / 2) < mp.mpf("1e-35")))
psi_form = (mp.sqrt(3) / 72) * (mp.psi(1, mp.mpf(1) / 6) + mp.psi(1, mp.mpf(1) / 3) - mp.psi(1, mp.mpf(2) / 3) - mp.psi(1, mp.mpf(5) / 6))
print("a trigamma form of Cl2(pi/3), (sqrt3/72)(psi1(1/6)+psi1(1/3)-psi1(2/3)-psi1(5/6)), dev %s" % mp.nstr(abs(psi_form - cl2), 3))
for name in ("m004", "m003"):
    M = snappy.ManifoldHP(name)
    S = M.symmetry_group()
    print("%s: vol/Cl2(pi/3) = %s ; tetrahedra %d ; H1 %s ; amphicheiral %s ; symmetry group order %d" % (
        name, mp.nstr(mp.mpf(str(M.volume()).replace(" ", "")) / cl2, 20), M.num_tetrahedra(), M.homology(),
        S.is_amphicheiral(), S.order()))
C3 = snappy.Manifold("m004").covers(3, cover_type="cyclic")[0]
S3 = C3.symmetry_group()
print("cyclic 3-cover of m004: vol/Cl2(pi/3) = %s ; tetrahedra %d ; amphicheiral %s" % (
    mp.nstr(mp.mpf(float(C3.volume())) / cl2, 12), C3.num_tetrahedra(), S3.is_amphicheiral()))
