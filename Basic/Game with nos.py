Link : https://practice.geeksforgeeks.org/problems/game-with-nos3123/1?page=2&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

def game_with_number (arr,  n) : 
    l = [arr[i] ^ arr[i+1] for i in range(n-1)]
    l.append(arr[-1])
    return l 


# Driver Code Starts
# Initial Template for Python 3

for _ in range(0,int(input())):    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = game_with_number(arr, n);
    print(*res)

# Driver Code Ends
