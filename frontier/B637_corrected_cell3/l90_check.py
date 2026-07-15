"""L90 close — B575's cup corrections vanish per-term (in-repo).

The corrected 2-cell chain adds, at each inverse letter x_i = l^-1,
the term -bracket(P_{i-1}.u(l^-1), P_i.v(l)). For ADJOINT cocycles
u(l^-1) = -Ad(l^-1) u(l), so P_{i-1}.u(l^-1) = -P_i.u(l): the diagonal
term is bracket(-y, y) = 0 and the polarized sum cancels by
antisymmetry. Verify the identity P_{i-1}.u(l^-1) = -P_i.u(l) EXACTLY
for every inverse-letter position and every block cocycle.
"""
import os, time
HERE = os.path.dirname(os.path.abspath(__file__))
L51 = os.path.join(HERE, "..", "B575_bridge_obstruction", "l51_obstruction.py")
src = open(L51).read()
cut = src.index("def cup_on_relator")
ns = {"__name__": "l90_check", "__file__": L51}
t0 = time.time()
exec(compile(src[:cut], L51, "exec"), ns)
print(f"l51 prefix+stage4 loaded in {time.time()-t0:.0f}s", flush=True)

REL = ns["REL"]
PREFIX, PREFIX_INV = ns["PREFIX"], ns["PREFIX_INV"]
letter_cocycle = ns["letter_cocycle"]
conj = ns["conj"]
BLOCK_DATA = ns["BLOCK_DATA"]
madd, mscale, mzero_p, mmul = (ns[k] for k in
                               ("madd", "mscale", "mzero_p", "mmul"))
A27, B27, A27i, B27i = ns["A27"], ns["B27"], ns["A27i"], ns["B27i"]
meye = ns["meye"]
LET = {'a': (A27, A27i), 'b': (B27, B27i),
       'A': (A27i, A27), 'B': (B27i, B27)}

nrel = len(REL)
allok = True
for m, D in BLOCK_DATA.items():
    u = D['u']
    for i, ch in enumerate(REL):
        if ch not in 'AB':
            continue
        ell = ch.lower()
        # x = P_{i-1} . u(l^-1)   (prefix action = conjugation for adjoint)
        Xi = conj(PREFIX[i], PREFIX_INV[i], letter_cocycle(m, u, ch))
        # y = P_i . u(l): P_i = P_{i-1} * letter(ch)
        Pnext = mmul(PREFIX[i], LET[ch][0])
        Pnext_i = mmul(LET[ch][1], PREFIX_INV[i])
        Yi = conj(Pnext, Pnext_i, letter_cocycle(m, u, ell))
        ok = mzero_p(madd(Xi, Yi))
        allok = allok and ok
        if not ok:
            print(f"  block m={m}, pos {i} ({ch}): x = -y FAILS", flush=True)
print(f"per-term identity x = -y for all inverse letters, all 6 blocks: "
      f"{allok}", flush=True)
assert allok
print("L90 CLOSED: the corrections vanish per-term; B575's Q == 0 is "
      "untouched by the corrected chain.", flush=True)
