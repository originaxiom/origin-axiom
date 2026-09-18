import sys, json, warnings, time
warnings.filterwarnings("ignore")
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from v3_full_character_variety import analyse
out={}
for n,e in [(6,40),(7,29)]:
    t=time.time()
    try:
        r=analyse(n,e,verbose=False)
        r.pop('per_component',None); r['seconds']=round(time.time()-t,1)
        out[n]=r; print(json.dumps(r),flush=True)
    except Exception as ex:
        print(n,"FAILED",ex,flush=True)
json.dump(out,open('<here>/v8_h12_high.json','w'),indent=1,default=str)
