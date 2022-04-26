import numpy as np

class Pipe:

    def __init__(self, id:'str', Q = 0., v = 2.): #liquid by default v = 2.0 m/s
        assert Q >= 0., f'negative volumetric flow rate'
        assert v >= 0., f'negative maximum pipe velocity'
        self.id = id #identification
        self.Q = Q #volumetric flow rate (m^3/s)
        self.v = v #maximum pipe velocity (m/s)
        
    #Pipe diameter sizing
    def diameter(self): #diameter
        return f'D = {round((100/2.54)*np.sqrt((4*self.Q/(np.pi*3600*self.v))), 4)} in'
            
    #Pipe object representation
    def __repr__(self):
        return f'Pipe of {self.id} (volumetric flow rate:{self.Q}, maximum pipe velocity: {self.v} )'