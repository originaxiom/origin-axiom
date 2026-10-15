import sys; sys.path.insert(0,'.')
from ref3 import *
for w,N in (("LLLLLRR",5),("LLRRRRR",5),("LLLR",3),("LLR",2)):
    print(w, word(w), "N=",N); run(word(w),N)
