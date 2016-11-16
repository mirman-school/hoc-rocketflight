class Rocket:

    def __init__(self,name,mass,max_fuel,thrust):
        '''
        Mass: kg
        Max Fuel: kg
        Thrust kN
        '''
        self.name = name
        self.mass = mass
        self.max_fuel = max_fuel
        self.thrust = thrust

    def __str__(self):
        return "{}:\n\tMass: {} kg\n\tMax Fuel: {} kg\n\tThrust: {} N".format(
            self.name,
            self.mass,
            self.max_fuel,
            self.thrust
        )

rockets = {
    "saturnv": Rocket("Saturn V",2970000,2950000,41000),
    "falcon9": Rocket("Falcon 9",549000,7607000,7570),
    "atlas": Rocket("Atlas",120000,107000,1300)
}
