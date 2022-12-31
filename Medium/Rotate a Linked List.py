Link : https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1?page=1&status[]=bookmarked&sortBy=submissions

Code :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def rotate(self, head, k):
        l = []
        if head is None:
            pass
        else:
            n = head
            while n is not None:
                l.append(n.data)
                n = n.next
            l[k:], l[:k] = l[:k], l[k:]
            for i in l:
                print(i, end=" ")


# Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        k = int(input())
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
        head = Solution().rotate(lis.head,k)
        printList(head)
# Driver Code Ends
