Link : ttps://practice.geeksforgeeks.org/problems/generate-binary-numbers-1587115620/1?page=3&difficulty[]=-1&status[]=unsolved&status[]=bookmarked&sortBy=submissions

Code :

def generate(N):
    l = []
    for i in range(1, N+1):
        l.append(bin(i)[2:])
    return l


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
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        res = generate(n)
        for i in range (len (res)):
            print (res[i], end=" ")
        print()
