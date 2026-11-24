# B1976: hashes fixed before the run (2026-11-24 22:06)

| file | sha256 |
|---|---|
| `frontier/B1976_the_level_as_a_lens_frame_c_at_order_30/CARD.md` | `59dfc2c46d98fbc7fb74c6c5dd45df0d4e6ae7fe4639a0a050fc8fbc827cc1ea` |
| `frontier/B1976_the_level_as_a_lens_frame_c_at_order_30/verification/level30.py` | `2be8a6cbdf6ab1a0b371f6ee7e5f78ee6722ac5fafc3b6697c37fbdb350da373` |

**Mended before any row printed (2026-11-24 22:07):** the first run stopped with a KeyError after E0 (the up sector's '1' channel was read as `r["one"]` for `r["up"]["one"]`, in two places). The card is unchanged; the mended script's sha256 is `71747915e1be9294a6eb1819f21daf8c76d44120bcf5b4a5113f56d4baba2938`. E0's printed lines came from the first run and are the same in the second.
