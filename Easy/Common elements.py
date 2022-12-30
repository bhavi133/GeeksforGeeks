Link : https://practice.geeksforgeeks.org/problems/common-elements1132/1?page=1&difficulty[]=0&status[]=solved&sortBy=submissions

Code :

#User function Template for python3
class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        set1 = set(A)
        set2 = set(B)
        set3 = set(C)
        set4 = set1.intersection(set2)
        set5 = set3.intersection(set4)
        return sorted(list(set5))

# Driver Code Starts
#Initial Template for Python 3
t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    ob = Solution()
    res = ob.commonElements (A, B, C, n1, n2, n3)    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()
# Driver Code Ends
