import numpy as np #library for using array objects 

#no if iterations
n = 150

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


#function for movement iteration
def move(ar,x,y,xi,yi): #move(array,x,y,x-increment,y-increment)
    ysize = ar.shape[0]
    xsize = ar.shape[1]
    global n
    while n>=0:
       n = n-1
       if x>=xsize or x<0 or y >=ysize or y<0: #condition to check if out of bounds
           reflection(ar,x-xi,y-yi,xi,yi)
       try:
           ar[y][x] = 1
           print(ar)
           x = x+xi
           y = y+yi
       except Exception as e:
           print


#function for declaring 2D array and starting
def createarray(y,x): #createarray(ysize,xsize)
    ar = np.zeros((y, x))
    move(ar,1,1,1,6)

#function call for creatarray()
createarray(6,3)
