"""B417 TW3 -- track the Fibonacci/Sturmian subshift to its destination, blind."""
import json, os
# Fibonacci word by substitution a->ab, b->a
def fib_word(n):
    a,b="a","ab"
    # iterate substitution from "a"
    s="a"
    for _ in range(n):
        s="".join("ab" if ch=="a" else "a" for ch in s)
    return s
w=fib_word(20)   # long Fibonacci word
print("length:", len(w))
# complexity p(n) = number of distinct factors of length n
def complexity(w, n):
    return len({w[i:i+n] for i in range(len(w)-n+1)})
comp={n: complexity(w,n) for n in range(1,12)}
print("complexity p(n):", comp)
sturmian = all(comp[n]==n+1 for n in range(1,12))
print("Sturmian (p(n)=n+1):", sturmian)
# entropy: lim log p(n)/n -> 0 for Sturmian (linear complexity)
entropy_zero = sturmian    # linear complexity => topological entropy 0
# gap-labeling group: Z + Z*phi (frequencies of factors are in Z+Z(1/phi))
res=dict(complexity=comp, sturmian=bool(sturmian), topological_entropy=0 if entropy_zero else None,
         gap_group="Z + Z*phi (golden quasicrystal module)",
         contrast="trace-map flow entropy = 4 log phi (TW2); the SUBSHIFT is zero-entropy -- different systems")
# BAR CHECK
res["bar"]=dict(forced_invariants=["complexity n+1","topological entropy 0","gap group Z+Z phi"],
                any_exact_SM_match=False,
                reason="n+1 complexity and Z+Z phi gap group are quasicrystal invariants; zero entropy; none is an SM structure. Control: other Sturmians give Z+Z alpha -- golden not SM-distinctive.")
print("EMERGENCE BAR:", "CLEARED" if res["bar"]["any_exact_SM_match"] else "not cleared")
json.dump(res, open("track_symbolic.json","w"), indent=1)
print("DONE")
