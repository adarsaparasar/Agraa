import numpy as np  #library for using arrays
def move(ar,x,y,xi,yi):
    xsize = ar.shape[0]
    ysize = ar.shape[1]
    while x<xsize or y<ysize:
       ar[x][y] = 1
       print(ar)
       x = x+xi
       y = y+yi

#function for declaring and printing 2D array
def createarray(n):
    ar = np.zeros((n, n))
    print(ar.shape[0],ar.shape[1])
    print(ar)
    move(ar,0,0,1,1)

#function call for printarray()
print("Enter number")
x = input()
createarray(int(x))
