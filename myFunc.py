import numpy
import pylab

g = 9.8             # gravitational acceleration
tunnelLength = 3.   # meter
timeLength = 1.     # second
dx = 1. / 10000
dt = 1. / 60000

def artificialWave(amplitude, period, offset, wave, timeArray, length, ifNoise, noiseRate):
    for i in range(length):
        wave[i] = amplitude * numpy.cos(period * 2 * numpy.pi * timeArray[i]) + offset
        if ifNoise == 1:
            wave[i] += amplitude * noiseRate * (numpy.random.random() - 0.5 * offset)
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
    pylab.grid()
    pylab.draw()


def threePlot(figNum, x1, y1, xLabel1, yLabel1, title1, xLimL1, xLimR1, yLimL1, yLimR1,
                      x2, y2, xLabel2, yLabel2, title2, xLimL2, xLimR2, yLimL2, yLimR2,
                      x3, y3, xLabel3, yLabel3, title3, xLimL3, xLimR3, yLimL3, yLimR3):
    # Figure(figsize=None, dpi=None, facecolor=None, edgecolor=None, linewidth=0.0, frameon=None, subplotpars=None, tight_layout=None)
    pylab.figure(figNum, figsize=(8, 3), dpi=300)
    pylab.subplots_adjust(left=0.08, right=0.97, bottom=0.15, top=0.9, wspace=0.3)

    pylab.subplot(131)
    pylab.title(title1)
    pylab.plot(x1, y1, linewidth=1.0)
    pylab.axis('tight')
    pylab.xlabel(xLabel1, fontsize=6)
    pylab.ylabel(yLabel1, fontsize=6)
    pylab.xlim(xLimL1, xLimR1)
    pylab.ylim(yLimL1, yLimR1)
    pylab.xticks(fontsize=6)
    pylab.yticks(fontsize=6)
    pylab.grid()

    pylab.subplot(132)
    pylab.title(title2)
    pylab.plot(x2, y2, linewidth=1.0)
    pylab.axis('tight')
    pylab.xlabel(xLabel2, fontsize=6)
    pylab.ylabel(yLabel2, fontsize=6)
    pylab.xlim(xLimL2, xLimR2)
    pylab.ylim(yLimL2, yLimR2)
    pylab.xticks(fontsize=6)
    pylab.yticks(fontsize=6)
    pylab.grid()

    pylab.subplot(133)
    pylab.title(title3)
    pylab.plot(x3, y3, linewidth=1.0)
    pylab.axis('tight')
    pylab.xlabel(xLabel3, fontsize=6)
    pylab.ylabel(yLabel3, fontsize=6)
    pylab.xlim(xLimL3, xLimR3)
    pylab.ylim(yLimL3, yLimR3)
    pylab.xticks(fontsize=6)
    pylab.yticks(fontsize=6)
    pylab.grid()

    pylab.draw()
    pylab.savefig(title1+'+'+title2+'+'+title3, facecolor='w', edgecolor='w')


if __name__ == "__main__":
    print "in myFunc"

