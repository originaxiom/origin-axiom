import os
os.environ["OMP_NUM_THREADS"]="1"
import sys, random, math, importlib.util
spec=importlib.util.spec_from_file_location("m",str(__import__("pathlib").Path(__file__).resolve().parents[2] / "the_pull_backs_strength.py"))
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
# invariance of f_raw under T and S at moderate points
for t in [0.2+1.2j,-0.3+0.9j,0.4+1.6j,0.1+1.05j]:
    print("inv", m.f_raw(t), m.f_raw(t+1), m.f_raw(-1/t), m.f_raw(-t.conjugate()))
# digit reliability: walk to 1e60 then continue to 1e150, compare digits
def step(M,x,p):
    a,b,c,d=M
    if x<(1-p)/2: return (a,a+b,c,c+d)
    if x<1-p: return (a+b,b,c+d,d)
    if x<1-p/2: return (a,b-a,c,d-c)
    return (a-b,b,c-d,d)
for p in (0.0,0.3,0.5):
    bad=0;short=0;N=300;lens=[];lost=[]
    for w in range(N):
        rng=random.Random(777+w+int(p*1000)*10000); M=(1,0,0,1); snap=None
        while True:
            M=step(M,rng.random(),p)
            if snap is None and max(map(abs,M))>=10**60: snap=M
            if max(map(abs,M))>=10**150: break
        a,c=snap[0],snap[2]
        if c==0: short+=1; continue
        d1=m.digits_of(a,c); d2=m.digits_of(M[0],M[2])
        k=0
        while k<min(len(d1),len(d2)) and d1[k]==d2[k]: k+=1
        lens.append(len(d1)); lost.append(len(d1)-k)
        if len(d1)-14>k: bad+=1
        if len(d1)-14<40: short+=1
    print(p,"bad(<14 dropped insufficient)",bad,"short",short,"mean digits",sum(lens)/len(lens),"max lost",max(lost),"mean lost",sum(lost)/len(lost))
