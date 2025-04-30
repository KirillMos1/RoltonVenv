def calculate(expr):
    if "+" in expr or "-" in expr or "*" in expr or "/" in expr or "^" in expr:
        return eval(expr)
    else:
        return "UTIL_ARGUMENT_ERROR (0x00000032): неправильный аргумент"