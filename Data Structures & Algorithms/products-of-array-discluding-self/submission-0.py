class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        front = 1
        for i in range(n):
            ans[i] *= front
            front *= nums[i]
        back = 1
        for i in range(n-1,-1,-1):
            ans[i] *= back
            back *= nums[i]
        return ans
        
            


            


        