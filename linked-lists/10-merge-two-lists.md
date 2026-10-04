## Problem: Merge Two Sorted Lists (Easy)
**Link:** https://leetcode.com/problems/merge-two-sorted-lists/

### Approach
Used an iterative two-pointer strategy with a dummy head node. Compare the current nodes of both sorted lists, link the smaller node to the merged list, and advance the corresponding pointer. Once one list is exhausted, attach the remaining chain directly to the tail.

### Complexity
- **Time:** $O(N + M)$ — Where $N$ and $M$ are the lengths of the two input linked lists.
- **Space:** $O(1)$ — Reuses existing node memory in-place without creating new node objects.

### Notes
Using a dummy head node simplifies edge cases by eliminating conditional checks for setting the root node of the result list.