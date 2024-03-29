Link : https://practice.geeksforgeeks.org/problems/find-all-pairs-whose-sum-is-x5808/0

Code :

# User function Template for python3

class Solution:
    def allPairs(self, A, B, N, M, X):
        # Your code goes here 
        l = []
        for i in range(N):
            for j in range(M):
                if A[i] + B[j] == X:
                    l.append((A[i], B[j]))
        return sorted(l)
    

# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())
    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        N, M, X = sz[0], sz[1], sz[2]
        A = [int(x) for x in input().strip().split()]
        B = [int(x) for x in input().strip().split()]
        ob=Solution()
        answer = ob.allPairs(A, B, N, M, X)
        sz = len(answer)
        
        if sz==0 :
        	print(-1)   
        else: 
        	for i in range(sz):
        		if i==sz-1:
        		    print(*answer[i])
        		else:
        		    print(*answer[i], end=', ')
        T -= 1

if __name__ == "__main__":
    main()
    
# Driver Code Ends
