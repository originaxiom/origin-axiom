#!/usr/bin/env python3
"""xB001 - the two hypotheses this seat KILLED, kept as their own controls.

(a) 'amphichirality is enriched at low complexity' -- killed by its own volume control.
(b) 'amphichiral <=> LR-word is a revswap palindrome' -- TRUE, and already banked:
    B136 (general LR words) / B134 (a corollary of Goodman-Heard-Hodgson 2008).
    Kept here as a reproduction of a banked result, NOT as a finding.
"""
import snappy, itertools, collections

def rs(w): return ''.join('L' if c=='R' else 'R' for c in reversed(w))
def cyc_eq(a,b): return len(a)==len(b) and b in (a+a)

def part_b():
    words=['LR','LLR','LRR','LLRR','LLLR','LRRR','LLRLR','LLRRR','LLLRRR','LLRLRR','LRLRR','LLLRLR','LLRRLR']
    ok=n=0
    print(f"{'word':>9} {'revswap':>9} {'palin':>6} {'amphi':>6}")
    for w in words:
        M=snappy.Manifold('b++'+w); a=bool(M.symmetry_group().is_amphicheiral())
        p=cyc_eq(w,rs(w)); n+=1; ok+= (p==a)
        print(f"{w:>9} {rs(w):>9} {str(p):>6} {str(a):>6}")
    print(f"criterion holds {ok}/{n}  (B136 / GHH 2008 -- reproduced, not new)")
    assert ok==n

def part_a():
    cen=snappy.OrientableCuspedCensus(cusps=1)
    buck=collections.defaultdict(lambda:[0,0])
    for M in itertools.islice(cen,5000):
        k=int(float(M.volume())); buck[k][1]+=1
        if M.symmetry_group().is_amphicheiral(): buck[k][0]+=1
    print(f"\n{'volume':>9} {'amphi':>6} {'total':>6} {'rate':>8}")
    rates=[]
    for k in sorted(buck):
        a,t=buck[k]
        if t>=20:
            print(f"{f'{k}-{k+1}':>9} {a:>6} {t:>6} {100*a/t:>7.2f}%"); rates.append(100*a/t)
    print("the control: the rate RISES with volume in the bulk, so 'simpler => more")
    print("amphichiral' is NOT a law. The seat's hypothesis (a) is KILLED by this cell.")
    assert rates[-1] > rates[0], "control must show the rising trend that kills the hypothesis"

if __name__=="__main__":
    part_b(); part_a(); print("\nVERIFIED (one banked reproduction, one self-kill)")
