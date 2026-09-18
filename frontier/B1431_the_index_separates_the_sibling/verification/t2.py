import time
from fractions import Fraction as F
from idx import index_class
from tet_index import s_str
for nm in ["m006","m015","m022"]:
    for cls in [(F(0),F(0)),(F(2),F(2))]:
        t=time.time(); s=index_class(nm,(cls,),44); print(f"{nm} {cls} {time.time()-t:.2f}s {s_str(s,24)[:90]}")
