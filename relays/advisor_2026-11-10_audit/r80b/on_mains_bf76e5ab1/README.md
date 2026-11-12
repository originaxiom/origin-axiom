# R80b, parts 2 to 5 (its first two patches), built again on main's `bf76e5ab1`

Main's head moved twice after these parts were built: its M15 commit, and the landing of R80a with main's seven
mends. **Part 1 applies on `bf76e5ab1` as sent** (its script and its two patches), and all 53 gates pass there.
**Part 2 does not:** its fifth patch stops at a generated page that main's mends changed. So parts 2 to 5 are built
again here, patch for patch, on `bf76e5ab1` with part 1 applied. The folders `../part_2/` to `../part_5/` keep what
was sent, on main's `10fbbc1c2`.

To apply, on `bf76e5ab1` with part 1:

```
git am relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/part_2/00*.patch
git am relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/part_3/00*.patch
git am relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/part_4/00*.patch
git am relays/advisor_2026-11-10_audit/r80b/on_mains_bf76e5ab1/part_5/00*.patch
```

The tree after all of them is `f7aec7c596bc63be9ece69b4c77bf7dd2c3dcfa3`: tried on a clean checkout.

## What differs from what was sent

**38 patches. 34 make the same change as sent, outside the generated pages.** In those only the pages that main's
generators write are different, because they are made again on each patch's tree: 16 of the 38 carry one.

Four differ outside the generated pages, each because main changed a line beside the patch's own:

| | what differs |
|---|---|
| part 2, patch 6 | harvest row 1733 and register row P-822: the patch's note stands in the row as main has it now |
| part 2, patch 8 | harvest row 1733, the same |
| part 2, patch 12 | the register: main changed row P-834 at the landing; the two new rows, P-835 and P-836, stand after it as written |
| part 3, patch 18 | the two logs: the part's entry stands above main's entry of the landing in the changelog, and after it in the progress log |

In each row that main also changed, each note of these parts stands once: counted.

## What was run on it

| | |
|---|---|
| all 53 gates, with part 1 on `bf76e5ab1` | 53 pass |
| the same, after part 2 | 53 pass |
| the same, after the last patch | 52 pass; the one that does not is the count of landings |
| the 19 test files these parts change, after the last patch | 174 passed, 1 skipped (B1884's, which runs the arc's script on request) |
| all 53 gates on a clean checkout of each of the 41 patches | running when this was pushed; its result is added here |

## One patch here is known to copy a fault

**Part 3, patch 17** gives B1894's quotation checker the strict placing of B1892's. Main's third folder, § 2, row A5,
says that B1892's placing still has a false pass and is not to be copied before it is mended: a path that is not
at the commit and ends in the name of a page is matched to every page of that name. The patch was built before
that was written, and it has the same fault. It is mended with row A5, in both arcs, in the sixth part of this
series (the card's second addition). Until then: the placing it reports for B1894 is right for the 38 quotations
it was run on, each of which names a path that is at the commit or names none.
