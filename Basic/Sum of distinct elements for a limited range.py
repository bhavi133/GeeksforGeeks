Link : https://practice.geeksforgeeks.org/problems/sum-of-distinct-elements-15115/1

Code :

class Solution:
    def sumOfDistinct(self, arr, n):
        sum = 0
		for i in set(arr):
		    sum += i
		return sum


# Driver Code Starts

if __name__ == '__main__':     
    t = int(input())
    for _ in range(0,t):
        n = int(input())
        a = list(map(int,input().split()))
        ob = Solution()
        ans = ob.sumOfDistinct(a,n)
        print(ans)
            
# Driver Code Ends
