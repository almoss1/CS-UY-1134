from ArrayStack import *
def iterative_inorder(bin_tree):
    current_node = bin_tree.root  
    stack = ArrayStack.ArrayStack() 
      
    while True: 
        if current_node is not None: 
            stack.append(current) 
          
            current_node = current_node.left  
        elif(stack): 
            current_node = stack.pop() 
            yield current_node.data
            current_node = current_node.right  
  
        else: 
            break