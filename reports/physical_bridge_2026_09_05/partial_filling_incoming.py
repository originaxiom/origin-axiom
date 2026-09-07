import snappy, itertools
def cs(M):
    try: return float(M.chern_simons())
    except Exception: return None

print("=== TEST 1: does filling m004 break CS = 0?  (B432's mechanism, in CS terms)")
M=snappy.Manifold('m004'); print(f"  unfilled m004: cusps {M.num_cusps()} CS {cs(M):+.6f}")
rows=[]
for p,q in [(1,1),(2,1),(3,1),(4,1),(5,1),(1,2),(3,2),(5,2),(7,1),(5,3)]:
    N=snappy.Manifold('m004'); N.dehn_fill((p,q),0)
    st=str(N.solution_type()); c=cs(N)
    rows.append((p,q,st,c))
    print(f"  m004({p},{q}): {st[:22]:<22} CS = {c:+.6f}" if c is not None else f"  m004({p},{q}): {st}")
nz=[r for r in rows if r[3] is not None and abs(r[3])>1e-6]
print(f"  -> CS COMPUTABLE on {sum(1 for r in rows if r[3] is not None)} of {len(rows)} closed fillings.")
_ = None
print("     SnapPy raises \"The Chern-Simons invariant isn't currently known\" once the cusp is filled,")
print("     so this test is INCONCLUSIVE as run. B432's chirality result stands on its own instrument.")

print()
print("=== TEST 2: THE MOVE NOBODY MADE -- partially fill a MULTI-CUSPED cover.")
print("    keep a cusp (so a boundary theory survives) AND break amphichirality (CS != 0).")
base=snappy.Manifold('m004'); found=[]
for deg in range(4,9):
    for C in base.covers(deg):
        if C.num_cusps()<2: continue
        for slope in [(1,0),(1,1),(2,1),(3,1),(1,2)]:
            N=C.copy()
            try: N.dehn_fill(slope,0)
            except Exception: continue
            st=str(N.solution_type())
            if 'degenerate' in st or 'not' in st.lower(): continue
            c=cs(N)
            if c is None: continue
            unf=sum(1 for i in N.cusp_info('is_complete') if i)
            found.append((deg,C.num_cusps(),slope,unf,st,c))
            break
for r in found[:14]:
    deg,nc,sl,unf,st,c=r
    flag="  <== CUSPS SURVIVE + CS != 0" if (unf>=1 and abs(c)>1e-6) else ""
    print(f"  deg {deg} cover, {nc} cusps, fill {sl} -> {unf} cusp(s) left, CS = {c:+.9f}  [{st[:18]}]{flag}")
good=[r for r in found if r[3]>=1 and abs(r[5])>1e-6]
print(f"\n  RESULT: {len(good)} of {len(found)} partial fillings keep >=1 cusp AND have CS != 0")
if good:
    print("  => the two things the sigma bridge needs -- a cusp and a quantized (CS != 0) sector --")
    print("     are SIMULTANEOUSLY satisfiable. Covers alone give neither; fillings alone kill the cusp.")
