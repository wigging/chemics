import numpy as np


def disp(D, L, u, t):
    """
    Calculate the 1-D continuum dispersion model for RTD.

    Parameters
    ----------
    D = dispersion coefficient
    L = characteristic mixing length
    u = average fluid velocity
    t = time vector

    Returns
    -------
    et = residence time distribution
    """
    tm1 = u/(np.sqrt(4*np.pi*D*t))
    tm2 = ((L-u*t)**2)/(4*D*t)
    et = tm1*np.exp(-tm2)
    return et


def scstr(n, tau, t):
    """
    Exit age distribution (RTD) for solids in multistaged fluidized beds from
    Eq 5 in Kunii 1991 book from pg 339.

    Parameters
    ----------
    n = number of stages, number of equal-sized beds in series
    tau = total solids residence time, s
    t = time vector, s

    Returns
    -------
    et = exit age distribution or RTD of solids as a whole
    """
    # solids residence time for each stage from Eq. 4
    ti = tau/n
    # RTD of the solids for the beds as a whole from Eq. 5
    et = 1/(np.math.factorial(n-1)*ti)*(t/ti)**(n-1)*np.exp(-t/ti)
    return et


def vusse(n, tau, t, q=1, r=1):
    """
    Residence time distribution function for stirred tank reactor from paper by
    Vusse 1962. Assumes circulating flow, pumping action of stirrer, isotropic
    homogeneous turbulence in the circulating fluid.

    Parameters
    ----------
    n = number of mixing stages, (-)
    tau = circulation time, s
    t = time vector, s
    q = feed rate, m^3/s
    r = circulation rate, m^3/s

    Returns
    -------
    rt = residence time distribution, 1/s

    Example
    -------
    r = rtd(n, tau, t) or rtd(n, tau, t, q=2, r=3)
    """
    a = (n/tau)*(r/(r+q))**(1/n)    # term from Eq. 30
    s = 0                           # initialize summation for g(at) Eq. 31

    for k in range(0, n):
        # summation loop for number of mixing stages, see g(at) from Eq. 31
        tm = np.exp(a*t*(np.cos(2*np.pi*k/n) + 1j*np.sin(2*np.pi*k/n))
                    + 1j*(2*np.pi*k)/n)
        s += tm

    # g as g(at) from Eq. 31 and rt as R(t) from Eq. 30
    g = (1/n)*s
    # vector of complex values for residence time distribution
    rt = (q/(r+q))*((r+q)/r)**((n-1)/n)*(n/tau)*np.exp(-(n*t)/tau)*g
    return rt


def weibull(x, lam, k):
    """
    Weibull distribution function.

    Parameters
    ----------
    x = time parameter
    k = shape parameter
    lam = lambda as scale parameter

    Returns
    -------
    w = weibull distribution
    """
    w = (k/lam)*((x/lam)**(k-1))*np.exp(-(x/lam)**k)
    return w
