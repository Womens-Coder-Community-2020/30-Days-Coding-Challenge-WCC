# Kadane's Algorithm to find max subarray sum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        msum=max(nums)
        s=0
        for i in nums:
            s+=i
            if s>msum:
                msum=s
            else:
                if s<0:
                    s=0
        return msum
            