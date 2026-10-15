import snappy, warnings, math
warnings.filterwarnings("ignore")
for s in ("b++LR","b+-LR"):
    M=snappy.Manifold(s); print(s, M.identify(), M.homology(), float(M.volume()))
def V(s): return float(snappy.Manifold(s).volume())
print("LR^n tower (+):", [(n, round(V("b++L"+"R"*n),5)) for n in (1,2,5,25,50,75,100)])
print("LR^n tower (-):", [(n, round(V("b+-L"+"R"*n),5)) for n in (3,21,46,71)])
print("L^aR^b, a,b>=2 (min candidates):", [(a,b,round(V("b++"+"L"*a+"R"*b),4), round(V("b+-"+"L"*a+"R"*b),4)) for a,b in ((2,2),(2,3),(3,3),(2,10),(2,23),(2,25))])
print("2-pair words (GF bound 4v3*... =4.0598):", [(w,round(V("b++"+w),4),round(V("b+-"+w),4)) for w in ("LRLRR","LRLRRR","LLRLR","LRRLRR")])
print("c=6 weights e^{-Vol/pi}: LR^25", round(math.exp(-V('b++L'+'R'*25)/math.pi),4), " LLLRLRRR", round(math.exp(-V('b++LLLRLRRR')/math.pi),4), " LR^50", round(math.exp(-V('b++L'+'R'*50)/math.pi),4))
# closing check for LR^{kN^2}
def mat(w):
    A,B,C,D=1,0,0,1
    for ch in w:
        if ch=="L": A,B,C,D=A+B,B,C+D,D
        else: A,B,C,D=A,A+B,C,C+D
    return A,B,C,D
for n in (25,50,75):
    A,B,C,D=mat("L"+"R"*n); print("LR^%d"%n, "Q(0,1)=",-B, "25|Q:", (-B)%25==0)
