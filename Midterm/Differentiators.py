import numpy as np

def finiteDifference(x,y):
    """This will take two arguments, x and y(x), and returns the derivative of y with respect to x"""
    dydx1 = np.zeros(y.shape,float)
    dydx1[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2]) #center difference
    dydx1[0] = (y[1] - y[0])/(x[1] - x[0]) #forward difference
    dydx1[-1] = (y[-1] - y[-2])/(x[-1] - x[-2]) #backward difference
    return dydx1

def fourPtFiniteDiff(x,y):
    dydx = np.zeros(y.shape)
    dydx[2:-2] = (y[:-4]-8*y[1:-3]+8*y[3:-1]-y[4:])/(x[:-4]-8*x[1:-3]+8*x[3:-1]-x[4:])
    dydx[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])
    dydx[1] = (y[2]-y[1])/(x[2]-x[1])
    dydx[-2] = (y[-2]-y[-3])/(x[-2]-x[-3])
    return dydx
