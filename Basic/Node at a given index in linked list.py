Link : https://practice.geeksforgeeks.org/problems/node-at-a-given-index-in-linked-list/1?page=1&difficulty[]=-2&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def getNth(head, k):
    l = []
    if head is None:
        return 
    else:
        n = head
        while n is not None:
            l.append(n.data)
            n = n.next
            
    for i in l:
        return l[k-1]
            

# Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

# Linked List class contains a Node object
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

if __name__ == '__main__':
    llist = LinkedList()
    T = int(input())
    while (T > 0):
        llist = LinkedList()
        n, k = list(map(int, input().split()))
        value = list(map(int, input().split()))
        for i in reversed(value):
            llist.push(int(i))
        m = getNth(llist.head, k)
        print(m)
        T -= 1
        
# Driver Code Ends
