## Problem: Dynamic Array
**Link:** https://www.hackerrank.com/challenges/dynamic-array/problem

### Approach
Initialized a 2D sequence array of size $N$ using nested lists. Processed each query dynamically using bitwise XOR (`x ^ lastAnswer`) modulo $N$ to find the target sub-array index. Query type 1 appends $y$, while Query type 2 updates `lastAnswer` and stores it in the result array.

### Complexity
- **Time Complexity:** $O(N + Q)$ — $O(N)$ array initialization + $O(1)$ per query operation.
- **Space Complexity:** $O(N + Q)$ — Stores elements across $N$ dynamic sub-arrays and buffers output.