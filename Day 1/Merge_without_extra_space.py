# Complexity- Time:O(m+n)log(m+n) Space:O(1)
class Solution:
    
    def merge(self,arr1,arr2,n,m):
        i,j,k=0,0,n-1
        while i<=k and j<m:
            if arr1[i]<arr2[j]:
                i+=1
            else:
                arr2[j],arr1[k]=arr1[k],arr2[j]
                j+=1
                k-=1
        arr1.sort()
        arr2.sort()
            
#Complexity- Time:O(m+n) Space:O(1)



# Initial Approach
# Complexity- Time:O(m*n) Space:O(1)

class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        #code here
        def picknput(arr2,m):
            a=arr2[0]
            i=1
            while i<m and arr2[i]<arr2[i-1]:
                arr2[i],arr2[i-1]=arr2[i-1],arr2[i]
                i+=1
            arr2[i-1]=a
                
        
        for j in range(n):
            if arr1[j]>arr2[0]:
                arr1[j],arr2[0]=arr2[0],arr1[j]
                picknput(arr2,m)
                #print(arr1,arr2)

# contributed by - @codeash14
