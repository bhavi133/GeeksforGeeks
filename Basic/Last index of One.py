Link : https://practice.geeksforgeeks.org/problems/last-index-of-15847/1?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def lastIndex(self, s):
        # lst = [i for i in range(len(s)) if s[i] is '1']
        # if len(lst) != 0:
        #     return max(lst)
        # else:
        #     return -1
        
        lst = [i for i in range(len(s)) if s[i] is '1']
        return max(lst) if len(lst) else -1
                

# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())
    while(T > 0):
    	s = input()
    	ob = Solution()
    	print(ob.lastIndex(s))
    	T -= 1
      
if __name__ == "__main__":
    main()
    
# Driver Code Ends
