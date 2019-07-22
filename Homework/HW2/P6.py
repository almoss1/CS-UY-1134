import Stacks

def eval_postfix_boolean_expression(boolean_exp_str):
    operators="<>|&<=>=!==="
    args_stack = Stacks.ArrayStack()
    exp = boolean_exp_str.split()
    for i in exp:
        arg2 = args_stack.pop()
        arg1 = args_stack.pop()
        if i == "<" and arg1 < arg2:
            return True
        elif i == ">" and arg1 > arg2:
            return True
        elif i == "<=" and arg1 <= arg2:
            return True
        elif i == ">=" and arg1 >= arg2:
            return True
        elif i == "!=" and arg1 != arg2:
            return True
        elif i == "==" and arg1 == arg2:
            return True
        else:
            return False
        

                
        


# print(eval_postfix_boolean_expression("1 2 <"))