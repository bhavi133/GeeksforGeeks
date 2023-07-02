Link : https://practice.geeksforgeeks.org/problems/delete-middle-of-linked-list/1?page=1&status[]=unsolved&category[]=Linked%20List&sortBy=submissions

Code :

# User function Template for python3

def deleteMid(head):
    l = []
    n = head
    while n is not None:
        l.append(n.data)
        n = n.next
    middle = len(l) // 2
    del l[middle]
    for i in l:
        print(i, end=" ")


# Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):
        n=int(input())
        arr1 = [int(x) for x in input().split()]
        ll = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll.insert(nodeData, tail)
        res=deleteMid(ll.head)
        printList(res)

# Driver Code Ends
