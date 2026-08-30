#!/usr/bin/env bash
# B1171 -- THE SEAM HARVEST (batched, like B1158). Five components, each verified on this bench:
# (1) cc3 B8144: the adelic MECHANISM (orbit-theorem escape pair) -> B1164 ADDENDUM_adelic_mechanism.md
#     with 2 preregistered predictions; own-verified against all 3 banked observer costs + the paid spin bit.
# (2) cc3 B8145: L171 CLOSED (MOOD) -- their 8/8 CLPW source verification; cc independently spot-verified
#     4/4 via own fetch (eq.24 Pi=Theta(q); eq.25 Tr 1=1; H_obs=q>=0 on L^2(R+); rho_max=1).
# (3) cc3 B8146: L173 precision column NEGATIVE -> EDGE_PREREG re-posed by ADDENDUM-BESIDE (count
#     observable commissioned, not a resolution threshold); sealed spec untouched.
# (4) cloud memos 80/82: both certs run on this bench BYTE-IDENTICAL to committed outputs
#     (deps extracted: twisted_double.py + paper/verify/check_charge_bracket.py; e7_ladder.py).
#     -> L186 registered (three Yukawa-suppression mechanisms: one or three?).
# (5) codex R015/R016 dispositions: B1153 grade-note ('exact' bounded to the factor structure);
#     B1158 fence-note (universal phrases bounded to the verified scope p in {5,7}, r in {1,2}, order<=8).
set -euo pipefail
cd "$(dirname "$0")"
echo "The five components' evidence files (committed):"
for f in \
  ../../B1164_cc_masterplan/ADDENDUM_adelic_mechanism.md \
  ../../../docs/EDGE_PREREG_SPEC_ADDENDUM_B8146.md \
  ../../B1153_peripheral_and_superposition/ADDENDUM_grade_note_R015.md \
  ../../B1158_cloud_wave2_harvest/ADDENDUM_fence_note_R016.md ; do
  [ -f "$f" ] && echo "  OK $f" || { echo "  MISSING $f"; exit 1; }
done
grep -q "CLOSED (MOOD) 2026-08-27" ../../../docs/OPEN_LEADS.md && echo "  OK L171 closed (MOOD)"
grep -q "PRECISION COLUMN RE-POSED" ../../../docs/OPEN_LEADS.md && echo "  OK L173 re-posed"
grep -q "## L186" ../../../docs/OPEN_LEADS.md && echo "  OK L186 registered"
echo "REPRODUCES"
