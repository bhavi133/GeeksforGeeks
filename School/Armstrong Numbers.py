Link : https://practice.geeksforgeeks.org/problems/armstrong-numbers2727/1?page=1&difficulty[]=-2&sortBy=submissions

Code :

#User function Template for python3
class Solution:
    def armstrongNumber (ob, n):
        l1 = list(map(int, str(n)))
        l2 = list(map(lambda x:x**3, l1))
        if(sum(l2) == n):
            return 'Yes'
        else:
            return 'No'


# Driver Code Starts
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# Driver Code Ends
