#!/bin/sh
set -e
D=frontier/B1229_the_consistency_turn
python3 $D/bootstrap.py && python3 $D/consistency_ledger.py && python3 $D/endstate.py
