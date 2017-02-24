import numpy
import pylab

g = 9.8             # gravitational acceleration
tunnelLength = 3.   # meter
timeLength = 1.     # second
dx = 1. / 10000
dt = 1. / 60000

def artificialWave(amplitude, period, offset, wave, timeArray, length):
    for i in range(length):
        wave[i] = amplitude * numpy.cos(period * 2 * numpy.pi * timeArray[i]) + offset
    return wave


def addTwoElements(var):
    # add 1 element before and after the list
    return numpy.hstack([0., var, 0.])


def neumannBoundaryConditions(var):
    # Neumann Boundary
    var[0] = var[1]
    var[-1] = var[-2]
    return var


def iteration_Lax_Friedrichs(h, hu):
    u = hu / h
    F_h = hu
    F_hu = h*u**2 + 0.5*g*h**2

    firstTermInLF = h[2:] + h[:-2]
    secondTermInLF = F_h[2:] - F_h[:-2]
    new_h = 0.5 * firstTermInLF - (0.5*dt/dx) * secondTermInLF

    firstTermInLF = F_h[2:] + F_h[:-2]
    secondTermInLF = F_hu[2:] - F_hu[:-2]
    new_hu = 0.5 * firstTermInLF - (0.5*dt/dx) * secondTermInLF
    return new_h, new_hu


def onePlot(figNum, x, y, xLabel, yLabel, title, xLimL, xLimR, yLimL, yLimR):
    pylab.figure(figNum)
    pylab.plot(x, y)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.title(title)
    pylab.axis('tight')
    pylab.xlim(xLimL, xLimR)
    pylab.ylim(yLimL, yLimR)
    pylab.draw()


if __name__ == "__main__":
    print "in myFunc"

