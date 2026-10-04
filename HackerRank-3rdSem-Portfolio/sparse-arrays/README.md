## Problem: Sparse Arrays
**Link:** https://www.hackerrank.com/challenges/sparse-arrays/problem

### Approach
Built a frequency hash map of the input string list using Python's `Counter`. For each query string, performed an $O(1)$ lookup in the hash map to retrieve frequency counts efficiently.

### Complexity
- **Time Complexity:** $O(N + Q)$ — $O(N)$ to populate the frequency map and $O(Q)$ for query lookups.
- **Space Complexity:** $O(N)$ — Stores unique string frequencies in memory.