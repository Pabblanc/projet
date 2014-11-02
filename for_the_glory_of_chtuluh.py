w=[60.0, 4186.0, 1]
f=[25.0, 1345.0, 0.3]
"""
temperature de départ, cp poid, poid en kg
"""
i=[0.03, 16.3, 0.03]
p=[0.1, 0.3, 0.3]
"""
surface en mètre^2, trasnfert chaleur, epaisseur en mètre
"""

def temperatur(water, fuel, inox, pom, step):
    for i in range (0, int(3600 / step)):
        x=fuel[0]
        fuel[0] = fuel[0]+step*heatflux(fuel[0], water[0], inox) / (fuel[2]*fuel[1])
        water[0] = water[0]-step*heatflux(x, water[0], inox) / (water[1]*water[2]) - step*heatflux(25, water[0], pom) / (water[1]*water[2])
    print (fuel[0], water[0])
        
def heatflux(Tinternal, Texternal, material):
    return material[0]*material[1]*(Texternal-Tinternal) / material[2]

s=0.01
temperatur (w, f, i, p, s)
