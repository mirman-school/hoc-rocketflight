# Hour of Code: Let's Fly a Rocket!
You might have seen the recent successes of [SpaceX](https://www.youtube.com/watch?v=RPGUQySBikQ) and [Blue Origin](https://www.youtube.com/watch?v=9pillaOxGCo)—private aerospace companies who are looking to reduce the cost of sending objects into space.

This is a massive problem that we need to solve if we ever want to go to Mars or elsewhere in the solar system. At the moment, it costs NASA about $10,000 per pound to launch payloads into LEO (Low Earth Orbit). If we can reduce that cost, say, tenfold, our ability to construct large spacecraft and orbital facilities is proportionately increased.

Let's see if we can program a rocket to launch and land gently. To do this, we'll be using the Python programming language. We will graph the altitude and velocity of our simulated flight, while changing the parameters of our rocket and its flight plan.

## What's in the box
After downloading this folder, you'll find the following files:

* `README.md`: The file you're reading RIGHT NOW!
* `rockets.py`: The file that describes `Rocket` objects and has three starter rockets in there for you.
* `flight.py`: The definitions for our simulation, and also where you program your flight plan.
* `visualizer.py`: A helper file that does the graphing of our flights.

## How to read these files
### `rockets.py`
This program is build using object-oriented programming (OOP). In OOP, we consider our information just as we do in the real world: broken up into separate _things_. If we can classify similar enough things, we make a _class_. Check out line 1:

    class Rocket:

But a class is just an idea of a thing, not an actual thing. Actual things, or _instances_, are constructed from the class. In Python, that's done using the `__init()__` function. We pass the constructor function certain paramters, and it returns to us an object of the given class. Let's look out our `__init__()` definition:

    def __init__(self,name,mass,burn_time,thrust):

`self` is always going to be there; it's the new object we're creating. So we give the constructor a name, a mass, a burn time, and thrust. With those, it goes and attaches those values (and a few others) to the object and returns it.

You'll see two other functions inside of the `Rocket` class. One of them is just a fun way to print out our rockets; the other we'll use in our flight simulation.

### `flight.py`
This is where the action is. You'll notice that we start by `import`ing information from the other files. Then we have another `Class` definition: `Vector`. This is just a helper to usefully contain the `x` and `y` values for the position and velocity of our rocket during flight. The `Tick` class represents a moment in time. Our simulation will be made of a collection of `Tick`s. How many? You'll decide that later.

Then two functions: `tick()` and `fly()`. `tick()` advances the simulation by one unit of time (in our case, a second), while `fly()` runs a flight simulation for a given rocket with a given flight plan for a specific amount of time.

Below that is where we'll do our programming.

## Your Objective
**Get a rocket aloft, and land it gently back on the surface.**

In other words, your rocket should have a final velocity of **< 10 m/s**. It's tricky, but then again, this is literally rocket science.

To do this, we will have to to the following:

1. Choose a rocket (or design one)
2. Choose a mission time
3. Program the flight plan

### 1. Choose a rocket (or design one)
Remember the `rockets` variable from `rockets.py`? This was your preset menu of rockets. Each entry had a key, a colon, then a `Rocket()` value. Notice how I access the Saturn V rocket by entering `rockets["saturnv"]`. That key inside the `[]` corresponds to the key in quotes on the left side of the `:` in `rockets`. Changing it to `rockets["atlas"]` would mean I fly the Atlas, with its mass, burn time, and thrust.

#### Can I make my own rocket?
Yes! You can do this in one of two ways: either in the `rockets` list or right there in `flight.py` when you assign `rocket` to a certain rocket value.

To add a rocket to the menu, you'd create a new `Rocket()` object and attach it to a key, like so:

    rockets = {
        "saturnv": Rocket("Saturn V",2970000,165,41000000),
        "falcon9": Rocket("Falcon 9",549000,160,7570000),
        "atlas": Rocket("Atlas",120000,300,1300000),
        "new": Rocket("New Rocket", 1350000, 150, 5000000)
    }

Remember your units: mass is in `kg`, burn time is in `s`, and thrust is in `N`.

Then in `flight.py`, you would type:

    rocket = rockets["new"]

You could also define the rocket without naming it, like so:

    rocket = Rocket("New Rocket", 1350000, 150, 5000000)

### 2. Choose a mission time
1000 ticks is the default, and that should be fine. Feel free to change it if you want and see how it affects the simulation.

### 3. Program the flight plan
Our rockets can turn their engines on and off. To do this, we tell the rocket at what `tick` of mission time we want to turn the engines on/off. So a flight plan that says:

    flight_plan = {
      1: "on",
      50: "off",
      100: "on",
      110: "off"
    }

Would start the engines burning at `tick` 1 (the start of the simulation). Then at `tick` 50, the engines turn off, letting gravity take over. We power back up at `tick` 100, until 110, when we power off for the last time.

Changing these values, along with different rockets, will alter your flight profile. See if you can make soft landings from multiple altitudes with multiple rockets.

## Running your code
To run the Python code, you will use Terminal. Open it up, and use the `cd` command to navigate to this folder. Terminal opens one level above your `Downloads/` folder, so if you downloaded/unzipped this folder in your Downloads, enter:

    cd Downloads/hoc-rocketflight-master

If it's on your Desktop, same thing, but `Desktop` in lieu of `Downloads`.

From there, to run and re-run your code, enter:

    python3 flight.py

**Make sure Python and Pylab are installed before running code!**
