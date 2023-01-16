Link : https://practice.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1?page=3&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions

Code :

class node:
    def __init__(self):
        self.data = None
        self.next = None

def delNode(head, k):
    l = []
    if head is None:
        return 
    else:
        n = head
        while n is not None:
            l.append(n.data)
            n = n.next

    popped_items = l.pop(k-1)
    for i in l:
        print(i, end=" ")
        

# Driver Code Starts
# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

def printlist(head):
    temp = head
    while(temp):
        print(temp.data, end=" ")
        temp = temp.next
    print('')

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        k = int(input())
        newhead = delNode(list1.head, k)
        printlist(newhead)
# Driver Code Ends
