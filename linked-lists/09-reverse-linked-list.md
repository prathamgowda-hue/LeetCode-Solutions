## Problem: Reverse Linked List (Easy)
**Link:** https://leetcode.com/problems/reverse-linked-list/

### Approach
Used an iterative three-pointer technique (`prev`, `curr`, `nxt`) to reverse node pointers in a single pass through the singly linked list.

### Complexity
- **Time:** $O(N)$ — Iterates through every node in the linked list once.
- **Space:** $O(1)$ — Reverses links in-place using constant extra memory.

### Notes
Storing `curr.next` in a temporary variable (`nxt`) before reassigning pointers avoids breaking the forward chain during traversal.