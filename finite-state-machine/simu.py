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