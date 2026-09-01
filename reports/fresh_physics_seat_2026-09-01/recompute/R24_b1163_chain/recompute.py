import snappy
from fractions import Fraction
rows=[]
for name in ['m004','m003','m202','s118']:
    M=snappy.Manifold(name)
    cs=float(M.chern_simons())
    # blind instrument (orientation-blind)
    N=M.copy(); N.reverse_orientation()
    blind=M.is_isometric_to(N)
    aware=M.symmetry_group().is_amphicheiral()
    H=M.homology()
    rows.append((name,round(M.volume(),6),str(H),blind,aware,round(cs,6),str(Fraction(cs).limit_denominator(100)), round((cs%0.5),6)))
print("name vol H1 blind_amph aware_amph CS CS_frac CS_mod_half")
for r in rows: print(*r)
# planted-positive control: a known chiral manifold and a known amphichiral one
for name in ['m015','m004']:
    M=snappy.Manifold(name); print('control',name,M.symmetry_group().is_amphicheiral(), round(M.chern_simons(),6))
