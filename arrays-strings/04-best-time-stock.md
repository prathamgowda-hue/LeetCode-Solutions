## Problem: Best Time to Buy and Sell Stock (Easy)
**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

### Approach
Maintained a running minimum price while traversing the list once, updating the maximum profit whenever the difference between the current price and minimum price exceeded previous profits.

### Complexity
- **Time:** O(N) — Single iteration through the array.
- **Space:** O(1) — Only two primitive variables used to track minimum price and max profit.

### Notes
Avoided O(N^2) double loops by tracking state variables dynamically during traversal.