class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        p=intervals[0]
        ans=[]
        for i in range(1,len(intervals)):
            a=intervals[i]
            if (p[0]<=a[1]<=p[1]) or (a[0]<=p[1]<=a[1]):
                p[1]=max(a[1],p[1])
            else:
                #print(p)
                ans.append(p)
                p=a
        ans.append(p)
        return(ans)


# Steps:
# 1. sort intervals and then store 1st interval in p
# 2. check if adjacent interval lies in p
# 3. if yes then merge interval
# 4. else store p in ans and update p
# 5. Do this with all interval and then store last interval and return ans

# contributed by - @codeash14