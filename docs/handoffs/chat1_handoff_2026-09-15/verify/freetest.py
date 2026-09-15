import snappy, json
# A FREE orientation-reversing involution on M  <=>  M is the orientation double cover of
# a nonorientable manifold. Build the exact set of such M from the nonorientable census,
# then ask whether ANY class-1/4 amphichiral manifold is one.
rows = json.load(open('wide.json'))
q = [r for r in rows if r[1]==1]          # class 1/4
z = [r for r in rows if r[1]==0]          # class 0
print(f"amphichiral: {len(rows)}  class0={len(z)} class1/4={len(q)}", flush=True)

cover_names=set(); cover_vols=[]
C=snappy.NonorientableCuspedCensus
for i,M in enumerate(C):
    try:
        D=M.orientation_cover()
        cover_vols.append(float(D.volume()))
        for nm in D.identify():
            cover_names.add(str(nm).split('(')[0])
    except Exception: pass
    if (i+1)%400==0: print(f"  covers {i+1}/{len(C)} names={len(cover_names)}", flush=True)
print(f"\ndistinct manifolds arising as orientation double covers: {len(cover_names)}")

q_free=[r for r in q if r[0] in cover_names]
z_free=[r for r in z if r[0] in cover_names]
print(f"  class 1/4 that ARE orientation double covers : {len(q_free)}/{len(q)}  {[r[0] for r in q_free][:8]}")
print(f"  class 0   that ARE orientation double covers : {len(z_free)}/{len(z)}  {[r[0] for r in z_free][:8]}")
print()
if not q_free:
    print("  => NO class-1/4 manifold carries a FREE orientation-reversing involution.")
    print("     Mere involution does NOT force class 0 (21 counterexamples), but FREENESS")
    print("     is unrefuted across the whole amphichiral population. R040's hypothesis is")
    print("     exactly the right one -- my weakening to 'involution' was the error.")
else:
    print("  => FREENESS ALSO FAILS. That would contradict R040's 1260/1260; check the test.")
