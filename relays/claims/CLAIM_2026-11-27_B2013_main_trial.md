# CLAIM CARD — B2013, Review 87 entered: three cold readers caught seven of the eight sealed plants and found real faults in all ten arcs read; main checked each finding and mended or answered it

- card id: new
- seat code: fam1-v1-unset-01
- seat, branch, commit: fam1-v1-unset-01, main, 13977a25feb6d94d74c9ea9b72c6a9492b85eec1
- kind: computation
- touches: none
- effect: none
- scope: frame: the record's window f4a0ab61f to 36f9cc5c2; object: ten arcs read by three readers with eight plants; reach: single; hypotheses: the readers' reports as main summarised them, and the lock reads the mended text of seven arcs
- identifications: none
- definitions: a plant is a fault placed on purpose in a reader's copy of the record, its list sealed by hash before any reader starts; a mend is a change to an arc's text after a reader's finding, marked with a dated bracket; the lock is the arc's test, which reads the committed plant list and the mended text
- imports: none
- premises on main: B1980, B1983, B1993, B1995, B1996, B2009, B2012 (the mends its lock reads)
- decisive script: relays/claims/main_trial/decisive.py, SHA-256 0f8f89e012cf7dfb, depends on the standard library, run as python3 relays/claims/main_trial/decisive.py B2013, output SHA-256 7271817474bcc98c
- decisive lines: 2 lines marked "DECISIVE:", SHA-256 7271817474bcc98c
- failing control: python3 relays/claims/main_trial/B2013_control.py
- second computation: none
- already on main?: the arc itself, B2013, landed at 8c22f0a6a; this card is filed after the arc's run (post hoc to it)
- what would make it fail: the committed plant list not the sealed one, or a mend the lock reads undone
