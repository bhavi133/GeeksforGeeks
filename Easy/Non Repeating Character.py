Link : https://practice.geeksforgeeks.org/problems/non-repeating-character-1587115620/1?page=2&difficulty[]=0&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

import collections

class Solution:
    def nonrepeatingCharacter(self,s):
        dic = collections.Counter(s)
        for i in s:
            if dic[i] == 1:
                return i
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
        obj = Solution()
        ans=obj.nonrepeatingCharacter(s)
        if(ans!='$'):
            print(ans)
        else:
            print(-1)
            
# Driver Code Ends
