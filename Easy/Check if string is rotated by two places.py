Link : https://practice.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places-1587115620/1?page=1&category[]=Strings&sortBy=submissions

Code :

# User function Template for python3
class Solution:
    def isRotated(self,str1,str2):
        return str1[2:] + str1[:2] == str2 or str1[-2:] + str1[:-2] == str2


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
        if(Solution().isRotated(s,p)):
            print(1)
        else:
            print(0)
# Driver Code Ends
