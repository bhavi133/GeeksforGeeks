Link : https://practice.geeksforgeeks.org/problems/stack-designer/1?page=1&difficulty[]=-1&sprint=b177b14354b699a74784fb34752c6a69&sortBy=submissions

Code :

# User function Template for python3

def _push(arr):
    return arr

def _pop(stack):
    l = []
    for i in range(len(stack)):
        x = arr.pop()
        l.append(x)
    for i in l:
        print(i, end=" ")


# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr=[int(i) for i in input().split()]
        stack = _push(arr)
        _pop(stack)
        print()

# Driver Code Ends
