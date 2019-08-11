#a)

#b)
import ArrayStack1017

def eval_postfix_exp(exp_str):
    operators = "+-*/"
    args_stack = ArrayStack1017.ArrayStack()
    exp_tokens = exp_str.split()
    for tokens in exp_tokens:
        if (tokens not in operators): #token is a number
            args_stack.push(int(tokens))
        else:
            arg2 = args_stack.pop()
            arg1 = args_stack.pop()
            if tokens == "+":
                res = arg1 + arg2
            elif tokens == "-":
                res = arg1 - arg2
            elif tokens == "*":
                res = arg1 * arg2
            else:  #token is "/"
                if arg2 == 0:
                    raise ZeroDivisionError
                res = arg1 / arg2
            
            args_stack.push(res)
    return args_stack.pop()


#c)
def create_expression_tree(prefix_exp_str):
    lst = prefix_exp_str.split(' ')
    root, pos = create_expression_tree_helper(lst, 0)
    a = LinkedBinaryTree(root)
    return a

def create_expression_tree_helper(prefix_exp, pos):
    Data = prefix_exp[pos]
    pos += 1
    if(prefix_exp[pos] in "+-*/"):
        Left = create_expression_tree_helper(prefix_exp, pos);
        left_Child = Left[0]
        pos = Left[1]
    else :
        left_Child = LinkedBinaryTree.Node(int(prefix_exp[pos]));
        pos += 1

    if(prefix_exp[pos] in "+-*/"):
        Right = create_expression_tree_helper(prefix_exp, pos);
        right_Child = Right[0]
        pos = Right[1]
    else :
        right_Child = LinkedBinaryTree.Node(int(prefix_exp[pos]));
        pos += 1

    return (LinkedBinaryTree.Node(Data, left_Child, right_Child), pos);
