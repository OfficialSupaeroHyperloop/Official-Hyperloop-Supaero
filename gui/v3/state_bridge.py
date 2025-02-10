class state:

    class GUI_State:
        # State Enum 
        (
            main_init,
            main_launch, 
            main_estop,
            main_prearm,
            main_arm,
            main_push,
            main_coast,
            main_braking,
            main_shutdown,
            null_state
        ) = range(10)

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
        if self.state_init is True: 
            return self.GUI_State.main_init
        
        if self.state_launch is True: 
            return self.GUI_State.main_launch
        
        if self.state_estop is True: 
            return self.GUI_State.main_estop
        
        if self.state_prearm is True: 
            return self.GUI_State.main_prearm
        
        if self.state_arm is True: 
            return self.GUI_State.main_arm
        
        if self.state_shutdown is True: 
            return self.GUI_State.main_shutdown