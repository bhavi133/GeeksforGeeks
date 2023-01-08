Link : https://practice.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1?page=6&difficulty[]=-1&difficulty[]=0&difficulty[]=1&status[]=unsolved&sortBy=submissions

Code :

#User function Template for python3
class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None
        
#Function to merge two sorted linked list.
def sortedMerge(head1, head2):
    l1 = []
    if head1 is None:
        return 
    else:
        n = head1
        while n is not None:
            l1.append(n.data)
            n = n.next
            
    l2 = []
    if head2 is None:
        return 
    else:
        n = head2
        while n is not None:
            l2.append(n.data)
            n = n.next
    
    l3 = l1 + l2
    for i in sorted(l3):
        print(i, end=" ")
    

# Driver Code Starts
# Initial Template for Python 3
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node
        
# prints the elements of linked list
def printList(n):
    while n is not None:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        n,m = map(int, input().strip().split())
        
        a = LinkedList() # create a new linked list 'a'.
        b = LinkedList() # create a new linked list 'b'.
        
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        
        for x in nodes_a:
            a.append(x)
        
        for x in nodes_b:
            b.append(x)
        
        printList(sortedMerge(a.head,b.head))

# Driver Code Ends
