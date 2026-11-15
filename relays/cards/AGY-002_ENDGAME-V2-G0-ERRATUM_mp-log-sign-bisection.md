# Card Erratum `AGY-002_ENDGAME-V2-G0-ERRATUM` — Analytic Antiderivative Domain Absolute Value (`0 of 19`)

- **Parent Card:** `AGY-002_ENDGAME-V2-G0` (`b59b2458b`)
- **Unmodified Sealed Script:** `faead675a` (left untouched to preserve `seal-immutable` and `artifact-hashes`; exited with `ValueError` at `B0.1` prior to generating any output file).
- **Technical Fix Before Any Output Exists:** In `B0.1`'s closed-form `2`-loop gauge antiderivative, \(a_{\mathrm{mp}} = -7 / (16\pi^2) < 0\) makes \(u / (a_{\mathrm{mp}} + c_{\mathrm{mp}} u) < 0\), so \(\log(|u / (a_{\mathrm{mp}} + c_{\mathrm{mp}} u)|)\) with monotone bracketed bisection on \([3/5, 2]\) replaces unbracketed `mp.findroot` on `mp.log(...)`. All tolerances, equations, and `5` planted fault controls of `AGY-002_ENDGAME-V2-G0` remain identical. `0 of 19.`
