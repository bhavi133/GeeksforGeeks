Link : https://practice.geeksforgeeks.org/problems/replace-all-0-with-5-in-an-input-integer/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

class Solution:
    def convertFive(self,n):
        string = str(n)
        if '0' in string:
            return string.replace("0", '5')
        else:
            return string


# Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        print(Solution().convertFive(n))
# Driver Code Ends
