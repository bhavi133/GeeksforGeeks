Link : https://practice.geeksforgeeks.org/problems/split-strings5211/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def splitString(ob, S): 
        alphabets = ""
        numbers = ""
        punctuations = ""
        l = []
        for i in S:
            if i.isalpha():
                alphabets += i
            elif i.isdigit():
                numbers += i
            else:
                punctuations += i
        l.append(alphabets)
        l.append(numbers)
        l.append(punctuations)
        return l    
        

# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        ob = Solution()
        ans = ob.splitString(S)
        for i in ans:
            if(i==""):
                print(-1)
            else:
                print(i)

# Driver Code Ends
