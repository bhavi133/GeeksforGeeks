Link : https://practice.geeksforgeeks.org/problems/get-minimum-element-from-stack/1?page=1&difficulty[]=1&status[]=solved&sortBy=submissions

Code :

#User function Template for python3

class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        return self.s.append(x)

    def pop(self):
        if len(self.s) == 0:
            return -1
        else:
            return self.s.pop()
        
    def getMin(self):
        if len(self.s) == 0:
            return -1
        else:
            return min(self.s)


# Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        q = int(input())

        arr = [int(x) for x in input().split()]

        stk=stack()  

        qi = 0
        qn=1
        while qn <= q:
            qt = arr[qi]

            if qt == 1:
                stk.push(arr[qi+1])
                qi+=2
            elif qt==2:
                print(stk.pop(),end=' ')
                qi+=1
            else:
                print(stk.getMin(),end=' ')
                qi+=1
            qn+=1
        print()

# Driver Code Ends
