# B52 Literature Scan

## Question

For multichannel, strip, matrix-valued, or spinful Fibonacci / quasiperiodic
Schrodinger models, do the physical transfer matrices live in `SL(3)` and induce
the PC12 Cayley-Hamilton recursion?

## Sources Checked

### Classical Fibonacci Hamiltonian

David Damanik, Anton Gorodetski, and William Yessen, *The Fibonacci
Hamiltonian*, Inventiones Mathematicae 206 (2016).

```text
model: scalar one-dimensional Fibonacci Hamiltonian
transfer group: 2x2 / SL(2,R)
trace map: classical Fibonacci trace map and Fricke-Vogt invariant
match to PC12 T_m: no; this is the SL(2) baseline, not higher-rank SL(3)
```

Source: https://arxiv.org/abs/1403.7823

### Tridiagonal Fibonacci Jacobi Operators

William Yessen, *Spectral analysis of tridiagonal Fibonacci Hamiltonians*,
Journal of Spectral Theory 3 (2013), 101-128.

```text
model: one-dimensional Jacobi operators with Fibonacci diagonal/off-diagonal data
transfer group: still second-order one-dimensional transfer matrices
trace map: trace-map methods
match to PC12 T_m: no evidence of SL(3) character-variety recursion
```

Source: https://ems.press/journals/jst/articles/11751

### General Trace Maps For Substitution Sequences

Y. Avishai, D. Berend, and V. Tkachenko, *Trace maps*, International Journal of
Modern Physics B 11 (1997), 3525-3542.

```text
model: products of 2x2 transfer matrices for substitution systems
transfer group: 2x2 matrices
trace map: minimal-dimensional trace maps for substitution sequences
match to PC12 T_m: no; useful positioning for the SL(2) substitution-map lineage
```

Source: https://cris.bgu.ac.il/en/publications/trace-maps

### Matrix-Valued / Block Jacobi Operators

The block Jacobi literature rewrites an `L`-channel second-order equation using
`2L x 2L` transfer matrices. For real energies, the transfer matrices lie in
symplectic groups.

```text
model: Jacobi matrices with LxL matrix entries
transfer group: Sp(2L), with 2L-dimensional doubled phase space
trace map: not the PC12 SL(3) character-variety map
match to PC12 T_m: no; for L=3 the natural transfer matrices are 6x6
```

Representative source: https://web.ma.utexas.edu/mpej/Vol/13/5.pdf

### Spinful Fibonacci-Modulated Chain

Recent spin-orbit / two-component Fibonacci-modulated chains use a transfer
matrix scheme on doubled right/left-moving or position/momentum components.

```text
model: spinful one-dimensional chain with Fibonacci onsite modulation
transfer group: doubled block transfer matrices, e.g. 4x4 for two components
trace map: scattering/transfer computation, not PC12 T_m
match to PC12 T_m: no
```

Representative source: https://www.nature.com/articles/s42005-025-02264-1

## Conclusion

The literature supports the B52 control result: multichannel physical transfer
matrices naturally double the channel dimension and live in symplectic-type
phase-space groups. I found no source in this scan where a three-channel
Fibonacci tight-binding model yields an `SL(3)` transfer matrix whose trace-map
renormalization is the PC12 `T_m`.

This does not kill PC12. It keeps PC12 in the correct category: character-variety
mathematics unless and until a verified physical dictionary is built.
