import ast


def calculate(expr):
    allowed_operators = (
        ast.Add,
        ast.Sub,
        ast.Mult,
        ast.Div,
        ast.Pow,
        ast.UAdd,
        ast.USub,
    )

    class SafetyVisitor(ast.NodeVisitor):
        def visit_BinOp(self, node):
            if not isinstance(node.op, allowed_operators):
                raise ValueError(
                    "UTIL_ARGUMENT_ERROR (0x00000032): неправильный аргумент"
                )
            self.generic_visit(node)

        def visit_UnaryOp(self, node):
            if not isinstance(node.op, (ast.UAdd, ast.USub)):
                raise ValueError(
                    "UTIL_ARGUMENT_ERROR (0x00000032): неправильный аргумент"
                )
            self.generic_visit(node)

        def visit_Name(self, node):
            raise ValueError("UTIL_ARGUMENT_ERROR (0x00000032): неправильный аргумент")

        def visit_Call(self, node):
            raise ValueError("UTIL_ARGUMENT_ERROR (0x00000032): неправильный аргумент")

        def visit_List(self, node):
            raise ValueError("UTIL_ARGUMENT_ERROR (0x00000032): неправильный аргумент")

        def visit_Str(self, node):
            raise ValueError("UTIL_ARGUMENT_ERROR (0x00000032): неправильный аргумент")

    try:
        expr_ast = ast.parse(expr, mode="eval")
        SafetyVisitor().visit(expr_ast)
        return eval(compile(expr_ast, "<string>", "eval"))
    except SyntaxError:
        return "UTIL_ARGUMENT_ERROR (0x00000032): неправильный аргумент"
    except ValueError as ve:
        return f"{ve}"
    except Exception as e:
        return f"UTIL_PROGRAMM_ERROR (0x00000033): {str(e)}"
