Link : https://practice.geeksforgeeks.org/problems/at-least-two-greater-elements4625/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def findElements(self,a, n):
        # Your code goes here
        l = sorted(a)
        return l[:-2]


# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())
    while(T > 0):
    	n = int(input())
    	a = [int(x) for x in input().strip().split()]
    	ob=Solution()
    	print(*ob.findElements(a, n))
    	T -= 1

if __name__ == "__main__":
    main()

# Driver Code Ends
