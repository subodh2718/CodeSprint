# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Description:
# Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def two_sum(nums, target):
    """
    This function finds two numbers in the list `nums` that add up to the given `target`.

    Args:
    nums (list): A list of integers.
    target (int): The target sum to find in the list.

    Returns:
    list: A list containing the indices of the two numbers that add up to the `target`.
    """
    # Dictionary to store the difference and its index
    index_map = {}

    # Iterate through the list of numbers
    for i, num in enumerate(nums):
        # Calculate the difference needed to reach the target
        difference = target - num

        # Check if the difference is already in the map
        if difference in index_map:
            # Return the indices of the numbers that add up to the target
            return [index_map[difference], i]

        # If not found, store the index of the current number in the map
        index_map[num] = i

    # If no solution is found, return an empty list (this should not happen per problem constraints)
    return []

# Example usage
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Indices of numbers that add up to {target} are: {result}")
