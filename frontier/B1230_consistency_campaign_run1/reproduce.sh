#!/bin/sh
set -e
D=frontier/B1230_consistency_campaign_run1
python3 $D/c1_basefield_audit.py && python3 $D/c5_menu_robustness.py && python3 $D/c5b_the_Z3_does_the_work.py
