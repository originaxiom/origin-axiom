import time
from fractions import Fraction as F
from idx import index_class
from tet_index import s_str
for X in [30,44,60]:
    for name in ["m004","m003"]:
        for cls in [(F(0),F(0)),(F(3),F(3))]:
            t=time.time(); s=index_class(name,(cls,),X); dt=time.time()-t
            print(f"{name} X={X} cls={cls}  {dt:.2f}s  -> {s_str(s, min(X-8,24))}")
