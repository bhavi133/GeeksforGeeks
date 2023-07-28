Link : https://practice.geeksforgeeks.org/problems/ceil-the-floor2802/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

def getFloorAndCeil(arr, n, x):
    floor = [i for i in arr if x <= i]
    ceil = [i for i in arr if x >= i]
    if len(ceil) != 0 and len(floor) == 0:
        return (max(ceil), -1)
    elif len(ceil) == 0 and len(floor) != 0:
        return (-1, min(floor))
    elif len(ceil) != 0 and len(floor) != 0:
        return (max(ceil), min(floor))
    elif len(ceil) == 0 and len(floor) == 0:
        return (-1, -1)


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ans = getFloorAndCeil(arr, n, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# Driver Code Ends
