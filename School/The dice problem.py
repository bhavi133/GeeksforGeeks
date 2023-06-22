Link : https://practice.geeksforgeeks.org/problems/the-dice-problem2316/1?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def oppositeFaceOfDice(self, N):
        # if N == 1:
        #     return 6
        # elif N == 2:
        # 	return 5
        # elif N == 3:
        # 	return 4
        # elif N == 4:
        # 	return 3
        # elif N == 5:
        #     return 2
        # else:
        #     return 1

        return 7 - N


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.oppositeFaceOfDice(N)
        print(ans)

# Driver Code Ends
