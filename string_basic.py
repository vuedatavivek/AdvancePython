from datetime import date, datetime


x = "This is strong"
y = 'This is also string'
z = 'this is string \'with esc \' char '
a = """
Multi 
Line
String 
"""
b = '''
This is also 
multy line 
string
'''

print(x)
print(y)
print(z)
print(a)
print(b)
print('len',len(x))
print('str', str(2))
print(x.find('is'))
print("x is "+ x + " y is" + y)
print ("x is %s and y is %s" %(x,y))
print ("x is {} and {} is y".format(x,y))