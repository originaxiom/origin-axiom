"""T1 step 4 -- typing the BLOCK: is the ACTUAL down/lepton coupling's Higgs-connecting
block anywhere in this repository? Programmatic probe with receipts.

What would unblock the cell (any one of):
  (D1) an exact Q(zeta_12) 1x18 (or 36-entry) down-Yukawa row/block;
  (D2) even a finite-field (GF(1009)) VALUE vector for the connecting entries;
  (D3) codex's in-flight artifacts: certify_yukawa_down_tail_cech_308.sage output values,
       the lepton connecting-block-at-three-good-primes transcript, or the normalized
       evaluator T_cal = (Delta_G, Tr_{Y,Omega}, S).
"""
import os, re, subprocess

ROOT = "/home/user/origin-axiom"

def grep(pattern, msg):
    r = subprocess.run(["grep", "-rl", "-E", pattern, ROOT,
                        "--include=*.py", "--include=*.md", "--include=*.json",
                        "--include=*.txt", "--include=*.sage", "--exclude-dir=.git",
                        "--exclude-dir=T1_third_column"],
                       capture_output=True, text=True)
    hits = [h for h in r.stdout.strip().split("\n") if h]
    print(f"  {msg}: {len(hits)} file(s)")
    for h in hits[:6]: print(f"    - {os.path.relpath(h, ROOT)}")
    return hits

print("[probe 1] the evaluator's load-target (flagged single-homed by B1185, E51 class):")
sage_hits = grep(r"certify_yukawa_down_tail_cech_308\.sage", "mentions of the .sage load-target")
sage_present = any(h.endswith(".sage") for h in sage_hits)
print(f"  -> the .sage FILE itself committed anywhere: {sage_present}")

print("[probe 2] codex's seat (B1232 re-ran their certs from a local path):")
codex_path = "/Users/dri/oa-audit-seat/aud1t/codex-r023"
print(f"  {codex_path} exists on this bench: {os.path.exists(codex_path)} (macOS path; this is a Linux container)")

print("[probe 3] any committed numeric/exact down-Yukawa entry value:")
grep(r"T_(i,j,k|connecting).*=.*[0-9]", "assigned T_connecting/T_ijk values")
grep(r"lepton connecting block", "lepton connecting-block transcripts")

print("[probe 4] the two committed spec documents' own proof boundaries (verbatim):")
spec = os.path.join(ROOT, "frontier/B1212_two_replies/documents/program-question-map/evidence/YUKAWA_DOWN_RESIDUE_SPEC_308.md")
memo = os.path.join(ROOT, "frontier/B1212_two_replies/memos/YUKAWA_CUP_PRODUCTS_308.md")
for f, keys in [(spec, ["No numerical or exact", "Not proved:"]),
                (memo, ["no nonzero down entry or rank"])]:
    txt = open(f).read()
    for k in keys:
        line = next((l.strip() for l in txt.splitlines() if k in l), None)
        print(f"  {os.path.basename(f)}: \"{line}\"")

print("""
S4 VERDICT: BLOCKED, datum typed.
  MISSING: the 27 Higgs-connecting entries T[i,j,conn_k] of the selected (A_7,B_6,B_2) block
  (equivalently the normalized evaluator T_cal = (Delta_G, Tr_{Y,Omega}, S) over Q(zeta_12),
  or at minimum codex's GF(1009) connecting-row values and the lepton three-good-primes
  transcript). Looked in: all committed frontier/, docs/, tests/, papers/ trees (grep above);
  codex's seat path (absent on this bench); the two committed spec documents, whose own proof
  boundaries state the values are not committed. The (3,4,1) sequence and the decision
  criterion are NOT missing -- s1/s2 supply them from committed data.""")
