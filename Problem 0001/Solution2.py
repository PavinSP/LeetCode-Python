class Solution2:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i + j == target:
                    return [i, j]
        return []

def main():
    solution = Solution2()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")

if __name__ == "__main__":
    main()