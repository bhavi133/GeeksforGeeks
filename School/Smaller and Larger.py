Link : https://practice.geeksforgeeks.org/problems/smaller-and-larger4005/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
  
	def getMoreAndLess(self,arr, n, x):
      smaller_count = []
      larger_count = []
      for i in arr:
          if i < x:
              smaller_count.append(i)
          elif i == x:
              smaller_count.append(i)
              larger_count.append(i)
          else:
              larger_count.append(i)
      return len(smaller_count), len(larger_count)

        
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMoreAndLess(arr, n, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# Driver Code Ends
