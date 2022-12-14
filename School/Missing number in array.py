Link : https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&status[]=solved&sortBy=submissions
    
Code :

class Solution:
    def MissingNumber(self,array,n):
        new_array = [i for i in range(1, n+1)]
        return sum(new_array) - sum(array)
   
# Driver Code Starts
t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# Driver Code Ends
