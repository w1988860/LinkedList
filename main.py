""" Python script to create a singly linked list for the following operations
   - Insert a Node at Beginning, at Ending and at a given Position
   - Delete a Node at Beginning, at Ending and at a given Position
   - Search, Count the Number of Nodes and Display """

# Write your code from here

#Version_01
#Use any visualization tool to understand the flow of execution

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

##first_element = Node(5)
##print("Data in the node is : ", first_element.data)

class Linked_List:
    def __init__(self):
        self.head = None


my_linked_list = Linked_List()
##my_linked_list.head = first_element

##second_element = Node(9)
##my_linked_list.head.next = second_element
##
####
####print(my_linked_list.head.data)
####
##### Insert element at the beginning
##
##element_1 = input("Enter a number to be inserted at the beginning: ")
##new_node = Node(element_1)
##my_linked_list.head = new_node
##new_node.next = first_element
####
##### Insert element at the end
##
##element_2 = input("Enter a number to be inserted at the end: ")
##new_node = Node(element_2)
##temporary_node = my_linked_list.head
##while temporary_node.next != None:
##    temporary_node = temporary_node.next
##temporary_node.next = new_node    
##    
##### Insert element at a particular location
##location = int(input("Enter the position or location U want to insert a new node: "))
### case where the location value is greater than the size of the linked list is not considered here
##element_3 = input("Enter a number to be inserted at a particular location: ")
##new_node = Node(element_3)
##temporary_node = my_linked_list.head
##
##for i in range(location-1):
##    temporary_node = temporary_node.next
##
##new_node.next = temporary_node.next
##temporary_node.next = new_node
    

def linkedlist_traversal(head_node):
    count = 0
    temporary_node = head_node
    while temporary_node != None:
        print(temporary_node.data)
        temporary_node = temporary_node.next
        count += 1
    print("Number of elements in the linked list is : ", count)
    

def linkedlist_search(head_node, element):
    temporary_node = head_node
    flag = False
    while temporary_node != None:
        if temporary_node.data == element:
            flag = True
            print("Element found")
            break
        temporary_node = temporary_node.next
    if flag == False:
        print("Element not found")
            

#Version_02

# Create a linked list with 10 nodes for demo purpose
node_elements = [5,4,3,2,1,6,7,8,9,0]

for i in range(10):
    new_node = Node(node_elements[i])
    if my_linked_list.head==None:  # Inserting first element
        my_linked_list.head = new_node
    else:
        temporary_node = my_linked_list.head
        while temporary_node.next != None:
            temporary_node = temporary_node.next
        temporary_node.next = new_node

linkedlist_traversal(my_linked_list.head)

## Search for an element in the linked list
element = int(input("Enter the number to be searched: "))

linkedlist_search(my_linked_list.head, element)
        

# Delete an element at the beginning
my_linked_list.head = my_linked_list.head.next
linkedlist_traversal(my_linked_list.head)

# Delete an element at the end
temporary_node = my_linked_list.head
while temporary_node.next.next != None:
    temporary_node = temporary_node.next
temporary_node.next = None    
linkedlist_traversal(my_linked_list.head)

# Delete an element at a particular location
position = int(input("Enter at what position U want the element to be deleted: "))
temporary_node = my_linked_list.head

for i in range(position-2):
    temporary_node = temporary_node.next
temporary_node.next = temporary_node.next.next
linkedlist_traversal(my_linked_list.head)
