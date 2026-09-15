"""R4b sign check recomputed on main's bench with EXACT branching rules and the standard one-loop formula
   b = (11/3) C2(G) - (2/3) sum_Weyl T(R) - (1/3) sum_complex_scalar T(R)   (b > 0: asymptotically free).
Chat-2's script doubled every fermion ("Dirac") although the 16 is a Weyl (chiral) multiplet, doubled the complex scalar,
and approximated the SO(8)/SU(4) fermion branching. Chain: E6 > SO(10)xU(1) > SO(8)xU(1)^2 > SU(4)xU(1)^3 > SU(3)xU(1)^4.
Matter: 3 x 16 of SO(10) (Weyl). Higgs: one complex 10 of SO(10) (chat-2's stated banked input).
Index normalisation: T(vector of SO(N)) = 1, C2(SO(N)) = N-2; T(fund SU(N)) = 1/2, C2(SU(N)) = N."""
F = 2/3; S = 1/3
stages = {
 # name: (C2, [(Weyl reps' T, count per generation)], [(complex scalar T, count)])
 "SO(10)": (8, [(2, 1)],            [(1, 1)]),        # 16: T=2; 10: T=1
 "SO(8)":  (6, [(1, 2)],            [(1, 1)]),        # 16 -> 8_s + 8_c (T=1 each); 10 -> 8_v + 1 + 1
 "SU(4)":  (4, [(0.5, 4)],          [(1, 1)]),        # 8_s -> 4 + 4bar, 8_c -> 4 + 4bar (T=1/2 each); 8_v -> 6 (T=1) + 1 + 1
 "SU(3)":  (3, [(0.5, 4)],          [(0.5, 2)]),      # 4 -> 3 + 1, 4bar -> 3bar + 1; 6 -> 3 + 3bar
}
gens = 3
for name, (c2, ferm, scal) in stages.items():
    bg = 11/3 * c2; bf = -F * gens * sum(t*n for t, n in ferm); bs = -S * sum(t*n for t, n in scal)
    print(f"{name:7s} gauge={bg:6.2f} fermions={bf:6.2f} scalars={bs:6.2f}  b={bg+bf+bs:6.2f}  AF={'YES' if bg+bf+bs>0 else 'NO'}")
print("control: SM SU(3) with 3 generations and no coloured scalar: b =", 11 - F*3*4*0.5, "(textbook 7)")
