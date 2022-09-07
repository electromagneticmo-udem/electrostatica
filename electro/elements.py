# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:06:16 2022

@author: Usuario
"""

import numpy as np

class Point:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.__x = x
        self.__y = y
        self.__z = z

    # A getter method
    @property
    def x(self) -> float:
        return self.__x
    
    # A setter method
    @x.setter
    def x(self, x: float):
        self.__x = x
        
    # A getter method
    @property
    def y(self: float) -> float:
        return self.__y
    
    # A setter method
    @y.setter
    def y(self, y):
        self.__y = y
        
    # A getter method
    @property
    def z(self) -> float:
        return self.__z
    
    # A setter method
    @z.setter
    def z(self, z: float):
        self.__z = z
        
    @property
    def coords(self) -> np.array:
        return np.array([self.__x, self.__y, self.__z])
        
    def calculateDistante(self, P: "Point") -> float:
        dist = np.sqrt((self.__x - P.x)**2 + \
                       (self.__y - P.y)**2 + \
                       (self.__z - P.z)**2)
        return dist 

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

class Particle:
    def __init__(self, name: str = "", q: float = 0, pos: "Point" = Point()):
        self.__name = name
        self.__q = q
        self.__pos = pos

    # A getter method
    @property
    def pos(self) -> Point:
        return self.__pos

    # A setter method
    @pos.setter
    def pos(self, pos: "Point"):
        self.__pos = pos
        
    # A getter method
    @property
    def q(self) -> float:
        return self.__q

    # A setter method
    @q.setter
    def q(self, q: float):
        self.__q = q
        
    # A getter method
    @property
    def name(self) -> str:
        return self.__name

    # A setter method
    @name.setter
    def name(self, name: str):
        self.__name = name
    
    def __str__(self) -> str:
        return f"{self.name}{self.pos} = {self.q}C"

class ParticleSystem: 
    def __init__(self, r: "Point" = Point()):
        self.__particles = {}
        self.__r = r
        self.__numParticles = 0
    
    def addParticle(self, p: "Particle"):
        # print(self.__particles)
        self.__numParticles += 1
        self.__particles[p.name] = p
        
    def removeParticle(self, idParticle: str):
        # print(self.__particles)
        self.__numParticles -= 1
        self.__particles.pop(idParticle)
        
    # A getter method
    @property
    def particles(self) -> Particle:
        return self.__particles
    
    # A getter method
    @property
    def r(self):
        return self.__r
    
    # A getter method
    @property
    def numParticles(self):
        return self.__numParticles
    
if __name__ == "__main__":
    # Test puntos
    A = Point()
    B = Point(4,3)
    print(f'A{A}')
    print(f'B{B}')
    print(f"(x_A, y_A, z_A)) = {A.get_coords}")
    print(f"dAB = {A.calculateDistante(B)}")
    # Test particulas
    PA = Particle(name = "Q1", q = 3, pos = A)
    PB = Particle("Q2",1,B)
    print(PA)
    print(PB)
    S1 = ParticleSystem(Point(10,6,0))
    S1.addParticle(PA)
    S1.addParticle(PB)
    print(S1.numParticles)
    partSystem = S1.particles
    print(partSystem)
    for idP in partSystem:
        print(f"{partSystem[idP]}")
    S1.removeParticle(PB.name)
    print("-----------------------------")
    for idP in partSystem:
        print(f"{partSystem[idP]}")
    
    
    
    
    