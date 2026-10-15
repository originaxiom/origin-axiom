import math
def word(w):
    A,B,C,D = 1,0,0,1
    for ch in w:
        if ch=="L": A,B,C,D = A+B,B,C+D,D
        else: A,B,C,D = A,A+B,C,C+D
    return A,B,C,D
def rot_height(w):  # chat1's: min |C| over cyclic rotations
    best=None
    for i in range(len(w)):
        A,B,C,D=word(w[i:]+w[:i])
        if best is None or abs(C)<best[0]: best=(abs(C),A+D)
    c,t=best; return math.sqrt(t*t-4)/(2*c)
def true_height(w, R=400):
    A,B,C,D=word(w); t=A+D
    # conjugate g gamma g^-1 has lower-left entry f(x,y) = C x^2 + (D-A) x y - B y^2 for primitive (x,y) (bottom row of g up to orientation)
    m=None
    for x in range(-R,R+1):
        for y in range(0,R+1):
            if (x,y)==(0,0) or math.gcd(x,y)!=1: continue
            v=abs(C*x*x+(D-A)*x*y-B*y*y)
            if v and (m is None or v<m): m=v
    return math.sqrt(t*t-4)/(2*m), m, t
for w in ("LR","LLLRLRRR","LLLRRRLR","LLLRLLRLR","LLLLLLLRLLLLR","LLLLLLRLLLLLLRLR","LLLLRLLRLLLRLLR","LLLRLRLLLRLRLR","L"*25+"R"*25):
    th,m,t=true_height(w, R=150)
    print(f"{w[:20]:20s} trace {t:6d}  chat1 height {rot_height(w):.3f}   true max height sqrt(t^2-4)/(2 min|f|) = {th:.3f} (min|f|={m})")
A,B,C,D=word("LLLRLRRR"); print("LLLRLRRR gamma",(A,B,C,D),"gamma-I entries gcd",math.gcd(math.gcd(A-1,B),math.gcd(C,D-1)),"det(gamma-I)",(A-1)*(D-1)-B*C)
