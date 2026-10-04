## Problem: Reverse String (Easy)
**Link:** https://leetcode.com/problems/reverse-string/

### Approach
Used a two-pointer approach starting at opposite ends of the array, swapping characters in-place while moving toward the center until the pointers meet.

### Complexity
- **Time:** O(N) — Each element is visited and swapped once.
- **Space:** O(1) — Array is modified in-place without extra memory allocation.

### Notes
Swapping in-place strictly respects the O(1) extra space constraint required by the problem.