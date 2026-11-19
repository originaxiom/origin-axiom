"""The web seat's THE CHANNEL NORMS' PAIR SUMS (row 1516; in the register since row 1968): the claims main settles here.
Nothing of the seat's is run.
 Q1  section 4: for the distance to the integers, ||ax + ay|| >= | ||ax|| - ||ay|| |, and 1/2 - ||ax + ay|| >= | 1/2 - ||ax|| - ||ay|| |,
     on 200 000 random pairs and on the pairs of fractions a/n, b/m with n, m <= 40 and a + b divisible by 7 (a subset, not
     every pair; corrected 2026-11-19 at the web seat's section 32.2: this line said 'every pair').
 Q2  section 7: c_inf(l) = -2 pi ln 2 pi - 2 pi gamma - pi [psi(l) + psi(1 - l)] at l = 3/8 and 1/8 against the closed forms
     2 pi [ln(8/pi) -+ sqrt 2 ln(1 + sqrt 2)] and the stated digits; P-512's x at L_max and L_2 (main's B1667 values), its zero
     and its quarter point.
 Q3  section 5: K(u; -S) = -K(-u; S) for K = theta1'(0) theta[c](u) / (theta[c](0) theta1(u)), at random c, u, tau.
 Q4  the record it quotes (lines 37 to 93): each double-quoted phrase of 12 characters or more, searched in main's tree at
     354a4ea4d (the head the note read) and now."""
import random, itertools, subprocess, re, json, sys
from fractions import Fraction as Fr
import mpmath as mp
mp.mp.dps = 30
d = lambda x: abs(x - round(x))
random.seed(1); bad1 = bad2 = 0
pairs = [(random.random(), random.random()) for _ in range(200000)] + [(Fr(a, n), Fr(b, m)) for n in range(1, 41) for m in range(1, 41) for a in range(n) for b in range(m) if (a + b) % 7 == 0][:200000]
for ax, ay in pairs:
    ax, ay = float(ax), float(ay)
    if d(ax + ay) < abs(d(ax) - d(ay)) - 1e-12: bad1 += 1
    if 0.5 - d(ax + ay) < abs(0.5 - d(ax) - d(ay)) - 1e-12: bad2 += 1
print("Q1: pairs %d; violations of the first inequality %d, of the second %d" % (len(pairs), bad1, bad2))
cinf = lambda l: -2 * mp.pi * mp.log(2 * mp.pi) - 2 * mp.pi * mp.euler - mp.pi * (mp.digamma(l) + mp.digamma(1 - l))
c1, cb = cinf(mp.mpf(3) / 8), cinf(mp.mpf(1) / 8)
f1 = 2 * mp.pi * (mp.log(8 / mp.pi) - mp.sqrt(2) * mp.log(1 + mp.sqrt(2))); fb = 2 * mp.pi * (mp.log(8 / mp.pi) + mp.sqrt(2) * mp.log(1 + mp.sqrt(2)))
x = lambda L: (2 * mp.pi * L + c1) / (2 * mp.pi * L + cb)
L0 = mp.sqrt(2) * mp.log(1 + mp.sqrt(2)) - mp.log(8 / mp.pi); Lq = (5 * mp.sqrt(2) * mp.log(1 + mp.sqrt(2)) - 3 * mp.log(8 / mp.pi)) / 3
print("Q2: c_inf(3/8) = %s (closed form %s, stated -1.95871280146); c_inf(1/8) = %s (closed form %s, stated 13.7046458862); x = 0 at L = %s (stated 0.311738824); x = 1/4 at L = %s (stated 1.14270581), x there %s"
      % (mp.nstr(c1, 14), mp.nstr(f1, 14), mp.nstr(cb, 14), mp.nstr(fb, 14), mp.nstr(L0, 10), mp.nstr(Lq, 10), mp.nstr(x(Lq), 10)))
th = lambda a, b, u, t: mp.nsum(lambda n: mp.exp(1j * mp.pi * t * (n + a) ** 2 + 2j * mp.pi * (n + a) * (u + b)), [-mp.inf, mp.inf])
th1 = lambda u, t: -th(mp.mpf(1) / 2, mp.mpf(1) / 2, u, t)
dth1 = lambda t: mp.diff(lambda u: th1(u, t), 0)
K = lambda u, a, b, t: dth1(t) * th(a, b, u, t) / (th(a, b, 0, t) * th1(u, t))
worst = 0
for _ in range(5):
    a, b = mp.mpf(random.random()), mp.mpf(random.random()); u = mp.mpc(random.random() * 0.4 + 0.05, random.random() * 0.3); t = mp.mpc(random.random() - 0.5, 1 + random.random())
    worst = max(worst, abs(K(u, -a, -b, t) + K(-u, a, b, t)) / abs(K(u, a, b, t)))
print("Q3: worst relative |K(u; -c) + K(-u; c)| on 5 random points: %s" % mp.nstr(worst, 3))
note = subprocess.run(["git", "show", "61a0684e0:relays/CHAT1_TO_CC_2026-11-03_THE_CHANNEL_NORMS_PAIR_SUMS_AND_B1788S_HYPOTHESES.md"], capture_output=True, text=True).stdout.split("\n")
found = {}
for ln in range(37, 94):
    for q in re.findall(r'"([^"]{12,})"', note[ln - 1]):
        q2 = q.split(" … ")[0].split("…")[0].strip()
        hit = {at: subprocess.run(["git", "grep", "-l", "-F", q2[:60], at, "--", "docs", "frontier", "audit"], capture_output=True, text=True).stdout.strip() != "" for at in ("354a4ea4d", "HEAD")}
        found[ln] = found.get(ln, []) + [(q2[:50], hit)]
print("Q4: %s" % json.dumps({k: [(q, h["354a4ea4d"], h["HEAD"]) for q, h in v] for k, v in found.items()}, ensure_ascii=False))
