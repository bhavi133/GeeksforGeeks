Link : https://practice.geeksforgeeks.org/problems/rearrange-an-array-such-that-arri-i3618/1

Code :

# User function Template for python3

class Solution:
    def modifyArray (self, arr,  n) :       
        l = set(arr)
        arr.clear()
        for i in range(0, n):
            if i in l:
                arr.append(i)
            else:
                arr.append(-1)
        return arr
                    
 
# Driver Code Starts
# Initial Template for Python 3

for _ in range(0,int(input())):  
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.modifyArray(arr, n);
    print(*res)

# Driver Code Ends
