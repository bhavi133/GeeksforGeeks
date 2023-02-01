Link : https://practice.geeksforgeeks.org/problems/check-if-a-string-is-isogram-or-not-1587115620/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def isIsogram(self,s):
        l = []
        for i in s:
            if s.count(i) > 1 and i not in l:
                l.append(i)
                
        return len(l) == 0

   
# Driver Code Starts
# Initial Template for Python 3

def main():
    T=int(input())    
    while(T>0):
        s=input()
        obj = Solution()
        if obj.isIsogram(s) is True:
            print(1)
        else:
            print(0)
        T-=1

if __name__=="__main__":
    main()
# Driver Code Ends
