# positional arg
# keyword arg
# required arg
# Optional arg

def addition(x=0, y=0):
    return x+y
x = addition()
print(x)
x = addition(10,20)
print(x)
x = addition(10)
print(x)
x = addition(y=5)
print(x)