#!/bin/sh
# Run in place, each once, after they are committed and pushed.  $1 is the seat's checkout of main; $2 a scratch directory.
cd "$(dirname "$0")" && python3 -I e7_ledger.py "$1" > e7_ledger_out.txt 2> e7_ledger_err.txt; echo "exit $?" >> e7_ledger_err.txt
python3 -I sweep_readout.py "$1" > sweep_readout_out.txt 2> sweep_readout_err.txt; echo "exit $?" >> sweep_readout_err.txt
python3 -I planted.py "$1" "$2" > planted_out.txt 2> planted_err.txt; echo "exit $?" >> planted_err.txt
