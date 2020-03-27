import numpy as np #library for using array objects
from equation import Equation
#no if iterations
n = 20

eqList = []

#function for reflection
def reflection(ar,x,y,xi,yi): #reflection(ar,x,y,x-increment,y-increment)
    xsize = ar.shape[1]
    ysize = ar.shape[0]
    x=x+xi
    y=y+yi

    #calculate the different out of bound points and inverting it
    if x<0:
        x=-x
        xi=-xi

    if y<0:
        y=-y
        yi=-yi

    if x>=xsize:
        x = xsize-abs((xi+x)-(xsize-1))
        xi = -xi

    if y>=ysize:
        y = ysize-abs((yi+y)-(ysize-1))
        yi = -yi


    move(ar,x,y,xi,yi)

#function to check ray re-tracing. Returns 0 if 0 found in current path otherwise 1
def checkRay(ar,x,y,xi,yi):
    x = x+xi
    y = y+yi
    xsize = ar.shape[1]
    ysize = ar.shape[0]
    while x>=0 and y>=0 and x<xsize and y<ysize:
        print(x,y)
        if ar[y][x] == 0:
            return 0
        x = x + xi
        y = y + yi
    return 1




#function for movement iteration
def move(ar,x,y,xi,yi): #move(array,x,y,x-increment,y-increment)
    ysize = ar.shape[0]
    xsize = ar.shape[1]
    global n

    #creating equation object using Equation
    eq = Equation(x,y,xi,yi)
    eq = eq.getLine()


    while n>=0:
        if x>=xsize or x<0 or y >=ysize or y<0: #condition to check if out of bounds
            reflection(ar,x-xi,y-yi,xi,yi)
        try:
            eqList.append(eq)
            n = n-1
            print(eq)
            ar[y][x] = 1
            print(ar)
            x = x+xi
            y = y+yi
        except Exception as e:
            print



#function for declaring 2D array and starting
def createarray(y,x): #createarray(ysize,xsize)
    ar = np.zeros((y, x))
    move(ar,1,1,1,1)

#function call for creatarray()
try:
    createarray(6,3)
except Exception:
    print
print("*")
for i in eqList:
    print(i)
