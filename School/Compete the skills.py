Link : https://practice.geeksforgeeks.org/problems/compete-the-skills5807/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def scores(self, a, b, cc):
        for i, j in zip(a, b):
            if i > j:
                cc[0] += 1
            elif i < j:
                cc[1] += 1
            else:
                pass
        return cc
        
    	 
# Driver Code Starts
#Initial Template for Python 3

def main():
    T = int(input())
    while(T > 0):
    	a = [int(x) for x in input().strip().split()]
    	b = [int(x) for x in input().strip().split()]    	
    	cc = [0, 0]
    	ob=Solution()
    	ob.scores(a, b, cc)
    	print(*cc)
    	T -= 1

if __name__ == "__main__":
    main()

# Driver Code Ends
