Link : https://practice.geeksforgeeks.org/problems/queue-using-two-stacks/1?page=7&difficulty[]=-1&difficulty[]=0&difficulty[]=1&status[]=unsolved&sortBy=submissions

Code :

#User function Template for python3
#Function to push an element in queue by using 2 stacks.
def Push(x,stack1,stack2):
    stack1.append(x)
    return stack1
    
#Function to pop an element from queue by using 2 stacks.
def Pop(stack1,stack2):
    if len(stack1) == 0:
        return -1
    else:
        z = stack1.pop(0)
        return z

# Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        qry=int(input())
        qtyp_qry=list(map(int, input().strip().split()))       
        i=0
        stack1=[]
        stack2=[]
        while i <len(qtyp_qry):
            #print(i)
            if qtyp_qry[i]==1:
                Push(qtyp_qry[i+1],stack1,stack2)
                #print(i)
                i+=2
            else:
                print(Pop(stack1,stack2),end=' ')
                i+=1          
        print()
# Driver Code Ends
