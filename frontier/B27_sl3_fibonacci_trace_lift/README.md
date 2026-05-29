# B27 -- SL(3) Fibonacci Trace Lift

Status: `frontier` / `STALLED`.

## Question

Does the half-step trace-lift structure survive when the character variety is
lifted from `SL(2)` to `SL(3)`?

## Scope

This probe computes the Fibonacci substitution

```text
sigma(a)=ab,  sigma(b)=a
```

on the standard eight trace coordinates for `SL(3)` representations of the free
group on two generators. It tests exact algebra only:

```text
x1=tr(a)          x2=tr(a^-1)
x3=tr(b)          x4=tr(b^-1)
x5=tr(ab)         x6=tr((ab)^-1)
x7=tr(ab^-1)      x8=tr(a^-1 b)
```

No physical particle, antiparticle, gauge, or spacetime interpretation is
claimed.

## Run

```bash
python frontier/B27_sl3_fibonacci_trace_lift/probe.py
```
