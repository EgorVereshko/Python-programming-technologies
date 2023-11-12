def validate_args(func):
    def wrapper(*args):
        if (len(args) != 1) and (len(args) < 1):
            return "Not enough arguments"
        if (len(args) != 1) and (len(args) > 1):
            return "Too many arguments"
        if not isinstance(args[0], int):
            return "Wrong types"
        if args[0] < 0:
            return "Negative argument"
        return func(*args)
    return wrapper


@validate_args
def example_function(argument):
    return argument


print(example_function(11))
print(example_function())
print(example_function(1, 2, 3, 4))
print(example_function("string"))
print(example_function(-5))
