import mpmath as mp
mp.mp.dps=30
# check the x-integral identity and the 1-D integral for c^0 (S_3,S_4 -> pi/sin(pi z)) and c_2^0 (S_2 -> pi cot(pi z) minus its pi^2 area term)
h=mp.mpf('0.37')
ix=mp.quad(lambda x: mp.pi**2/abs(mp.sin(mp.pi*(x+1j*h)))**2,[-0.5,0,0.5])
print("x-integral:",ix," formula pi^2/(sinh cosh):", mp.pi**2/(mp.sinh(mp.pi*h)*mp.cosh(mp.pi*h)))
f=lambda h: mp.pi**2/(mp.sinh(mp.pi*h)*mp.cosh(mp.pi*h)) - 2/h*mp.atan(1/(2*h))
c0=2*mp.quad(f,[0,0.5,2,10,mp.inf])
print("c^0 (S3,S4) =",c0," -2 pi ln(pi/2) =", -2*mp.pi*mp.log(mp.pi/2))
# S_2 -> pi cot: |pi cot(pi z)|^2 - pi^2 integrated; x-integral of |cot|^2:
g=lambda h: mp.quad(lambda x: mp.pi**2*(abs(mp.cot(mp.pi*(x+1j*h)))**2-1),[-0.5,0,0.5])
f2=lambda h: g(h) - 2/h*mp.atan(1/(2*h))
c20=2*mp.quad(f2,[0,0.5,2,10,mp.inf])
print("c_2^0 =",c20," -2 pi ln(2 pi) =", -2*mp.pi*mp.log(2*mp.pi))
