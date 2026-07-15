import sympy as sp
I=sp.I; pi=sp.pi

phi=(1+sp.sqrt(5))/2
h3_abs2 = sp.Rational(1,2) - sp.sqrt(5)/10

amps = {
 "h3": h3_abs2,
 "E62_1(j'=1,k=3)": sp.Rational(4,7)*sp.sin(2*pi/7)**2,
 "E62_2(j'=3,k=-2)": sp.Rational(4,7)*sp.sin(pi/7)**2,
 "E62_3(j'=2,k=-1)": sp.Rational(4,7)*sp.cos(pi/14)**2,
}

lines = {
 "V4_shallow(wt+2)": {"su3": sp.Rational(1,2), "su2": sp.Rational(2,29), "mult(1,0,0)": sp.Rational(25,58)},
 "V4_top(wt+8)": {"su3": sp.Integer(0), "su2": sp.Integer(0), "mult_total(4x1/4)": sp.Integer(1)},
 "V8_shallow(wt+2)": {"su3": sp.Rational(1,2), "su2": sp.Rational(8,25), "mult(1,0,0)": sp.Rational(9,50)},
 "V8_top(wt+16,tip)": {"su3": sp.Integer(0), "su2": sp.Integer(0), "mult_total(1,1,2)=1": sp.Integer(1)},
}

print("=== |A|^2 exact and 30-digit ===")
for name,a2 in amps.items():
    print(f"{name}: |A|^2 = {sp.nsimplify(a2)}   = {sp.N(a2,30)}")

print()
print("=== f * |A|^2  (class-projected) ===")
for lname, fracs in lines.items():
    for cname, f in fracs.items():
        for aname, a2 in amps.items():
            val = f*a2
            if val == 0:
                print(f"{lname} | {cname} | {aname}: f={f}  -> f*|A|^2 = 0 (exact)")
            else:
                print(f"{lname} | {cname} | {aname}: f={f}  -> f*|A|^2 exact = {sp.nsimplify(sp.simplify(val))}  decimal30 = {sp.N(val,30)}")
    print()

print("=== cross-layer products: {N(h3)=1/5, normprod=1/49} x su3/su2 fraction pairs (shallow lines) ===")
anchors = {"N(h3)": sp.Rational(1,5), "normprod(E62 product)": sp.Rational(1,49)}
pairs = {
 "V4_shallow su3=1/2": sp.Rational(1,2),
 "V4_shallow su2=2/29": sp.Rational(2,29),
 "V8_shallow su3=1/2": sp.Rational(1,2),
 "V8_shallow su2=8/25": sp.Rational(8,25),
}
for aname, aval in anchors.items():
    for pname, pval in pairs.items():
        prod = aval*pval
        print(f"{aname} x {pname} = {aval} x {pval} = {sp.nsimplify(prod)}")

print()
print("=== ratios f_su3/f_su2 per line (exact, restated) ===")
print("V4:", sp.nsimplify(sp.Rational(1,2)/sp.Rational(2,29)))
print("V8:", sp.nsimplify(sp.Rational(1,2)/sp.Rational(8,25)))
