Link : https://practice.geeksforgeeks.org/problems/implement-atoi/1?page=1&status[]=bookmarked&sortBy=submissions

Code :

# User function template for Python

class Solution:
    def atoi(self,string):
        if string[0] == '-':
            if string[1:].isdigit():
                return int(string)
            else:
                return -1
        else:
            if string.isdigit():
                return int(string)
            else:
                return -1
                

# Driver Code Starts
# Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# Driver Code Ends
