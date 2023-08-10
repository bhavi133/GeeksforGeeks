Link : https://practice.geeksforgeeks.org/problems/12-hour-clock-multiplication4709/1?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def mulClock(self, num1, num2):
        # num3 = num1 * num2
        # return num3 % 12
        
        return (num1 * num2) % 12


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        num1,num2=map(int,input().split())    
        ob = Solution()
        print(ob.mulClock(num1,num2))

# Driver Code Ends
