class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Phase1
        tortoise = hare = nums[0]           #starting from 0th index
        while True:                         #Running loop till tortoise and hare meet
            tortoise = nums[tortoise]       #tortoise moves 2x faster than hare
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        #phase2
        # Find the "entrance" to the cycle.
        tortoise = nums[0]                  #now hare is lost in cycle and tortoise will find it from start
        while tortoise != hare:             #wherever tortoise meets hare cycle is detected
            tortoise = nums[tortoise]    
            hare = nums[hare]
        
        return hare


#Complexity - Time: O(n) Space: O(1)

#another approach - bit manipulation
#for each number num in [1,n]
#it's represented as a bit in bitmap: 1 << num
#If it appears again, that bit is set (a & 1<< num) and num is returned
#else, it's appearing for the first time, set the bit (a |= 1 << num)


def findDuplicate(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            if a & 1 << num:
                return num
            else:
                a |= 1 << num

