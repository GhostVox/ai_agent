import ast
import operator as op

# Supported operators
operators = {
    ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
    ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
    ast.USub: op.neg
}

def eval_expr(expr):
    """
    Evaluates an arithmetic expression safely using ast.
    """
    node = ast.parse(expr, mode='eval').body
    return eval_(node)


def eval_(node):
    if isinstance(node, ast.Constant):
        return node.value
    elif isinstance(node, ast.BinOp):
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp):
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)

if __name__ == '__main__':
    expression = "3 + 7 * 2"
    try:
        result = eval_expr(expression)
        print(result)
    except Exception as e:
        print(f"Error: {e}")