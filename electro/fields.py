# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:22:40 2022

@author: Usuario
"""

import numpy as np
import scipy as sp
from numpy import linalg as LA
from elements import Point, Particle, ParticleSystem

class ElectricField:
    # Constantes
    e0 = 8.85*10**(-12)        # permetivity of free space
    ke = 1 / (4 * sp.pi* e0)   # Electric constant
    
    def __init__(self, r: "Point", particleSystem: "ParticleSystem" = ParticleSystem()):
        self.__particleSystem = particleSystem
        self.__r = r
    
    # A getter method
    @property
    def particleSystem(self) -> ParticleSystem:
        return self.__particleSystem
    
    # A setter method
    @particleSystem.setter
    def particleSystem(self, particleSystem: "ParticleSystem"):
        self.__particleSystem = particleSystem
       
    # A getter method
    @property
    def r(self) -> float:
        return self.__r
    
    # A setter method
    @r.setter
    def r(self, r: float):
        self.__r = r


    
    
    def getElectricField(self) -> np.array:
        electricField = np.array([0,0,0],dtype=float)
        if(self.particleSystem.numParticles == 0):
            return electricField
        else:
            for idP in self.particleSystem.particles:
                q_i = self.particleSystem.particles[idP].q
                r = self.r.coords
                r_i = self.particleSystem.particles[idP].pos.coords
                d_i = r - r_i
                electricField += (q_i/LA.norm(d_i)**3)*d_i
            return electricField

if __name__ == "__main__":
    # Test particulas
    P1 = Particle(name = "Q1", q = 3, pos = Point())
    P2 = Particle("Q2",1, Point(4,3))
    print(P1)
    print(P2)
    S1 = ParticleSystem(Point(10,6,0))
    S1.addParticle(P1)
    S1.addParticle(P2)
    print(S1.numParticles)
    E1 = ElectricField(Point(6,6,0),S1)
    print(E1.r)
    print(E1.getElectricField())
    
    
   
    
    
