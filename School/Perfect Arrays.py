Link : https://practice.geeksforgeeks.org/problems/perfect-arrays4645/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def IsPerfect(self,arr,n):
        return arr == arr[::-1]


# Driver Code Starts
# Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    if(ob.IsPerfect(arr,n)):
        print("PERFECT")
    else:
        print("NOT PERFECT")
    
# Driver Code Ends
