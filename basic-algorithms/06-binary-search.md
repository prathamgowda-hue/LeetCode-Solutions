## Problem: Binary Search (Easy)
**Link:** https://leetcode.com/problems/binary-search/

### Approach
Used logarithmic search on a sorted array by comparing target to the middle element and halving the search space in each iteration.

### Complexity
- **Time:** O(log N) — Search range divides by 2 in every step.
- **Space:** O(1) — Iterative pointer-based search requiring constant space.

### Notes
Calculated `mid` as `left + (right - left) // 2` to avoid overflow in systems with fixed integer limits.