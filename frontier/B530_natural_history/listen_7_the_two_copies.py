import sympy as sp
letters='abAB'; sub={'a':'abAAB','b':'aAB','A':'abAB','B':'aA'}
M=sp.Matrix([[sub[j].count(i) for j in letters] for i in letters])   # growth, basis (a,b,A,B)
D=sp.Matrix([[0,0,-1,0],[0,0,0,-1],[1,0,0,0],[0,1,0,0]])            # the symplectic form (thread 1)

print("=== does the object's growth M preserve its own symplectic form D? ===")
MtDM=sp.simplify(M.T*D*M)
print("M^T D M ="); sp.pprint(MtDM)
print("\n  M^T D M == D  (symplectic)?      ", MtDM==D)
print("  M^T D M == -D (anti-symplectic)? ", MtDM==-D)
# is it a scalar multiple? (conformally symplectic)
ratio=None
for i in range(4):
    for j in range(4):
        if D[i,j]!=0: ratio=sp.simplify(MtDM[i,j]/D[i,j]); break
    if ratio is not None: break
print("  M^T D M == c*D for scalar c? c =", ratio, "  holds:", sp.simplify(MtDM-ratio*D)==sp.zeros(4))
print("  det(M) =", M.det())

print("\n=== the two natural 2+2 splits of the four letters ===")
print("  COPY split (the bootstrap's two Fibonacci copies): {a,b} | {A,B}")
print("  ROLE split (deciders | couriers)                 : {a,A} | {b,B}  <- this is what D pairs")
print("  => D pairs across BOTH: a<->A and b<->B are cross-copy, same-role. The symplectic axis is the")
print("     'same role, other copy' pairing -- not the copy split, not the role split, but their diagonal.")

# does M respect the copy-swap c: a<->A, b<->B is role... let me test the COPY involution t: a<->b? no.
# the two copies are (a,b) and (A,B); the copy-swap is a<->A, b<->B = the SAME s as role-cross. Interesting:
print("\n=== is the swap s (a<->A,b<->B) simultaneously the copy-exchange AND the role-cross? ===")
print("  copy1={a,b}, copy2={A,B}; s sends copy1->copy2 (a->A,b->B): YES s is the copy-exchange.")
print("  so the ONE involution s is both 'swap the two golden copies' and 'the symplectic pairing'.")
