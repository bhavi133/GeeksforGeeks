Link : https://practice.geeksforgeeks.org/problems/product-of-array-element/1?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

def product(arr,n,mod):
    p = 1
    for i in arr:
        p *= i
    return p % mod


# Driver Code Starts
# Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    mod=1000000007
    for j in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        print(product(arr,n,mod))

# Driver Code Ends
