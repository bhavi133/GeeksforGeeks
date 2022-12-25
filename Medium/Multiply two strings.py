Link : https://practice.geeksforgeeks.org/problems/multiply-two-strings/1?page=1&difficulty[]=1&status[]=solved&sortBy=submissions

Code :

#User function Template for python3

class Solution:
    def multiplyStrings(self,s1,s2):
        # code here
        # return the product string
        return int(int(s1)*int(s2))


# Driver Code Starts
# Initial Template for Python 3
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        a,b=input().split()
        print(Solution().multiplyStrings( a.strip() , b.strip() ))
# Driver Code Ends
