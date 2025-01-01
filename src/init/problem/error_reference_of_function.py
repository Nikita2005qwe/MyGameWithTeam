class ExampleClass:
    def __init__(self, func):
        self.func = func
        print(self.func)

    def call_func(self, arg):
        self.func(arg)

def my_function(x):
    print(f"Value from function: {x}")

print(my_function)
instance = ExampleClass(my_function)
print(instance.func)
instance.call_func(42)
