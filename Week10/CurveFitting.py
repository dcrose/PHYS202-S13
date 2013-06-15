def LinearLeastSquaresFit(x,y):
    from numpy import *
    """Take in arrays representing (x,y) values for a set of linearly varying data and
    preform a linear least squares regression. Return the resulting slope and intercept
    parameters of the best fit line with their uncertainties."""
    a = average
    slope = (a(x*y)-a(x)*a(y))/(a(x**2)-(a(x))**2)
    intercept = (a(x*x)*a(y)-a(x)*a(x*y))/(a(x**2)-(a(x))**2)
    f = y-(slope*x+intercept)
    n = len(x)
    slerr = ((1/(n-2.))*a(f**2)/(a(x**2)-(a(x))**2))**.5
    interr = ((1/(n-2.))*(a(f**2)*a(x**2))/(a(x**2)-(a(x))**2))**.5
    
    return slope,intercept,slerr,interr

def WeightedLinearLeastSquaresFit(x,y,w):
    from numpy import *
    """Take in arrays representing (x,y) values for a set of linearly varying data and
    and an array of weights w. Perform a weighted linear least squares fit regression.
    Return the resulting slope and intercept parameters of the best fit line with their
    uncertainties.

    If the weights are all equal to one, the uncertainties on the parameters are calculated
     using the non-weighted least squares equations."""
    a = average
    
    slope = ((sum(w)*sum(w*x*y))-sum(w*x)*sum(w*y))/((sum(w)*sum(w*x*x))-(sum(w*x))**2)
    intercept = ((sum(w*x*x)*sum(w*y))-sum(x*w)*sum(w*x*y))/((sum(w)*sum(w*x*x))-(sum(w*x))**2)
    
    if all(w == ones(len(w))):
        f = y-(slope*x+intercept)
        n = len(x)
        slerr = ((1/(n-2.))*a(u**2)/(a(x**2)-(a(x))**2))**.5
        interr = ((1/(n-2.))*(a(u**2)*a(x**2))/(a(x**2)-(a(x))**2))**.5
    
    else:
        slerr = (sum(w)/((sum(w)*sum(w*x*x))-sum(w*x)**2))**.5
        interr = (sum(w*x*x)/((sum(w)*sum(w*x*x))-sum(w*x)**2))**.5
    
    return slope,intercept,slerr,interr
