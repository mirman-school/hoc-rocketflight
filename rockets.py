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

    def __str__(self):
        return "{}:\n\tMass: {} kg\n\tBurn Time: {} s\n\tThrust: {} N".format(
            self.name,
            self.mass,
            self.burn_time,
            self.thrust
        )

rockets = {
    "saturnv": Rocket("Saturn V",2970000,165,41000),
    "falcon9": Rocket("Falcon 9",549000,160,7570),
    "atlas": Rocket("Atlas",120000,300,1300)
}
