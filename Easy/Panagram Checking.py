Link : https://practice.geeksforgeeks.org/problems/pangram-checking-1587115620/1

Code :

# User function Template for python3

class Solution:
    def checkPangram(self,s):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        s = list(s.lower())
        l = list('!@#$%^&*()-,./?><~`')
        for i in s:
            if i in l:
                s.remove(i)
        s = "".join(sorted(list(set(s))))
        s = s.replace(' ', '')
        return letters == s
        

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
        obj = Solution()
        if(obj.checkPangram(s)):
            print(1)
        else:
            print(0)

# Driver Code Ends
