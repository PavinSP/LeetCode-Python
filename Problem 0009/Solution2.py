# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        xcopy = x
        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10
        return reverse == xcopy

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