Link : https://practice.geeksforgeeks.org/problems/data-type-1666706751/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=data-type

Code :

# User function Template for python3

class Solution:
    def dataTypeSize(self, str):
        if str == 'Character':
            return 1
        elif str == 'Integer' or str == 'Float':
            return 4
        elif str == 'Long' or str == 'Double':
            return 8
        

# Driver Code Starts.

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str = input()
        ob = Solution()
        res = ob.dataTypeSize(str)
        print(res)

# Driver Code Ends
