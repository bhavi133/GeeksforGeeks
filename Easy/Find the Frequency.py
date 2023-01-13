Link : https://practice.geeksforgeeks.org/problems/find-the-frequency/1?page=3&curated[]=2&sortBy=submissions

Code :

# User function Template for python3
def findFrequency (arr, n, x):
    dic = {}
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
            
    for i, j in dic.items():
        if i == x:
            return j
    else:
        return 0


# Driver Code Starts
# Initial Template for Python 3
t = int (input ())
for tc in range (t):
    n = int (input ())
    arr = list (map (int, input ().split ()))
    x = int (input ())
    print (findFrequency (arr, n, x))
# Driver Code Ends
