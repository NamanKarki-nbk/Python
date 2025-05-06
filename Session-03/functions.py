#*args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#This are also called Arbitrary Arguments

def my_functions(*kids):
    print("The youngest child is " + kids[2])
    
my_functions("Naman", "Karan", "Tsukasa")


#*kwargs
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition
def demo(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

demo(1, 2, 3, name="Alice", age=25)
