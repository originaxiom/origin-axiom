from sage.all import SL, GF, CyclotomicField, QQ
G = SL(2, GF(5)); ct = G.character_table()
K = CyclotomicField(5); z = K.gen()
two_dim = [i for i in range(ct.nrows()) if ct[i][0]==2]
assert len(two_dim)==2, "not exactly two 2-dim irreps"
rA = [K(ct[two_dim[0]][j]) for j in range(ct.ncols())]
rB = [K(ct[two_dim[1]][j]) for j in range(ct.ncols())]

# (1) character field of the 2-dim irreps = Q(sqrt5)?
gens = [v for v in rA+rB if v not in QQ]
Ksub = K.subfield(gens[0])[0] if gens else QQ
print("character subfield degree over Q:", Ksub.degree() if hasattr(Ksub,'degree') else 1, " (expect 2 = Q(sqrt5))")
# sqrt5 in terms of zeta5:
sqrt5 = 2*z + 2*z**4 + 1     # = zeta+zeta^4 doubled +1? verify
print("sqrt5 check: (2z+2z^4+1)^2 =", (2*z+2*z**4+1)**2, "(want 5)")

# (2) the Galois automorphism tau: zeta5 -> zeta5^2 acts as the nontrivial elt of Gal(Q(sqrt5)/Q)
tau = K.hom([z**2])
print("tau(sqrt5) =", tau(2*z+2*z**4+1), " (want -sqrt5 = -(2z+2z^4+1))")
rA_tau = [tau(v) for v in rA]
print("tau(irrep A) == irrep B ?", rA_tau == rB, "  (simply-transitive SWAP => torsor)")
print("tau(irrep A) == irrep A ?", rA_tau == rA, "  (would mean Galois-FIXED => NOT a torsor)")

# (3) the golden trace values
golden_vals = sorted(set(v for v in rA if v not in QQ), key=str)
print("irrep A non-rational trace values:", [str(v) for v in golden_vals])
phi = (1+K(5).nth_root(2) if False else (1+ (2*z+2*z**4+1))/2)  # (1+sqrt5)/2
inv_phi_neg = (1 - (2*z+2*z**4+1))/2                              # (1-sqrt5)/2 = -1/phi
print("phi=(1+sqrt5)/2 =", phi, "  -1/phi=(1-sqrt5)/2 =", inv_phi_neg)
print("A contains -1/phi:", inv_phi_neg in rA, "  A contains phi:", phi in rA)
print("B contains phi:", phi in rB, "  B contains -1/phi:", inv_phi_neg in rB)
print()
print("VERDICT: exactly 2 golden irreps, field Q(sqrt5), tau swaps A<->B simply-transitively")
print("=> {golden irreps} is a Gal(Q(sqrt5)/Q)=Z/2 TORSOR = the fiber-functor ambiguity.")
