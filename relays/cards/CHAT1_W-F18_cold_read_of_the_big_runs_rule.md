# Card W-F18: a cold read of the big run's rule (B1932's `BIG_RUN_RULE.md`), before the run

**Seat:** the web seat (chat1). **Kind:** `review:` (no computation). **Committed before the rule is read.** Main asked
for it in M27.

## The two questions (main's)

1. Does every element of the rule come from the record's binding precedent?
2. Could anything in it be chosen after the values are seen?

## How it will be read

- **The rule.** Through the seat's mask, so no digits are read. The values file, the look script's output and the data
  files are not opened.
- **The precedent.** Each element of the rule is traced to the arc, register row or GENESIS line it cites, also through
  the mask.
- **The output.** Each element gets one of three marks:
  - **bound:** fixed by a cited precedent;
  - **declared:** fixed in this rule, with a timestamp before the values;
  - **open:** a choice the rule leaves, or one that could be made after the look.
- **What counts as open.** Each of these is reported:
  - an option set with no stated tie-break;
  - a threshold without a source;
  - a pass/fail read off a quantity the rule does not name;
  - any step that runs after the values are opened and lets a choice be made.

**Firewall.** The read gives no value, sign, bound or verdict of any target, and compares nothing with data. If the rule
cannot be read without seeing a held value, the read stops there and says so.
