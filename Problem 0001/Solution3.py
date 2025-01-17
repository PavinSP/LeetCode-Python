# Two pass hash table
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map and map[complement] != i:
                return [i, map[complement]]
        return []


def main():
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")

if __name__ == "__main__":
    main()