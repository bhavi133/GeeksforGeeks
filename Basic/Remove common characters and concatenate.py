Link : https://practice.geeksforgeeks.org/problems/remove-common-characters-and-concatenate-1587115621/1?page=2&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def concatenatedString(self,s1,s2):
        l1 = [i for i in s1 if i not in s2]
        l2 = [i for i in s2 if i not in s1]
                
        if len(l1+l2) != 0:
            return "".join(l1 + l2)
        else:
            return -1
        
 
# Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        obj = Solution()
        print(obj.concatenatedString(s,p))

# Driver Code Ends
