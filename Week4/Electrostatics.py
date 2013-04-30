import numpy as np

def pointPotential(x,y,q,posx,posy):
    """Return the point potential of a particle given the x and y values."""
    k = 8.98755*10**9; q = 1.6*10**(-19)
    Vpoint = (k*q/((x-posx)**2+(y-posy)**2)**(1/2.))
    return Vpoint

def dipolePotential(x,y,q,d):
    """Returns the dipole potential of a particle given the x and y values."""
    k = 8.98755*10**9;
    Vdipole = (k*q/(y**2+(x-(d/2))**2)**(1/2.))-(k*q/(y**2+(x+(d/2))**2)**(1/2.))
    return Vdipole
