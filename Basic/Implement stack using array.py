Link : https://practice.geeksforgeeks.org/problems/implement-stack-using-array/1?page=1&status[]=bookmarked&sortBy=submissions

Code :

#User function Template for python3

class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        self.arr.append(data)
        return self.arr
    
    #Function to remove an item from top of the stack.
    def pop(self):
        if len(self.arr) == 0:
            return -1
        else:
            popped_item = self.arr.pop()
            return popped_item
        
# Driver Code Starts
#Initial Template for Python 3
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyStack()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   
# Driver Code Ends
