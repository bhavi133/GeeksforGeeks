Link : https://practice.geeksforgeeks.org/problems/repeated-ids0116/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=difficulty

Code :

def uniqueId( a, n):
    l = []
    for i in a:
        if a.count(i) >= 1 and i not in l:
            l.append(i)
    return l
    
    
# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())
    while(T > 0):
        n = int(input())
        a = [x for x in input().strip().split()]
        print(*uniqueId(a, n))
        T -= 1
        
if __name__ == "__main__":
    main()

# Driver Code Ends
