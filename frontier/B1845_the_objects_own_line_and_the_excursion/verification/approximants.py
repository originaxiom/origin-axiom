from mpmath import mp, sqrt, matrix
mp.dps = 30
L = matrix([[1,0],[1,1]]); R = matrix([[1,1],[0,1]]); S = matrix([[0,-1],[1,0]]); Si = matrix([[0,1],[-1,0]])
def word(s):
    M = matrix([[1,0],[0,1]])
    for ch in s: M = M * (L if ch == 'L' else R)
    return M
def apex(M):
    a,b,c,d = M[0,0],M[0,1],M[1,0],M[1,1]
    disc = (a+d)**2 - 4
    if c == 0: return None
    x1 = ((a - d) + sqrt(disc)) / (2*c); x2 = ((a - d) - sqrt(disc)) / (2*c)
    return ((x1 + x2)/2) % 1, abs(x1 - x2)/2
def top(s):
    best = (0, 0)
    for i in range(len(s)):
        w = word(s[i:] + s[:i])
        for M in (w, S * w * Si):
            r = apex(M)
            if r and r[1] > best[1]: best = r
    return best
def cf_lagrange(seq):
    # max over i of (a_i + [0; a_{i+1}, ...] + [0; a_{i-1}, ...]) / 2 for the periodic sequence
    n = len(seq); best = 0
    def tail(start, step):
        x = mp.mpf(0)
        for j in range(400, 0, -1): x = 1 / (seq[(start + step*j) % n] + x)
        return x
    for i in range(n):
        h = (seq[i] + tail(i, 1) + tail(i, -1)) / 2
        best = max(best, h)
    return best
target = 2 + sqrt(5)/2
for k in range(0, 13):
    s = 'L'*5 + 'R' + 'LR'*k
    re, im = top(s); lag = cf_lagrange([5] + [1]*(1 + 2*k))
    print("k=%2d  highest apex (orbit incl. S) Re %.6f Im %.12f | CF formula %.12f | Im - (2+sqrt5/2) = %+.2e" % (k, float(re), float(im), float(lag), float(im - target)))
