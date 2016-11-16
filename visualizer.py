from matplotlib import pyplot as plt

def visualize(flight):
    plt.figure()
    altitude = [t.position.y for t in flight]
    velocity = [t.velocity.y for t in flight]
    time = list(range(len(flight)))
    plt.figure()
    plt.title("Flight Log")
    plt.subplot(211)
    plt.xlabel("Time (secs)")
    plt.ylabel("Altitude(m)")
    plt.plot(time, altitude)
    plt.subplot(212)
    plt.xlabel("Time (secs)")
    plt.ylabel("Velocity(m/s)")
    plt.plot(time,velocity)
    plt.show()
