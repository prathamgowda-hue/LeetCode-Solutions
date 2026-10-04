## Problem: Time Conversion
**Link:** https://www.hackerrank.com/challenges/time-conversion/problem

### Approach
Parsed the 12-hour AM/PM string into hour components and period flags. Handled edge cases: midnight (`12:00:00AM` -> `00:00:00`) and noon (`12:00:00PM` -> `12:00:00`). For other PM times, added 12 to the hour value and formatted with leading zeros.

### Complexity
- **Time Complexity:** $O(1)$ — String operations run on fixed-length input strings.
- **Space Complexity:** $O(1)$ — Uses constant space for string formatting.