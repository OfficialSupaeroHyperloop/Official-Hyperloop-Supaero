class breakSim:
    def __init__(self):
        self.break_closed = None
        self.breaks_open = None
        self.breaks_pressure = 0

    def openBreak(self):
        self.breaks_closed = False
        self.breaks_open = True

        self.breaks_pressure = 4

        return None

    def closeBreak(self):
        self.breaks_closed = True
        self.breaks_open = False

        self.breaks_pressure = 10

        return None

    def getBreakVal(self):

        return self.breaks_pressure
    
class telemetrySim:
    def __init__(self):
        self.ack = False

    def sendAck(self):
        self.ack = True

        return self.ack

class powerSim:
    def __init__(self):
        self.lpc_okay = False
    
    def activateLpc(self):
        self.lpc_okay = True

    def getLpcVal(self):
        return self.lpc_okay
    
class propSim:  
    def computeAccel(self):
        self.computedAccel= 0.000
        self.accelCounter.setInterval(1000)
        self.accelCounter.timeout.connect(self.setAccel)
        self.accelCounter.start()

    def computeVelocity(self):
        self.computedVelocity= 0.000
        self.velocityCounter.setInterval(1000)
        self.velocityCounter.timeout.connect(self.setVelocity)
        self.velocityCounter.start()

    def computeDistance(self):
        self.computedDistance= 0.000
        self.distanceCounter.setInterval(1000)
        self.distanceCounter.timeout.connect(self.setDistance)
        self.distanceCounter.start()
        
    def setAccel(self):
        self.computedAccel+=0.05
        self.AccelReading.setText("{:.2f}".format(self.computedAccel))

    def setVelocity(self):
        self.computedVelocity += (self.computedAccel/20)
        self.VelocityReading.setText("{:.2f}".format(self.computedVelocity))
        self.velocities.append(self.computedVelocity)
        self.timestamps.append(self.time)
        # self.graphWidget.plot(self.timestamps, self.velocities)
    
    def setDistance(self):
        self.computedDistance += 1.0
        self.DistanceReading.setText("{:.2f}".format(self.computedDistance))