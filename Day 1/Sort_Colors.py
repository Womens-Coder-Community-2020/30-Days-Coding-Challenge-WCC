# Sort an array of 0’s 1’s 2’s without using extra space or sorting algo 

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #r:red, w:white, b:blue
        
        r, w, b = 0, 0, len(nums)-1

        while w <= b:
            if nums[w] == 0:                            #swap with r-th index if 0 occurs at w-th index
                nums[r], nums[w] = nums[w], nums[r]
                w += 1
                r += 1
            elif nums[w] == 1:
                w += 1
            else:                                       #swap with b-th index if 2 occurs at w-th index
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1        



#naive approach in python

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        pos0=nums.count(0)
        pos1=nums.count(1)
        pos2=nums.count(2)
        nums.extend([0]*pos0)
        nums.extend([1]*pos1)
        nums.extend([2]*pos2)
        del nums[0:l]
        
