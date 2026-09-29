import json
from fractions import Fraction as F
from tet_index import s_str
D=json.load(open("scan.json"))
W=64   # common comparison window in x = q^{1/2}
def ser(d,key,w=W): return {int(k):v for k,v in d[key]["ser"].items() if int(k)<=w and v}
def sig(d,key,w=W): return tuple(sorted(ser(d,key,w).items()))

for name in ["m004","m003"]:
    d=D[name]
    print("="*100); print(f"{name}: index over boundary classes  (minD = exact lower bound on the leading x-degree)")
    print("="*100)
    ks=sorted(d, key=lambda s:(F(s.split(',')[0]),F(s.split(',')[1])))
    for k in ks:
        x,y=k.split(',')
        if abs(F(x))>2 or abs(F(y))>2: continue
        e=d[k]
        print(f"  ({x:>4},{y:>4}) minD={e['minD']:>3} lead={e['lead']}   {s_str(ser(d,k,min(e['minD']+24,40)))}")
    print()

print("="*100); print("MULTISET COMPARISON over the common window q^32")
print("="*100)
S4={k:sig(D['m004'],k) for k in D['m004']}
S3={k:sig(D['m003'],k) for k in D['m003']}
set4=set(S4.values()); set3=set(S3.values())
print(f"  m004: {len(S4)} classes -> {len(set4)} distinct series")
print(f"  m003: {len(S3)} classes -> {len(set3)} distinct series")
only3=set3-set4; only4=set4-set3
print(f"  series occurring for m003 but NOT for m004 (in this range): {len(only3)}")
print(f"  series occurring for m004 but NOT for m003 (in this range): {len(only4)}")
def show(s,lim=6):
    return s_str({k:v for k,v in s}, 40) if s else "0"
if only3:
    print("\n  --- m003-only series (class list) ---")
    for s in sorted(only3, key=lambda t:(t[0][0] if t else 99)):
        cls=[k for k,v in S3.items() if v==s]
        print(f"    classes {cls}: {show(s)}")
if only4:
    print("\n  --- m004-only series (class list) ---")
    for s in sorted(only4, key=lambda t:(t[0][0] if t else 99)):
        cls=[k for k,v in S4.items() if v==s]
        print(f"    classes {cls}: {show(s)}")
