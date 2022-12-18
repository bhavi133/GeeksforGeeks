Link : https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1?page=1&difficulty[]=-2&difficulty[]=-1&sortBy=submissions

Code : 

#User function Template for python3

def rotate(arr, n):
    x = arr[-1]
    arr.insert(0, x)
    arr.pop()
    return arr

 
# Driver Code Starts
def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1

if __name__ == "__main__":
    main()
# Driver Code Ends
