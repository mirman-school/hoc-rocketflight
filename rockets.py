class Rocket:

    def __init__(self,name,mass,burn_time,thrust):
        '''
        Mass: kg
        burn_time: s
        Thrust kN
        '''
        self.name = name
        self.mass = mass
        self.burn_time = burn_time
        self.thrust = thrust
        self.total_burn = 0
        self.engine_on = False

    def __str__(self):
        return "{}:\n\tMass: {} kg\n\tBurn Time: {} s\n\tThrust: {} N".format(
            self.name,
            self.mass,
            self.burn_time,
            self.thrust
        )

    def set_engine_state(self, elapsed, flight_plan):
        '''
        Determines whether the rocket engine should be burning based on
        flight plan commands and if there's fuel left.
        '''
        try:
            plan_key = flight_plan[elapsed]
            if plan_key == "on":
                self.engine_on = self.total_burn < self.burn_time
            else:
                self.engine_on = False
        except KeyError:
            self.engine_on = self.total_burn < self.burn_time

# Notice how each entry has a key in quotes, then a Rocket value
rockets = {
    "saturnv": Rocket("Saturn V",2970000,165,41000000),
    "falcon9": Rocket("Falcon 9",549000,160,7570000),
    "atlas": Rocket("Atlas",120000,300,1300000)
}
