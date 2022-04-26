from Unit_Operations import Pipe
from Volumetric_flow_rates import *

V6 = 15.6 #given volumetric flow rate of 'etanol p/ tanque'
V7 = 21257.218 #given volumetric flow rate of 'flegma'

#object pipe instantiation
Pipeline_1 = Pipe('Alcool de segunda:', V1, 20.)
Pipeline_2 = Pipe('Vinhaca:', V2)
Pipeline_3 = Pipe('Oleo fusel:', V3)
Pipeline_4 = Pipe('Vapor de agua p/ a coluna A:', V4, 20.)
Pipeline_5 = Pipe('Vapor de agua p/ a coluna B:', V5, 20.)
Pipeline_6 = Pipe('Etanol p/ tanque:', V6)
Pipeline_7 = Pipe('Flegma:', V7, 20.)

#printing diameter property of objects
print(Pipeline_1.id, Pipeline_1.diameter())
print(Pipeline_2.id, Pipeline_2.diameter())
print(Pipeline_3.id, Pipeline_3.diameter())
print(Pipeline_4.id, Pipeline_4.diameter())
print(Pipeline_5.id, Pipeline_5.diameter())
print(Pipeline_6.id, Pipeline_6.diameter())
print(Pipeline_7.id, Pipeline_7.diameter())