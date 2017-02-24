import numpy
import pylab
import matplotlib
import myFunc

print "1D-SWE"

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
    hu = [0 for x_index in range(xTotalNumber)]
    new_h = h
    new_hu = hu

    h = myFunc.addTwoElements(h)
    hu = myFunc.addTwoElements(hu)

    # The wave at point x=0     (amplitude, period, offset, wave, timeArray, length)
    h_X0 = myFunc.artificialWave(0.01, 12.5, 1, wave, timeArray, timeTotalNumber)

    # myFunc.onePlot(1, timeArray, h_X0, 'Time(s)', 'Amplitude', 'Artificial Wave', 0., timeLength, .9, 1.1)
    timeSum = 0
    while timeSum < timeTotalNumber :
        # artificialWave: start boundary condition
        h[1] = h_X0[timeSum]
        # end boundary condition
        hu[-2] = 0

        # apply boundary conditions
        h = myFunc.neumannBoundaryConditions(h)
        hu = myFunc.neumannBoundaryConditions(hu)

        u = hu / h

        h[1:-1], hu[1:-1] = myFunc.iteration_Lax_Friedrichs(h, hu)
        timeSum += 1

        if timeSum == timeTotalNumber :
            myFunc.onePlot(2, xArray, h[1:-1], 'x(m)', 'h', 'h-x', 0., tunnelLength, .9, 1.1)
            myFunc.onePlot(3, xArray, u[1:-1], 'x(m)', 'u', 'u-x', 0., tunnelLength, -.3, .3)
            pylab.show()
    print "finish SWE"

if __name__ == "__main__":
    SWE()

