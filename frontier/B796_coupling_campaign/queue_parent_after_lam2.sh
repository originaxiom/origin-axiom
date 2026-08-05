#!/bin/bash
# Auto-queue: waits for the lam_2 process to exit, then launches the
# parent (7.072004187) run under the same sealed protocol (v3 169e9042).
cd /Users/dri/oa-audit-seat/origin-axiom
while pgrep -f "cell9_rung1_v2.py 4.900085373" >/dev/null; do sleep 300; done
sleep 60  # let the JSON flush
echo "[queue] lam_2 process ended $(date)" >> frontier/B796_coupling_campaign/cell9_queue_log.txt
nohup python frontier/B796_coupling_campaign/cell9_rung1_v2.py 7.072004187 \
  >> frontier/B796_coupling_campaign/cell9_parent_real_log.txt 2>&1 &
echo "[queue] parent launched $(date)" >> frontier/B796_coupling_campaign/cell9_queue_log.txt
