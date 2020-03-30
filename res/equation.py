import math

class Equation:
    eq ="y=0x+0"
    x,y,x1,y1 = 0,0,0,0
    m,c = 0,0

    def setLine(self):
        eflag = 0
        a = self.y1-self.y
        b = self.x1-self.x
        g = math.gcd(a,b)
        try:
            a = a/g
            b = b/g
        except ZeroDivisionError:
            a = a
            b = b



        #finding c (y-intercept)(m is slope)
        try:
            self.m = a/b
            self.c = self.y - self.x*self.m
        except ZeroDivisionError:
            eflag = 1

        #final string equation in the form y = mx + c
        if eflag == 0:
            self.eq = "y="+str(a)+"/"+str(b)+"x"+"+"+str(self.c)
        else:
            self.eq = "x="+str(self.x)


    def __init__(self,x,y,x1,y1):
        self.x = int(x)
        self.y = int(y)
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.setLine()

    def getSlope(self):
        return self.m

    def getC(self):
        return self.c

    def getLine(self):
        return self.eq

    def getMat(self):
        return [[-self.m,self.m],self.m*(self.x-self.y)]
