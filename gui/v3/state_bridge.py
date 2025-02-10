class state:

    def __init__(self):
        self.state_init = None
        self.state_prearm = None
        self.state_arm = None
        self.state_launch = None 
        self.state_estop = None 
        self.state_shutdown = None
    
    def updateState(self, state, value):
        if state == 0:
            self.state_init = value
        else:
            self.state_init = False

        if state == 1:
            self.state_prearm = value
        else:
            self.state_prearm = False

        if state == 2:
            self.state_arm = value
        else:
            self.state_arm = False

        if state == 3:
            self.state_launch = value
        else:
            self.state_launch = False

        if state == 4:
            self.state_estop = value
        else:
            self.state_estop = False

        if state == 5:
            self.state_shutdown = value
        else:
            self.state_shutdown = False

    def getStateInput(self):
        