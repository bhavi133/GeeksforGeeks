Link : https://practice.geeksforgeeks.org/problems/find-transition-point-1587115620/1?page=1&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions

Code :

def transitionPoint(arr, n):
    if 1 in arr:
        return arr.index(1)
    else:
        return -1
        
        
# Driver Code Starts
# Driver code

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))

# Driver Code Ends
