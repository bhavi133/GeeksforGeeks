Link : https://practice.geeksforgeeks.org/problems/union-of-two-linked-list/1

Code :

# User function Template for python3

class Solution:
    def union(self, head1,head2):        
        l1 = []
        l2 = []
        n = head1
        while n is not None:
            l1.append(n.data)
            n = n.next
        m = head2
        while m is not None:
            l2.append(m.data)
            m = m.next
        
        l3 = sorted(list(set(l1+l2)))
        for i in l3:
            print(i, end=" ")


# Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    for _ in range(int(input())):   
        n1 = int(input())
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)
        
        n2 = int(input())
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        
        ob = Solution()
        printList(ob.union(ll1.head,ll2.head))
        print()

# Driver Code Ends
