# growth of one term q^p conj(q^p') y^k ds along a semicircle of radius R (the top of a deep geodesic).
# claim: exponential growth iff p < 0 and p' < 0, with rate d ln|I|/dR = 2 pi sqrt(A^2 - D^2) = 4 pi sqrt(p p'),
# A = -(p + p'), D = p - p'; otherwise |I| grows at most polynomially (contour shift).
import mpmath as mp
def I(p, pp, R, k=2.5):
    f = lambda th: mp.exp(2j*mp.pi*(p*(R*mp.cos(th) + 1j*R*mp.sin(th)) - pp*(R*mp.cos(th) - 1j*R*mp.sin(th)))) * (R*mp.sin(th))**k / mp.sin(th)
    pts = mp.linspace(mp.mpf(1)/R, mp.pi - mp.mpf(1)/R, int(12*R))
    return mp.quad(f, pts)
cases = [("-15/8", "1/8"), ("-15/8", "0"), ("-7/8", "-7/8"), ("-1", "-1/2"), ("-17/16", "-3/8")]
for ps, pps in cases:
    p, pp = mp.mpf(eval(ps + ".0")), mp.mpf(eval(pps + ".0"))
    pred = 4*mp.pi*mp.sqrt(p*pp) if (p < 0 and pp < 0) else 0
    Rs = (4, 8, 12)
    mp.mp.dps = 30 + int(2*mp.pi*float(-(p+pp))*Rs[-1]/2.3)
    r = [mp.log(abs(I(p, pp, R))) for R in Rs]
    print(f"p={ps:>6} p'={pps:>5}  ln|I| at R=4,8,12: {[round(float(x),2) for x in r]}  slope(8->12) {float((r[2]-r[1])/4):.4f}  predicted {float(pred):.4f}", flush=True)
