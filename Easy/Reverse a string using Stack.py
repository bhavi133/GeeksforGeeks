Link : https://practice.geeksforgeeks.org/problems/reverse-a-string-using-stack/1?page=4&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions

Code :

def reverse(S):
    stack = []
    for i in S:
        stack.append(i)
    
    string = ""
    while stack:
        string += stack.pop()
    return string
    


# Driver Code Starts.

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))

# Driver Code Ends
