from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i
    return []

# --- Local Test Cases ---
if __name__ == "__main__":
    # Test Case 1: Standard case
    nums1, target1 = [2, 7, 11, 15], 9
    print("Test 1 Result:", twoSum(nums1, target1))  # Expected output: [0, 1]

    # Test Case 2: Edge case (Duplicate values / negative numbers)
    nums2, target2 = [3, 3], 6
    print("Test 2 Result:", twoSum(nums2, target2))  # Expected output: [0, 1]