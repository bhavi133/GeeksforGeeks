Link : https://practice.geeksforgeeks.org/problems/linked-list-that-is-sorted-alternatingly/1

Code :

def sort(h1):    
    l = []
    n = h1
    while n is not None:
        l.append(n.data)
        n = n.next
    
    for i in sorted(l):
        print(i, end=" ")


# Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())   
    for tcs in range(t):
        n1=int(input())
        arr1=[int(x) for x in input().split()]
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
        resHead=sort(ll1.head)
        printList(resHead)
        print()
        
# Driver Code Ends
