import numpy as np

def pointPotential(x,y,q,posx,posy):
    """Return the point potential of a particle given the x and y values."""
    k = 8.98755*10**9; q = 1.6e-19
    Vpoint = (k*q/((x-posx)**2+(y-posy)**2)**(1/2.))
    return Vpoint

def dipolePotential(x,y,q1,q2,d):
    """Returns the dipole potential of a particle given the x and y values."""
    k = 8.98755*10**9;
    Vdipole = (k*q1/(x**2+(y-(d/2))**2)**(1/2.))-(k*q2/(x**2+(y+(d/2))**2)**(1/2.))
    return Vdipole
