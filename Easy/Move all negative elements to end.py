Link : https://practice.geeksforgeeks.org/problems/move-all-negative-elements-to-end1813/1?page=1&curated[]=2&sortBy=submissions

Code :

# User function Template for python3
class Solution:
    def segregateElements(self, arr, n):
        positive = []
        negative = []
        for i in arr:
            if i >= 1:
                positive.append(i)
            else:
                negative.append(i)
                
        arr[::] = positive + negative


# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())
    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)
        T -= 1

if __name__ == "__main__":
    main()
# Driver Code Ends
