#volumetric flow rates

#calculating volume of pipeline L1 'alcool de segunda' per hour
me = 1175. #ethanol mass in Kg
mw = 1506.4102 - me #water mass in Kg
#data for gas volume
MMe = 0.04607 #ethanol molecular mass in Kg/mol
MMw = 0.01802 #water molecular mass in Kg/mol
R = 8.2057e-5 #molar gas constant
Te = 78. #boiling point of alcoholic mixture in celsius degrees
T = 273. + Te #boiling point of alcoholic mixture in kelvin
P = 1. #pressure in atm
Ve = (me*R*T)/(MMe*1) #volume of ethanol vapour
Vw = (mw*R*T)/(MMw*1) #volume of steam
V1 = Ve + Vw #volumetric flow rate of 'alcool de segunda' as vapour



#calculating volume of pipeline L2 'vinhaça' per hour
V2 = 184636.44/1e3 #given volumetric flow rate of 'vinhaca'



#calculating volume of pipeline L3 'Óleo de fusel' per hour
V3 = 400./800. #volumetric flow rate of 'oleo de fusel' and mass density of 800 Kg/m^3



#calculating volume of pipeline L4 'Vapor de agua p/ a coluna A' per hour
'''for a recommended saturated steam pressure of 3Kgf/cm^2
from steam table:
International Steam Tables
Properties of Water and Steam based on
the Industrial Formulation IAPWS-IF97
3rd Edition
Hans-Joachim Kretzschmar · Wolfgang Wagner, page 186
'''
Ps = 3*0.980665 #converting Kgf/cm^2 pressure for bar
#proceeding with linear interpolation of 3 and 2.9 bar values
vs = ((0.625355 - 0.605785)*(3 - Ps)/(3 - 2.9)) + 0.605785
#using calculated specific volume
V4 = 25000.*vs #volumetric flow rate of steam for column A



#calculating volume of pipeline L5 'Vapor de agua p/ a coluna B' per hour
V5 = 10000.*vs #volumetric flow rate of steam for column BV6 = 15.6 #given volumetric flow rate of 'etanol p/ tanque'
#using calculated specific volume vs