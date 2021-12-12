

class store:
    def __init__(self):
        self.emptyState = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.reset()

    def clearState(self, unit):
        unit = self.emptyState



class Registers(store):
    def reset(self):
        Acumulator = self.emptyState
        MAR        = self.emptyState
        MDR        = self.emptyState
        PC         = self.emptyState
        REG0       = self.emptyState
        REG1       = self.emptyState
        REG2       = self.emptyState
        REG3       = self.emptyState
        REG4       = self.emptyState

    




class RAM(store):
    def reset(self):
        self.RAM = [
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
            [self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState, self.emptyState],
        ]



RAM = RAM()
for x in RAM.RAM:
    for y in x:
        print(y)