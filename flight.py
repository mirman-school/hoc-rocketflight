import math
from rockets import *
from visualizer import visualize

'''
Ticks are "seconds" of mission time. Each tick is a tuple of (Vector Position, Vector velocity)
'''
GRAVITY = -10

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


def tick(r, last_tick, elapsed, flight_plan):
    '''
    Perform the Tsiolkovsky equation every "tick" for the flight.
    '''
    global GRAVITY
    r.set_engine_state(elapsed, flight_plan) # Look in the Rocket class for set_engine_state()
    if r.engine_on:
        delta_v = Vector(0,(r.thrust/(r.mass - (r.total_burn)) + GRAVITY))
        r.total_burn += 1
    else:
        delta_v = Vector(0,GRAVITY)
    v = last_tick.velocity
    pos = last_tick.position
    v += delta_v
    pos += v

    # Don't go underground
    # if pos.y <= 0:
    #     pos.y = 0
    #     v.y = 0
    return Tick(v, pos)

def fly(rocket, mission_time, flight_plan):
    '''
    Simulates the flight of a given rocket
    '''
    ticks = [Tick(p=Vector(0,1))]
    for i in range(mission_time):
        last_tick = ticks[-1]
        # Stop if we hit the ground last tick
        if last_tick.position.y <= 0:
            break
        next_tick = tick(
                        rocket,
                        last_tick,
                        len(ticks),
                        flight_plan
                        )
        ticks.append(next_tick)

    return ticks

# Uncomment these lines to print your rockets!
# for r in rockets:
#     print(rockets[r])

# Program your flight here!
# ---

rocket = rockets["saturnv"]
flight_time = 1000
flight_plan = {
    1: "on",
    30: "off",
    50: "on"
}
flight = fly(rocket, flight_time, flight_plan)

# ---

# This line makes the graph appear
visualize(flight)
