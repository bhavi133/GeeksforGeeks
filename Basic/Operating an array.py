Link : https://practice.geeksforgeeks.org/problems/operating-an-array/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

def searchEle(a, x):
    return x in a

def insertEle(a, y, yi):
    a.insert(y, yi)
    return a

def deleteEle(a, z):
    return True
    

# Driver Code Starts

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        x,y,yi,z = list(map(int, input().strip().split()))
        if(searchEle(a, x)):
            print('1', end=' ')
        else:
            print('0', end=' ')
        if(insertEle(a, y, yi)):
            print('1', end=' ')
        else:
            print('0', end=' ')
        if(deleteEle(a, z)):
            print('1', end=' ')
        else:
            print('0', end=' ')
        print()

# Driver Code Ends
