# helper: split the REVISED instrument into its cell blocks by the "# ----" section markers
import re
SRC = open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', '..', 'the_norm_of_the_boundary_class.py')).read()
parts = re.split(r'(?m)^(?=# -{20,} )', SRC)
BLK = {}
for p in parts:
    first = p.split('\n',1)[0]
    BLK[first] = p
def get(key):
    ks=[k for k in BLK if key in k]
    assert len(ks)==1, (key, ks)
    return BLK[ks[0]]
if __name__=="__main__":
    for k in BLK: print(repr(k[:100]))
