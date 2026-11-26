seat: sm2
read: M2
state: working
on: P1, P2
needs: nothing
next push: when V_P1 and V_P2 and their hashes are committed

- seat code: fam1-v1-unset-05
- branch: sm2/banking
- listener: python3 scripts/seats/listen.py --seat sm2, running in the background
