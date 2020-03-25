import numpy as np

#no if iterations
n = 150

#function for reflection
def reflection(ar,x,y,xi,yi):
    xsize = ar.shape[1]
    ysize = ar.shape[0]
    print(x,y)
    x=x+xi
    y=y+yi

    #calc the diff out of bound point and inverting it wrt to boundary
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
def move(ar,x,y,xi,yi):
    ysize = ar.shape[0]
    xsize = ar.shape[1]
    global n
    while n>=0:
       n = n-1
       if x>=xsize or x<0 or y >=ysize or y<0:
           reflection(ar,x-xi,y-yi,xi,yi)
       try:
           ar[y][x] = 1
           print(ar)
           x = x+xi
           y = y+yi
       except Exception as e:
           print


#function for declaring and printing 2D array
def createarray(y,x):
    ar = np.zeros((y, x))
    move(ar,1,1,1,6)

#function call for creatarray()
createarray(6,3)
