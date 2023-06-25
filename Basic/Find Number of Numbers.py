Link : https://practice.geeksforgeeks.org/problems/find-number-of-numbers/1?page=4&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# Your task is to complete this function
# Function should return an integer

def num(arr, n, k):
    string = ""
    for i in arr:
        string = str(i) + string
    return string.count(str(k))


# Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        print(num(arr, n, k))

# Driver Code Ends
