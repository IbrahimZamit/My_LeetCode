class Solution:
    def isPalindrome(self, x: int) -> bool:

        # if x < 0: return False

        # div = 1
        # while x >= 10*div:
        #     div *= 10

        # while x:
        #     if x // div != x % 10: return False
        #     x = (x % 10) // 10
        #     div = div / 100
        # return True

        original_numb = x
        reverse_numb = 0
        if x < 0: return False
        if x == 0 : return True
        if x % 10 == 0: return False
        else:
            while x:
                reverse_numb = reverse_numb * 10 + x % 10
                x = x // 10
            return reverse_numb == original_numb

if __name__ =="__main__":

    sol = Solution()
    print(sol.isPalindrome(30))