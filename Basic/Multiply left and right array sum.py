Link : https://practice.geeksforgeeks.org/problems/multiply-left-and-right-array-sum1555/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

def multiply (arr, n) : 
    #Complete the function
    middle = len(arr) // 2
    l1 = arr[0:middle]
    l2 = arr[middle:]
    return sum(l1) * sum(l2)
    

# Driver Code Starts
# Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = multiply(arr, n)
    print(ans)
# Driver Code Ends
