Link : https://practice.geeksforgeeks.org/problems/queue-designer/1?page=3&sprint=b177b14354b699a74784fb34752c6a69&sortBy=submissions

Code :

# User function Template for python3

def push(arr,n): 
    queue = []
    for i in arr:
        queue.append(i)
    return queue
    
    
def _pop(q):
    for i in range(len(q)):
        print(q.pop(0), end=" ")
    

# Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys
from collections import deque


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arr = list(map(int,input().strip().split()))
        q=deque()
        q=push(arr,n)
        _pop(q)
        print()

# Driver Code Ends
