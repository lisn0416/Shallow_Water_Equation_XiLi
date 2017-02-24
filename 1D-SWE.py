import numpy
import pylab
import matplotlib

print "SWE"

g = 9.8             # gravitational acceleration
tunnelLength = 3.   # meter
timeLength = 1.     # second
dx = 1. / 10000
dt = 1. / 60000

xTotalNumber = int(tunnelLength / dx)
timeTotalNumber = int(timeLength / dt) + 1  # [0s , 1s], 60001 points
timeArray = numpy.linspace(0, timeLength, timeTotalNumber)
xArray = numpy.linspace(0, tunnelLength, xTotalNumber)

wave = [0. for time_index in range(timeTotalNumber)]

def SWE():
    # Initial Conditions
    h = [1 for x_index in range(xTotalNumber)]
    #u = [0 for x_index in range(xTotalNumber)]
    hu = [0 for x_index in range(xTotalNumber)]
    new_h = [1 for x_index in range(xTotalNumber)]

    #for i in range(xTotalNumber):
    #    hu[i] = h[i] * u[i]

    h = addTwoElements(h)
    #u = addTwoElements(u)
    hu = addTwoElements(hu)

    # The wave at point x=0
    h_X0 = artificialWave(0.05, 12.5, wave, timeArray, timeTotalNumber)

    pylab.figure(1)
    pylab.plot(timeArray, h_X0)
    pylab.xlabel('Time(s)')
    pylab.ylabel('Amplitude')
    pylab.axis('tight')
    pylab.xlim(0., timeLength)
    pylab.ylim(.9, 1.1)
    pylab.draw()

    timeSum = 0
    while timeSum < timeTotalNumber :
        # artificialWave
        h[1] = h_X0[timeSum]
        # apply boundary conditions
        h = neumannBoundaryConditions(h)
        hu = neumannBoundaryConditions(hu)
        u = hu / h
        Fh = hu
        Fhu = h*u**2 + 0.5*g*h**2

        firstTermInLF = h[2:] + h[:-2]
        secondTermInLF = hu[2:] - hu[:-2]
        new_h = 0.5 * firstTermInLF - (0.5*dt/dx) * secondTermInLF
        h[1:-1] = new_h

        firstTermInLF = Fh[2:] + Fh[:-2]
        secondTermInLF = Fhu[2:] - Fhu[:-2]
        new_hu = 0.5 * firstTermInLF - (0.5 * dt / dx) * secondTermInLF
        hu[1:-1] = new_hu

        timeSum += 1

        if timeSum == 60000 :
            print "plot h"
            pylab.figure(2)
            pylab.plot(xArray, h[1:-1])
            pylab.xlabel('x(m)')
            pylab.ylabel('h')
            pylab.axis('tight')
            pylab.xlim(0., tunnelLength)
            pylab.ylim(.9, 1.1)
            pylab.show()
    print "finish SWE"


def artificialWave(amplitude, period, wave, timeArray, length):
    for i in range(length):
        wave[i] = amplitude * numpy.cos(period * 2 * numpy.pi * timeArray[i]) + 1
    return wave

def addTwoElements(var):
    # add 1 element before and after the list
    return numpy.hstack([0., var, 0.])

def neumannBoundaryConditions(var):
    # Neumann Boundary
    var[0] = var[1]
    var[-1] = var[-2]
    return var

SWE()