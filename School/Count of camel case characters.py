Link : https://practice.geeksforgeeks.org/problems/find-the-camel3348/1?page=1&difficulty[]=-2&status[]=unsolved&category[]=Strings&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def countCamelCase (self,s):
        count = 0
        for i in s:
            if ord(i) > 64 and ord(i) <= 90:
                count += 1
        return count


# Driver Code Starts
# Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print (ob.countCamelCase (s))

# Driver Code Ends
