Link : https://practice.geeksforgeeks.org/problems/print-the-pattern-set-1/1?page=1&difficulty[]=-2&status[]=solved&sortBy=submissions

Code :

def printPat(n):
    string = ""
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            string += i * (str(j) + " ")
        string += "$"
    print(string)


# Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n= int(input())
        printPat(n)
# Driver Code Ends
