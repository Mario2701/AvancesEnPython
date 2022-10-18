#Variables globales
from tkinter import Y


x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

#La palabra clave mundial
def myfunc():
    global y 
    y = "awesome"
    
myfunc()

print("Python is " + y)

z = "not awesome"

def myfunc():
    global z
    z = "awesome"
    
myfunc()

print("Python is " + z)