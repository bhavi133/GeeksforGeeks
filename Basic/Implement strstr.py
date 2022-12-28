Link : https://practice.geeksforgeeks.org/problems/implement-strstr/1?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

def strstr(s,x):
    if x in s:
        return s.index(x)
    else:
        return -1
    
        
        

# Driver Code Starts
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

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        s,p =input().strip().split()
        print(strstr(s,p))
# Driver Code Ends
