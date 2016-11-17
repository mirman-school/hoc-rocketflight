import math
from rockets import *
from visualizer import visualize
# for r in rockets:
#     print(rockets[r])

'''
Ticks are "seconds" of mission time. Each tick is a tuple of (Vector Position, Vector velocity)
'''


class Vector:
    '''
    describes 2D values such as velocity and position.
    '''

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)

class Tick:
    '''
    Tick object describing the state of a vehicle at a moment in time.
    velocity: Vector
    position: Vector
    '''
    def __init__(self, v=Vector(), p=Vector()):
        self.velocity = v
        self.position = p

def tick(r, last_tick, elapsed_time):
    '''
    Perform the Tsiolkovsky equation every "tick" for the flight.
    '''
    if elapsed_time < r.burn_time:
        delta_v = Vector(0,r.thrust/r.mass)
    else:
        delta_v = Vector(0,-10)
    v = last_tick.velocity
    pos = last_tick.position
    v += delta_v
    pos += v

    # Don't go underground
    if pos.y <= 0:
        pos.y = 0
        v.y = 0
    return Tick(v, pos)

def fly(rocket,mission_time):
    '''
    Simulates the flight of a given rocket
    '''
    ticks = [Tick()]
    for i in range(mission_time):
        ticks.append(tick(rocket, ticks[-1],len(ticks)))

    return ticks

# Program your flight here!
rocket = rockets["saturnv"]
flight_time = 1000
flight = fly(rocket,flight_time)

#This line makes the graph appear
visualize(flight)
