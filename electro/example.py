# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 22:33:09 2022

@author: Usuario
"""

from elements import Point, Particle, ParticleSystem
from fields import ElectricField


def example1():
    Q = [1e-3, -2e-3]
    P = [Point(3, -2, 1), Point(-1, -1, 4)]
    rt = Point(0, 3, 1)
    QT = Particle(name = "QT", q = 1e-9, pos = rt)
    SP = ParticleSystem(r = rt)
    for i in range(len(Q)):
        SP.addParticle(Particle(name = 'Q'+str(i+1),q = Q[i],pos = P[i]))
    print(SP.numParticles)    
    E = ElectricField(r = rt, particleSystem= SP)
    print(E.getElectricField())


if __name__ == "__main__":
    print("Test")
    example1()
    
    