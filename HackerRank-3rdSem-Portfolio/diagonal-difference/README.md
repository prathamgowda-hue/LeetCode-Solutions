## Problem: Diagonal Difference
**Link:** https://www.hackerrank.com/challenges/diagonal-difference/problem

### Approach
Traversed the $N \times N$ square matrix in a single pass ($O(N)$). For each row index `i`, aggregated the primary diagonal element `arr[i][i]` and the secondary diagonal element `arr[i][n - 1 - i]`. Calculated the absolute difference between the two sums using `abs()`.

### Complexity
- **Time Complexity:** $O(N)$ — Iterates through the matrix dimensions once.
- **Space Complexity:** $O(1)$ — Uses constant auxiliary space for sum tracking.