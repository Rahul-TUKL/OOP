#*************************Singly Linked**************************************
class SingleyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)

Head = SingleyNode(1)
A = SingleyNode(3)
B = SingleyNode(4)
C = SingleyNode(5)
Head.next = A
A.next = B
B.next = C
curr =Head
while curr:
    curr =curr.next # becomes A and then B and then C and then None

def display(Head):
    curr = Head
    elements = []
    while curr:
        elements.append(str(curr))
        curr =curr.next
    print(" -> ".join(elements))

#display(Head)

def search(Head, target):
    curr =Head
    while curr:
        if int(str(curr))==target:
            return True
        curr = curr.next
    return False
#print(search(Head, 5))
#***************************************************Doubly Linked List***********************************       

class DoublyNode:
    def __init__(self, val, next=None, prev =None):
        self.val = val
        self.next = next
        self.prev = None
    def __str__(self):
        return str(self.val)
    
Head  = DoublyNode(1)
A = DoublyNode(3)
B = DoublyNode(5)
C = DoublyNode(7)
tail =C
Head.next = A
A.next =B
A.prev = Head
B.next = C
B.prev = A
C.prev = B

def display_forward(Head):
    curr =Head
    elements_n = []
    elements_p = []
    while curr:
        elements_n.append(str(curr.val))
        curr = curr.next
    return print(" <-> ".join(elements_n))

#display_forward(Head)

def display_backward(Head):
    curr =Head
    elements_p = []
    while curr and curr.next: # C does not have next
        curr = curr.next
    while curr:
        elements_p.append("None" if curr.prev is curr.val else str(curr))
        curr = curr.prev
    return print(" <-> ".join(elements_p))
#display_backward(Head)
#*************************************** Insert at Start***********************************************************
def insert_at_beginning (Head, tail, val):
    new_node = DoublyNode(val, next=Head)
    Head.prev = new_node
    return new_node, tail

Head, tail = insert_at_beginning(Head, tail,9)
display(Head)

def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node 
    new_node.prev = tail
    return head, new_node
head , tail = insert_at_end(Head, tail, 20)
display_forward(Head)



    