# linkedlist.py


class ListNode:
  def __init__(self, data): 
    # store data
    self.data = data
    # store the reference (next item)
    self.next = None
    return


# 在建立一個節點時，需要傳入一個data的值，並且指標預設是指向None的。
# 這樣就會建立一個帶有15的資料的節點了，
node1 = ListNode(15)
print(node1.data)
print(node1.next)


# Single Linked-list
# 在建立list的一開始，我們預設裡面是沒有節點的。而linked-list本身帶有head跟tail兩個屬性。當我們加入一個新的節點時：
# 1. 若list本身還沒有任何節點，則head以及tail都會變成新的結點
# 2. 若list已經包含有其他節點，則新加入的節點變成新的tail（本來的tail指向新的節點）。

class SingleLinkedList:
	def __init__(self): 
		self.head = None
		self.tail = None
		return

	def traversal(self):
		node = self.head

		if node is not None:
			print(node.data)
			node = node.next
			
	def add_list_item(self, item):
		# make sure item is a proper node  
		if not isinstance(item, ListNode):
			item = ListNode(item)

		if self.head is None:
			self.head = item
		else:
			self.tail.next = item

		self.tail = item
		return

list1 = SingleLinkedList()
list1.add_list_item(node1)
list1.add_list_item(12)






# class LinkNode:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None

# class Single_Linklist:
# 	def __init__(self):
# 		self.head = None

# 	def traversal(self):
# 		node = self.head
# 		while node is not None:
# 			print(node.data)
# 			node = node.next