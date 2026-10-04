## Problem: Valid Parentheses (Easy)
**Link:** https://leetcode.com/problems/valid-parentheses/

### Approach
Used a stack to keep track of opening brackets and popped the top bracket to verify compatibility whenever a closing bracket was encountered.

### Complexity
- **Time:** O(N) — Traverses the input string of length N once.
- **Space:** O(N) — Stack stores up to N elements in worst-case scenarios.

### Notes
Checking `not stack` at the end ensures no opening brackets are left unmatched.