""" Python script to create a singly linked list for the following operations
   - Insert a Node at Beginning, at Ending and at a given Position
   - Delete a Node at Beginning, at Ending and at a given Position
   - Search, Count the Number of Nodes and Display """

# Write your code from here

# Created a Node class to insert a node in linkedlist
class Node :
    def __init__(self,data,next):
        self.data = data
        self.next = next

# Created a Linked List class        
class LinkedList :
    # A head function for linked lists
    def __init__(self):
        self.head = None


## INSERTION FUNCTIONS :

    # This is a function to insert data list and convert the list into linked-list
    def insert_list(self, data_list) :
      self.head = None
      for data in data_list :
        self.insert_at_end(data) 

    # This function is to insert a Node at the Begining
    def insert_at_begining(self, data):
        self.head = Node(data, self.head)

    # This function is to insert a Node at the Ending
    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data,self.head)
            return
        itr = self.head
        while itr.next :
            itr = itr.next
        itr.next = Node(data,None)

    # This function is to insert a node at a given index   
    def insert_at (self,index,data) :
      if index<0 or index >= self.length():
        raise Exception("Invalid index")
      if index == 0 :
        self.insert_at_begining(data)
        return
      count = 0 
      itr = self.head
      while itr :
        if count == index-1 :
          node = Node(data,itr.next) 
          itr.next = node
          break 
        itr = itr.next
        count += 1


## DELETTING FUNCTIONS :

    # This function is used to delete node at begining
    def remove_at_begining (self) :
        self.head = self.head.next
    
    # This function is used to delete node at end   
    def remove_at_end (self) :
        count = 0
        itr = self.head
        a = list.length()
        while itr :
            if count == a-2 :
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1       
      
    # This remove function is used to delete a node at a given index
    def remove_at (self, index):
        if index < 0 or index >= self.length():
            raise Exception("Invalid index")
            
        if index == 0:
            self.head = self.head.next
            return
        
        count =0
        itr = self.head
        while itr:
            if count == index-1 :
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1


## Length and Searching Functions

    # This funtion is to get the length of data in Linked List
    def length(self):
      count=0
      itr = self.head
      while itr :
        count += 1
        itr = itr.next
      return count
    
    # This function is to search the elements in LinkedList 
    def Search(self,data) :
      if self.head.data == data:
        print(data,"is in LinkedList")
        return
      itr = self.head
      while itr.next:
          if itr.next.data == data:
              print(data,"is in LinkedList")
              return
          itr = itr.next
      print(data,"is not found in LinkedList")


## Printing Funtion of linked lists

    # This print function is to print the linked list
    def print(self) :
        if self.head is None :
            print("Linked list is Empty")
            return 
        itr = self.head
        llstr = ''
        while itr :
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)


if __name__ == '__main__' :
    list = LinkedList()
## Inserting Nodes
    # Inserting a list of data to make LinkedList
    list.insert_list(["Banana","Mango","Grapes","Orange"])
    list.print()
    print() 
    # Inserting a Node at Begining of the LinkedList
    list.insert_at_begining("Begining")
    list.print()
    print()
    # Inserting a Node at end of the LinkedList
    list.insert_at_end("Ending")
    list.print()
    print()
    # Inserting a Node at the specified index of LinkedList
    list.insert_at(3, "insert_1")
    list.print()
    print()
## Deleting Node 
    # Deleting a Node at Begining of the LinkedList 
    list.remove_at_begining ()
    list.print()
    print()
    # Deleting a Node at end of the LinkedList
    list.remove_at_end()
    list.print()
    print()
    # Deleting a Node at the specified index of LinkedList
    list.remove_at(2)
    list.print()
    print()
## Searching in LinkedList and length of LinkedList
    # Printing Length of the LinkedList
    print("Now Length is",list.length())
    print()
    list.Search("Mango")
    print() 
    list.Search("Sadiq")