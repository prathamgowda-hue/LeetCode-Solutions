## Problem: Longest Common Prefix (Easy)
**Link:** https://leetcode.com/problems/longest-common-prefix/

### Approach
Initialized the prefix as the first string and iteratively trimmed it from the end until every subsequent string matched the starting prefix.

### Complexity
- **Time:** O(S) — Where S is the sum of all characters in all strings in worst-case scenarios.
- **Space:** O(1) — Uses constant extra space.

### Notes
Trimming the candidate string backwards is faster than column-by-column string comparison for small string arrays.