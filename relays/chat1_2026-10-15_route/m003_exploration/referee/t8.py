import sys; sys.path.insert(0,'.')
from ref4 import *
for w,N in (("LLLLLRR",5),("LLRRRRR",5),("LLLR",3),("LLR",2)):
    print(w, word(w)); run2(word(w),N)
