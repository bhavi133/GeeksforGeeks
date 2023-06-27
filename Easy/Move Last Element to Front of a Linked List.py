Link : https://practice.geeksforgeeks.org/problems/move-last-element-to-front-of-a-linked-list/1

Code :

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

class Solution:
    def moveToFront(self, head : Optional['Node']) -> Optional['Node']:
        l = []
        n = head
        while n is not None:
            l.append(n.data)
            n = n.next
        x = l.pop()
        y = l.insert(0, x)
        for i in l:
            print(i, end=" ")


# Driver Code Starts

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

def printList(node):
    while (node != None):
        print(node.data,end=" ")
        node = node.next
    print()

def inputList():
    n=int(input())#lenght of link list
    data=[int(i) for i in input().strip().split()]#all data of linked list in a line
    head = Node(data[0])
    tail = head;
    for i in range(1,n):
        tail.next = Node(data[i]);
        tail = tail.next;
    return head;

if __name__=="__main__":
    t = int(input())
    for _ in range(t):     
        head = inputList()
        obj = Solution()
        res = obj.moveToFront(head)
        printList(res)
        
# Driver Code Ends
