#!/usr/bin/env python3
"""
B783 / A1 -- Pointer tracking maps on the Fibonacci word.

Substitution  sigma: a -> ab, b -> a
Mirror subst  sigma_mirror: a -> ba, b -> a   (= R . sigma . R)

Two tracking modes when the current letter is 'a':
  PARENT  -- follow the left  copy (the 'a' in 'ab')
  CHILD   -- follow the right copy (the 'b' in 'ab')
When the letter is 'b', both agree (unique image).
"""

import math, sys, io

PHI = (1 + math.sqrt(5)) / 2
out_lines = []

def pr(s=""):
    out_lines.append(s)
    print(s)

# ------------------------------------------------------------------ 1
pr("=" * 72)
pr("SECTION 1 -- Fibonacci words F_0 .. F_18")
pr("=" * 72)

fibs = ["a", "ab"]
for k in range(2, 19):
    fibs.append(fibs[k - 1] + fibs[k - 2])

for k, w in enumerate(fibs):
    pr(f"  F_{k:2d}  len={len(w):6d}  prefix={w[:40]}{'...' if len(w) > 40 else ''}")

# ------------------------------------------------------------------ 2
pr()
pr("=" * 72)
pr("SECTION 2 -- Position maps  F_k -> F_{k+1}  (verify k=2 first)")
pr("=" * 72)

def build_position_map(word_k):
    """Return list of (offset, letter, parent_pos, child_pos_or_None)."""
    mapping = []
    off = 0
    for i, ch in enumerate(word_k):
        if ch == 'a':
            mapping.append((off, 'a', off, off + 1))
            off += 2
        else:
            mapping.append((off, 'b', off, None))
            off += 1
    return mapping

# Verify k=2
pr("\nVerification: F_2 = 'aba' -> F_3 = 'abaab'")
vmap = build_position_map(fibs[2])
for i, (off, ch, par, child) in enumerate(vmap):
    child_str = str(child) if child is not None else "N/A"
    pr(f"  pos {i} ('{ch}')  offset={off}  parent={par}  child={child_str}")
assert vmap == [(0, 'a', 0, 1), (2, 'b', 2, None), (3, 'a', 3, 4)], "Verification FAILED"
pr("  [VERIFIED OK]")

# Print maps for k = 0..5 (small enough)
for k in range(6):
    mp = build_position_map(fibs[k])
    pr(f"\n  Map F_{k} (len {len(fibs[k])}) -> F_{k+1} (len {len(fibs[k+1])}):")
    for i, (off, ch, par, child) in enumerate(mp):
        child_str = str(child) if child is not None else "---"
        pr(f"    i={i} '{ch}'  offset={off}  parent={par}  child={child_str}")

# ------------------------------------------------------------------ 3 & 4
pr()
pr("=" * 72)
pr("SECTION 3 & 4 -- Parent-tracking and child-tracking trajectories")
pr("           Starting positions 0..4 in F_3, tracking to F_15")
pr("=" * 72)

def track(start_k, start_pos, end_k, mode):
    """mode = 'parent' or 'child'. Returns list of (k, pos, letter, word_len)."""
    traj = []
    pos = start_pos
    for k in range(start_k, end_k + 1):
        ch = fibs[k][pos]
        traj.append((k, pos, ch, len(fibs[k])))
        if k < end_k:
            mp = build_position_map(fibs[k])
            off, letter, par, child = mp[pos]
            if letter == 'a':
                pos = par if mode == 'parent' else child
            else:
                pos = par  # only option
    return traj

START_K, END_K = 3, 15
STARTS = [0, 1, 2, 3, 4]

parent_trajs = {}
child_trajs = {}

for s in STARTS:
    parent_trajs[s] = track(START_K, s, END_K, 'parent')
    child_trajs[s] = track(START_K, s, END_K, 'child')

for mode_name, trajs in [("PARENT", parent_trajs), ("CHILD", child_trajs)]:
    pr(f"\n--- {mode_name}-tracking trajectories ---")
    for s in STARTS:
        pr(f"\n  Start pos {s} in F_3 (letter '{fibs[3][s]}'):")
        pr(f"  {'k':>3s}  {'pos':>6s}  letter  {'len(F_k)':>8s}")
        for (k, pos, ch, wlen) in trajs[s]:
            pr(f"  {k:3d}  {pos:6d}  {ch:>4s}    {wlen:8d}")

# ------------------------------------------------------------------ 5
pr()
pr("=" * 72)
pr("SECTION 5 -- Position ratios  n_{k+1} / n_k")
pr("           phi = {:.10f}".format(PHI))
pr("=" * 72)

for mode_name, trajs in [("PARENT", parent_trajs), ("CHILD", child_trajs)]:
    pr(f"\n--- {mode_name}-tracking ---")
    for s in STARTS:
        pr(f"\n  Start pos {s}:")
        t = trajs[s]
        ratios = []
        for idx in range(1, len(t)):
            n_prev = t[idx - 1][1]
            n_curr = t[idx][1]
            if n_prev == 0:
                ratio_str = "  inf (prev=0)"
            else:
                r = n_curr / n_prev
                ratio_str = f"  {r:.8f}  (diff from phi: {r - PHI:+.8f})"
                ratios.append(r)
            pr(f"    k={t[idx][0]:2d}: pos {n_curr:6d} / {n_prev:6d} = {ratio_str}")
        if ratios:
            pr(f"    last ratio = {ratios[-1]:.10f},  phi = {PHI:.10f}")

# ------------------------------------------------------------------ 6
pr()
pr("=" * 72)
pr("SECTION 6 -- Normalized positions  n_k / len(F_k)")
pr("=" * 72)

for mode_name, trajs in [("PARENT", parent_trajs), ("CHILD", child_trajs)]:
    pr(f"\n--- {mode_name}-tracking ---")
    for s in STARTS:
        pr(f"\n  Start pos {s}:")
        t = trajs[s]
        for (k, pos, ch, wlen) in t:
            norm = pos / wlen
            pr(f"    k={k:2d}: {pos:6d} / {wlen:6d} = {norm:.10f}")
        last_norm = t[-1][1] / t[-1][3]
        pr(f"    converges toward: {last_norm:.10f}")

# ------------------------------------------------------------------ 7
pr()
pr("=" * 72)
pr("SECTION 7 -- THE CRITICAL REVERSAL TEST")
pr("=" * 72)

# --- 7a: Full reversal test ---
pr("\n--- 7a: Full conjugation test ---")
pr("  sigma_mirror(a)=ba, sigma_mirror(b)=a")
pr("  Test: parent-tracking under sigma_mirror == child-tracking under sigma?")
pr("        child-tracking under sigma_mirror == parent-tracking under sigma?")

def apply_sigma(word):
    return ''.join('ab' if c == 'a' else 'a' for c in word)

def apply_sigma_mirror(word):
    return ''.join('ba' if c == 'a' else 'a' for c in word)

def build_position_map_mirror(word_k):
    """Position map for sigma_mirror: a->ba, b->a."""
    mapping = []
    off = 0
    for i, ch in enumerate(word_k):
        if ch == 'a':
            # 'a' -> 'ba', so offset gives 'b' at off, 'a' at off+1
            # PARENT of 'a' = the 'a' in 'ba' = off+1
            # CHILD  of 'a' = the 'b' in 'ba' = off
            mapping.append((off, 'a', off + 1, off))   # parent=off+1 (the 'a'), child=off (the 'b')
            off += 2
        else:
            mapping.append((off, 'b', off, None))
            off += 1
    return mapping

# Verify: sigma_mirror applied to F_k should give same result as R(sigma(R(F_k)))...
# Actually no: sigma_mirror is defined letter-by-letter with a->ba, b->a.
# The relationship is: sigma_mirror(w) = R(sigma(R(w))) only for single letters;
# for words it's: sigma_mirror(w) = sigma_mirror applied letter by letter.
# Let's verify the algebraic relationship on small examples.
pr("\n  Algebraic check: sigma_mirror(w) vs R(sigma(R(w)))")
for w in ["a", "b", "ab", "aba", "abaab"]:
    sm = apply_sigma_mirror(w)
    rsr = apply_sigma(w[::-1])[::-1]
    match = "OK" if sm == rsr else f"DIFFER: sm={sm}, rsr={rsr}"
    pr(f"    w={w:10s}  sigma_mirror(w)={sm:15s}  R(sigma(R(w)))={rsr:15s}  {match}")

# Now the actual test for each k
def track_one_step(word_k, pos, mode, use_mirror=False):
    """Track position pos in word_k through one substitution step.
    Returns new position in the substituted word."""
    if use_mirror:
        mp = build_position_map_mirror(word_k)
    else:
        mp = build_position_map(word_k)
    off, letter, par, child = mp[pos]
    if letter == 'a':
        return par if mode == 'parent' else child
    else:
        return par

pr("\n  Position-by-position reversal test:")
for k in [3, 4, 5, 6, 7, 8]:
    word_k = fibs[k]
    L = len(word_k)
    mismatches_pc = 0  # parent-sigma vs child-sigma_mirror
    mismatches_cp = 0  # child-sigma vs parent-sigma_mirror
    total_a = 0

    pr(f"\n  k={k}, F_k has length {L}:")
    detail_limit = 10 if k <= 4 else 3

    for i in range(L):
        if word_k[i] != 'a':
            continue
        total_a += 1

        # Under sigma: parent and child positions
        p_sigma = track_one_step(word_k, i, 'parent', use_mirror=False)
        c_sigma = track_one_step(word_k, i, 'child',  use_mirror=False)

        # Under sigma_mirror: parent and child positions
        p_mirror = track_one_step(word_k, i, 'parent', use_mirror=True)
        c_mirror = track_one_step(word_k, i, 'child',  use_mirror=True)

        # The conjecture: p_sigma == c_mirror  and  c_sigma == p_mirror
        match_pc = (p_sigma == c_mirror)
        match_cp = (c_sigma == p_mirror)

        if not match_pc:
            mismatches_pc += 1
        if not match_cp:
            mismatches_cp += 1

        if total_a <= detail_limit:
            pr(f"    i={i:4d}  p_sigma={p_sigma:5d}  c_sigma={c_sigma:5d}"
               f"  p_mirror={p_mirror:5d}  c_mirror={c_mirror:5d}"
               f"  p==c_m:{match_pc}  c==p_m:{match_cp}")

    pr(f"    Total 'a' positions: {total_a}")
    pr(f"    parent_sigma == child_mirror mismatches:  {mismatches_pc}")
    pr(f"    child_sigma  == parent_mirror mismatches: {mismatches_cp}")
    if mismatches_pc == 0 and mismatches_cp == 0:
        pr(f"    *** PERFECT SWAP: reversal exactly exchanges parent <-> child ***")
    else:
        pr(f"    *** SWAP FAILS for {mismatches_pc + mismatches_cp} cases ***")

# --- 7b: Multi-step trajectory reversal test ---
pr("\n--- 7b: Multi-step trajectory test ---")
pr("  Does a full parent-trajectory under sigma equal full child-trajectory under sigma_mirror?")

def track_multi(start_k, start_pos, end_k, mode, use_mirror=False):
    """Track through multiple substitution steps."""
    traj = []
    pos = start_pos
    for k in range(start_k, end_k + 1):
        word_k = fibs[k]
        ch = word_k[pos]
        traj.append((k, pos, ch))
        if k < end_k:
            pos = track_one_step(word_k, pos, mode, use_mirror=use_mirror)
    return traj

for s in STARTS:
    p_sigma  = track_multi(START_K, s, END_K, 'parent', use_mirror=False)
    c_mirror = track_multi(START_K, s, END_K, 'child',  use_mirror=True)
    c_sigma  = track_multi(START_K, s, END_K, 'child',  use_mirror=False)
    p_mirror = track_multi(START_K, s, END_K, 'parent', use_mirror=True)

    match1 = all(a[1] == b[1] for a, b in zip(p_sigma, c_mirror))
    match2 = all(a[1] == b[1] for a, b in zip(c_sigma, p_mirror))

    pr(f"\n  Start pos {s}:")
    pr(f"    parent(sigma) positions:       {[t[1] for t in p_sigma]}")
    pr(f"    child(sigma_mirror) positions: {[t[1] for t in c_mirror]}")
    pr(f"    MATCH: {match1}")
    pr(f"    child(sigma) positions:        {[t[1] for t in c_sigma]}")
    pr(f"    parent(sigma_mirror) positions:{[t[1] for t in p_mirror]}")
    pr(f"    MATCH: {match2}")

# ------------------------------------------------------------------ 8
pr()
pr("=" * 72)
pr("SECTION 8 -- Letter-visit patterns (start pos 0 in F_3)")
pr("=" * 72)

for mode_name, trajs in [("PARENT", parent_trajs), ("CHILD", child_trajs)]:
    t = trajs[0]
    letters = [ch for (k, pos, ch, wlen) in t]
    a_count = letters.count('a')
    b_count = letters.count('b')
    total = len(letters)
    pr(f"\n  {mode_name}-tracking from pos 0:")
    pr(f"    Letter sequence: {' '.join(letters)}")
    pr(f"    a-count: {a_count}/{total} = {a_count/total:.6f}")
    pr(f"    b-count: {b_count}/{total} = {b_count/total:.6f}")
    pr(f"    Expected d(a) = 1/phi = {1/PHI:.6f}")

# ------------------------------------------------------------------ 9
pr()
pr("=" * 72)
pr("SECTION 9 -- Choice patterns")
pr("=" * 72)
pr("  At each step, record: letter at current position, and which way we went.")
pr("  'P' = parent chosen, 'C' = child chosen, '.' = no choice (letter was b)")

for mode_name, trajs in [("PARENT", parent_trajs), ("CHILD", child_trajs)]:
    pr(f"\n  {mode_name}-tracking:")
    for s in STARTS:
        t = trajs[s]
        choices = []
        for (k, pos, ch, wlen) in t[:-1]:  # no choice at last step
            if ch == 'a':
                choices.append('P' if mode_name == 'PARENT' else 'C')
            else:
                choices.append('.')
        pr(f"    Start {s}: {''.join(choices)}  (choices at 'a': {choices.count('P') + choices.count('C')}, forced at 'b': {choices.count('.')})")

# ------------------------------------------------------------------ 10
pr()
pr("=" * 72)
pr("SECTION 10 -- A vs B density along trajectories")
pr("=" * 72)
pr(f"  Global density: d(a) = 1/phi = {1/PHI:.10f}")
pr(f"                  d(b) = 1/phi^2 = {1/PHI**2:.10f}")

for mode_name, trajs in [("PARENT", parent_trajs), ("CHILD", child_trajs)]:
    pr(f"\n  {mode_name}-tracking:")
    for s in STARTS:
        t = trajs[s]
        letters = [ch for (k, pos, ch, wlen) in t]
        a_count = letters.count('a')
        b_count = letters.count('b')
        total = len(letters)
        a_frac = a_count / total
        b_frac = b_count / total
        pr(f"    Start {s}: a={a_count}/{total}={a_frac:.6f}  b={b_count}/{total}={b_frac:.6f}"
           f"  (dev from global: {a_frac - 1/PHI:+.6f})")

pr()
pr("=" * 72)
pr("SUMMARY")
pr("=" * 72)
pr(f"  phi = {PHI:.10f}")
pr(f"  1/phi = {1/PHI:.10f}")
pr(f"  Fibonacci word lengths: {[len(fibs[k]) for k in range(19)]}")

# Check ratio convergence
pr("\n  Position ratio convergence (last 3 steps, start pos 0):")
for mode_name, trajs in [("PARENT", parent_trajs), ("CHILD", child_trajs)]:
    t = trajs[0]
    for idx in range(len(t)-3, len(t)):
        if t[idx-1][1] > 0:
            r = t[idx][1] / t[idx-1][1]
            pr(f"    {mode_name} k={t[idx][0]}: {r:.10f}")

pr("\n  Normalized position convergence (last step, all starts):")
for mode_name, trajs in [("PARENT", parent_trajs), ("CHILD", child_trajs)]:
    for s in STARTS:
        t = trajs[s]
        norm = t[-1][1] / t[-1][3]
        pr(f"    {mode_name} start={s}: n/L = {norm:.10f}")

# Write output
OUTPUT_PATH = "/Users/dri/oa-audit-seat/origin-axiom/frontier/B783_observer_ground_zero/A1_tracking_computation.txt"
with open(OUTPUT_PATH, 'w') as f:
    f.write('\n'.join(out_lines) + '\n')
print(f"\n[Output saved to {OUTPUT_PATH}]")
