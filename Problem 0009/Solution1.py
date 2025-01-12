# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            return True
        return False

def main():
    solution = Solution()
    x1 = 121
    x2 = -121
    output1 = solution.isPalindrome(x1)
    output2 = solution.isPalindrome(x2)
    print(f"Input: x = {x1}, Output: {output1}")
    print(f"Input: x = {x2}, Output: {output2}")

if __name__ == "__main__":
    main()