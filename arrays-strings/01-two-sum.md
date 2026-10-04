## Problem: Two Sum (Easy)
**Link:** https://leetcode.com/problems/two-sum/

### Approach
We use a hash map (dictionary) to store numbers and their indices as we iterate through the array. For each number, we check if its complement (target minus the current number) is already in our hash map, allowing us to find the solution efficiently in a single pass.

### Complexity
- **Time:** O(n) - We traverse the list containing n elements only once using a single loop.
- **Space:** O(n) - The hash map stores up to n elements in the worst-case scenario.

### Notes
Using a hash map avoids the need for nested loops, reducing the time complexity from quadratic to linear. We must ensure we don't use the same element twice.
