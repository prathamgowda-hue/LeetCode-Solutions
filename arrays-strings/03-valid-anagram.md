## Problem: Valid Anagram (Easy)
**Link:** https://leetcode.com/problems/valid-anagram/

### Approach
Used a hash map to count character frequencies in string `s`, then decremented the counts while iterating through string `t`. Returns false if lengths differ or character frequencies mismatch.

### Complexity
- **Time:** O(N) — Single pass over both strings of length N.
- **Space:** O(1) — At most 26 unique lowercase English characters stored in the map.

### Notes
An early length equality check (`len(s) != len(t)`) optimizes execution for obvious non-anagrams.