Link : https://practice.geeksforgeeks.org/problems/professor-and-parties2000/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def PartyType(self, a, n):
        if len(set(a)) == n:
            return "GIRLS"
        return "BOYS"


# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())
    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.PartyType(a, n))
        T -= 1

if __name__ == "__main__":
    main()

# Driver Code Ends
