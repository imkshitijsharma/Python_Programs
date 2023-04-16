#!/usr/bin/env python
# coding: utf-8

# # PERIMETER OF SHAPES 
# 

# In[2]:


def pot(x,y,z):                                              ###### function defining parimeter of triangle                          
    print("Perimeter of a triangle:", x + y + z)

def poc(rad):                                                ##### function defining parimeter of circle    
    print("Perimeter of a circle:", 2 * 3.14 * rad)

def por(x, y):                                               ##### function defining parimeter of rectangle   
    print("Perimeter of a rectangle:", 2 * (x + y))

def pos(side):                                               ##### function defining parimeter of square    
    print("Perimeter of a square:", 4 * side)

print("Perimeter of shapes\n1.Perimeter of triangle\n2.Perimeter of circle\n3.Perimeter of rectangle\n4.Perimeter of square")
menu = int(input("Enter the number of the shape to calculate perimeter: "))     
if menu == 1:
    x = int(input("Enter the length of the first side of the triangle: "))
    y = int(input("Enter the width of the second side of the triangle: "))
    z = int(input("Enter the height of the third side of the triangle: "))
    pot(x,y,z)
elif menu == 2:
    rad = int(input("Enter the radius of the circle: "))
    poc(rad)
elif menu == 3:
    x = int(input("Enter the length of the rectangle: "))
    y = int(input("Enter the width of the rectangle: "))
    por(x, y)
elif menu == 4:
    side = int(input("Enter the length of the side of the square: "))
    pos(side)
else:
    print("Enter a value between 1 and 4")


# In[ ]:




