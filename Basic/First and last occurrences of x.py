Link : https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=first-and-last-occurrences-of-x

Code :

# User function Template for python3

def find(arr,n,x):
    l = []
    for i in range(n):
        if arr[i] == x:
            l.append(i)
    
    if len(l) >= 1:
        return min(l), max(l)
    else:
        return [-1, -1]

 
# Driver Code Starts

t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)

# Driver Code Ends
