from LinkedList import Node
from Queue import Queue
from Stack import Stack

class TreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    def set_data(self, data):
        self.data = data
    def get_data(self):
        return self.data
    def set_left(self, left):
        self.left = left   
    def get_left(self):
        return self.left            
    def set_right(self, right):
        self.right = right
    def get_right(self):
        return self.right
        
class BinarySearchTree:
    def __init__(self, root = None):
        self.root = root
        self.size = 0
    
    def insert(self, data):
        newNode = TreeNode(data)
        pPre, pCur = None, self.root
        
        if self.root is None:
            self.root = newNode
            return
        while True:
            if pCur is None:
                pCur = newNode
                pPre.set_left(newNode) if data < pPre.get_data() else pPre.set_right(newNode)
                break
            elif data < pCur.get_data():
                pPre = pCur
                pCur = pCur.get_left()
            else:
                pPre = pCur
                pCur = pCur.get_right()
    
    def remove(self, key):
        self.root = self.deleteNode(self.root, key)
    def deleteNode(self, root, key): 
        '''
        Taken from https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
        '''
        # Base Case 
        if root is None: 
            return root  
        
        # If the key to be deleted is smaller than the root's 
        # key then it lies in  left subtree 
        if key < root.data: 
            root.left = deleteNode(root.left, key) 
  
            # If the kye to be delete is greater than the root's key 
            # then it lies in right subtree 
        elif(key > root.data):
            root.right = deleteNode(root.right, key) 
            
            # If key is same as root's key, then this is the node 
            # to be deleted 
        else:   
          
            # Node with only one child or no child 
            if root.left is None : 
                temp = root.right  
                root = None     
                return temp   
              
            elif root.right is None : 
                temp = root.left  
                root = None
                return temp 
  
            # Node with two children: Get the inorder successor 
            # (smallest in the right subtree) 
            temp = minValueNode(root.right) 
  
            # Copy the inorder successor's content to this node 
            root.key = temp.key 
  
            # Delete the inorder successor 
            root.right = deleteNode(root.right , temp.key) 
  
            return root  
        
    def search(self, key):
        rover = self.root
        value = None
        while True:
            if rover == None:
                break
            if rover.get_data() == key:
                value = rover.get_data()
                break
            elif key < rover.get_data():
                rover = rover.get_left() 
            else:
                rover = rover.get_right()
        return value
        
    def get_height(self, node):
        if node is None:
            return -1
        left_H = self.get_height(node.get_left())
        right_H = self.get_height(node.get_right())
        return 1 + max(left_H, right_H)
        
    def is_complete(self, node):
        # An empty tree is complete Binary Tree
        if node is None:
            return 1
    
        # This flag variable is set true
        # when a non full node is seen.
        flag = 0
        
        queue = Queue()
        queue.Push(Node(node))
        
        while queue.IsEmpty() is False:
            tempNode = queue.Pop()
            
            # Check if left child is present
            if tempNode.get_left() is not None:
                # If we have seen a non full node, and we see a node
                # with non-empty left child, then the given tree is not
                # a complete Binary Tree
                if flag is True:
                    return 0
                
                # Enqueue left child
                queue.Push(Node(tempNode.get_left()))
    
            # If this is a non-full node, set the flag true
            else:
                flag = 1
                
            # Check if right child is present
            if tempNode.get_right() is not None:
                # If we have seen a non full node, and we see a node
                # with non-empty right child, then the given tree is not
                # a complete Binary Tree.
                if flag is True:
                    return 0
                
                # Enqueue right child
                queue.Push(Node(tempNode.get_right()))
                
            # If this is a non-full node, set the flag true
            else:
                flag = 1
                
        # If we reach here, then the tree is complete Binary Tree
        return true
        
    def print_in_order(self):
        self.Print_in_order(self.root)
    def Print_in_order(self, ptr):
        if ptr is None:
            return
        self.Print_in_order(ptr.get_left())
        print(ptr.get_data())
        self.Print_in_order(ptr.get_right())
            
    def print_pre_order(self):
        self.Print_pre_order(self.root)
    def Print_pre_order(self, ptr):
        if ptr is None:
            return
        print(ptr.get_data())
        self.Print_pre_order(ptr.get_left())
        self.Print_pre_order(ptr.get_right())
            
    def print_post_order(self):
        self.Print_post_order(self.root)
    def Print_post_order(self, ptr):
        if ptr is None:
            return
        self.Print_post_order(ptr.get_left())
        self.Print_post_order(ptr.get_right())
        print(ptr.get_data())
            
            
    def print_level_order(self):
        if self.root is None:
            return
        stack = Stack()
        stack.Push(Node(self.root))
        level = 1
            
        while stack.IsEmpty() is False:
            temp = Stack()
                
            while stack.IsEmpty() is False:
                temp.Push(Node(stack.Pop()))
                    
                print("Level", str(level))
                level += 1
                    
            while temp.IsEmpty() is False:
                node = temp.Pop()
                print(node.get_data(), end = ' ')
                if node.get_left() is not None:
                    stack.Push(Node(node.get_left()))
                if node.get_right() is not None:
                    stack.Push(Node(node.get_right()))
            print('\n')
