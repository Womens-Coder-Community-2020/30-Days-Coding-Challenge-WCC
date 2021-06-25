class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        a=sum(list(set(arr)))
        return([sum(arr)-a, (n*(n+1)//2)-a])

#Explaination :
'''
sum(arr): sum of given list of numbers
conver arr to set and then to list to remove repeating digit

a=sum(list(set(arr))): sum of given list after eleminating repeating digit

now,

Missing no.: sum of numbers from 1 to n - sum of given list after eleminating repeating digit(a)
Repeating no.: sum of given list - sum of given list after eleminating repeating digit(a)
'''

# contributed by - @codeash14