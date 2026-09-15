# Reader r3 — memo 219 (PARI_ARRIVES_AND_THE_LITERATURE_WALL)

## 1. HEADLINE
"PARI ARRIVES AND IS VALIDATED; AND THE LITERATURE CHANNEL IS NARROWER THAN
'UNREAD'." **2026-09-13.**

## 2. CLAIMS
1. PARI/GP 2.15.4 (amd64, GMP-6.3.0) installed from the **signed Ubuntu
   noble/universe archive** via `apt-get`; no third-party source, no build from
   source, no TLS bypass, no proxy bypass; two unrelated PPAs refused by the
   gateway and left refused; 28G free after. — **installation fact, verified operationally**
2. **7 of 7 checks agree** between PARI and B1093's hand proof on
   `K = ℚ[x]/(x³−12x−5)`: disc = 6237; `ℤ[θ]=O_K` (index 1); signature [3,0]
   (totally real); class number h=1, class group `[]`; both fundamental units
   `x²+2x−4`, `3x²+6x+2`; narrow class number `[1,[],[]]`. — **VERIFIED, exact agreement**
3. Operational note: `bnfinit(...,1)` (unconditional certification) hangs; without
   it the computation returns in under a second — **flagged, not a correctness issue**
4. The literature channel is narrower than "unread": `arxiv.org`,
   `people.tamu.edu` (author's own copy), `escholarship.org` all return
   `EGRESS_BLOCKED`; only WebSearch works. Replaces "literature, unread here" (memos
   211/214/218) with "unreachable from here, by a named network policy." — **measured, verified operationally**
5. Search-derived (labelled, not read): Rowell–Stong–Wang (arXiv:0712.1377)
   classify rank≤4 unitary MTCs — 35 up to ribbon equivalence from 10 non-trivial
   prime UMTCs. Mignard–Schauenburg (arXiv:1708.02796): modular data does not
   determine the category; smallest known counterexample family is **rank 49**
   (`G=ℤ₁₁⋊ℤ₅`). — **SEARCH-DERIVED, explicitly not verified as theorems here**
6. Memo 211's rank-3 Müger-centraliser residual: both facts point the same way (a
   finite classified list; the known failure is 14 ranks up) but **"still not
   discharged"** on search summaries alone — the bench does not close a residual
   that way. — **explicit non-closure, stated standard**
7. What PARI does NOT unblock: memo 204 addendum 4's "is E split over K?" is only
   half a PARI question — the quaternion algebra is pinned as `(77,b)_K` with `b`
   **unknown**; PARI decides splitting from `(a,b)` but cannot supply `b`. The live
   computable item is instead the 48×48 commutant over ℚ ("twice killed by resource
   limits" under sympy) — **named, not attempted in this memo**.
8. **ADDENDUM 1** (same day): §6's "still not discharged" is **SUPERSEDED** — the
   owner supplied both settling PDFs; memo 220 reads RSW §5.4 verbatim and closes
   the residual (our centraliser = the complex conjugate of RSW's listed
   representative, exact match on fusion rules and quantum dimensions). — **superseded in place, resolved positively**
9. **ADDENDUM 2** (2026-09-13): §7's "live computable item" (the 48×48 commutant) is
   **discharged without being run** — the owner supplied KMRT; memo 222 answers "is
   E split over K?" = **YES**, via KMRT Prop. 43.6 + a finite exhaustive local
   computation (`n_p ≤ 1` for every prime p, forced even by corestriction, hence 0;
   unramified everywhere ⇒ split). — **superseded in place, resolved positively, cheaper route than the named commutant**

## 3. CERTIFICATE
`outside_bench/certificates/pari_arrives.py` exists.
`outside_bench/outputs/pari_arrives.txt` exists. Tail of the output: *"7 of 7
checks agree. A tool that reproduces a hand proof is usable; one that does not
is."* — each of the six line items (index, totally real, class number, class group,
fundamental units, narrow class number) is individually confirmed `[OK]` in the
output with both the hand-proof value and the PARI value printed side by side and
matching exactly what the memo quotes. **Agrees exactly** with the memo's table in
§2. **No seal** (memo states "this records a capability, a validation, and a
measured constraint"); sha256 check N/A.

## 4. ON MAIN ALREADY?
- Claim 1/2 (PARI installed and validated): **(c) NOT on main** as a repository
  capability — `docs/TOOLBOX_LIVE.md` and `docs/PRACTICES.md` contain no PARI/GP
  reference (checked directly; the only string hits were false positives inside the
  word "comparison"). This is expected: memo 219 records a *capability* discovered
  and validated in the outside-bench sandbox, not (yet) adopted as a standing tool
  in the main toolbox docs.
- Claim 4 (egress wall measured): **(c) NOT independently mirrored on main** —
  this is an environment/operational fact about the outside-bench sandbox, not a
  repository claim; nothing on main asserts or contradicts it.
- Claim 8 (memo 220 closes L72's rank-3 residual via RSW): **(c) NOT checked
  against `docs/OPEN_LEADS.md`'s L72 row** by this reader (memo 220 is outside my
  assignment); worth a follow-up read since L72's row (per memo 207, my other
  assignment) was already found to be behind on other grounds.
- Claim 9 (memo 222: E is split over K, via KMRT Prop 43.6): **(c) NOT on main.**
  `frontier/B1077_intrinsic_split/FINDINGS.md` and `frontier/B882_magic_square_naming/`
  make no mention of "split" resolution of E over K via KMRT 43.6; the splitting
  result lives only in `outside_bench/THE_OWNER_REGISTER.md` (R130-2). This
  compounds with memo 203's finding (also mine): B882's arc_verdict.json on main
  still says PROVED while the outside-bench chain (204→222) treats it as refuted
  and its residual questions (E split?) as answered — none of this has been
  written back into `frontier/B882_magic_square_naming/` or `B1077_intrinsic_split/`.

## 5. NEEDS COMPUTATION HERE
- Claim 2: re-run PARI/GP on `K=ℚ[x]/(x³−12x−5)` (`bnfinit` without the `,1`
  flag, `nfdisc`, `bnfcertify`-free class group, `bnfunits`) and confirm the same
  6237/index-1/[3,0]/h=1/units/narrow-h=1 outputs — cheap (<1s per the memo), a
  clean reproduction check.
- Claim 9 (E split over K): re-run the finite local computation — for each rational
  prime p dividing `disc(K(√77))` (memo says only 3, 7, 11 ramify) and the
  unramified S₃-Frobenius classes, confirm `n_p ≤ 1` for every p and that
  corestriction forces the total count even, hence 0, hence split. This is the one
  claim in this memo's addenda chain most worth an independent re-derivation since
  it retires a computation ("48×48 commutant") that was twice killed by resource
  limits under sympy — confirming the cheaper KMRT-Prop-43.6 route independently
  would let main safely drop the commutant as a to-do.

## 6. SUPERSESSION
Self-superseding by design, twice, same day: **ADDENDUM 1 supersedes §6**
(residual closed via memo 220), **ADDENDUM 2 supersedes §7** (commutant no longer
needed, via memo 222). Both addenda are positive resolutions, not retractions of
the memo's headline (PARI's arrival/validation stands throughout). No later
INDEX.md row (220 onward) retracts the PARI installation/validation itself.

## 7. GRADE PROPOSAL
**REGISTER** for the PARI capability/validation itself (documentary: a tool now
exists and is proven trustworthy against a hand proof — worth a row, not an arc,
unless/until PARI is adopted into `docs/TOOLBOX_LIVE.md`). Flagging as an
associated **not-yet-on-main** item: the two positive results this memo's addenda
chain leads to (memo 220's L72 closure, memo 222's E-split-over-K result feeding
B882/B1077) have not been written back into any frontier arc file on main — same
register-lag pattern documented by memo 207 and found again independently at memo
203; not calling this DISPUTED (main does not contradict it, it simply hasn't
caught up), but it is adjacent to the same standing defect.
