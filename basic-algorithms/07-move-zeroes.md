## Problem: Move Zeroes (Easy)
**Link:** https://leetcode.com/problems/move-zeroes/

### Approach
Used a two-pointer technique: overwrote non-zero values sequentially from index 0 forward, then filled remaining trailing positions with zeroes.

### Complexity
- **Time:** O(N) — Single pass to copy non-zeroes and a second short loop to write trailing zeroes.
- **Space:** O(1) — Array is updated in-place without extra array allocations.

### Notes
Maintains relative order of all non-zero elements while placing zeroes at the end.