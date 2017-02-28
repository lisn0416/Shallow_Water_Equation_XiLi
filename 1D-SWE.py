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

    # The wave at point x=0     (amplitude, period, offset, wave, timeArray, length, ifNoise, noiseRate)
    h_X0 = myFunc.artificialWave(0.05, 12.5, 1, wave, timeArray, timeTotalNumber, 0, 0.2)
    # myFunc.onePlot(1, timeArray, h_X0, 'Time(s)', 'Amplitude', 'Artificial Wave', 0., timeLength, .9, 1.1)

    timeSum = 0
    while timeSum < timeTotalNumber :
        # artificialWave: start boundary condition
        h[1] = h_X0[timeSum]

        if timeSum == numpy.ceil((timeTotalNumber-1)/2) :
            if 1: # quantisation
                for i in range(len(h)):
                    h[i] = round(h[i]*4)/(4)
                    hu[i] = round(hu[i]*4)/(4)
            else: # noise
                for i in range(len(h)):
                    h[i] += (numpy.random.random() - 0.5) * 0.2
                    hu[i] += (numpy.random.random() - 0.5) * 0.2

        # end boundary condition
        hu[-2] = 0

        # apply boundary conditions
        h = myFunc.neumannBoundaryConditions(h)
        hu = myFunc.neumannBoundaryConditions(hu)

        h[1:-1], hu[1:-1] = myFunc.iteration_Lax_Friedrichs(h, hu)

        u = hu / h
        timeSum += 1

        if timeSum == numpy.ceil((timeTotalNumber-1)) :
            #myFunc.onePlot(2, xArray, h[1:-1], 'x(m)', 'h(m)', 'Height', 0., tunnelLength, .9, 1.1)
            #myFunc.onePlot(3, xArray, u[1:-1], 'x(m)', 'u(m/s)', 'Velocity', 0., tunnelLength, -.3, .3)
            #myFunc.onePlot(4, xArray, hu[1:-1], 'x(m)', 'hu(m^2/s)', 'Momentum', 0., tunnelLength, -.5, .5)

            myFunc.threePlot(5, xArray, h[1:-1], 'x(m)', 'h(m)', 'Height', 0., tunnelLength, .9, 1.1,
                                xArray, u[1:-1], 'x(m)', 'u(m/s)', 'Velocity', 0., tunnelLength, -.3, .3,
                                xArray, hu[1:-1], 'x(m)', 'hu(m^2/s)', 'Momentum', 0., tunnelLength, -.5, .5)

            pylab.show()
            break
    print "finish 1D-SWE"

if __name__ == "__main__":
    SWE()

