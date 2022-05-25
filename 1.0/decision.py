class decision:
    def __init__(self,creature,time_until_activation, action):
        self.time_until_activation = time_until_activation
        self.action = action
        
    def effect(self):
        if self.action == "right_1":
            pass
            