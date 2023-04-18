Link : https://practice.geeksforgeeks.org/problems/reorganize-the-array4810/1

Code :

# User function Template for python3

def Rearrange (arr,  n) : 
    l = set(arr)
    arr.clear()
    for i in range(0, n):
        if i in l:
            arr.append(i)
        else:
            arr.append(-1)
    return arr


# Driver Code Starts
# Initial Template for Python 3

for _ in range(0,int(input())):  
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = Rearrange(arr, n);
    print(*res)

# Driver Code Ends
