Link : https://practice.geeksforgeeks.org/problems/first-element-to-occur-k-times5150/1?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def firstElementKTime(self,  a, n, k):        
        dic = {}
        for i in a:
            dic[i] = 0
        for i in a:
            dic[i] += 1
            if dic[i] == k:
                return i
        return -1
                
    
# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())
    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstElementKTime(a, n, k))
        T -= 1

if __name__ == "__main__":
    main()

# Driver Code Ends
