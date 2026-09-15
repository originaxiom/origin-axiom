# E₆ subregular WDD identification

## Source
arXiv:1203.2930 (Chacaltana–Distler–Tachikawa), Table 14, row E₆(a₁).

## What the table shows
The E₆ nilpotent orbits with their weighted Dynkin diagrams.
E₆(a₁) (the unique subregular orbit, dim 70) has WDD displayed as:

```
     2
  2  0  2  2
```

In Bourbaki ordering for E₆:
```
1 — 3 — 4 — 5 — 6
        |
        2
```
Node 4 (Bourbaki α₄) is TRIVALENT (valence 3, connected to nodes 3, 5, 2).

The table's format: bottom row = chain nodes (1,3,4,5,6), top = branch node (2).
Reading off: α₁=2, α₂=2, α₃=0, α₄=2, α₅=2, α₆=2.

**The zero is on α₃ (Bourbaki), which is connected to α₁ and α₄.**

## My Cartan matrix mapping
My Cartan matrix has the trivalent node at index 2 (= "my node 3"):
```python
E6_cartan[2,:] = [0, -1, 2, -1, 0, -1]  # connected to indices 1, 3, 5
```
So: Bourbaki α₄ (trivalent) = my node 3 (index 2).

**CORRECTION: the table's "0" is on Bourbaki α₃, NOT on the trivalent α₄.**

In my indexing: Bourbaki α₃ maps to my node 2 (index 1), which has valence 2.
So the zero is at my node 2, NOT my node 3 (trivalent).

## The decomposition at my node 2 (= Bourbaki α₃)
From my computation: zero at my node 2 gives decomposition [19, 15, 13, 11, 9, 7, 3, 1].
V₁ = 1, V₃ = 1 → h¹ = 2.

## WAIT — this contradicts what I reported

I reported h¹ = 1 (same as principal), citing zero at the trivalent node.
If the zero is actually at α₃ (non-trivalent), the decomposition is DIFFERENT
and gives h¹ = 2.

**THIS IDENTIFICATION NEEDS INDEPENDENT VERIFICATION BY CC.**
The mapping between Bourbaki's numbering and my Cartan matrix rows is the
single point of failure. I got confused between α₃ and α₄ multiple times
during the session.

## What CC should check
1. Which node in the E₆ Dynkin diagram carries value 0 in the E₆(a₁) row of Table 14
2. Map that node to the Cartan matrix used in the computation
3. Recompute the decomposition of the 78 under that sl(2)
4. Count V₁ and V₃ summands to get h¹

If h¹ = 2 (not 1), the subregular escape hatch is OPEN, not closed.


*(main's note: two invalid bytes in the seat's file were replaced on archiving; content unchanged.)*
