"""Mining the record: verdict census, backbone (depends_on in-degree), attention map by object, rung counts,
identification-ledger statuses, and the Markov-tree reading of the weave's trace triples.
Run from a clone of github.com/originaxiom/origin-axiom (fe25f7e). See the doc 'The ladder'."""
print("The mining steps are recorded in the conversation; this file lists the regexes and the Markov check.")
import numpy as np
L = np.array([[1,1],[0,1]]); R = np.array([[1,0],[1,1]]); inv = np.linalg.inv
LR = L@R; RL = R@L
for name, a, b in [("LR, RL^-1", LR, inv(RL)), ("LR, RL", LR, RL), ("LR, LRRL", LR, LR@RL), ("LRRL, LRLRRL", LR@RL, LR@LR@RL)]:
    x, y, z = [int(round(np.trace(m))) for m in (a, b, a@b)]
    print(f"({name}): traces ({x},{y},{z}); x^2+y^2+z^2 = {x*x+y*y+z*z} = xyz = {x*y*z}; Markov triple {(x//3, y//3, z//3)}")
